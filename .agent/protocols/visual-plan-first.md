# Visual Plan First Protocol

## Purpose

Define when visual planning is required and what makes a plan acceptable.

## When Plan Is Required

Visual plan **MUST** be created for:

- ✅ README changes
- ✅ SVG changes
- ✅ Architecture changes
- ✅ Workflow changes
- ✅ Security changes
- ✅ Public presentation changes
- ✅ Any multi-file change (3+ files)

Visual plan **NOT REQUIRED** for:

- ⏭️ Typo-only fix
- ⏭️ Single-line documentation correction
- ⏭️ Mechanical formatting cleanup
- ⏭️ Comment additions
- ⏭️ Trivial variable renames

## Plan Requirements

### 1. Task Goal

Must be specific and actionable:

❌ Bad: "Fix README"
✅ Good: "Fix README.md rendering by converting single-line format to proper 635-line structure"

### 2. Impacted Files

Must list all files:

❌ Bad: "Some files will change"
✅ Good: "Modified: README.md, assets/speakops-architecture.svg"

### 3. File Map

Must show structure:

❌ Bad: "Will create new skills"
✅ Good: "skills/markdown-render-validator/SKILL.md (NEW)"

### 4. Flow Diagram

Must show process:

❌ Bad: "Will implement and test"
✅ Good: "Inspect → Detect → Reformat → Validate → Gate"

### 5. Current vs Target State

Must show before/after:

❌ Bad: "README will be better"
✅ Good: "Current: README is single line. Target: README has 635 lines."

### 6. Risks

Must identify what could go wrong:

❌ Bad: No risks listed
✅ Good: "Risk: May introduce formatting errors during reconstruction"

### 7. Open Questions

Must list unknowns:

❌ Bad: No questions
✅ Good: "Question: Should validators be scripts or documentation?"

### 8. Validation Plan

Must include validation steps:

❌ Bad: No validation mentioned
✅ Good: "Will run markdown-render-validator and svg-layout-validator"

### 9. Expected Diff

Must estimate changes:

❌ Bad: Unknown
✅ Good: "~15 new files, ~3 modified files, ~1000 lines added"

### 10. Rollback Plan

Must explain how to undo:

❌ Bad: No plan
✅ Good: "Git reset if reconstruction fails"

## Hard-Fail Criteria

Plan **FAILS** if:

- ❌ Plan is generic (could apply to any repo)
- ❌ Plan is not grounded in actual files
- ❌ Plan has no validation steps
- ❌ Plan ignores security/privacy
- ❌ Plan does not say what will be changed

## Plan Creation Process

### 1. Use Visual Plan Skill

```
/skills/visual-plan/SKILL.md
```

### 2. Store Plan

Store in one of:

- `.agent/memory/working.md` (for current work)
- `docs/plans/YYYY-MM-DD-task-name.md` (for long-term reference)

### 3. Reference During Implementation

Keep plan open during implementation
Check off items as completed
Update plan if scope changes

### 4. Include in Final Report

Reference plan in final output
Show plan vs actual changes
Document any deviations

## Example Plans

### GOOD Plan (Passes)

```markdown
# Visual Plan: Fix README Rendering

## Task Goal
Fix README.md rendering issues caused by single-line format

## Impacted Files
- Modified: README.md

## File Map
README.md (single 20KB line) → README.md (635 properly formatted lines)

## Flow Diagram
Inspect → Detect single line → Reformat → Validate → Gate

## Current vs Target State
- **Current:** README.md is one giant line, breaks GitHub rendering
- **Target:** README.md has proper line breaks and spacing

## Risks
- May introduce formatting errors during reconstruction
- Time-consuming to reconstruct

## Open Questions
- None

## Validation Plan
- Run markdown-render-validator
- Check for trailing whitespace
- Verify heading structure

## Expected Diff
- +635 lines (reconstruction)
- -1 line (original broken format)

## Rollback Plan
Git reset if reconstruction fails
```

### BAD Plan (Fails)

```markdown
# Visual Plan: Fix README

## Task Goal
Fix README

## Impacted Files
- Some files maybe

## File Map
Missing

## Flow Diagram
Missing

## Current vs Target State
Missing

## Risks
None mentioned

## Open Questions
None

## Validation Plan
None - will just do it

## Expected Diff
Unknown

## Rollback Plan
Missing
```

**Result: FAIL** - Not specific, no validation, no evidence of planning

## Integration

Use this protocol to decide if visual-plan skill should be invoked.
Works with claude-codex-dual-review.md and staged-validation.md.
