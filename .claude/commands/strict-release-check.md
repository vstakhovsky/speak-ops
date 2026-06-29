# Strict Release Check Command

## Purpose

Run final validation gate before commit. Only allow READY if all validators pass.

## When to Use

- After all implementation work is complete
- After all validators have run
- Before any git commit
- Before marking any task as "done"

## Inputs

- Evidence from all validators:
  - markdown-render-validator output
  - svg-layout-validator output
  - github-readme-auditor output
  - ci-gate-reviewer output
  - codex-cross-review output
- Git diff showing changes

## What It Does

Runs release-readiness-gate skill to make final READY/NOT READY decision.

### Checks All Validators

1. markdown-render-validator - Must PASS
2. svg-layout-validator - Must PASS
3. github-readme-auditor - Must PASS
4. ci-gate-reviewer - Must PASS
5. codex-cross-review - Must PASS

### Collects Evidence

- Validator outputs
- Files inspected
- Known limitations
- Remaining risks

### Makes Final Decision

**READY** only if:
- ✅ All 5 validators PASS
- ✅ Evidence provided for each
- ✅ No blocking issues
- ✅ No suspicious claims

**NOT READY** if:
- ❌ Any validator FAILS
- ❌ Evidence missing
- ❌ Blocking issues remain
- ❌ CI will fail
- ❌ Security regression

### Prevents Override

Agent must NOT override gate:

- No self-approval
- No "close enough" judgments
- No "I'll fix later" promises
- No skipping validators

If NOT READY, agent must fix issues and re-run gate.

## Validators to Run

Run all 5 validators and collect outputs:
1. /skills/markdown-render-validator/SKILL.md
2. /skills/svg-layout-validator/SKILL.md
3. /skills/github-readme-auditor/SKILL.md
4. /skills/ci-gate-reviewer/SKILL.md
5. /skills/codex-cross-review/SKILL.md
6. /skills/release-readiness-gate/SKILL.md (decision maker)

## Output Format

```markdown
## Release Readiness Gate

| Validator                | Status | Evidence                  | Notes               |
| ------------------------ | ------ | ------------------------- | ------------------- |
| markdown-render-validator | PASS  | [evidence]                | ✅                  |
| svg-layout-validator     | PASS  | [evidence]                | ✅                  |
| github-readme-auditor    | PASS  | [evidence]                | ✅                  |
| ci-gate-reviewer         | PASS  | [evidence]                | ✅                  |
| codex-cross-review       | PASS  | [evidence]                | ✅                  |

## Final Status

READY / NOT READY

## Evidence

* Checks run: [list]
* Files inspected: [list]
* Known limitations: [list]
* Remaining risks: [list]
```

## Hard-Fail Criteria

Command FAILS (returns NOT READY) if:

- Any validator returns FAIL
- Evidence is missing or incomplete
- Blocking issues remain unresolved
- CI will fail on GitHub
- Security regression detected

## Integration

This is the FINAL gate before commit.
No commit allowed unless gate returns READY.
Use with claude-codex-dual-review and staged-validation protocols.
