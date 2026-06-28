# Voice Hooks — Alert System

## Overview

Voice hooks provide notifications for SpeakOps when user attention is needed.

**Principle:** "Do not make the user watch long agent runs. Notify the user when speaking practice or human intervention matters."

## Alert Triggers

Voice hooks trigger notifications for:

| Trigger | Description | Priority |
|---------|-------------|----------|
| Phrases extracted and ready | New phrases ready for review | Medium |
| Daily drill due | Time for daily practice | High |
| Weekly eval due | Time for weekly benchmark | High |
| Weak phrase replay due | Weak phrases need practice | High |
| Claude Code needs decision | User input required | Critical |
| Source processing failed | Ingestion error | Medium |
| Phrase pack ready | New phrases compiled | Low |

## Alert Types

### 1. Phrases Extracted and Ready

**When:** After phrase extraction completes

**Alert:**
```
🔔 SpeakOps: Phrases Ready

New phrases extracted and ready for review.

Source: [source name]
Phrases: [count]
Domain: [domain]

Next step: Review phrases and build cards.

Run: /build-phrase-cards --target obsidian
```

### 2. Daily Drill Due

**When:** 24+ hours since last practice session

**Alert:**
```
⏰ SpeakOps: Daily Practice Due

Time for your daily voice drill!

Last practice: [X] days ago
Weak phrases: [count]
Recommended drill: [drill name]

Run: /build-voice-drill --mode [mode] --session [n]
```

### 3. Weekly Eval Due

**When:** 7+ days since last weekly eval

**Alert:**
```
📊 SpeakOps: Weekly Eval Due

Time for your weekly benchmark evaluation.

Week: [week number]
Previous readiness: [score]%

This week's benchmarks:
1. Senior PM interview question
2. Roadmap trade-off meeting
3. Stakeholder pushback
4. AI/evals technical discussion

Run: /weekly-eval
```

### 4. Weak Phrase Replay Due

**When:** 5+ weak phrases accumulated

**Alert:**
```
🔄 SpeakOps: Weak Phrase Replay

You have [count] weak phrases that need practice.

Weak phrases:
- [phrase 1]
- [phrase 2]
- [phrase 3]

Run: /replay-weak --count 5
```

### 5. Claude Code Needs Decision

**When:** Agent requires user input

**Alert:**
```
❓ SpeakOps: Input Required

Agent needs your decision.

Topic: [topic]
Options: [option 1, option 2]
Context: [brief context]

Please provide input to continue.
```

### 6. Source Processing Failed

**When:** Ingestion fails

**Alert:**
```
⚠️ SpeakOps: Processing Failed

Source processing encountered an error.

Source: [source type]
Error: [error message]

Please check the source and try again.
```

### 7. Phrase Pack Ready

**When:** New phrase pack compiled

**Alert:**
```
✨ SpeakOps: Phrase Pack Ready

New phrase pack is ready!

Pack: [pack name]
Phrases: [count]
Domain: [domain]

Ready for voice drill practice.
```

## Implementation

### For MVP

MVP implementation uses **markdown alerts**:

- Alerts written to `voice-hooks/alerts.md`
- File timestamp used for "unread" status
- Claude Code reads alerts on startup

### Future Implementation

**Webhook support (optional):**

```yaml
webhook:
  url: https://your-webhook-endpoint.com/alerts
  events:
    - phrases_ready
    - daily_drill_due
    - weekly_eval_due
    - weak_phrase_replay
    - claude_needs_decision
    - processing_failed
    - phrase_pack_ready
```

**Notification channels (optional):**
- Desktop notifications
- Email alerts
- Slack/webhook
- Push notifications

### Alert Format

**Markdown alert format:**
```markdown
## [Timestamp] [Priority] [Title]

[Message body]

**Actions:**
- [Action 1]
- [Action 2]

**Metadata:**
- Source: [source]
- Count: [number]
- Related: [files/commands]
```

## Alert States

| State | Description |
|-------|-------------|
| pending | Alert created, not yet seen |
| delivered | Alert shown to user |
| acknowledged | User acknowledged alert |
| dismissed | User dismissed alert |
| actioned | User took action |

## Alert Storage

**Location:** `voice-hooks/alerts.jsonl`

**Format:**
```json
{
  "timestamp": "2025-06-28T10:00:00Z",
  "trigger": "daily_drill_due",
  "priority": "high",
  "title": "Daily Practice Due",
  "message": "...",
  "state": "pending",
  "actions": ["build-voice-drill"],
  "metadata": {
    "days_since_practice": 2,
    "weak_phrases": 5
  }
}
```

## Privacy

Alerts contain:
- Timestamps
- Trigger types
- Counts and metadata
- Action suggestions

Alerts do NOT contain:
- Full phrase content
- Transcript content
- Source content
- Personal information

## Commands

### View alerts
```bash
/voice-alerts
```

### Acknowledge alert
```bash
/voice-alert --acknowledge <alert-id>
```

### Dismiss alert
```bash
/voice-alert --dismiss <alert-id>
```

### Configure alerts
```bash
/voice-alert --configure
```

## Configuration

**Alert preferences:**
```yaml
alerts:
  enabled: true
  daily_drill_reminder: true
  weekly_eval_reminder: true
  weak_phrase_threshold: 5
  quiet_hours:
    start: "22:00"
    end: "08:00"
```

## Examples

### Example 1: Daily reminder
```
🔔 SpeakOps Alert (2025-06-28 09:00)

Daily drill due! Last practice was 2 days ago.

Run: /build-voice-drill --mode interview --session 5
```

### Example 2: Weekly eval
```
📊 SpeakOps Alert (2025-06-28 10:00)

Weekly eval due! Week 24.

Run: /weekly-eval
```

### Example 3: Weak phrases
```
🔄 SpeakOps Alert (2025-06-28 14:00)

5 weak phrases need replay.

Run: /replay-weak --count 5
```

---

**Status:** MVP (markdown alerts)
**Future:** Webhook support, notification channels
