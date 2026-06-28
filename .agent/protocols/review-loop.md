# Review Loop Protocol

## Purpose

Define the standard workflow for reviewing changes in SpeakOps.

## Process

### 1. Self-Review

Before requesting review:

1. **Check changes** — What was modified
2. **Verify functionality** — Does it work
3. **Check quality gates** — Tests/evals pass
4. **Review docs** — Documentation updated
5. **Check shortcuts** — Ponytail comments present

### 2. Codex Review

Request independent review:

1. **Provide context** — What and why
2. **Share changes** — Diff or summary
3. **Specify concerns** — Areas to focus on
4. **Get feedback** — Independent assessment

### 3. Security Review

For security-sensitive changes:

1. **Privacy review** — Data handling
2. **Security review** — Vulnerabilities
3. **Input validation** — Sanitization
4. **File access** — Path restrictions

### 4. Decision Log

After review:

1. **Document decision** — Approve/reject/revise
2. **Record rationale** — Why this decision
3. **Note concerns** — Any issues raised
4. **Plan follow-up** — Next steps

## Review Types

### Code Review

**Focus:**
- Correctness — Does it work
- Quality — Is it well-written
- Simplicity — Is it minimal
- Safety — Are there risks

**Checklist:**
- [ ] Code works as intended
- [ ] No unnecessary complexity
- [ ] No overengineering
- [ ] Ponytail rules followed
- [ ] Tests/evals added if needed

### Architecture Review

**Focus:**
- Structure — Is organization clear
- Boundaries — Are responsibilities clear
- Duplication — Is code duplicated
- Dependencies — Are dependencies appropriate

**Checklist:**
- [ ] Module boundaries clear
- [ ] No circular dependencies
- [ ] No duplication
- [ ] Minimal dependencies
- [ ] Local-first maintained

### Prompt Review

**Focus:**
- Clarity — Are instructions clear
- Quality — Do prompts produce good results
- Safety — Are inputs sanitized
- Naturalness — Do prompts sound natural

**Checklist:**
- [ ] Instructions clear
- [ ] Prompts tested
- [ ] Inputs sanitized
- [ ] Natural spoken language
- [ ] Not AI-like

### Security Review

**Focus:**
- Secrets — No credentials in repo
- Privacy — Data handled appropriately
- Inputs — All inputs sanitized
- Access — File access restricted

**Checklist:**
- [ ] No secrets in repo
- [ ] Privacy maintained
- [ ] Inputs sanitized
- [ ] File access restricted
- [ ] No unsafe operations

## Review Format

### Self-Review Format

```markdown
## Self-Review

**Changes:** [what changed]
**Files:** [files modified]

**Quality Gates:**
- Tests: [pass/fail/NA]
- Evals: [pass/fail/NA]
- Security: [pass/fail/NA]
- Docs: [updated/NA]

**Self-Assessment:**
- Works: [yes/no]
- Simple: [yes/no]
- Safe: [yes/no]

**Concerns:**
[Any concerns or areas needing review]
```

### Codex Review Format

```markdown
## Codex Review

**Input:** [changes provided]
**Focus:** [specific concerns]

**Findings:**

### Critical Issues (block before merge)
- [Issue]

### Quick Wins (should fix)
- [Issue]

### Can Wait (nice to have)
- [Issue]

### Risk Assessment
- Overall risk: [Low/Medium/High]
- Recommendation: [approve/needs revision/block]

**Rationale:**
[Why this recommendation]
```

### Security Review Format

```markdown
## Security Review

**Change:** [description]

**Findings:**

### Critical (block)
- [Issue]

### Recommendations (should fix)
- [Issue]

### Observations (good to note)
- [Issue]

### Approval
[Approved/Needs revision/Blocked]

**Rationale:**
[Why this decision]
```

## Review Triggers

**When to request review:**

- Code changes >20 lines
- Architecture changes
- New features
- Security-sensitive changes
- Prompt changes
- Eval changes

**When to skip review:**

- Typos or trivial fixes
- Comment-only changes
- Documentation clarifications
- Test additions (not modifications)

## Review Process

### For Reviewer

1. **Understand context** — Read the spec/issue
2. **Review changes** — Check diff/summary
3. **Check quality gates** — Tests/evals/security
4. **Provide feedback** — Specific, actionable
5. **Make recommendation** — Approve/revise/block

### For Author

1. **Address feedback** — Fix or respond to issues
2. **Re-run gates** — Ensure nothing broke
3. **Request re-review** — If significant changes
4. **Update decision log** — Document final decision

## Decision Log

After review decision:

```markdown
## Decision Log Entry

**Date:** [date]
**Change:** [what changed]
**Decision:** [approve/reject/revise]

**Rationale:**
[Why this decision]

**Concerns Raised:**
- [Concern 1]
- [Concern 2]

**Follow-up:**
- [Action 1]
- [Action 2]

**Decision Maker:** [who]
**Review Type:** [self/codex/security]
```

## Examples

### Example 1: Code Review

**Change:** Add phrase ingestion from Obsidian

**Self-Review:**
- Changes: New script, security checks
- Files: ingest_obsidian.py
- Tests: Added sanitization tests
- Security: Path restrictions, sanitization
- Docs: Workflow documented

**Codex Review:**
- Critical: None
- Quick Wins: Add error handling for missing files
- Can Wait: Consider adding progress indicator
- Risk: Low
- Recommendation: Approve with quick wins

### Example 2: Security Review

**Change:** Add Google Docs ingestion

**Security Review:**
- Critical: No Google API credentials in repo ✓
- Recommendations: Add prompt injection tests
- Observations: Manual paste is safe approach
- Approval: Approved

## Review Quality

**Good review:**
- Specific feedback
- Actionable suggestions
- Clear rationale
- Balanced (not nitpicky)

**Poor review:**
- Vague feedback
- No suggestions
- Unclear rationale
- Too nitpicky

## Anti-Patterns

**Don't do this:**
- Merge without review (for significant changes)
- Ignore review feedback
- Skip security review for sensitive changes
- Forget decision log
- Make feedback personal

**Do this instead:**
- Review all significant changes
- Address all feedback
- Always security-review sensitive changes
- Always document decisions
- Keep feedback professional

---

**Protocol Version:** 1.0
**Status:** Active
