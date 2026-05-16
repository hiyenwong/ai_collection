---
name: agentic-graphrag-citation-provenance
description: >
  Methodology for evaluating citation faithfulness in Agentic GraphRAG systems as a
  trajectory-level problem. Addresses how cited evidence, traversal context, and graph
  structure influence answer accuracy. Use when: building GraphRAG systems, evaluating
  citation quality, designing knowledge graph retrieval, or analyzing agent traversal
  patterns. Triggers: GraphRAG citation evaluation, retrieval provenance, knowledge
  graph traversal analysis, citation faithfulness, agentic RAG.
---

# Agentic GraphRAG Citation Provenance

## Overview

From arXiv:2605.15109 - "Why Neighborhoods Matter: Traversal Context and Provenance in Agentic GraphRAG"

Traditional RAG citation evaluation checks if cited sources support the answer.
In Agentic GraphRAG, this is insufficient because:
1. Agents traverse knowledge graphs before answering
2. Visited-but-uncited entities influence the final answer
3. Graph structure and traversal path matter for provenance

## Key Findings

### Cited Evidence: Necessary but NOT Sufficient

| Test | Result |
|------|--------|
| Remove cited entities | Answers change substantially, accuracy drops |
| Remove uncited traversal context | Answers also change, showing hidden influence |
| Mask visited entities | Similar degradation to removal |

### Citation Faithfulness is Trajectory-Level

Final citations must account for:
- **Graph traversal path** - the route taken through the KG
- **Visited-but-uncited entities** - nodes that influenced reasoning
- **Surrounding graph structure** - connectivity patterns that shaped retrieval

## Evaluation Methodology

### Controlled Ablation Experiments

```python
def evaluate_citation_faithfulness(agent, graph, query):
    # Baseline: full graph traversal
    baseline_answer, baseline_citations = agent.query(graph, query)
    
    # Ablation 1: Remove cited entities
    no_cited = graph.remove(baseline_citations)
    answer_no_cited = agent.query(no_cited, query)
    
    # Ablation 2: Remove uncited visited entities
    visited = agent.get_traversal_trace()
    uncited_visited = visited - baseline_citations
    no_uncited = graph.remove(uncited_visited)
    answer_no_uncited = agent.query(no_uncited, query)
    
    # Ablation 3: Mask entities (keep structure, hide content)
    masked = graph.mask(uncited_visited)
    answer_masked = agent.query(masked, query)
    
    return {
        'cited_necessary': baseline_answer != answer_no_cited,
        'uncited_influential': baseline_answer != answer_no_uncited,
        'structural_dependence': baseline_answer != answer_masked,
    }
```

### Provenance-Aware Evaluation Framework

Instead of binary citation support, measure:
1. **Source Support** - Do citations back up claims? (traditional)
2. **Coverage** - Do citations cover all influential sources? (new)
3. **Trajectory Fidelity** - Does the citation path match the retrieval path? (new)
4. **Structural Faithfulness** - Are graph neighborhood influences accounted for? (new)

## Design Implications

### For GraphRAG Systems

- **Log full traversal traces** - not just final citations
- **Consider neighborhood context** - nearby entities influence retrieval ranking
- **Evaluate at trajectory level** - single citations don't tell the full story
- **Account for structural bias** - graph connectivity shapes what agents "see"

### For Citation Evaluation

- Move beyond source-level support to trajectory-level provenance
- Track visited-but-uncited entities as part of answer attribution
- Consider graph structure as a confounding factor in evaluation

## Resources

- Paper: https://arxiv.org/abs/2605.15109
