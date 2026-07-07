---
name: llm-structured-concept-evolution
description: "Structured Concept Evolution (SCE) — search framework pairing LLMs with structured algebraic mutation grammars to discover quantum LDPC code families. Evolves structured concepts (algebraic specifications + executable programs) via hierarchical mutations on group algebra, protograph geometry, or base space, discovering competitive CSS qLDPC codes including non-abelian group constructions beyond bivariate-bicycle codes. Use when discovering quantum error-correcting codes, running LLM-guided algebraic search, or exploring lifted-product code families."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.24808"
  published: "2026-06-23"
  authors: "Zidu Liu, Florian Marquardt"
  tags: [quantum, error-correction, llm, ldpc, structured-concept-evolution, css-codes, non-abelian]
---

# LLM Structured Concept Evolution for Quantum LDPC Code Discovery

## Paper Summary

**Title**: Large-Language-Model Discovery of Quantum LDPC Codes through Structured Concept Evolution
**arXiv**: 2606.24808
**Date**: June 23, 2026
**Authors**: Zidu Liu, Florian Marquardt

## Core Innovation

**Structured Concept Evolution (SCE)** is a search framework that pairs a large language model with a **structured algebraic mutation grammar** to discover **lifted-product code families** — a class of CSS qLDPC (quantum low-density parity-check) codes. Unlike prior approaches that ask LLMs to design codes from first principles, SCE **evolves structured concepts** consisting of:

1. **Algebraic specifications** (group algebra definitions, protograph geometry, base space)
2. **Executable programs** that realize those specifications

Using **hierarchical mutations** that modify the group algebra, protograph geometry, or base space, SCE discovers a diverse set of competitive code families ranging from abelian constructions to families over **non-abelian groups** beyond standard designs such as bivariate-bicycle codes.

## How SCE Works

### Structured Concept Representation

Each "concept" is a pair `(spec, program)`:
- **spec**: Algebraic specification (group algebra, protograph geometry, base space)
- **program**: Executable Python code that constructs the code from the specification

### Hierarchical Mutation Grammar

Mutations operate at three levels of abstraction:

1. **Group Algebra Level**: Modify the underlying group (abelian → non-abelian, change generators, relations)
2. **Protograph Geometry Level**: Change the base protograph structure, connectivity patterns
3. **Base Space Level**: Alter the lifting parameters, expansion factors

### Search Loop

```
1. Initialize: Seed concepts from known code families (bivariate-bicycle, etc.)
2. Mutate: Apply hierarchical mutations from the grammar to create candidate concepts
3. Execute: Run the executable program to construct the code
4. Evaluate: Check code parameters (n, k, d) under BP+OSD decoding
5. Select: Keep competitive codes, discard duplicates
6. Repeat until convergence or budget exhausted
```

### Evaluation Protocol

- **Decoder**: BP+OSD (Belief Propagation + Ordered Statistics Decoding)
- **Noise Model**: Code-capacity depolarizing noise
- **Metrics**: Code parameters [[n, k, d]], encoding rate k/n, relative distance d/n

## Key Results

- Discovered code families over **non-abelian groups** beyond bivariate-bicycle codes
- Used **lightweight models** (GPT-5.4-mini and GPT-5.4-nano) — demonstrates SCE is model-efficient
- Found competitive codes with diverse algebraic structures
- Characterized performance under standard decoding assumptions

## Implementation Notes

### Mutation Grammar Design

The mutation grammar is the critical design element:

```python
class MutationGrammar:
    def mutate_group_algebra(self, concept):
        # Change generators: add/remove/modify group generators
        # Change relations: modify group presentation
        # Change group type: abelian ↔ non-abelian
        
    def mutate_protograph(self, concept):
        # Change protograph dimensions
        # Add/remove edges in protograph
        # Modify edge weights/labels
        
    def mutate_base_space(self, concept):
        # Change lifting parameters
        # Modify expansion factors
        # Alter base field characteristics
```

### Executable Program Synthesis

Each concept's program must:
1. Construct the parity check matrices (H_X, H_Z)
2. Verify CSS conditions (H_X @ H_Z^T = 0 mod 2)
3. Compute code parameters (n, k, d)
4. Export for BP+OSD decoding evaluation

### LLM Prompt Design

```
Given the following algebraic specification for a lifted-product code:
{spec}

Apply a [group_algebra/prot_geometry/base_space] mutation to produce
a new specification. The mutation should:
- Maintain mathematical validity
- Explore a different region of code space
- Preserve the lifted-product structure

Output the new specification and corresponding Python implementation.
```

## Comparison with Prior Approaches

| Aspect | Prior LLM Code Discovery | SCE (This Paper) |
|--------|-------------------------|------------------|
| Search Space | Unstructured programs | Structured algebraic concepts |
| Mutation | Program-level edits | Hierarchical algebraic mutations |
| Discoverability | Limited to known patterns | Discovers non-abelian families |
| Model Size | Typically requires large models | Works with lightweight models |

## When to Use

- **Quantum code discovery**: Finding new qLDPC code families
- **Algebraic code exploration**: Exploring non-abelian group constructions
- **Lightweight LLM search**: When compute budget limits model size
- **CSS code design**: Specifically for CSS qLDPC codes via lifted-product construction

## Activation Keywords

- structured concept evolution, SCE
- LLM quantum code discovery
- quantum LDPC code search
- lifted-product codes
- non-abelian quantum codes
- bivariate bicycle codes
- CSS qLDPC discovery
- algebraic mutation grammar
- code family evolution
- group algebra code design

## Pitfalls

- **Grammar design**: The mutation grammar must be expressive enough to discover new codes but constrained enough to maintain mathematical validity
- **Verification cost**: Each candidate requires full code construction and parameter computation — use cheap filters before expensive decoding
- **Duplicate detection**: Many mutations produce equivalent codes — implement efficient isomorphism checking
- **LLM prompt drift**: Lighter models may drift from the structured format — use strict output parsing
- **Noise model assumptions**: Code-capacity depolarizing noise is simplified — validate under more realistic circuit-level noise

## Resources

- arXiv:2606.24808 — "Large-Language-Model Discovery of Quantum LDPC Codes through Structured Concept Evolution"
- BP+OSD decoder implementations for qLDPC code evaluation
- CSS code construction via lifted-product method

## Related Skills

- `llm-guided-quantum-code-discovery` — Evolutionary BB code discovery (different paper, different approach)
- `quantum-error-correction-methods` — QEC patterns and methods
- `quantum-ldpc-breakeven` — qLDPC breakeven demonstration
- `llm-quantum-reasoning` — Fine-tuning LLMs for quantum reasoning