# Staged Validation Protocol

## Purpose

Define stages that all changes must pass through, with clear gates and decision points.

## Stages

### Stage 0 — Repo Inspection

**Goal:** Understand current state and problems

**Actions:**
- Read relevant files
- Check git status
- Identify what's broken
- Form root cause hypothesis

**Gate:** Must have problem identified before proceeding

**Exit Criteria:**
- Clear problem statement
- List of affected files
- Hypothesis confirmed

### Stage 1 — Visual Plan

**Goal:** Plan before implementation (for non-trivial changes)

**Actions:**
- Create visual plan (skills/visual-plan/SKILL.md)
- Define impacted files
- Map current → target state
- Identify validation steps
- Plan rollback

**Gate:** Plan must be specific and grounded

**Exit Criteria:**
- Plan saved to memory or docs/plans/
- Plan includes validation steps
- Plan addresses security/privacy

**Skip for:** Typo fixes, single-line changes

### Stage 2 — Implementation

**Goal:** Make the changes

**Actions:**
- Implement changes per plan
- Keep diffs small
- Document changes
- Don't claim success yet

**Gate:** Changes must match plan

**Exit Criteria:**
- Files modified as planned
- No unintended changes
- Changes documented

### Stage 3 — Local Validation

**Goal:** Basic local checks

**Actions:**
- Check file syntax (markdown YAML)
- Verify file structure
- Check for obvious errors
- Test locally if possible

**Gate:** No obvious local errors

**Exit Criteria:**
- Files parse correctly
- No syntax errors
- Basic structure intact

### Stage 4 — Visual/Render Validation

**Goal:** Ensure visual correctness

**Actions:**
- Run markdown-render-validator
- Run svg-layout-validator
- Run github-readme-auditor
- Check visual appearance

**Gate:** All visual validators must PASS

**Exit Criteria:**
- markdown-render-validator: PASS
- svg-layout-validator: PASS
- github-readme-auditor: PASS

### Stage 5 — CI/Security Validation

**Goal:** Ensure CI and safety

**Actions:**
- Run ci-gate-reviewer
- Check workflows syntax
- Verify no false positives
- Confirm security model maintained

**Gate:** CI validator must PASS

**Exit Criteria:**
- ci-gate-reviewer: PASS
- No security regressions
- Workflows valid

### Stage 6 — Codex Skeptical Review

**Goal:** Independent review

**Actions:**
- Codex reviews diff
- Codex challenges claims
- Codex searches for issues
- Codex requires evidence

**Gate:** Codex must find no blocking issues

**Exit Criteria:**
- codex-cross-review: PASS
- Evidence provided
- No suspicious claims

### Stage 7 — Release Readiness Gate

**Goal:** Final decision

**Actions:**
- Run release-readiness-gate
- Collect all validator results
- Make final decision

**Gate:** All 5 validators must PASS

**Exit Criteria:**
- All validators: PASS
- Evidence documented
- Final status: READY

### Stage 8 — Commit/Push

**Goal:** Ship the changes

**Actions:**
- Commit with proper message
- Push to GitHub
- Verify CI passes

**Gate:** Only if Stage 7 returned READY

**Exit Criteria:**
- Changes committed
- CI green on GitHub
- Task complete

## Decision Matrix

| Stage | Can Proceed To | Must Fix First | Abort If |
|-------|---------------|----------------|----------|
| 0. Inspection | 1 (Plan) or 2 (Implement) | Problem unclear | No problem found |
| 1. Visual Plan | 2 (Implement) | Plan too generic | Cancel task |
| 2. Implementation | 3 (Local Validation) | Changes don't match plan | Revert changes |
| 3. Local Validation | 4 (Visual Validation) | Syntax errors | Fix syntax |
| 4. Visual Validation | 5 (CI Validation) | Visual FAIL | Fix visual issues |
| 5. CI Validation | 6 (Codex Review) | CI FAIL | Fix CI issues |
| 6. Codex Review | 7 (Release Gate) | Codex FAIL | Fix Codex issues |
| 7. Release Gate | 8 (Commit/Push) | Any FAIL | Fix all issues |
| 8. Commit/Push | Complete | CI fails on GitHub | Fix and retry |

## Fast-Path for Trivial Changes

For **trivial changes only** (typo, single line):

- Skip Stage 1 (Visual Plan)
- Skip Stage 3-6 (Validation)
- Go directly to Stage 7 (Release Gate)
- Must still pass all validators

## Validation Commands

At each validation stage, run appropriate commands:

```bash
# Stage 3: Local validation
bash -n script.sh
python -m py_compile file.py
yamllint workflow.yml

# Stage 4: Visual validation
/skills/markdown-render-validator/SKILL.md README.md
/skills/svg-layout-validator/SKILL.md assets/*.svg
/skills/github-readme-auditor/SKILL.md README.md

# Stage 5: CI validation
/skills/ci-gate-reviewer/SKILL.md .github/workflows/*

# Stage 6: Codex review
/skills/codex-cross-review/SKILL.md [git diff]

# Stage 7: Release gate
/skills/release-readiness-gate/SKILL.md [all validator outputs]
```

## Integration

Use this protocol with claude-codex-dual-review.md for complete workflow.
Reference visual-plan-first.md for when Stage 1 is required.
