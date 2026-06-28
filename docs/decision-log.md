# Decision Log

## Overview

This document records significant architectural and product decisions for SpeakOps.

## Format

Each decision includes:
- Date
- Decision
- Rationale
- Trade-offs
- Status

---

## 2025-06-28: Repository Structure

**Decision:** Create full SpeakOps repository structure with agentic development OS

**Rationale:**
- Need systematic approach to development
- Quality gates required at every step
- Eval-driven development prevents feature creep
- Agent roles provide clear responsibilities

**Trade-offs:**
- More upfront structure
- Slower initial development
- Higher long-term quality

**Status:** ✓ Implemented

---

## 2025-06-28: Local-First Architecture

**Decision:** SpeakOps is local-first, no web app or mobile app

**Rationale:**
- Privacy — user data stays on device
- Simplicity — no backend required
- Control — user owns all data
- Security — no external dependencies

**Trade-offs:**
- No cloud sync
- No multi-device access
- User responsible for backups

**Status:** ✓ Implemented

---

## 2025-06-28: ChatGPT Voice as Runtime

**Decision:** Use ChatGPT Voice as practice runtime, not custom voice system

**Rationale:**
- ChatGPT Voice already exists and works well
- No need to build voice infrastructure
- User can use existing ChatGPT subscription
- Focus on content, not infrastructure

**Trade-offs:**
- Dependent on OpenAI product
- No direct transcript access
- Limited control over voice experience

**Status:** ✓ Implemented

---

## 2025-06-28: Manual Source Ingestion (MVP)

**Decision:** Manual paste/export for Google Docs and YouTube (MVP)

**Rationale:**
- No API keys required
- Simpler security model
- User control over content
- No dependency on external APIs

**Trade-offs:**
- More manual work for user
- No automatic syncing
- Can't process large sources easily

**Future consideration:** API integration if user demand

**Status:** ✓ Implemented

---

## 2025-06-28: Activation Score Model

**Decision:** 100-point activation score with 7 dimensions

**Rationale:**
- Comprehensive but explainable
- Clear progression (passive → meeting-ready)
- Motivational (visible progress)
- Actionable (know what to improve)

**Trade-offs:**
- More complex than binary (active/inactive)
- Requires tracking multiple dimensions
- May be overwhelming for new users

**Dimensions:**
- Meaning understood: 10
- Used without hint: 20
- Correct usage: 20
- Natural spoken usage: 20
- Context transfer: 15
- Retrieval speed: 10
- Retention after 7+ days: 5

**Status:** ✓ Implemented

---

## 2025-06-28: Spoken Naturalness Focus

**Decision:** Prioritize spoken naturalness over formal correctness

**Rationale:**
- Goal is active spoken English
- Formal English is already taught
- Meeting/interview success requires naturalness
- AI-like language is counterproductive

**Trade-offs:**
- May reject grammatically correct but formal phrases
- Subjective assessment of naturalness
- Cultural differences in spoken English

**Red flags:**
- "I would like to emphasize..."
- "It is crucial to note..."
- "Furthermore..."
- "Moreover..."

**Prefer:**
- Short spoken phrases
- Direct but polite wording
- Natural rhythm
- Realistic meeting language

**Status:** ✓ Implemented

---

## 2025-06-28: Evals for Every Behavior

**Decision:** Every AI behavior must have eval coverage

**Rationale:**
- Prevents quality drift
- Ensures changes don't break functionality
- Provides objective quality measures
- Enables regression testing

**Trade-offs:**
- More upfront work
- Slower development
- Need to maintain eval suite

**Required evals:**
- Phrase extraction quality
- Spoken naturalness
- Voice drill quality
- Activation scoring consistency
- Privacy/security
- Weekly regression

**Status:** ✓ Implemented

---

## 2025-06-28: Ponytail Mode (Lazy Development)

**Decision:** Apply lazy development principles — minimal code, maximum value

**Rationale:**
- Prevents overengineering
- Faster development
- Easier to maintain
- Forces focus on essentials

**Trade-offs:**
- May need to rewrite later
- Some inefficiencies
- Not "production" polished

**The ladder:**
1. Does this need to exist?
2. Stdlib does it?
3. Native platform feature?
4. Already-installed dependency?
5. Can it be one line?
6. Only then: minimal code

**Status:** ✓ Implemented

---

## 2025-06-28: Security by Default

**Decision:** Privacy and security considered from the start, not added later

**Rationale:**
- Hard to add security later
- User trust is essential
- Language learning involves personal data
- Local-first requires security discipline

**Trade-offs:**
- More constraints on development
- May reject convenient features
- Slower initial implementation

**Security rules:**
- No secrets in repo
- No API keys
- Local-only data
- Sanitized inputs
- Restricted file access
- No external calls by default

**Status:** ✓ Implemented

---

## 2025-06-28: Decision Log Required

**Decision:** Every meaningful change must be documented in decision log

**Rationale:**
- Prevents forgetting why decisions were made
- Enables review and revision
- Helps onboarding
- Documents trade-offs

**Trade-offs:**
- More documentation burden
- Slower development
- May feel bureaucratic

**When to log:**
- Architecture changes
- Feature additions
- Significant refactors
- Security/privacy decisions
- Rejected alternatives

**Status:** ✓ Implemented

---

## 2025-06-28: Voice Hooks (Markdown Alerts)

**Decision:** Implement voice hooks as markdown alerts (MVP), not real notifications

**Rationale:**
- Simpler implementation
- No external dependencies
- User can check manually
- Can upgrade to real notifications later

**Trade-offs:**
- No push notifications
- User must check manually
- May miss time-sensitive alerts

**Future consideration:** Real notifications if user demand

**Status:** ✓ Implemented

---

## Future Decisions

These decisions will be made as needed:

- [ ] API integration for Google Docs/YouTube
- [ ] Real-time transcript capture
- [ ] Cloud sync option
- [ ] Mobile app consideration
- [ ] Multi-language support
- [ ] Collaboration features

---

**Log Version:** 1.0
**Last Updated:** 2025-06-28
