# phrase-extractor

Extracts useful spoken Business English phrases from sources.

## Trigger Conditions

User runs:
```bash
/extract-phrases --domain <domain> --level <level>
```

Or when:
- Ingesting source material
- Processing Google Docs, Obsidian, YouTube notes
- Building phrase bank from scratch

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| source_text | string | Text to extract phrases from |
| domain | string | ai-evals, technical-pm, senior-pm, etc. |
| level | string | b1, b2, c1, c2 |
| context | string | Optional context about source |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| phrase | string | The extracted phrase |
| russian_meaning | string | Russian translation |
| domain | string | Domain tag |
| context | string | Where to use it |
| spoken_example | string | Natural spoken example |
| too_formal_version | string | Version to avoid |
| activation_priority | string | high, medium, low |

## Workflow

1. **Read source text** — Parse input text
2. **Identify candidate phrases** — Look for useful patterns
3. **Filter by domain** — Keep phrases relevant to domain
4. **Filter by level** — Keep phrases appropriate for level
5. **Assess usefulness** — Prioritize high-value phrases
6. **Check naturalness** — Run through spoken-naturalness-gate
7. **Generate metadata** — Add Russian meaning, context, examples
8. **Output results** — Return extracted phrases

## Prioritization

Prioritize phrases useful for:
- Interviews
- Meetings
- Stakeholder pushback
- Technical discussions
- AI/evals conversations
- Executive updates
- Conflict situations

Reject phrases that are:
- Too academic
- Too formal
- Too written
- Too AI-like
- Too generic
- Not relevant to IT/Product/AI

## Examples

### Good extraction
```
Source: "We need to push back on this requirement."
Phrase: "push back on"
Russian: возразить против, отрицательно отреагировать
Domain: stakeholder-pushback
Context: When disagreeing with a requirement
Spoken example: "I'd push back on that timeline."
Too formal version: "I would respectfully disagree with said timeline."
Activation priority: high
```

### Bad extraction (should reject)
```
Source: "Furthermore, it is imperative that we..."
Phrase: "it is imperative that"
Russian: необходимо, чтобы
Domain: generic
Context: N/A
Spoken example: N/A
Too formal version: N/A
Activation priority: reject
```

## Eval Cases

### Test 1: Extract useful phrases
**Input:** Meeting transcript with natural phrases
**Expected:** Extract 5–10 useful spoken phrases
**Pass criteria:** All extracted phrases score 4+ on naturalness

### Test 2: Reject formal phrases
**Input:** Academic text with formal language
**Expected:** Reject or rewrite formal phrases
**Pass criteria:** No phrases with naturalness < 4

### Test 3: Domain filtering
**Input:** General business text
**Expected:** Filter by specified domain
**Pass criteria:** Only relevant domains tagged

## Risks and Limitations

- May extract phrases that sound written
- May miss context-dependent phrases
- May over-extract generic phrases
- Requires manual review for quality
- Depends on source text quality

## Related Skills

- **spoken-naturalness-gate** — Filters extracted phrases
- **phrase-card-generator** — Creates cards from extracted phrases
- **activation-scorer** — Assigns initial activation scores
