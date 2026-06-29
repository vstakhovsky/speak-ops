# GitHub README Auditor

## Purpose

Review README.md as a GitHub landing page to ensure professional presentation and clear communication.

## When to Use

- After README.md changes
- Before release-readiness-gate
- When repository structure changes
- For new project repositories

## Inputs

- README.md file path
- Repository context (purpose, audience)

## Checks Performed

### First Screen Clarity

1. **Project identity**
   - Clear title and tagline
   - Purpose immediately apparent
   - Not confusing or cluttered

2. **Visual hierarchy**
   - Proper heading structure
   - Clear sections
   - Not overwhelming

3. **Key value proposition**
   - What the project does
   - Why it matters
   - Who it's for

### Rendering Issues

4. **Broken Markdown**
   - Headings displaying as text
   - Lists not rendering
   - Code blocks broken
   - Tables malformed

5. **Image sizing**
   - Images too large
   - Images too small
   - Responsive width handling
   - Alt text present

### Navigation and Structure

6. **Badges and status**
   - Badges present and accurate
   - Status indicators clear
   - Not excessive

7. **Navigation links**
   - Table of contents or quick links
   - Internal links working
   - Not broken

8. **Section order**
   - Logical flow
   - Key information first
   - Details later

### Content Quality

9. **Overlong sections**
   - Excessive verbosity
   - Information overload
   - Better suited to separate docs

10. **Professional appearance**
    - Not broken or messy
    - Consistent formatting
    - Dark/light theme safe

### Readability

11. **Mobile-ish readability**
    - Not dependent on wide viewport
    - Responsive images
    - Text doesn't overflow

12. **Dark/light theme safety**
    - Works in both themes
    - No hardcoded colors
    - Contrast maintained

## Hard-Fail Criteria

Auditor returns FAIL if any of:

- First screen is confusing (unclear what project is)
- Markdown is visibly broken (headings as text, merged content)
- Images dominate too much (take up entire viewport)
- Key value proposition is unclear (what/why/who missing)
- README looks unprofessional (broken layout, inconsistent formatting)

## Output Format

```markdown
## GitHub README Audit

Status: PASS / FAIL

## What Works

* Positive aspects of current README
* Clear project title and tagline
* Good use of badges
* Well-structured sections

## Blocking Issues

* Critical issues that prevent professional presentation
* First screen confusing - unclear project purpose
- Section "X" is broken and renders as plain text

## Improvements

* Recommended enhancements (non-blocking)
* Consider adding architecture diagram
* Shorten "Y" section, link to docs instead
```

## Examples

### PASS Example

```markdown
## GitHub README Audit

Status: PASS

## What Works

- Clear title: "SpeakOps - Local-first Business English Voice Activation OS"
- Professional badge display
- Well-organized sections
- Good visual hierarchy
- Images properly sized

## Blocking Issues

None

## Improvements

- Consider adding quick start earlier
- Could benefit from screenshot/examples
```

### FAIL Example

```markdown
## GitHub README Audit

Status: FAIL

## What Works

- Project name is present

## Blocking Issues

- First screen confusing - tagline merged with content
- Markdown visibly broken - headings render as plain text
- Images too large - architecture diagram takes entire viewport
- Key value proposition unclear - what does this project actually do?

## Improvements

- Fix Markdown rendering (see markdown-render-validator)
- Reduce image sizes or use responsive width
- Clarify project purpose in first 3 lines
```

## Limitations

- Subjective assessment of "professional"
- Cannot test actual GitHub rendering perfectly
- Mobile responsiveness estimates only
- Cultural/contextual factors may vary

## Integration

Run after markdown-render-validator and before release-readiness-gate.
Combine with svg-layout-validator if README contains SVG images.
