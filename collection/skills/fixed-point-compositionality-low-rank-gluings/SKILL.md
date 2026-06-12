---
name: fixed-point-compositionality-low-rank-gluings
description: Mathematical framework for compositional dynamics in threshold-linear networks via low-rank gluing rules. Use when studying modular network assembly, fixed point decomposition, compositional limit cycles, or engineering networks with predictable attractor repertoires.
license: MIT
---

# Fixed Point Compositionality via Low-Rank Gluing Rules

Mathematical theory of compositional dynamics in inhibition-dominated threshold-linear networks (TLNs) through structured modular assembly.

## Core Concept: Compositionality

Brains generate complex behaviors from stable structures with limited resources via **compositionality** - decomposing complex tasks into reusable primitives.

This work provides **first rigorous mathematical characterization** linking structural modularity to functional compositionality in nonlinear networks.

## Key Innovation: Low-Rank Gluing Rules

Novel modular network assembly connecting component subnetworks via **specific low-rank couplings**:

### Network Architecture
- Component subnetworks: arbitrary internal connectivity
- Inter-module coupling: **low-rank connections** (rank-1, rank-k)
- Inhibition-dominated dynamics: threshold-linear units

### Main Theorems

#### Theorem 1: Fixed Point Compositionality
Global fixed points constrained to **combinations of local fixed points** of constituent modules.

For low-rank gluings:
```
FixedPoints(Global) ⊆ Combinations(FixedPoints(Module₁) × FixedPoints(Module₂) × ...)
```

#### Theorem 2: Rank-1 Gluing Characterization
Complete classification determining **which combinations yield global fixed points**:
- Explicit construction rules for compositional attractors
- Predictable assembly of global dynamics from local motifs

#### Theorem 3: gCTLN Extension
Fixed point decomposition rules extended from CTLNs to **generalized CTLNs (gCTLNs)**:
- Structural rules more robust than initially posited
- Wider applicability to biological network architectures

## Applications

### 1. Combinatorial Attractor Engineering

Construct networks with **combinatorially large repertoire of predictable attractors**:
- Understanding from simpler component motifs
- Systematic design of complex dynamics

### 2. Compositional Limit Cycles

Beyond fixed points: **compositional limit cycles** emerge from gluing rules:
- Periodic dynamics from module oscillations
- Predictable timing from structural assembly

### 3. Graph-Based Networks

Extension to graph structures:
- Network topology → fixed point constraints
- Module structure → functional composition

## Mathematical Framework

### Threshold-Linear Networks (TLNs)

Dynamics governed by:
```
dx_i/dt = -x_i + [∑_j W_ij x_j + b_i]_+
```
where:
- `[·]_+` = threshold-linear nonlinearity (ReLU-like)
- `W_ij` = synaptic weights (inhibition-dominated)
- `b_i` = external inputs

### Low-Rank Coupling Structure

Inter-module connections:
```
W_inter = UV^T  (rank-k coupling)
```
where:
- `U, V` = low-rank factors
- Specific structure constrains global dynamics

### Fixed Point Decomposition

For rank-1 gluing `W_inter = uv^T`:
```
x_global = combination of {x_local(Module₁), x_local(Module₂), ...}
```
with explicit membership rules.

## Biological Relevance

### Compositional Brain Dynamics
- Modular cortical circuits → compositional computation
- Stable structure + flexible combinations
- Limited resources → efficient reuse of primitives

### Inhibition-Dominated Networks
- Realistic cortical dynamics
- Winner-take-all competition
- Fixed point stability through inhibition

### Network Assembly Rules
- Development: modules assembled via specific coupling rules
- Learning: modify low-rank factors → new compositional capabilities
- Evolution: reusable motifs across behavioral repertoire

## Implementation Guidance

### When to Use This Framework

**Trigger conditions:**
- Modeling modular neural circuits
- Engineering predictable attractor dynamics
- Studying compositionality in biological/artificial networks
- Analyzing fixed point structure of TLNs
- Designing networks with combinatorial dynamics

### Construction Workflow

1. **Identify component modules** - subnetworks with known fixed points
2. **Design low-rank coupling** - specify `U, V` factors
3. **Apply rank-1 theorem** - determine valid combinations
4. **Construct global network** - assemble with gluing rules
5. **Validate attractor repertoire** - check combinatorial predictions

### Graph-Based Application

1. **Define graph topology** - network structure
2. **Apply gCTLN rules** - fixed point decomposition
3. **Extend to generalized networks** - beyond CTLN constraints
4. **Validate robustness** - structural rule preservation

## Theoretical Significance

First rigorous proof that:
1. **Modularity → Compositionality** in nonlinear networks
2. **Low-rank structure** constrains global attractors
3. **Combinatorial dynamics** emerge from simple motifs
4. **Engineering recipe** for predictable complex networks

Bridges gap between:
- Structural modularity (observed in brain)
- Functional compositionality (behavioral flexibility)
- Mathematical characterization (predictable assembly)

## Paper Reference

**arXiv:2606.07336** (q-bio.NC)
- Author: Juliana Londono Alvarez
- 39 pages, 18 figures
- Submitted: 2026-06-05

## Related Work

- Combinatorial Threshold-Linear Networks (CTLNs)
- Attractor dynamics in recurrent networks
- Network assembly theory
- Modular circuit design

---

**Activation**: compositional dynamics, threshold-linear network, TLN, low-rank gluing, fixed point decomposition, modular network, attractor engineering, combinatorial dynamics, inhibition-dominated, gCTLN, network assembly, compositional limit cycle