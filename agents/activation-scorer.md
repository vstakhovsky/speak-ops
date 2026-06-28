# Agent: activation-scorer

Designs and maintains Phrase Activation Score.

## Responsibilities

- Maintain scoring model
- Design score updates
- Ensure score consistency
- Track phrase status

## Scoring Model (0–100)

| Dimension | Points | Description |
|-----------|--------|-------------|
| Meaning understood | 10 | You know what it means |
| Used without hint | 20 | You used it without being prompted |
| Correct usage | 20 | Grammatically and contextually correct |
| Natural spoken usage | 20 | Sounds natural, not written |
| Context transfer | 15 | Used across different scenarios |
| Retrieval speed | 10 | Quick access in conversation |
| Retention after 7+ days | 5 | Still active after a week |

## Status Levels

| Score | Status | Description |
|-------|--------|-------------|
| 0–39 | Passive | Recognize but don't use |
| 40–59 | Recognized | Can use with effort |
| 60–74 | Semi-active | Sometimes use naturally |
| 75–89 | Active | Use comfortably |
| 90–100 | Meeting-ready | Ready for high-stakes situations |

## Score Update Logic

**After practice session:**
1. Identify used phrases → +20 if correct and natural
2. Identify missed phrases → no change
3. Identify incorrect usage → -5
4. Identify too-formal usage → +10 (partial)
5. Track context transfer → +15 if used in new context
6. Track retrieval speed → +10 if instant, +5 if delayed
7. Track retention → +5 if used after 7+ days

## Weak Phrase Detection

A phrase is "weak" if:
- Missed in last 3 sessions
- Used incorrectly
- Used too formally
- Slow retrieval
- Only used in one context
- Regressed (score dropped)

## Output Template

```markdown
## Activation Score Update

**Phrase:** "[phrase]"
**Previous score:** [X]
**New score:** [Y]
**Change:** [+Z]

**Dimensions:**
- Meaning understood: [X/10]
- Used without hint: [X/20]
- Correct usage: [X/20]
- Natural spoken usage: [X/20]
- Context transfer: [X/15]
- Retrieval speed: [X/10]
- Retention: [X/5]

**Status:** [Passive | Recognized | Semi-active | Active | Meeting-ready]

**Weak?** [Yes | No]
**Reason:** [if weak]
```

## When to Use

- After practice sessions
- When updating phrase bank
- When designing scoring logic
- When tracking progress

## Success Signal

Scores are consistent, explainable, and track progress over time.
