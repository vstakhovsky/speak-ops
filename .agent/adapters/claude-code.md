# Claude Code Adapter

## Purpose

Define how SpeakOps integrates with Claude Code.

## Overview

SpeakOps is designed to work with Claude Code as the primary interface.

## Integration Points

### 1. Skills

SpeakOps provides Claude Code skills:

- **phrase-extractor** — Extract phrases from sources
- **spoken-naturalness-gate** — Filter for naturalness
- **voice-drill-builder** — Build voice drills
- **interview-activator** — Build interview drills
- **meeting-simulator** — Build meeting drills
- **weak-phrase-replayer** — Replay weak phrases
- **activation-scorer** — Score sessions
- **weekly-eval** — Run weekly benchmarks
- **source-ingestor** — Ingest source material
- **phrase-card-generator** — Generate phrase cards

### 2. Commands

Conceptual commands (implemented via skills):

```bash
/ingest-obsidian --path "<vault-path>"
/ingest-gdoc --source <file>
/ingest-youtube --source <file>
/extract-phrases --domain <domain> --level <level>
/filter-spoken
/build-phrase-cards --target <target>
/build-voice-drill --mode <mode> --scenario <scenario>
/score-session --transcript <file> | --summary <text>
/update-phrase-bank
/replay-weak --count <n>
/weekly-eval
```

### 3. Data Files

Claude Code reads/writes to:

- `data/phrases.csv` — Phrase bank
- `data/sessions.jsonl` — Session logs
- `data/scores.jsonl` — Score history
- `data/weak_phrases.jsonl` — Weak phrases

### 4. Scripts

Claude Code can execute:

- `scripts/ingest_obsidian.py` — Obsidian ingestion
- `scripts/score_session.py` — Session scoring
- `scripts/update_phrase_bank.py` — Phrase bank updates
- `scripts/run_evals.py` — Eval runner

## Usage Patterns

### Pattern 1: Skill Invocation

User invokes skill directly:

```bash
claude

> /voice-drill-builder --mode interview --scenario stakeholder-conflict
```

### Pattern 2: Script Execution

Claude Code executes script:

```bash
python scripts/score_session.py --summary "[session summary]"
```

### Pattern 3: File Operations

Claude Code reads/writes files:

```bash
# Read phrase bank
Read data/phrases.csv

# Write phrase cards
Write templates/phrase-card.md
```

## Session Flow

### Typical Session

1. **Start Claude Code**
   ```bash
   claude
   ```

2. **Invoke skill**
   ```
   > /build-voice-drill --mode meeting --scenario stakeholder-pushback
   ```

3. **Receive output**
   - Voice drill prompt
   - Practice log template
   - Scoring rubric

4. **Use output**
   - Copy prompt to ChatGPT Voice
   - Run voice session
   - Return with summary

5. **Score session**
   ```
   > /score-session --summary "[summary]"
   ```

6. **Update phrase bank**
   ```
   > /update-phrase-bank
   ```

## Error Handling

### Skill Errors

**If skill fails:**
1. Error message displayed
2. Suggested fix provided
3. User can retry

### Script Errors

**If script fails:**
1. Error output displayed
2. Stack trace if debug mode
3. Suggested fix provided

### File Errors

**If file operation fails:**
1. Error message displayed
2. File permissions checked
3. Suggested workaround provided

## Configuration

### Claude Code Settings

**In `.claude/settings.json`:**

```json
{
  "allowedPaths": [
    "~/ObsidianVault",
    "~/Documents/SpeakOps"
  ],
  "skills": [
    "phrase-extractor",
    "spoken-naturalness-gate",
    "voice-drill-builder",
    "interview-activator",
    "meeting-simulator",
    "weak-phrase-replayer",
    "activation-scorer",
    "weekly-eval",
    "source-ingestor",
    "phrase-card-generator"
  ]
}
```

## Permissions

### Required Permissions

**File access:**
- Read: `data/`, `templates/`, `evals/`
- Write: `data/`, `voice-hooks/alerts.jsonl`

**Script execution:**
- Execute: `scripts/*.py`

**Bash commands:**
- Read files
- Write files
- Execute Python scripts

### Safety

**All inputs:**
- Sanitized for prompt injection
- Validated for security
- Checked against allowed paths

## Best Practices

### For Users

1. **Start Claude Code in repo**
   ```bash
   cd ~/Projects/speak-ops
   claude
   ```

2. **Use skills for workflows**
   - Skills handle complex tasks
   - Scripts handle automation
   - File operations for simple tasks

3. **Review outputs**
   - Check generated drills
   - Verify scoring results
   - Review extracted phrases

### For Development

1. **Skill design**
   - Clear trigger conditions
   - Well-defined inputs/outputs
   - Eval cases documented

2. **Script design**
   - Minimal dependencies
   - Clear error messages
   - Ponytail shortcuts marked

3. **Integration**
   - Test with Claude Code
   - Verify permissions
   - Document usage

## Troubleshooting

### Issue: Skill not found

**Solution:**
- Check skill is in `skills/` directory
- Verify SKILL.md exists
- Restart Claude Code

### Issue: Script fails

**Solution:**
- Check Python version (3.13+)
- Verify script permissions
- Check error output

### Issue: File access denied

**Solution:**
- Check allowedPaths in settings
- Verify file permissions
- Check path is within allowed paths

## Future Enhancements

**Potential additions:**
- Real-time voice session integration
- Automatic transcript capture
- Calendar integration for reminders
- Webhook support for alerts

---

**Adapter Version:** 1.0
**Status:** Active
