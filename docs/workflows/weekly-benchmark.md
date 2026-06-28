# Workflow 5: Weekly Benchmark Eval

## Overview

Run fixed benchmark scenarios every week to track progress, identify regressions, and plan next week's practice.

## Prerequisites

- Phrase bank with 20+ phrases
- Completed practice sessions
- 7+ days since last weekly eval

## Steps

### Step 1: Trigger Weekly Eval

```bash
/weekly-eval
```

**What happens:**
1. Weekly-eval skill checks phrase bank
2. Selects 20 benchmark phrases (5 per scenario)
3. Generates 4 benchmark scenarios
4. Creates scoring package

**Output:**
- 4 benchmark drills
- Practice log templates
- Scoring rubrics

### Step 2: Run Benchmark 1 — Senior PM Interview

**Scenario:** Tell me about a time you managed a difficult stakeholder relationship.

**Target phrases:** 5 stakeholder-conflict phrases

1. Run interview drill (5 minutes)
2. Note phrase usage
3. Note AI feedback

### Step 3: Run Benchmark 2 — Roadmap Trade-off Meeting

**Scenario:** Discussing roadmap priorities with constraints.

**Target phrases:** 5 prioritization phrases

1. Run meeting drill (5 minutes)
2. Note phrase usage
3. Note AI feedback

### Step 4: Run Benchmark 3 — Stakeholder Pushback

**Scenario:** VP questioning your roadmap decisions.

**Target phrases:** 5 pushback phrases

1. Run meeting drill (5 minutes)
2. Note phrase usage
3. Note AI feedback

### Step 5: Run Benchmark 4 — AI/Evals Technical Discussion

**Scenario:** Discussing evaluation strategy with technical team.

**Target phrases:** 5 AI/evals phrases

1. Run technical drill (5 minutes)
2. Note phrase usage
3. Note AI feedback

### Step 6: Score All Benchmarks

```bash
/score-session --summary "[all 4 sessions]"
```

**Format:**
```
Weekly Eval Benchmarks

Benchmark 1: Senior PM Interview
Used: push back on (✓), loop in (✓), align on (✓), find middle ground (✗), table this (✓)

Benchmark 2: Roadmap Trade-off
Used: prioritize (✓), trade-off (✓), defer (✗), shelve (✓), revisit (✓)

Benchmark 3: Stakeholder Pushback
Used: double down (✓), push back (✓), hold firm (✗), compromise (✓), stand ground (✗)

Benchmark 4: AI/Evals Discussion
Used: at scale (✓), latency (✓), baseline (✓), production-grade (✗), robust (✓)
```

**What happens:**
1. Activation-scorer scores all sessions
2. Calculates weekly readiness score
3. Identifies active phrases added
4. Identifies weak phrases remaining
5. Detects regressed phrases
6. Identifies naturalness issues

**Output:**
- Weekly readiness score (0–100)
- Active phrases added
- Weak phrases remaining
- Regressed phrases
- Naturalness issues
- Next week plan

### Step 7: Generate Weekly Report

```bash
/weekly-report
```

**What happens:**
1. Compiles weekly results
2. Compares with previous week
3. Generates progress report
4. Creates recommendations

**Output:**
- Weekly review report
- Progress summary
- Recommendations
- Next week plan

### Step 8: Update Decision Log

Based on weekly eval results:

**If readiness improved:**
- Document what worked
- Note effective strategies
- Plan to continue

**If readiness regressed:**
- Identify causes
- Document challenges
- Plan adjustments

**If stagnation:**
- Review practice quality
- Consider drill changes
- Assess phrase relevance

### Step 9: Plan Next Week

Based on weekly report:

```bash
/build-voice-drill --mode [mode] --scenario [scenario]
```

**Priorities:**
1. Replay weak phrases
2. Practice regressed phrases
3. Context transfer for single-context phrases
4. Naturalness practice for formal phrases

## Example: Full Weekly Eval

```bash
# Step 1: Trigger
/weekly-eval
# Output: 4 benchmark drills generated, 20 phrases selected

# Steps 2-5: Run benchmarks (20 minutes total)
# [All 4 drills completed]

# Step 6: Score
/score-session --summary "[all 4 sessions]"
# Output:
# Weekly readiness: 78/100
# Active phrases added: 3
# Weak phrases: 8
# Regressed: 2
# Naturalness issues: 1

# Step 7: Report
/weekly-report
# Output:
# Week 4 → Week 5: +12 points improvement
# Active: 18 → 21 phrases
# Weak: 12 → 8 phrases
# Regressed: 0 → 2 phrases

# Step 8-9: Plan next week
/replay-weak --count 5
# Output: Weak phrase replay drill created
```

## Benchmark Scenarios

### Benchmark 1: Senior PM Interview Question

**Scenario:** Tell me about a time you had to manage a difficult stakeholder relationship.

**Domain:** stakeholder-conflict

**Phrases tested:** 5
- push back on
- loop in
- align on
- find middle ground
- table this

**Duration:** 5 minutes

**Success criteria:**
- Use 4/5 phrases naturally
- Handle conflict appropriately
- Sound confident but diplomatic

### Benchmark 2: Roadmap Trade-off Meeting

**Scenario:** Discussing roadmap priorities with resource constraints.

**Domain:** prioritization

**Phrases tested:** 5
- prioritize / deprioritize
- trade-off
- defer / shelve
- revisit
- double down

**Duration:** 5 minutes

**Success criteria:**
- Use 4/5 phrases naturally
- Explain trade-offs clearly
- Sound decisive but flexible

### Benchmark 3: Stakeholder Pushback

**Scenario:** VP of Sales pushing for unrealistic feature/timeline.

**Domain:** stakeholder-pushback

**Phrases tested:** 5
- push back on
- hold firm
- compromise
- find middle ground
- stand ground

**Duration:** 5 minutes

**Success criteria:**
- Use 4/5 phrases naturally
- Push back appropriately
- Maintain relationship

### Benchmark 4: AI/Evals Technical Discussion

**Scenario:** Discussing evaluation strategy with technical team.

**Domain:** ai-evals

**Phrases tested:** 5
- at scale
- latency / throughput
- baseline
- production-grade
- robust

**Duration:** 5 minutes

**Success criteria:**
- Use 4/5 phrases naturally
- Sound technically competent
- Explain concepts clearly

## Readiness Score Calculation

**Components (100 points total):**

| Component | Points | How measured |
|-----------|--------|--------------|
| Active phrases (75+ score) | 40 | 2 points per active phrase (max 20) |
| Weak phrases remaining | -20 | -2 points per weak phrase (max -10) |
| Regressed phrases | -25 | -5 points per regressed phrase |
| Naturalness issues | -15 | -3 points per issue (max -5) |
| Benchmark performance | 40 | 10 points per benchmark passed |

**Status levels:**
- 90–100: Ready for interviews/meetings
- 75–89: Good, keep practicing
- 60–74: Making progress, not ready yet
- <60: Need more practice

## Weekly Report Sections

1. **Overall Progress**
   - This week vs last week
   - Readiness score change
   - Active phrase count
   - Weak phrase count

2. **Active Phrases Added**
   - New phrases that reached 75+ score
   - What made the difference

3. **Weak Phrases Remaining**
   - Phrases still below 60 score
   - Why they're weak
   - How to address

4. **Regressed Phrases**
   - Phrases that dropped in score
   - Possible causes
   - Recovery plan

5. **Naturalness Issues**
   - Phrases still sounding formal
   - Better spoken versions
   - Practice recommendations

6. **Next Week Plan**
   - Focus areas
   - Recommended drills
   - Phrases to replay

## Regression Detection

**Regression indicators:**
- Readiness score dropped >5 points
- Active phrases decreased
- Weak phrases increased
- Multiple phrases regressed

**Common causes:**
- Inconsistent practice
- Long gap between sessions
- Phrase overloading (too many at once)
- Insufficient context transfer
- Naturalness not addressed

**Recovery strategies:**
- Increase practice frequency
- Reduce phrase count per session
- Focus on context transfer
- Prioritize naturalness over correctness

## Time Estimate

- Step 1: 2 minutes (automated)
- Steps 2–5: 20 minutes (4 × 5-minute drills)
- Step 6: 3 minutes (scoring automated)
- Step 7: 2 minutes (report automated)
- Steps 8–9: 3 minutes (planning)

**Total:** 30 minutes

## Best Practices

1. **Same time each week** — Consistent schedule
2. **Same scenarios** — Enables comparison
3. **Honest scoring** — Don't inflate usage
4. **Review trends** — Look at multi-week patterns
5. **Adjust based on data** — Let results guide practice

## Next Steps

After weekly eval:

1. **Review report** — Understand progress
2. **Identify focus areas** — Prioritize next week
3. **Schedule next week** — Set practice schedule
4. **Update phrase bank** — Ensure scores current
5. **Document decisions** — Note in decision log

---

**Workflow ID:** weekly-benchmark
**Status:** Active
