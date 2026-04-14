# Golf Rules Evaluation System

A two-stage evaluation system for testing golf rules AI bots with comprehensive grading and versioned results.

## Quick Start

### 1. Run Evaluation Test
```bash
# Run with default settings (auto-extracts all versions)
./run_golf_rules_eval.py

# Use different model (any working Claude model)
./run_golf_rules_eval.py --model "claude-3-haiku-20240307"
```

### 2. Grade Results
```bash
# Grade the results (replace with your actual eval directory)
./grade_golf_rules_eval.py --eval-dir "v0.1_haiku_rv1_20260413_143000"
```

## Workflow

### Stage 1: Test Runner (`run_golf_rules_eval.py`)
- Auto-extracts system prompt version from `../prompts/golf_rules_system_prompt_v0.2.md` frontmatter
- Auto-extracts rubric version from local `RUBRIC.md` frontmatter  
- Loads golf rules test cases from local `golf_rules_test_cases.json`
- Sends each question sequentially to Anthropic API with system prompt
- Creates versioned folder: `v{prompt_version}_{model_abbrev}_r{rubric_version}_{timestamp}`
- Copies all reference files and creates initial manifest

### Stage 2: Grader (`grade_golf_rules_eval.py`) 
- Loads responses and auto-detects ground truth answers
- Uses Claude Haiku at temperature=0 for deterministic grading
- Grades each response on 4 dimensions according to local `RUBRIC.md`
- Semantic comparison (not literal) - tone/format differences not penalized
- Updates manifest with final scores and breakdowns

## Output Structure

Each evaluation run creates a folder: `v{prompt_version}_{model_abbrev}_r{rubric_version}_{timestamp}/`

**Complete file structure:**
- `manifest.json` - Metadata + summary with scores and breakdowns  
- `system_prompt.md` - Copy of system prompt used
- `rubric.md` - Copy of evaluation rubric used
- `test_cases.json` - Copy of test cases evaluated
- `responses.json` - Raw model outputs
- `grades.json` - Per-case scores + reasoning
- `summary.json` - Aggregates (total, by difficulty, by category)
- `report.md` - Human-readable analysis report

## Model Compatibility

Both scripts default to `claude-3-haiku-20240307` which is known to work. If you want to use other models, verify they're available in your API access before running.

## Command Line Options

### Test Runner
```bash
./run_golf_rules_eval.py \
  --model "claude-3-haiku-20240307" \
  --test-cases "golf_rules_test_cases.json" \
  --system-prompt "../prompts/golf_rules_system_prompt_v0.2.md" \
  --rate-limit 1.0
```

### Grader  
```bash
./grade_golf_rules_eval.py \
  --eval-dir "v0.1_haiku_rv1_20260413_143000" \
  --model "claude-3-haiku-20240307" \
  --rate-limit 0.5
```

## Manifest Structure

The `manifest.json` file contains complete evaluation metadata:

```json
{
  "version": "v0.1",
  "timestamp": "2026-04-13T14:30:00Z", 
  "commit_hash": "abc1234",
  "model": "claude-3-haiku-20240307",
  "grader_model": "claude-3-haiku-20240307",
  "temperature": 0,
  "grader_temperature": 0,
  "n_cases": 40,
  "changes_from_previous": "Baseline run",
  "aggregate_score": 75.2,
  "aggregate_max": 100,
  "breakdowns": {
    "by_category": {"penalty_area": 80, "bunker": 70},
    "fail_conditions_triggered": {"Cited rule number": 7, "safety_violation": 0}
  }
}
```

## Grading Dimensions

From local `RUBRIC.md`:
1. **Accuracy (0-2, weighted ×2)** - Was the correct ruling made?
2. **Completeness (0-2)** - All required elements provided?
3. **Format (0-2)** - Proper structure and tone?
4. **Guardrails (0-2)** - No hallucinated rules or inappropriate advice?

**Maximum Score:** 10 points  
**Fail Conditions:** Cap scores for cited rule numbers (3), safety violations (4), format ignored (4)

## Example Usage

```bash
# Run baseline evaluation (all versions auto-detected)
./run_golf_rules_eval.py
# Creates: v0.1_haiku_rv1_20260413_143000/

# Grade the results  
./grade_golf_rules_eval.py --eval-dir "v0.1_haiku_rv1_20260413_143000"

# Test with different model
./run_golf_rules_eval.py --model "claude-3-haiku-20240307"
# Creates: v0.1_haiku_rv1_20260413_144500/

# Grade the new results
./grade_golf_rules_eval.py --eval-dir "v0.1_haiku_rv1_20260413_144500"
```

The system enables easy comparison across different models, prompts, and configurations with complete reproducibility through versioned artifacts.