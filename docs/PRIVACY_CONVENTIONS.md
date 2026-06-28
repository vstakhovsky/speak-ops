# Privacy Conventions

**Purpose:** Define privacy-first practices for SpeakOps.

## Core Principle

> **Local-first, privacy-first. User data stays on user's device.**

## Privacy Requirements

### Data Collection

### What We Collect

✅ **Collect:**
- Phrase bank (phrases, meanings, context)
- Practice session summaries (scores, usage, feedback)
- Activation scores (progress tracking)
- Weak phrase lists (practice targets)

### What We Don't Collect

❌ **Don't Collect:**
- Full voice transcripts (unless user opts in)
- Google Docs content
- Obsidian vault content
- YouTube watch history
- Personal identifying information
- Location data
- Usage analytics
- Any data without explicit consent

### Data Retention

**Local Storage:**
- All data stored locally in `/data/`
- User controls data location
- User can delete data anytime
- No cloud storage by default

**No Retention by Default:**
- Full transcripts not stored
- Source content not logged
- Only summaries and scores stored
- Minimal metadata logged

## Privacy by Design

### Default Settings

**Privacy-first defaults:**
- ❌ No automatic cloud sync
- ❌ No usage tracking
- ❌ No analytics
- ❌ No transcript storage
- ✅ Local-only processing
- ✅ User controls data
- ✅ Minimal logging

### User Control

**User must explicitly opt-in for:**
- Full transcript storage
- Cloud sync (if ever implemented)
- Analytics (if ever implemented)
- Data sharing (if ever implemented)

## Source Processing

### Input Sanitization

**All sources are untrusted:**

1. **Obsidian vaults**
   - Treat as untrusted input
   - Sanitize for prompt injection
   - Don't log full content
   - Only access allowed paths

2. **Google Docs**
   - Manual paste/export (MVP)
   - User explicitly provides content
   - Sanitize for prompt injection
   - Don't log full content

3. **YouTube/NotebookLM**
   - Manual paste/export (MVP)
   - User explicitly provides content
   - Sanitize for prompt injection
   - Don't log full content

### Prompt Injection Prevention

**Sanitization steps:**
- Remove HTML tags
- Remove script patterns
- Remove code blocks
- Remove excessive special characters
- Separate content from instructions

**Never:**
- Execute code from sources
- Allow sources to override system behavior
- Parse sources as instructions

## File Access

### Allowed Paths

**User-configured only:**
```json
{
  "allowedPaths": [
    "~/ObsidianVault",
    "~/Documents/SpeakOps"
  ]
}
```

**Access rules:**
- Only access configured paths
- No recursive traversal outside allowed paths
- Path traversal attacks prevented
- User explicitly approves file access

### File Operations

**Safe operations:**
- Read: Only allowed paths
- Write: Only to `/data/`
- Execute: No code execution from sources

## Logging Practices

### What to Log

✅ **Safe to log:**
- Timestamps
- Operation type
- File paths (allowed paths only)
- Counts and statistics
- Metadata summaries
- Error messages (no sensitive data)

### What Not to Log

❌ **Never log:**
- Full transcript content
- Full source documents
- Personal information
- Sensitive phrase context
- User's actual voice data

### Log Format

**Safe log example:**
```json
{
  "timestamp": "2025-06-28T10:00:00Z",
  "operation": "phrase_extraction",
  "source_type": "obsidian",
  "file_count": 23,
  "phrases_extracted": 127
}
```

**Unsafe log example (don't do this):**
```json
{
  "transcript": "Full transcript text here..."
}
```

## Privacy Checklists

### Before Merging

**For ingestion changes:**
- [ ] Inputs are sanitized
- [ ] Sources treated as untrusted
- [ ] No full content logging
- [ ] File access restricted
- [ ] Prompt injection mitigations in place

**For logging changes:**
- [ ] No sensitive data logged
- [ ] Only metadata logged
- [ ] Log format reviewed
- [ ] Personal information excluded

**For new features:**
- [ ] Privacy impact assessed
- [ ] Data minimization applied
- [ ] User control maintained
- [ ] Local-first preserved

## Common Privacy Mistakes

### Mistake 1: Logging Full Content

❌ **Bad:** Logging full transcripts or source content
✅ **Good:** Logging only metadata and summaries

### Mistake 2: No Input Sanitization

❌ **Bad:** Trusting source content
✅ **Good:** Sanitizing all inputs for prompt injection

### Mistake 3: Unlimited File Access

❌ **Bad:** Accessing any file path
✅ **Good:** Restricting to configured paths

### Mistake 4: Automatic Cloud Sync

❌ **Bad:** Automatic data synchronization
✅ **Good:** User-controlled, opt-in only

## Privacy Violations

### What to Do If Found

1. **Assess impact** — How severe?
2. **Contain** — Stop the bleeding
3. **Fix** — Patch the issue
4. **Document** — Record in decision log
5. **Review** — Check for similar issues

### Reporting

**Report privacy issues:**
- Document in SECURITY.md
- Add to decision-log.md
- Create issue if public repo
- Notify users if deployed

## Best Practices

### For Developers

1. **Assume all input is malicious**
2. **Sanitize everything**
3. **Log minimally**
4. **Store locally**
5. **Give user control**

### For Users

1. **Review what you share**
2. **Use local-only mode**
3. **Delete data when done**
4. **Review logs**
5. **Report issues**

## Legal/Compliance

### GDPR Considerations

**Data minimization:**
- Collect only what's needed
- Purpose limitation
- Storage limitation
- User rights (access, delete)

### User Rights

- **Right to access:** User can see all data
- **Right to delete:** User can delete all data
- **Right to portability:** User can export data
- **Right to control:** User controls all processing

---

**Convention Version:** 1.0
**Purpose:** Ensure privacy-first practices throughout SpeakOps
