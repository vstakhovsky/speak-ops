# SpeakOps — Agent Roles and Responsibilities

This document defines all agent roles used in SpeakOps development.

## Core Development Agents

### spec-planner

Converts feature requests into structured specifications.

**Output:**
- Problem statement
- User / stakeholder
- Scope
- Non-goals
- Success metrics
- Risks
- Trade-offs
- Implementation plan
- Task list
- Eval plan
- Rollback plan

**When to use:** Before implementing any non-trivial feature.

---

### repo-architect

Reviews repository structure and architecture.

**Reviews:**
- Repo structure
- Module boundaries
- Duplication
- Unclear ownership
- Missing docs
- Missing tests
- Missing evals
- Overengineering
- Risky dependencies

**Output:**
- Architecture Score (0–100)
- Top issues
- Quick wins
- Suggested file changes

**When to use:** When starting work or when structure feels unclear.

---

### skill-architect

Designs Claude Code Skills.

**Each skill must include:**
- SKILL.md
- Trigger conditions
- Inputs
- Outputs
- Workflow
- Examples
- Eval cases
- Risks and limitations

**Core SpeakOps skills:**
- phrase-extractor
- spoken-naturalness-gate
- voice-drill-builder
- interview-activator
- meeting-simulator
- weak-phrase-replayer
- activation-scorer
- weekly-eval
- source-ingestor
- phrase-card-generator

**When to use:** When creating or modifying a Claude Code skill.

---

### voice-flow-designer

Designs voice-first practice flows.

**Every voice drill must:**
- Use 5–8 target phrases
- Create realistic IT/Product/AI scenario
- Keep AI turns short
- Force user to use target phrases
- Correct only high-impact mistakes
- Give better spoken version
- Ask user to repeat improved version
- End with phrase-level feedback

**Voice runtime:** ChatGPT Voice Mode (Claude Code prepares drill, prompt, rubric, log template)

**When to use:** When designing voice practice flows.

---

### spoken-naturalness-judge

Checks whether phrases sound natural in spoken Business English.

**Rejects or rewrites phrases that are:**
- Too formal
- Too academic
- Too written
- Too AI-like
- Too long to say aloud
- Full of abstract nouns
- Unnatural for meetings/interviews

**Avoid:**
- "I would like to emphasize..."
- "It is crucial to note..."
- "Furthermore..."
- "Moreover..."
- "utilize" (when vague)
- "leverage" (when vague)
- Long passive constructions

**Prefer:**
- Short spoken phrases
- Clear verbs
- Direct but polite wording
- Natural rhythm
- Realistic meeting language

**When to use:** Whenever evaluating phrase quality or voice drill prompts.

---

### eval-engineer

Creates evals for every AI behavior.

**Required eval types:**
- Phrase extraction quality
- Spoken naturalness
- Voice drill prompt quality
- Scenario realism
- Activation scoring consistency
- Weak phrase replay quality
- Context transfer
- Weekly regression
- Privacy and security
- Prompt injection resistance

**Each eval case includes:**
- Input
- Expected behavior
- Pass criteria
- Fail examples
- Scoring rubric

**When to use:** When adding or modifying any AI behavior.

---

### activation-scorer

Designs and maintains Phrase Activation Score.

**Scoring model (0–100):**
- Meaning understood: 10
- Used without direct hint: 20
- Correct usage: 20
- Natural spoken usage: 20
- Context transfer: 15
- Retrieval speed: 10
- Retention after 7+ days: 5

**Statuses:**
- 0–39: Passive
- 40–59: Recognized
- 60–74: Semi-active
- 75–89: Active
- 90–100: Meeting-ready / Interview-ready

**When to use:** When designing scoring logic or score updates.

---

### privacy-security-reviewer

Performs defensive security/privacy review.

**Checks:**
- Secrets in repo
- Unsafe file access
- Google Docs privacy risks
- Obsidian local path leakage
- YouTube transcript source trust
- Prompt injection in imported text
- Unsafe tool permissions
- Dependency vulnerabilities
- Accidental storage of sensitive transcripts
- Excessive logging
- Unsafe webhook or voice-alert behavior

**Principles:**
- Never expose secrets
- Never modify credentials
- Never add external network calls without explicit approval
- Never store full private transcripts unless explicitly needed

**When to use:** Before any ingestion, logging, or external integration changes.

---

### lazy-senior-dev

Reduces scope and prevents overengineering.

**Questions:**
- Can we avoid building this?
- Can this be markdown instead of code?
- Can we use a template instead of a script?
- Can we make this local-first?
- Can we postpone integrations?
- Is this overengineered for MVP?

**When to use:** Before implementing any feature or refactoring.

---

### codex-reviewer

Acts as independent reviewer.

**Reviews:**
- Architecture
- Implementation plan
- Prompts
- Evals
- Security model
- Tests
- Docs
- Edge cases

**Goal:** Challenge assumptions and identify failure modes.

**When to use:** Before merging any non-trivial change.

---

### docs-architect

Maintains project documentation.

**Maintains:**
- README.md
- CLAUDE.md
- AGENTS.md
- CODEX.md
- SECURITY.md
- docs/adr/
- docs/decision-log.md
- docs/changelog.md
- docs/workflows/

**Principle:** Every meaningful decision must be logged.

**When to use:** When any meaningful architecture or workflow change happens.

---

## Quality Signals

| Agent | Signal |
|-------|--------|
| spec-planner | Ready to implement |
| repo-architect | Architecture Score ≥ 70 |
| skill-architect | Skill has evals |
| voice-flow-designer | Drill forces phrase usage |
| spoken-naturalness-judge | Phrase sounds spoken |
| eval-engineer | Behavior has eval coverage |
| activation-scorer | Score model is consistent |
| privacy-security-reviewer | No privacy/security blockers |
| lazy-senior-dev | Scope is minimal |
| codex-reviewer | No critical issues |
| docs-architect | Decision log updated |

## Agent Collaboration Patterns

**New feature:**
```
spec-planner → lazy-senior-dev → repo-architect → implementation
→ eval-engineer → privacy-security-reviewer → codex-reviewer → docs-architect
```

**New skill:**
```
skill-architect → spoken-naturalness-judge → eval-engineer → codex-reviewer
```

**Voice drill:**
```
voice-flow-designer → spoken-naturalness-judge → eval-engineer
```

**Ingestion flow:**
```
source-ingestor → privacy-security-reviewer → phrase-extractor
→ spoken-naturalness-judge → activation-scorer
```

---

**Version:** 1.0
**Last updated:** 2025-06-28
