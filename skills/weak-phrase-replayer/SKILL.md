# weak-phrase-replayer

Takes weak phrases from previous sessions and forces them into new contexts.

## Trigger Conditions

User runs:
```bash
/replay-weak --count <n>
```

Or when:
- Weekly review identifies weak phrases
- After scoring session with mistakes
- Building targeted practice drills

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| weak_phrases | list | Phrases flagged as weak |
| count | number | Number of phrases to replay (5–8) |
| previous_contexts | list | Contexts where phrases were weak |
| user_level | string | b1, b2, c1, c2 |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| selected_phrases | list | Phrases selected for replay |
| new_contexts | list | New contexts for each phrase |
| scenario | string | Replay scenario description |
| chatgpt_prompt | string | Ready-to-paste prompt |

## Weak Phrase Types

A phrase is "weak" if:

1. **Missed** — Not used in session when targeted
2. **Avoided** — User used alternative phrasing
3. **Used incorrectly** — Grammatically or contextually wrong
4. **Too formal** — Used written-style instead of spoken
5. **Too slow** — Hesitated or struggled to retrieve
6. **Single context** — Only ever used in one context

## Replay Strategy

**Context Transfer:**
- If phrase was weak in interview → Put in meeting scenario
- If phrase was weak in meeting → Put in interview scenario
- If phrase was weak in technical → Put in stakeholder scenario
- If phrase was weak in formal → Put in casual scenario

**Scaffolding:**
- First replay: Provide hint/context
- Second replay: No hint, natural situation
- Third replay: High-pressure situation

## Workflow

1. **Get weak phrases** — Load from weak_phrases.jsonl
2. **Select phrases** — Choose 5–8 for replay
3. **Analyze weakness** — Why was phrase weak?
4. **Choose new contexts** — Different from previous contexts
5. **Design scenario** — Force usage in new context
6. **Create ChatGPT prompt** — Replay simulation
7. **Track replays** — Log replay attempts and outcomes
8. **Output drill** — Complete replay drill

## Examples

### Example 1: Missed phrase replay
```
Phrase: "push back on"
Weakness: Missed in last 3 sessions
Previous context: Interview question
New context: Stakeholder meeting

Scenario: "VP of Sales is pushing for an unrealistic deadline. You need to push back."

ChatGPT Prompt:
"You are the VP of Sales. I'm the PM.

Start: 'We need this feature by next week. Can you make it happen?'

Conduct a 5-minute meeting where you:
- Push hard on the timeline
- Create situations where I NEED to say 'push back on'
- If I don't use it within 2 minutes, give me a hint: 'How do you feel about this timeline?'
- Keep your turns short

After I use 'push back on':
- Acknowledge it
- Continue the conversation naturally
- End with feedback on whether I used it well"
```

### Example 2: Incorrect usage replay
```
Phrase: "loop in"
Weakness: Used incorrectly ("loop in with")
Previous context: Casual meeting
New context: Technical discussion

Scenario: "Engineering needs to be involved in a decision."

ChatGPT Prompt:
[Prompt text with focus on correct preposition usage]
```

### Example 3: Too formal replay
```
Phrase: "align on"
Weakness: Used "we should align ourselves on" (too formal)
Previous context: Team meeting
New context: Casual sync

Scenario: "Quick sync about next steps."

ChatGPT Prompt:
[Prompt text with focus on short, natural usage]
```

## Eval Cases

### Test 1: Selects appropriate weak phrases
**Input:** 20 weak phrases
**Expected:** Selects 5–8 most critical
**Pass criteria:** Prioritizes frequently missed or incorrectly used

### Test 2: Creates new context
**Input:** Phrase weak in interview context
**Expected:** New context is different (meeting, casual, etc.)
**Pass criteria:** Context is meaningfully different

### Test 3: Forces phrase usage
**Input:** Replay drill
**Expected:** Prompt creates natural but clear opportunity
**Pass criteria:** Phrase has natural usage moment

## Risks and Limitations

- May create forced scenarios
- May not transfer context appropriately
- User may still avoid phrase
- New context may be unnatural
- May not address root cause of weakness

## Related Skills

- **activation-scorer** — Identifies weak phrases
- **voice-drill-builder** — Base drill building logic
- **weekly-eval** — Triggers replay sessions
