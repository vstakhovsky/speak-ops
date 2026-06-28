# Phrase Extraction Conventions

**Purpose:** Define how to extract and select useful Business English phrases.

## What is a Useful Phrase?

A useful phrase is:

1. **Practical** — Used in real meetings/interviews
2. **Spoken** — Natural in conversation, not written
3. **Context-specific** — IT/Product/AI workplace
4. **Transferable** — Usable across scenarios
5. **Actionable** — Can be practiced and improved

## Phrase Characteristics

### Good Phrase ✅

**Example:** "push back on"

- **Length:** 3 words (2–6 ideal)
- **Context:** Stakeholder discussions
- **Spoken:** Natural in meetings
- **Actionable:** Can practice in drills
- **Transferable:** Interview, meeting, email

### Bad Phrase ❌

**Example:** "I would like to emphasize"

- **Too formal:** Written style
- **Too long:** 5 words, but formal
- **Not actionable:** AI-like
- **Not transferable:** Limited use

## Extraction Criteria

### Priority Phrases (Extract First)

**Stakeholder Management:**
- push back on
- loop in
- align on
- table this
- find middle ground

**Prioritization:**
- prioritize / deprioritize
- trade-off
- shelve / defer
- revisit
- double down

**Technical Discussion:**
- under the hood
- at scale
- bottleneck
- latency / throughput
- baseline

### Reject Phrases (Don't Extract)

**Too Academic:**
- "leverage" (when vague)
- "utilize" (when "use" works)
- "optimize" (overused, vague)

**Too Generic:**
- "touch base"
- "circle back"
- "move the needle"

**Too Formal:**
- "furthermore"
- "moreover"
- "it is crucial to note"

**Too AI-like:**
- "I would like to emphasize"
- "It is important to note that"
- "Additionally, we should"

## Domain Filtering

### AI/Evals Domain

**Include:**
- baseline
- benchmark
- at scale
- latency / accuracy
- production-grade
- robust
- evaluation metrics

**Exclude:**
- Generic business terms
- Non-technical phrases
- Academic phrases

### Senior PM Domain

**Include:**
- stakeholder management
- roadmap prioritization
- trade-off discussions
- strategic alignment
- executive communication

**Exclude:**
- Technical implementation details
- Junior-level phrases
- Non-PH context

### Technical PM Domain

**Include:**
- technical trade-offs
- engineering collaboration
- design discussion
- architecture decisions
- feasibility analysis

**Exclude:**
- Pure technical terms (unless contextual)
- Non-PH context
- Overly technical jargon

## Level Filtering

### B1-B2 Level (Intermediate)

**Characteristics:**
- Common workplace vocabulary
- Simple grammatical structures
- Clear, direct expressions

**Examples:**
- "set up a meeting"
- "follow up on"
- "move forward with"

### B2-C1 Level (Upper-Intermediate)

**Characteristics:**
- Professional vocabulary
- Complex structures (but natural)
- Industry-appropriate

**Examples:**
- "push back on"
- "loop in engineering"
- "find middle ground"

### C1-C2 Level (Advanced)

**Characteristics:**
- Sophisticated vocabulary
- Complex ideas simply expressed
- Senior-level discourse

**Examples:**
- "at scale" (technical nuance)
- "production-grade" (quality context)
- "baseline" (reference point)

## Metadata Requirements

### Required Fields

Every extracted phrase must have:

1. **Phrase** — The actual phrase (2–6 words)
2. **Russian meaning** — Translation
3. **Context** — Where to use it
4. **Spoken example** — Natural usage
5. **Too-formal version** — What to avoid
6. **Activation priority** — high/medium/low

### Example

```json
{
  "phrase": "push back on",
  "russian": "возразить против",
  "context": "Use when disagreeing with stakeholder requests",
  "spoken_example": "I'd push back on that timeline.",
  "too_formal_version": "I would respectfully disagree with said timeline.",
  "activation_priority": "high"
}
```

## Quantity Guidelines

### Per Source

**Optimal:** 50–100 phrases
- Enough for variety
- Not overwhelming
- Quality over quantity

### Per Domain

**Optimal:** 30–50 phrases
- Cover key scenarios
- Manageable for practice
- Focused learning

### Per Session

**Optimal:** 5–8 phrases
- Focused practice
- Not overwhelming
- Deep learning

## Quality Checks

### Before Accepting a Phrase

Ask yourself:

1. ✅ **Is it spoken?** Would someone say this in a meeting?
2. ✅ **Is it useful?** Will this help in interviews/meetings?
3. ✅ **Is it natural?** Does it sound like a real person?
4. ✅ **Is it appropriate?** IT/Product/AI context?
5. ✅ **Is it actionable?** Can it be practiced?

If any answer is "no," reject or improve the phrase.

## Common Mistakes

### Mistake 1: Over-Extraction

❌ **Bad:** Extracting every 2–3 word combination
✅ **Good:** Extracting only useful, meaningful phrases

### Mistake 2: Ignoring Context

❌ **Bad:** Extracting phrases without context
✅ **Good:** Considering where and how phrases are used

### Mistake 3: Wrong Level

❌ **Bad:** Extracting C2 phrases for B2 learner
✅ **Good:** Matching phrases to target level

### Mistake 4: No Naturalness Check

❌ **Bad:** Accepting formal phrases
✅ **Good:** Filtering for natural spoken English

## Extraction Workflow

1. **Read source** — Understand context
2. **Identify candidates** — Note potential phrases
3. **Check naturalness** — Is it spoken?
4. **Check usefulness** — Is it practical?
5. **Check domain** — Is it relevant?
6. **Check level** — Is it appropriate?
7. **Generate metadata** — Add translations, examples
8. **Output phrases** — Return extracted phrases

---

**Convention Version:** 1.0
**Purpose:** Ensure consistent, high-quality phrase extraction
