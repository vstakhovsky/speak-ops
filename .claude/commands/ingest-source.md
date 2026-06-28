# Ingest Source Material

**Purpose:** Import text content from Obsidian vaults, Google Docs, or YouTube transcripts for phrase extraction.

## When to Use

- You have new source material with Business English phrases
- Starting to build a phrase bank from scratch
- Adding phrases in a new domain (AI/evals, technical PM, etc.)
- After meetings, interviews, or conferences with useful vocabulary

## Inputs

```bash
# For Obsidian vaults
/ingest-obsidian --path "~/ObsidianVault/Phrases"

# For Google Docs (exported text)
/ingest-gdoc --source /tmp/gdoc_content.txt

# For YouTube/NotebookLM transcripts
/ingest-youtube --source /tmp/transcript.txt --via notebooklm
```

## Workflow Steps

1. **Validate input**
   - Check file exists
   - Verify file is within allowed paths
   - Check file size (< 10MB)

2. **Sanitize content**
   - Remove HTML tags
   - Remove script patterns
   - Remove excessive whitespace
   - Strip formatting

3. **Extract text**
   - Parse source content
   - Extract meaningful text
   - Count words

4. **Output metadata**
   - Source type and location
   - Word count
   - Text preview (first 500 chars)
   - Timestamp

5. **Pass to phrase-extractor**
   - Call phrase-extractor skill
   - Provide sanitized text
   - Return extracted phrases

## Output Format

```json
{
  "status": "success",
  "source_type": "obsidian|gdoc|youtube",
  "source_path": "/path/to/source",
  "word_count": 4500,
  "text_preview": "First 500 characters...",
  "timestamp": "2025-06-28T10:00:00Z"
}
```

## Safety & Privacy Notes

⚠️ **Security:**
- Source content is treated as untrusted
- All inputs are sanitized for prompt injection
- File access is restricted to configured paths
- No automatic API calls to external services

🔒 **Privacy:**
- Source content is NOT logged by default
- Only metadata is stored
- User must explicitly opt-in to save full content
- Google Docs/YouTube require manual export (no API keys)

## Related Skills

- **phrase-extractor** — Extracts phrases from ingested content
- **spoken-naturalness-gate** — Filters extracted phrases
- **source-ingestor** — Core ingestion skill

## Related Evals

- **privacy-security** — Ensures safe ingestion
- **prompt-injection** — Tests against malicious inputs

## Example

```bash
# Ingest Obsidian vault
/ingest-obsidian --path "~/ObsidianVault/PMPhrases"

# Output
{
  "status": "success",
  "source_type": "obsidian",
  "source_path": "/Users/user/ObsidianVault/PMPhrases",
  "word_count": 12345,
  "text_preview": "push back on — to object to...",
  "timestamp": "2025-06-28T14:30:00Z"
}
```

---

**Command Version:** 1.0
**Status:** Active
