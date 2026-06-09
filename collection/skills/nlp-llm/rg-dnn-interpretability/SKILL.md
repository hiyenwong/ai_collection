---
name: rg-dnn-interpretability
description: >
  Renormalization Group (RG) interpretability framework for deep neural networks.
  Establishes correspondence between RG in statistical physics and DNN training,
  proving DNN feature extraction is equivalent to RG flow on exponential family distributions.
  Based on arXiv:2606.00157 (Gong & Xia, 2026).
---

# RG-DNN Interpretability Framework

## Core Insight

**DNN training ≈ Renormalization Group (RG) flow**: When FC DNN parameters reach optimal values after training, the characteristic parameters of the feature layer output equal the fixed points of the characteristic parameters of input data under RG for continuous fields.

## Mathematical Framework

### Exponential Family Correspondence

For data distributions in the exponential family:

```
p(x|θ) = h(x) exp(θ·T(x) - A(θ))
```

where θ are natural parameters, T(x) are sufficient statistics, A(θ) is the log-partition function.

### RG-DNN Equivalence Theorem

**Theorem**: For FC DNNs trained on exponential family data, at convergence:
- Feature layer output characteristic parameters = RG fixed points
- DNN training trajectory ≈ RG coarse-graining flow
- Feature extraction mechanism = RG decimation/decimation of irrelevant degrees of freedom

### Key Steps to Apply

1. **Identify the data distribution family** — Check if data belongs to exponential family (Gaussian, Bernoulli, Poisson, etc.)
2. **Define RG transformation** — Construct coarse-graining operator that preserves sufficient statistics
3. **Map DNN layers to RG steps** — Each hidden layer corresponds to one RG iteration
4. **Verify fixed point convergence** — Check if feature layer parameters converge to RG fixed points

## Application Patterns

### Interpreting DNN Feature Extraction

```python
# Conceptual workflow
# 1. Fit exponential family model to input data
# 2. Compute RG flow of sufficient statistics
# 3. Train DNN and extract feature layer statistics
# 4. Compare: DNN features ≈ RG fixed points
```

### Why DNNs Work — RG Perspective

- DNNs succeed because they implement RG-like coarse-graining
- Each layer progressively removes irrelevant information (like RG decimation)
- Final layer captures universal features (RG fixed points)
- Explains generalization: DNNs find the same relevant features as RG

## Connections to Quantum/Statistical Physics

- **Ising Model → DNN**: Proved equivalence for 1D Ising model (discrete), generalized to continuous exponential family
- **Gibbs States**: Connection to thermal states in quantum systems (see arXiv:2606.00239)
- **Critical Points**: DNN training near phase transitions exhibits universal scaling

## Triggers

When to load this skill:
- Interpreting deep neural network behavior
- Understanding why DNNs generalize well
- Analyzing feature extraction mechanisms
- Statistical physics approaches to ML
- Renormalization group in machine learning
- Exponential family distributions + neural networks
- Connecting physics concepts to deep learning

## References

- arXiv:2606.00157: "Interpreting FCDNNs via RG on Exponential Family" (Gong & Xia, 2026)
- arXiv:2606.00239: "Bath-induced deviations from Gibbs statistics for strongly interacting oscillators" (quantum stats connection)
