---
version: v0.1
date: 2026-04-13
model: claude-sonnet (via Anthropic API)
baseline_score: 81.25%
---

# v0.1 Eval Analysis

## Summary

Baseline evaluation of the golf rules bot across 40 test cases (10 easy, 10 medium, 10 hard, 10 adversarial). Overall average score: **8.125 / 10 (81.25%)**. Max possible score is 10, calculated as accuracy (weighted 2x) + completeness + format + guardrails, each scored 0-2.

## Dimension Averages

- **Accuracy: 1.425 / 2** — weakest dimension, heavily impacted by hallucinated rule numbers
- **Completeness: 1.725 / 2**
- **Format: 1.775 / 2**
- **Guardrails: 1.775 / 2**

Accuracy is the clear outlier. The other three dimensions cluster near the top of the scale, suggesting the model generally provides complete, well-formatted, on-topic responses — but frequently cites incorrect or non-existent rule numbers.

## Difficulty Breakdown

| Difficulty | Avg Score | Count |
|---|---|---|
| Easy | 8.8 | 10 |
| Medium | 8.3 | 10 |
| Hard | 8.0 | 10 |
| Adversarial | 7.4 | 10 |

Scores decrease with difficulty as expected, validating that the test case difficulty tiers are appropriately calibrated.

## Score Distribution

| Score | Count |
|---|---|
| 10 | 25 |
| 8 | 3 |
| 7 | 3 |
| 6 | 1 |
| 3 | 8 |

The distribution is heavily bimodal: 25 perfect scores and 8 scores of 3. The 8 scores of 3 correspond exactly to the 8 cases where the "Hallucinated Rule Number" fail condition was triggered (which caps the total at 3). This means the fail condition is doing nearly all the differentiation work — the four-dimension rubric contributes relatively little signal beyond the binary "did it hallucinate or not." This is worth revisiting in future rubric iterations: either the cap is too aggressive, or the dimension scoring is too generous, or the model's performance is genuinely that bimodal.

## Fail Conditions

- **Hallucinated Rule Number: 8 / 40 (20%)** — the dominant failure mode
- Safety violations: 0
- Format violations: 0

## Weakest Categories

| Category | Avg Score | Cases |
|---|---|---|
| ball_in_motion | 3.0 | 1 |
| pitch_mark | 3.0 | 1 |
| embedded | 4.67 | 3 |
| provisional | 5.33 | 3 |
| OB | 6.0 | 1 |

Categories with single cases should be interpreted cautiously. The embedded and provisional categories have enough cases to indicate a systematic weakness.

## Strongest Categories

| Category | Avg Score | Cases |
|---|---|---|
| ball_marking | 10.0 | 1 |
| caddie | 10.0 | 1 |
| dropping | 10.0 | 1 |
| GUR | 10.0 | 2 |
| obstruction | 10.0 | 1 |
| relief | 10.0 | 1 |
| unplayable | 10.0 | 2 |
| bunker | 9.5 | 4 |

## Data Quality Issue

One test case has an empty category field (`"": 1 case`). This should be corrected before the next eval run.

## Recommended Actions for v0.2

1. **Address hallucinated rule numbers (highest priority).** Add explicit instruction to the system prompt: only cite rule numbers when certain they exist; describe the rule without citing a number when unsure. This single change targets 20% of cases and the only active fail condition.
2. **Review embedded and provisional test cases.** Determine whether failures are due to the system prompt lacking domain-specific guidance or the model's underlying knowledge gaps.
3. **Fix the empty category field** in the test case data.
4. **Consider rubric calibration.** The bimodal score distribution suggests the fail condition cap (3) may need adjustment, or the dimension scoring may need to be more discriminating to produce useful signal beyond the binary hallucination check.
