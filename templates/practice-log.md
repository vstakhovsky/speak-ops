# Practice Log Template

## Session: {{ session_number }}

**Date:** {{ date }}
**Drill:** {{ drill_title }}
**Duration:** {{ duration }} minutes
**Mode:** {{ mode }}

---

## Target Phrases

{% for phrase in target_phrases %}
### {{ phrase.phrase }}
**Status before:** {{ phrase.previous_status }}
**Used:** {{ phrase.used ? 'Yes' : 'No' }}
**Correct:** {{ phrase.correct ? 'Yes' : 'No' }}
**Natural:** {{ phrase.natural ? 'Yes' : 'No' }}
**Notes:** {{ phrase.notes }}

{% endfor %}

---

## Session Summary

**Phrases used:** {{ used_count }}/{{ total_count }}
**Phrases correct:** {{ correct_count }}/{{ used_count }}
**Phrases natural:** {{ natural_count }}/{{ used_count }}

### Missed Phrases
{% for phrase in missed_phrases %}
- {{ phrase }}
{% endfor %}

### Incorrect Usage
{% for phrase in incorrect_phrases %}
- {{ phrase }}: {{ notes }}
{% endfor %}

### Too Formal Usage
{% for phrase in formal_phrases %}
- {{ phrase }} → better: "{{ better_version }}"
{% endfor %}

---

## AI Feedback

{{ ai_feedback }}

---

## Self-Reflection

**What felt natural:**


**What felt forced:**


**What I hesitated on:**


**What I want to improve:**


---

## Score Updates

| Phrase | Previous | New | Change |
|-------|----------|-----|--------|
{% for score in score_updates %}
| {{ score.phrase }} | {{ score.previous }} | {{ score.new }} | {{ score.change }} |
{% endfor %}

---

## Next Session

**Weak phrases to replay:**
{% for phrase in weak_phrases %}
- {{ phrase }}
{% endfor %}

**Recommended next drill:** {{ next_drill }}

**Practice focus:** {{ practice_focus }}

---

**Logged by:** {{ user }}
**Session ID:** {{ session_id }}
