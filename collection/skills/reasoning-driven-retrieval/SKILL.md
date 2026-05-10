---
name: reasoning-driven-retrieval
description: "Retrieval as iterative reasoning methodology. Treat retrieval as explicit hypothesis-driven search with evidence evaluation and self-improving refinement. Use when building RAG systems, information retrieval agents, search optimization, or any system that needs to go beyond black-box retrieval to find latent-pattern documents."
---

# Reasoning-Driven Retrieval

Treat retrieval as an explicit reasoning process — iterative, self-improving search guided by hypothesis formulation, evidence evaluation, and search refinement.

## Core Insight

Traditional RAG treats retrieval as a black box: issue query, inspect snippets, synthesize answer. But reasoning LLMs can reliably recognize latent relevance when documents are surfaced — the failure is that retrieval pipelines don't surface the most relevant documents for oblique queries seeking latent patterns (implicit stance, failure modes, abstract scenarios).

## Retrieval Agent Framework

### Phase 1: Hypothesis Formulation

```
Given query Q:
1. What implicit patterns might relevant documents instantiate?
2. What evidence would confirm/refute each hypothesis?
3. What search strategies would surface such evidence?
```

### Phase 2: Iterative Search

```
For each hypothesis H:
1. Generate targeted search queries for H
2. Retrieve candidate documents
3. Evaluate each document as evidence for H
4. Update hypothesis confidence
5. Refine search strategy based on evidence gaps
```

### Phase 3: Self-Improvement

```
After search iteration:
1. Which hypotheses were confirmed/refuted?
2. What search strategies failed to surface relevant docs?
3. What oblique query patterns were missed?
4. Update retrieval policy for future queries
```

## Implementation

```python
class RetrievalAgent:
    def __init__(self, retriever, reasoner):
        self.retriever = retriever
        self.reasoner = reasoner  # Reasoning LLM for hypothesis/evidence
        self.max_iterations = 5
    
    def retrieve_with_reasoning(self, query):
        # Phase 1: Generate hypotheses
        hypotheses = self.reasoner.generate_hypotheses(query)
        
        evidence = {}
        for iteration in range(self.max_iterations):
            # Phase 2: Search and evaluate
            for h in hypotheses:
                queries = self.reasoner.generate_search_queries(h, query)
                docs = self.retriever.search(queries)
                evidence[h] = self.reasoner.evaluate_evidence(docs, h)
            
            # Phase 3: Refine
            gaps = self.reasoner.identify_gaps(evidence, hypotheses)
            if not gaps:
                break
            hypotheses = self.reasoner.refine_hypotheses(hypotheses, evidence, gaps)
        
        return self.reasoner.synthesize(evidence, query)
```

## Oblique Query Patterns (OBLIQ-Bench)

Key retrieval bottleneck: oblique queries seeking documents that instantiate **latent patterns**:

1. **Implicit Stance**: Documents revealing author position without explicit statement
2. **Failure Modes**: Documents describing system failures implicitly
3. **Abstract Scenarios**: Documents matching abstract structural patterns
4. **Cross-Domain Parallels**: Documents with analogous reasoning patterns
5. **Assumption Exposure**: Documents revealing unstated assumptions

Reasoning LLMs can recognize latent relevance once surfaced — but traditional retrievers fail to surface them.

## Key Metrics

- **Latent Recall**: Fraction of relevant documents found for oblique queries
- **Hypothesis Precision**: Fraction of generated hypotheses that yield relevant evidence
- **Search Efficiency**: Documents examined per relevant document found
- **Self-Improvement Rate**: Performance gain across iterations

## Pitfalls

- Over-iteration wastes compute — set max iterations based on task complexity
- Hypothesis generation must be diverse — avoid confirmatory bias
- Evidence evaluation should be calibrated — reasoning LLMs can over-confidently endorse irrelevant documents

## References

- arXiv: OBLIQ-Bench (ID: 676) — Exposes overlooked bottlenecks in modern retrievers
- arXiv: Superintelligent Retrieval Agent (ID: 657) — Retrieval as reasoning process
