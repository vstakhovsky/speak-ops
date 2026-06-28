# SpeakOps — TODO List

## Immediate Priorities (Next Steps)

### 1. Core Skill Implementation
- [ ] Implement phrase-extractor skill with actual extraction logic
- [ ] Implement spoken-naturalness-gate with naturalness scoring
- [ ] Implement voice-drill-builder with prompt generation
- [ ] Implement activation-scorer with score calculation
- [ ] Test all skills with sample data

### 2. Evals Implementation
- [ ] Create golden datasets for each eval type
- [ ] Implement automated eval runners
- [ ] Add regression test suite
- [ ] Set up continuous eval running

### 3. Script Enhancement
- [ ] Add error handling to all scripts
- [ ] Add command-line argument parsing
- [ ] Add progress indicators for long operations
- [ ] Add configuration file support

### 4. Data Files
- [ ] Create sample phrases.csv with example data
- [ ] Create sample sessions.jsonl with example sessions
- [ ] Add data validation schemas
- [ ] Add data migration scripts

### 5. Documentation
- [ ] Add getting started guide
- [ ] Add troubleshooting guide
- [ ] Add FAQ
- [ ] Add architecture diagrams

## Short-Term Goals (1-2 Weeks)

### 1. Workflow Testing
- [ ] Test Obsidian → voice drill workflow end-to-end
- [ ] Test Google Docs → voice drill workflow end-to-end
- [ ] Test YouTube → AI/evals phrase pack workflow end-to-end
- [ ] Test transcript → scoring workflow end-to-end
- [ ] Test weekly eval workflow end-to-end

### 2. Quality Improvements
- [ ] Add more eval cases (edge cases, failures)
- [ ] Improve spoken naturalness detection
- [ ] Enhance voice drill prompt quality
- [ ] Refine activation scoring model

### 3. User Experience
- [ ] Add progress indicators
- [ ] Improve error messages
- [ ] Add command help text
- [ ] Add examples for all commands

### 4. Security Hardening
- [ ] Add more input sanitization tests
- [ ] Add file access tests
- [ ] Add prompt injection tests
- [ ] Security audit

## Medium-Term Goals (1 Month)

### 1. Feature Expansion
- [ ] Implement weak-phrase-replayer skill
- [ ] Implement interview-activator skill
- [ ] Implement meeting-simulator skill
- [ ] Implement weekly-eval skill
- [ ] Implement source-ingestor skill
- [ ] Implement phrase-card-generator skill

### 2. Integration Improvements
- [ ] Consider Google Docs API integration
- [ ] Consider YouTube API integration
- [ ] Consider NotebookLM integration
- [ ] Consider automatic transcript capture

### 3. Voice Hooks Enhancement
- [ ] Implement markdown alert system
- [ ] Add alert viewing command
- [ ] Add alert state management
- [ ] Consider webhook support

### 4. Analytics
- [ ] Add progress tracking dashboard
- [ ] Add phrase usage statistics
- [ ] Add learning analytics
- [ ] Add practice streak tracking

## Long-Term Goals (3+ Months)

### 1. Platform Expansion
- [ ] Consider mobile app
- [ ] Consider web interface
- [ ] Consider cloud sync option
- [ ] Consider collaboration features

### 2. AI Enhancement
- [ ] Better natural language processing
- [ ] Improved context detection
- [ ] Personalized recommendations
- [ ] Adaptive difficulty

### 3. Content Expansion
- [ ] More domain coverage
- [ ] More scenario types
- [ ] More difficulty levels
- [ ] More language support

### 4. Community
- [ ] Share phrase packs
- [ ] Share voice drills
- [ ] Community evals
- [ ] Best practices library

## Technical Debt

### 1. Code Quality
- [ ] Add type hints to Python scripts
- [ ] Add docstrings to all functions
- [ ] Add unit tests for scripts
- [ ] Refactor for better modularity

### 2. Documentation
- [ ] Add API documentation
- [ ] Add contribution guide
- [ ] Add architecture documentation
- [ ] Add performance guidelines

### 3. Infrastructure
- [ ] Set up CI/CD
- [ ] Add automated testing
- [ ] Add automated security scanning
- [ ] Add performance monitoring

## Research & Exploration

### 1. Technical Exploration
- [ ] Explore real-time transcript capture options
- [ ] Explore voice-to-text accuracy
- [ ] Explore LLM integration options
- [ ] Explore alternative voice platforms

### 2. User Research
- [ ] User interview needs assessment
- [ ] User testing of workflows
- [ ] User feedback collection
- [ ] Usage pattern analysis

### 3. Market Research
- [ ] Competitive analysis
- [ ] Feature gap analysis
- [ ] Pricing strategy (if applicable)
- [ ] Market positioning

## Dependencies

### 1. External Dependencies
- [ ] Monitor Claude Code updates
- [ ] Monitor ChatGPT Voice changes
- [ ] Monitor NotebookLM updates
- [ ] Monitor AI model changes

### 2. Internal Dependencies
- [ ] Complete core skills before advanced features
- [ ] Complete evals before automation
- [ ] Complete security before external integrations
- [ ] Complete workflows before UX improvements

## Risks & Mitigations

### 1. Technical Risks
- [ ] Risk: ChatGPT Voice changes break integration
  - Mitigation: Monitor for changes, have fallbacks
- [ ] Risk: LLM quality degrades
  - Mitigation: Evals catch degradation
- [ ] Risk: Performance issues at scale
  - Mitigation: Ponytail shortcuts, optimization plan

### 2. User Risks
- [ ] Risk: Users don't practice consistently
  - Mitigation: Voice hooks, reminders
- [ ] Risk: Users find scoring confusing
  - Mitigation: Better documentation, examples
- [ ] Risk: Users don't see progress
  - Mitigation: Better visualization, feedback

### 3. Security Risks
- [ ] Risk: Prompt injection attacks
  - Mitigation: Input sanitization, eval coverage
- [ ] Risk: Data loss
  - Mitigation: Backup recommendations, local-first
- [ ] Risk: Privacy violations
  - Mitigation: Security review, privacy by design

---

**TODO Version:** 1.0
**Last Updated:** 2025-06-28
**Total Items:** 80+
**Completed:** 0
**In Progress:** 0
**Pending:** 80+
