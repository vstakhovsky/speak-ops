# Voice Drill Conventions

**Purpose:** Define how to build high-quality ChatGPT Voice prompts for practice.

## Drill Requirements

Every voice drill must:

1. **Use 5–8 target phrases** — Not too many, not too few
2. **Create realistic scenario** — IT/Product/AI context
3. **Keep AI turns short** — 2–3 sentences max
4. **Force phrase usage** — Natural opportunities for phrases
5. **Correct major mistakes** — Only high-impact errors
6. **Give better spoken version** — Natural alternative
7. **Ask user to repeat** — Reinforce improvement
8. **End with feedback** — Phrase-level summary

## Prompt Structure

### Standard Format

```markdown
You are [AI role]. I am [user role].

**Scenario:** [realistic situation]

**Target phrases I need to use:**
- [phrase 1]
- [phrase 2]
- [phrase 3]
- [phrase 4]
- [phrase 5]

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

## Scenario Design

### Realistic Scenarios ✅

**Interview:**
- "Tell me about a time you handled a difficult stakeholder"
- "Describe a situation where you had to push back on a request"
- "Walk me through a trade-off decision you made"

**Meeting:**
- "VP of Sales pushing for unrealistic timeline"
- "Roadmap review with constrained resources"
- "Technical design discussion with engineering"

**AI/Evals:**
- "Discussing evaluation strategy with technical team"
- "Explaining trade-offs between latency and accuracy"
- "Presenting model behavior to CTO"

### Unrealistic Scenarios ❌

**Too vague:**
- "Talk about business"
- "Have a general conversation"

**Too extreme:**
- "Aliens are attacking, what do you do?"
- "You're the President, decide on world peace"

**Too simple:**
- "Say these phrases one by one"
- "Repeat after me"

## Phrase Selection

### Balanced Selection

Choose 5–8 phrases that:

1. **Mix difficulty levels** — Some active, some semi-active
2. **Fit the scenario** — Natural for the context
3. **Cover different aspects** — Not all the same type
4. **Create variety** — Different moments to use them

### Example Selection

**Stakeholder Pushback Drill:**
- push back on (managing disagreement)
- loop in (involving others)
- align on (reaching agreement)
- table this (postponing discussion)
- find middle ground (compromising)

**Good mix:**
- 2 phrases for direct pushback
- 2 phrases for collaboration
- 1 phrase for compromise

## Turn Length

### AI Turns

**Ideal:** 2–3 sentences

✅ **Good:**
```
"I hear your concerns about the timeline. But given the technical complexity, can we discuss a more realistic date?"
```

❌ **Too Long:**
```
```
"I completely understand your perspective regarding the timeline constraints. However, given the current technical complexity and the resource limitations we are facing, I believe it would be prudent to engage in a detailed discussion about establishing a more realistic and achievable target date that takes into account all the various factors involved."
```

### User Turns

Let user speak naturally. Don't interrupt unless:
- Major grammatical error
- Clearly wrong usage
- Very formal phrasing (can improve)

## Correction Guidelines

### When to Correct

**Correct major mistakes:**
- Wrong meaning (phrase used incorrectly)
- Wrong grammar (clearly wrong)
- Too formal (sounds written)
- Awkward phrasing (unnatural)

**Don't correct:**
- Minor phrasing differences
- Slight hesitation
- Accent/pronunciation (unless unintelligible)
- Personal speaking style

### How to Correct

✅ **Good correction:**
```
"You used 'align ourselves on' — that's a bit formal. A more natural way to say this would be 'align on'. Can you try saying that again with 'align on'?"
```

❌ **Bad correction:**
```
"That was wrong. Say it like this: 'align on'."
```

## Ending the Drill

### Required Feedback

Every drill must end with:

1. **Phrases used well** — What went right
2. **Phrases missed** — What wasn't used
3. **Incorrect usage** — What was wrong
4. **Naturalness feedback** — How to sound more natural

### Example Ending

```
"Great job overall! You used 'push back on' and 'loop in' very naturally — those sounded confident and appropriate.

You missed 'table this' and 'find middle ground', but that's okay for this session.

One thing to work on: 'align on' sounded a little formal. Next time, try just 'align on' instead of 'align ourselves on' — it's more direct and natural.

Overall, you're getting better at using these phrases in context. Keep practicing!"
```

## Duration Guidelines

### Recommended Duration

- **Short drill:** 3–5 minutes (1–2 phrases)
- **Standard drill:** 5–7 minutes (3–5 phrases)
- **Long drill:** 7–10 minutes (6–8 phrases)

### Time by Phrase

Roughly **1 minute per phrase**:
- 30 seconds: Natural conversation
- 20 seconds: Phrase opportunity
- 10 seconds: Feedback/transition

## Quality Checklist

Before finalizing a drill:

### ✅ Structure
- [ ] 5–8 target phrases
- [ ] Realistic scenario
- [ ] Clear roles defined
- [ ] Conversation rules specified

### ✅ Content
- [ ] Phrases fit scenario naturally
- [ ] AI turns are short (2–3 sentences)
- [ ] Correction guidance is clear
- [ ] Feedback requirement specified

### ✅ Quality
- [ ] Scenario is realistic
- [ ] Phrases are spread throughout
- [ ] Natural language (no AI-like phrasing)
- [ ] Appropriate difficulty level

## Common Mistakes

### Mistake 1: Too Many Phrases

❌ **Bad:** 10–15 phrases
- Overwhelming
- Hard to force naturally
- Shallow practice

✅ **Good:** 5–8 phrases
- Focused
- Deep practice
- Quality over quantity

### Mistake 2: Unrealistic Scenario

❌ **Bad:** Generic or extreme scenarios
- Don't prepare user for real situations

✅ **Good:** Realistic workplace scenarios
- Direct transfer to real meetings

### Mistake 3: Long AI Turns

❌ **Bad:** AI talks too much
- Dominates conversation
- User can't practice

✅ **Good:** AI turns are short
- User speaks most
- Practice-focused

### Mistake 4: No Feedback

❌ **Bad:** Drill ends abruptly
- No learning
- No improvement

✅ **Good:** Drill ends with feedback
- Learning happens
- Clear next steps

## Template Usage

Always use templates as starting point:
- `templates/chatgpt-voice-prompt.md`
- Adjust for specific scenario
- Keep core structure
- Customize content

---

**Convention Version:** 1.0
**Purpose:** Ensure consistent, high-quality voice drills
