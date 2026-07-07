---
name: superintelligent-retrieval-agent
description: "Superintelligent Retrieval Agent methodology for building retrieval-augmented systems that actively reason about information needs beyond black-box query issuance."
---

# Superintelligent Retrieval Agent

## Description
Retrieval-augmented agents are increasingly the interface to large organizational knowledge bases. This methodology proposes agents that go beyond exploratory black-box queries to actively reason about information needs, iteratively refine search strategies, and evaluate retrieval quality before generation. Based on arXiv:2605.06647.

## Activation Keywords
- superintelligent retrieval
- retrieval agent reasoning
- active retrieval strategy
- RAG agent optimization
- 智能检索代理
- 推理式检索
- retrieval-augmented agent design
- IR agent architecture

## Core Concepts

### 1. Beyond Black-Box Retrieval
Traditional RAG systems issue queries and accept whatever is returned. Superintelligent retrieval agents:
- Analyze the query's information gap before searching
- Select appropriate retrieval strategies based on query type
- Evaluate returned documents for relevance before passing to generator
- Iterate retrieval if gaps remain unfilled

### 2. Information Gap Analysis
Before retrieval, the agent should:
- Identify what type of information is needed (factual, procedural, analytical)
- Determine the depth required (surface-level vs. deep-dive)
- Assess what is already known vs. what needs to be retrieved

### 3. Strategy Selection
Match retrieval strategy to query characteristics:
- **Factual queries**: Direct keyword search + exact match
- **Analytical queries**: Multi-hop reasoning chains with iterative retrieval
- **Procedural queries**: Step-by-step documentation retrieval with context chaining
- **Exploratory queries**: Broad search followed by focused refinement

### 4. Quality Assessment Loop
After retrieval, before generation:
- Score documents for relevance to the specific information gap
- Detect contradictions between retrieved sources
- Identify missing information types that require additional retrieval
- Prune irrelevant or low-quality results

## Implementation Pattern

### Step 1: Query Decomposition
```
query -> analyze_intent -> identify_gaps -> [gap_type, depth_needed]
```

### Step 2: Strategy Selection
```
[gap_type, depth_needed] -> select_strategy -> [retrieval_method, parameters]
```

### Step 3: Iterative Retrieval
```
results = []
for round in max_rounds:
    results += retrieve(strategy, query, context)
    if gaps_filled(results, gaps):
        break
    query = refine_query(query, results, remaining_gaps)
```

### Step 4: Quality Gate
```
filtered = quality_assess(results, original_query)
if len(filtered) < threshold:
    fallback_strategy()
return filtered
```

## Error Handling

### Retrieval Failure
If no relevant documents are found:
1. Broaden search terms (remove specificity constraints)
2. Try alternative retrieval methods (vector search vs. keyword)
3. Generate synthetic context from known information
4. Explicitly state knowledge gaps to the user

### Contradictory Sources
If retrieved sources contradict:
1. Present both views with source attribution
2. Check publication dates for currency
3. Assess source credibility
4. Flag the contradiction explicitly

## Examples

### Example: Complex Analytical Query
```
User: "What are the economic impacts of AI on labor markets in developing countries?"

Agent reasoning:
1. Information gaps: economic data, labor statistics, developing country specifics
2. Strategy: Multi-hop retrieval
   - Round 1: "AI labor market impact developing countries"
   - Round 2: "automation employment substitution effect emerging economies"
   - Round 3: "World Bank AI jobs developing nations report"
3. Quality gate: Filter for recent reports, academic papers, policy documents
4. Synthesize across sources with source attribution
```

## Resources
- arXiv:2605.06647 - Superintelligent Retrieval Agent: The Next Frontier of Information Retrieval

## Related Skills
- memory-retrieval
- skill-rag-indexer
- llm-decision-centric-design
