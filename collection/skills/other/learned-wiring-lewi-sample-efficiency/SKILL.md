---
name: learned-wiring-lewi-sample-efficiency
description: "Use when high-dimensional prediction suffers the curse of dimensionality and the target has hidden compositional structure. LeWi jointly learns neuron wiring (via low-dim embeddings, nearby-neurons-connect) with weights for 27% lower learning-curve area than dense nets."
category: ai_collection
metadata:
  arxiv_id: "2610.28555"
---

# LeWi: Learned Wiring for Sample-Efficient Prediction of Computationally Sparse Targets

Source: arXiv:2610.28555 (Zhou, Dovrolis, Mussmann, Oct 2026). Computationally sparse functions admit a composition of local functions, each depending on few variables, so sample complexity could scale with **local arity rather than ambient dimension** — but practical gradient training does not automatically exploit this hidden structure.

## Diagnosis benchmark: CSFRBench

- Controlled benchmark that **hides the target's compositional computation during training** but retains it for diagnosis.
- Finding: dense networks and sparsity-based baselines leave much of the compositional benefit **unrealized** — knowing the theory is not enough; the architecture must be able to learn the wiring.

## Method (LeWi — Learned Wiring)

1. Each neuron carries a **learned low-dimensional embedding** (position in a virtual space).
2. **Only nearby neurons connect** — connectivity is a function of embedding distance, inspired by the spatial organization of biological neural circuits.
3. **Embeddings and weights are trained jointly** — the network learns *where* neurons are (hence *which* subcircuits exist) while learning *what* they compute.

## Results

- Targets with hierarchical structure, intermediate reuse, or independent modules: LeWi improves sample efficiency; across 32 targets from independently sampled computation graphs it is the **most sample-efficient method not given the target graph**, with **27% lower mean learning-curve area** than dense networks.
- Honest negative: dense networks **perform better on single high-arity functions** (no compositional structure to exploit).
- LeWi representations and connectivity align with the target computation.
- 17 world-model prediction tasks (control, navigation, manipulation): beats the dense baseline on **16/17**, wins **99/119** baseline comparisons.

## Reuse pattern

- When a prediction target plausibly has **compositional/modular structure** (physical systems, multi-object scenes, pipelines), make connectivity itself a learned function of per-neuron embeddings rather than fixed dense/sparse masks.
- Budget check first: if the target is a single high-arity function, dense wins — LeWi pays off only when structure exists.
- Wiring learned jointly with weights also yields interpretable subcircuits (embedding clusters ≈ modules) for free.

Related: connectome-informed wiring priors (fixed, not learned), L-system/lottery sparse nets, differentiable NAS (architecture-level), growing-neural-network breadth/depth/time cost frameworks.
