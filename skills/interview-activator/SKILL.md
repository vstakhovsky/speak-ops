# interview-activator

Creates interview simulations for senior PM and technical PM interviews.

## Trigger Conditions

User runs:
```bash
/build-voice-drill --mode interview --scenario <scenario>
```

Or when:
- Preparing for PM interviews
- Practicing interview answers
- Building interview phrase packs

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| interview_type | string | senior-pm, technical-pm |
| question_type | string | Specific question category |
| phrases | list | Target phrases for drill |
| user_level | string | b1, b2, c1, c2 |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| scenario | string | Interview scenario description |
| chatgpt_prompt | string | Ready-to-paste prompt |
| expected_phrases | list | Phrases to use in answer |
| practice_log | string | How to log session |

## Interview Types

### Senior PM Interviews
- **tell-me-about-yourself** — Introduction and background
- **stakeholder-conflict** — Handling disagreement
- **prioritization** — Making trade-offs
- **working-with-engineers** — Technical collaboration
- **ambiguity** — Handling uncertainty
- **leadership** — Leading without authority
- **failure-story** — Learning from mistakes
- **product-strategy** — Strategic thinking

### Technical PM Interviews
- **technical-deep-dive** — Explaining technical concepts
- **trade-offs** — Technical vs business trade-offs
- **ai-strategy** — AI/ML product decisions
- **data-fluency** — Working with data
- **engineering-collaboration** — Working with technical teams
- **system-design** — Technical system thinking
- **evals-strategy** — AI evaluation strategy

## Workflow

1. **Select interview type** — Senior PM or Technical PM
2. **Select question type** — Specific category
3. **Choose target phrases** — 5–8 relevant phrases
4. **Design scenario** — Realistic interview question
5. **Create ChatGPT prompt** — Interview simulation prompt
6. **Add evaluation criteria** — How to judge answer
7. **Output drill** — Complete interview drill

## Examples

### Example 1: Stakeholder conflict
```
Type: Senior PM Interview
Question: Stakeholder conflict

Target phrases:
- push back on
- align on
- loop in
- find middle ground
- move forward

Scenario: "The Sales VP wants a feature that Engineering says will take 3 months. You need to handle this pushback."

ChatGPT Prompt:
"You are a Senior PM interviewer. Ask: 'Tell me about a time you had to push back on a stakeholder request.'

Conduct a 5-minute interview where you:
- Ask probing follow-up questions
- Challenge their approach
- Force them to use: 'push back on', 'align on', 'loop in', 'find middle ground', 'move forward'
- Keep your turns short (2-3 sentences)

If they make major mistakes:
- Correct them
- Give a better spoken version
- Ask them to repeat it

After 5 minutes:
- Summarize which phrases they used well
- Note which they missed or used incorrectly
- Give specific feedback on naturalness"
```

### Example 2: Technical deep dive
```
Type: Technical PM Interview
Question: Technical deep-dive

Target phrases:
- under the hood
- at scale
- trade-off
- latency
- bottleneck

Scenario: "Explain how a recommendation system works."

ChatGPT Prompt:
[Prompt text]
```

## Eval Cases

### Test 1: Realistic interview question
**Input:** Generate interview drill
**Expected:** Question is realistic for PM interview
**Pass criteria:** Question matches actual interview patterns

### Test 2: Forces phrase usage
**Input:** Interview drill with target phrases
**Expected:** Prompt creates natural opportunities for phrases
**Pass criteria:** All phrases have natural usage moments

### Test 3: Appropriate difficulty
**Input:** User level B2
**Expected:** Scenario complexity matches level
**Pass criteria:** Not too easy, not too hard

## Risks and Limitations

- May not match actual interview style
- Questions may be too generic
- May not adapt to user's background
- ChatGPT may not follow interview format perfectly
- May not cover all interview question types

## Related Skills

- **voice-drill-builder** — Base drill building logic
- **meeting-simulator** — Similar logic for meetings
- **phrase-extractor** — Provides interview phrases
