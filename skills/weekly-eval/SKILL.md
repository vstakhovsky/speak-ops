# weekly-eval

Runs fixed benchmark scenarios every week to track progress.

## Trigger Conditions

User runs:
```bash
/weekly-eval
```

Or when:
- Week has passed since last eval
- User wants to check progress
- Before high-stakes event (interview, presentation)

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| phrase_bank | list | All phrases with scores |
| practice_logs | list | Recent practice sessions |
| previous_evals | list | Previous weekly eval results |
| target_count | number | Number of phrases to eval (default: 20) |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| active_phrases_added | list | New phrases that became active |
| weak_phrases_remaining | list | Phrases still weak |
| regressed_phrases | list | Phrases that dropped in score |
| naturalness_issues | list | Phrases with naturalness problems |
| readiness_score | number | Overall readiness score (0–100) |
| next_week_plan | dict | Recommended drills for next week |

## Benchmark Scenarios

### 1. Senior PM Interview Question
**Scenario:** Tell me about a time you had to manage a difficult stakeholder relationship.
**Target phrases:** 5 phrases from stakeholder-conflict domain
**Duration:** 5 minutes
**Eval:** Did you use target phrases naturally?

### 2. Roadmap Trade-off Meeting
**Scenario:** Discussing prioritization with constraints.
**Target phrases:** 5 phrases from prioritization domain
**Duration:** 5 minutes
**Eval:** Did you handle trade-offs naturally?

### 3. Stakeholder Pushback
**Scenario:** VP questioning your roadmap decisions.
**Target phrases:** 5 phrases from pushback domain
**Duration:** 5 minutes
**Eval:** Did you push back appropriately?

### 4. AI/Evals Technical Discussion
**Scenario:** Discussing evaluation strategy with technical team.
**Target phrases:** 5 phrases from ai-evals domain
**Duration:** 5 minutes
**Eval:** Did you discuss technical concepts naturally?

## Workflow

1. **Select benchmark phrases** — Choose 20 phrases across domains
2. **Run 4 benchmark scenarios** — User practices each
3. **Score each scenario** — Evaluate phrase usage
4. **Compare with previous** — Check progress vs last week
5. **Identify trends** — What improved, what regressed
6. **Calculate readiness score** — Overall readiness percentage
7. **Generate recommendations** — What to practice next week
8. **Log results** — Save to weekly_evals.jsonl
9. **Output report** — Weekly eval summary

## Scoring

**Readiness Score (0–100):**
- Active phrases (75+ score): 40 points max
- Weak phrases remaining: -2 points each
- Regressed phrases: -5 points each
- Naturalness issues: -3 points each
- Benchmark performance: 40 points max

**Status Levels:**
- 90–100: Ready for interviews/meetings
- 75–89: Good, keep practicing
- 60–74: Making progress, not ready yet
- <60: Need more practice

## Examples

### Example 1: Weekly progress
```
Previous eval (Week 1):
- Active phrases: 12
- Weak phrases: 8
- Regressed: 0
- Naturalness issues: 3
- Readiness score: 68

Current eval (Week 2):
- Active phrases: 18 (+6)
- Weak phrases: 5 (-3)
- Regressed: 1
- Naturalness issues: 2 (-1)
- Readiness score: 78

Result: +10 points, making good progress
```

### Example 2: Regression detected
```
Previous eval (Week 3):
- Active phrases: 20
- Weak phrases: 3
- Regressed: 0
- Readiness score: 85

Current eval (Week 4):
- Active phrases: 18 (-2)
- Weak phrases: 5 (+2)
- Regressed: 3
- Readiness score: 72

Result: -13 points, regression detected
Next week: Focus on regressed phrases
```

## Eval Cases

### Test 1: Detects improvement
**Input:** Week 1 → Week 2 with practice
**Expected:** Readiness score increases
**Pass criteria:** Score reflects actual improvement

### Test 2: Detects regression
**Input:** Week with no practice
**Expected:** Some regression detected
**Pass criteria:** Regressed phrases identified

### Test 3: Provides useful recommendations
**Input:** Weekly eval completed
**Expected:** Specific next week plan
**Pass criteria:** Plan targets actual weaknesses

## Risks and Limitations

- Benchmark scenarios may not cover all domains
- User may have good/bad day affecting results
- May not capture long-term retention
- Regression may be temporary
- Readiness score is heuristic

## Related Skills

- **activation-scorer** — Provides phrase scores
- **weak-phrase-replayer** — Uses weak phrases from eval
- **voice-drill-builder** — Builds recommended drills
