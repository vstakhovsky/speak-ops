# CI Gate Reviewer

## Purpose

Inspect GitHub Actions workflows to ensure CI checks are effective, safe, and don't fail on false positives.

## When to Use

- After workflow changes
- When CI fails unexpectedly
- Before release-readiness-gate
- When adding new checks

## Inputs

- Workflow files in `.github/workflows/`
- Pre-commit configuration
- CI failure logs (if available)

## Checks Performed

### Workflow Integrity

1. **Workflow syntax**
   - Valid YAML structure
   - Proper indentation
   - Correct GitHub Actions syntax

2. **Job dependencies**
   - Logical job ordering
   - Required dependencies present
   - No circular dependencies

### Check Effectiveness

3. **Markdown check**
   - Trailing whitespace detection
   - Code fence validation
   - HTML tag balance check
   - Should fail on real errors

4. **Secret scan**
   - Must NOT fail on docs mentioning "API key", "secret", "token" as concepts
   - Must detect realistic secret patterns (actual keys, not words)
   - Should ignore `.git`, `node_modules`, `.venv`, images
   - Should allow `.env.example` files
   - Must not be disabled to make checks green

5. **Python check**
   - Linting configured correctly
   - Tests run on appropriate Python versions
   - Dependencies specified

6. **Eval regression check**
   - Runs evals correctly
   - Detects regressions
   - Fails on score degradation

7. **Pre-commit config**
   - Hooks configured appropriately
   - Not overly aggressive
   - Fast enough for development

### False Positive Prevention

8. **Naive secret grep**
   - Avoids generic word matching
   - Uses realistic patterns (ghp_, sk-, AKIA, etc.)
   - Excludes documentation and examples

9. **Check disabling**
   - Security checks not disabled
   - Failures not ignored
   - Real issues fixed, not hidden

10. **Workflow safety**
    - No credential exposure
    - No unsafe operations
    - Appropriate permissions

## Hard-Fail Criteria

Reviewer returns FAIL if any of:

- Markdown CI fails (should be fixed, not disabled)
- Secret scan fails on false positives (patterns too broad)
- Python check fails (uncommitted lint issues)
- Workflow syntax invalid (YAML errors)
- Checks are disabled instead of fixed (security issue)
- Secret scan uses naive grep that fails on documentation words

## Output Format

```markdown
## CI Gate Review

Status: PASS / FAIL

## Workflow Issues

* Critical workflow problems
* secret-scan.yml:45 - Pattern matches documentation words
* markdown-check.yml - Fails on long lines that are acceptable

## False Positive Risks

* Patterns that may fail on safe content
* "API_KEY" pattern fails docs/security.md
* "token" pattern fails examples/

## Required Fixes

[Specific fixes needed]
```

## Examples

### PASS Example

```markdown
## CI Gate Review

Status: PASS

## Workflow Issues

None

## False Positive Risks

None - secret scan uses realistic patterns (ghp_[A-Za-z0-9]{36})

## Required Fixes

None
```

### FAIL Example

```markdown
## CI Gate Review

Status: FAIL

## Workflow Issues

* secret-scan.yml - Greps for word "token" - fails on docs/
* markdown-check.yml - No HTML tag validation - unclosed tags not caught
* python-check.yml - Not configured for Python 3.13+

## False Positive Risks

* Pattern "SECRET_KEY" will match security documentation
* Pattern "password" will match example configuration

## Required Fixes

1. Update secret-scan patterns to realistic formats only
2. Add HTML validation to markdown-check
3. Configure python-check for correct Python version
```

## Limitations

- Cannot test actual CI execution (local vs GitHub)
- May miss edge cases in complex workflows
- False positive analysis requires understanding of repo content
- Workflow interaction effects hard to predict

## Integration

Run during CI changes and before release-readiness-gate.
Works with security-reviewer for comprehensive safety checks.
