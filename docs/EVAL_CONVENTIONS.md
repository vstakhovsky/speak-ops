# Eval Conventions

**Purpose:** Define how to create and run evals for SpeakOps quality assurance.

## Eval Philosophy

> **Every AI behavior must have eval coverage.**

Evals are NOT optional. They are required quality gates that:
- Prevent quality drift
- Ensure changes don't break functionality
- Provide objective quality measures
- Enable regression testing

## When to Create Evals

### Required Evals (Must Have)

Create evals when:
- ✅ New skill is added
- ✅ Skill behavior is modified
- ✅ Scoring logic changes
- ✅ Workflow is updated
- ✅ Security/privacy changes

### Eval Types

### 1. Quality Evals

Assess behavior quality:

- **phrase-extraction-quality** — Phrase extraction
- **spoken-naturalness** — Natural language check
- **voice-drill-quality** — Drill quality
- **scenario-realism** — Scenario authenticity

### 2. Consistency Evals

Assess consistency over time:

- **activation-scoring** — Scoring consistency
- **weekly-regression** — Regression detection

### 3. Security Evals

Assess security/privacy:

- **privacy-security** — Privacy standards
- **prompt-injection** — Injection resistance

## Eval Case Template

```markdown
# Eval Case: [Name]

**Category:** [quality/consistency/security]
**Priority:** [high/medium/low]
**Last updated:** [date]

## Description
[What this eval tests]

## Input
```json
[Input data]
```

## Expected Behavior
[What should happen]

## Pass Criteria
- [Criterion 1]
- [Criterion 2]

## Fail Examples
- [Example of failure]

## Scoring Rubric
| Score | Criteria |
|-------|----------|
| 1 | [Failed] |
| 2 | [Poor] |
| 3 | [Acceptable] |
| 4 | [Good] |
| 5 | [Excellent] |

**Pass threshold:** [4]
```

## Eval Rubric Template

```markdown
# [Eval Name] Rubric

## Eval Goal
[What this eval tests]

## Scoring Rubric

| Score | Level | Criteria |
|-------|-------|----------|
| 1 | Failed | [Description] |
| 2 | Poor | [Description] |
| 3 | Acceptable | [Description] |
| 4 | Good | [Description] |
| 5 | Excellent | [Description] |

**Pass threshold:** [4]

## Dimensions
[Key dimensions being evaluated]

## Sample Cases
[Example test cases]

## Edge Cases
[Boundary conditions]

## Fail Examples
[What failure looks like]
```

## Running Evals

### Command Line

```bash
# Run all evals
python scripts/run_evals.py --all

# Run specific eval
python scripts/run_evals.py --eval phrase-extraction-quality

# Run with report
python scripts/run_evals.py --all --report
```

### GitHub Actions

```bash
# Eval regression runs automatically on PR
# Manual trigger available
```

## Interpreting Results

### Score 5 (Excellent)

- Behavior exceeds expectations
- Ready to merge
- Document best practices

### Score 4 (Good)

- Behavior meets requirements
- Ready to merge
- Consider minor improvements

### Score 3 (Acceptable)

- Behavior works but has issues
- Fix before merge
- Re-run eval after fixes

### Score 1–2 (Failed)

- Behavior is broken or problematic
- Must fix before merge
- Blocking issue

## Quality Gates

### Before Merge

**For skill changes:**
- [ ] Skill evals pass (≥4/5)
- [ ] Naturalness eval passes (≥4/5)
- [ ] Related evals pass

**For scoring changes:**
- [ ] Scoring consistency eval passes
- [ ] Regression eval passes

**For ingestion/logging:**
- [ ] Privacy/security eval passes
- [ ] Prompt injection eval passes

### Eval Regression

**When eval fails:**
1. Identify breaking change
2. Assess impact
3. Fix or revert
4. Re-run eval
5. Document decision

## Common Mistakes

### Mistake 1: No Evals

❌ **Bad:** Modifying skill without evals
✅ **Good:** Always create/update evals with skill changes

### Mistake 2: Vague Criteria

❌ **Bad:** "Should work well"
✅ **Good:** "Extract 5–10 phrases, 80% natural"

### Mistake 3: No Fail Examples

❌ **Bad:** Only success cases
✅ **Good:** Include failure examples and edge cases

### Mistake 4: Skipping Regression

❌ **Bad:** Not checking for breakage
✅ **Good:** Always run regression evals

## Eval Maintenance

### Monthly

- Review all evals
- Add discovered edge cases
- Update thresholds if needed
- Remove outdated evals

### When Behavior Changes

- Update eval criteria
- Add new test cases
- Update rubrics
- Document changes

### When Issues Found

- Add failing case to eval
- Update expected behavior
- Re-test after fix

## Eval Quality Checklist

### Good Eval ✅

- [ ] Clear purpose
- [ ] Specific input/output
- [ ] Objective pass criteria
- [ ] Multiple test cases
- [ ] Edge cases covered
- [ ] Fail examples included
- [ ] Scoring rubric defined
- [ ] Pass threshold set

### Poor Eval ❌

- Vague purpose
- Unclear criteria
- Subjective assessment
- Missing test cases
- No edge cases
- No fail examples
- No scoring rubric
- No pass threshold

## Documentation

### For Each Eval

- [ ] Eval rubric created
- [ ] Test cases documented
- [ ] Pass criteria defined
- [ ] Edge cases listed
- [ ] Fail examples provided

### For Eval Runs

- [ ] Results documented
- [ ] Failures analyzed
- [ ] Fixes implemented
- [ ] Re-testing completed

---

**Convention Version:** 1.0
**Purpose:** Ensure consistent, comprehensive eval coverage
