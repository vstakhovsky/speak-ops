# voice-drill-builder

Generates ready-to-paste ChatGPT Voice prompts.

## Trigger Conditions

User runs:
```bash
/build-voice-drill --mode <mode> --scenario <scenario> --session <n>
```

Or when:
- Creating practice drills from phrase cards
- Building interview simulations
- Building meeting simulations
- Creating weak phrase replay drills

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| phrases | list | 5–8 target phrases |
| mode | string | interview, meeting, ai-evals |
| scenario | string | Specific scenario type |
| session_length | number | Target session duration (minutes) |
| user_level | string | b1, b2, c1, c2 |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| title | string | Drill title |
| target_phrases | list | Selected phrases for drill |
| scenario | string | Scenario description |
| chatgpt_prompt | string | Ready-to-paste prompt |
| practice_log_template | string | How to log session |
| scoring_rubric | string | How to score usage |

## Voice Prompt Requirements

Every generated prompt must:

1. **Use 5–8 target phrases** — Not overwhelming, not too few
2. **Create realistic scenario** — IT/Product/AI context
3. **Keep AI turns short** — 2–3 sentences max
4. **Force phrase usage** — Create natural situations for phrases
5. **Correct high-impact mistakes** — Only major errors
6. **Give better spoken version** — Natural alternative
7. **Ask user to repeat** — Reinforce improvement
8. **End with phrase feedback** — Summary of usage

## Workflow

1. **Select phrases** — Choose 5–8 target phrases from phrase bank
2. **Choose scenario** — Pick realistic scenario based on mode
3. **Design flow** — Plan conversation that forces phrase usage
4. **Generate prompt** — Create ChatGPT Voice prompt
5. **Create log template** — How to record session
6. **Create scoring rubric** — How to evaluate usage
7. **Output drill** — Return complete drill package

## Scenario Types

### Interview Scenarios
- tell-me-about-yourself — Introduction
- stakeholder-conflict — Disagreement situation
- prioritization — Trade-off discussion
- working-with-engineers — Technical collaboration
- ambiguity — Handling uncertainty
- failure-story — Learning from mistakes
- ai-strategy — AI/Product discussion

### Meeting Scenarios
- roadmap-review — Presenting roadmap
- engineering-sync — Technical sync
- stakeholder-pushback — Pushback situation
- design-discussion — Technical design
- incident-review — Post-incident review
- evals-review — AI/evals discussion
- executive-update — Executive presentation

### AI/Evals Scenarios
- technical-pm-discussion — Technical PM conversation
- cto-pushback — CTO-style technical pushback
- governance — AI governance discussion
- evaluation-strategy — Evaluation planning

## Examples

### Example 1: Interview drill
```
Title: "Stakeholder Conflict Drill"

Target phrases:
- push back on
- loop in
- align on
- move forward
- table this

Scenario: "Sales wants a feature that Engineering says is too complex."

ChatGPT Voice Prompt:
[Prompt text]

Practice Log Template:
[Template]

Scoring Rubric:
[Rubric]
```

### Example 2: Meeting drill
```
Title: "Roadmap Review Pushback"

Target phrases:
- double down
- double down on
- double down on [initiative]
- shelve [plan]
- revisit [topic]

Scenario: "VP questions roadmap priorities."

ChatGPT Voice Prompt:
[Prompt text]
```

## Eval Cases

### Test 1: Forces phrase usage
**Input:** 8 target phrases
**Expected:** Prompt creates situations where phrases are natural
**Pass criteria:** All phrases have natural usage opportunities

### Test 2: Keeps turns short
**Input:** Generate drill
**Expected:** AI turns are 2–3 sentences max
**Pass criteria:** No long AI monologues

### Test 3: Realistic scenario
**Input:** Generate meeting drill
**Expected:** Scenario is realistic IT/Product situation
**Pass criteria:** Scenario passes realism eval

## Risks and Limitations

- May create unrealistic scenarios
- May force phrase usage unnaturally
- ChatGPT Voice may not follow instructions perfectly
- User may deviate from script
- May not adapt to user responses appropriately

## Related Skills

- **phrase-extractor** — Provides target phrases
- **spoken-naturalness-gate** — Ensures phrases are natural
- **interview-activator** — Specialized for interviews
- **meeting-simulator** — Specialized for meetings
- **weak-phrase-replayer** — Specialized for weak phrases
