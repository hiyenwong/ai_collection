---
name: quantum-like-cognition-gksl
description: >
  Research skill for the paper "Quantum-Like Models of Cognition and Decision Making:
  Open-Systems and Gorini-Kossakowski-Sudarshan-Lindblad Framework" (arXiv:2604.18643)
  by Masanari Asano and Andrei Khrennikov (2026). Covers quantum-like modeling of
  cognitive dynamics using the GKSL master equation, density matrix evolution,
  Lindblad operators, and applications to decision-making under uncertainty, order
  effects, and contextual influences on mental states.
activation_triggers:
  - quantum cognition
  - GKSL
  - GKSL master equation
  - decision making
  - open quantum systems
  - cognitive dynamics
  - quantum-like models
  - Lindblad equation
  - density matrix cognition
  - order effects
  - quantum probability
  - cognitive psychology
  - mental state evolution
paper:
  title: "Quantum-Like Models of Cognition and Decision Making: Open-Systems and Gorini–Kossakowski–Sudarshan–Lindblad Framework"
  authors:
    - Masanari Asano
    - Andrei Khrennikov
  published: 2026-04-19
  arxiv: "2604.18643"
  categories:
    - q-bio.NC
    - quant-ph
---

# Quantum-Like Models of Cognition: GKSL Framework

## Paper Overview

This paper surveys the evolution of quantum-like models of cognition and decision making, transitioning from **static kinematic representations** to a robust **dynamical framework** based on open quantum systems theory. The authors apply the Gorini-Kossakowski-Sudarshan-Lindblad (GKSL) master equation to model cognitive dynamics, providing a unified mathematical treatment connecting quantum probability with cognitive psychology phenomena.

### Key Thesis

Traditional quantum-like cognitive models used static quantum probability (e.g., Born rule, state superposition) to explain behavioral anomalies. This paper advances the field by introducing **dynamical open-system models** where mental states evolve continuously under environmental interaction, described by the GKSL master equation.

---

## Core Methodology: GKSL Master Equation for Cognitive Dynamics

The central methodological contribution is the application of the **GKSL (Lindblad) master equation** to describe the time evolution of a cognitive agent's mental state as an open quantum system interacting with its environment (context):

$$
\frac{d\rho(t)}{dt} = -i[H, \rho(t)] + \sum_k \gamma_k \left( L_k \rho(t) L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \rho(t)\} \right)
$$

Where:
- **ρ(t)** — density matrix representing the cognitive state at time *t*
- **H** — Hamiltonian governing unitary (internal) cognitive dynamics
- **L_k** — Lindblad operators encoding environmental/contextual interactions
- **γ_k** — dissipation rates controlling the strength of contextual influence

### Transition from Static to Dynamical Models

| Feature | Static Models | GKSL Dynamical Models |
|---|---|---|
| State representation | Fixed state vector \|ψ⟩ | Time-dependent density matrix ρ(t) |
| Evolution | None (or unitary only) | Continuous, governed by GKSL equation |
| Context | Embedded in initial state | Dynamically coupled via Lindblad operators |
| Decoherence | Not modeled | Naturally emerges from open-system dynamics |
| Predictions | Point estimates | Time-dependent probability distributions |

---

## Mathematical Framework

### 1. Density Matrix Representation

The cognitive state is represented as a **density matrix** ρ on a Hilbert space H:

- **Pure states**: ρ = |ψ⟩⟨ψ| (agent has a definite mental disposition)
- **Mixed states**: ρ = Σ_i p_i |ψ_i⟩⟨ψ_i| (agent is in a superposition or statistical mixture of mental states)

The density matrix framework naturally handles:
- **Incompatibility** of mental observables (non-commuting operators)
- **Interference effects** in judgment and perception
- **Contextuality** of cognitive measurements

### 2. Hamiltonian (H) — Internal Cognitive Dynamics

The Hamiltonian H governs the **unitary evolution** component, representing intrinsic cognitive processes:
- Belief updating and deliberation
- Information integration across mental dimensions
- Rotational dynamics in belief space

### 3. Lindblad Operators (L_k) — Contextual Coupling

Lindblad operators model the interaction between the cognitive system and its environment/context:

- **Decision context** (framing effects, presentation order)
- **Social influence** (group pressure, normative information)
- **Environmental stimuli** (cues, priming, anchoring)
- **Memory and learning** (feedback from past decisions)

Each L_k captures a specific channel of contextual influence with associated rate γ_k.

### 4. Decoherence and Relaxation

The GKSL framework naturally produces:
- **Decoherence**: Loss of quantum-like coherence in mental states over time, transitioning from superposition to classical mixture
- **Relaxation**: Convergence to a steady-state (attractor) representing a stable belief or decision
- **Dissipation**: Energy/information exchange with the environment

These phenomena model:
- How initial indecisiveness resolves into a decision
- How context gradually shapes preferences
- How order effects diminish or accumulate over sequential evaluations

---

## Key Technical Contributions

### 1. Unified Dynamical Framework
Provides a single mathematical formalism (GKSL equation) that unifies multiple quantum-like cognitive phenomena previously treated separately.

### 2. Open-Systems Modeling of Cognition
Treats the cognitive agent as an **open system** coupled to context/environment, moving beyond closed-system (unitary-only) quantum models that cannot capture irreversible cognitive processes.

### 3. Modeling Order Effects in Sequential Measurements
The framework reproduces **question-order effects** observed in surveys and psychological experiments (e.g., Clinton-Gore order effect) as a natural consequence of state collapse and dynamical evolution under the GKSL equation.

### 4. Decision-Making Under Uncertainty
Models the **deliberation process** as a dynamical trajectory in state space, where:
- Initial state represents the agent's a priori mental disposition
- GKSL evolution under context drives the state toward a decision
- Measurement (response) collapses the state

### 5. Contextual Influence Formalization
Context is not a static backdrop but a **dynamical coupling** formalized through Lindblad operators, enabling:
- Quantitative prediction of framing effects
- Modeling of how context strength (γ_k) modulates decision outcomes
- Time-dependent analysis of contextual influence

### 6. Connection to Quantum Probability
The framework bridges the **Born rule** (static probability) with **dynamical probability distributions** that evolve as the cognitive state evolves under the GKSL equation.

---

## Applications in Cognitive Modeling

### Decision Making Under Uncertainty
- Model how agents deliberate and converge to choices under ambiguity
- Capture violation of sure-thing principle and other classical decision anomalies
- Represent Allais and Ellsberg paradox-type behaviors dynamically

### Order Effects in Sequential Judgments
- Reproduce question-order effects in survey responses
- Model how answering one question changes the mental state for the next
- Quantify the magnitude of order effects via trace distance between state sequences

### Context-Dependent Preferences
- Model framing effects (gain vs. loss framing)
- Capture how social context shifts preference distributions
- Represent priming and anchoring as Lindblad-mediated state preparation

### Perception and Categorization
- Model ambiguous figure perception (e.g., Necker cube) as oscillatory dynamics
- Represent categorization as measurement on a prepared cognitive state
- Capture interference effects in similarity judgments

### Memory and Learning
- Model memory retrieval as a measurement process with back-action
- Represent learning as environmental coupling modifying the Hamiltonian
- Capture forgetting as decoherence of stored quantum-like information

### Behavioral Economics
- Model bounded rationality as constrained quantum-like dynamics
- Represent preference reversals as state transitions
- Capture violations of utility theory through non-commutative mental observables

---

## Key Concepts for Reference

| Concept | Quantum Analogue | Cognitive Interpretation |
|---|---|---|
| State vector \|ψ⟩ | Wavefunction | Mental state / belief state |
| Density matrix ρ | Statistical operator | Probabilistic mental disposition |
| Hamiltonian H | Energy operator | Internal cognitive dynamics |
| Lindblad operator L_k | Decoherence channel | Contextual / environmental influence |
| Measurement | State collapse | Decision / response / judgment |
| Superposition | Coherent state | Ambivalence / indecisiveness |
| Decoherence | Loss of coherence | Resolution of ambivalence |
| Non-commutativity | [A,B] ≠ 0 | Order dependence of questions |
| Entanglement | Correlated states | Association between mental concepts |
| Pure state | \|ψ⟩⟨ψ\| | Definite mental disposition |
| Mixed state | Σ p_i \|ψ_i⟩⟨ψ_i\| | Uncertain / conflicted mental state |

---

## Related Work and References

- **Pothos & Busemeyer (2013)**: Quantum models of cognition and decision
- **Busemeyer & Bruza (2012)**: Quantum models of cognition
- **Khrennikov (2010)**: Ubiquitous quantum structure in cognition
- **Asano et al.**: Previous work on quantum-like modeling of decision making
- **Gorini, Kossakowski, Sudarshan (1976)**: Original GKSL theorem
- **Lindblad (1976)**: Generators of quantum dynamical semigroups

---

## Practical Usage Guidelines

### When to Apply This Framework
- Modeling **time-dependent** cognitive phenomena (deliberation, preference formation)
- When context is **dynamic** rather than static
- When **order effects** are central to the phenomenon
- When modeling **irreversible** cognitive processes (decisions, learning)
- When classical probability models fail to capture observed behavioral patterns

### Limitations and Considerations
- The quantum-like approach is **mathematical/formal**, not claiming physical quantum processes in the brain
- Parameter identification (γ_k, H, L_k) requires experimental data fitting
- The framework is agnostic to neural implementation details
- Interpretational questions remain about the ontological status of the "mental Hilbert space"

---

*Skill based on arXiv:2604.18643 — Asano & Khrennikov (2026)*
