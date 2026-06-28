# Phrase Extraction Quality Rubric

## Eval Goal

Assess whether phrase extraction identifies useful spoken Business English phrases and rejects written/formal/AI-like phrases.

## Scoring Rubric

| Score | Level | Criteria |
|-------|-------|----------|
| 1 | Failed | Extracts formal/written phrases, misses useful ones |
| 2 | Poor | Mix of useful and formal phrases, poor filtering |
| 3 | Acceptable | Mostly useful phrases, some formal ones slip through |
| 4 | Good | Consistently useful phrases, minimal formal content |
| 5 | Excellent | Only natural spoken phrases, perfect domain filtering |

**Pass threshold:** 4

## Dimensions

### 1. Phrase Usefulness (40 points)
- Relevant to IT/Product/AI contexts: 15 points
- Practical for interviews/meetings: 15 points
- Not too generic: 10 points

### 2. Naturalness (30 points)
- Sounds spoken, not written: 15 points
- Appropriate for business meetings: 10 points
- Not AI-like: 5 points

### 3. Domain Filtering (20 points)
- Matches specified domain: 15 points
- Appropriate level (B1-C2): 5 points

### 4. Metadata Quality (10 points)
- Accurate Russian meaning: 3 points
- Clear context: 3 points
- Good examples: 4 points

## Sample Cases

### Case 1: Good extraction
**Input:** Meeting transcript with natural phrases
**Expected output:** Extract "push back on", "loop in", "align on"
**Pass criteria:** All phrases score 4+ on naturalness, metadata accurate

### Case 2: Reject formal phrases
**Input:** Academic text with formal language
**Expected output:** Reject or rewrite "I would like to emphasize", "Furthermore"
**Pass criteria:** Formal phrases identified and filtered out

### Case 3: Domain filtering
**Input:** General business text, domain: ai-evals
**Expected output:** Only AI/evals-related phrases extracted
**Pass criteria:** Non-AI phrases filtered out

### Case 4: Level appropriate
**Input:** C2-level text, target level: B2
**Expected output:** Extract B2-appropriate phrases, skip overly complex ones
**Pass criteria:** Extracted phrases match target level

## Edge Cases

### Edge case 1: Borderline formality
**Input:** "Therefore, we should proceed with..."
**Expected:** Flag as borderline, provide rewrite
**Pass criteria:** Borderline phrases identified, not accepted as-is

### Edge case 2: Multi-word phrases
**Input:** "get buy-in from", "push back on"
**Expected:** Extract complete phrases, not sub-phrases
**Pass criteria:** Phrase boundaries correct

### Edge case 3: Context-dependent phrases
**Input:** "under the hood" (in technical vs non-technical context)
**Expected:** Extract for technical domain, reject for general
**Pass criteria:** Context awareness demonstrated

## Fail Examples

### Example 1: Over-extraction
**Input:** Generic business email
**Output:** Extracts "sincerely", "regarding", "concerning"
**Why it fails:** These are too generic, not specific to IT/Product

### Example 2: Missed natural phrases
**Input:** Natural meeting transcript
**Output:** Misses "let's loop in engineering", "I'd push back on that"
**Why it fails:** Useful phrases not extracted

### Example 3: Accepted formal phrases
**Input:** Formal report
**Output:** Accepts "it is crucial to note that", "furthermore"
**Why it fails:** Formal phrases should be rejected or rewritten

## Related Evals

- Spoken Naturalness — Filters extracted phrases
- Voice Drill Quality — Uses extracted phrases

---

**Eval ID:** phrase-extraction-quality
**Category:** Quality
**Status:** Active
