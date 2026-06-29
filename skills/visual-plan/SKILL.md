# Visual Plan

## Purpose

Create a visual plan grounded in the real repository before implementation, ensuring changes are well-thought-out and validated.

## When to Use

**Required for:**
- README changes
- SVG changes
- Architecture changes
- Workflow changes
- Security changes
- Public presentation changes
- Any multi-file change

**Not required for:**
- Typo-only fix
- Single-line documentation correction
- Mechanical formatting cleanup

## Inputs

- Task description or user request
- Current repository state
- Relevant files to be changed

## Plan Components

### 1. Task Goal

Clear statement of what will be accomplished:

```
Task goal: Fix README rendering and add validation gates
```

### 2. Impacted Files

List all files that will be:

- Created (new files)
- Modified (changed files)
- Deleted (removed files)

### 3. File Map

Visual representation of file structure:

```
skills/
├── markdown-render-validator/SKILL.md (NEW)
├── svg-layout-validator/SKILL.md (NEW)
...
```

### 4. Flow Diagram

Text-based flow showing process:

```
Inspect → Validate → Create → Test → Gate
```

### 5. Current vs Target State

- **Current:** What exists now
- **Target:** What will exist after changes

### 6. Risks

What could go wrong:

- Validation may not catch all issues
- Time constraints
- Complex interactions
- Edge cases

### 7. Open Questions

What we don't know:

- Should validators be scripts or docs?
- How to integrate with existing workflows?
- Performance impact?

### 8. Validation Plan

How we'll verify the changes:

- Run markdown-render-validator
- Run svg-layout-validator
- Test on GitHub renderer
- Manual visual review

### 9. Expected Diff

Rough estimate of changes:

- ~15 new files
- ~3 modified files
- ~1000 lines added

### 10. Rollback Plan

How to undo if things go wrong:

- Git reset to previous commit
- Revert specific files
- Fallback to known-good state

## Hard-Fail Criteria

Visual plan FAILS if:

- Plan is generic (not specific to this repository)
- Plan is not grounded in actual files
- Plan has no validation steps
- Plan ignores security/privacy
- Plan does not say what will be changed

## Output Format

```markdown
# Visual Plan: [Task Name]

## Task Goal
[Clear goal statement]

## Impacted Files
- Created: [list]
- Modified: [list]
- Deleted: [list]

## File Map
[ASCII or text-based structure]

## Flow Diagram
[Text-based process flow]

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
- [rough estimate]

## Rollback Plan
[How to undo changes]
```

## Examples

### PASS Example

```markdown
# Visual Plan: Fix README Rendering

## Task Goal
Fix README.md rendering issues caused by single-line format

## Impacted Files
- Modified: README.md

## File Map
README.md (single 20KB line) → README.md (635 properly formatted lines)

## Flow Diagram
Inspect → Detect single line → Reformat → Validate → Commit

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

### FAIL Example

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

**Result: FAIL** - Plan is generic, lacks specifics, no validation steps

## Limitations

- Text-based diagrams may be unclear
- Diff estimates are rough
- Risk assessment may be incomplete
- May not anticipate all issues

## Integration

Create visual plan before any non-trivial implementation.
Store plan in `.agent/memory/working.md` or `docs/plans/YYYY-MM-DD-task-name.md`
Reference plan during implementation and validation.
