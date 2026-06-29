---
name: llm-guided-quantum-code-discovery
description: Structured Concept Evolution (SCE) methodology for discovering quantum LDPC codes using LLM + algebraic mutation grammar. Evolves structured concepts of algebraic specifications with executable programs via hierarchical mutations.
category: quantum-error-correction
trigger_words: structured concept evolution, SCE, qLDPC code discovery, LLM code design, lifted-product codes, algebraic mutation, CSS qLDPC, code search, group algebra
source: arXiv:2606.24808
---

# Structured Concept Evolution (SCE) for qLDPC Code Discovery

## Overview

SCE is a search framework that combines Large Language Models with structured algebraic mutation grammars to discover quantum LDPC (qLDPC) code families, specifically lifted-product codes. Rather than asking LLMs to design codes from first principles, SCE evolves structured concepts through hierarchical mutations.

## Key Insight

**Concept Evolution over Generation**: Instead of free-form code generation, SCE evolves structured concepts — pairs of algebraic specifications + executable programs — through controlled mutations. This constrains the search space to valid code constructions while enabling creative exploration.

## Core Components

### 1. Structured Concept Representation
- Each concept = (algebraic specification, executable program)
- Algebraic spec: group algebra, protograph geometry, base space
- Executable program: code realization (parity check matrices, etc.)

### 2. Hierarchical Mutation Grammar
Three levels of mutation:
- **Group algebra level**: Modify group structure (abelian ↔ non-abelian)
- **Protograph geometry level**: Modify base graph topology
- **Base space level**: Modify underlying algebraic field/ring

### 3. LLM-Guided Evolution
- LLM proposes mutations within the grammar
- Lightweight models sufficient (GPT-5.4-mini, GPT-5.4-nano)
- Evolution driven by code performance metrics

### 4. Evaluation Pipeline
- Test under code-capacity depolarizing noise
- Decode with BP+OSD (Belief Propagation + Ordered Statistics Decoding)
- Track code rate, distance, and logical error rate

## Discovery Results

SCE discovered diverse code families:
- Abelian constructions (standard approach)
- Non-abelian group families beyond bivariate-bicycle codes
- Novel lifted-product constructions with competitive parameters

## Implementation Pattern

```
1. Define initial concept population (known code families)
2. For each generation:
   a. LLM proposes mutations via grammar
   b. Generate executable programs from mutated specs
   c. Evaluate code parameters and performance
   d. Select top performers for next generation
3. Track discovered families and characterize diversity
```

## Pitfalls

- **Grammar completeness**: Mutation grammar must cover the interesting design space; missing mutations = missed discoveries
- **Evaluation cost**: BP+OSD decoding is expensive; limit evaluations to promising candidates
- **LLM hallucination**: Algebraic specs must be validated before execution; invalid specs waste compute
- **Local optima**: Evolution can get stuck; use diverse initial population

## Applications

- Automated discovery of new qLDPC code families
- Exploration of algebraic code construction space
- LLM-assisted quantum code design
- Discovery of codes optimized for specific hardware constraints

## Activation

Use when: discovering new qLDPC codes, LLM-assisted quantum code design, algebraic code construction, lifted-product codes, CSS code search, quantum error correction code optimization, automated code family discovery.
