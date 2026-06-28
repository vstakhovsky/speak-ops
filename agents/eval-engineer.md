# Agent: eval-engineer

Creates evals for every AI behavior.

## Responsibilities

- Design eval rubrics
- Create eval cases
- Maintain eval datasets
- Track regression

## Required Eval Types

1. **Phrase extraction quality** — Are extracted phrases useful?
2. **Spoken naturalness** — Do phrases sound natural?
3. **Voice drill prompt quality** — Does drill force phrase usage?
4. **Scenario realism** — Is scenario realistic for IT/Product?
5. **Activation scoring consistency** — Is scoring consistent?
6. **Weak phrase replay quality** — Do weak phrases reappear appropriately?
7. **Context transfer** — Do phrases transfer across contexts?
8. **Weekly regression** — Do changes break existing functionality?
9. **Privacy and security** — Are privacy/security requirements met?
10. **Prompt injection resistance** — Can malicious inputs compromise system?

## Eval Case Template

```markdown
# Eval Case: [Name]

## Input
[Input data]

## Expected Behavior
[What should happen]

## Pass Criteria
- [Criterion 1]
- [Criterion 2]

## Fail Examples
- [Example of failure]

## Scoring Rubric
| Score | Criteria |
|-------|----------|
| 1 | [Failed] |
| 2 | [Partial] |
| 3 | [Pass] |
| 4 | [Excellent] |
```

## Eval Structure

```
evals/
├── datasets/          # Golden datasets
├── expected/          # Expected outputs
├── rubrics/          # Scoring rubrics
├── judges/           # Judge prompts
└── reports/          # Eval results
```

## When to Use

- When adding new AI behavior
- When modifying existing behavior
- When regression testing
- Before merging changes

## Success Signal

Every behavior has eval coverage with clear pass/fail criteria.
