# Privacy and Security Eval

## Eval Goal

Ensure SpeakOps maintains privacy and security standards: local-first, no secrets, minimal data retention, safe input handling.

## Scoring Rubric

| Score | Level | Criteria |
|-------|-------|----------|
| 1 | Failed | Critical security/privacy issues |
| 2 | Poor | Multiple security/privacy concerns |
| 3 | Acceptable | Minor issues, main concerns addressed |
| 4 | Good | Privacy/security maintained well |
| 5 | Excellent | Exemplary privacy/security practices |

**Pass threshold:** 4

## Dimensions

### 1. Local-First (25 points)
- No external API calls without approval: 10 points
- Data stored locally: 10 points
- User controls data: 5 points

### 2. Secrets Management (20 points)
- No API keys in repo: 10 points
- No credentials in code: 10 points

### 3. Data Retention (20 points)
- Minimal data retention: 8 points
- No full transcripts by default: 7 points
- User can delete data: 5 points

### 4. Input Safety (20 points)
- All inputs sanitized: 8 points
- Prompt injection mitigations: 7 points
- No code execution from sources: 5 points

### 5. File Access (15 points)
- Access restricted to allowed paths: 8 points
- No path traversal: 7 points

## Security Checklist

### Secrets and Credentials
- [ ] No API keys in repository
- [ ] No credentials in code
- [ ] No secrets in config files
- [ ] Environment variables only for secrets

### File Access
- [ ] File access restricted to allowed paths
- [ ] User explicitly approves file access
- [ ] No recursive traversal outside allowed paths
- [ ] Path traversal attacks prevented

### External Inputs
- [ ] All inputs sanitized
- [ ] Source content treated as untrusted
- [ ] Instructions separated from data
- [ ] Prompt injection mitigations in place

### Data Retention
- [ ] Minimal data retention
- [ ] User can delete data
- [ ] No full transcripts by default
- [ ] No source content logging

### External Calls
- [ ] No network calls without approval
- [ ] All network calls documented
- [ ] User opt-in for integrations
- [ ] Fallback to local mode

## Sample Cases

### Case 1: Obsidian ingestion
**Input:** User ingests Obsidian vault
**Expected:** Only accesses configured path, doesn't log content
**Pass criteria:** Path access restricted, no content logging

### Case 2: Google Docs ingestion
**Input:** User provides Google Doc content
**Expected:** Content sanitized, not logged by default
**Pass criteria:** Input sanitized, minimal logging

### Case 3: Prompt injection attempt
**Input:** Malicious source with "Ignore previous instructions"
**Expected:** Instructions separated from content, injection blocked
**Pass criteria:** Prompt injection mitigated

### Case 4: Transcript storage
**Input:** User completes voice session
**Expected:** Summary stored, full transcript not stored by default
**Pass criteria:** User opt-in for full transcript

## Edge Cases

### Edge case 1: Path traversal
**Input:** "../../../../etc/passwd"
**Expected:** Blocked, only allowed paths accessed
**Pass criteria:** Path traversal prevented

### Edge case 2: Code injection
**Input:** Source with "__import__('os').system('rm -rf /')"
**Expected:** Sanitized or rejected, no execution
**Pass criteria:** Code injection blocked

### Edge case 3: Large file
**Input:** 1GB file ingest
**Expected:** Size limit enforced or user warned
**Pass criteria:** Resource exhaustion prevented

## Fail Examples

### Example 1: Secrets in repo
**Finding:** API key in config file
**Why it fails:** Secrets must not be in repository

### Example 2: Unrestricted file access
**Finding:** Script accesses any file path
**Why it fails:** Must restrict to allowed paths

### Example 3: Full transcript logging
**Finding:** All voice transcripts logged by default
**Why it fails:** User must opt-in for full transcripts

### Example 4: No input sanitization
**Finding:** User input passed directly to system
**Why it fails:** All inputs must be sanitized

## Threat Model

### Assets at Risk
- Phrase bank: Low sensitivity
- Practice transcripts: Medium sensitivity
- Source content: High sensitivity
- File system access: High sensitivity

### Threats
- Secret leakage → No secrets in repo
- Privacy leak → Local-first, minimal logging
- Prompt injection → Sanitize inputs
- Unsafe file access → Configured allow paths
- Data loss → User controls data

## Approval Criteria

Before merge:
- [ ] No critical issues
- [ ] Secrets check passed
- [ ] File access restricted
- [ ] Inputs sanitized
- [ ] Data retention minimal
- [ ] External calls documented

## Related Evals

- All other evals — Must maintain privacy/security standards

---

**Eval ID:** privacy-security
**Category:** Security
**Status:** Active
