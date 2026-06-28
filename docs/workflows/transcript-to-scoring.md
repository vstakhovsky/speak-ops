# Workflow 4: Voice Session Transcript to Scoring

## Overview

Process a voice practice transcript or summary, score phrase usage, and update activation scores.

## Prerequisites

- Completed voice practice session
- Transcript or session summary
- Target phrases known

## Steps

### Step 1: Prepare Transcript/Summary

**Option A: Full transcript**

If you have a full transcript:

1. Save transcript to file
2. Ensure text format

**Option B: Session summary**

If using summary format:

1. List phrases used
2. Note correctness and naturalness
3. Note missed phrases
4. Note any issues

### Step 2: Score Session

**With transcript file:**
```bash
/score-session --transcript /tmp/session_transcript.txt
```

**With summary:**
```bash
/score-session --summary "[summary text]"
```

**Example summary:**
```
Session: Stakeholder pushback drill
Target phrases: 8

Used phrases:
- push back on: Yes, correct, natural, instant
- loop in: Yes, correct, natural, slight delay
- align on: Yes, correct but too formal ("align ourselves on")
- move forward: Yes, correct, natural
- table this: No
- find middle ground: Yes, correct, natural
- double down: No
- revisit: Yes, correct but hesitant

Overall: Felt natural on some, formal on "align on", hesitated on "revisit"
```

**What happens:**
1. Activation-scorer analyzes transcript/summary
2. Identifies used, missed, incorrect phrases
3. Scores each phrase (0–100)
4. Calculates score updates
5. Identifies weak phrases

**Output:**
- Session scoring report
- Updated activation scores
- Weak phrase list
- Feedback summary

### Step 3: Review Score Report

**Report sections:**

1. **Session Summary**
   - Phrases used: X/Y
   - Phrases correct: X/Y
   - Phrases natural: X/Y

2. **Score Updates**
   - Each phrase: previous → new score
   - Score change breakdown

3. **Weak Phrases**
   - Missed phrases
   - Incorrect usage
   - Too formal usage
   - Slow retrieval

4. **Feedback**
   - What went well
   - What needs work
   - Better spoken versions

### Step 4: Update Phrase Bank

```bash
/update-phrase-bank
```

**What happens:**
1. Updates phrases.csv with new scores
2. Updates status levels
3. Saves session to sessions.jsonl
4. Saves weak phrases to weak_phrases.jsonl

**Output:**
- Updated phrase bank
- Session log
- Weak phrases identified

### Step 5: Plan Next Session

Based on scoring report:

**If weak phrases identified:**
```bash
/replay-weak --count 5
```

**If scores good:**
```bash
/build-voice-drill --mode [mode] --session [next]
```

**If regression detected:**
```bash
/weekly-eval
```

## Example: Full Workflow

**Session:** Interview practice, "tell me about yourself"

```bash
# Step 1-2: Score session
/score-session --summary "
Used: worked on (natural), led the team (natural), responsible for (too formal)
Missed: spearheaded, drove the initiative
Too formal: tasked with → better: handled
"

# Output:
# Session Summary
# Phrases used: 3/5
# Phrases correct: 3/3
# Phrases natural: 2/3
#
# Score Updates
# worked on: 50 → 70 (+20)
# led the team: 60 → 80 (+20)
# responsible for: 45 → 55 (+10, formal penalty)
#
# Weak Phrases
# - spearheaded (missed)
# - drove the initiative (missed)

# Step 3-4: Review and update
/update-phrase-bank
# Output: Updated 3 phrases, 2 weak phrases identified

# Step 5: Plan next session
/replay-weak --count 2
# Output: Weak phrase replay drill created
```

## Transcript Format

**Good format (plain text):**
```
[Interviewer]
Tell me about a time you had to handle a difficult stakeholder situation.

[Me]
Sure. So I was working on this product launch and the VP of Sales wanted to add this feature at the last minute. I had to push back on the timeline because Engineering was already at capacity. I looped in my manager and we aligned on pushing the feature to the next release instead.

[Interviewer]
How did that go over?

[Me]
Actually pretty well. I found middle ground where we'd do a quick MVP for the sales demo but wouldn't commit to the full feature. We tabled the discussion until after launch.
```

**Summary format (structured):**
```
Session: Stakeholder conflict
Target phrases: push back on, loop in, align on, find middle ground, table this

Usage:
- push back on: ✓ Correct, natural, instant
- loop in: ✓ Correct, natural, slight delay
- align on: ✓ Correct but formal ("align ourselves on")
- find middle ground: ✓ Correct, natural
- table this: ✗ Missed

Self-reflection: Felt natural on most, "align on" sounded too formal, forgot to use "table this" when I had the chance.
```

## Scoring Dimensions

**How scoring works:**

| Dimension | Points | How it's measured |
|-----------|--------|------------------|
| Used without hint | 20 | Phrase used without AI prompting |
| Correct usage | 20 | Grammatically and contextually correct |
| Natural spoken usage | 20 | Sounds natural, not written |
| Retrieval speed | 10 | Instant (10), delayed (5), struggled (0) |
| Context transfer | 15 | Used in new context (15), same context (0) |
| Retention | 5 | Used after 7+ days (5), otherwise (0) |

**Status levels:**
- 0–39: Passive
- 40–59: Recognized
- 60–74: Semi-active
- 75–89: Active
- 90–100: Meeting-ready

## Weak Phrase Types

A phrase is flagged as weak if:

1. **Missed** — Targeted but not used
2. **Incorrect** — Used with wrong meaning/grammar
3. **Too formal** — Used in written style
4. **Too slow** — Hesitated or struggled
5. **Single context** — Only ever used in one scenario
6. **Regressed** — Score dropped from previous

## Privacy Notes

- Transcripts processed locally
- No external transmission
- User controls transcript storage
- Summary format preferred for privacy
- Full transcripts optional

## Time Estimate

- Step 1: 2 minutes (prepare transcript/summary)
- Step 2: 3 minutes (scoring automated)
- Step 3: 2 minutes (review report)
- Step 4: 1 minute (update automated)
- Step 5: 2 minutes (plan next session)

**Total:** 10 minutes

## Next Steps

After scoring:

1. **Review weak phrases** — Identify what needs practice
2. **Schedule replay** — Plan weak phrase drill
3. **Track progress** — Monitor activation trends
4. **Plan next drill** — Choose appropriate scenario

## Troubleshooting

**Problem:** Scores don't update
- **Solution:** Check phrase names match exactly

**Problem:** Incorrect scoring
- **Solution:** Provide clearer summary with correctness notes

**Problem:** Too many weak phrases
- **Solution:** Focus on 5–8 per session, prioritize

**Problem:** Regression detected
- **Solution:** Run `/weekly-eval` to check overall progress

---

**Workflow ID:** transcript-to-scoring
**Status:** Active
