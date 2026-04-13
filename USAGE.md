# FairWaze Evaluation Harness Usage Guide

A comprehensive evaluation framework for testing AI models via the Anthropic API with detailed metrics and reporting.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your API key:**
   ```bash
   # Option 1: Environment variable
   export ANTHROPIC_API_KEY="your_api_key_here"
   
   # Option 2: Create .env file (copy from .env.example)
   cp .env.example .env
   # Edit .env and add your API key
   ```

3. **Run with sample prompts:**
   ```bash
   python eval_harness.py --prompts sample_prompts.json
   ```

## Usage Examples

### Basic Usage
```bash
# Run evaluation with JSON prompts
python eval_harness.py --prompts sample_prompts.json

# Run with CSV prompts
python eval_harness.py --prompts sample_prompts.csv --format csv

# Use a different model
python eval_harness.py --prompts sample_prompts.json --model claude-3-opus-20240229

# Custom output directory and rate limiting
python eval_harness.py --prompts sample_prompts.json --output-dir my_results --rate-limit 2.0
```

### Programmatic Usage
```python
import asyncio
from eval_harness import EvalHarness, EvalPrompt

# Initialize harness
harness = EvalHarness(
    model="claude-3-5-sonnet-20241022",
    output_dir="my_eval_results",
    rate_limit_delay=1.0
)

# Create prompts programmatically
prompts = [
    EvalPrompt(
        id="test_001",
        prompt="What is the capital of Japan?",
        expected_response="Tokyo",
        category="geography",
        difficulty="easy"
    ),
    EvalPrompt(
        id="test_002", 
        prompt="Explain quantum computing in simple terms.",
        category="science",
        difficulty="hard"
    )
]

# Run evaluation
async def run_eval():
    results = await harness.run_evaluation(prompts)
    harness.save_results(results, format="json")
    harness.save_summary(results)

asyncio.run(run_eval())
```

## Prompt File Formats

### JSON Format
```json
[
  {
    "id": "unique_identifier",
    "prompt": "Your prompt text here",
    "expected_response": "Optional expected response",
    "category": "Optional category",
    "difficulty": "easy|medium|hard",
    "metadata": {
      "custom_field": "custom_value"
    }
  }
]
```

### CSV Format
```csv
id,prompt,expected_response,category,difficulty,metadata
test_001,"What is 2+2?","4",math,easy,"{""topic"": ""arithmetic""}"
```

## Output Files

The harness generates several output files:

### Results Files
- `eval_results_YYYYMMDD_HHMMSS.json` - Detailed results in JSON format
- `eval_results_YYYYMMDD_HHMMSS.csv` - Results in CSV format (if requested)

### Summary Files  
- `eval_summary_YYYYMMDD_HHMMSS.json` - Summary statistics and metrics
- `eval_harness.log` - Execution logs

### Result Structure
Each result contains:
- `prompt_id` - Unique identifier for the prompt
- `prompt_text` - The original prompt
- `response` - Model's response
- `model` - Model used
- `timestamp` - When the prompt was processed
- `response_time_ms` - Response time in milliseconds
- `input_tokens` - Number of input tokens
- `output_tokens` - Number of output tokens
- `total_tokens` - Total tokens used
- `success` - Whether the request succeeded
- `error_message` - Error details if failed
- `metadata` - Additional metadata from prompt

## Configuration Options

### Command Line Arguments
- `--prompts` - Path to prompts file (required)
- `--model` - Model to use (default: claude-3-5-sonnet-20241022)
- `--output-dir` - Output directory (default: eval_results)
- `--rate-limit` - Delay between requests in seconds (default: 1.0)
- `--format` - Output format: json or csv (default: json)
- `--api-key` - API key (or use ANTHROPIC_API_KEY env var)

### Environment Variables
- `ANTHROPIC_API_KEY` - Your Anthropic API key
- `DEFAULT_MODEL` - Default model to use
- `OUTPUT_DIR` - Default output directory
- `RATE_LIMIT_DELAY` - Default rate limiting delay

## Available Models

Common Anthropic models you can use:
- `claude-3-5-sonnet-20241022` (default) - Latest Sonnet model
- `claude-3-5-haiku-20241022` - Fast and efficient
- `claude-3-opus-20240229` - Most capable model

## Rate Limiting

The harness includes built-in rate limiting to respect API limits:
- Default: 1 second delay between requests
- Adjustable via `--rate-limit` parameter
- Recommended: 1-2 seconds for sustained usage

## Error Handling

The harness handles various error scenarios:
- API rate limiting
- Network timeouts
- Invalid responses
- Malformed prompts
- Authentication errors

Failed requests are logged but don't stop the evaluation process.

## Best Practices

1. **Start Small**: Test with a few prompts first
2. **Monitor Costs**: Track token usage in summary files
3. **Use Categories**: Organize prompts by category for better analysis
4. **Rate Limiting**: Don't set rate limit too low to avoid hitting API limits
5. **Backup Results**: Results files include timestamps for easy organization
6. **Review Logs**: Check eval_harness.log for detailed execution information

## Troubleshooting

### Common Issues

**"API key not found"**
- Set ANTHROPIC_API_KEY environment variable
- Or use --api-key command line argument

**"Rate limit exceeded"**
- Increase --rate-limit value
- Check your API usage limits

**"Model not found"**
- Verify model name spelling
- Check available models in Anthropic console

**"File not found"**
- Verify prompts file path
- Check file format (must be .json or .csv)

### Getting Help

1. Check the logs in eval_harness.log
2. Verify your API key and limits
3. Test with the sample_prompts.json file first
4. Review the error messages in failed results