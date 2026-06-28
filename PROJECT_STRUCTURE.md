# SpeakOps Repository Structure

> **Anatomy of an AI-Ready Voice Activation OS**

---

## 📁 Directory Tree

```
speakops/
│
├── 🤖 .claude/                              # Claude Code integration layer
│   ├── commands/                           # 🎯 Slash commands for Claude Code
│   │   ├── ingest-source.md                # Ingest Obsidian/GDocs/YouTube content
│   │   ├── extract-phrases.md              # Extract Business English phrases
│   │   ├── build-voice-drill.md            # Generate ChatGPT Voice prompts
│   │   ├── score-session.md                # Score phrase usage from sessions
│   │   ├── weekly-eval.md                  # Run weekly benchmark evals
│   │   ├── review-skill.md                 # Review skill quality
│   │   └── improve-repo.md                 # Analyze and improve repository
│   │
│   └── skills/                             # 🔗 Claude-facing skills bridge
│       └── README.md                       # Entry point to /skills directory
│
├── 🧠 .agent/                              # Agentic Development OS
│   ├── memory/                             # 💾 Agent working memory
│   │   ├── working.md                      # Current context and tasks
│   │   ├── decisions.md                    # Architectural decisions
│   │   └── episodic.md                     # Episode traces and learnings
│   │
│   ├── protocols/                          # 📋 Development protocols
│   │   ├── coding-loop.md                  # Coding workflow and quality gates
│   │   ├── eval-loop.md                    # Eval creation and running
│   │   ├── review-loop.md                  # Review process (self/Codex/security)
│   │   └── release-loop.md                 # Release process and versioning
│   │
│   └── adapters/                           # 🔌 System adapters
│       ├── claude-code.md                  # Claude Code integration
│       ├── chatgpt-voice.md                # ChatGPT Voice runtime
│       └── codex-cli.md                    # Codex CLI (future)
│
├── 👥 agents/                              # Agent role specifications
│   ├── spec-planner.md                     # Converts requests to specs
│   ├── repo-architect.md                   # Reviews repository structure
│   ├── skill-architect.md                  # Designs Claude Code skills
│   ├── voice-flow-designer.md             # Designs voice practice flows
│   ├── spoken-naturalness-judge.md        # Judges phrase naturalness
│   ├── eval-engineer.md                   # Creates evals for behaviors
│   ├── activation-scorer.md                # Maintains scoring model
│   ├── privacy-security-reviewer.md        # Security/privacy reviewer
│   ├── lazy-senior-dev.md                  # Reduces scope and prevents bloat
│   ├── codex-reviewer.md                   # Independent reviewer
│   └── docs-architect.md                   # Maintains documentation
│
├── 🛠️ skills/                              # Claude Code Skills (primary)
│   ├── phrase-extractor/                   # Extract phrases from sources
│   ├── spoken-naturalness-gate/            # Filter for spoken naturalness
│   ├── voice-drill-builder/                # Build voice drill prompts
│   ├── interview-activator/               # Build interview simulations
│   ├── meeting-simulator/                 # Build meeting simulations
│   ├── weak-phrase-replayer/              # Replay weak phrases
│   ├── activation-scorer/                 # Score phrase usage
│   ├── weekly-eval/                       # Run weekly benchmarks
│   ├── source-ingestor/                   # Ingest source material
│   └── phrase-card-generator/             # Create phrase cards
│
├── ✅ evals/                               # Quality and regression testing
│   ├── rubrics/                           # 📊 Scoring rubrics
│   │   ├── phrase-extraction-quality.md    # Phrase extraction eval
│   │   ├── spoken-naturalness.md           # Naturalness filtering eval
│   │   ├── voice-drill-quality.md         # Voice drill quality eval
│   │   ├── activation-scoring.md          # Scoring consistency eval
│   │   ├── privacy-security.md             # Security/privacy eval
│   │   └── weekly-regression.md            # Regression testing
│   │
│   ├── datasets/                           # 🧪 Golden test datasets
│   ├── expected/                           # 📋 Expected outputs
│   ├── judges/                             # 🧑‍⚖️ Eval judge prompts
│   └── reports/                            # 📈 Eval results
│
├── 📚 docs/                                # User and developer documentation
│   ├── workflows/                          # 🔄 User-facing workflow guides
│   │   ├── obsidian-to-voice-drill.md      # Obsidian → voice drill workflow
│   │   ├── gdoc-to-voice-drill.md          # Google Docs → voice drill
│   │   ├── youtube-to-evals-phrase-pack.md # YouTube → AI/evals pack
│   │   ├── transcript-to-scoring.md        # Session → scoring workflow
│   │   └── weekly-benchmark.md             # Weekly eval workflow
│   │
│   ├── conventions/                        # 📐 Development conventions
│   │   ├── SPEAKING_STYLE_GUIDE.md         # Spoken English style guide
│   │   ├── PHRASE_EXTRACTION_CONVENTIONS.md
│   │   ├── VOICE_DRILL_CONVENTIONS.md
│   │   ├── EVAL_CONVENTIONS.md
│   │   ├── PRIVACY_CONVENTIONS.md
│   │   ├── AGENT_WORKFLOW_CONVENTIONS.md
│   │   └── README_DESIGN_GUIDE.md
│   │
│   ├── adr/                                # 🏗️ Architecture Decision Records
│   ├── decision-log.md                     # 📝 All significant decisions
│   ├── changelog.md                        # 📋 Version history
│   ├── GITHUB_PROFILE_SETUP.md             # ⚙️ GitHub repository setup
│   └── VISUAL_DESIGN.md                    # 🎨 Visual design system
│
├── 📄 templates/                           # Output templates
│   ├── phrase-card.md                     # Phrase card template
│   ├── chatgpt-voice-prompt.md            # Voice prompt template
│   ├── practice-log.md                    # Session log template
│   ├── weekly-review.md                   # Weekly eval template
│   ├── eval-case.md                       # Eval case template
│   └── adr.md                             # ADR template
│
├── 🐍 scripts/                             # Automation scripts
│   ├── ingest_obsidian.py                 # Obsidian ingestion
│   ├── score_session.py                   # Session scoring
│   ├── update_phrase_bank.py              # Phrase bank updates
│   ├── run_evals.py                       # Eval runner
│   ├── ingest_gdoc.md                     # GDocs ingestion guide
│   └── ingest_youtube_notebooklm.md        # YouTube ingestion guide
│
├── 🔔 voice-hooks/                         # Voice alert system
│   ├── README.md                          # Alert system overview
│   └── voice-alert-spec.md                # Alert specification
│
├── 🔒 security/                            # Security and privacy
│   ├── threat-model.md                    # Threat analysis
│   ├── privacy-model.md                   # Privacy requirements
│   └── prompt-injection-risks.md         # Injection threats
│
├── 💾 data/                                # Local data storage (gitignored)
│   ├── phrases.csv                        # Phrase bank
│   ├── sessions.jsonl                     # Session logs
│   ├── scores.jsonl                       # Score history
│   └── weak_phrases.jsonl                # Weak phrases
│
├── 🎯 examples/                            # Safe demo examples
│   ├── source-sample.md                   # Example source material
│   ├── phrase-cards-sample.md             # Example phrase cards
│   ├── voice-drill-sample.md              # Example voice drill
│   └── scoring-report-sample.md           # Example scoring report
│
├── 🔧 .github/                             # GitHub configuration
│   └── workflows/                        # CI/CD workflows
│       ├── markdown-check.yml             # Markdown linting
│       ├── python-check.yml               # Python linting
│       ├── eval-regression.yml            # Eval regression tests
│       └── secret-scan.yml                # Secret scanning
│
├── ⚙️ .pre-commit-config.yaml             # Pre-commit hooks
│
├── 📖 README.md                            # Project landing page
├── 🤖 CLAUDE.md                            # Claude Code development guide
├── 👥 AGENTS.md                            # Agent roles and responsibilities
├── ⚖️ CODEX.md                             # Independent reviewer guidelines
├── 🔒 SECURITY.md                          # Security and privacy model
├── 📁 PROJECT_STRUCTURE.md                # This file
├── 📋 TODO.md                              # Development roadmap
└── ⚖️ LICENSE                              # MIT License
```

---

## 🎯 Directory Purposes

### 🤖 Core Integration (`.claude/`)
- **Purpose:** Claude Code integration layer
- **Contains:** Commands and skills bridge
- **Key:** Entry point for Claude Code workflows

### 🧠 Development OS (`.agent/`)
- **Purpose:** Systematic development process
- **Contains:** Protocols, memory, adapters
- **Key:** Ensures quality and consistency

### 👥 Agent Definitions (`agents/`)
- **Purpose:** Agent role specifications
- **Contains:** 11 agent definitions
- **Key:** Clear responsibilities for each agent

### 🛠️ Skills (`skills/`)
- **Purpose:** Claude Code Skills (primary definitions)
- **Contains:** 10 skills with evals and examples
- **Key:** Reusable AI capabilities

### ✅ Evals (`evals/`)
- **Purpose:** Quality and regression testing
- **Contains:** Rubrics, datasets, expected outputs
- **Key:** Quality gates for all AI behaviors

### 📚 Documentation (`docs/`)
- **Purpose:** User and developer guides
- **Contains:** Workflows, conventions, decisions
- **Key:** How to use and develop SpeakOps

### 📄 Templates (`templates/`)
- **Purpose:** Output format templates
- **Contains:** Phrase cards, prompts, logs
- **Key:** Consistent output formatting

### 🐍 Scripts (`scripts/`)
- **Purpose:** Automation and utilities
- **Contains:** Ingestion, scoring, eval runners
- **Key:** Automated workflows

### 🎯 Examples (`examples/`)
- **Purpose:** Safe demonstration files
- **Contains:** Sample data and outputs
- **Key:** Learning and testing

### 💾 Data (`data/`)
- **Purpose:** Local user data (gitignored)
- **Contains:** Phrases, sessions, scores
- **Key:** User's phrase bank and progress

---

## 🎨 Visual Color Legend

| Color | Purpose |
|-------|---------|
| 🤖 Purple | AI-ready integration |
| 🧠 Brain | Development OS |
| 👥 People | Agent layer |
| 🛠️ Tools | Skills & capabilities |
| ✅ Check | Quality & evaluation |
| 📚 Books | Documentation |
| 🔔 Bell | Alert system |
| 🔒 Lock | Security & privacy |
| 💾 Disk | Data storage |

---

## 🔗 Related Documentation

- **Development Guide:** [CLAUDE.md](CLAUDE.md)
- **Agent Roles:** [AGENTS.md](AGENTS.md)
- **Security Model:** [SECURITY.md](SECURITY.md)
- **Visual Design:** [docs/VISUAL_DESIGN.md](docs/VISUAL_DESIGN.md)

---

**Structure Version:** 1.0  
**Last Updated:** 2025-06-29
