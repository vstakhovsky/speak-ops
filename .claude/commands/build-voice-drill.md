# Build Voice Drill

**Purpose:** Generate ready-to-paste ChatGPT Voice prompts for practice sessions.

## When to Use

- After extracting and filtering phrases
- When preparing for interviews or meetings
- To practice weak phrases in new contexts
- For regular speaking practice

## Inputs

```bash
/build-voice-drill --mode <mode> --scenario <scenario>

# Examples
/build-voice-drill --mode interview --scenario stakeholder-conflict
/build-voice-drill --mode meeting --scenario roadmap-review
/build-voice-drill --mode ai-evals --scenario evaluation-strategy
```

## Mode Options

| Mode | Description | Target Skills |
|------|-------------|---------------|
| `interview` | Interview practice | Storytelling, conflict, priorities |
| `meeting` | Meeting simulation | Roadmap, pushback, technical |
| `ai-evals` | Technical PM discussion | Evaluation, governance, strategy |

## Scenario Options

### Interview Scenarios
- `tell-me-about-yourself` — Introduction and background
- `stakeholder-conflict` — Handling disagreement
- `prioritization` — Making trade-offs
- `working-with-engineers` — Technical collaboration
- `ambiguity` — Handling uncertainty
- `failure-story` — Learning from mistakes

### Meeting Scenarios
- `roadmap-review` — Presenting roadmap
- `engineering-sync` — Technical sync
- `stakeholder-pushback` — Handling pushback
- `design-discussion` — Technical design
- `incident-review` — Post-incident review
- `executive-update` — Executive presentation

### AI/Evals Scenarios
- `evaluation-strategy` — Evaluation planning
- `model-behavior` — Model behavior discussion
- `governance` — AI governance conversation
- `technical-pm-discussion` — Technical PM deep-dive

## Workflow Steps

1. **Select target phrases**
   - Choose 5–8 phrases from phrase bank
   - Balance difficulty (mix of active/semi-active)
   - Prioritize weak phrases if present
   - Ensure scenario relevance

2. **Create scenario**
   - Define realistic situation
   - Set user and AI roles
   - Establish context and constraints
   - Plan conversation flow

3. **Generate ChatGPT Voice prompt**
   - Include target phrases
   - Specify conversation rules
   - Set turn length (2–3 sentences max)
   - Define correction behavior
   - Request end feedback

4. **Create practice log template**
   - List target phrases
   - Usage tracking table
   - Feedback section
   - Self-reflection prompts

5. **Create scoring rubric**
   - Phrase usage scoring
   - Naturalness assessment
   - Session quality rating

## Output Format

```markdown
# Voice Drill: [Title]

## Target Phrases
1. [phrase 1]
2. [phrase 2]
...

## Scenario
[Scenario description]

## ChatGPT Voice Prompt
[Prompt to paste into ChatGPT Voice]

## Practice Log Template
[How to log the session]

## Scoring Rubric
[How to score phrase usage]
```

## Prompt Requirements

Every generated prompt must:

✅ **Include:**
- 5–8 target phrases
- Realistic scenario description
- Clear AI role and user role
- Conversation rules
- Turn length limits
- Correction guidance
- End feedback request

❌ **Avoid:**
- Vague scenarios
- Too many phrases (>8)
- Long AI turns
- No phrase forcing
- Unclear correction rules

## Safety & Quality Notes

⚠️ **Quality:**
- Scenarios must be realistic
- Phrases must fit naturally
- AI turns must be short
- Feedback must be specific

✅ **Best Practices:**
- Test prompt yourself first
- Adjust phrase count if needed
- Modify scenario for your context
- Keep drills under 10 minutes

## Related Skills

- **voice-drill-builder** — Core drill building logic
- **interview-activator** — Interview-specific drills
- **meeting-simulator** — Meeting-specific drills
- **weak-phrase-replayer** — Weak phrase drills

## Related Evals

- **voice-drill-quality** — Tests drill quality
- **scenario-realism** — Tests scenario authenticity

## Example

```bash
/build-voice-drill --mode interview --scenario stakeholder-conflict

# Output
# Voice Drill: Stakeholder Conflict

## Target Phrases
1. push back on
2. loop in
3. align on
4. find middle ground
5. table this

## Scenario
Tell me about a time you had to handle a difficult stakeholder who wanted something that wasn't feasible.

## ChatGPT Voice Prompt
You are a Senior PM interviewer. I am a candidate.
[... full prompt ...]
```

---

**Command Version:** 1.0
**Status:** Active
