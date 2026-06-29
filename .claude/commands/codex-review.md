# Codex Review Command

## Purpose

Run skeptical independent review of implementation after Claude makes changes.

## When to Use

- After Claude implements changes
- Before release-readiness-gate
- When work affects critical paths
- For any multi-file change

## Inputs

- Git diff of Claude's changes
- Implementation plan (if available)
- Context about task goals

## What It Does

Acts as skeptical reviewer, checking for:

1. **Bugs** - Logic errors, edge cases, incorrect assumptions
2. **Broken rendering** - Markdown, SVG, HTML issues
3. **Overclaiming** - "Done" without evidence, success claimed prematurely
4. **Missing tests** - No validation performed, critical paths untested
5. **Weak docs** - Incomplete documentation, missing decision log
6. **Security regressions** - New vulnerabilities, privacy issues
7. **Hidden CI failures** - Workflow syntax, missing dependencies
8. **SVG visual issues** - Text overlaps, font too small, poor contrast
9. **Markdown formatting** - Sections merged, headings as text, broken code blocks
10. **Overengineering** - Unnecessary complexity, over-abstraction

## Review Tone

Direct, skeptical, strict. Challenge assumptions. Question evidence. Require proof.

## Validators to Run

- Codex cross-review skill
- All validator outputs must be checked
- Evidence must be reviewed

## Output Format

```markdown
## Codex Cross-Review

Status: PASS / FAIL

## Blocking Issues

* [Critical problems]
* file:line - issue - impact

## Suspicious Claims

* [Claims without evidence]
* "README is fixed" - no validation shown

## Required Fixes

[Specific actions needed]

## Questions for Claude

[Clarifications needed]
```

## Hard-Fail Criteria

Review FAILS if:

- Claude claims success without evidence
- Validation not performed or skipped
- README still broken (markdown issues)
- SVG still unreadable (font/spacing)
- CI failing or unverified
- Security regression introduced

## Integration

This is the skeptical review before final gate.
Run after implementation and validators.
Use with claude-codex-dual-review protocol.
