# Fix SVG Layout Command

## Purpose

Fix SVG diagram layout issues for GitHub rendering.

## When to Use

- SVG has overlapping text
- Labels are too small (< 14px)
- Cards are cramped
- Arrows cross through labels
- Poor contrast
- Diagram unreadable at README width

## Inputs

- SVG file path(s)
- Description of visual issue

## What It Does

Diagnoses and fixes SVG layout problems:

1. **Detects issues**
   - Text overlaps (text-on-text, text-on-shape)
   - Font sizes below 14px
   - Labels clipped or outside canvas
   - Arrows crossing through text
   - Poor contrast ratios
   - Use of foreignObject (GitHub incompatible)

2. **Applies fixes**
   - Increases font sizes to minimum 14px
   - Adjusts spacing to prevent overlaps
   - Repositions labels within canvas
   - Reroutes arrows around text
   - Improves contrast
   - Replaces foreignObject with standard SVG

3. **Validates fixes**
   - Runs svg-layout-validator
   - Checks all font sizes
   - Verifies no overlaps
   - Tests at various widths

## Rules

1. No foreignObject (GitHub doesn't support it)
2. Fixed viewBox (no dynamic sizing)
3. Safe fonts only: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace
4. Minimum font size: 14px
5. Title font: 28-36px
6. Enough spacing between cards
7. No text overlaps
8. No arrows through labels
9. Short labels only
10. Fewer elements over visual noise
11. Must look good in GitHub dark mode
12. Must remain readable at width="100%"

## Validators to Run

- svg-layout-validator (must PASS)
- Visual inspection at 100% width
- Dark mode check

## Output Format

```markdown
## SVG Layout Fix

### Issues Found
- Font size 12px at line 29 (below 14px minimum)
- Text "Feedback" overlaps with arrow
- Label clipped at right edge

### Fixes Applied
- Increased all fonts to minimum 14px
- Adjusted spacing to prevent overlap
- Repositioned labels within canvas

### Validation Results
[PASTE svg-layout-validator OUTPUT]

### Status
PASS / FAIL
```

## Hard-Fail Criteria

Command FAILS if:

- SVG still has overlapping text
- Any font < 14px
- Labels still clipped
- foreignObject still used
- Diagram unreadable at 100% width
- svg-layout-validator returns FAIL

## Integration

Use this command when SVG layout breaks.
Run before release-readiness-gate.
Works with fix-readme-rendering for complete visual fixes.
