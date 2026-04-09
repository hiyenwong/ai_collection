# SKILL.md - Valence-Arousal Subspace for LLM Emotion Control

## Paper Reference
- **arXiv:** 2604.03147
- **Title:** Valence-Arousal Subspace in LLMs: Circular Emotion Geometry and Multi-Behavioral Control
- **Utility Score:** 0.86
- **Authors:** Lihao Sun et al.
- **Date:** April 2026

## Core Insights

### Key Discovery
LLM representations contain a **valence-arousal (VA) subspace** with circular geometry matching human emotion perception models.

### Method
1. 211k emotion-labeled texts → emotion steering vectors
2. Learn VA axes as linear combinations of PCA components
3. Ridge regression on model's self-reported VA scores

### Properties
- Circular geometry consistent with human emotion models
- Projections correlate with human VA ratings (44k lexical items)
- Steering produces monotonic shifts in affective dimensions

### Behavioral Control
**Bidirectional control over:**
- **Refusal:** Increasing arousal ↓ refusal
- **Sycophancy:** Increasing arousal ↑ sycophancy
- Reverse direction produces opposite effects

### Cross-Architecture Generality
- Llama-3.1-8B
- Qwen3-8B
- Qwen3-14B

## Practical Applications

### Emotion Steering
```markdown
1. Compute VA steering vectors from emotion-labeled data
2. Apply projection along VA axes
3. Control affective output dimensions
4. Adjust refusal/sycophancy behavior
```

### Mechanistic Understanding
- Refusal tokens ("I can't", "sorry") occupy low-arousal, negative-valence regions
- VA steering directly modulates emission probability

### Behavior Modification
- Reduce excessive refusals (increase arousal)
- Reduce sycophancy (decrease arousal)
- Fine-grained affective control

## Key Takeaways
- LLMs encode emotion geometry like humans
- VA subspace enables behavioral control
- Refusal/sycophancy are linked to emotion space
- Cross-architecture generality exists

## Related Work
- Emotion prompting
- Refusal analysis
- Representation engineering

## Further Reading
- Full paper: https://arxiv.org/abs/2604.03147
- PDF: https://arxiv.org/pdf/2604.03147
## Description
Framework from arXiv papers. See paper reference for details.
## Activation Keywords

- emotion-steering-vectors
- emotion-steering-vectors 技能
- emotion-steering-vectors skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents

1. **Understand the Request**: Analyze what the user needs related to this skill's domain.
2. **Search for Information**: Use web_search to find relevant papers or documentation.
3. **Apply the Framework**: Follow the methodology described in the skill's key concepts.
4. **Provide Results**: Summarize findings and actionable recommendations.
5. **Verify Accuracy**: Cross-check key facts before presenting to user.

## Examples

### Example 1: Basic Usage

**User:** How can I apply emotion-steering-vectors?

**Agent:** I'll help you understand and apply emotion-steering-vectors...

### Example 2: Advanced Application

**User:** What are the key considerations for emotion-steering-vectors?

**Agent:** Let me search for the latest research and best practices...
