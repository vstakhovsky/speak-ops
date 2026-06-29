# Fix README Rendering Command

## Purpose

Fix README.md rendering issues on GitHub.

## When to Use

- README.md renders incorrectly
- Headings display as plain text
- Sections merge together
- Lists appear as paragraphs
- HTML tags are broken
- Trailing whitespace causes CI failure

## Inputs

- README.md file path
- Description of rendering issue

## What It Does

Diagnoses and fixes README rendering problems:

1. **Detects issues**
   - Single-line file (entire README on one line)
   - Missing blank lines between sections
   - Unclosed HTML tags
   - Broken code fences
   - Trailing whitespace

2. **Applies fixes**
   - Splits single-line format into proper lines
   - Adds blank lines around HTML blocks
   - Closes unclosed HTML tags
   - Fixes code fence pairing
   - Removes trailing whitespace

3. **Validates fixes**
   - Runs markdown-render-validator
   - Checks heading structure
   - Verifies HTML balance
   - Confirms no trailing whitespace

## Rules

1. Use plain Markdown for normal content
2. Use HTML only for centered images (isolated blocks)
3. Close all HTML tags
4. Add blank lines before/after headings, HTML, lists, images
5. Avoid huge text blocks
6. Keep sections short and readable
7. Don't wrap Markdown sections in `<p>` or `<div>`
8. Remove trailing whitespace

## Validators to Run

- markdown-render-validator (must PASS)
- github-readme-auditor (must PASS)
- Local rendering check

## Output Format

```markdown
## README Rendering Fix

### Issues Found
- Single-line file (20KB on one line)
- Missing blank lines before headings
- Unclosed <div> tags

### Fixes Applied
- Split into 635 properly formatted lines
- Added blank lines around HTML blocks
- Closed all HTML tags

### Validation Results
[PASTE markdown-render-validator OUTPUT]

### Status
PASS / FAIL
```

## Hard-Fail Criteria

Command FAILS if:

- README still renders incorrectly
- markdown-render-validator returns FAIL
- Trailing whitespace remains
- HTML tags still unclosed
- Headings still display as text

## Integration

Use this command when README rendering breaks.
Run before release-readiness-gate.
Works with fix-svg-layout for complete visual fixes.
