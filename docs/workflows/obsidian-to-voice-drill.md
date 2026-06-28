# Workflow 1: Obsidian Phrase Bank to Voice Drill

## Overview

Convert Obsidian markdown notes with phrases into a ready-to-use ChatGPT Voice drill.

## Prerequisites

- Obsidian vault with phrase notes
- Phrases marked or tagged appropriately
- Claude Code installed

## Steps

### Step 1: Ingest Obsidian Content

```bash
/ingest-obsidian --path "/Users/user/ObsidianVault/Phrases"
```

**What happens:**
1. Script scans vault for markdown files
2. Extracts text content
3. Sanitizes content
4. Passes to phrase-extractor

**Output:**
- Raw text from Obsidian
- Metadata (files scanned, word count)

### Step 2: Extract Phrases

```bash
/extract-phrases --domain <domain> --level <level>
```

**Example:**
```bash
/extract-phrases --domain stakeholder-pushback --level b2-c1
```

**What happens:**
1. Phrase-extractor skill analyzes text
2. Identifies useful Business English phrases
3. Filters by domain and level
4. Passes to spoken-naturalness-gate

**Output:**
- Extracted phrases with metadata
- Russian meanings
- Context examples
- Natural spoken versions

### Step 3: Filter for Spoken Naturalness

```bash
/filter-spoken --remove-ai-like
```

**What happens:**
1. Spoken-naturalness-gate evaluates each phrase
2. Rejects or rewrites formal/AI-like phrases
3. Provides better spoken alternatives
4. Scores naturalness (1–5)

**Output:**
- Filtered phrases (naturalness ≥ 4)
- Better spoken versions
- Confident and softer variations

### Step 4: Build Phrase Cards

```bash
/build-phrase-cards --target obsidian
```

**What happens:**
1. Phrase-card-generator creates cards
2. Formats for Obsidian markdown
3. Includes all metadata
4. Saves to vault

**Output:**
- Phrase cards in Obsidian
- Organized by domain
- Ready for review

### Step 5: Build Voice Drill

```bash
/build-voice-drill --mode meeting --scenario stakeholder-pushback
```

**What happens:**
1. Voice-drill-builder selects 5–8 phrases
2. Creates realistic meeting scenario
3. Generates ChatGPT Voice prompt
4. Creates practice log template
5. Creates scoring rubric

**Output:**
- Ready-to-paste ChatGPT Voice prompt
- Practice log template
- Scoring rubric

### Step 6: Practice Session

1. Copy ChatGPT Voice prompt
2. Paste into ChatGPT Voice
3. Run voice session (5–10 minutes)
4. Note which phrases you used
5. Note AI feedback

### Step 7: Score Session

```bash
/score-session --summary "[session summary]"
```

**Example summary:**
```
Used: push back on (yes, correct, natural), loop in (yes, correct, natural)
Missed: align on, table this
Too formal: Therefore we should (should use "So let's")
```

**What happens:**
1. Activation-scorer analyzes usage
2. Updates activation scores
3. Identifies weak phrases
4. Generates score report

**Output:**
- Updated activation scores
- Weak phrase list
- Session summary

### Step 8: Update Phrase Bank

```bash
/update-phrase-bank
```

**What happens:**
1. Updates phrases.csv with new scores
2. Updates status levels
3. Saves weak phrases for replay
4. Logs session

**Output:**
- Updated phrase bank
- Weak phrases identified
- Session logged

## Example: Full Workflow

```bash
# Step 1: Ingest
/ingest-obsidian --path "~/ObsidianVault/PMPhrases"
# Output: Scanned 23 files, 45,000 words

# Step 2: Extract
/extract-phrases --domain stakeholder-pushback --level b2
# Output: Extracted 127 phrases

# Step 3: Filter
/filter-spoken
# Output: 89 phrases passed naturalness filter

# Step 4: Build cards
/build-phrase-cards --target obsidian
# Output: Created 89 phrase cards

# Step 5: Build drill
/build-voice-drill --mode meeting --scenario stakeholder-pushback
# Output: Drill with 8 phrases created

# Step 6-7: Practice and score (done outside Claude Code)
# Session completed

# Step 8: Update
/update-phrase-bank
# Output: Updated 8 phrases, 3 weak phrases identified
```

## Time Estimate

- Steps 1–4: 10–15 minutes (mostly automated)
- Step 5: 2–3 minutes
- Step 6: 5–10 minutes (voice session)
- Steps 7–8: 2–3 minutes

**Total:** 20–30 minutes

## Next Steps

After completing workflow:

1. **Review weak phrases** — Identify phrases to replay
2. **Plan next drill** — Choose scenario for weak phrases
3. **Schedule practice** — Set daily drill reminder
4. **Track progress** — Review activation scores

## Troubleshooting

**Problem:** No phrases extracted
- **Solution:** Check domain filter, try broader domain

**Problem:** Too many formal phrases
- **Solution:** Run `/filter-spoken` again with stricter criteria

**Problem:** Drill doesn't force phrase usage
- **Solution:** Report as eval failure, regenerate drill

**Problem:** Scores don't update
- **Solution:** Check session summary format, ensure phrase names match

---

**Workflow ID:** obsidian-to-voice-drill
**Status:** Active
