# Release Readiness Gate

## Purpose

Final gate that decides if work is ready to commit. All validators must pass before READY status.

## When to Use

- After all implementation work is complete
- After all validators have run
- Before any git commit
- Before marking any task as "done"

## Required Validators

Must run and PASS all of:

1. **markdown-render-validator** - README/docs render correctly
2. **svg-layout-validator** - Diagrams are readable
3. **github-readme-auditor** - Landing page is professional
4. **ci-gate-reviewer** - CI checks are effective
5. **codex-cross-review** - Skeptical review passes

## Input Requirements

Before running this gate, must have:

- Evidence of validator execution (output files or logs)
- Git diff showing what changed
- Visual plan (for non-trivial changes)
- Decision log (for architectural changes)

## Final Status Rules

### READY

Return **READY** only if:

- ✅ All 5 validators return PASS
- ✅ Evidence is provided for each validator
- ✅ No blocking issues remain
- ✅ Codex cross-review finds no suspicious claims
- ✅ CI gate review shows no false positive risks

### NOT READY

Return **NOT READY** if any validator returns FAIL or:

- ❌ Any validator failed
- ❌ Validation not performed
- ❌ Evidence missing
- ❌ Blocking issues unresolved
- ❌ CI will fail on GitHub
- ❌ Security regression detected
- ❌ Documentation incomplete

## Override Prevention

The agent must NOT override this gate.

- No self-approval
- No "close enough" judgments
- No "I'll fix it later" promises
- No skipping validators to save time

If gate returns NOT READY, agent must:

1. Fix all blocking issues
2. Re-run failed validators
3. Re-run release-readiness-gate
4. Only commit if gate returns READY

## Output Format

```markdown
## Release Readiness Gate

| Validator                | Status | Evidence                             | Notes               |
| ------------------------ | ------ | ------------------------------------ | ------------------- |
| markdown-render-validator | PASS   | 635 lines, 0 trailing whitespace     | ✅ README formatted |
| svg-layout-validator     | PASS   | Min font 14px, no overlaps            | ✅ Diagrams readable |
| github-readme-auditor    | PASS   | First screen clear, no broken MD     | ✅ Professional     |
| ci-gate-reviewer         | PASS   | Workflows valid, no false positives   | ✅ CI effective     |
| codex-cross-review       | PASS   | No suspicious claims, evidence shown   | ✅ Review passed    |

## Final Status

READY / NOT READY

## Evidence

* Checks run: [list of validators executed]
* Files inspected: [files reviewed]
* Known limitations: [any caveats]
* Remaining risks: [what could still go wrong]
```

## Examples

### READY Example

```markdown
## Release Readiness Gate

| Validator                | Status | Evidence                          | Notes               |
| ------------------------ | ------ | --------------------------------- | ------------------- |
| markdown-render-validator | PASS  | 635 lines, 0 trailing whitespace    | ✅ README formatted |
| svg-layout-validator     | PASS  | Min font 14px, no overlaps           | ✅ Diagrams readable |
| github-readme-auditor    | PASS  | Clear first screen, no broken MD     | ✅ Professional     |
| ci-gate-reviewer         | PASS  | Workflows valid, no false positives  | ✅ CI effective     |
| codex-cross-review       | PASS  | Evidence provided, no issues found   | ✅ Review passed    |

## Final Status

READY

## Evidence

* Checks run: markdown-render-validator, svg-layout-validator, github-readme-auditor, ci-gate-reviewer, codex-cross-review
* Files inspected: README.md, assets/speakops-architecture.svg, assets/speakops-core-loop.svg, .github/workflows/*
* Known limitations: GitHub rendering may differ slightly from local
* Remaining risks: None significant - all validators pass
```

### NOT READY Example

```markdown
## Release Readiness Gate

| Validator                | Status | Evidence                              | Notes                  |
| ------------------------ | ------ | ------------------------------------- | --------------------- |
| markdown-render-validator | FAIL   | README.md still single line            | ❌ Not fixed          |
| svg-layout-validator     | FAIL   | Font 12px found at line 45            | ❌ Below minimum      |
| github-readme-auditor    | PASS  | N/A                                   | ✅                    |
| ci-gate-reviewer         | FAIL   | Secret scan has false positive patterns | ❌ Will fail on docs |
| codex-cross-review       | FAIL   | No evidence of validation             | ❌ Unverified claims |

## Final Status

NOT READY

## Evidence

* Checks run: markdown-render-validator, svg-layout-validator, github-readme-auditor, ci-gate-reviewer, codex-cross-review
* Files inspected: README.md, assets/speakops-architecture.svg, assets/speakops-core-loop.svg
* Known limitations: None
* Remaining risks: High - 3/5 validators failed, evidence missing
```

## Integration

This is the FINAL gate. Runs after all other validators.
Decision is binary: READY or NOT READY.
No commit allowed unless gate returns READY.
