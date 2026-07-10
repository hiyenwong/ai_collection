---
name: dsm-llm-modularization
description: "LLM-based Design Structure Matrix (DSM) modularization methodology. Use when partitioning complex systems into cohesive modules, optimizing system architecture, or applying LLMs to combinatorial engineering problems. Activation triggers: DSM, design structure matrix, system modularization, architecture decomposition, LLM combinatorial optimization, semantic alignment hypothesis, engineering design optimization."
---

# DSM Modularization with Large Language Models

> LLM-based approach to Design Structure Matrix modularization achieving near-reference quality within 30 iterations without specialized optimization code. Introduces the semantic-alignment hypothesis governing when domain knowledge helps or hurts LLM-based optimization.

## Metadata
- **Source**: arXiv:2604.28018
- **Authors**: Shuo Jiang, Jianxi Luo
- **Published**: 2026-04-30
- **Subjects**: cs.CE (Computational Engineering); cs.AI

## Core Methodology

### Key Innovation

DSM modularization partitions system elements into cohesive modules — a fundamental combinatorial challenge in engineering design. This paper shows that **LLMs can solve DSM modularization** through iterative prompting, without requiring specialized optimization code.

### Technical Framework

**Three-stage LLM-based modularization**:

1. **Input Representation**
   - Convert DSM (N×N dependency matrix) into natural language description
   - Include element names, dependency strengths, and constraints
   - **Best practice**: Include raw matrix structure + semantic labels

2. **Objective Formulation**
   - Frame modularization as minimizing inter-module dependencies
   - Use standard metrics: Minimum Description Length (MDL), clustering coefficient
   - **Best practice**: Provide explicit objective function in natural language

3. **Solution Pool Design**
   - Maintain a pool of candidate solutions across iterations
   - LLM generates new candidates, evaluates against pool
   - **Best practice**: Pool size 5-10, retain top-k by objective value

### Critical Finding: Semantic-Alignment Hypothesis

**Counterintuitive result**: Domain knowledge, beneficial in DSM *sequencing*, consistently **impairs** performance on DSM *modularization* for complex DSMs.

**Hypothesis**: LLM effectiveness with domain knowledge depends on **semantic alignment** between:
- The LLM's functional priors (what it "knows" about the domain)
- The optimization objective (structural vs. functional)

**When knowledge helps**: The domain semantics align with the optimization goal
**When knowledge hurts**: The LLM's functional priors conflict with structural optimization objectives

**Testable condition**: Before adding domain knowledge to LLM prompts, verify whether the knowledge supports or contradicts the mathematical objective.

### Implementation Guide

**Step 1: DSM Construction**
- Build N×N matrix of element dependencies
- Weight edges by dependency strength
- Validate matrix completeness

**Step 2: LLM Prompt Design**
```
System: You are an expert in system architecture modularization.
Task: Partition these {N} system elements into cohesive modules.
Input: {DSM_description_with_element_names_and_dependencies}
Objective: Minimize inter-module dependencies (total coupling between modules).
Constraints: {max_modules, min_module_size, etc.}
Format: Return module assignments as JSON.
```

**Step 3: Iterative Optimization**
- Run 30 iterations of LLM prompting
- Each iteration: present current best + ask for improvement
- Track objective value across iterations
- Convergence typically within 20-30 iterations

**Step 4: Validation**
- Compare against reference solutions (if available)
- Compute modularity metrics (MDL, clustering coefficient)
- Evaluate semantic coherence of modules

### Pitfalls
- **Semantic misalignment**: Adding domain knowledge to prompts can degrade results if the knowledge conflicts with structural optimization. Test both with and without domain context.
- **LLM variability**: Different backbone LLMs produce different quality results. Test across 2-3 models.
- **Prompt sensitivity**: Input representation format significantly impacts results. Use ablation studies to find optimal format.
- **Scale limits**: Method validated on DSMs up to moderate size. Very large DSMs (N > 200) may need hierarchical decomposition.

## Applications
- System architecture design
- Software modularization
- Product family planning
- Organization design
- Supply chain clustering

## Related Skills
- modern-systems-engineering-patterns
- emergent-systems-design
- agent-first-bootstrap
