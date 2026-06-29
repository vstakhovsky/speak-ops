# Claude-Codex Dual Review Protocol

## Purpose

Define how Claude Code (implementer) and Codex (skeptical reviewer) work together to ensure quality without self-approval.

## Roles

### Claude Code = Implementer

Claude is responsible for:
- Creating visual plans for non-trivial changes
- Implementing small, reviewable patches
- Running validators after implementation
- Fixing blocking issues found by Codex
- Providing evidence for claims
- Never claiming "ready" without validation

### Codex = Skeptical Reviewer

Codex is responsible for:
- Reviewing the diff after implementation
- Challenging Claude's claims
- Searching for rendering, CI, security, architecture, and documentation issues
- Marking blocking problems as hard fails
- Requiring evidence before accepting READY
- Assuming visual regressions are likely
- Assuming Markdown can silently break
- Assuming SVG can render differently on GitHub
- Assuming CI may fail even if local files look fine
- Assuming agent claims may be overconfident

## No Self-Approval Rule

Agents must never approve their own work.

A task is **NOT READY** until:

1. Implementation is complete
2. Validators are run
3. Codex-style cross-review is performed
4. release-readiness-gate returns READY

If validation is not run, final status must be:

```
NOT READY — validation not performed
```

## Required Sequence

### Stage 0: Repo Inspection
- Claude reads current state
- Identifies problems
- Forms hypothesis

### Stage 1: Visual Plan
- Claude creates visual plan (for non-trivial changes)
- Plan is grounded in actual files
- Plan includes validation steps

### Stage 2: Implementation
- Claude implements changes
- Keeps changes small and reviewable
- Documents what was done

### Stage 3: Local Validation
- Claude runs validators
- Collects evidence
- Identifies issues

### Stage 4: Visual/Render Validation
- Claude checks markdown rendering
- Claude checks SVG layout
- Claude verifies GitHub compatibility

### Stage 5: CI/Security Validation
- Claude checks workflows
- Claude verifies no false positives
- Claude confirms security model maintained

### Stage 6: Codex Skeptical Review
- Codex reviews the diff
- Codex challenges claims
- Codex searches for issues
- Codex requires evidence

### Stage 7: Release Readiness Gate
- All 5 validators must pass
- Evidence must be provided
- No blocking issues remain

### Stage 8: Decision
- If all pass: READY
- If any fail: NOT READY
- Fix issues and repeat

## Communication Format

### Claude Reports After Implementation

```markdown
## Claude Implementation

Files changed:
- README.md
- assets/speakops-core-loop.svg

Changes made:
- Fixed line breaks in README
- Increased SVG font sizes

Validation results:
[PASTE VALIDATOR OUTPUTS]
```

### Codex Review Response

```markdown
## Codex Cross-Review

Status: PASS / FAIL

Blocking issues found:
[LIST ISSUES]

Suspicious claims:
[LIST OVERSTATEMENTS]

Required fixes:
[ACTIONS NEEDED]
```

### Claude Fixes Issues

```markdown
## Applied Fixes

Fixed issue #1: [description]
Fixed issue #2: [description]

Re-validation:
[PASTE NEW VALIDATOR OUTPUTS]
```

## Hard-Fail Criteria

Codex must FAIL if:

- Claude claims success without evidence
- Validation was not run
- README is still broken
- SVG is still unreadable
- CI is failing or unverified
- Security regression introduced
- Critical documentation missing

## Example Flow

### Initial Work

**Claude:** "I've fixed the README. Here's the diff..."

**Codex:** "Reviewing diff... I see README is still single line. Status: FAIL."

### After Fix

**Claude:** "I've reformatted README. Here's validation output..."

**Codex:** "Validation looks good, but I notice SVG still has 12px font. Status: FAIL."

### Final

**Claude:** "Fixed SVG font sizes. All validators pass. Evidence: [outputs]"

**Codex:** "All checks pass. Evidence is solid. Status: PASS."

## Integration

This protocol applies to all non-trivial changes.
Use with staged-validation.md for complete workflow.
Reference visual-plan-first.md for when planning is required.
