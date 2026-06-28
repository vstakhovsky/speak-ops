# Voice Alert Specification

## Purpose

This spec defines the voice alert system for SpeakOps.

## Goals

1. Notify users when practice is due
2. Alert users to review new phrases
3. Prompt users to run weekly evals
4. Flag weak phrases for replay
5. Request user decisions when needed
6. Report processing failures

## Non-Goals

1. Real-time push notifications (MVP)
2. SMS/email alerts (MVP)
3. Calendar integration (MVP)
4. Mobile app notifications (MVP)

## Alert Types

### Type 1: Practice Reminder

**Name:** `daily_drill_due`

**Trigger:** 24+ hours since last practice session

**Priority:** High

**Template:**
```
⏰ SpeakOps: Daily Practice Due

Time for your daily voice drill!

Last practice: {days_ago} days ago
Weak phrases: {weak_count}
Recommended drill: {drill_name}

Run: /build-voice-drill --mode {mode} --session {session_number}
```

**Metadata:**
- `days_ago`: Number of days since last practice
- `weak_count`: Number of weak phrases
- `drill_name`: Recommended drill
- `mode`: Suggested practice mode
- `session_number`: Next session number

### Type 2: Weekly Eval Reminder

**Name:** `weekly_eval_due`

**Trigger:** 7+ days since last weekly eval

**Priority:** High

**Template:**
```
📊 SpeakOps: Weekly Eval Due

Time for your weekly benchmark evaluation.

Week: {week_number}
Previous readiness: {readiness_score}%

This week's benchmarks:
1. Senior PM interview question
2. Roadmap trade-off meeting
3. Stakeholder pushback
4. AI/evals technical discussion

Run: /weekly-eval
```

**Metadata:**
- `week_number`: Current week number
- `readiness_score`: Previous readiness score
- `benchmarks`: List of benchmark scenarios

### Type 3: Weak Phrase Alert

**Name:** `weak_phrase_replay_due`

**Trigger:** 5+ weak phrases accumulated

**Priority:** High

**Template:**
```
🔄 SpeakOps: Weak Phrase Replay

You have {weak_count} weak phrases that need practice.

Weak phrases:
{weak_phrases_list}

Run: /replay-weak --count {count}
```

**Metadata:**
- `weak_count`: Number of weak phrases
- `weak_phrases_list`: List of weak phrases
- `count`: Number to replay

### Type 4: Phrases Ready

**Name:** `phrases_ready`

**Trigger:** Phrase extraction completes

**Priority:** Medium

**Template:**
```
✨ SpeakOps: Phrases Ready

New phrases extracted and ready for review.

Source: {source_name}
Phrases: {phrase_count}
Domain: {domain}

Next step: Review phrases and build cards.

Run: /build-phrase-cards --target {target}
```

**Metadata:**
- `source_name`: Name of source
- `phrase_count`: Number of phrases extracted
- `domain`: Domain of phrases
- `target`: Suggested target (obsidian, anki, markdown)

### Type 5: Processing Failed

**Name:** `processing_failed`

**Trigger:** Ingestion or processing fails

**Priority:** Medium

**Template:**
```
⚠️ SpeakOps: Processing Failed

Source processing encountered an error.

Source: {source_type}
Error: {error_message}

Please check the source and try again.
```

**Metadata:**
- `source_type`: Type of source (obsidian, gdoc, youtube)
- `error_message`: Error details

### Type 6: User Decision Needed

**Name:** `user_decision_needed`

**Trigger:** Agent requires user input

**Priority:** Critical

**Template:**
```
❓ SpeakOps: Input Required

Agent needs your decision.

Topic: {topic}
Options: {options}
Context: {context}

Please provide input to continue.
```

**Metadata:**
- `topic`: What needs decision
- `options`: Available options
- `context`: Brief context
- `agent`: Which agent needs input

## Alert Storage

**File:** `voice-hooks/alerts.jsonl`

**Format:**
```json
{
  "id": "alert_20250628_100000",
  "timestamp": "2025-06-28T10:00:00Z",
  "trigger": "daily_drill_due",
  "priority": "high",
  "title": "Daily Practice Due",
  "message": "Time for your daily voice drill!",
  "state": "pending",
  "actions": ["build-voice-drill"],
  "metadata": {
    "days_ago": 2,
    "weak_count": 5,
    "drill_name": "stakeholder-pushback",
    "mode": "meeting",
    "session_number": 6
  }
}
```

## Alert States

- `pending`: Alert created, not yet seen
- `delivered`: Alert shown to user
- `acknowledged`: User acknowledged alert
- `dismissed`: User dismissed alert
- `actioned`: User took action

## Alert Lifecycle

```
Trigger → Create Alert → Store in alerts.jsonl
         ↓
         Show to User (mark as delivered)
         ↓
         User Action (acknowledge/dismiss/action)
         ↓
         Update State
```

## Privacy

Alerts contain only:
- Timestamps
- Trigger types
- Counts and metadata
- Action suggestions

Alerts do NOT contain:
- Full phrase content
- Transcript content
- Source content
- Personal information

## Security

- Alerts are local-only
- No external transmission (MVP)
- User controls alert data
- Alerts can be deleted

## Implementation Priority

### MVP (Current)
- [x] Markdown alert format
- [x] JSONL storage
- [x] Basic trigger logic
- [ ] Alert viewing command
- [ ] Alert state management

### Future
- [ ] Webhook support
- [ ] Desktop notifications
- [ ] Quiet hours
- [ ] Alert configuration
- [ ] Alert history

## Testing

**Test Case 1: Daily drill trigger**
- Set last practice to 2 days ago
- Trigger alert
- Verify alert created with correct metadata

**Test Case 2: Weekly eval trigger**
- Set last eval to 8 days ago
- Trigger alert
- Verify alert created with week number

**Test Case 3: Weak phrase trigger**
- Create 6 weak phrases
- Trigger alert
- Verify alert lists weak phrases

**Test Case 4: Alert states**
- Create alert
- Mark as delivered
- Acknowledge alert
- Verify state updates

---

**Spec Version:** 1.0
**Status:** Active
