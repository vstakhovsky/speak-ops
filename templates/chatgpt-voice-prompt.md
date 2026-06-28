# ChatGPT Voice Prompt Template

## Drill: {{ title }}

**Mode:** {{ mode }}
**Scenario:** {{ scenario }}
**Target Phrases:** {{ count }} phrases
**Duration:** {{ duration }} minutes

---

## Instructions for ChatGPT Voice

**Your Role:** {{ ai_role }}

**My Role:** {{ user_role }}

**Scenario:** {{ scenario_description }}

**Target phrases I need to use:**
{% for phrase in phrases %}
- {{ phrase }}
{% endfor %}

**Conversation Rules:**
1. Keep your turns short (2–3 sentences max)
2. Create natural situations where I would use the target phrases
3. If I don't use a target phrase within 1–2 minutes, gently steer the conversation that way
4. Correct ONLY major mistakes (grammar, clearly wrong usage)
5. If I make a major mistake:
   - Stop me gently
   - Give me a better spoken version
   - Ask me to repeat the better version aloud
6. Don't correct minor differences in phrasing
7. After {{ duration }} minutes, end with:
   - Which phrases I used well
   - Which phrases I missed or used incorrectly
   - Specific feedback on naturalness

**Start the conversation now.**

---

## Practice Log Template

**Date:** {{ date }}
**Drill:** {{ title }}
**Target Phrases:** {{ phrases_count }}

### Phrase Usage

| Phrase | Used? | Correct? | Natural? | Notes |
|--------|-------|----------|----------|-------|
{% for phrase in phrases %}
| {{ phrase }} | [Yes/No] | [Yes/No] | [Yes/No] | [Notes] |
{% endfor %}

### Overall Feedback

**What went well:**


**What needs work:**


**AI Feedback:**


### Action Items

- Weak phrases to replay: {{ weak_phrases }}
- Next drill: {{ next_drill }}

---

## Scoring Rubric

**Phrase Usage Score:**
- Used correctly and naturally: +40
- Used correctly but formally: +30
- Used with minor errors: +20
- Used with major errors: +10
- Not used: 0

**Overall Session Score:**
- 90–100: Excellent
- 75–89: Good
- 60–74: Needs work
- <60: Needs significant practice
