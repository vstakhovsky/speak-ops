# Activation Scoring Consistency Rubric

## Eval Goal

Assess whether activation scoring is consistent, explainable, and accurately reflects phrase activation.

## Scoring Rubric

| Score | Level | Criteria |
|-------|-------|----------|
| 1 | Failed | Scoring is random or inconsistent |
| 2 | Poor | Scoring has major inconsistencies |
| 3 | Acceptable | Mostly consistent, some edge cases unclear |
| 4 | Good | Consistent scoring, explainable |
| 5 | Excellent | Highly consistent, perfectly explainable |

**Pass threshold:** 4

## Dimensions

### 1. Consistency (30 points)
- Same inputs give same scores: 15 points
- Similar inputs give similar scores: 15 points

### 2. Explainability (25 points)
- Score changes are explainable: 15 points
- Dimension scores make sense: 10 points

### 3. Accuracy (25 points)
- Correct usage increases score: 10 points
- Incorrect usage decreases or stagnates: 10 points
- Natural usage rewarded: 5 points

### 4. Progress Tracking (20 points)
- Score increases over time with practice: 10 points
- Regression detected when appropriate: 10 points

## Scoring Model Verification

**Correct usage:**
- Used correctly + naturally → +40 points
- Used correctly + formally → +30 points
- Used with minor errors → +20 points
- Used with major errors → +10 points
- Not used → 0 points

**Additional dimensions:**
- Retrieval speed: +10 (instant), +5 (delayed), 0 (struggled)
- Context transfer: +15 (new context), 0 (same context)
- Retention: +5 (used after 7+ days)

## Sample Cases

### Case 1: Perfect usage
**Input:** Phrase used correctly, naturally, instantly in new context
**Expected:** Score +40 (usage) +10 (speed) +15 (context) = +65
**Pass criteria:** Score reflects all positive factors

### Case 2: Incorrect usage
**Input:** Phrase used incorrectly (wrong preposition, wrong meaning)
**Expected:** Score +0 to +10 (used but incorrect)
**Pass criteria:** Incorrect usage penalized appropriately

### Case 3: Missed phrase
**Input:** Phrase targeted but not used
**Expected:** No score change (0 points)
**Pass criteria:** Missed phrases don't increase score

### Case 4: Regression detection
**Input:** Phrase previously at 80, now used incorrectly
**Expected:** Score decreases, flagged as regression
**Pass criteria:** Regression detected and flagged

### Case 5: Consistency check
**Input:** Same phrase usage in two different sessions
**Expected:** Similar score changes
**Pass criteria:** Consistent scoring demonstrated

## Edge Cases

### Edge case 1: Partial correctness
**Input:** Phrase used with minor grammatical error but meaning clear
**Expected:** Partial points (+20)
**Pass criteria:** Partial correctness recognized

### Edge case 2: Very formal but correct
**Input:** Phrase used correctly but overly formally
**Expected:** +30 (correct but not fully natural)
**Pass criteria:** Formal usage partially rewarded

### Edge case 3: Slow but correct
**Input:** Phrase used correctly but after long hesitation
**Expected:** Full usage points, reduced speed points
**Pass criteria:** Slow retrieval not penalized too heavily

## Consistency Tests

### Test 1: Same input, same score
**Input:** Phrase "push back on" used correctly, naturally, instantly (session A)
**Input:** Phrase "push back on" used correctly, naturally, instantly (session B)
**Expected:** Identical score changes
**Pass criteria:** Scores match

### Test 2: Similar usage, similar score
**Input:** Phrase used correctly with 2-second delay (session A)
**Input:** Phrase used correctly with 3-second delay (session B)
**Expected:** Similar score changes
**Pass criteria:** Scores within 5 points

### Test 3: Better performance, better score
**Input:** Session 1: Used slowly, formally → Score +25
**Input:** Session 2: Used instantly, naturally → Score +50
**Expected:** Session 2 score higher
**Pass criteria:** Improvement reflected

## Fail Examples

### Example 1: Inconsistent scoring
**Input:** Same usage in two sessions
**Output:** Score +40 in session A, +20 in session B
**Why it fails:** Identical inputs should give identical scores

### Example 2: Unexplained score
**Input:** Phrase used correctly
**Output:** Score +65 with no explanation
**Why it fails:** Score should be explainable

### Example 3: No regression detection
**Input:** Phrase dropped from 80 to 60
**Output:** No flag or warning
**Why it fails:** Regression should be detected

## Related Evals

- Weekly Regression — Tracks score trends over time
- Weak Phrase Replay — Uses scoring to identify weak phrases

---

**Eval ID:** activation-scoring
**Category:** Quality
**Status:** Active
