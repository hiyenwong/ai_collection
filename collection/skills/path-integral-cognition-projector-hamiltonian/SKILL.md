---
name: path-integral-cognition-projector-hamiltonian
description: "A Path Integral Model of Cognition — goal-directed cognitive process as imaginary-time evolution under a projector Hamiltonian; double-bracket flow = Riemannian gradient descent on Hilbert-Schmidt cost; Wick rotation maps non-unitary descent to unitary evolution with exact discrete path-integral representation; unconscious-to-conscious continuum = system-probe interaction strength recovering GKSL decoherence. Use when modeling cognition/consciousness with quantum operators, optimizing with double-bracket flows, or deriving path-integral formulations of neural decision processes."
---

# Path Integral Model of Cognition (Projector Hamiltonian + Double-Bracket Flow)

## Paper
- **Title**: A Path Integral Model of Cognition (arXiv:2607.24807, 2026-07-10)
- **Authors**: Haruki Emori, Kazunori Kondo, Atsushi Iriki, Andrei Khrennikov
- **Categories**: q-bio.NC, cs.AI, quant-ph
- **Relation to KG**: Central node of 2026-10-05 Monday neuroscience×quantum import (degree 18, connects quantum cognition cluster: confirmation bias 2606.23325, ABS liar paradox 2609.09228, quantum logic contexts 2607.09032, supraliminal information processing 2605.25214)

## Core Methodology

### 1. Cognitive Cost Optimization as Imaginary-Time Evolution (ITE)
Goal-directed cognition is modeled as **imaginary-time evolution** under a **projector Hamiltonian** `H = P_target` that "rewards" configurations consistent with a target concept:

```
dρ/dτ = -[H, [H, ρ]]        (double-bracket flow, non-unitary)
```

- The target concept is encoded in a projector (Hilbert-Schmidt observable).
- Evolution descends the cost `C(ρ) = Tr(ρH) - (Tr(ρH))²`... equivalently minimizes distance between current belief state and target subspace.
- Unique minimum: the state fully supported on the target subspace.

### 2. Double-Bracket Flow = Riemannian Gradient Flow
The ITE coincides with a **double-bracket flow**, which is the **Riemannian gradient flow** of a Hilbert-Schmidt cost. This identification gives:
- Convergence guarantee (unique minimizer)
- Geometric interpretation: steepest descent on the spectrahedron of density matrices
- Practical algorithm: commutator-based update steps (no gradient derivation needed — the commutator IS the gradient direction)

```python
# Two verified flows (tested 2026-10-05, see test_pathintegral_skill.py):
#
# (A) Double-bracket flow dρ/dτ = -[P,[P,ρ]] under projector P:
#     -[P,[P,ρ]] == 2·(PρP - (Pρ+ρP)/2)  = 2× GKSL dissipator with jump operator P
#   → DEPHASING flow: kills coherences between target/non-target blocks,
#     PRESERVES populations (diagonal), stationary for states commuting with P.
#   This IS the paper's weak-coupling GKSL limit — unconscious processing.
for step in range(max_steps):
    comm = P @ rho - rho @ P
    rho = rho - eta * (P @ comm - comm @ P)
    rho = (rho + rho.T) / 2

# (B) Normalized imaginary-time evolution (goal-directed concentration):
#     dρ/dτ = -(Hρ+ρH)/2 + <H>ρ  with cost H = I - P_target
#   → drives support ONTO the target subspace (verified: support → 1.0).
#   This is the full ITE of the paper WITH the diffusion/kinetic projector —
#   the naive commutator iteration alone dephases but does NOT concentrate
#   (a maximally mixed belief state is stationary under (A) alone).
H_cost = np.eye(dim) - P
for step in range(max_steps):
    EH = np.trace(H_cost @ rho)
    drho = -0.5 * (H_cost @ rho + rho @ H_cost) + EH * rho
    rho = rho + eta * drho
    rho = rho / np.trace(rho)
```

### 3. Wick Rotation to Unitary Evolution + Exact Path Integral
A **Wick rotation** (τ → it) re-expresses the non-unitary descent as **equivalent unitary evolution** on the same Hilbert space, admitting an **exact discrete path-integral representation**:
- Oracle projector → potential energy term
- Initial-state diffusion projector → kinetic energy term
- Transition amplitudes factor into products of local propagators — a lattice path integral over cognitive trajectories.

### 4. Consciousness Continuum via System-Probe Interaction Strength
The **unconscious → conscious** processing continuum is identified with the **strength of unitary interaction** between:
- The cognitive system, and
- A neural-environment probe (measurement apparatus)

Two limits:
- **Weak coupling / Markovian limit** → recovers the **GKSL (Gorini-Kossakowski-Sudarshan-Lindblad) decoherence model** of Asano et al. (unconscious, gradual decoherence)
- **Strong coupling** → projective, reportable **fixation of an optimized state** (conscious report)

This unifies prior quantum-cognition models (Khrennikov, Asano-Iriki) under one path-integral umbrella.

## Reusable Patterns

### Pattern A: Projector-Hamiltonian goal encoding
Encode any goal/target concept as an orthogonal projector onto a subspace, then optimize belief state via commutator flow. Reusable for: alignment targets, concept fixation, constraint satisfaction in Hilbert space.

### Pattern B: Commutator-as-gradient (double-bracket) optimization
When optimizing over density matrices (or any spectrally-constrained manifold), the double commutator `[H,[H,ρ]]` provides a descent direction without deriving gradients. **Verified caveat (2026-10-05 test)**: under a projector target, this flow is a GKSL dephasing dissipator — it purifies coherences but is stationary on states commuting with the target. For concentration, combine with the normalized ITE term (Pattern B′). Reusable for: quantum state preparation, decoherence modeling, anytime the feasible set is a spectrahedron.

### Pattern C: Wick-rotation duality for sampling
Non-unitary descent (optimization) ↔ unitary evolution (sampling) connected by Wick rotation. Reusable for: converting variational optimization into a sampling scheme, or interpreting dissipative neural dynamics as rotations of a Hermitian equivalent.

### Pattern D: Coupling-strength continuum as phenomenology axis
Model an observable psychological phenomenon (consciousness, attention, reportability) as a function of a single continuous parameter — system-probe coupling. Reusable for: building testable continuum models where prior work posited discrete categories.

## Key Formulas

| Concept | Formula |
|---|---|
| Double-bracket flow | `dρ/dτ = -[H,[H,ρ]]`, H = target projector |
| Hilbert-Schmidt cost | `C(ρ) = ||ρ - P_target ρ P_target||²_HS` |
| Label capacity (paper) | unique minimum at ρ* with full support on target subspace |
| GKSL limit (weak coupling) | `dρ/dt = -i[H,ρ] + Σ_k γ_k (L_k ρ L_k† - ½{L_k†L_k, ρ})` |

## Implementation Checklist
1. Define target concept as projector `H` (rank-r Hermitian, H² = H).
2. Initialize belief state ρ₀ (mixed state allowed — cognition is not pure).
3. Iterate double-bracket flow with renormalization until commutator norm < tol.
4. For sampling: Wick-rotate and build discrete path integral with oracle as potential.
5. For phenomenology: sweep system-probe coupling γ; check Markovian limit matches GKSL, strong limit gives projective fixation.

## When to Use
- Quantum cognition / quantum-probability models of decision-making
- Consciousness modeling with testable operator-dynamics commitments
- Optimization over density matrices (double-bracket beats naive gradient)
- Deriving path-integral or GKSL limits of discrete cognitive models

## Related Skills
- `gksl-quantum-cognition` (GKSL master-equation cognitive psychology)
- `gskl-quantum-cognition-dynamics`
- `thermal-equilibrium-connectome` (algebraic quantum brain states)
- `harmonic-theory-behavior` (behavior spectra)
- `confirmation-bias-quantum-probability` (if later created — companion paper 2606.23325 shows the rational origin of confirmation bias in the same framework)

## Source
- arXiv:2607.24807 — Emori, Kondo, Iriki, Khrennikov (2026). "A Path Integral Model of Cognition."
