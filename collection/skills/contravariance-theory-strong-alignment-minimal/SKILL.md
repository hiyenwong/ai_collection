---
name: contravariance-theory-strong-alignment-minimal
description: "Contravariance Theory proving that minimal DNN solutions to hard tasks guarantee strong alignment of privileged axes, formalizing convergent evolution between artificial networks and brain networks"
tags: [neuroai, brain-alignment, deep-neural-networks, convergent-evolution, representational-similarity, privileged-axes, contravariance]
arxiv_id: "2607.08561"
authors: ["Dan Yamins", "Aran Nayempa"]
date: "2026-07-09"
subjects: ["cs.LG", "q-bio.NC"]
---

# Contravariance Theory: Strong Alignment for Minimal Solutions to Hard Tasks

## Core Contribution

Proves that for any two **minimal DNN solutions** to a sufficiently hard task:
1. **Weak alignment** (affine mappings) guarantees **strong alignment** of privileged axes
2. Alignment **zippers up** the network hierarchy
3. Privileged axes emerge from end-to-end task optimization

This formalizes the notion of **contravariance** from Cao and Yamins [2024] and has profound implications for NeuroAI.

## Key Theoretical Results

### Weak-to-Strong Alignment Theorem
- For minimal solutions to hard tasks, weak alignment (based on affine mappings) **implies** strong alignment of privileged axes
- This means: if two networks solve the same hard task minimally, their internal representations must align at the level of functionally important features

### Alignment Zipping
- Alignment propagates **up the network hierarchy**
- Early layers may differ, but higher layers converge
- Emergence of privileged axes is inevitable under sufficient task pressure

### Convergent Evolution is Probable
- With sufficiently strong tasks, choice of metric for inter-network comparison is **not that sensitive**
- Convergent evolution between artificial and biological networks is **probably inevitable**
- This provides theoretical grounding for brain-DNN alignment research

## Implications for NeuroAI

### For Brain-DNN Comparison
- The specific alignment metric matters less than previously thought
- Task difficulty and minimality are the key drivers of alignment
- Explains why diverse DNN architectures can all align with brain data

### For Understanding Brain Computation
- Suggests brain networks are near-optimal solutions to their computational tasks
- Privileged axes in the brain may emerge from task optimization, not architectural constraints
- Provides framework for predicting which brain areas should align with which DNN layers

### For AI Design
- Hard task optimization naturally produces brain-like representations
- Minimal solutions are key - overparameterized networks may not converge
- Suggests design principles for more brain-efficient AI

## Methodology Notes

- Formal mathematical proof framework
- Builds on 15 years of NeuroAI results
- Extends Cao and Yamins [2024] contravariance formalization
- Applies to any two minimal DNN solutions (architecture-agnostic)

## Limitations

- Theoretical result - requires empirical validation
- "Sufficiently hard task" is not precisely quantified
- Minimality condition may be difficult to verify in practice
- Does not address how biological constraints shape alignment

## Related Work

- Brain-DNN alignment (Yamins et al., 2014)
- Representational Similarity Analysis (Kriegeskorte et al.)
- Canonical Correlation Analysis for neural networks
- Net2Brain comparison frameworks
- Cao and Yamins [2024] - original contravariance formulation

## Activation

contravariance, brain alignment, neuroai, convergent evolution, privileged axes, minimal solutions, deep neural networks, representational similarity, hard tasks, dnn-brain comparison