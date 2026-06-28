# Improve Repository

**Purpose:** Analyze and improve the SpeakOps repository structure, documentation, and quality.

## When to Use

- Onboarding to SpeakOps development
- Before making significant changes
- When repository quality is unclear
- As part of regular maintenance

## Inputs

```bash
/improve-repo

# Optional: Focus on specific area
/improve-repo --focus <area>

# Focus options
/improve-repo --focus docs
/improve-repo --focus structure
/improve-repo --focus security
/improve-repo --focus evals
```

## Workflow Steps

1. **Analyze repository structure**
   - Check directory organization
   - Review file placement
   - Identify missing components
   - Note duplications

2. **Review documentation**
   - Check README completeness
   - Review CLAUDE.md clarity
   - Verify AGENTS.md accuracy
   - Assess CODEX.md usefulness
   - Check SECURITY.md completeness

3. **Assess skills**
   - Verify all skills have SKILL.md
   - Check skill eval coverage
   - Review skill examples
   - Identify missing skills

4. **Check evals**
   - Verify eval rubrics exist
   - Check eval case coverage
   - Review eval quality
   - Identify missing evals

5. **Security review**
   - Check for secrets
   - Review file access patterns
   - Assess data handling
   - Verify privacy compliance

6. **Generate improvement report**
   - Critical issues (fix immediately)
   - Quick wins (should fix soon)
   - Can wait (nice to have)
   - Specific recommendations

## Review Dimensions

| Dimension | Weight | Checks |
|-----------|--------|--------|
| Structure | 20% | Directory organization, file placement |
| Documentation | 25% | README, guides, completeness |
| Skills | 20% | SKILL.md files, eval coverage |
| Evals | 15% | Rubrics, cases, quality |
| Security | 10% | Secrets, privacy, safety |
| Quality | 10% | Consistency, best practices |

## Output Format

```markdown
# Repository Improvement Report

**Generated:** [timestamp]
**Focus:** [area or "full repository"]

## Overall Score
**Score:** [X/100]
**Status:** [EXCELLENT/GOOD/NEEDS WORK/CRITICAL]

## Critical Issues (fix immediately)
- [Issue]
- [Impact]
- [Recommendation]

## Quick Wins (should fix soon)
- [Issue]
- [Impact]
- [Recommendation]

## Can Wait (nice to have)
- [Issue]
- [Recommendation]

## Specific Recommendations

### Documentation
1. [Recommendation]
2. [Recommendation]

### Skills
1. [Recommendation]
2. [Recommendation]

### Evals
1. [Recommendation]
2. [Recommendation]

### Security
1. [Recommendation]
2. [Recommendation]

## Summary
[Brief summary of overall state]
```

## Quality Checklist

✅ **Structure:**
- [ ] Clear directory organization
- [ ] No duplicate files
- [ ] Logical file placement
- [ ] No orphaned files

✅ **Documentation:**
- [ ] README is comprehensive
- [ ] CLAUDE.md is clear
- [ ] AGENTS.md is accurate
- [ ] CODEX.md is useful
- [ ] SECURITY.md is complete

✅ **Skills:**
- [ ] All skills have SKILL.md
- [ ] All skills have evals
- [ ] Examples are helpful
- [ ] Risks are documented

✅ **Evals:**
- [ ] All behaviors have evals
- [ ] Rubrics are comprehensive
- [ ] Cases are specific
- [ ] Pass criteria clear

✅ **Security:**
- [ ] No secrets in repo
- [ ] File access restricted
- [ ] Privacy maintained
- [ ] Inputs sanitized

## Common Issues

❌ **Critical (fix immediately):**
- Secrets in repository
- Missing security review
- No eval coverage
- Unclear documentation

⚠️ **Quick Wins (should fix soon):**
- Missing SKILL.md files
- Incomplete documentation
- Weak examples
- Missing eval cases

💡 **Can Wait (nice to have):**
- Better formatting
- More examples
- Enhanced documentation
- Additional eval cases

## Related Skills

- **repo-architect** — Repository structure analysis
- **docs-architect** — Documentation improvement
- **privacy-security-reviewer** — Security review
- **eval-engineer** — Eval quality assessment

## Example

```bash
/improve-repo --focus docs

# Output
# Repository Improvement Report

**Generated:** 2025-06-28
**Focus:** Documentation

## Overall Score
**Score:** 72/100
**Status:** NEEDS WORK

## Critical Issues (fix immediately)
- README missing architecture diagram
- CLAUDE.md lacks concrete examples
- SECURITY.md missing incident response

## Quick Wins (should fix soon)
- Add getting started guide
- Improve FAQ section
- Add more examples to README

## Can Wait (nice to have)
- Add video tutorials
- Create contribution guide
- Expand troubleshooting section

## Specific Recommendations

### Documentation
1. Add architecture diagram to README
2. Add concrete examples to CLAUDE.md
3. Complete SECURITY.md incident response section
4. Create getting started guide
5. Improve FAQ with real questions

## Summary
Documentation has good foundation but needs concrete examples and completeness improvements to be excellent.
```

---

**Command Version:** 1.0
**Status:** Active
