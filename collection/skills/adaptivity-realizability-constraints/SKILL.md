---
name: adaptivity-realizability-constraints
description: "Theoretical framework comparing in-context learning (fixed queries) vs agentic learning (adaptive queries) under neural network realizability constraints. Use when: analyzing when adaptive querying helps or hurts, comparing ICL with agentic RL, understanding representational constraints in learning systems, designing adaptive query strategies for neural networks. Keywords: in-context learning, agentic learning, adaptivity, realizability, neural network approximation, ReLU networks, learning theory."
---

# Adaptivity Under Realizability Constraints

> Theoretical framework revealing four distinct scenarios where adaptivity's advantage depends critically on whether the learning system is unrestricted or constrained to neural network implementations.

## Metadata
- **Source**: arXiv:2605.04995
- **Authors**: Anastasis Kratsios, A. Martina Neuman, Philipp Petersen
- **Published**: 2026-05-06

## Core Methodology

### Key Insight
**Adaptivity's advantage is NOT universal** — it depends on the interplay between task families and representational constraints. The paper identifies four distinct approximation scenarios:

| Scenario | Unrestricted Regime | ReLU Realizable Regime |
|----------|-------------------|----------------------|
| (a) No advantage | ≈ ICL | ≈ Agentic |
| (b) Persistent advantage | Agentic > ICL | Agentic > ICL |
| (c) Emergent advantage | ≈ | Agentic > ICL |
| (d) Disappearing advantage | Agentic > ICL | ≈ ICL |

### Technical Framework

**Two Regimes:**
1. **Unrestricted**: Querying and approximation are arbitrary functions
2. **Realizable**: All operations must be implemented by ReLU neural networks

**Key Theorem:** In both regimes, adaptivity never hinders approximation performance for uniform approximation of task families. However, the **magnitude** of advantage changes between regimes.

**Four Scenarios (each witnessed by explicit task families):**

**(a) No Advantage of Adaptivity**
- Task structure is simple enough that fixed queries suffice
- Representational constraints don't change this

**(b) Persistent Advantage**
- Adaptive queries genuinely help
- Advantage survives ReLU implementation
- Typical for tasks requiring sequential refinement

**(c) Emergent Advantage (only under realizability)**
- Counterintuitive: adaptivity helps ONLY when constrained
- ReLU representational bottleneck makes fixed queries insufficient
- Adaptive queries circumvent the bottleneck through sequential composition

**(d) Disappearing Advantage**
- Adaptive queries help in unrestricted setting
- But ReLU constraint eliminates the advantage
- Fixed ICL becomes equally powerful under neural implementation

### Analytical Tools
- Uniform approximation theory for task families
- ReLU neural network expressivity bounds
- Compositional function representation
- Realizability constraint analysis

## Implementation Guide

### Step 1: Characterize Task Family
```python
# Define the family of tasks to be approximated
# Specify input/output spaces and target functions
```

### Step 2: Analyze Unrestricted Regime
```python
# Determine optimal fixed-query strategy (ICL)
# Determine optimal adaptive-query strategy (agentic)
# Compare approximation errors
```

### Step 3: Analyze Realizable Regime
```python
# Constrain all operations to ReLU networks
# Re-compute approximation errors
# Identify which scenario (a-d) applies
```

### Step 4: Design Strategy
```python
# If scenario (b): use adaptive queries
# If scenario (c): use adaptive queries (especially important!)
# If scenario (d): fixed queries sufficient, save computation
# If scenario (a): either strategy works
```

## Applications
- Deciding between ICL and agentic workflows for specific tasks
- Understanding when agent-style adaptive prompting is worth the overhead
- Neural architecture design for learning systems
- Theoretical analysis of LLM reasoning strategies
- Resource allocation: when to invest in adaptive vs. fixed computation

## Pitfalls
- Analysis assumes uniform approximation; average-case may differ
- ReLU realizability is specific to the architecture choice
- Task family characterization is critical and non-trivial
- Results apply to approximation quality, not convergence speed

## Related Skills
- meta-learning-in-context-brain-decoding
- agent-delegation-rules
- representation-steering
- validation-driven-llm-workflow
