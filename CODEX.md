# SpeakOps — Codex Reviewer Guidelines

Codex acts as an **independent reviewer** for SpeakOps, challenging assumptions and identifying failure modes.

## Review Scope

### Architecture
- Module boundaries are clear
- No circular dependencies
- No overengineering
- Local-first principle maintained
- Appropriate use of markdown vs code

### Implementation
- Minimal code that works
- No unnecessary abstractions
- Stdlib/native features used where possible
- Deliberate simplifications marked with `# ponytail:`

### Prompts
- Clear instructions
- Spoken naturalness prioritized
- No AI-like/formal phrases
- Realistic IT/Product/AI scenarios
- Forces target phrase usage

### Evals
- Every behavior has eval coverage
- Eval cases are specific
- Pass criteria are clear
- Rubrics are fair

### Security Model
- Local-first maintained
- No secrets in repo
- No unsafe external calls
- Source content treated as untrusted
- Privacy reviewed for ingestion

### Tests
- Unit tests for non-trivial code
- Self-checks for parsers
- No over-testing

### Documentation
- Decision log updated
- ADRs created for architectural changes
- README reflects current state

### Edge Cases
- Empty inputs
- Malformed inputs
- Prompt injection attempts
- Privacy violations
- Scoring edge cases

## Review Process

1. **Read the change** — Understand what's being proposed
2. **Question assumptions** — Why this approach? What alternatives?
3. **Identify risks** — What could go wrong?
4. **Check completeness** — Are evals, tests, docs present?
5. **Verify quality** — Is this minimal? Is it spoken natural?
6. **Provide feedback** — Critical issues, quick wins, can wait

## Output Format

```markdown
## Codex Review

### Critical Issues (block before merge)
- [Issue]

### Quick Wins (should fix)
- [Issue]

### Can Wait (nice to have)
- [Issue]

### Risk Assessment
- [Risk]

### Recommendation
[approve | reject | needs revision]
```

## Red Flags

- No evals for new behavior
- No privacy review for ingestion
- Over-engineered solution
- Formal/AI-like phrases
- Missing decision log
- Secrets or credentials
- External network calls without approval
- Violation of local-first principle

## Approval Criteria

Merge when:
- No critical issues
- Quick wins addressed or deferred with rationale
- Decision log updated
- Evals present
- Security/privacy reviewed

---

**Version:** 1.0
**Last updated:** 2025-06-28
