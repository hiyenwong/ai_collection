# SKILL.md - Contextual Enrichment in LLMs (RAG Evolution)

## Paper Reference
- **arXiv:** 2604.03174
- **Title:** Beyond the Parameters: A Technical Survey of Contextual Enrichment in Large Language Models
- **Utility Score:** 0.85
- **Authors:** Shivangi Agarwal et al.
- **Date:** April 2026

## Core Insights

### Problem Addressed
LLMs limited by:
- Static knowledge
- Finite context windows
- Weakly structured causal reasoning

### Augmentation Spectrum
Ranked by degree of structured context:

1. **In-Context Learning & Prompt Engineering**
   - Minimal structure
   - Ad-hoc prompting

2. **Retrieval-Augmented Generation (RAG)**
   - Document retrieval
   - Unstructured context injection

3. **GraphRAG**
   - Graph-structured retrieval
   - Entity relationship preservation

4. **CausalRAG**
   - Causal structure in retrieval
   - Reasoning-aware augmentation

## Practical Applications

### Deployment Decision Framework
```markdown
Assess needs:
1. Knowledge freshness → RAG needed
2. Entity relationships → GraphRAG
3. Causal reasoning → CausalRAG
4. Context limits → Determine augmentation level

Choose augmentation based on:
- Task complexity
- Reasoning requirements
- Domain structure
- Latency constraints
```

### Literature Screening Protocol
- Transparent filtering methodology
- Cross-paper evidence synthesis
- Higher-confidence vs. emerging results distinction

## Key Takeaways
- Contextual enrichment is a spectrum, not a single technique
- More structure → better reasoning, higher cost
- RAG evolution: documents → graphs → causal
- Decision framework for deployment choices

## Related Work
- Classic RAG implementations
- Graph-based knowledge systems
- Causal reasoning in NLP

## Further Reading
- Full paper: https://arxiv.org/abs/2604.03174
- PDF: https://arxiv.org/pdf/2604.03174
- 4 tables comparing approaches
## Description
Framework from arXiv papers. See paper reference for details.
## Activation Keywords

- rag-contextual-enrichment
- rag-contextual-enrichment 技能
- rag-contextual-enrichment skill

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

**User:** How can I apply rag-contextual-enrichment?

**Agent:** I'll help you understand and apply rag-contextual-enrichment...

### Example 2: Advanced Application

**User:** What are the key considerations for rag-contextual-enrichment?

**Agent:** Let me search for the latest research and best practices...
