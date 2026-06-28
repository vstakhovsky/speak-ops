# meeting-simulator

Creates meeting simulations for IT/Product/AI scenarios.

## Trigger Conditions

User runs:
```bash
/build-voice-drill --mode meeting --scenario <scenario>
```

Or when:
- Preparing for stakeholder meetings
- Practicing technical discussions
- Building meeting phrase packs

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| meeting_type | string | Specific meeting scenario |
| role | string | User's role in meeting |
| phrases | list | Target phrases for drill |
| difficulty | string | easy, medium, hard |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| scenario | string | Meeting scenario description |
| chatgpt_prompt | string | Ready-to-paste prompt |
| participants | list | Meeting participants and roles |
| expected_phrases | list | Phrases to use in meeting |

## Meeting Types

### Roadmap Meetings
- **roadmap-review** — Presenting roadmap to stakeholders
- **prioritization** — Discussing feature priorities
- **trade-off-discussion** — Making roadmap trade-offs
- **timeline-negotiation** — Negotiating timelines

### Engineering Meetings
- **engineering-sync** — Technical sync with engineers
- **design-discussion** — Technical design discussion
- **incident-review** — Post-incident review
- **technical-planning** — Technical planning session

### Stakeholder Meetings
- **stakeholder-pushback** — Handling pushback
- **executive-update** — Executive presentation
- **resource-negotiation** — Negotiating resources
- **conflict-resolution** — Resolving conflicts

### AI/Evals Meetings
- **ai-strategy** — AI strategy discussion
- **evals-review** — Evaluation results review
- **model-behavior** — Model behavior discussion
- **governance** — AI governance conversation
- **technical-pm-discussion** — Technical PM deep-dive

## Workflow

1. **Select meeting type** — Choose scenario
2. **Define user role** — What role user plays
3. **Choose target phrases** — 5–8 relevant phrases
4. **Design scenario** — Realistic meeting situation
5. **Create participants** — Define meeting participants
6. **Create ChatGPT prompt** — Meeting simulation prompt
7. **Add conflict points** — Natural places for phrases
8. **Output drill** — Complete meeting drill

## Examples

### Example 1: Stakeholder pushback
```
Type: Stakeholder Meeting
Scenario: Stakeholder pushback

Target phrases:
- push back on
- double down
- table this
- revisit
- align on

Participants:
- You (PM)
- VP of Sales (pushing for feature)
- Engineering Lead (concerned about complexity)
- CPO (observing)

Scenario: "Sales VP wants a feature that Engineering says is too complex. You're in a meeting to discuss this."

ChatGPT Prompt:
"You are the VP of Sales. I'm the PM. Engineering Lead and CPO are also in the meeting.

Start by pushing hard for the feature: 'We really need this feature for the Q2 target. Can we make it work?'

Conduct a 5-minute meeting where you:
- Push back on my attempts to delay
- Create situations where I need to use: 'push back on', 'double down', 'table this', 'revisit', 'align on'
- Keep your turns short (2-3 sentences)
- Be somewhat aggressive but professional

If I make major mistakes:
- Correct me
- Give a better spoken version
- Ask me to repeat it

After 5 minutes:
- Summarize which phrases I used well
- Note which I missed or used incorrectly
- Give specific feedback on naturalness"
```

### Example 2: Technical design discussion
```
Type: Engineering Meeting
Scenario: Design discussion

Target phrases:
- under the hood
- at scale
- bottleneck
- latency
- trade-off

Participants:
- You (Technical PM)
- Staff Engineer (technical)
- Senior Engineer (implementation)
- Engineering Manager

Scenario: "Discussing architecture for a new feature."

ChatGPT Prompt:
[Prompt text]
```

## Eval Cases

### Test 1: Realistic meeting scenario
**Input:** Generate meeting drill
**Expected:** Scenario is realistic meeting situation
**Pass criteria:** Scenario matches real meeting patterns

### Test 2: Natural phrase opportunities
**Input:** Meeting drill with target phrases
**Expected:** Phrases fit naturally into meeting flow
**Pass criteria:** All phrases have natural usage moments

### Test 3: Appropriate difficulty
**Input:** Difficulty: medium
**Expected:** Meeting complexity matches difficulty
**Pass criteria:** Not too easy, not too hard

## Risks and Limitations

- May not match real meeting dynamics
- Participants may be unrealistic
- May not capture organizational politics
- ChatGPT may not stay in character
- May be too generic

## Related Skills

- **voice-drill-builder** — Base drill building logic
- **interview-activator** — Similar logic for interviews
- **phrase-extractor** — Provides meeting phrases
