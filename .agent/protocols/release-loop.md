# Release Loop Protocol

## Purpose

Define the standard workflow for releasing changes in SpeakOps.

## Process

### 1. Pre-Release Checks

Before releasing:

1. **Run all evals** — Ensure quality
2. **Run regression tests** — Check for breakage
3. **Security review** — Final security check
4. **Docs check** — Documentation complete
5. **Decision log** — All changes documented

### 2. Prepare Release

1. **Update version** — Increment version number
2. **Changelog** — Document changes
3. **Release notes** — User-facing summary
4. **Migration guide** — If breaking changes

### 3. Test Release

1. **Smoke test** — Basic functionality
2. **Integration test** — Key workflows
3. **Security test** — Privacy/security checks
4. **Performance test** — If applicable

### 4. Release

1. **Commit changes** — Final commit
2. **Tag release** — Version tag
3. **Create release** — GitHub release (if applicable)
4. **Announce** — Notify users (if applicable)

### 5. Post-Release

1. **Monitor issues** — Watch for problems
2. **Address bugs** — Quick fixes if needed
3. **Gather feedback** — User input
4. **Plan next release** — Roadmap update

## Release Types

### Patch Release (X.Y.Z)

**Scope:** Bug fixes, small improvements

**Process:**
1. Fix bug
2. Add test (regression)
3. Run evals (regression check)
4. Update changelog
5. Release

**Timeframe:** As needed

### Minor Release (X.Y)

**Scope:** New features, improvements

**Process:**
1. Implement feature
2. Add evals
3. Update docs
4. Run all tests
5. Update changelog
6. Release

**Timeframe:** Monthly or as needed

### Major Release (X)

**Scope:** Significant changes, breaking changes

**Process:**
1. Design changes
2. Implement (with evals)
3. Migration guide
4. Comprehensive testing
5. Update all docs
6. Changelog
7. Release notes
8. Release

**Timeframe:** Quarterly or as needed

## Pre-Release Checklist

**Before any release:**

- [ ] All evals pass
- [ ] Regression tests pass
- [ ] Security review passed
- [ ] Documentation updated
- [ ] Decision log complete
- [ ] Changelog updated
- [ ] Version number updated
- [ ] Release notes prepared (if minor/major)

**For major releases:**
- [ ] Migration guide written
- [ ] Breaking changes documented
- [ ] Backward compatibility considered
- [ ] Rollback plan documented

## Release Notes Template

```markdown
# Release X.Y.Z

## Summary
[Brief description of release]

## What's New

### Features
- [Feature 1]
- [Feature 2]

### Improvements
- [Improvement 1]
- [Improvement 2]

## Bug Fixes
- [Bug fix 1]
- [Bug fix 2]

## Breaking Changes
[Any breaking changes with migration guide]

## Security
[Any security-related changes]

## Known Issues
[Any known issues]

## Upgrade Notes
[Any special upgrade instructions]
```

## Changelog Format

```markdown
# Changelog

## [Unreleased]

### Added
- [New features]

### Changed
- [Improvements to existing features]

### Deprecated
- [Features deprecated]

### Removed
- [Features removed]

### Fixed
- [Bug fixes]

### Security
- [Security fixes]
```

## Versioning

**Semantic Versioning:**
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes (backward compatible)

**Examples:**
- 0.1.0 → Initial MVP
- 0.2.0 → Add new skill
- 0.2.1 → Fix bug in skill
- 1.0.0 → Stable release

## Release Criteria

**Patch release:**
- Bug fix confirmed
- Regression test added
- Evals pass
- No breaking changes

**Minor release:**
- Feature complete
- Evals added and passing
- Docs updated
- No breaking changes

**Major release:**
- All features complete
- All evals passing
- Comprehensive docs
- Breaking changes documented
- Migration guide available

## Rollback Plan

**If release has issues:**

1. **Assess impact** — How bad is it?
2. **Determine action** — Fix forward or rollback?
3. **Execute plan** — Hotfix or rollback
4. **Communicate** — Notify users
5. **Post-mortem** — Learn from it

**Rollback triggers:**
- Critical bug
- Security vulnerability
- Data loss risk
- Widespread failure

## Post-Release

**Monitor for:**
- Bug reports
- Performance issues
- Security issues
- User confusion

**Quick fixes:**
- Patch release
- Fast turnaround
- Minimal testing (just regression)
- Clear communication

## Examples

### Example 1: Patch Release

**Issue:** Scoring not updating correctly

**Process:**
1. Fix bug in update_phrase_bank.py
2. Add regression test
3. Run evals (pass)
4. Update changelog
5. Release 0.1.1

### Example 2: Minor Release

**Feature:** Add weak-phrase-replayer skill

**Process:**
1. Implement weak-phrase-replayer
2. Add evals
3. Update docs
4. Run all evals (pass)
5. Update changelog
6. Release 0.2.0

### Example 3: Major Release

**Changes:** New activation scoring model

**Process:**
1. Design new model
2. Implement with evals
3. Migration guide (old → new)
4. Comprehensive testing
5. Update all docs
6. Changelog
7. Release notes
8. Release 1.0.0

## Anti-Patterns

**Don't do this:**
- Release without evals passing
- Skip changelog
- Forget to update version
- Release breaking changes without notice
- Ignore rollback planning

**Do this instead:**
- Always ensure evals pass
- Always update changelog
- Always update version
- Always document breaking changes
- Always plan for rollback

---

**Protocol Version:** 1.0
**Status:** Active
