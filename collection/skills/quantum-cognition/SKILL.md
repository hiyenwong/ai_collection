---
name: quantum-cognition
description: >
  Quantum cognition methodology for modeling cognitive processes using quantum probability theory.
  Combines neuroscience insights with quantum information formalism to model decision making,
  context-dependent reasoning, mental state dynamics, and non-classical cognitive correlations.
  Use when: (1) modeling cognitive phenomena that violate classical probability (order effects,
  conjunction fallacy), (2) building quantum-like models of decision making, (3) analyzing
  contextuality in mental representations, (4) designing quantum neural architectures for
  brain-inspired computing, (5) studying quantum effects in biological systems (radical-pair
  mechanism, cryptochrome), (6) implementing quantum photonic neural networks for neuromorphic
  computing.
---

# Quantum Cognition

Model cognitive processes using quantum probability theory and quantum information formalism.
This methodology spans two interpretations: quantum-like cognition (informational) and physical
quantum brain hypotheses.

## Two Paradigms

### 1. Quantum-Like Cognition (Informational)

Uses quantum formalism to model cognition without claiming quantum processes in the brain.
Based on Khrennikov's framework: mental contexts induce non-classical correlations analogous
to quantum entanglement. Key insight: incompatible measurements arise naturally from
context-dependent mental representations.

**When to use**: decision making, judgment under uncertainty, concept combinations,
cognitive biases, order effects in survey responses.

### 2. Physical Quantum Brain Hypotheses

Proposes actual quantum coherence in biological substrates. Wakaura (2026) evaluates CQEC
(covariant quantum error correction) in radical-pair proteins MAO-A and cryptochrome.
Key finding: CQEC can maintain coherence over 200ms behavioral windows, but layer-protein
tradeoffs exist — no single protein optimizes all layers.

**When to use**: biophysical modeling of neural processes, radical-pair mechanism analysis,
quantum error correction in biological systems.

## Core Mathematical Framework

### Quantum Probability Model

Replace classical Kolmogorov probability with quantum probability:

```python
import numpy as np

def quantum_probability(state_vector, projector):
    """P(outcome) = |<outcome|state>|^2 = ||projector @ state||^2"""
    return np.abs(np.dot(projector, state_vector))**2

def interference_effect(p_A, p_B, theta):
    """Classical: p = p_A + p_B
       Quantum: p = p_A + p_B + 2*sqrt(p_A*p_B)*cos(theta)"""
    return p_A + p_B + 2 * np.sqrt(p_A * p_B) * np.cos(theta)
```

### Contextuality Detection

Bell-CHSH inequality violation indicates non-classical correlations:

```python
def chsh_inequality(E_ab, E_ab_prime, E_a_prime_b, E_a_prime_b_prime):
    """|S| = |E(ab) - E(ab') + E(a'b) + E(a'b')| <= 2 (classical)
       Quantum bound: |S| <= 2*sqrt(2) (Tsirelson bound)"""
    S = abs(E_ab - E_ab_prime + E_a_prime_b + E_a_prime_b_prime)
    return S, S > 2.0, S <= 2 * np.sqrt(2)
```

### Cognitive State Evolution

Mental states evolve via unitary transformations (closed system) or Lindblad dynamics (open system):

```python
from scipy.linalg import expm

def mental_state_evolution(H, psi_0, t):
    """|psi(t)> = exp(-iHt)|psi(0)> — unitary evolution"""
    U = expm(-1j * H * t)
    return U @ psi_0
```

## Quantum Photonic Neural Networks (QPNN)

Boras Vazquez et al. (2026): time-bin-encoded QPNN for quantum information processing.

Key architectural insight: time-encoded networks use constant number of photonic elements
regardless of size/depth, enabling scaling. Trained via realistic nonlinearities (quantum
dot + waveguide) to achieve 0.96+ fidelity Bell-state analysis.

```python
def qpnn_architecture(n_modes, depth, nonlinearity="kerr"):
    """Time-bin QPNN: same elements regardless of network depth.
    Layers: (1) time-delay interferometer, (2) phase shifters,
    (3) nonlinear element (Kerr or quantum dot scattering)"""
    # Each time step processes one mode through same physical elements
    # Complexity: O(n_modes * depth) elements, not O(n_modes * depth) physical components
    return {
        "encoding": "time-bin",
        "elements": "constant with depth",
        "nonlinearity": nonlinearity,
        "fidelity": ">0.96 (realistic), >0.99 (time-gated)"
    }
```

## Quantum Error Correction in Biological Systems

CQEC protocol for radical-pair proteins:

1. **Three-layer architecture**: nuclear spin memory → electron spin interface → electrochemistry
2. **Coherence preservation**: CQEC extends T2 coherence beyond decoherence rate
3. **Layer-protein tradeoff**: CRY has longer T2 (52ms) but shorter T1 (0.53ns); MAO-A has opposite
4. **Behavioral threshold**: 200ms Schultze-Kraft veto window is the minimum coherence requirement

## Decision Making Patterns

### Order Effects

```
P(A then B) ≠ P(B then A) — classical commutativity violation
Quantum: P(A then B) = ||P_B P_A |psi>||^2 ≠ ||P_A P_B |psi>||^2
```

### Conjunction Fallacy

Linda problem: P(bank teller AND feminist) > P(bank teller)
Explained by quantum interference between mental representations.

### Disjunction Effect

Violation of sure-thing principle in decision making under uncertainty.
Traditionally modeled via quantum interference term in probability calculation.

**Updated (2026-06-29)**: arXiv:2603.23233 proves that a classical probability model
with continuous expectation parameter partitioning reproduces the disjunction effect exactly.
Classical and quantum-like models have identical observable expressiveness — their
substantive difference is ambiguity representation (expectation partitions vs quantum
superposition states), not probability law violation. **Key insight**: when comparing
classical vs quantum-like decision models, the disjunction effect alone cannot distinguish
them; look for structural differences in event semantics instead.

See `classical-disjunction-effect-model` skill for the full classical model.

## Application Workflow

1. Identify classical probability violation in cognitive data
2. Construct quantum state space (Hilbert space dimension = number of distinguishable outcomes)
3. Define mental state vector and measurement projectors
4. Fit interference parameters to empirical data
5. Validate with contextuality tests (Bell-CHSH, Leggett-Garg inequalities)
6. Predict novel effects (order reversal, compatibility effects)

## Key Findings from Literature

- **CQEC coherence**: 0.83 at decoherence rate 0.19 (6.9x improvement over uncorrected)
- **QPNN fidelity**: 0.96 with realistic nonlinearity, 0.99+ with time gating
- **Contextuality**: Mental markers exhibit quantum-like incompatibility without physical quantum processes
- **Layer tradeoff**: No single radical-pair protein optimizes both T1 and T2 coherence times

## References

See `references/` for detailed mathematical derivations and implementation guides.

### Confirmation Bias as Optimal Evidence (arXiv:2606.23325)
- **Skill**: `confirmation-bias-quantum-probability`
- Confirmation bias emerges from optimal evidence selection on square-root probability space
- Sequential hypothesis testing: minimum memory capacity + exponential error reduction
- Active inference (max info) = error-minimizing evidence choice

### Classical Disjunction Effect Model (arXiv:2603.23233)
- **Skill**: `classical-disjunction-effect-model`
- Classical model reproduces disjunction effect without violating law of total probability
- Introduces continuous expectation parameter replacing certainty-only premise
- Classical and quantum-like models have equal observable expressiveness

### Recent Papers (2026)
- arXiv:2601.10588 - *Searching for Quantum Effects in the Brain: A Bell-Type Test for Nonclassical Latent Representations in Autoencoders* → See `quantum-nonclassicality-latent-test` skill
- arXiv:2605.23943 - *Spacetime Formation under Requirements: Contextual Realization and Form-Dependent Probability* (quantum cognition as fixed-spacetime projection)
- arXiv:2605.29877 - *Verifying Adversarial Robustness in QML* → See `qml-adversarial-robustness-verification` skill
- arXiv:2605.29557 - *Quantum Subliminal Learning* → See `quantum-subliminal-learning` skill
- arXiv:2605.24152 - *Neuro-Inspired Inverse Learning for Planning and Control* → See `neuro-inspired-inverse-learning` skill

**Overlap alerts**: 
- `confirmation-bias-quantum-probability` (2606.23325) and `quantum-like-associative-benchmark-adaptive` (2606.12449) both address quantum probability models of cognitive biases — candidate for consolidation.
- `quantum-opinion-dynamics-networks` (2607.01452) ↔ `quantum-probability-statistics` — both use density matrix formalism for non-classical correlations.

### Quantum Opinion Dynamics on Networks (arXiv:2607.01452)
- Cognitive states as density matrices in networked multi-agent systems
- Each agent's cognitive state = density matrix encoding expressed opinion + cognitive ambivalence
- Survey questions = non-commuting self-adjoint operators → principled explanation for order effects
- Under product state approximation, reduces to classical Friedkin-Johnsen opinion model
- Quantum coherence decays exponentially at network-independent rate; pairwise correlations converge to network-independent steady state
- **Activation**: "quantum opinion dynamics", "quantum social networks", "density matrix opinion", "cognitive ambivalence network"

### Tensor Network Emotional Memory (arXiv:2606.28470)
- **Skill**: `quantum-emotional-memory-tensor-networks`
- Tensor networks model order-dependent emotional memory in children (77.98% accuracy)
- Emotional valence influences memory for adjacent items in a sequence
- Quantum-inspired method (not strictly quantum cognition) for order-dependent phenomena
- Novel task protocol for exploring emotional temporal memory in children

### Quantum Structure in AI Language (arXiv:2511.21731)
- **Skill**: `quantum-structure-in-ai-language`
- LLMs violate Bell inequalities in conceptual combination tests (ChatGPT, Gemini)
- Word distributions follow Bose-Einstein statistics, not Maxwell-Boltzmann
- Evolutionary convergence: quantum-like meaning organization emerges in both human and artificial cognition
- Key insight: meaning-bearing vector spaces exhibit quantum organization regardless of physical substrate
- Extends quantum cognition from human to artificial intelligence
- See `references/quantum-structure-in-ai-language.md` for detailed analysis

### Self-Modulating QFWP with Bounded Memory (arXiv:2607.02363)
- Quantum Fast-Weight Programmers store temporal info in circuit parameters, not recurrent hidden states
- Unbounded self-modulating QFWP diverges on long sequences; bounded variant uses sign-preserving tanh gate on recurrent memory branch
- Old-state modulation is key mechanism for improvement over standard QFWP
- **Activation**: "quantum fast weight", "QFWP", "bounded memory gate", "quantum sequence modeling"
- **Related skill**: `quantum-fast-weight-memory-gates`

### XOR Games and Nonlocal Game Complexity (arXiv:2607.06876)
- **Skill**: `tilted-xor-games`
- Tilted XOR games (winning condition depends on XOR + one output bit) are RE-complete for quantum value approximation
- Standard XOR games are polynomial-time approximable; the single-bit extension creates dramatic complexity gap
- Classical complexity unchanged (both NP-complete) — the separation is purely quantum
- **Relevance to cognition**: Nonlocal games provide the mathematical foundation for contextuality tests (Bell-CHSH) used in quantum cognition. Tilted XOR results inform the limits of quantum vs classical cognitive model expressiveness.
- **Related skill**: `quantum-opinion-dynamics-networks` (density matrix formalism for networked cognition)
