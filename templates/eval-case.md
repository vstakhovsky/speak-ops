# Eval Case Template

## Eval Case: {{ eval_name }}

**Category:** {{ category }}
**Priority:** {{ priority }}
**Last updated:** {{ date }}

---

## Description

{{ description }}

**What it tests:** {{ what_it_tests }}

---

## Input

```json
{{ input_json }}
```

**Input description:** {{ input_description }}

---

## Expected Behavior

{{ expected_behavior }}

**Success criteria:**
- {{ criterion_1 }}
- {{ criterion_2 }}
- {{ criterion_3 }}

---

## Pass Criteria

| Criterion | How to Verify | Pass Threshold |
|-----------|----------------|----------------|
| {{ criterion_1 }} | {{ verification_method }} | {{ threshold }} |
| {{ criterion_2 }} | {{ verification_method }} | {{ threshold }} |
| {{ criterion_3 }} | {{ verification_method }} | {{ threshold }} |

---

## Fail Examples

### Example 1: {{ fail_example_name }}
**Input:** {{ fail_input }}
**Why it fails:** {{ failure_reason }}
**Expected fix:** {{ expected_fix }}

### Example 2: {{ fail_example_name }}
**Input:** {{ fail_input }}
**Why it fails:** {{ failure_reason }}
**Expected fix:** {{ expected_fix }}

---

## Scoring Rubric

| Score | Level | Criteria |
|-------|-------|----------|
| 1 | Failed | {{ score_1_criteria }} |
| 2 | Poor | {{ score_2_criteria }} |
| 3 | Acceptable | {{ score_3_criteria }} |
| 4 | Good | {{ score_4_criteria }} |
| 5 | Excellent | {{ score_5_criteria }} |

**Pass threshold:** {{ pass_threshold }}

---

## Edge Cases

### Edge Case 1: {{ edge_case_name }}
**Description:** {{ edge_case_description }}
**Expected behavior:** {{ edge_case_expected }}

### Edge Case 2: {{ edge_case_name }}
**Description:** {{ edge_case_description }}
**Expected behavior:** {{ edge_case_expected }}

---

## Related Evals

- {{ related_eval_1 }}
- {{ related_eval_2 }}

---

## History

| Date | Result | Score | Notes |
|------|--------|-------|-------|
| {{ date_1 }} | {{ result_1 }} | {{ score_1 }} | {{ notes_1 }} |
| {{ date_2 }} | {{ result_2 }} | {{ score_2 }} | {{ notes_2 }} |

---

**Eval ID:** {{ eval_id }}
**Status:** {{ status }}
