# Weekly Review Template

## Week of: {{ week_start }} — {{ week_end }}

**Date:** {{ review_date }}
**Week Number:** {{ week_number }}

---

## Benchmark Results

### 1. Senior PM Interview Question
**Scenario:** {{ interview_scenario }}
**Target phrases:** {{ interview_phrases_count }}
**Result:** {{ interview_result }}
**Score:** {{ interview_score }}/100

**Used phrases:**
- {{ used_phrases }}

**Missed phrases:**
- {{ missed_phrases }}

**Feedback:** {{ interview_feedback }}

---

### 2. Roadmap Trade-off Meeting
**Scenario:** {{ roadmap_scenario }}
**Target phrases:** {{ roadmap_phrases_count }}
**Result:** {{ roadmap_result }}
**Score:** {{ roadmap_score }}/100

**Used phrases:**
- {{ used_phrases }}

**Missed phrases:**
- {{ missed_phrases }}

**Feedback:** {{ roadmap_feedback }}

---

### 3. Stakeholder Pushback
**Scenario:** {{ pushback_scenario }}
**Target phrases:** {{ pushback_phrases_count }}
**Result:** {{ pushback_result }}
**Score:** {{ pushback_score }}/100

**Used phrases:**
- {{ used_phrases }}

**Missed phrases:**
- {{ missed_phrases }}

**Feedback:** {{ pushback_feedback }}

---

### 4. AI/Evals Technical Discussion
**Scenario:** {{ ai_scenario }}
**Target phrases:** {{ ai_phrases_count }}
**Result:** {{ ai_result }}
**Score:** {{ ai_score }}/100

**Used phrases:**
- {{ used_phrases }}

**Missed phrases:**
- {{ missed_phrases }}

**Feedback:** {{ ai_feedback }}

---

## Overall Progress

### This Week vs Last Week

| Metric | Last Week | This Week | Change |
|--------|-----------|-----------|--------|
| Active phrases (75+) | {{ last_active }} | {{ this_active }} | {{ active_change }} |
| Weak phrases remaining | {{ last_weak }} | {{ this_weak }} | {{ weak_change }} |
| Regressed phrases | {{ last_regressed }} | {{ this_regressed }} | {{ regressed_change }} |
| Naturalness issues | {{ last_naturalness }} | {{ this_naturalness }} | {{ naturalness_change }} |
| **Readiness Score** | **{{ last_readiness }}** | **{{ this_readiness }}** | **{{ readiness_change }}** |

---

## Active Phrases Added This Week

{% for phrase in new_active_phrases %}
### {{ phrase.phrase }}
**Previous score:** {{ phrase.previous_score }}
**New score:** {{ phrase.new_score }}
**Status:** Active → Ready
**Context:** {{ phrase.context }}

{% endfor %}

---

## Weak Phrases Remaining

{% for phrase in weak_phrases %}
### {{ phrase.phrase }}
**Score:** {{ phrase.score }}
**Weakness type:** {{ phrase.weakness_type }}
**Times missed:** {{ phrase.times_missed }}
**Recommendation:** {{ phrase.recommendation }}

{% endfor %}

---

## Regressed Phrases

{% for phrase in regressed_phrases %}
### {{ phrase.phrase }}
**Previous score:** {{ phrase.previous_score }}
**Current score:** {{ phrase.current_score }}
**Change:** {{ phrase.change }}
**Possible cause:** {{ phrase.cause }}

{% endfor %}

---

## Naturalness Issues

{% for phrase in naturalness_issues %}
### {{ phrase.phrase }}
**Issue:** {{ phrase.issue }}
**Better version:** "{{ phrase.better_version }}"
**Practice recommendation:** {{ phrase.recommendation }}

{% endfor %}

---

## Next Week's Plan

### Focus Areas
1. {{ focus_area_1 }}
2. {{ focus_area_2 }}
3. {{ focus_area_3 }}

### Recommended Drills
- {{ drill_1 }}
- {{ drill_2 }}
- {{ drill_3 }}

### Phrases to Replay
{% for phrase in replay_phrases %}
- {{ phrase.phrase }} ({{ phrase.reason }})
{% endfor %}

---

## Weekly Reflection

**What worked well this week:**


**What didn't work:**


**What I noticed about my speaking:**


**What I want to focus on next week:**


---

## Week Status

**Status:** {{ status }}
**Readiness:** {{ readiness_status }}
**Next milestone:** {{ next_milestone }}

---

**Reviewed by:** {{ user }}
**Week ID:** {{ week_id }}
