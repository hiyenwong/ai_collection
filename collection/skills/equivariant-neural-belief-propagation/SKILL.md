---
name: equivariant-neural-belief-propagation
category: quantum
description: "Equivariant Neural Belief Propagation (ENBP) for SE(3)-symmetric probabilistic inference with Gaussian mixture messages"
activation: equivariant neural belief propagation, SE(3) symmetry, Gaussian mixture model, factor-graph inference, conformational coverage, molecular modeling
---

# equivariant-neural-belief-propagation

## Description
Equivariant Neural Belief Propagation (ENBP) methodology for probabilistic inference over spatially embedded variables with exact SE(3) symmetry. Based on arXiv: 2606.06344.

## Activation Keywords
- equivariant neural belief propagation
- SE(3) symmetry inference
- Gaussian mixture model messages
- factor-graph probabilistic inference
- conformational coverage
- molecular modeling
- equivariant outer products
- differentiable spectral decomposition

## Source Paper
- **arXiv**: 2606.06344
- **Title**: Equivariant Neural Belief Propagation
- **Published**: 2026-06-04

## Core Methodology

### Key Concepts
ENBP is a factor-graph framework whose messages are equivariant Gaussian mixture models with sufficient statistics that transform exactly under SE(3). It addresses the limitation of existing equivariant networks that produce only scalars and vectors, not the rank-2 precision tensors needed for anisotropic uncertainty.

### Mathematical Framework
- **Message Representation**: Equivariant Gaussian mixture models with SE(3)-transforming sufficient statistics
- **Rank-2 Precision Matrices**: Synthesized via equivariant outer products
- **Ingestion**: Through differentiable spectral decomposition
- **Tractability**: Maintained by greedy KL-based mixture reduction that provably commutes with SE(3)
- **Multi-body Inference**: Vanilla loopy BP diverges at 15+ agents while ENBP converges with near-zero collision rates

### Key Results
- 98.9% conformational coverage at 0.090 Angstrom error on GEOM-QM9 and GEOM-Drugs
- Sub-second latency, 100x faster than diffusion baselines at higher accuracy
- Near-zero collision rates on multi-body robotic inference
- Machine-precision equivariance error (~10^-7 vs 10^-1 for augmented baselines)

## Usage Patterns

### Pattern 1: Molecular Conformation Inference
Apply ENBP for predicting molecular conformations with SE(3) equivariance guarantees.

### Pattern 2: Multi-Agent Robotic Inference
Use ENBP for probabilistic inference in multi-robot systems where spatial symmetry must be preserved.

## Instructions for Agents

### Step 1: Identify SE(3) Symmetry Requirement
Determine if the problem involves spatially embedded variables requiring rotational and translational equivariance.

### Step 2: Choose ENBP over Standard Approaches
When standard equivariant networks fail to capture anisotropic uncertainty or collapse multi-modal landscapes, use ENBP.

### Step 3: Implement Factor-Graph with Gaussian Mixture Messages
Construct factor-graph where messages are Gaussian mixture models with SE(3)-transforming sufficient statistics.

## Error Handling
- If divergence occurs in loopy BP at 15+ agents, switch to ENBP framework
- Ensure equivariance error is at machine precision level (~10^-7)

## Resources
- arXiv: https://arxiv.org/abs/2606.06344
