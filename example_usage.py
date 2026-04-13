#!/usr/bin/env python3
"""
Example usage of the FairWaze Evaluation Harness
"""

import asyncio
import os
from eval_harness import EvalHarness, EvalPrompt

async def run_simple_evaluation():
    """Simple evaluation example"""
    print("=== Simple Evaluation Example ===")

    # Initialize harness with environment variables or default settings
    harness = EvalHarness(
        model="claude-3-5-sonnet-20241022",
        output_dir="example_results",
        rate_limit_delay=0.5  # Faster for demo purposes
    )

    # Create a few test prompts
    prompts = [
        EvalPrompt(
            id="math_001",
            prompt="What is 15 * 7?",
            expected_response="105",
            category="mathematics",
            difficulty="easy",
            metadata={"operation": "multiplication"}
        ),
        EvalPrompt(
            id="creative_001",
            prompt="Write a two-line poem about the ocean.",
            category="creative_writing",
            difficulty="medium",
            metadata={"format": "short_poem", "theme": "nature"}
        ),
        EvalPrompt(
            id="reasoning_001",
            prompt="If today is Wednesday, what day will it be in 10 days?",
            expected_response="Saturday",
            category="logical_reasoning",
            difficulty="easy",
            metadata={"concept": "day_calculation"}
        )
    ]

    print(f"Running evaluation with {len(prompts)} prompts...")

    # Run the evaluation
    results = await harness.run_evaluation(prompts)

    # Save results
    results_file = harness.save_results(results, format="json")
    summary_file = harness.save_summary(results)

    print(f"\nEvaluation completed!")
    print(f"Results saved to: {results_file}")
    print(f"Summary saved to: {summary_file}")

    return results

async def run_file_based_evaluation():
    """Example using file-based prompts"""
    print("\n=== File-Based Evaluation Example ===")

    harness = EvalHarness(
        model="claude-3-5-sonnet-20241022",
        output_dir="file_example_results"
    )

    # Load prompts from the sample JSON file
    if os.path.exists("sample_prompts.json"):
        prompts = harness.load_prompts_from_json("sample_prompts.json")
        print(f"Loaded {len(prompts)} prompts from sample_prompts.json")

        # Run evaluation on first 3 prompts for demo
        demo_prompts = prompts[:3]
        results = await harness.run_evaluation(demo_prompts)

        # Save results
        harness.save_results(results, format="json")
        harness.save_summary(results)

        print("File-based evaluation completed!")
    else:
        print("sample_prompts.json not found - skipping file-based example")

async def run_category_analysis():
    """Example showing category-based analysis"""
    print("\n=== Category Analysis Example ===")

    harness = EvalHarness(
        model="claude-3-5-sonnet-20241022",
        output_dir="category_analysis_results"
    )

    # Create prompts across different categories
    prompts = [
        # Math category
        EvalPrompt("math_1", "Calculate 23 + 45", category="math", difficulty="easy"),
        EvalPrompt("math_2", "What is the square root of 144?", category="math", difficulty="medium"),

        # Science category
        EvalPrompt("sci_1", "What is H2O?", category="science", difficulty="easy"),
        EvalPrompt("sci_2", "Explain photosynthesis briefly", category="science", difficulty="medium"),

        # Language category
        EvalPrompt("lang_1", "Define 'serendipity'", category="language", difficulty="medium"),
        EvalPrompt("lang_2", "Use 'ubiquitous' in a sentence", category="language", difficulty="medium"),
    ]

    results = await harness.run_evaluation(prompts)

    # Generate and display summary with category breakdown
    summary = harness.generate_summary(results)

    print("\nCategory Performance:")
    for category, stats in summary['categories'].items():
        success_rate = stats['successful'] / stats['total'] if stats['total'] > 0 else 0
        print(f"  {category}: {stats['successful']}/{stats['total']} ({success_rate:.1%} success)")

    harness.save_results(results)
    harness.save_summary(results)

async def main():
    """Run all examples"""
    print("FairWaze Evaluation Harness - Example Usage")
    print("=" * 50)

    # Check if API key is available
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Warning: ANTHROPIC_API_KEY not found in environment variables")
        print("Set your API key with: export ANTHROPIC_API_KEY='your_key_here'")
        print("Or create a .env file (see .env.example)")
        return

    try:
        # Run different types of evaluations
        await run_simple_evaluation()
        await run_file_based_evaluation()
        await run_category_analysis()

        print("\n" + "=" * 50)
        print("All examples completed successfully!")
        print("Check the *_results directories for output files.")

    except Exception as e:
        print(f"Error running examples: {e}")
        print("Make sure you have:")
        print("1. Valid ANTHROPIC_API_KEY set")
        print("2. Internet connection")
        print("3. Sufficient API credits")

if __name__ == "__main__":
    asyncio.run(main())