#!/usr/bin/env python3
"""
Golf Rules Evaluation Grader

Grades golf rules bot responses using Claude API according to the evaluation rubric.
"""

import asyncio
import json
import os
import time
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
import argparse
from collections import defaultdict

import anthropic


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


class GolfRulesGrader:
    """Golf Rules Evaluation Grader"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude-3-5-sonnet-20241022",
        rate_limit_delay: float = 1.0
    ):
        """Initialize the grader"""
        # Load environment variables
        load_env_file()

        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided or set in ANTHROPIC_API_KEY environment variable")

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = model
        self.rate_limit_delay = rate_limit_delay

        # Load rubric
        self.rubric = self._load_rubric()

        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[logging.StreamHandler()]
        )
        self.logger = logging.getLogger(__name__)

    def _load_rubric(self) -> str:
        """Load rubric from file"""
        # Try different possible locations for RUBRIC.md
        possible_paths = [
            "RUBRIC.md",
            "../RUBRIC.md",
            "../../RUBRIC.md"
        ]

        for path in possible_paths:
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Handle frontmatter
                    if content.startswith('---'):
                        # Split by frontmatter delimiter
                        parts = content.split('---', 2)
                        if len(parts) >= 3:
                            content = parts[2].strip()  # Take content after frontmatter
                    return content

        raise FileNotFoundError(f"RUBRIC.md not found. Tried: {possible_paths}")

    def load_responses_and_ground_truth(self, eval_dir: str):
        """Load responses and ground truth from eval directory"""
        eval_path = Path(eval_dir)

        # Load responses from eval directory
        responses_file = eval_path / "responses.json"
        with open(responses_file, 'r', encoding='utf-8') as f:
            responses = json.load(f)

        # Load ground truth from current directory or eval directory
        ground_truth_files = [
            "golf_rules_test_cases_with_answers.json",  # Current directory
            eval_path / "golf_rules_test_cases_with_answers.json"  # Eval directory
        ]

        ground_truth = None
        for gt_file in ground_truth_files:
            if os.path.exists(gt_file):
                with open(gt_file, 'r', encoding='utf-8') as f:
                    ground_truth = json.load(f)
                break

        if ground_truth is None:
            raise FileNotFoundError("Ground truth file not found")

        # Create lookup for ground truth by ID
        gt_lookup = {item['id']: item for item in ground_truth}

        return responses, gt_lookup

    async def grade_single_response(self, response_data: Dict[str, Any], ground_truth: Dict[str, Any], output_file: Path) -> Dict[str, Any]:
        """Grade a single response"""

        grading_prompt = f"""You are grading a golf rules bot response according to the evaluation rubric below.

EVALUATION RUBRIC:
{self.rubric}

IMPORTANT GRADING INSTRUCTIONS:
- Grade semantically, not literally - tone/format/warmth differences should NOT be penalized
- Focus on rule accuracy, completeness of information, format adherence, and guardrail compliance
- Temperature is set to 0 for deterministic grading

QUESTION:
{response_data['question']}

GROUND TRUTH ANSWER:
{ground_truth.get('ground_truth', 'No ground truth available')}

MODEL RESPONSE TO GRADE:
{response_data.get('response', 'No response provided')}

Please grade this response and return ONLY a JSON object with the following structure:
{{
    "accuracy": <0-2>,
    "completeness": <0-2>,
    "format": <0-2>,
    "guardrails": <0-2>,
    "total": <calculated total>,
    "fail_conditions_triggered": [<list of any fail conditions>],
    "reasoning": "Detailed explanation of scores with specific examples"
}}

Remember: Accuracy is weighted x2 in the total score calculation.
"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2048,
                temperature=0.0,  # Deterministic grading
                messages=[
                    {"role": "user", "content": grading_prompt}
                ]
            )

            # Extract response text
            response_text = ""
            for content_block in response.content:
                if hasattr(content_block, 'text'):
                    response_text += content_block.text

            # Parse JSON response
            try:
                grade_data = json.loads(response_text)
            except json.JSONDecodeError:
                # Try to extract JSON from response if it's wrapped in other text
                import re
                json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
                if json_match:
                    grade_data = json.loads(json_match.group(0))
                else:
                    raise ValueError("Could not parse JSON from response")

            # Validate and calculate total
            accuracy = grade_data.get('accuracy', 0)
            completeness = grade_data.get('completeness', 0)
            format_score = grade_data.get('format', 0)
            guardrails = grade_data.get('guardrails', 0)

            # Calculate total with accuracy weighted x2
            total = (accuracy * 2) + completeness + format_score + guardrails

            # Apply fail conditions
            fail_conditions = grade_data.get('fail_conditions_triggered', [])
            if fail_conditions:
                if 'hallucinated_rule' in fail_conditions:
                    total = min(total, 3)
                if 'safety_violation' in fail_conditions or 'format_ignored' in fail_conditions:
                    total = min(total, 4)

            grade_result = {
                'id': response_data['id'],
                'question': response_data['question'],
                'difficulty': response_data['difficulty'],
                'category': response_data['category'],
                'accuracy': accuracy,
                'completeness': completeness,
                'format': format_score,
                'guardrails': guardrails,
                'total': total,
                'fail_conditions_triggered': fail_conditions,
                'reasoning': grade_data.get('reasoning', ''),
                'timestamp': datetime.now().isoformat()
            }

            # Write individual result immediately
            self._append_grade_to_file(grade_result, output_file)

            return grade_result

        except Exception as e:
            self.logger.error(f"✗ Grading error for {response_data['id']}: {str(e)}")

            error_result = {
                'id': response_data['id'],
                'question': response_data['question'],
                'difficulty': response_data['difficulty'],
                'category': response_data['category'],
                'accuracy': 0,
                'completeness': 0,
                'format': 0,
                'guardrails': 0,
                'total': 0,
                'fail_conditions_triggered': ['grading_error'],
                'reasoning': f"Grading failed: {str(e)}",
                'timestamp': datetime.now().isoformat()
            }

            self._append_grade_to_file(error_result, output_file)
            return error_result

    def _append_grade_to_file(self, grade_result: Dict[str, Any], output_file: Path):
        """Append individual grade result to file immediately"""
        # Create file if it doesn't exist
        if not output_file.exists():
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump([], f)

        # Read existing data
        try:
            with open(output_file, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            existing_data = []

        # Append new result
        existing_data.append(grade_result)

        # Write back to file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, indent=2, ensure_ascii=False)

    def generate_summary_report(self, grades: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate aggregate summary report"""
        total_questions = len(grades)

        # Overall stats
        total_scores = [g['total'] for g in grades]
        avg_total = sum(total_scores) / total_questions if total_questions > 0 else 0

        # Dimension averages
        dimensions = ['accuracy', 'completeness', 'format', 'guardrails']
        dimension_averages = {}
        for dim in dimensions:
            scores = [g[dim] for g in grades]
            dimension_averages[dim] = sum(scores) / total_questions if total_questions > 0 else 0

        # Breakdown by difficulty
        difficulty_breakdown = defaultdict(lambda: {'count': 0, 'total_scores': [], 'avg': 0})
        for grade in grades:
            diff = grade['difficulty']
            difficulty_breakdown[diff]['count'] += 1
            difficulty_breakdown[diff]['total_scores'].append(grade['total'])

        for diff_data in difficulty_breakdown.values():
            if diff_data['total_scores']:
                diff_data['avg'] = sum(diff_data['total_scores']) / len(diff_data['total_scores'])

        # Breakdown by category
        category_breakdown = defaultdict(lambda: {'count': 0, 'total_scores': [], 'avg': 0})
        for grade in grades:
            cat = grade['category']
            category_breakdown[cat]['count'] += 1
            category_breakdown[cat]['total_scores'].append(grade['total'])

        for cat_data in category_breakdown.values():
            if cat_data['total_scores']:
                cat_data['avg'] = sum(cat_data['total_scores']) / len(cat_data['total_scores'])

        # Fail conditions
        fail_conditions = defaultdict(int)
        for grade in grades:
            for fail_condition in grade.get('fail_conditions_triggered', []):
                fail_conditions[fail_condition] += 1

        # Score distribution
        score_distribution = defaultdict(int)
        for score in total_scores:
            score_distribution[score] += 1

        summary = {
            'total_questions': total_questions,
            'overall_average': avg_total,
            'max_possible_score': 10,
            'dimension_averages': dimension_averages,
            'difficulty_breakdown': dict(difficulty_breakdown),
            'category_breakdown': dict(category_breakdown),
            'fail_conditions': dict(fail_conditions),
            'score_distribution': dict(score_distribution),
            'timestamp': datetime.now().isoformat()
        }

        return summary

    async def run_grading(self, eval_dir: str):
        """Run grading on all responses"""
        # Load data
        responses, gt_lookup = self.load_responses_and_ground_truth(eval_dir)

        # Setup output files
        output_path = Path(eval_dir)
        grades_file = output_path / "grades.json"
        summary_file = output_path / "summary.json"
        manifest_file = output_path / "manifest.json"

        # Load existing manifest
        with open(manifest_file, 'r', encoding='utf-8') as f:
            manifest = json.load(f)

        # Clear existing grades file
        if grades_file.exists():
            grades_file.unlink()

        self.logger.info(f"Starting grading: {len(responses)} responses, model: {self.model}")

        # Grade each response
        grades = []
        for i, response_data in enumerate(responses, 1):
            print(f"\rGrading {i}/{len(responses)}", end="", flush=True)

            # Get ground truth for this response
            ground_truth = gt_lookup.get(response_data['id'], {})

            # Grade the response
            grade = await self.grade_single_response(response_data, ground_truth, grades_file)
            grades.append(grade)

            # Rate limiting
            if i < len(responses):
                await asyncio.sleep(self.rate_limit_delay)

        print()  # New line after progress
        # Generate summary report
        summary = self.generate_summary_report(grades)

        # Save summary
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        # Update manifest with grading results
        manifest.update({
            "grader_model": self.model,
            "grader_temperature": 0.0,
            "aggregate_score": summary['overall_average'],
            "aggregate_max": 10,
            "breakdowns": {
                "by_difficulty": {diff: data['avg'] for diff, data in summary['difficulty_breakdown'].items()},
                "by_category": {cat: data['avg'] for cat, data in summary['category_breakdown'].items()},
                "fail_conditions_triggered": summary['fail_conditions']
            }
        })

        # Save updated manifest
        with open(manifest_file, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

        self.logger.info(f"Grading completed! Overall average: {summary['overall_average']:.2f}/10")

        return grades, summary


async def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Golf Rules Evaluation Grader")
    parser.add_argument("--eval-dir",
                       required=True,
                       help="Directory containing evaluation results to grade")
    # Removed --ground-truth argument since it's now auto-detected
    parser.add_argument("--model",
                       default="claude-3-5-sonnet-20241022",
                       help="Model to use for grading")
    parser.add_argument("--rate-limit",
                       type=float, default=0.5,
                       help="Delay between grading requests (seconds)")

    args = parser.parse_args()

    try:
        # Validate eval directory
        eval_path = Path(args.eval_dir)
        if not eval_path.exists():
            raise FileNotFoundError(f"Evaluation directory not found: {eval_path}")

        responses_file = eval_path / "responses.json"
        if not responses_file.exists():
            raise FileNotFoundError(f"Responses file not found: {responses_file}")

        # Initialize grader
        grader = GolfRulesGrader(
            model=args.model,
            rate_limit_delay=args.rate_limit
        )

        # Run grading
        grades, summary = await grader.run_grading(args.eval_dir)

        print(f"\n🎯 Grading completed successfully!")
        print(f"📊 Overall average: {summary['overall_average']:.2f}/10")
        print(f"📁 Results saved to: {eval_path}")

        # Print difficulty breakdown
        print(f"\n📈 Breakdown by difficulty:")
        for difficulty, data in summary['difficulty_breakdown'].items():
            print(f"  {difficulty}: {data['avg']:.2f}/10 ({data['count']} questions)")

        # Print fail conditions if any
        if summary['fail_conditions']:
            print(f"\n⚠️  Fail conditions triggered:")
            for condition, count in summary['fail_conditions'].items():
                print(f"  {condition}: {count} times")

    except Exception as e:
        print(f"❌ Grading failed: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(asyncio.run(main()))