# Spoken Naturalness Rubric

## Eval Goal

Assess whether phrases sound natural in real spoken Business English, not written/AI-like.

## Scoring Rubric

| Score | Naturalness | Example |
|-------|-------------|---------|
| 1 | Written/robotic/AI-like | "I would like to emphasize that..." |
| 2 | Too formal for speech | "Furthermore, it is crucial to note..." |
| 3 | Understandable but stiff | "Therefore, we should proceed with..." |
| 4 | Natural but could be shorter | "So I think we should..." |
| 5 | Natural, short, easy to say | "Let's go with..." |

**Pass threshold:** 4

## Dimensions

### 1. Spoken Rhythm (25 points)
- Sounds like someone speaking: 10 points
- Natural pauses and flow: 10 points
- Not essay-like: 5 points

### 2. Formality Level (25 points)
- Appropriate for meetings: 15 points
- Not overly formal: 10 points

### 3. Length (20 points)
- Short enough to say easily: 10 points
- Not convoluted: 10 points

### 4. Vocabulary (15 points)
- Clear, common words: 8 points
- Not overly academic: 7 points

### 5. Context Fit (15 points)
- Fits IT/Product/AI context: 10 points
- Natural in meetings/interviews: 5 points

## Red Flags

**Automatic score ≤ 2:**
- "I would like to emphasize..."
- "It is crucial to note..."
- "Furthermore..."
- "Moreover..."
- "utilize" (when vague)
- "leverage" (when vague)
- Long passive constructions
- Academic transitions

## Sample Cases

### Case 1: Reject AI-like phrase
**Input:** "I would like to emphasize the importance of..."
**Expected:** Verdict: reject, score ≤ 2
**Better version:** "The key thing is..."
**Pass criteria:** Phrase identified as unnatural, better version provided

### Case 2: Accept natural phrase
**Input:** "Let's loop in engineering."
**Expected:** Verdict: accept, score = 5
**Pass criteria:** Phrase identified as natural spoken

### Case 3: Rewrite stiff phrase
**Input:** "Therefore, we should proceed with the implementation."
**Expected:** Verdict: rewrite, score = 3
**Better version:** "So let's start implementing."
**Pass criteria:** Phrase identified as borderline, better version provided

### Case 4: Accept confident but natural
**Input:** "I'm confident this approach will work."
**Expected:** Verdict: accept, score = 4 or 5
**Pass criteria:** Confident language recognized as natural

## Edge Cases

### Edge case 1: "utilize" vs "use"
**Input:** "We'll utilize the new API."
**Expected:** Score 2-3, suggest "use"
**Pass criteria:** Vague "utilize" flagged

### Edge case 2: Professional but natural
**Input:** "I'd recommend we take a closer look at this."
**Expected:** Score 4-5
**Pass criteria:** Professional language not penalized

### Edge case 3: Short but formal
**Input:** "Proceed with caution."
**Expected:** Score 2-3
**Pass criteria:** Short but unnatural phrasing flagged

## Fail Examples

### Example 1: Accepted formal phrase
**Input:** "It is imperative that we..."
**Verdict:** accept, score 4
**Why it fails:** Too formal for speech, should be rejected

### Example 2: Rejected natural phrase
**Input:** "Let's double down on this."
**Verdict:** reject, score 2
**Why it fails:** Natural phrase incorrectly flagged

### Example 3: Poor rewrite
**Input:** "Furthermore, we should..."
**Better version:** "And also we should..."
**Why it fails:** Rewrite is still unnatural

## Related Evals

- Phrase Extraction Quality — Filters extracted phrases
- Voice Drill Quality — Ensures drills use natural phrases

---

**Eval ID:** spoken-naturalness
**Category:** Quality
**Status:** Active
