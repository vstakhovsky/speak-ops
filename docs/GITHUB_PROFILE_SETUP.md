# GitHub Repository Profile Setup

**Purpose:** Guide for setting up the SpeakOps GitHub repository for maximum clarity and appeal.

---

## Repository Description

**Recommended description (160 characters max):**

```
Local-first Business English Voice Activation OS with AI skills, agents, evals, and voice drills. Turn passive vocabulary into active spoken English for IT, Product, and AI professionals.
```

**Alternative (shorter):**

```
Local-first Business English Voice Activation OS for IT/Product/AI professionals. Claude Code skills, agents, evals, and ChatGPT Voice drills.
```

---

## GitHub Topics

**Add these topics to the repository:**

```
business-english
voice-ai
ai-agents
claude-code
skills
evals
language-learning
prompt-engineering
local-first
product-management
interview-prep
spoken-english
voice-activation
agentic-ai
quality-gates
eval-driven
```

**How to add:**
1. Go to repository Settings
2. Scroll to "Topics"
3. Add each topic (they autocomplete)

---

## Social Preview

**Repository social image (if desired):**

Create a simple social preview image that shows:
- SpeakOps logo or name
- Tagline: "Local-first Business English Voice Activation"
- Visual: Clean, professional, minimal

**Recommended tools:**
- Canva (free)
- Figma (free)
- Image size: 1280×640px

**Upload to:**
- Repository → Settings → Social preview
- Or add to: `docs/social-preview.png`

---

## Pinned Repository Pitch (Optional)

If you pin repositories to your GitHub profile, use this pitch:

**Short (one line):**

```
SpeakOps — Local-first English Voice Activation for IT/Product/AI professionals
```

**Medium (2–3 lines):**

```
SpeakOps
Local-first Business English Voice Activation OS

Turn passive English vocabulary into active spoken communication through Claude Code skills, agents, evals, and ChatGPT Voice drills.
For IT, Product, and AI professionals.
```

**Long (for profile README):**

```
## SpeakOps

**Local-first Business English Voice Activation OS for IT/Product/AI professionals**

SpeakOps transforms passive professional English vocabulary into active spoken communication through:
- Claude Code skills for phrase extraction and filtering
- Agent-based development with quality gates
- Comprehensive evals for quality assurance
- ChatGPT Voice drill prompts for practice
- Activation scoring for progress tracking

**Perfect for:** Senior PM interviews, stakeholder meetings, technical discussions, AI/evals conversations.

**Key features:**
- Local-first (data stays on your device)
- Privacy-first (no external API calls)
- Eval-driven (quality gates everywhere)
- Agent-based (systematic development)

**Get started:** `git clone https://github.com/vstakhovsky/speak-ops`
```

---

## About Section (Repository)

**Add this to the repository "About" section:**

```
SpeakOps helps IT, Product, and AI professionals transform passive English vocabulary into active spoken communication through local-first voice practice with AI skills, agents, evals, and ChatGPT Voice drills.

🎯 Focus: Natural spoken Business English for interviews, meetings, and technical discussions
🔒 Privacy: Local-first, no API keys, no external calls
🤖 AI-driven: Claude Code skills, agents, and comprehensive evals
📊 Progress: Activation scoring from passive to meeting-ready

**Core loop:** Source → Extract → Filter → Cards → Voice Drill → Practice → Score → Replay → Weekly Eval

**Tech stack:** Claude Code, ChatGPT Voice, Python 3.13+, Markdown
**Development:** Eval-driven, agent-based, privacy-first

Get started: claude (in repo directory) → /build-voice-drill
```

---

## README Badges (Optional)

**Add badges to README.md for quick status information:**

```markdown
![Status: Active](https://img.shields.io/badge/status-active-success)
![Claude Code](https://img.shields.io/badge/claude--code-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
```

---

## Repository Visibility

**Recommended:** Public repository

**Rationale:**
- Open source by design (MIT License)
- Community can learn from approach
- Transparency in development
- Easier to share and reference

**Private considerations:**
- Keep private if:
  - Contains personal phrase banks
  - Has private transcripts
  - Not ready for public viewing

---

## README Hero Section (Optional)

**Add a hero section at the top of README.md:**

```markdown
<div align="center">

# 🎤 SpeakOps

### Local-first Business English Voice Activation OS

**Transform passive vocabulary into active spoken communication**

[Features](#features) • [Quick Start](#quick-start) • [Architecture](#architecture) • [Development](#development)

[Get Started](#quick-start) • [Read the Docs](#documentation) • [View Examples](#examples)

</div>
```

---

## Links and Resources

**Add to repository "Website" and "Links" sections:**

**Website:** (optional)
- Leave blank or link to: `https://vstakhovsky.github.io/speak-ops/` (if you create a site)

**Links:**
- Documentation: Link to `docs/` directory or GitHub Pages
- Examples: Link to `examples/` directory
- Issue tracker: GitHub Issues
- Related projects: (if any)

---

## Release Strategy

**For initial release:**

1. **Create release:** v0.1.0
2. **Tag:** `v0.1.0`
3. **Release notes:** Describe MVP capabilities
4. **Assets:** None (no binaries needed)

**Release notes template:**

```markdown
# SpeakOps v0.1.0

## MVP Release

SpeakOps is now available as an MVP with:
- 10 Claude Code skills
- 8 agent specifications
- 6 eval rubrics
- 5 documented workflows
- Local-first architecture
- Privacy-first design

## Getting Started

See [README.md](README.md) for quick start.

## What's Next

- Skill implementation with actual logic
- Golden datasets for evals
- Enhanced error handling
- More example workflows

## Known Limitations

- Manual source ingestion (no API for MVP)
- Skills need implementation
- Evals need test cases
- Scripts need enhancement
```

---

## Visibility Settings

**Repository visibility:** Public (recommended)

**Features to enable:**
- ✅ Issues (for feedback and discussion)
- ✅ Discussions (for Q&A)
- ✅ Actions (CI/CD workflows)
- ✅ Wiki (if you want additional docs)
- ❌ Projects (not needed for single repo)

**Security settings:**
- ✅ Security advisories (if vulnerabilities found)
- ✅ Dependabot (if dependencies added later)
- ✅ CodeQL alerts (if using advanced security)

---

## Community Guidelines

**If open to contributions:**

Add a `CONTRIBUTING.md` that references CLAUDE.md:

```markdown
# Contributing to SpeakOps

Thanks for your interest in contributing!

## Development Process

SpeakOps uses an **Agentic Development OS** approach. See [CLAUDE.md](CLAUDE.md) for the complete development process.

## Quick Start

1. Read [README.md](README.md)
2. Read [CLAUDE.md](CLAUDE.md)
3. Check [TODO.md](TODO.md) for open tasks
4. Fork and create a branch
5. Follow development process in CLAUDE.md

## Quality Gates

All contributions must pass:
- ✅ Eval coverage (for AI behaviors)
- ✅ Security review (for ingestion/logging)
- ✅ Documentation (for workflow changes)
- ✅ Decision log (for architecture changes)

## Contact

Open an issue or discussion to propose a contribution.
```

---

## Branch Protection

**Recommended rules for main branch:**

```yaml
Branch protection rules:
  - Require pull request before merging
  - Require status checks to pass
    - markdown-check
    - python-check
    - secret-scan
  - Require 1 approval (for initial releases)
  - Limit who can push (maintainers only)
```

---

## Issue Templates (Optional)

**Create issue templates for common requests:**

**1. Bug Report:**
```markdown
---
name: Bug report
about: Report a problem with SpeakOps
title: '[Bug] '
labels: bug
assignees: ''
---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment**
- OS: [e.g. macOS, Linux]
- Python version: [e.g. 3.13]
- Claude Code version: [if applicable]

**Additional context**
Add any other context about the problem here.
```

**2. Feature Request:**
```markdown
---
name: Feature request
about: Suggest an idea for SpeakOps
title: '[Feature] '
labels: enhancement
assignees: ''
---

**Is your feature request related to a problem?**
A clear and concise description of what the problem is.

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.
```

---

## Checklist

**Before publishing repository:**

- [ ] Repository description added
- [ ] Topics added
- [ ] README.md is comprehensive
- [ ] LICENSE file exists (MIT)
- [ ] CONTRIBUTING.md created (if accepting contributions)
- [ ] .github/ workflows are set up
- [ ] Branch protection enabled (if desired)
- [ ] Issues/Discussions enabled
- [ ] Release v0.1.0 created
- [ ] Social preview (optional)

---

## Next Steps

**After setting up profile:**

1. **Create initial release:** Tag v0.1.0
2. **Announce (if desired):** Share on relevant channels
3. **Monitor issues:** Respond to questions and bug reports
4. **Iterate:** Improve based on feedback

---

**Profile Setup Version:** 1.0
**Last Updated:** 2025-06-28
