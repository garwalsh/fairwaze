#!/usr/bin/env python3
"""
FairWaze Evaluation Harness

A comprehensive evaluation harness for testing AI models via the Anthropic API.
Sends multiple sequential prompts and records results with detailed metrics.
"""

import asyncio
import json
import csv
import time
import logging
import argparse
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
import os

import anthropic
from anthropic import Anthropic


def load_env_file(env_path=".env"):
    """Simple .env file loader"""
    if not os.path.exists(env_path):
        return

    with open(env_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()


@dataclass
class EvalResult:
    """Structure for storing evaluation results"""
    prompt_id: str
    prompt_text: str
    response: str
    model: str
    timestamp: str
    response_time_ms: float
    input_tokens: int
    output_tokens: int
    total_tokens: int
    success: bool
    error_message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class EvalPrompt:
    """Structure for evaluation prompts"""
    id: str
    prompt: str
    expected_response: Optional[str] = None
    category: Optional[str] = None
    difficulty: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class EvalHarness:
    """Main evaluation harness class"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude-3-5-sonnet-20241022",
        output_dir: str = "eval_results",
        rate_limit_delay: float = 1.0
    ):
        """
        Initialize the evaluation harness

        Args:
            api_key: Anthropic API key (if None, will use ANTHROPIC_API_KEY env var)
            model: Model to use for evaluation
            output_dir: Directory to save results
            rate_limit_delay: Delay between API calls in seconds
        """
        # Load environment variables from .env file
        load_env_file()

        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided or set in ANTHROPIC_API_KEY environment variable")

        self.client = Anthropic(api_key=self.api_key)
        self.model = model
        self.output_dir = Path(output_dir)
        self.rate_limit_delay = rate_limit_delay
        self.results: List[EvalResult] = []

        # Create output directory
        self.output_dir.mkdir(exist_ok=True)

        # Setup logging
        self._setup_logging()

    def _setup_logging(self):
        """Setup logging configuration"""
        log_file = self.output_dir / "eval_harness.log"
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def load_prompts_from_json(self, file_path: str) -> List[EvalPrompt]:
        """Load evaluation prompts from a JSON file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        prompts = []
        for item in data:
            prompt = EvalPrompt(
                id=item['id'],
                prompt=item['prompt'],
                expected_response=item.get('expected_response'),
                category=item.get('category'),
                difficulty=item.get('difficulty'),
                metadata=item.get('metadata')
            )
            prompts.append(prompt)

        return prompts

    def load_prompts_from_csv(self, file_path: str) -> List[EvalPrompt]:
        """Load evaluation prompts from a CSV file"""
        prompts = []
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                prompt = EvalPrompt(
                    id=row['id'],
                    prompt=row['prompt'],
                    expected_response=row.get('expected_response'),
                    category=row.get('category'),
                    difficulty=row.get('difficulty'),
                    metadata=json.loads(row.get('metadata', '{}'))
                )
                prompts.append(prompt)

        return prompts

    async def send_prompt(self, prompt: EvalPrompt) -> EvalResult:
        """Send a single prompt to the API and record the result"""
        start_time = time.time()
        timestamp = datetime.now().isoformat()

        try:
            self.logger.info(f"Sending prompt {prompt.id}: {prompt.prompt[:50]}...")

            response = self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                messages=[
                    {"role": "user", "content": prompt.prompt}
                ]
            )

            end_time = time.time()
            response_time_ms = (end_time - start_time) * 1000

            # Extract response text
            response_text = ""
            for content_block in response.content:
                if hasattr(content_block, 'text'):
                    response_text += content_block.text

            # Create result
            result = EvalResult(
                prompt_id=prompt.id,
                prompt_text=prompt.prompt,
                response=response_text,
                model=self.model,
                timestamp=timestamp,
                response_time_ms=response_time_ms,
                input_tokens=response.usage.input_tokens,
                output_tokens=response.usage.output_tokens,
                total_tokens=response.usage.input_tokens + response.usage.output_tokens,
                success=True,
                metadata={
                    'category': prompt.category,
                    'difficulty': prompt.difficulty,
                    'expected_response': prompt.expected_response,
                    'prompt_metadata': prompt.metadata
                }
            )

            self.logger.info(f"✓ Prompt {prompt.id} completed in {response_time_ms:.2f}ms")
            return result

        except Exception as e:
            end_time = time.time()
            response_time_ms = (end_time - start_time) * 1000

            self.logger.error(f"✗ Prompt {prompt.id} failed: {str(e)}")

            result = EvalResult(
                prompt_id=prompt.id,
                prompt_text=prompt.prompt,
                response="",
                model=self.model,
                timestamp=timestamp,
                response_time_ms=response_time_ms,
                input_tokens=0,
                output_tokens=0,
                total_tokens=0,
                success=False,
                error_message=str(e),
                metadata={
                    'category': prompt.category,
                    'difficulty': prompt.difficulty,
                    'expected_response': prompt.expected_response,
                    'prompt_metadata': prompt.metadata
                }
            )

            return result

    async def run_evaluation(self, prompts: List[EvalPrompt]) -> List[EvalResult]:
        """Run evaluation on a list of prompts"""
        self.logger.info(f"Starting evaluation with {len(prompts)} prompts")
        self.results = []

        for i, prompt in enumerate(prompts, 1):
            self.logger.info(f"Processing prompt {i}/{len(prompts)}")

            result = await self.send_prompt(prompt)
            self.results.append(result)

            # Rate limiting
            if i < len(prompts):  # Don't delay after the last prompt
                await asyncio.sleep(self.rate_limit_delay)

        self.logger.info("Evaluation completed")
        return self.results

    def save_results(self, results: List[EvalResult], format: str = "json"):
        """Save results to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        if format.lower() == "json":
            filename = self.output_dir / f"eval_results_{timestamp}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump([asdict(result) for result in results], f, indent=2, ensure_ascii=False)

        elif format.lower() == "csv":
            filename = self.output_dir / f"eval_results_{timestamp}.csv"
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                if results:
                    writer = csv.DictWriter(f, fieldnames=asdict(results[0]).keys())
                    writer.writeheader()
                    for result in results:
                        row = asdict(result)
                        # Convert complex fields to JSON strings for CSV
                        if row['metadata']:
                            row['metadata'] = json.dumps(row['metadata'])
                        writer.writerow(row)

        self.logger.info(f"Results saved to {filename}")
        return filename

    def generate_summary(self, results: List[EvalResult]) -> Dict[str, Any]:
        """Generate summary statistics from results"""
        total_prompts = len(results)
        successful = sum(1 for r in results if r.success)
        failed = total_prompts - successful

        if successful > 0:
            avg_response_time = sum(r.response_time_ms for r in results if r.success) / successful
            total_input_tokens = sum(r.input_tokens for r in results if r.success)
            total_output_tokens = sum(r.output_tokens for r in results if r.success)
            total_tokens = sum(r.total_tokens for r in results if r.success)
        else:
            avg_response_time = 0
            total_input_tokens = 0
            total_output_tokens = 0
            total_tokens = 0

        # Category breakdown
        categories = {}
        for result in results:
            category = result.metadata.get('category', 'Unknown') if result.metadata else 'Unknown'
            if category not in categories:
                categories[category] = {'total': 0, 'successful': 0, 'failed': 0}
            categories[category]['total'] += 1
            if result.success:
                categories[category]['successful'] += 1
            else:
                categories[category]['failed'] += 1

        summary = {
            'total_prompts': total_prompts,
            'successful': successful,
            'failed': failed,
            'success_rate': successful / total_prompts if total_prompts > 0 else 0,
            'avg_response_time_ms': avg_response_time,
            'total_input_tokens': total_input_tokens,
            'total_output_tokens': total_output_tokens,
            'total_tokens': total_tokens,
            'model': self.model,
            'categories': categories,
            'timestamp': datetime.now().isoformat()
        }

        return summary

    def save_summary(self, results: List[EvalResult]):
        """Save evaluation summary"""
        summary = self.generate_summary(results)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.output_dir / f"eval_summary_{timestamp}.json"

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        self.logger.info(f"Summary saved to {filename}")

        # Also log summary to console
        self.logger.info("=== EVALUATION SUMMARY ===")
        self.logger.info(f"Total prompts: {summary['total_prompts']}")
        self.logger.info(f"Successful: {summary['successful']}")
        self.logger.info(f"Failed: {summary['failed']}")
        self.logger.info(f"Success rate: {summary['success_rate']:.2%}")
        self.logger.info(f"Average response time: {summary['avg_response_time_ms']:.2f}ms")
        self.logger.info(f"Total tokens used: {summary['total_tokens']}")

        return filename


async def main():
    """Main function for CLI usage"""
    parser = argparse.ArgumentParser(description="FairWaze Evaluation Harness")
    parser.add_argument("--prompts", required=True, help="Path to prompts file (JSON or CSV)")
    parser.add_argument("--model", default="claude-3-5-sonnet-20241022", help="Model to use")
    parser.add_argument("--output-dir", default="eval_results", help="Output directory")
    parser.add_argument("--rate-limit", type=float, default=1.0, help="Delay between requests (seconds)")
    parser.add_argument("--format", choices=["json", "csv"], default="json", help="Output format")
    parser.add_argument("--api-key", help="Anthropic API key (or set ANTHROPIC_API_KEY env var)")

    args = parser.parse_args()

    # Initialize harness
    harness = EvalHarness(
        api_key=args.api_key,
        model=args.model,
        output_dir=args.output_dir,
        rate_limit_delay=args.rate_limit
    )

    # Load prompts
    prompts_file = Path(args.prompts)
    if prompts_file.suffix.lower() == '.json':
        prompts = harness.load_prompts_from_json(args.prompts)
    elif prompts_file.suffix.lower() == '.csv':
        prompts = harness.load_prompts_from_csv(args.prompts)
    else:
        raise ValueError("Prompts file must be JSON or CSV format")

    # Run evaluation
    results = await harness.run_evaluation(prompts)

    # Save results
    harness.save_results(results, format=args.format)
    harness.save_summary(results)

    print(f"Evaluation completed! Results saved to {args.output_dir}")


if __name__ == "__main__":
    asyncio.run(main())