# SpeakOps Skills — Claude Code Entry Point

**Purpose:** Bridge between Claude Code and the SpeakOps `/skills/ directory.

## Overview

Primary skill definitions live in `/skills/[skill-name]/SKILL.md`. This file serves as the Claude Code-facing entry point to help you choose the right skill and understand quality requirements.

## Available Skills

| Skill | Purpose | When to Use |
|-------|---------|-------------|
| **phrase-extractor** | Extract Business English phrases from sources | After ingesting source material |
| **spoken-naturalness-gate** | Filter phrases for spoken naturalness | After phrase extraction |
| **voice-drill-builder** | Build ChatGPT Voice prompts | When preparing practice sessions |
| **interview-activator** | Build interview simulations | For interview preparation |
| **meeting-simulator** | Build meeting simulations | For meeting practice |
| **weak-phrase-replayer** | Replay weak phrases in new contexts | After scoring session |
| **activation-scorer** | Score phrase usage from sessions | After practice sessions |
| **weekly-eval** | Run benchmark evaluations | Weekly progress tracking |
| **source-ingestor** | Ingest source material | Starting phrase extraction |
| **phrase-card-generator** | Create phrase cards | After extraction/filtering |

## How to Choose a Skill

### For Phrase Workflows

```
Source Material → source-ingestor → phrase-extractor → spoken-naturalness-gate → phrase-card-generator
```

### For Practice Workflows

```
Phrase Bank → voice-drill-builder → [interview-activator OR meeting-simulator] → Practice Session → activation-scorer
```

### For Improvement Workflows

```
Weak Phrases → weak-phrase-replayer → New Practice Session → activation-scorer
```

### For Evaluation Workflows

```
Phrase Bank → weekly-eval → Benchmark Sessions → Readiness Report
```

## Skill Quality Requirements

Before using or modifying a skill, ensure:

### ✅ Required Components

Every skill must have:

1. **SKILL.md file** in `/skills/[skill-name]/`
   - Clear purpose and trigger conditions
   - Documented inputs and outputs
   - Explained workflow steps
   - Provided examples
   - Eval cases documented
   - Risks and limitations noted

2. **Eval coverage**
   - At least one eval rubric
   - Pass/fail criteria defined
   - Edge cases considered
   - Fail examples provided

3. **Natural language**
   - No AI-like phrasing
   - No formal/written language
   - Natural spoken Business English
   - IT/Product/AI context appropriate

### ❌ Red Flags

Avoid skills that:

- Use AI-like language ("Furthermore", "Moreover", "It is crucial to note")
- Sound too formal or written
- Lack eval coverage
- Have unclear instructions
- Missing examples
- No risks documented

## Running Evals

### When to Run Evals

**Before merging skill changes:**
- Modified SKILL.md
- Changed skill logic
- Added new examples
- Updated workflow

### How to Run Evals

```bash
# Run all evals
python scripts/run_evals.py --all

# Run specific eval
python scripts/run_evals.py --eval [eval-name]

# Run skill-specific evals
python scripts/run_evals.py --eval phrase-extraction-quality
python scripts/run_evals.py --eval spoken-naturalness
python scripts/run_evals.py --eval voice-drill-quality
```

### Interpreting Results

**Score 4–5:** PASS — Skill quality is good
**Score 3:** REVIEW — Consider improvements
**Score 1–2:** FAIL — Skill needs revision

## Updating Documentation

When a skill changes:

1. **Update SKILL.md**
   - Modify workflow steps
   - Update examples
   - Add new risks

2. **Update or add evals**
   - Create new eval cases if needed
   - Update rubrics if criteria changed
   - Add edge cases discovered

3. **Update decision log**
   - Document why skill changed
   - Note trade-offs
   - Record alternatives considered

4. **Update related docs**
   - Update workflows in `/docs/workflows/`
   - Update README if user-facing
   - Update CLAUDE.md if development process changed

## Conventions

### Spoken Naturalness

**Always prefer:**
- Short phrases (2–6 words)
- Direct but polite wording
- Natural meeting language
- IT/Product/AI context

**Always avoid:**
- "I would like to emphasize..."
- "It is crucial to note..."
- "Furthermore..."
- "Moreover..."
- Long passive sentences
- Academic language

### Privacy & Security

**Always:**
- Treat source content as untrusted
- Sanitize all inputs
- Local-only processing
- No secrets in skill definitions

**Never:**
- Include API keys
- Store personal data
- Log full transcripts by default
- Access files outside allowed paths

## Common Patterns

### Pattern 1: Phrase Extraction

```bash
# 1. Ingest source
/ingest-obsidian --path "~/vault"

# 2. Extract phrases
/extract-phrases --domain stakeholder-pushback --level b2-c1

# 3. Filter for naturalness
/filter-spoken

# 4. Build phrase cards
/build-phrase-cards --target obsidian
```

### Pattern 2: Voice Practice

```bash
# 1. Build drill
/build-voice-drill --mode meeting --scenario stakeholder-pushback

# 2. Practice session (in ChatGPT Voice)

# 3. Score session
/score-session --summary "[session summary]"

# 4. Update phrase bank
/update-phrase-bank
```

### Pattern 3: Weak Phrase Replay

```bash
# 1. Check weak phrases
/replay-weak --count 5

# 2. Practice replay session

# 3. Score session
/score-session --summary "[session summary]"
```

## Getting Help

### For Skill Issues

1. **Check SKILL.md** — Review skill documentation
2. **Check evals** — Run skill evals
3. **Check examples** — Review skill examples
4. **Review decision log** — Check for known issues

### For Quality Issues

1. **Run `/review-skill`** — Get skill review
2. **Run `/improve-repo`** — Get repository analysis
3. **Check eval results** — Identify specific issues
4. **Update documentation** — Fix identified problems

## Best Practices

### For Users

- Start with `/improve-repo` to understand current state
- Use `/review-skill` before relying on a skill
- Run evals after skill modifications
- Check decision log for context

### For Developers

- Always eval skill changes
- Document decisions in decision log
- Follow naturalness conventions
- Maintain privacy/security standards

---

**Bridge Version:** 1.0
**Last Updated:** 2025-06-28
**Primary Skills Location:** `/skills/[skill-name]/SKILL.md`
