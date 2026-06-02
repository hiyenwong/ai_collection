---
name: llm-guided-quantum-code-discovery
description: "LLM-guided evolutionary workflow for quantum LDPC code discovery. Language models mutate Python programs generating bivariate-bicycle (BB) and perturbed BB code ansätze, paired with staged validation pipeline (GF(2) rank, distance estimation/certification, MILP, BLISS Tanner-graph dedup, decomposability analysis, local-Clifford equivalence checks). Use when discovering quantum error-correcting codes, running evolutionary search with LLM guidance, validating quantum code candidates, or comparing CSS vs non-CSS quantum codes. Activation: quantum code discovery, LLM-guided search, bivariate bicycle codes, quantum LDPC, evolutionary code search, CSS codes, Tanner graph dedup, local-Clifford equivalence"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.02418"
  published: "2026-06-01"
  authors: "Juan Cruz-Benito, Andrew W. Cross, David Kremer, Ismael Faro"
  tags: [quantum, error-correction, llm, evolutionary-search, ldpc, bivariate-bicycle]
---

## Core Workflow

LLM-guided evolutionary discovery of quantum LDPC codes follows a generate-screen-validate loop:

### 1. LLM-Guided Program Evolution
- LLM mutates Python programs that generate BB and perturbed BB code ansätze
- Each campaign runs ~330 evolutionary iterations, screening ~40K candidates
- Total effort: ~1650 iterations, ~2×10⁵ candidates, ~140h compute, ~$400 LLM cost

### 2. Staged Validation Pipeline
Each candidate passes through independent evaluation stages:

1. **GF(2) rank computation** — verify stabilizer matrix rank
2. **Distance estimation** — estimate minimum distance d
3. **Distance certification** — certify exact distance when feasible
4. **MILP** (Mixed-Integer Linear Programming) — optimization-based verification
5. **BLISS Tanner-graph deduplication** — eliminate isomorphic duplicates
6. **Decomposability analysis** — check if code decomposes into smaller components
7. **Local-Clifford equivalence checks** — identify equivalent codes under local Clifford transformations

### 3. Key Results (n ≤ 360)
- 465 distinct candidate codes found
- 97 CSS bivariate-bicycle codes
- 368 non-CSS perturbed variants
- Notable: indecomposable [[288,16,12]] code, higher-weight codes up to k=50 at d=8
- Non-CSS: perturbed codes matching gross-code figure of merit at [[144,12,12]]

## Activation Keywords
- quantum code discovery
- LLM-guided search
- bivariate bicycle codes
- quantum LDPC
- evolutionary code search
- CSS codes
- non-CSS quantum codes
- Tanner graph deduplication
- local-Clifford equivalence

## Pitfalls
- **LLM cost**: ~$400 per campaign — budget accordingly
- **Candidate explosion**: 2×10⁵ candidates require efficient staged filtering — early stages must reject quickly
- **GF(2) arithmetic**: Use efficient finite field libraries for rank computation on large stabilizer matrices
- **MILP scalability**: Distance certification via MILP becomes intractable for large n — report upper bounds when MILP times out
- **Deduplication bottleneck**: BLISS Tanner-graph isomorphism checking is expensive — run after cheap filters
