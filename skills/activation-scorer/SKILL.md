# activation-scorer

Scores phrase activation from practice transcripts.

## Trigger Conditions

User runs:
```bash
/score-session --transcript <file>
```

Or when:
- Processing practice session summary
- Updating phrase bank after practice
- Running weekly eval
- Tracking progress over time

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| transcript | string | Practice transcript or summary |
| previous_scores | dict | Previous activation scores |
| target_phrases | list | Phrases targeted in session |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| used_phrases | list | Phrases used in session |
| missed_phrases | list | Target phrases not used |
| incorrect_phrases | list | Phrases used incorrectly |
| too_formal_phrases | list | Phrases used too formally |
| improved_versions | dict | Better spoken versions |
| updated_scores | dict | New activation scores |
| weak_phrases | list | Phrases needing replay |

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

## Score Update Logic

**After practice session:**

1. **Identify used phrases**
   - Found in transcript → Continue evaluation
   - Not found → Mark as missed, no score change

2. **Evaluate used phrases**
   - Correct and natural → +20 (used without hint) +20 (correct) +20 (natural)
   - Correct but formal → +20 (used without hint) +20 (correct) +10 (partial naturalness)
   - Incorrect usage → +20 (used without hint) +0 (incorrect) +0 (not natural)
   - Used with hint → +10 (with hint) + [score for correctness]

3. **Check retrieval speed**
   - Instant usage → +10
   - Delayed usage → +5
   - Struggled → +0

4. **Check context transfer**
   - Used in new context → +15
   - Used in same context → +0

5. **Check retention**
   - Used after 7+ days since last use → +5

## Status Levels

| Score | Status | Description |
|-------|--------|-------------|
| 0–39 | Passive | Recognize but don't use |
| 40–59 | Recognized | Can use with effort |
| 60–74 | Semi-active | Sometimes use naturally |
| 75–89 | Active | Use comfortably |
| 90–100 | Meeting-ready | Ready for high-stakes situations |

## Weak Phrase Detection

A phrase is "weak" if:
- Missed in last 3 sessions
- Used incorrectly
- Used too formally
- Slow retrieval
- Only used in one context
- Regressed (score dropped)

## Workflow

1. **Parse transcript** — Extract used phrases
2. **Compare with targets** — Identify missed phrases
3. **Evaluate usage** — Score correctness and naturalness
4. **Check retrieval speed** — Assess how quickly phrases were accessed
5. **Check context** — Determine if new context
6. **Check retention** — See if retention bonus applies
7. **Update scores** — Calculate new activation scores
8. **Identify weak phrases** — Find phrases needing replay
9. **Generate report** — Output scoring summary

## Examples

### Example 1: Perfect usage
```
Phrase: "push back on"
Previous score: 50
Used: Yes, correctly, naturally, instantly
New score: 50 + 20 (used) + 20 (correct) + 20 (natural) + 10 (speed) = 120 → 100 (max)
Status: Meeting-ready
```

### Example 2: Incorrect usage
```
Phrase: "loop in"
Previous score: 60
Used: Yes, but incorrectly (wrong preposition)
New score: 60 + 20 (used) + 0 (incorrect) + 0 (not natural) = 80
Status: Active
Weak: Yes (incorrect usage)
```

### Example 3: Missed phrase
```
Phrase: "align on"
Previous score: 45
Used: No
New score: 45 (no change)
Status: Recognized
Weak: Yes (missed)
```

## Eval Cases

### Test 1: Score correct usage
**Input:** Transcript with correct phrase usage
**Expected:** Score increases appropriately
**Pass criteria:** Score reflects correct + natural usage

### Test 2: Detect incorrect usage
**Input:** Transcript with incorrect phrase usage
**Expected:** Identify as incorrect, penalize appropriately
**Pass criteria:** Incorrect usage flagged and scored lower

### Test 3: Identify weak phrases
**Input:** Session with missed/mistaken phrases
**Expected:** Generate weak phrase list
**Pass criteria:** All weak phrases identified

## Risks and Limitations

- Subjective assessment of "natural"
- Depends on transcript quality
- May not capture retrieval speed accurately
- Context transfer detection is heuristic
- Retention tracking requires historical data

## Related Skills

- **voice-drill-builder** — Provides target phrases
- **weak-phrase-replayer** — Uses weak phrase list
- **weekly-eval** — Uses score trends
