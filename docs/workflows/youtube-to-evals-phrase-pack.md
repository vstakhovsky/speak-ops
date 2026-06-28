# Workflow 3: YouTube/NotebookLM to AI/Evals Phrase Pack

## Overview

Convert a YouTube conference video (via NotebookLM or Gemini notes) into an AI/evals phrase pack and technical discussion drill.

## Prerequisites

- YouTube video URL or transcript
- Access to NotebookLM or Gemini (optional)
- Claude Code installed

## Steps

### Step 1: Get Video Content

**Option A: NotebookLM**

1. Go to notebooklm.google.com
2. Create new notebook
3. Add YouTube video URL
4. Let NotebookLM generate summary/notes
5. Copy notes

**Option B: Gemini**

1. Go to gemini.google.com
2. Upload or provide YouTube URL
3. Ask for transcript or summary
4. Copy output

**Option C: Manual transcript**

1. Watch video with captions
2. Copy caption text
3. Or use transcript service

### Step 2: Ingest Video Content

```bash
cat > /tmp/youtube_notes.txt
[Paste notes/transcript]
^D

/ingest-youtube --source /tmp/youtube_notes.txt --via notebooklm
```

**What happens:**
1. Source-ingestor reads content
2. Removes timestamps/metadata
3. Sanitizes for prompt injection
4. Passes to phrase-extractor

**Output:**
- Cleaned text
- Video metadata (title, source)

### Step 3: Extract AI/Evals Phrases

```bash
/extract-phrases --domain ai-evals --level c1-c2
```

**What happens:**
1. Phrase-extractor analyzes content
2. Identifies AI/evals terminology
3. Extracts technical phrases
4. Filters for AI/Product context

**Output:**
- AI/evals phrases
- Technical meanings
- Context examples

### Step 4: Filter for Technical Naturalness

```bash
/filter-spoken --domain ai-evals
```

**What happens:**
1. Spoken-naturalness-gate evaluates technical phrases
2. Ensures phrases sound natural in technical discussions
3. Rejects overly academic phrases
4. Provides spoken alternatives

**Output:**
- Natural technical phrases
- Spoken technical examples
- Context: technical PM discussions

### Step 5: Build AI/Evals Phrase Pack

```bash
/build-phrase-cards --domain ai-evals --target markdown
```

**What happens:**
1. Phrase-card-generator creates cards
2. Organizes by AI/evals subtopics
3. Adds technical context
4. Outputs markdown file

**Output:**
- AI/evals phrase pack (markdown)
- Organized by subtopics
- Ready for review

**Subtopics:**
- Evaluation metrics
- Benchmark design
- Model behavior
- Testing strategies
- Governance
- Technical trade-offs

### Step 6: Build Technical Discussion Drill

```bash
/build-voice-drill --mode ai-evals-discussion --scenario evaluation-strategy
```

**What happens:**
1. Meeting-simulator creates scenario
2. Selects AI/evals phrases
3. Creates technical PM discussion
4. Generates ChatGPT Voice prompt
5. Creates technical scoring rubric

**Output:**
- Technical discussion drill
- CTO-style pushback scenario
- Technical scoring rubric

**Scenario examples:**
- Evaluation strategy discussion
- Model behavior review
- Benchmark design debate
- Governance conversation

### Step 7: Practice Technical Discussion

1. Copy ChatGPT Voice prompt
2. Start technical discussion
3. Practice explaining technical concepts
4. Use AI/evals phrases naturally
5. Handle technical pushback

### Step 8: Score Technical Session

```bash
/score-session --summary "[technical session summary]"
```

**Example summary:**
```
Technical PM discussion about evaluation strategy.

Used: "at scale" (natural), "trade-off" (correct), "latency vs accuracy" (natural)
Missed: "baseline", "production-grade"
Incorrect: "utilize the model" → better: "use the model"
Too formal: "It is imperative to establish" → better: "We need to set up"
```

**What happens:**
1. Activation-scorer analyzes technical usage
2. Scores phrase activation
3. Checks technical correctness
4. Identifies weak technical phrases

**Output:**
- Updated activation scores
- Weak technical phrases
- Technical usage feedback

### Step 9: Update Phrase Bank

```bash
/update-phrase-bank
```

**What happens:**
1. Updates phrases.csv with AI/evals phrases
2. Updates status levels
3. Saves weak technical phrases
4. Logs technical session

**Output:**
- Updated phrase bank with AI/evals phrases
- Weak technical phrases identified
- Session logged

## Example: Full Workflow

**Input:** NeurIPS conference talk on evaluation

```bash
# Step 1-2: Get and ingest content
# (From NotebookLM)

/ingest-youtube --source /tmp/neurips_talk.txt --via notebooklm
# Output: 8,500 words, NeurIPS talk on evaluation

# Step 3: Extract AI/evals phrases
/extract-phrases --domain ai-evals --level c2
# Output: 156 AI/evals phrases extracted

# Step 4: Filter
/filter-spoken --domain ai-evals
# Output: 112 phrases passed technical naturalness filter

# Step 5: Build phrase pack
/build-phrase-cards --domain ai-evals --target markdown
# Output: AI/evals phrase pack created (112 phrases)

# Step 6: Build drill
/build-voice-drill --mode ai-evals-discussion --scenario evaluation-strategy
# Output: Technical PM discussion drill with 8 phrases

# Step 7-8: Practice and score
# Technical session completed

# Step 9: Update
/update-phrase-bank
# Output: Updated 8 phrases, 3 weak technical phrases identified
```

## YouTube Video Types

### Type 1: Conference Talks
**Conferences:** NeurIPS, ICML, ACL, CHI
**Focus:** Research papers, technical concepts
**Phrases:** Technical terminology, research methodology

### Type 2: Technical Podcasts
**Shows:** Lenny's Podcast, Machine Learning Street Talk
**Focus:** Applied AI, product discussions
**Phrases:** Technical PM, business trade-offs

### Type 3: Engineering Talks
**Sources:** Engineering conferences, tech talks
**Focus:** Implementation, architecture
**Phrases:** Engineering practices, technical decisions

## AI/Evals Subtopics

| Subtopic | Example Phrases |
|----------|----------------|
| Evaluation metrics | precision/recall, F1, AUC, calibration |
| Benchmark design | golden set, human eval, adversarial testing |
| Model behavior | hallucination, bias, fairness, robustness |
| Testing strategies | red teaming, prompt injection, edge cases |
| Governance | ethical guidelines, compliance, oversight |
| Technical trade-offs | latency vs accuracy, cost vs quality |

## Privacy Notes

- YouTube content is public
- Notes/transcript processed locally
- No YouTube API integration (MVP)
- Content sanitized for prompt injection
- No full transcript logging

## Time Estimate

- Steps 1–2: 10–15 minutes (manual, depending on video)
- Steps 3–5: 15 minutes (automated)
- Step 6: 3 minutes
- Step 7: 5–10 minutes (voice session)
- Steps 8–9: 3 minutes

**Total:** 40–50 minutes

## Next Steps

After completing workflow:

1. **Review phrase pack** — Learn AI/evals terminology
2. **Practice technical discussions** — Build technical fluency
3. **Explore subtopics** — Master specific AI/evals areas
4. **Track technical progress** — Monitor activation scores

## Troubleshooting

**Problem:** Too few technical phrases extracted
- **Solution:** Try broader domain (technical-pm instead of ai-evals)

**Problem:** Phrases too academic
- **Solution:** Use `/filter-spoken` with stricter criteria

**Problem:** Technical scenario unrealistic
- **Solution:** Provide more context about your technical level

**Problem:** Scoring doesn't recognize technical correctness
- **Solution:** Report as eval issue, provide technical context

---

**Workflow ID:** youtube-to-evals-phrase-pack
**Status:** Active
