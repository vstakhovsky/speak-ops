# Voice Drill Quality Rubric

## Eval Goal

Assess whether generated voice drills force target phrase usage naturally in realistic scenarios.

## Scoring Rubric

| Score | Level | Criteria |
|-------|-------|----------|
| 1 | Failed | Drill doesn't create opportunities for phrases |
| 2 | Poor | Forced, unnatural phrase opportunities |
| 3 | Acceptable | Some natural opportunities, some forced |
| 4 | Good | Natural opportunities for most phrases |
| 5 | Excellent | All phrases have natural, realistic usage moments |

**Pass threshold:** 4

## Dimensions

### 1. Phrase Integration (35 points)
- All 5–8 target phrases covered: 15 points
- Natural opportunities created: 15 points
- Not forced or awkward: 5 points

### 2. Scenario Realism (25 points)
- Realistic IT/Product/AI situation: 15 points
- Appropriate difficulty: 10 points

### 3. Instruction Quality (20 points)
- Clear instructions for ChatGPT Voice: 10 points
- Appropriate turn length: 5 points
- Good correction guidance: 5 points

### 4. Flow (10 points)
- Natural conversation flow: 5 points
- Appropriate duration: 5 points

### 5. Feedback Quality (10 points)
- Phrase-level feedback specified: 5 points
- Actionable next steps: 5 points

## Sample Cases

### Case 1: Interview drill
**Input:** 8 interview phrases, scenario: stakeholder conflict
**Expected output:** Prompt creates natural situations for all phrases
**Pass criteria:** All phrases fit naturally into interview flow

### Case 2: Meeting drill
**Input:** 6 meeting phrases, scenario: roadmap review
**Expected output:** Prompt creates realistic meeting discussion
**Pass criteria:** Phrases fit naturally into meeting context

### Case 3: Pushback drill
**Input:** 5 pushback phrases, scenario: VP questioning timeline
**Expected output:** AI naturally creates pushback opportunities
**Pass criteria:** User can use phrases in response to pressure

### Case 4: Technical drill
**Input:** 7 technical phrases, scenario: design discussion
**Expected output:** Technical discussion creates phrase opportunities
**Pass criteria:** Technical terms and phrases used naturally

## Edge Cases

### Edge case 1: Too many phrases
**Input:** 10 phrases
**Expected:** Flag as too many, reduce to 5–8
**Pass criteria:** Overloaded drill identified

### Edge case 2: Too few phrases
**Input:** 3 phrases
**Expected:** Flag as too few, suggest more
**Pass criteria:** Under-loaded drill identified

### Edge case 3: Mismatched phrases
**Input:** Technical phrases in social scenario
**Expected:** Flag as mismatched, suggest better scenario
**Pass criteria:** Phrase-scenario mismatch detected

## Fail Examples

### Example 1: Forced phrase usage
**Drill:** AI randomly asks "Say 'push back on' now"
**Why it fails:** Completely unnatural, breaks conversation flow

### Example 2: Unrealistic scenario
**Drill:** "You're meeting with aliens about roadmap"
**Why it fails:** Not realistic, doesn't prepare user for real situations

### Example 3: No phrase opportunities
**Drill:** Scenario created but phrases never come up naturally
**Why it fails:** Drill doesn't achieve its primary goal

### Example 4: AI monologues
**Drill:** AI gives long speeches, no user input
**Why it fails:** Violates "short turns" requirement

## Quality Checklist

Before a drill is marked as ready:

- [ ] Has 5–8 target phrases
- [ ] All phrases have natural usage opportunities
- [ ] Scenario is realistic for IT/Product/AI
- [ ] AI turns are short (2–3 sentences)
- [ ] Instructions are clear for ChatGPT Voice
- [ ] Feedback mechanism specified
- [ ] Duration specified (typically 5 minutes)
- [ ] Appropriate for user level

## Related Evals

- Spoken Naturalness — Uses natural phrases
- Scenario Realism — Ensures realistic scenarios

---

**Eval ID:** voice-drill-quality
**Category:** Quality
**Status:** Active
