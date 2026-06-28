# SpeakOps — Security and Privacy Model

SpeakOps is a **local-first** system. Security and privacy are foundational.

## Core Principles

1. **Local-first** — Data stays on user's machine by default
2. **Minimal retention** — Keep only what's necessary
3. **No secrets** — No API keys, credentials, or tokens
4. **Untrusted inputs** — All external sources treated as untrusted
5. **Defensive defaults** — Safe by default, explicit opt-in for sharing

## Threat Model

### Assets

| Asset | Sensitivity | Storage |
|-------|-------------|---------|
| Phrase bank | Low | Local CSV |
| Practice transcripts | Medium | Local JSONL (optional) |
| Google Docs content | High | Not logged |
| Obsidian vault path | Medium | Local config |
| YouTube transcripts | Low | Local cache |
| Activation scores | Low | Local JSONL |

### Threats

| Threat | Impact | Mitigation |
|--------|--------|------------|
| Secret leakage | High | No secrets in repo |
| Privacy leak | High | Local-first, minimal logging |
| Prompt injection | Medium | Sanitize inputs, separate instructions |
| Unsafe file access | Medium | Configured allow paths |
| Dependency vulns | Medium | Minimal dependencies |
| Data loss | Low | User controls data |

### Attacker Model

- **Assume:** User's machine is compromised
- **Assume:** Imported sources are malicious (prompt injection)
- **Assume:** Dependencies have vulnerabilities
- **Do not assume:** Network is safe
- **Do not assume:** External services are available

## Security Rules

### Must Do

- Sanitize all imported content
- Treat source files as untrusted
- Separate source text from instructions
- Support local-only mode
- Document all permissions
- Provide minimal data retention mode

### Must Not Do

- Store API keys in repo
- Commit credentials
- Log full private Google Docs content
- Store full voice transcripts by default
- Execute arbitrary commands from sources
- Allow imported text to override system instructions
- Add external network calls without approval
- Process files outside configured paths

## Privacy Model

### Data Collection

SpeakOps collects:

- **Phrase bank** — User's phrases with metadata
- **Sessions** — Practice session summaries (optional)
- **Scores** — Activation scores per phrase
- **Weak phrases** — Phrases needing replay

SpeakOps does NOT collect by default:

- Full voice transcripts
- Google Docs content
- Obsidian vault content
- YouTube watch history
- Personal identifying information

### Data Retention

| Data | Retention | User Control |
|------|-----------|--------------|
| Phrases | Indefinite | User can delete |
| Session summaries | Indefinite | User can delete |
| Full transcripts | Not stored | User opt-in |
| Source content | Not logged | N/A |

### Data Sharing

SpeakOps does NOT share data externally. All processing happens locally.

## Prompt Injection

### Threat

Malicious sources (Google Docs, Obsidian, YouTube transcripts) may attempt to:

- Override system instructions
- Exfiltrate data
- Modify scoring logic
- Inject harmful phrases

### Mitigations

1. **Separation** — Source text separated from instructions
2. **Sanitization** — Remove or escape special characters
3. **Validation** — Reject malformed inputs
4. **Sandboxing** — No code execution from sources
5. **Review** — User reviews extracted phrases before use

## File Access

### Allowed Paths

User configures allowed paths in `.claude/settings.json`:

```json
{
  "allowedPaths": [
    "/Users/user/ObsidianVault",
    "/Users/user/Documents/SpeakOps"
  ]
}
```

### Access Control

- Scripts only access configured paths
- User explicitly approves file access
- No recursive traversal outside allowed paths
- Obsidian ingestion requires explicit vault path

## External Services

### Policy

- No external API calls by default
- No third-party services required
- User must explicitly approve network calls
- All network calls logged

### Optional Integrations

| Service | Purpose | Required | User Approval |
|---------|---------|----------|---------------|
| Google Docs | Phrase import | No | Yes |
| YouTube | Transcript import | No | Yes |
| NotebookLM | Notes import | No | Yes |

## Dependencies

### Current Dependencies

- Python 3.13+ (standard library only)
- Claude Code (platform)

### Dependency Policy

- Prefer stdlib
- No external packages for MVP
- Document any future dependencies
- Review for vulnerabilities before adding

## Security Checklist

Before merging:

- [ ] No secrets in repo
- [ ] No credentials in code
- [ ] File access restricted
- [ ] External inputs sanitized
- [ ] Prompt injection mitigations in place
- [ ] Privacy reviewed for ingestion
- [ ] Local-first maintained
- [ ] No unnecessary external calls
- [ ] Documentation updated

## Incident Response

If security issue discovered:

1. **Document** in decision log
2. **Assess** impact
3. **Mitigate** immediately
4. **Review** by codex-reviewer
5. **Update** SECURITY.md if needed
6. **Communicate** if user-facing

## Reporting Security Issues

SpeakOps is local-first. Security issues are typically:

- File access outside allowed paths
- Unwanted data retention
- Prompt injection vulnerabilities

Report issues via:
- GitHub Issues (for repo-level issues)
- Decision log (for architectural issues)

---

**Version:** 1.0
**Last updated:** 2025-06-28
