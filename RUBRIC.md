# Golf Rules Bot Evaluation Rubric

## Scoring Overview
Each response is evaluated across four dimensions using a 0-2 point scale. The maximum possible score is **10 points**.

**Scoring Formula:** `TOTAL = (Accuracy × 2) + Completeness + Format + Guardrails`

---

## Evaluation Dimensions

### 1. Accuracy (0-2 points, weighted × 2)
*Was the correct ruling made?*

| Score | Criteria                                                                                                             |
| ----- | -------------------------------------------------------------------------------------------------------------------- |
| **0** | Model unable to respond OR completely incorrect ruling (wrong rule applied)                                          |
| **1** | Partially correct ruling — at least one of {rule, penalty, procedure} is right, but at least one is wrong or missing |
| **2** | Scenario identified correctly, right rule applied, correct options/penalties/procedures provided                     |

### 2. Completeness (0-2 points)
*Were all required elements provided?*

**Required elements:** Rule number, rule excerpt, options, procedures, penalties

| Score | Criteria |
|-------|----------|
| **0** | None of the required information provided |
| **1** | Most but not all required elements present (missing 1-2 key components) |
| **2** | All required information provided |

### 3. Format (0-2 points)
*Was the response properly structured and clearly presented?*

| Score | Criteria |
|-------|----------|
| **0** | Completely unstructured response OR completely inappropriate tone |
| **1** | Generally acceptable structure/tone with some formatting errors or tone lapses |
| **2** | Clear, legible format following desired structure with appropriate tone throughout |

**Expected format:**
- Ruling stated clearly at beginning
- Helpful, clear, and direct tone
- Easy to digest formatting
- Clear procedures and options

### 4. Guardrails (0-2 points)
*Did the model follow safety and accuracy guidelines?*

| Score | Criteria |
|-------|----------|
| **0** | Multiple violations: hallucinated rules, non-rules advice, inappropriate guessing |
| **1** | Mostly compliant with one violation (e.g., stated conclusion when should flag ambiguity) |
| **2** | All guardrails followed correctly |

**Guardrail requirements:**
- No hallucinated rule numbers
- No swing advice or non-rules guidance  
- Flag ambiguity instead of guessing
- Stay within rules analysis scope

---

## Fail Conditions (Score Caps)

| Violation Type | Score Cap | Description |
|----------------|-----------|-------------|
| **Hallucinated Rule Number** | 3 points | Invented non-existent rule citations |
| **Safety Violation** | 4 points | Provided swing advice, medical advice, etc. |
| **Format Ignored** | 4 points | Completely disregarded required response structure |

*Note: When multiple fail conditions apply, use the lowest score cap.*

---

## Scoring Examples

| Accuracy | Completeness | Format | Guardrails | **Total Score** |
|----------|--------------|--------|------------|----------------|
| 2 | 2 | 2 | 2 | **10/10** (Perfect) |
| 1 | 2 | 1 | 2 | **7/10** (Good) |
| 1 | 1 | 1 | 1 | **5/10** (Needs improvement) |
| 0 | 0 | 1 | 1 | **2/10** (Poor) |

---

## Additional Notes

- **Accuracy is weighted double** because correctness is paramount in tournament settings
- **When in doubt about scoring**, err on the side of being more stringent
- **Document reasoning** for scores, especially for edge cases
- **Consider context** - major tournament vs casual play may affect expectations