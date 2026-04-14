#!/usr/bin/env python3
"""
Golf Rules Evaluation Test Runner

Sends golf rules questions sequentially to the Anthropic API with the system prompt
and saves results to a versioned folder.
"""

import asyncio
import json
import os
import time
import logging
import subprocess
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
import argparse
import shutil

import anthropic


def parse_frontmatter(content: str) -> Tuple[Dict[str, str], str]:
    """Parse YAML frontmatter from content"""
    frontmatter_data = {}

    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter_lines = parts[1].strip().split('\n')
            for line in frontmatter_lines:
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter_data[key.strip()] = value.strip().strip('>')
            content = parts[2].strip()

    return frontmatter_data, content


def get_git_commit_hash() -> str:
    """Get current git commit hash"""
    try:
        result = subprocess.run(['git', 'rev-parse', 'HEAD'],
                              capture_output=True, text=True, cwd='..')
        return result.stdout.strip()[:7]  # Short hash
    except:
        return "unknown"


def load_env_file(env_path=".env"):
    """Simple .env file loader"""
    # Try multiple possible locations for .env file
    possible_paths = [
        env_path,
        f"../{env_path}",
        f"../../{env_path}"
    ]

    for path in possible_paths:
        if os.path.exists(path):
            with open(path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        os.environ[key.strip()] = value.strip()
            return

    # If no .env file found, that's okay - will use environment variables


class GolfRulesEvaluator:
    """Golf Rules Evaluation Test Runner"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude-3-haiku-20240307",
        rate_limit_delay: float = 1.0,
        system_prompt_file: str = "golf_rules_system_prompt_v0.1.md"
    ):
        """Initialize the evaluator"""
        # Load environment variables
        load_env_file()

        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided or set in ANTHROPIC_API_KEY environment variable")

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = model
        self.rate_limit_delay = rate_limit_delay

        # Load system prompt
        self.system_prompt, self.system_prompt_full, self.system_prompt_path = self._load_system_prompt(system_prompt_file)

        # Parse system prompt version
        frontmatter, _ = parse_frontmatter(self.system_prompt_full)
        self.system_prompt_version = frontmatter.get('version', 'v0.1')

        # Load and parse rubric version
        self.rubric_version = self._load_rubric_version()

        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[logging.StreamHandler()]
        )
        self.logger = logging.getLogger(__name__)

    def _load_system_prompt(self, system_prompt_file: str) -> Tuple[str, str, str]:
        """Load system prompt from file and return (prompt_content, full_content, file_path)"""
        # Try different possible locations
        possible_paths = [
            system_prompt_file,
            f"../{system_prompt_file}",
            f"../../{system_prompt_file}",
            "../prompts/golf_rules_system_prompt_v0.1.md",  # Default fallback
            "../golf_rules_system_prompt_v0.1.md"  # Legacy fallback
        ]

        for path in possible_paths:
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    full_content = f.read()
                    frontmatter, content = parse_frontmatter(full_content)

                    # Extract just the prompt content, skip markdown headers
                    lines = content.split('\n')
                    # Skip lines that start with # (headers) but keep the content
                    prompt_lines = [line for line in lines if not line.strip().startswith('#')]
                    prompt_content = '\n'.join(prompt_lines).strip()

                    return prompt_content, full_content, path

        raise FileNotFoundError(f"System prompt file not found. Tried: {possible_paths}")

    def _load_rubric_version(self) -> str:
        """Extract rubric version from RUBRIC.md frontmatter"""
        rubric_paths = [
            "RUBRIC.md",
            "../RUBRIC.md",
            "../../RUBRIC.md"
        ]

        for path in rubric_paths:
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    frontmatter, _ = parse_frontmatter(content)
                    return frontmatter.get('version', 'v1')

        self.logger.warning("RUBRIC.md not found, using default version v1")
        return 'v1'

    def load_test_cases(self, test_cases_file: str) -> List[Dict[str, Any]]:
        """Load test cases from JSON file"""
        with open(test_cases_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    async def evaluate_single_question(self, test_case: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate a single golf rules question"""
        start_time = time.time()
        timestamp = datetime.now().isoformat()

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                system=self.system_prompt,
                messages=[
                    {"role": "user", "content": test_case['question']}
                ]
            )

            end_time = time.time()
            response_time_ms = (end_time - start_time) * 1000

            # Extract response text
            response_text = ""
            for content_block in response.content:
                if hasattr(content_block, 'text'):
                    response_text += content_block.text

            # Create result with response field
            result = test_case.copy()
            result.update({
                'response': response_text,
                'model': self.model,
                'timestamp': timestamp,
                'response_time_ms': response_time_ms,
                'input_tokens': response.usage.input_tokens,
                'output_tokens': response.usage.output_tokens,
                'total_tokens': response.usage.input_tokens + response.usage.output_tokens,
                'success': True,
                'error_message': None
            })

            return result

        except Exception as e:
            end_time = time.time()
            response_time_ms = (end_time - start_time) * 1000

            self.logger.error(f"✗ {test_case['id']} failed: {str(e)}")

            result = test_case.copy()
            result.update({
                'response': "",
                'model': self.model,
                'timestamp': timestamp,
                'response_time_ms': response_time_ms,
                'input_tokens': 0,
                'output_tokens': 0,
                'total_tokens': 0,
                'success': False,
                'error_message': str(e)
            })

            return result

    async def run_evaluation(self, test_cases: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Run evaluation on all test cases"""
        self.logger.info(f"Starting evaluation: {len(test_cases)} questions, model: {self.model}")

        results = []

        for i, test_case in enumerate(test_cases, 1):
            print(f"\rProcessing {i}/{len(test_cases)}", end="", flush=True)

            result = await self.evaluate_single_question(test_case)
            results.append(result)

            # Rate limiting
            if i < len(test_cases):  # Don't delay after the last question
                await asyncio.sleep(self.rate_limit_delay)

        print()  # New line after progress
        successful = sum(1 for r in results if r['success'])
        self.logger.info(f"Completed: {successful}/{len(results)} successful")

        return results

    def save_results(self, results: List[Dict[str, Any]], test_cases: List[Dict[str, Any]]):
        """Save results to versioned folder with new naming convention"""
        # Create timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Create output directory with new naming convention
        output_dir = Path(f"{self.system_prompt_version}_r{self.rubric_version}_{timestamp}")
        output_dir.mkdir(parents=True, exist_ok=True)

        # 1. responses.json - Raw model outputs
        responses_file = output_dir / "responses.json"
        with open(responses_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        # 2. system_prompt.md - Copy of system prompt
        system_prompt_file = output_dir / "system_prompt.md"
        with open(system_prompt_file, 'w', encoding='utf-8') as f:
            f.write(self.system_prompt_full)

        # 3. rubric.md - Copy of rubric
        rubric_file = output_dir / "rubric.md"
        try:
            with open("RUBRIC.md", 'r', encoding='utf-8') as f:
                rubric_content = f.read()
            with open(rubric_file, 'w', encoding='utf-8') as f:
                f.write(rubric_content)
        except FileNotFoundError:
            self.logger.warning("RUBRIC.md not found in current directory")

        # 4. test_cases.json - Copy of test cases
        test_cases_file = output_dir / "test_cases.json"
        with open(test_cases_file, 'w', encoding='utf-8') as f:
            json.dump(test_cases, f, indent=2, ensure_ascii=False)

        # 5. manifest.json - Initial manifest (will be updated by grader)
        manifest = {
            "version": self.system_prompt_version,
            "timestamp": datetime.now().isoformat(),
            "commit_hash": get_git_commit_hash(),
            "model": self.model,
            "grader_model": None,  # Will be set by grader
            "temperature": 0,  # Assuming 0 for now
            "grader_temperature": None,  # Will be set by grader
            "n_cases": len(results),
            "changes_from_previous": "Baseline run",  # TODO: Extract from frontmatter
            "aggregate_score": None,  # Will be set by grader
            "aggregate_max": None,  # Will be set by grader
            "breakdowns": None,  # Will be set by grader
            "rubric_version": self.rubric_version,
            "successful_responses": sum(1 for r in results if r['success']),
            "rate_limit_delay": self.rate_limit_delay
        }

        manifest_file = output_dir / "manifest.json"
        with open(manifest_file, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

        self.logger.info(f"Results saved to: {output_dir}")

        return output_dir


async def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Golf Rules Evaluation Test Runner")
    parser.add_argument("--test-cases",
                       default="golf_rules_test_cases.json",
                       help="Path to test cases JSON file")
    parser.add_argument("--model",
                       default="claude-3-haiku-20240307",
                       help="Model to use for evaluation")
    # Removed --version argument since it's now extracted from system prompt
    # Removed --rubric-version argument since it's now extracted from RUBRIC.md
    parser.add_argument("--rate-limit",
                       type=float, default=1.0,
                       help="Delay between requests (seconds)")
    parser.add_argument("--system-prompt",
                       default="../prompts/golf_rules_system_prompt_v0.1.md",
                       help="Path to system prompt file")

    args = parser.parse_args()

    try:
        # Initialize evaluator
        evaluator = GolfRulesEvaluator(
            model=args.model,
            rate_limit_delay=args.rate_limit,
            system_prompt_file=args.system_prompt
        )

        # Load test cases
        test_cases = evaluator.load_test_cases(args.test_cases)

        # Run evaluation
        results = await evaluator.run_evaluation(test_cases)

        # Save results
        output_dir = evaluator.save_results(results, test_cases)

        print(f"\n🎯 Evaluation completed successfully!")
        print(f"📁 Results saved to: {output_dir}")
        print(f"📊 Success rate: {sum(1 for r in results if r['success'])}/{len(results)}")
        print(f"\nNext step: Run grader script on the results")

    except Exception as e:
        print(f"❌ Evaluation failed: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(asyncio.run(main()))