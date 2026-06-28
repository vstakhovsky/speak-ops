# Changelog

All notable changes to SpeakOps will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Claude Code integration layer** — `.claude/` directory with commands and skills bridge
- **7 Claude Code commands** — ingest-source, extract-phrases, build-voice-drill, score-session, weekly-eval, review-skill, improve-repo
- **PROJECT_STRUCTURE.md** — Repository anatomy and documentation
- **7 convention docs** — SPEAKING_STYLE_GUIDE, PHRASE_EXTRACTION_CONVENTIONS, VOICE_DRILL_CONVENTIONS, EVAL_CONVENTIONS, PRIVACY_CONVENTIONS, AGENT_WORKFLOW_CONVENTIONS, README_DESIGN_GUIDE
- **GitHub quality workflows** — markdown-check, python-check, secret-scan, eval-regression
- **Pre-commit hooks** — .pre-commit-config.yaml for quality checks
- **GitHub profile setup guide** — docs/GITHUB_PROFILE_SETUP.md
- **4 example files** — source-sample, phrase-cards-sample, voice-drill-sample, scoring-report-sample

### Changed
- **Improved README.md** — Enhanced with badges, clearer structure, better GitHub presentation
- **Updated decision-log.md** — Added AI-ready repository upgrade decision

### Security
- **Secret scanning** — GitHub workflow for detecting secrets
- **Pre-commit checks** — Local validation before commits
- **Markdown quality checks** — Ensure consistent documentation

## [0.1.0] - 2025-06-28

### Added
- Initial MVP release
- Core repository structure
- Documentation (README, CLAUDE, AGENTS, CODEX, SECURITY)
- Skills infrastructure
- Eval framework
- Basic scripts
- Workflow templates
- Decision log

### Security
- Privacy-first design
- Local-only data storage
- Input sanitization
- File access restrictions

---

## [Future Versions]

### [0.2.0] - Planned
- Enhanced skill implementations
- More eval cases
- Improved script error handling
- Better documentation

### [1.0.0] - Planned
- Stable release
- Comprehensive eval coverage
- Full workflow automation
- Complete documentation

---

**Changelog Version:** 1.1
**Last Updated:** 2025-06-28
