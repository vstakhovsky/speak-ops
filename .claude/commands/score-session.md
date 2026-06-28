# Score Session

**Purpose:** Score phrase usage from a voice practice session and update activation scores.

## When to Use

- After completing a voice drill
- After any practice session
- To track progress over time
- Before planning next practice session

## Inputs

```bash
# With transcript file
/score-session --transcript /tmp/session.txt

# With session summary
/score-session --summary "[summary text]"

# Example summary
/score-session --summary "
Session: Stakeholder pushback drill
Used: push back on (✓ natural), loop in (✓ correct), align on (✓ too formal)
Missed: table this, find middle ground
Too formal: align ourselves on → better: align on
"
```

## Summary Format

Provide a clear, structured summary:

```text
Session: [drill name]

Used phrases:
- phrase name: [✓/✗] [correct/incorrect] [natural/formal] [instant/slow]

Missed phrases:
- phrase 1
- phrase 2

Too formal usage:
- phrase: formal version → better spoken version

Self-reflection:
[What felt natural, what felt forced]
```

## Workflow Steps

1. **Parse session data**
   - Identify used phrases
   - Identify missed phrases
   - Note incorrect usage
   - Note too-formal usage
   - Assess retrieval speed

2. **Score each phrase**
   - Meaning understood: 10 points (base)
   - Used without hint: ±20 points
   - Correct usage: ±20 points
   - Natural spoken usage: ±20 points
   - Retrieval speed: ±10 points
   - Context transfer: ±15 points
   - Retention bonus: ±5 points

3. **Calculate score updates**
   - Previous score + earned points
   - Cap at 100
   - Update status level
   - Flag regression if score dropped

4. **Identify weak phrases**
   - Missed phrases
   - Incorrect usage
   - Too formal usage
   - Slow retrieval
   - Single context only

5. **Generate scoring report**
   - Session summary
   - Score updates per phrase
   - Weak phrase list
   - Next session recommendations

## Output Format

```json
{
  "timestamp": "2025-06-28T15:30:00Z",
  "session_type": "stakeholder-pushback",
  "total_phrases_targeted": 8,
  "used_phrases": 5,
  "missed_phrases": 3,
  "score_updates": {
    "push back on": {
      "previous_score": 60,
      "new_score": 80,
      "change": "+20",
      "dimensions": {
        "used_without_hint": 20,
        "correct_usage": 20,
        "natural_spoken_usage": 20
      }
    }
  },
  "weak_phrases": ["table this", "find middle ground"],
  "recommendations": "Replay weak phrases in new context"
}
```

## Scoring Rubric

| Dimension | Points | How to Assess |
|-----------|--------|---------------|
| Used without hint | +20 | Phrase used without AI prompting |
| Used with hint | +10 | Phrase used after prompting |
| Correct usage | +20 | Grammatically and contextually correct |
| Incorrect usage | +0 | Wrong meaning or grammar |
| Natural spoken usage | +20 | Sounds natural, not written |
| Too formal | +10 | Correct but formal style |
| Instant retrieval | +10 | Used immediately |
| Delayed retrieval | +5 | Used after hesitation |
| Struggled | +0 | Had significant difficulty |
| New context | +15 | Used in different scenario type |
| Same context | +0 | Used in similar scenario |
| Retention (7+ days) | +5 | Used after a week |

## Status Levels

| Score Range | Status | Description |
|-------------|--------|-------------|
| 0–39 | Passive | Recognize but don't use |
| 40–59 | Recognized | Can use with effort |
| 60–74 | Semi-active | Sometimes use naturally |
| 75–89 | Active | Use comfortably |
| 90–100 | Meeting-ready | Ready for high-stakes situations |

## Weak Phrase Detection

A phrase is flagged as weak if:

- ❌ Missed in session (targeted but not used)
- ❌ Used incorrectly (wrong meaning/grammar)
- ❌ Used too formally (written style)
- ❌ Slow retrieval (hesitated or struggled)
- ❌ Single context (only used in one scenario type)
- ❌ Regressed (score dropped from previous)

## Safety & Privacy Notes

⚠️ **Privacy:**
- Summaries preferred over full transcripts
- Full transcripts not stored by default
- User must opt-in to save transcripts
- Local processing only

✅ **Best Practices:**
- Be honest about usage
- Note formality issues
- Acknowledge missed phrases
- Include self-reflection

## Related Skills

- **activation-scorer** — Core scoring logic
- **weak-phrase-replayer** — Uses weak phrase list
- **weekly-eval** — Tracks score trends

## Related Evals

- **activation-scoring** — Tests scoring consistency
- **weekly-regression** — Detects score regression

## Example

```bash
/score-session --summary "
Session: Stakeholder pushback
Used: push back on (✓, ✓, ✓, instant), loop in (✓, ✓, ✓, slight delay)
Missed: table this, find middle ground
Too formal: align ourselves on → better: align on
Self-reflection: Felt natural on most, 'align on' sounded stiff
"

# Output
{
  "timestamp": "2025-06-28T15:30:00Z",
  "session_type": "stakeholder-pushback",
  "total_phrases_targeted": 5,
  "used_phrases": 3,
  "missed_phrases": 2,
  "score_updates": {
    "push back on": {"previous_score": 60, "new_score": 80, "change": "+20"},
    "loop in": {"previous_score": 70, "new_score": 85, "change": "+15"}
  },
  "weak_phrases": ["table this", "find middle ground", "align on"]
}
```

---

**Command Version:** 1.0
**Status:** Active
