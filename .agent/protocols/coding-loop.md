# Coding Loop Protocol

## Purpose

Define the standard workflow for implementing features in SpeakOps.

## Process

### 1. Read and Understand

Before writing code:

1. **Read the repository** — Understand structure
2. **Identify the change** — What needs to be done
3. **Check existing code** — Don't duplicate
4. **Understand context** — How this fits the system

### 2. Spec the Change

Before implementing:

1. **Write spec** — Use spec-planner agent
2. **Review with lazy-senior-dev** — Cut scope if needed
3. **Review with repo-architect** — Check structure
4. **Review with privacy-security-reviewer** — Check risks

### 3. Implement

When writing code:

1. **Minimal change** — Smallest diff that works
2. **No overengineering** — Simple over clever
3. **Mark shortcuts** — Use `# ponytail:` comments
4. **Test as you go** — Verify each part works

### 4. Quality Gates

Before marking done:

1. **Tests** — Unit tests for non-trivial code
2. **Evals** — For AI behavior changes
3. **Security** — Privacy/security review
4. **Docs** — Update documentation

### 5. Review

Before merging:

1. **Self-review** — Check your own work
2. **Codex review** — Independent review
3. **Decision log** — Document changes

## Quality Checklist

Before marking a task complete:

- [ ] Code works
- [ ] Tests pass (if tests added)
- [ ] Evals pass (if evals added)
- [ ] Security review passed (if applicable)
- [ ] Docs updated (if applicable)
- [ ] Decision log updated (if applicable)
- [ ] No shortcuts left unmarked (or documented)

## Ponytail Rules

**The ladder:**
1. Does this need to exist?
2. Stdlib does it?
3. Native platform feature?
4. Already-installed dependency?
5. Can it be one line?
6. Only then: minimal code

**Mark shortcuts:**
```python
# ponytail: O(n²) scan, upgrade to hash map if >1000 items
# ponytail: Global lock, per-account locks if throughput matters
# ponytail: Simplified error handling, proper errors in production
```

## Examples

### Example 1: New Feature

**Task:** Add phrase ingestion from Google Docs

**Process:**
1. Read repo structure
2. Write spec (ingestion, security, privacy)
3. Review with agents (cut API scope for MVP)
4. Implement (manual paste, not API)
5. Add security review (input sanitization)
6. Add tests (injection prevention)
7. Codex review (privacy check)
8. Update docs (workflow documented)
9. Decision log (MVP scope decision)

### Example 2: Bug Fix

**Task:** Fix scoring not updating

**Process:**
1. Read scoring code
2. Identify bug (score not saved)
3. Implement fix (add save call)
4. Test (verify score updates)
5. Add test (regression test)
6. Update decision log (bug fix documented)

### Example 3: Refactor

**Task:** Simplify phrase extraction

**Process:**
1. Read extraction code
2. Identify complexity
3. Review with lazy-senior-dev (can we simplify?)
4. Implement simplification
5. Add tests (verify same output)
6. Update docs (if API changed)

## Anti-Patterns

**Don't do this:**
- Write code before understanding
- Implement without spec
- Overengineer "for later"
- Skip quality gates
- Ignore security/privacy
- Forget to document

**Do this instead:**
- Read first, code second
- Spec before implement
- Build for now, not later
- Always run quality gates
- Always review security/privacy
- Always document decisions

## Output Format

For coding tasks, return:

```markdown
## Implementation

**Changes:** [what changed]
**Files:** [files modified]
**Lines changed:** [approximate]

## Testing

**Tests added:** [yes/no]
**Tests pass:** [yes/no]

## Quality Gates

**Evals:** [pass/fail/NA]
**Security:** [pass/fail/NA]
**Docs updated:** [yes/no]

## Summary

[What was done and why]
```

---

**Protocol Version:** 1.0
**Status:** Active
