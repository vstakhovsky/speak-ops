# Google Docs Ingestion Workflow

## Overview

This workflow describes how to ingest phrases from Google Docs into SpeakOps.

**Important:** For MVP, there is no Google Docs API integration. User must manually export/paste content.

## Process

### Step 1: Export Google Doc

1. Open the Google Doc
2. Select all content (Cmd+A / Ctrl+A)
3. Copy (Cmd+C / Ctrl+C)

### Step 2: Create local text file

```bash
# Create a temporary file
cat > /tmp/gdoc_content.txt
# Paste the content
# Press Ctrl+D to save
```

### Step 3: Run ingestion

```bash
# Use Claude Code to process the content
claude

# In Claude Code:
/extract-phrases --source /tmp/gdoc_content.txt --domain <domain>
```

## Alternative: Direct Paste

You can also paste the content directly into Claude Code:

```bash
claude

# In Claude Code:
/source-ingestor

[Paste Google Doc content]

[Ctrl+D to end input]
```

## Privacy Considerations

- Google Doc content is NOT automatically uploaded
- User explicitly provides content
- Content is processed locally
- No API keys required
- No Google Docs access permissions needed

## Security

- Treat Google Doc content as untrusted
- Sanitize all inputs
- Remove HTML, scripts, injection vectors
- Don't log full doc content

## Output

After ingestion, you'll have:

- Extracted phrases
- Filtered for spoken naturalness
- Metadata (Russian meaning, context, examples)
- Ready for phrase card generation

## Next Steps

After ingestion:

1. Review extracted phrases
2. Adjust domain filtering if needed
3. Generate phrase cards:
   ```bash
   /build-phrase-cards --target obsidian
   ```
4. Build voice drill:
   ```bash
   /build-voice-drill --mode interview --session 1
   ```

---

**Workflow ID:** gdoc-ingestion
**Status:** Manual (MVP)
