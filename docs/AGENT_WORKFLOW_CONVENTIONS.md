# Agent Workflow Conventions

**Purpose:** Define how agents work together in SpeakOps development.

## Agent Roles

SpeakOps uses 11 specialized agents with clear responsibilities:

| Agent | Purpose | When Used |
|-------|---------|----------|
| **spec-planner** | Convert requests to specs | Before implementing features |
| **repo-architect** | Review repository structure | Before structural changes |
| **skill-architect** | Design Claude Code skills | When creating/modifying skills |
| **voice-flow-designer** | Design voice practice flows | When building voice drills |
| **spoken-naturalness-judge** | Judge phrase naturalness | When filtering phrases |
| **eval-engineer** | Create evals for behaviors | When adding/changing behaviors |
| **activation-scorer** | Maintain scoring model | When working with scores |
| **privacy-security-reviewer** | Security/privacy review | Before ingestion/security changes |
| **lazy-senior-dev** | Reduce scope | Before any implementation |
| **codex-reviewer** | Independent review | Before merging changes |
| **docs-architect** | Maintain documentation | When documentation changes |

## Agent Collaboration Patterns

### Pattern 1: Feature Development

```
spec-planner → lazy-senior-dev → repo-architect → implementation
             → eval-engineer → privacy-security-reviewer → codex-reviewer → docs-architect
```

**When:** Implementing new features

**Flow:**
1. **spec-planner** creates spec
2. **lazy-senior-dev** cuts scope
3. **repo-architect** checks structure
4. Implementation happens
5. **eval-engineer** creates evals
6. **privacy-security-reviewer** checks security
7. **codex-reviewer** independent review
8. **docs-architect** updates docs

### Pattern 2: Skill Creation

```
skill-architect → spoken-naturalness-judge → eval-engineer → codex-reviewer
```

**When:** Creating new skills

**Flow:**
1. **skill-architect** designs skill
2. **spoken-naturalness-judge** checks naturalness
3. **eval-engineer** creates evals
4. **codex-reviewer** independent review

### Pattern 3: Voice Drill

```
voice-flow-designer → spoken-naturalness-judge → eval-engineer
```

**When:** Building voice drills

**Flow:**
1. **voice-flow-designer** designs drill
2. **spoken-naturalness-judge** checks phrases
3. **eval-engineer** creates evals

### Pattern 4: Ingestion

```
source-ingestor → privacy-security-reviewer → phrase-extractor → spoken-naturalness-judge
```

**When:** Processing source material

**Flow:**
1. **source-ingestor** ingests content
2. **privacy-security-reviewer** checks privacy
3. **phrase-extractor** extracts phrases
4. **spoken-naturalness-judge** filters phrases

## Agent Outputs

### Standard Output Format

Each agent should return:

```markdown
## [Agent Name] Review

**Input:** [What was reviewed]
**Context:** [Background information]

### Findings

**Critical Issues (block):**
- [Issue description]

**Quick Wins (should fix):**
- [Issue description]

**Can Wait (nice to have):**
- [Issue description]

### Recommendation
[What to do next]

### Rationale
[Why this recommendation]
```

## Using Agents in Workflow

### Before Implementation

1. **Call spec-planner** with feature request
2. **Call lazy-senior-dev** to reduce scope
3. **Call repo-architect** to check structure
4. **Review findings** and adjust plan

### During Implementation

1. **Follow implementation plan**
2. **Call appropriate agents** for specific checks
3. **Update based on feedback**

### After Implementation

1. **Call eval-engineer** to create evals
2. **Call privacy-security-reviewer** if needed
3. **Call codex-reviewer** for independent review
4. **Call docs-architect** to update docs

## Agent Interaction Rules

### Rule 1: Explicit Invocation

**Call agents explicitly:**
```bash
# As spec-planner
/agent spec-planner "Convert this feature request into a spec"

# As lazy-senior-dev
/agent lazy-senior-dev "Review this plan for scope"

# As privacy-security-reviewer
/agent privacy-security-reviewer "Review this ingestion change"
```

### Rule 2: Sequential Flow

**Follow natural sequence:**
- Planning → Review → Implementation → Eval → Review
- Don't skip steps
- Don't run agents in wrong order

### Rule 3: Output Consistency

**All agents return:**
- Clear findings
- Actionable recommendations
- Specific next steps
- Rationale for decisions

### Rule 4: Independent Review

**Codex-reviewer is always last:**
- After all other agents
- Independent assessment
- Can challenge consensus
- Final approval gate

## Common Patterns

### Pattern A: New Skill

```bash
# 1. Design skill
/agent skill-architect "Design a skill for [purpose]"

# 2. Check naturalness
/agent spoken-naturalness-judge "Review skill for naturalness"

# 3. Create evals
/agent eval-engineer "Create evals for this skill"

# 4. Independent review
/agent codex-reviewer "Review this skill and its evals"
```

### Pattern B: Security Review

```bash
# 1. Privacy/security review
/agent privacy-security-reviewer "Review this ingestion change"

# 2. Address findings

# 3. Re-review if needed
/agent privacy-security-reviewer "Re-review after fixes"
```

### Pattern C: Scope Reduction

```bash
# 1. Create plan
[Create implementation plan]

# 2. Reduce scope
/agent lazy-senior-dev "Review this plan and cut scope"

# 3. Proceed with reduced plan
[Implement reduced plan]
```

## Agent Quality

### Good Agent Usage ✅

- Clear agent invocation
- Appropriate agent for task
- Sequential workflow
- Output reviewed and acted on
- Decision documented

### Poor Agent Usage ❌

- Vague agent invocation
- Wrong agent for task
- Skipping agents
- Ignoring agent output
- No documentation

## Troubleshooting

### Issue: Agent Recommendations Conflicting

**Solution:**
1. Review all recommendations
2. Identify conflicts
3. Make decision based on priority
4. Document trade-offs

### Issue: Agent Output Unclear

**Solution:**
1. Re-read agent specification
2. Clarify the task
3. Re-invoke agent with clearer prompt
4. Ask for specific format

### Issue: Too Many Agents

**Solution:**
1. Use lazy-senior-dev to cut scope
2. Combine agent reviews where possible
3. Focus on critical agents only
4. Skip optional agents for minor changes

## Documentation

### For Each Agent Invocation

- [ ] Agent purpose documented
- [ ] Input provided
- [ ] Output reviewed
- [ ] Findings acted on
- [ ] Decision logged

### For Decisions

- [ ] Which agents were consulted
- [ ] What recommendations were followed
- [ ] What recommendations were rejected
- [ ] Why decisions were made
- [ ] Trade-offs documented

## Best Practices

### For Users

1. **Use agents explicitly** — Clear invocations
2. **Follow sequence** — Natural workflow order
3. **Review outputs** — Don't ignore findings
4. **Document decisions** — Record rationale
5. **Use lazy-senior-dev** — Cut scope early

### For Development

1. **Agent-first approach** — Consult agents before implementing
2. **Sequential workflow** — Follow natural order
3. **Independent review** — Always get Codex review
4. **Documentation** — Log all decisions
5. **Iteration** — Re-run agents if needed

---

**Convention Version:** 1.0
**Purpose:** Ensure consistent, effective agent collaboration
