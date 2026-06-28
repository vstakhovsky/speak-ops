# Workflow 2: Google Docs Phrase List to Voice Drill

## Overview

Convert a Google Docs phrase list into a ready-to-use ChatGPT Voice drill for interview practice.

## Prerequisites

- Google Doc with phrase list
- Access to Google Doc
- Claude Code installed

## Steps

### Step 1: Export Google Doc

**Manual export (MVP):**

1. Open Google Doc
2. Select all (Cmd+A)
3. Copy (Cmd+C)
4. Paste into local file:

```bash
cat > /tmp/gdoc_phrases.txt
# Paste content
# Press Ctrl+D
```

**Alternative:** Use Google Docs "Download as → Plain Text"

### Step 2: Ingest Google Doc Content

```bash
/ingest-gdoc --source /tmp/gdoc_phrases.txt
```

**What happens:**
1. Source-ingestor reads content
2. Sanitizes for prompt injection
3. Removes HTML/formatting
4. Passes to phrase-extractor

**Output:**
- Cleaned text content
- Metadata (word count, source)

### Step 3: Extract Phrases

```bash
/extract-phrases --domain <domain> --level <level>
```

**Example:**
```bash
/extract-phrases --domain senior-pm-interview --level c1
```

**What happens:**
1. Phrase-extractor analyzes text
2. Identifies interview-relevant phrases
3. Adds metadata (Russian, context, examples)
4. Filters by level

**Output:**
- Interview phrases with metadata
- Spoken examples
- Avoided formal versions

### Step 4: Filter for Naturalness

```bash
/filter-spoken --remove-ai-like
```

**What happens:**
1. Spoken-naturalness-gate evaluates phrases
2. Rejects formal/AI-like phrases
3. Provides spoken alternatives
4. Flags interview-appropriate language

**Output:**
- Natural spoken phrases
- Interview-ready versions
- Confidence vs diplomatic variations

### Step 5: Build Interview Drill

```bash
/build-voice-drill --mode interview --scenario tell-me-about-yourself
```

**What happens:**
1. Interview-activator creates scenario
2. Selects 5–8 target phrases
3. Generates ChatGPT Voice prompt
4. Creates practice log
5. Creates interview scoring rubric

**Output:**
- Interview drill prompt
- Practice log template
- Interview scoring rubric

### Step 6: Practice Session

1. Copy ChatGPT Voice prompt
2. Start ChatGPT Voice session
3. Practice interview answer (5–10 minutes)
4. Note AI feedback on phrase usage
5. Self-reflect on naturalness

### Step 7: Score Session

```bash
/score-session --summary "[summary]"
```

**Example summary:**
```
Tell me about yourself answer.

Used: "worked on" (natural), "responsible for" (too formal), "led the team" (natural)
Missed: "spearheaded", "drove the initiative"
Too formal: "I was tasked with" → better: "I handled"
```

**What happens:**
1. Activation-scorer analyzes usage
2. Scores phrase activation (0–100)
3. Identifies weak phrases
4. Suggests improvements

**Output:**
- Updated activation scores
- Weak phrase list
- Better spoken versions

### Step 8: Update Phrase Bank

```bash
/update-phrase-bank
```

**What happens:**
1. Updates phrases.csv
2. Updates status levels
3. Saves session to sessions.jsonl
4. Logs weak phrases

**Output:**
- Updated phrase bank
- Session log
- Weak phrases for replay

## Example: Full Workflow

**Input:** Google Doc with 50 interview phrases

```bash
# Step 1-2: Export and ingest
cat > /tmp/interview_phrases.txt
[Paste Google Doc content]
^D

/ingest-gdoc --source /tmp/interview_phrases.txt
# Output: 3,200 words, 50 phrases

# Step 3: Extract
/extract-phrases --domain senior-pm-interview --level c1
# Output: 42 interview phrases extracted

# Step 4: Filter
/filter-spoken
# Output: 35 phrases passed naturalness filter

# Step 5: Build drill
/build-voice-drill --mode interview --scenario stakeholder-conflict
# Output: Interview drill with 7 phrases

# Step 6-7: Practice and score
# Session completed with summary

# Step 8: Update
/update-phrase-bank
# Output: Updated 7 phrases, 2 weak phrases identified
```

## Google Doc Format Tips

**Good format:**
```
push back on — возразить против
Use when disagreeing with stakeholder requests
Example: "I'd push back on that timeline"

loop in — подключать к обсуждению
Use when need to involve someone
Example: "Let's loop in engineering"
```

**Avoid:**
- Complex formatting
- Tables (convert to list)
- Images (skip)
- Links (extract text only)

## Privacy Notes

- Google Doc content is processed locally
- No API integration for MVP
- User explicitly provides content
- Content is not logged by default
- Sanitized for prompt injection

## Time Estimate

- Steps 1–2: 5 minutes (manual export)
- Steps 3–5: 10 minutes (automated)
- Step 6: 5–10 minutes (voice session)
- Steps 7–8: 3 minutes (automated)

**Total:** 25–30 minutes

## Next Steps

After completing workflow:

1. **Review formal phrases** — Identify phrases to soften
2. **Practice weak phrases** — Schedule replay session
3. **Build more drills** — Try other interview scenarios
4. **Track progress** — Monitor activation scores

## Troubleshooting

**Problem:** Phrases not extracting
- **Solution:** Check Google Doc format, use plain text

**Problem:** Too many formal phrases
- **Solution:** Review `/filter-spoken` output, adjust level

**Problem:** Interview scenario unrealistic
- **Solution:** Try different scenario or provide context

**Problem:** Phrases not recognized in scoring
- **Solution:** Ensure exact phrase match in summary

---

**Workflow ID:** gdoc-to-voice-drill
**Status:** Active
