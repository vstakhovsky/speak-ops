# Weekly Regression Eval

## Eval Goal

Ensure changes to SpeakOps don't break existing functionality or regress phrase activation scores.

## Scoring Rubric

| Score | Level | Criteria |
|-------|-------|----------|
| 1 | Failed | Critical regression detected |
| 2 | Poor | Multiple regressions, system degraded |
| 3 | Acceptable | Some regressions, main functionality intact |
| 4 | Good | Minimal to no regression |
| 5 | Excellent | No regression, improvements detected |

**Pass threshold:** 4

## Dimensions

### 1. Phrase Extraction (20 points)
- Previously extracted phrases still extract: 10 points
- No new false positives: 10 points

### 2. Naturalness Filtering (20 points)
- Previously accepted phrases still accepted: 10 points
- Previously rejected phrases still rejected: 10 points

### 3. Voice Drill Generation (20 points)
- Previous drills still generate: 10 points
- Drill quality not degraded: 10 points

### 4. Activation Scoring (20 points)
- Scoring consistency maintained: 10 points
- No unexplained score changes: 10 points

### 5. Weak Phrase Detection (10 points)
- Previously weak phrases still detected: 5 points
- No false positives: 5 points

### 6. Privacy/Security (10 points)
- Privacy standards maintained: 5 points
- Security standards maintained: 5 points

## Regression Tests

### Test Suite 1: Phrase Extraction
**Input:** 50 previously extracted phrases
**Expected:** All phrases still extracted with same metadata
**Pass criteria:** ≥95% of phrases extracted identically

### Test Suite 2: Naturalness Filtering
**Input:** 25 accepted phrases, 25 rejected phrases
**Expected:** Same verdicts (accept/reject)
**Pass criteria:** ≥90% of verdicts match

### Test Suite 3: Voice Drills
**Input:** 10 previous drill specifications
**Expected:** Drills generate successfully with same quality
**Pass criteria:** All drills generate, quality ≥ previous

### Test Suite 4: Activation Scoring
**Input:** 20 phrase usage scenarios
**Expected:** Same scores within ±5 points
**Pass criteria:** ≥90% of scores within tolerance

### Test Suite 5: Privacy/Security
**Input:** Security checklist
**Expected:** All items pass
**Pass criteria:** No security regressions

## Edge Cases

### Edge case 1: Model drift
**Scenario:** LLM behavior changes slightly
**Expected:** Minor score variations (±10 points) acceptable
**Pass criteria:** System still functional, no critical regressions

### Edge case 2: Updated scoring model
**Scenario:** Scoring dimensions changed
**Expected:** Scores update consistently, backward compatibility
**Pass criteria:** Historical scores can be recalculated

### Edge case 3: New skill added
**Scenario:** New skill integrated
**Expected:** Existing skills not affected
**Pass criteria:** No regressions in existing functionality

## Fail Examples

### Example 1: Phrase extraction regression
**Issue:** Previously extracted phrase no longer extracts
**Why it fails:** User loses existing phrases

### Example 2: Naturalness filtering regression
**Issue:** Previously accepted phrase now rejected
**Why it fails:** Inconsistent filtering, user confusion

### Example 3: Scoring regression
**Issue:** Same usage gives different score
**Why it fails:** Scoring inconsistency, loss of trust

### Example 4: Security regression
**Issue:** New feature bypasses security checks
**Why it fails:** Security regression, must block

## Regression Prevention

### Before merge
1. Run full regression test suite
2. Compare with previous benchmark results
3. Check scoring consistency
4. Verify privacy/security standards
5. Test on sample data

### After regression detected
1. Identify breaking change
2. Assess impact
3. Fix or rollback
4. Update tests if behavior change is intentional
5. Document in decision log

## Weekly Benchmark

**Run every week before merge:**
- Phrase extraction test suite
- Naturalness filtering test suite
- Voice drill generation test suite
- Activation scoring test suite
- Privacy/security checklist

**Pass criteria:** All tests pass, scores ≥4

## Related Evals

- All other evals — Regression tests all evals

---

**Eval ID:** weekly-regression
**Category:** Regression
**Status:** Active
