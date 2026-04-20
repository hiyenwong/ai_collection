# SKILL.md - RACE: Fine-Grained LLM Text Detection

## Paper Reference
- **arXiv ID**: 2604.04932
- **Title**: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection
- **Authors**: Yang Li et al.
- **Venue**: ACL 2026 (Accepted)
- **Date**: April 2026
- **URL**: https://arxiv.org/abs/2604.04932

## Utility Score
**0.88** - High utility for LLM regulation and content verification

## Core Insight
Existing binary/ternary classification is insufficient for nuanced LLM regulation. A four-class setting distinguishing pure human, pure LLM, LLM-polished human text, and humanized LLM text enables policy-aligned detection.

## Key Methods
### RACE Framework
**Rhetorical Analysis for Creator-Editor Modeling**

1. **Creator Foundation**: Rhetorical Structure Theory constructs logic graph
2. **Editor Style**: Elementary Discourse Unit-level feature extraction
3. **Dual Role Characterization**: Separates creator and editor signatures

### Four-Class Detection
- Pure human text
- Pure LLM-generated text
- LLM-polished human text (human created, LLM edited)
- Humanized LLM text (LLM created, human edited)

## When to Apply
- Content authenticity verification
- LLM regulation compliance
- Academic integrity checking
- Policy enforcement for AI-generated content

## Practical Applications
1. **Content Moderation**: Detect different levels of AI involvement
2. **Academic Integrity**: Distinguish LLM-polished from pure LLM work
3. **Platform Policy**: Enforce nuanced AI content rules
4. **Regulatory Compliance**: EU AI Act alignment

## Key Takeaways
- **Policy consequences differ** by creator/editor roles
- **Binary detection is insufficient** for modern regulation
- **Rhetorical structure analysis** provides fine-grained signals
- Low false alarm rate critical for practical deployment

## Advantages
- Outperforms 12 baselines
- Low false alarm rates
- Policy-aligned output categories
- Handles collaborative/hybrid content

## Tags
`text-detection` `llm-regulation` `rhetorical-analysis` `content-authenticity` `acl-2026` `policy-compliance`

## Activation Keywords

- "paper-race"
- "paper race"
- "use paper race"
- "paper race help"
- "paper race tool"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Paper Race usage
```
User: "Help me with paper race"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed paper race assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
