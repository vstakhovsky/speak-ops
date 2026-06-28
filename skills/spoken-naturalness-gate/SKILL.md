# spoken-naturalness-gate

Judges whether phrases sound natural in real meetings.

## Trigger Conditions

User runs:
```bash
/filter-spoken --remove-ai-like
```

Or when:
- Filtering extracted phrases
- Reviewing voice drill prompts
- Checking phrase cards
- Evaluating practice transcripts

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| phrase | string | Phrase to judge |
| context | string | Optional context (meeting, interview, etc.) |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| verdict | string | accept, reject, rewrite |
| score | number | 1–5 naturalness score |
| better_version | string | Improved spoken version |
| confident_version | string | Stronger version |
| softer_version | string | More diplomatic version |
| reason | string | Why it sounds better |

## Scoring Rubric

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Written/robotic/AI-like | "I would like to emphasize that..." |
| 2 | Too formal for speech | "Furthermore, it is crucial to note..." |
| 3 | Understandable but stiff | "Therefore, we should proceed with..." |
| 4 | Natural but could be shorter | "So I think we should..." |
| 5 | Natural, short, easy to say | "Let's go with..." |

## Workflow

1. **Receive phrase** — Get phrase to judge
2. **Assess naturalness** — Score 1–5
3. **Check red flags** — Look for formal/AI patterns
4. **Generate verdict** — Accept, reject, or rewrite
5. **Create alternatives** — Better, confident, softer versions
6. **Explain reasoning** — Why the alternative is better

## Red Flags

**Reject or rewrite phrases that are:**
- Too formal
- Too academic
- Too written
- Too AI-like
- Too long to say aloud
- Full of abstract nouns
- Unnatural for meetings/interviews

**Avoid patterns:**
- "I would like to emphasize..."
- "It is crucial to note..."
- "Furthermore..."
- "Moreover..."
- "utilize" (when vague)
- "leverage" (when vague)
- Long passive constructions

## Examples

### Example 1: Reject formal phrase
```
Input: "I would like to emphasize the importance of..."
Verdict: reject
Score: 1
Better version: "The key thing is..."
Confident version: "What matters is..."
Softer version: "It's worth noting that..."
Reason: Short, direct, natural spoken rhythm
```

### Example 2: Accept natural phrase
```
Input: "Let's loop in engineering."
Verdict: accept
Score: 5
Reason: Short, natural meeting language
```

### Example 3: Rewrite stiff phrase
```
Input: "Therefore, we should proceed with the implementation."
Verdict: rewrite
Score: 3
Better version: "So let's start implementing."
Confident version: "Let's get this implemented."
Softer version: "Maybe we should start implementing."
Reason: "Therefore" is too formal for speech
```

## Eval Cases

### Test 1: Reject AI-like phrases
**Input:** "I would like to emphasize that..."
**Expected:** Verdict: reject, score ≤ 2
**Pass criteria:** Phrase identified as unnatural

### Test 2: Accept natural phrases
**Input:** "Let's loop in engineering."
**Expected:** Verdict: accept, score ≥ 4
**Pass criteria:** Phrase identified as natural

### Test 3: Rewrite borderline phrases
**Input:** "Therefore, we should..."
**Expected:** Verdict: rewrite, better version provided
**Pass criteria:** Improved version is more natural

## Risks and Limitations

- Subjective judgment of naturalness
- Cultural differences in spoken English
- Context-dependent appropriateness
- May prefer casual over professional in some cases
- Different norms for different seniority levels

## Related Skills

- **phrase-extractor** — Provides phrases to filter
- **voice-drill-builder** — Uses filtered phrases in drills
- **activation-scorer** — May adjust scores based on naturalness
