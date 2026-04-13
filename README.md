# FairWaze

A comprehensive evaluation harness for testing AI models via the Anthropic API with detailed metrics and reporting.

## Features

- **Sequential Prompt Processing**: Send multiple prompts to AI models in sequence
- **Comprehensive Metrics**: Track response times, token usage, success rates
- **Multiple Input Formats**: Support for JSON and CSV prompt files
- **Detailed Reporting**: Generate summaries with category breakdowns
- **Error Handling**: Robust error handling with detailed logging
- **Rate Limiting**: Built-in rate limiting to respect API limits
- **Flexible Configuration**: Command-line and programmatic configuration options

## Quick Start

1. **Setup**:
   ```bash
   python setup.py
   ```

2. **Configure API Key**:
   ```bash
   export ANTHROPIC_API_KEY="your_api_key_here"
   ```

3. **Run Evaluation**:
   ```bash
   python eval_harness.py --prompts sample_prompts.json
   ```

## Files

- `eval_harness.py` - Main evaluation harness script
- `example_usage.py` - Example usage patterns
- `sample_prompts.json` - Sample prompts for testing
- `sample_prompts.csv` - Sample prompts in CSV format
- `setup.py` - Setup and installation script
- `USAGE.md` - Comprehensive usage documentation
- `requirements.txt` - Python dependencies

## Documentation

See [USAGE.md](USAGE.md) for detailed documentation, examples, and troubleshooting.

## Quick Example

```python
from eval_harness import EvalHarness, EvalPrompt

# Create harness
harness = EvalHarness(model="claude-3-5-sonnet-20241022")

# Define prompts
prompts = [
    EvalPrompt(id="test1", prompt="What is 2+2?", category="math"),
    EvalPrompt(id="test2", prompt="Explain photosynthesis", category="science")
]

# Run evaluation
results = await harness.run_evaluation(prompts)
harness.save_results(results)
```