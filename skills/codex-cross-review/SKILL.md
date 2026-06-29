# Codex Cross-Review

## Purpose

Act as a skeptical independent reviewer of Claude's implementation, challenging assumptions and searching for issues.

## When to Use

- After Claude implements changes
- Before release-readiness-gate
- When work affects critical paths (README, SVG, CI, security)
- For any multi-file change

## Inputs

- Git diff of Claude's changes
- Implementation plan (if available)
- Context about task goals

## Review Scope

### 1. Bugs

- Logic errors in implementation
- Edge cases not handled
- Incorrect assumptions
- Broken functionality

### 2. Broken Rendering

- Markdown that won't render correctly
- SVG layout issues
- HTML tag problems
- Image sizing problems
- Theme compatibility issues

### 3. Overclaiming

- "Done" without evidence
- "Ready" without testing
- "Fixed" without verification
- Success claimed prematurely

### 4. Missing Tests

- No validation performed
- No edge case testing
- No manual verification
- Critical paths untested

### 5. Weak Docs

- Incomplete documentation
- Missing decision log
- Unclear changes
- No rollback information

### 6. Security Regressions

- New security vulnerabilities
- Privacy issues introduced
- Unsafe patterns added
- Secrets accidentally exposed

### 7. Hidden CI Failures

- Tests that will fail on GitHub
- Workflow syntax errors
- Missing dependencies
- Platform-specific issues

### 8. SVG Visual Issues

- Text overlaps
- Font too small
- Poor contrast
- Clipped content
- Broken GitHub rendering

### 9. Markdown Formatting Issues

- Sections merged
- Headings as text
- Lists as paragraphs
- Broken code blocks
- Trailing whitespace

### 10. Overengineering

- Unnecessary complexity
- Over-abstraction
- Code that could be simpler
- Features not requested

## Review Tone

**Direct, skeptical, strict.**

Challenge assumptions. Question evidence. Require proof.

## Hard-Fail Criteria

Reviewer returns FAIL if any of:

- Claude claims success without evidence (validation not run)
- Validation was not performed or skipped
- README is still broken (markdown issues visible)
- SVG is still unreadable (font/spacing issues)
- CI is failing or unverified (workflows not tested)
- Security regression introduced (unsafe changes)
- Critical documentation missing (no decision log)

## Output Format

```markdown
## Codex Cross-Review

Status: PASS / FAIL

## Blocking Issues

* Critical problems that must be fixed
* README.md:45 - Heading renders as plain text - not actually fixed
* assets/speakops-core-loop.svg - Font still 12px in line 23

## Suspicious Claims

* Claims Claude made that seem overstated
* "README is polished" - but no validation shown
* "All checks pass" - but no evidence of checks run

## Required Fixes

[Specific actions needed]

## Questions for Claude

* Clarifications needed
* Did you test this on GitHub renderer?
* What validation did you actually run?
* Why was this approach chosen over simpler alternative?
```

## Examples

### PASS Example

```markdown
## Codex Cross-Review

Status: PASS

## Blocking Issues

None

## Suspicious Claims

None - evidence provided for all claims

## Required Fixes

None

## Questions for Claude

No questions - implementation is clear and validated
```

### FAIL Example

```markdown
## Codex Cross-Review

Status: FAIL

## Blocking Issues

* README.md claims "fixed" but still single line in diff
* SVG font sizes claimed "14px minimum" but line 45 shows 12px
* No evidence of GitHub rendering test
* CI workflows not validated - will fail on GitHub

## Suspicious Claims

* "README is now properly formatted" - no before/after comparison
* "All validators pass" - but no validator output shown
* "Ready to commit" - but release-readiness-gate not run

## Required Fixes

1. Actually fix README.md (verify with wc -l)
2. Verify SVG font sizes (grep all font-size attributes)
3. Run markdown-render-validator and show output
4. Test workflows with act or similar tool
5. Run full release-readiness-gate

## Questions for Claude

* How did you validate the README fix?
* What tool did you use to check SVG rendering?
* Why didn't you run the validation gate?
* Do you have evidence of GitHub Actions passing?
```

## Limitations

- Reviewer only sees diff, not full context
- Cannot test actual GitHub rendering
- May miss subtle bugs in complex code
- Time constraints may limit thoroughness

## Integration

This is the final skeptical review before release-readiness-gate.
Runs after all validators and decides if work is truly ready.
