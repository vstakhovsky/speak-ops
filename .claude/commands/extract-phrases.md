# Extract Phrases

**Purpose:** Extract useful Business English phrases from source text and prepare them for filtering.

## When to Use

- After ingesting source material
- When you have raw text with potential phrases
- To build or expand your phrase bank
- After meetings, interviews, or conferences

## Inputs

```bash
/extract-phrases --domain <domain> --level <level>

# Examples
/extract-phrases --domain stakeholder-pushback --level b2-c1
/extract-phrases --domain ai-evals --level c1-c2
/extract-phrases --domain senior-pm --level b2
```

## Domain Options

| Domain | Description | Use For |
|--------|-------------|---------|
| `stakeholder-pushback` | Managing disagreements | Interviews, meetings |
| `ai-evals` | AI evaluation and testing | Technical discussions |
| `senior-pm` | Senior product management | Leadership scenarios |
| `technical-pm` | Technical product management | Engineering collaboration |
| `prioritization` | Roadmap and trade-off decisions | Planning meetings |
| `interview-general` | General interview phrases | Interview preparation |

## Level Options

| Level | Description | Target Audience |
|-------|-------------|-----------------|
| `b1-b2` | Intermediate | Building foundation |
| `b2-c1` | Upper-intermediate | Professional contexts |
| `c1-c2` | Advanced | Senior roles, technical discussions |

## Workflow Steps

1. **Analyze source text**
   - Identify candidate phrases
   - Check phrase length (2–6 words ideal)
   - Assess phrase frequency

2. **Filter by domain**
   - Keep phrases relevant to domain
   - Remove out-of-domain phrases
   - Tag with subdomain if needed

3. **Filter by level**
   - Assess vocabulary complexity
   - Check grammatical structures
   - Match to target level

4. **Generate metadata**
   - Russian meaning
   - Context description
   - Natural spoken example
   - Too-formal version to avoid
   - Activation priority

5. **Output extracted phrases**
   - List of phrases with metadata
   - Count by domain
   - Flag for review

## Output Format

```json
{
  "status": "success",
  "domain": "stakeholder-pushback",
  "level": "b2-c1",
  "phrases_extracted": 127,
  "phrases": [
    {
      "phrase": "push back on",
      "russian": "возразить против",
      "context": "Use when disagreeing with stakeholder requests",
      "spoken_example": "I'd push back on that timeline.",
      "too_formal_version": "I would respectfully disagree with said timeline.",
      "activation_priority": "high"
    }
  ],
  "timestamp": "2025-06-28T10:05:00Z"
}
```

## Phrase Selection Criteria

✅ **Extract phrases that are:**
- Useful for interviews/meetings
- IT/Product/AI context appropriate
- Spoken Business English (not written)
- 2–6 words in length
- High-frequency in professional settings

❌ **Reject phrases that are:**
- Too academic
- Too formal
- Too written/AI-like
- Too generic
- Outside domain
- Wrong level

## Safety & Privacy Notes

⚠️ **Quality:**
- Phrases are NOT yet filtered for naturalness
- Review output before proceeding
- Some phrases may be too formal
- Check Russian meanings for accuracy

🔒 **Privacy:**
- No personal data in phrases
- Source content not stored
- Only extracted phrases are saved

## Related Skills

- **spoken-naturalness-gate** — Filters extracted phrases for naturalness
- **phrase-card-generator** — Creates phrase cards from output
- **source-ingestor** — Provides input text

## Related Evals

- **phrase-extraction-quality** — Tests extraction quality
- **spoken-naturalness** — Next step filtering

## Example

```bash
/extract-phrases --domain stakeholder-pushback --level b2-c1

# Output
{
  "status": "success",
  "domain": "stakeholder-pushback",
  "level": "b2-c1",
  "phrases_extracted": 89,
  "phrases": [
    {
      "phrase": "push back on",
      "russian": "возразить против",
      "context": "Use when disagreeing with stakeholder requests",
      "spoken_example": "I'd push back on that timeline.",
      "too_formal_version": "I would respectfully disagree with said timeline.",
      "activation_priority": "high"
    }
  ]
}
```

---

**Command Version:** 1.0
**Status:** Active
