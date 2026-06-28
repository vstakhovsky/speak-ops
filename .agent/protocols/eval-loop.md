# Eval Loop Protocol

## Purpose

Define the standard workflow for creating and running evals in SpeakOps.

## Process

### 1. Identify Eval Need

When to create eval:

- New AI behavior added
- Existing behavior modified
- Scoring logic changed
- Quality issue detected
- Regression risk

### 2. Design Eval

Use eval-engineer agent:

1. **Define eval type** — What to test
2. **Write rubric** — Scoring criteria
3. **Create test cases** — Input/output pairs
4. **Define thresholds** — Pass/fail criteria
5. **Document edge cases** — Boundary conditions

### 3. Implement Eval

1. **Create rubric file** — `evals/rubrics/[name].md`
2. **Add test cases** — Sample inputs/outputs
3. **Implement runner** — If automated
4. **Document usage** — How to run

### 4. Run Eval

1. **Run test cases** — Against current implementation
2. **Score results** — Using rubric
3. **Check thresholds** — Pass/fail
4. **Generate report** — Summary of findings

### 5. Review Results

1. **Analyze failures** — Why did it fail?
2. **Check false positives** — Eval too strict?
3. **Check false negatives** — Eval too lenient?
4. **Refine eval** — Adjust if needed

### 6. Fix or Iterate

**If eval fails:**
1. Fix implementation
2. Re-run eval
3. Verify fix

**If eval is wrong:**
1. Fix rubric
2. Adjust thresholds
3. Re-run eval

## Eval Types

### Quality Evals

- **phrase-extraction-quality** — Phrase extraction
- **spoken-naturalness** — Natural language check
- **voice-drill-quality** — Drill quality
- **scenario-realism** — Scenario realism

### Consistency Evals

- **activation-scoring** — Scoring consistency
- **weekly-regression** — Regression detection

### Security Evals

- **privacy-security** — Privacy/security standards
- **prompt-injection** — Injection resistance

## Eval Template

```markdown
# [Eval Name]

## Eval Goal
[What this eval tests]

## Scoring Rubric
| Score | Level | Criteria |
|-------|-------|----------|

## Sample Cases
### Case 1: [name]
**Input:** [input]
**Expected:** [expected]
**Pass criteria:** [criteria]

## Edge Cases
### Edge case 1: [name]
**Description:** [description]
**Expected:** [expected]

## Fail Examples
### Example 1: [name]
**Input:** [input]
**Why it fails:** [reason]
```

## Running Evals

**Run all evals:**
```bash
python scripts/run_evals.py --all
```

**Run specific eval:**
```bash
python scripts/run_evals.py --eval [eval-name]
```

**View results:**
```bash
cat evals/reports/eval_report_[timestamp].json
```

## Quality Gates

**Before merging:**

- [ ] All quality evals pass (≥4/5)
- [ ] All security evals pass (≥4/5)
- [ ] No regression eval failures
- [ ] Eval report reviewed

**If eval fails:**
- Fix implementation OR
- Adjust eval thresholds (documented) OR
- Document known issue

## Continuous Improvement

**Weekly:**
- Run regression evals
- Check for score drift
- Update test cases

**Monthly:**
- Review all evals
- Add edge cases discovered
- Adjust thresholds if needed

**Quarterly:**
- Comprehensive eval review
- Remove outdated evals
- Add new eval types

## Examples

### Example 1: New Skill Eval

**Task:** Add spoken-naturalness-gate skill

**Process:**
1. Design eval (naturalness scoring)
2. Write rubric (1–5 scale)
3. Add test cases (formal, natural, borderline)
4. Run eval (check scoring)
5. Fix issues (adjust threshold)
6. Document (eval rubric created)

### Example 2: Regression Eval

**Task:** Ensure activation scoring doesn't regress

**Process:**
1. Run baseline evals (score known inputs)
2. Make code changes
3. Re-run evals (compare results)
4. Check regression (scores within tolerance)
5. Fix or revert (if regression detected)

## Eval Maintenance

**When to update evals:**
- Behavior changes intentionally
- New edge cases discovered
- Thresholds too strict/lenient
- Better evaluation methods found

**When to remove evals:**
- Feature deprecated
- Eval no longer relevant
- Duplicate eval exists

## Anti-Patterns

**Don't do this:**
- Add behavior without eval
- Ignore eval failures
- Set thresholds too low
- Skip regression testing
- Over-fit evals to implementation

**Do this instead:**
- Eval every AI behavior
- Fix failures before merging
- Set meaningful thresholds
- Test for regression
- Keep evals independent

---

**Protocol Version:** 1.0
**Status:** Active
