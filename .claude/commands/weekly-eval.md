# Weekly Eval

**Purpose:** Run benchmark scenarios every week to track progress and identify regressions.

## When to Use

- 7+ days since last weekly eval
- Before high-stakes events (interviews, presentations)
- To assess overall readiness
- When planning practice focus for next week

## Inputs

```bash
/weekly-eval

# Optional: With previous week comparison
/weekly-eval --compare-week 4
```

## Benchmark Scenarios

Weekly eval consists of 4 fixed benchmark scenarios:

### 1. Senior PM Interview Question
**Scenario:** Tell me about a time you managed a difficult stakeholder relationship.
**Domain:** stakeholder-conflict
**Target phrases:** 5 phrases
**Duration:** 5 minutes

### 2. Roadmap Trade-off Meeting
**Scenario:** Discussing roadmap priorities with resource constraints.
**Domain:** prioritization
**Target phrases:** 5 phrases
**Duration:** 5 minutes

### 3. Stakeholder Pushback
**Scenario:** VP questioning your roadmap decisions.
**Domain:** stakeholder-pushback
**Target phrases:** 5 phrases
**Duration:** 5 minutes

### 4. AI/Evals Technical Discussion
**Scenario:** Discussing evaluation strategy with technical team.
**Domain:** ai-evals
**Target phrases:** 5 phrases
**Duration:** 5 minutes

## Workflow Steps

1. **Select benchmark phrases**
   - Choose 20 phrases from phrase bank
   - 5 phrases per scenario
   - Mix of difficulty levels
   - Include recently practiced phrases

2. **Generate 4 benchmark drills**
   - Create scenario-specific prompts
   - Include target phrases
   - Set scoring rubrics
   - Prepare practice logs

3. **Run benchmark sessions**
   - Complete each 5-minute drill
   - Note phrase usage
   - Record AI feedback
   - Self-assess naturalness

4. **Score all sessions**
   - Score each benchmark
   - Calculate readiness score
   - Identify active phrases added
   - Identify weak phrases remaining
   - Detect regressed phrases

5. **Compare with previous week**
   - Calculate score changes
   - Note improvements
   - Identify regressions
   - Track naturalness issues

6. **Generate weekly report**
   - Overall readiness score (0–100)
   - Active phrases added
   - Weak phrases remaining
   - Regressed phrases
   - Naturalness issues
   - Next week plan

## Output Format

```json
{
  "week_number": 5,
  "timestamp": "2025-06-28T16:00:00Z",
  "readiness_score": 78,
  "previous_score": 68,
  "change": "+10",

  "active_phrases_added": 3,
  "active_phrases": ["push back on", "loop in", "align on"],

  "weak_phrases_remaining": 8,
  "weak_phrases": ["table this", "find middle ground", "..."],

  "regressed_phrases": 2,
  "regressions": [
    {
      "phrase": "double down",
      "previous_score": 75,
      "current_score": 65,
      "change": "-10"
    }
  ],

  "naturalness_issues": 1,
  "issues": ["align on — still too formal"],

  "next_week_plan": {
    "focus_areas": ["weak phrase replay", "naturalness practice"],
    "recommended_drills": ["stakeholder-pushback", "interview-conflict"],
    "phrases_to_replay": ["table this", "find middle ground"]
  }
}
```

## Readiness Score Calculation

**Components (100 points total):**

| Component | Points | How Measured |
|-----------|--------|--------------|
| Active phrases (75+ score) | 40 | 2 points per active phrase (max 20) |
| Weak phrases remaining | -20 | -2 points per weak phrase |
| Regressed phrases | -25 | -5 points per regressed phrase |
| Naturalness issues | -15 | -3 points per issue |
| Benchmark performance | 40 | 10 points per benchmark passed |

**Status Levels:**
- **90–100:** Ready for interviews/meetings
- **75–89:** Good, keep practicing
- **60–74:** Making progress, not ready yet
- **<60:** Need more practice

## Regression Detection

**Regression indicators:**
- Readiness score dropped >5 points
- Active phrases decreased
- Weak phrases increased
- Multiple phrases regressed

**Common causes:**
- Inconsistent practice
- Long gap between sessions
- Phrase overloading
- Insufficient context transfer

## Quality Notes

⚠️ **Requirements:**
- Complete all 4 benchmarks
- Be honest about usage
- Use same scenarios each week
- Score consistently

✅ **Best Practices:**
- Same day each week
- Honest self-assessment
- Review trends over time
- Adjust practice based on results

## Related Skills

- **weekly-eval** — Core weekly eval logic
- **activation-scorer** — Scores each session
- **weak-phrase-replayer** — Uses weak phrases

## Related Evals

- **weekly-regression** — Tests for regression
- **activation-scoring** — Scoring consistency

## Example

```bash
/weekly-eval

# Output
{
  "week_number": 5,
  "timestamp": "2025-06-28T16:00:00Z",
  "readiness_score": 78,
  "previous_score": 68,
  "change": "+10",
  "active_phrases_added": 3,
  "weak_phrases_remaining": 8,
  "regressed_phrases": 2,
  "naturalness_issues": 1,
  "next_week_plan": {
    "focus_areas": ["weak phrase replay"],
    "recommended_drills": ["stakeholder-pushback"]
  }
}
```

---

**Command Version:** 1.0
**Status:** Active
