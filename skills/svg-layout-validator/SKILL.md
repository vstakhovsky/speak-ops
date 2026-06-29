# SVG Layout Validator

## Purpose

Ensure SVG diagrams render correctly on GitHub with readable text and proper spacing.

## When to Use

- After any SVG file changes
- Before committing architecture diagrams
- In release-readiness-gate for visual assets

## Inputs

- SVG file path(s) to validate
- Optional: Rendering width (default: 100%, check at common widths)

## Checks Performed

### Critical Checks (Hard Fail)

1. **Overlapping text**
   - Text elements that intersect
   - Labels covering other labels
   - Text overlapping shapes

2. **Labels outside canvas**
   - Text beyond viewBox boundaries
   - Clipped content
   - Elements outside visible area

3. **Font smaller than 14px**
   - Text below minimum readability threshold
   - Labels too small to read
   - Subtitle text < 14px

4. **Cards too small**
   - Containers that can't fit content
   - Cramped layout
   - Insufficient padding

5. **Arrows crossing through labels**
   - Connector lines intersecting text
   - Misleading visual flow
   - Confusing diagram structure

6. **Unreadable contrast**
   - Text color too similar to background
   - Dark text on dark background
   - Low contrast ratios

7. **Broken GitHub SVG rendering risk**
   - Use of foreignObject (not supported)
   - External font dependencies
   - Complex CSS that may not render

### Warning Checks

8. **Too much text in diagram**
   - Excessive labels
   - Information overload
   - Better suited for markdown

## Hard-Fail Criteria

Validator returns FAIL if any of:

- Any text overlaps (text-on-text or text-on-shape)
- Any font < 14px (hard minimum)
- Labels are clipped or outside canvas
- SVG uses foreignObject (GitHub doesn't support)
- Diagram is unreadable at README width (100% or typical viewport)
- Arrows cross through text elements

## Output Format

```markdown
## SVG Layout Validation

Status: PASS / FAIL

## Blocking Issues

* file - issue description
* assets/speakops-architecture.svg - Text overlap at (x,y)
* assets/speakops-core-loop.svg - Font size 12px at line 45

## Visual Warnings

* file - non-critical visual issues
* assets/speakops-architecture.svg - Many labels, consider simplifying

## Required Fixes

[Specific fixes needed to pass]
```

## Examples

### PASS Example

```markdown
## SVG Layout Validation

Status: PASS

## Blocking Issues

None

## Visual Warnings

None
```

### FAIL Example

```markdown
## SVG Layout Validation

Status: FAIL

## Blocking Issues

* assets/speakops-architecture.svg - Font size 13px at line 29 (below 14px minimum)
* assets/speakops-core-loop.svg - Text "Feedback" overlaps with arrow

## Required Fixes

1. Increase all font sizes to minimum 14px
2. Adjust spacing to prevent text-arrow overlap
3. Verify rendering at 100% width
```

## Limitations

- Cannot detect all visual issues programmatically
- Manual visual review still recommended
- GitHub rendering may differ from local preview
- Complex diagrams may need manual inspection

## Integration

Run this validator after SVG changes and before release-readiness-gate.
Combine with github-readme-auditor for complete visual validation.
