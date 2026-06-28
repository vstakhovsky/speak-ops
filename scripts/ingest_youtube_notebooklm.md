# YouTube / NotebookLM Ingestion Workflow

## Overview

This workflow describes how to ingest phrases from YouTube videos using NotebookLM or Gemini transcripts into SpeakOps.

**Important:** For MVP, there is no YouTube API integration. User must manually provide transcript/notes.

## Process

### Step 1: Get Video Transcript/Notes

**Option A: NotebookLM**
1. Open NotebookLM (notebooklm.google.com)
2. Create new notebook
3. Add YouTube video URL
4. Let NotebookLM generate notes/summary
5. Copy the notes

**Option B: Gemini**
1. Open Gemini (gemini.google.com)
2. Upload YouTube video or provide URL
3. Ask for transcript or summary
4. Copy the output

**Option C: Manual transcript**
1. Watch video with captions
2. Copy caption text
3. Or use transcript service

### Step 2: Create local text file

```bash
# Create a temporary file
cat > /tmp/youtube_notes.txt
# Paste the transcript/notes
# Press Ctrl+D to save
```

### Step 3: Run ingestion

```bash
# Use Claude Code to process the content
claude

# In Claude Code:
/extract-phrases --source /tmp/youtube_notes.txt --domain ai-evals
```

## Alternative: Direct Paste

You can also paste the content directly into Claude Code:

```bash
claude

# In Claude Code:
/source-ingestor

[Paste YouTube transcript/notes]

[Ctrl+D to end input]
```

## Domains

For YouTube conference videos, common domains:

- `ai-evals` — AI evaluation and governance
- `technical-pm` — Technical product management
- `senior-pm` — Senior product management
- `machine-learning` — ML/AI technical discussions
- `research` — Research and engineering

## Privacy Considerations

- YouTube content is public
- Transcript/notes are processed locally
- No API keys required
- No YouTube access permissions needed
- Viewing is not tracked

## Security

- Treat transcript content as untrusted
- Sanitize all inputs
- Remove timestamps, metadata
- Don't log full transcripts

## Output

After ingestion, you'll have:

- AI/evals related phrases
- Technical terminology
- Conference vocabulary
- Filtered for spoken naturalness
- Ready for phrase card generation

## Example Use Cases

### Use Case 1: AI Evaluation Conference
**Source:** NeurIPS or ICML conference talk
**Domain:** ai-evals
**Target phrases:** evaluation metrics, benchmarking, model behavior

### Use Case 2: Technical PM Discussion
**Source:** Lenny's Podcast or similar
**Domain:** technical-pm
**Target phrases:** roadmap prioritization, stakeholder alignment

### Use Case 3: Engineering Leadership
**Source:** Engineering leadership talk
**Domain:** senior-pm
**Target phrases:** managing teams, technical decisions

## Next Steps

After ingestion:

1. Review extracted AI/evals phrases
2. Adjust domain filtering if needed
3. Generate phrase cards:
   ```bash
   /build-phrase-cards --target obsidian
   ```
4. Build voice drill:
   ```bash
   /build-voice-drill --mode ai-evals-discussion
   ```

---

**Workflow ID:** youtube-notebooklm-ingestion
**Status:** Manual (MVP)
