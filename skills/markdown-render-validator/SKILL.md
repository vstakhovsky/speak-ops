# Markdown Render Validator

## Purpose

Validate that Markdown files render correctly on GitHub, preventing broken documentation from reaching users.

## When to Use

- After any README.md changes
- After any documentation file changes
- Before marking any task as complete
- In CI pipeline for all markdown files

## Inputs

- File path(s) to validate (default: README.md)
- Optional: Specific checks to run

## Checks Performed

### Critical Checks (Hard Fail)

1. **Unclosed HTML tags**
   - Detects `<div>`, `<p>`, `<span>` without matching closures
   - Fails if HTML structure is broken

2. **Broken Markdown headings**
   - Headings that render as plain text
   - Missing blank lines before headings
   - Malformed heading levels

3. **Missing blank lines around HTML blocks**
   - HTML blocks without surrounding newlines
   - Content merged with HTML

4. **Broken code fences**
   - Unmatched triple backticks
   - Missing language identifiers
   - Unclosed code blocks

5. **Malformed lists**
   - List items merged into paragraphs
   - Incorrect indentation
   - Mixed list formats

6. **Trailing whitespace**
   - Spaces/tabs at end of lines
   - Causes CI failure
   - Invisible but breaks rendering

### Warning Checks

7. **Broken internal links**
   - Links to non-existent anchors
   - Incorrect reference syntax

8. **Huge merged paragraphs**
   - Missing blank lines between sections
   - Content that renders as one giant block

## Hard-Fail Criteria

Validator returns FAIL if any of:

- Headings render as plain text (e.g., `## Heading` appears as text)
- HTML tags are unclosed (`<div>` without `</div>`)
- Code fences are unbalanced (odd number of ``` markers)
- README sections merge together
- Trailing whitespace present (causes CI failure)
- Content is clearly broken on GitHub renderer

## Output Format

```markdown
## Markdown Render Validation

Status: PASS / FAIL

## Blocking Issues

* file:line - issue description - impact
* README.md:1 - Unclosed <div> tag - breaks entire layout
* README.md:25 - Heading without blank line - renders as text

## Warnings

* file:line - non-blocking issue - optional fix

## Suggested Patch

[diff or fix instructions if applicable]
```

## Examples

### PASS Example

```markdown
## Markdown Render Validation

Status: PASS

## Blocking Issues

None

## Warnings

None
```

### FAIL Example

```markdown
## Markdown Render Validation

Status: FAIL

## Blocking Issues

* README.md:1 - Single-line file (20KB) - entire README is one line
* README.md:23 - Unclosed <div> tag - breaks layout
* README.md:45 - Trailing whitespace - CI failure

## Suggested Patch

Split README.md into proper lines with correct spacing.
```

## Limitations

- Cannot perfectly simulate GitHub rendering
- May miss edge cases in complex Markdown
- Does not check external link validity
- Local validation may differ from GitHub rendering

## Integration

Run this validator after any documentation changes and before release-readiness-gate.
