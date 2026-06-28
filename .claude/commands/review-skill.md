# Review Skill

**Purpose:** Review and improve a SpeakOps skill for quality, naturalness, and completeness.

## When to Use

- After creating or modifying a skill
- Before merging skill changes
- When skill quality is unclear
- When evals indicate skill issues

## Inputs

```bash
/review-skill --skill <skill-name>

# Examples
/review-skill --skill phrase-extractor
/review-skill --skill voice-drill-builder
/review-skill --skill activation-scorer
```

## Workflow Steps

1. **Read skill definition**
   - Load SKILL.md file
   - Understand skill purpose
   - Review trigger conditions
   - Check inputs/outputs

2. **Check skill components**
   - SKILL.md exists and complete
   - Eval cases documented
   - Examples provided
   - Risks and limitations noted

3. **Assess quality dimensions**
   - Clarity of instructions
   - Naturalness of language
   - Completeness of workflow
   - Quality of examples
   - Relevance to IT/Product/AI context

4. **Run skill evals**
   - Execute skill-specific evals
   - Check pass/fail criteria
   - Identify failures
   - Note edge cases

5. **Generate review report**
   - Overall assessment (pass/fail)
   - Critical issues (block)
   - Quick wins (should fix)
   - Can wait (nice to have)
   - Specific recommendations

## Review Dimensions

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| Clarity | 20% | Instructions are clear and unambiguous |
| Naturalness | 25% | Language sounds natural, not AI-like |
| Completeness | 20% | All required components present |
| Examples | 15% | Examples are helpful and accurate |
| Context | 10% | IT/Product/AI context appropriate |
| Evals | 10% | Eval cases are comprehensive |

## Output Format

```markdown
# Skill Review: [skill-name]

## Overall Assessment
**Status:** PASS / NEEDS REVISION / BLOCK

## Critical Issues (block before merge)
- [Issue description]

## Quick Wins (should fix)
- [Issue description]

## Can Wait (nice to have)
- [Issue description]

## Eval Results
- [Eval name]: [PASS/FAIL] - [notes]
- [Eval name]: [PASS/FAIL] - [notes]

## Recommendations
1. [Specific recommendation]
2. [Specific recommendation]

## Summary
[Brief summary of findings]
```

## Quality Checklist

Before a skill passes review:

✅ **Documentation:**
- [ ] SKILL.md exists
- [ ] Purpose is clear
- [ ] Trigger conditions defined
- [ ] Inputs documented
- [ ] Outputs documented
- [ ] Workflow explained

✅ **Quality:**
- [ ] Instructions are clear
- [ ] Language is natural
- [ ] Examples are helpful
- [ ] Context is appropriate
- [ ] No AI-like phrasing

✅ **Evals:**
- [ ] Eval cases documented
- [ ] Pass criteria defined
- [ ] Edge cases considered
- [ ] Fail examples provided

✅ **Safety:**
- [ ] Risks documented
- [ ] Limitations noted
- [ ] Privacy reviewed
- [ ] Security checked

## Common Issues

❌ **Critical (block):**
- Missing SKILL.md
- Unclear instructions
- AI-like language
- No eval cases
- Privacy/security issues

⚠️ **Quick Wins (should fix):**
- Weak examples
- Unclear workflow
- Missing context
- Incomplete documentation

💡 **Can Wait (nice to have):**
- More examples
- Better formatting
- Additional edge cases
- Enhanced documentation

## Related Skills

- **eval-engineer** — Creates evals for skills
- **docs-architect** — Improves documentation
- **codex-reviewer** — Independent review

## Related Evals

- All skill-specific evals
- Quality consistency evals

## Example

```bash
/review-skill --skill phrase-extractor

# Output
# Skill Review: phrase-extractor

## Overall Assessment
**Status:** NEEDS REVISION

## Critical Issues (block before merge)
- Eval cases missing for domain filtering
- Privacy review not documented

## Quick Wins (should fix)
- Add more examples for B2-level phrases
- Improve workflow clarity
- Add phrase selection criteria

## Can Wait (nice to have)
- Add edge cases for empty input
- Expand domain options

## Eval Results
- phrase-extraction-quality: PASS - Good extraction quality
- spoken-naturalness: NEEDS REVISION - Some formal phrases slipping through

## Recommendations
1. Add eval cases for domain filtering
2. Run privacy/security review
3. Improve naturalness filtering
4. Add more examples

## Summary
Skill has good extraction logic but needs eval coverage and privacy review before merging.
```

---

**Command Version:** 1.0
**Status:** Active
