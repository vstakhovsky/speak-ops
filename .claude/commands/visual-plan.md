# Visual Plan Command

## Purpose

Create a visual plan before implementing non-trivial changes.

## When to Use

Required for:
- README changes
- SVG changes
- Architecture changes
- Workflow changes
- Security changes
- Public presentation changes
- Any multi-file change

Not required for:
- Typo-only fix
- Single-line documentation correction
- Mechanical formatting cleanup

## Inputs

- Task description
- Current repository state
- Files to be changed

## What It Does

Creates a visual plan grounded in the real repository including:

1. Task goal (specific and actionable)
2. Impacted files (created/modified/deleted)
3. File map (structure visualization)
4. Flow diagram (process flow)
5. Current vs target state
6. Risks (what could go wrong)
7. Open questions (unknowns)
8. Validation plan (how to verify)
9. Expected diff (rough estimate)
10. Rollback plan (how to undo)

## Validators to Run

- visual-plan skill (self-validation)
- Plan must not be generic
- Plan must be grounded in actual files

## Output Format

```markdown
# Visual Plan: [Task Name]

## Task Goal
[Specific goal]

## Impacted Files
- Created: [list]
- Modified: [list]
- Deleted: [list]

## File Map
[Structure diagram]

## Flow Diagram
[Process flow]

## Current vs Target State
- **Current:** [what exists now]
- **Target:** [what will exist after]

## Risks
- [risk 1]
- [risk 2]

## Open Questions
- [question 1]
- [question 2]

## Validation Plan
- [step 1]
- [step 2]

## Expected Diff
- [estimate]

## Rollback Plan
[how to undo]
```

## Hard-Fail Criteria

Command FAILS if plan is:

- Generic (not specific to this repository)
- Not grounded in actual files
- Missing validation steps
- Ignoring security/privacy
- Not saying what will change

## Integration

Run this command before implementation for non-trivial changes.
Store plan in `.agent/memory/working.md` or `docs/plans/YYYY-MM-DD-task-name.md`.
Reference plan during implementation.
