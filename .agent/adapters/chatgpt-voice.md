# ChatGPT Voice Adapter

## Purpose

Define how SpeakOps integrates with ChatGPT Voice for practice sessions.

## Overview

SpeakOps generates prompts for ChatGPT Voice but does not run the conversation itself.

## Integration Pattern

### 1. Drill Generation

SpeakOps generates:
- ChatGPT Voice prompt
- Practice log template
- Scoring rubric

### 2. User Action

User:
1. Copies prompt from SpeakOps
2. Pastes into ChatGPT Voice
3. Runs voice session
4. Returns with summary

### 3. Scoring

SpeakOps:
1. Receives session summary
2. Scores phrase usage
3. Updates activation scores
4. Identifies weak phrases

## Prompt Format

### Standard Voice Drill Prompt

```markdown
You are [role]. I am [user role].

**Scenario:** [scenario description]

**Target phrases I need to use:**
- [phrase 1]
- [phrase 2]
- [phrase 3]
...

**Conversation rules:**
1. Keep your turns short (2–3 sentences max)
2. Create natural situations where I would use the target phrases
3. If I don't use a target phrase within 1–2 minutes, gently steer the conversation that way
4. Correct ONLY major mistakes (grammar, clearly wrong usage)
5. If I make a major mistake:
   - Stop me gently
   - Give me a better spoken version
   - Ask me to repeat the better version aloud
6. Don't correct minor differences in phrasing
7. After [duration] minutes, end with:
   - Which phrases I used well
   - Which phrases I missed or used incorrectly
   - Specific feedback on naturalness

**Start the conversation now.**
```

## Session Flow

### Step 1: Generate Drill

In SpeakOps/Claude Code:

```bash
/build-voice-drill --mode meeting --scenario stakeholder-pushback
```

**Output:**
- ChatGPT Voice prompt
- Target phrases listed
- Practice log template

### Step 2: Copy to ChatGPT Voice

1. Copy the prompt
2. Open ChatGPT Voice
3. Paste prompt
4. Start voice session

### Step 3: Run Session

- Speak naturally
- Try to use target phrases
- Respond to AI feedback
- Repeat improved versions if asked

### Step 4: Note Summary

After session, note:
- Which phrases you used
- How natural they felt
- AI feedback received
- Any phrases you missed

### Step 5: Score Session

In SpeakOps/Claude Code:

```bash
/score-session --summary "[session summary]"
```

## Prompt Quality

### Good Prompt Characteristics

1. **Clear role definition** — Who is AI, who is user
2. **Specific scenario** — Realistic situation
3. **Target phrases listed** — What to use
4. **Short turns specified** — Keep AI concise
5. **Correction guidance** — How to handle mistakes
6. **Feedback format** — What AI should report

### Poor Prompt Characteristics

1. **Vague scenario** — Unclear situation
2. **No phrase forcing** — Phrases may not come up
3. **Long AI turns** — AI talks too much
4. **No correction guidance** — Unclear how to handle errors
5. **No feedback format** — Unclear what to report

## Prompt Templates

### Interview Prompt Template

```markdown
You are a Senior PM interviewer. I am a candidate.

**Scenario:** Tell me about a time you had to handle a difficult stakeholder relationship.

**Target phrases:**
- push back on
- loop in
- align on
- find middle ground
- table this

[Standard rules]

Start the interview now.
```

### Meeting Prompt Template

```markdown
You are the VP of Sales. I am a PM.

**Scenario:** You're pushing for a feature that Engineering says is too complex. We're in a meeting to discuss this.

**Target phrases:**
- push back on
- double down
- table this
- revisit
- align on

[Standard rules]

Start by pushing hard for the feature.
```

### Technical Discussion Prompt Template

```markdown
You are a Staff Engineer. I am a Technical PM.

**Scenario:** Discussing evaluation strategy for a new AI system.

**Target phrases:**
- at scale
- latency vs accuracy
- baseline
- production-grade
- robust

[Standard rules]

Start by asking about my evaluation approach.
```

## Best Practices

### For Prompt Generation

1. **Keep scenarios realistic** — Real meetings/interviews
2. **Force phrase usage** — Natural opportunities
3. **Keep AI turns short** — 2–3 sentences max
4. **Specify corrections** — What to fix
5. **Request feedback** — End with summary

### For Session Practice

1. **Speak naturally** — Don't force phrases
2. **Listen to AI** — Take feedback seriously
3. **Repeat improvements** — Say better versions aloud
4. **Note struggles** — Which phrases were hard
5. **Be honest** — Don't inflate usage

### For Scoring

1. **Be honest** — Don't claim usage you didn't do
2. **Note formality** — Acknowledge if you sounded formal
3. **Listen to AI feedback** — It's usually right
4. **Note context** — Was usage natural?
5. **Track retrieval** — Did you hesitate?

## Limitations

### ChatGPT Voice Limitations

1. **Not perfect instruction following** — May talk too long
2. **May miss phrases** — Might not notice usage
3. **May over-correct** — Could be too picky
4. **May under-correct** — Could miss major errors

### Workarounds

1. **Repeat prompt** — If AI goes off track
2. **Refocus** — Gently redirect conversation
3. **Self-monitor** — Note your own usage
4. **Record summary** — Don't rely on AI memory

## Future Enhancements

**Potential additions:**
- Direct API integration (if available)
- Real-time transcript capture
- Automatic phrase detection
- Scoring integration

## Examples

### Example 1: Good Session

**Prompt:** Well-structured stakeholder pushback drill
**Session:** Natural conversation, phrases used appropriately
**AI Feedback:** "Great use of 'push back on' — sounded natural. 'Loop in' was a bit forced but correct."
**Summary:** Honest assessment of usage

### Example 2: Poor Session

**Prompt:** Vague scenario, no phrase forcing
**Session:** AI talks too much, phrases never come up
**AI Feedback:** Generic, no specific feedback
**Summary:** "Phrases didn't come up naturally"

---

**Adapter Version:** 1.0
**Status:** Active
