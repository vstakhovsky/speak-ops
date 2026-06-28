# SpeakOps

Local-first Business English Voice Activation system for IT/Product/AI professionals.

## Product Goal

Transform passive professional English vocabulary into **active spoken English** for:
- Senior PM interviews
- Technical PM interviews
- Stakeholder meetings
- Roadmap discussions
- Technical discussions with engineers
- AI/evals/governance conversations
- Executive updates
- Conflict and pushback situations

**Principle:** Optimize for natural spoken Business English, not formal written English.

## Architecture

SpeakOps is built as an **Agentic Development OS**:

- **Claude Code Skills** — Reusable voice and phrase workflows
- **Agents & Subagents** — Specialized reviewers and builders
- **Evals & Rubrics** — Quality gates for every behavior
- **Security & Privacy Gates** — Defensive review for ingestion
- **Local Data Files** — Phrase bank, sessions, scores
- **ChatGPT Voice Prompts** — Ready-to-paste drills
- **Decision Log** — Every meaningful change tracked

## Core Loop

```
Sources → Extract → Filter → Cards → Voice Drill → Practice → Score → Replay → Weekly Eval
```

**Sources:** Google Docs, Obsidian, YouTube, NotebookLM, meeting notes, interview answers

1. **Ingest** source material
2. **Extract** Business English/IT/AI phrases
3. **Filter** out formal/robotic/AI-like phrases
4. **Create** phrase cards
5. **Build** voice practice scenarios
6. **Generate** ChatGPT Voice prompts
7. **Score** transcript after session
8. **Update** Activation Score per phrase
9. **Replay** weak phrases in new contexts
10. **Run** weekly benchmark evals

## Quick Start

```bash
# Ingest phrases from Obsidian
/ingest-obsidian --path "<vault-path>"

# Extract and filter spoken phrases
/extract-phrases --domain ai-evals --level b2-c1
/filter-spoken --remove-ai-like

# Build voice drill
/build-voice-drill --mode interview --session 8

# Score session
/score-session --transcript "<file>"

# Weekly eval
/weekly-eval
```

## Repository Structure

```
speakops/
├── README.md
├── CLAUDE.md              # Claude Code development guide
├── AGENTS.md              # Agent roles and responsibilities
├── CODEX.md               # Independent reviewer guidelines
├── SECURITY.md            # Security and privacy model
│
├── .agent/                # Agentic development OS
│   ├── memory/            # Working memory, decisions, episodic traces
│   ├── protocols/         # Coding, eval, review, release loops
│   └── adapters/          # Claude Code, Codex CLI, ChatGPT Voice
│
├── specs/                 # Specifications (constitution, product, technical)
│
├── skills/                # Claude Code Skills
│   ├── phrase-extractor/
│   ├── spoken-naturalness-gate/
│   ├── voice-drill-builder/
│   ├── interview-activator/
│   ├── meeting-simulator/
│   ├── weak-phrase-replayer/
│   ├── activation-scorer/
│   ├── weekly-eval/
│   ├── source-ingestor/
│   └── phrase-card-generator/
│
├── agents/                # Agent specification files
│
├── data/                  # Local data files
│   ├── phrases.csv
│   ├── sessions.jsonl
│   ├── scores.jsonl
│   └── weak_phrases.jsonl
│
├── templates/             # Templates for outputs
│
├── evals/                 # Evals, rubrics, datasets
│
├── security/              # Threat model, privacy model
│
├── scripts/               # Utility scripts
│
├── voice-hooks/           # Voice alert specifications
│
└── docs/                  # Architecture, workflows, ADRs, decision log
```

## Activation Score Model

Each phrase is scored 0–100 across dimensions:

| Dimension | Points | Description |
|-----------|--------|-------------|
| Meaning understood | 10 | You know what it means |
| Used without hint | 20 | You used it without being prompted |
| Correct usage | 20 | Grammatically and contextually correct |
| Natural spoken usage | 20 | Sounds natural, not written |
| Context transfer | 15 | Used across different scenarios |
| Retrieval speed | 10 | Quick access in conversation |
| Retention after 7+ days | 5 | Still active after a week |

**Statuses:**
- 0–39: **Passive** — Recognize but don't use
- 40–59: **Recognized** — Can use with effort
- 60–74: **Semi-active** — Sometimes use naturally
- 75–89: **Active** — Use comfortably
- 90–100: **Meeting-ready** / **Interview-ready**

## Quality Rules

### Avoid (too formal/written/AI-like)
- "I would like to emphasize..."
- "It is crucial to note..."
- "Furthermore..."
- "Moreover..."
- Overuse of abstract nouns
- Long passive sentences
- Essay tone

### Prefer (natural spoken)
- Short spoken phrases
- Direct but polite wording
- Realistic meeting language
- Business clarity
- Natural rhythm
- PM/IT context

## Workflows

See `/docs/workflows/` for detailed workflows:
1. Obsidian phrase bank → voice drill
2. Google Docs phrase list → voice drill
3. YouTube/NotebookLM → AI/evals phrase pack
4. Voice transcript → scoring
5. Weekly benchmark eval

## Development

See `/CLAUDE.md` for development process.

**Quality gates before merge:**
- Unit tests if scripts changed
- Evals if skills/prompts changed
- Regression evals if scoring changed
- Privacy/security review if ingestion changed
- Docs update if workflow changed
- Decision log update if architecture changed

## Security & Privacy

SpeakOps is **local-first**:
- No API keys stored
- No external network calls without approval
- Source content treated as untrusted
- Minimal data retention
- Private transcripts not logged by default

See `/SECURITY.md` for full security model.

## License

MIT

---

**Status:** Active development — MVP in progress
