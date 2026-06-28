# phrase-card-generator

Creates phrase cards from extracted phrases.

## Trigger Conditions

User runs:
```bash
/build-phrase-cards --target obsidian
```

Or when:
- Adding new phrases to bank
- Creating practice materials
- Exporting to Obsidian/Anki

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| phrases | list | Extracted phrases with metadata |
| target_format | string | obsidian, anki, markdown |
| domain | string | Domain tag for cards |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| cards | list | Generated phrase cards |
| file_path | string | Path to generated file |
| cards_count | number | Number of cards generated |

## Card Template

### Obsidian Format
```markdown
# [[phrase]]

**Russian:** [[russian_meaning]]
**Domain:** [[domain]]
**Status:** #[passive|recognized|semi-active|active|meeting-ready]

## Context
[[context]]

## Examples
**Natural:** "[spoken_example]"
**Too formal:** "[too_formal_version]"

## Practice
- [ ] Used in interview
- [ ] Used in meeting
- [ ] Used in technical discussion
- [ ] Used in casual conversation

## Activation Log
- [[date]]: [[score]] — [[notes]]
```

### Anki Format
```markdown
Front: [[phrase]]
Back:
- Russian: [[russian_meaning]]
- Context: [[context]]
- Natural example: "[spoken_example]"
- Avoid: "[too_formal_version]"

Tag: [[domain]] #[status]
```

### Plain Markdown
```markdown
## Phrase: [[phrase]]

**Russian:** [[russian_meaning]]
**Domain:** [[domain]]
**Status:** [[status]]

**Where to use it:** [[context]]

**Natural example:**
> "[spoken_example]"

**Avoid:**
> "[too_formal_version]"
```

## Workflow

1. **Receive phrases** — Get extracted phrases with metadata
2. **Choose format** — Obsidian, Anki, or markdown
3. **Generate cards** — Create card for each phrase
4. **Organize by domain** — Group cards by domain
5. **Add metadata** — Include tags, status, examples
6. **Write file** — Save to appropriate location
7. **Report summary** — Count and location

## Examples

### Example 1: Obsidian card
```markdown
# push back on

**Russian:** возразить против, отрицательно отреагировать
**Domain:** stakeholder-pushback
**Status:** #passive

## Context
Use when disagreeing with a stakeholder request or timeline.

## Examples
**Natural:** "I'd push back on that timeline."
**Too formal:** "I would respectfully disagree with said timeline."

## Practice
- [ ] Used in interview
- [ ] Used in meeting
- [ ] Used in technical discussion
- [ ] Used in casual conversation

## Activation Log
- 2025-06-28: 45 — Used correctly but too formal
- 2025-06-30: 65 — Used naturally in meeting
```

### Example 2: Anki card
```markdown
Front: push back on
Back:
- Russian: возразить против, отрицательно отреагировать
- Context: Disagreeing with stakeholder requests
- Natural example: "I'd push back on that timeline."
- Avoid: "I would respectfully disagree with said timeline."

Tag: stakeholder-pushback #passive
```

## Output Locations

| Format | Default Location |
|--------|------------------|
| Obsidian | `~/ObsidianVault/SpeakOps/Phrases/` |
| Anki | `~/Documents/SpeakOps/Anki/` |
| Markdown | `data/phrase_cards/` |

## Eval Cases

### Test 1: Generates correct format
**Input:** Phrase list, target: obsidian
**Expected:** Valid Obsidian markdown
**Pass criteria:** All cards use correct template

### Test 2: Includes all metadata
**Input:** Phrase with full metadata
**Expected:** All metadata present in card
**Pass criteria:** Russian, domain, context, examples included

### Test 3: Organizes by domain
**Input:** Mixed domain phrases
**Expected:** Cards grouped by domain
**Pass criteria:** Domain folders/files created

## Risks and Limitations

- May not match user's Obsidian structure
- Anki format may need manual adjustment
- File locations may not match user preferences
- May overwrite existing cards
- May not handle special characters well

## Related Skills

- **phrase-extractor** — Provides phrases
- **activation-scorer** — Provides status updates
- **source-ingestor** — Triggers card generation
