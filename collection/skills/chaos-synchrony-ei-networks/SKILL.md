---
name: chaos-synchrony-ei-networks
description: "Extended Sompolinsky-Crisanti-Sommers (SCS) theory for two-population Excitatory-Inhibitory networks with target-specific inhibition. DMFT derivation of phase diagrams showing quiescence, asynchronous chaos, persistent activity, structured chaos, and coherent oscillations. Shows target-specific inhibition determines which collective instability dominates. Activation: SCS E/I theory, DMFT neural networks, chaos-synchrony transition, E/I balance, neural phase diagram, 兴奋抑制网络混沌."
---

# Chaos to Synchrony in E/I Networks with Target-Specific Inhibition

Extended SCS framework for two-population firing-rate networks with segregated excitatory/inhibitory neurons and target-specific inhibitory couplings that break E/I balance. Uses Dynamic Mean-Field Theory (DMFT) to derive unified phase diagrams linking inhibitory architecture to large-scale dynamical regimes.

## Paper Reference

- **Title:** From Chaos to Synchrony in Recurrent Excitatory-Inhibitory Networks with Target-Specific Inhibition
- **Authors:** Carles Martorell, Rubén Calvo, Alessia Annibale, Miguel A. Muñoz
- **arXiv:** 2605.14916v1 (cond-mat.dis-nn)
- **Date:** 2026-05-14
- **PDF:** https://arxiv.org/pdf/2605.14916.pdf

## Background: SCS Theory

The seminal Sompolinsky-Crisanti-Sommers (SCS) theory showed random recurrent networks undergo a transition from quiescence to **asynchronous chaos** as connectivity strength increases:
- Random connectivity → dynamical instability → internally generated fluctuations
- Dynamic Mean-Field Theory (DMFT) became the standard framework for phase diagrams

## Extended Framework: Two-Population E/I with Target-Specific Inhibition

### Network Architecture

```
Two-population firing-rate network:
  - Excitatory population (E): N/2 neurons
  - Inhibitory population (I): N/2 neurons
  - Target-specific inhibitory couplings (β, δ):
    β: E→I inhibitory strength
    δ: I→I inhibitory strength
```

The connectivity matrix has i.i.d. entries with mean J₀/N and variance J²/N.
Parameters β, δ > 0 control relative inhibitory coupling strengths — a minimal extension that breaks E/I balance.

### Key Question

How does target-specific inhibition reorganize the SCS phase diagram?
Specifically: Can persistent activity coexist with chaos? What determines whether the system enters structured chaos vs. collective oscillations?

## DMFT Equations

The mean-field theory yields self-consistent equations for:
1. **Mean activities** Mₓ(t), Mᵧ(t) — macroscopic order parameters
2. **Autocorrelation functions** Cₓ(τ), Cᵧ(τ) — fluctuation statistics
3. **Cross-correlations** between E and I populations

These are solved self-consistently to determine phase boundaries.

## Three Qualitatively Distinct Phase Diagram Organizations

The nature of the phase diagram is classified by the dominant eigenvalue λₘ of an effective matrix M_{β,δ} determined by (β, δ):

### Type 1: Inhibition-Dominated (λₘ real and positive)
**Phases:** Quiescent (Q) → Asynchronous Chaos (AC) → Persistent Activity (PA)
- Classical SCS phenomenology preserved
- E/I network behaves like extended single-population model

### Type 2: Strictly Balanced (λₘ complex with positive real part)
**Phases:** Quiescent (Q) → Asynchronous Chaos (AC) → Coherent Oscillatory Activity (COA)
- New regime: collective oscillations emerge
- Chaos-to-oscillation transition via competition mechanism

### Type 3: Excitation-Dominated (λₘ with negative real part)
**Phases:** Quiescent (Q) → Asynchronous Chaos (AC) only
- Simple phase diagram — only disorder-driven instability

## Emergent Phases Beyond Asynchronous Chaos

### Persistent Activity (PA)
- Non-zero mean activity fixed point
- Stable when λₘ is real and positive
- Analogous to working memory states

### Structured/Synchronous Chaos (SC)
- Chaos with **non-vanishing mean activity**
- Extends synchronous chaos from single-population to E/I system
- Chaotic fluctuations around structured (non-zero) mean trajectory

### Coherent Oscillatory Activity (COA)
- **Key discovery:** Collective oscillations **suppress** chaotic fluctuations
- Transition from AC → COA reflects competition between:
  - Disorder-driven chaotic state (high-dimensional)
  - Low-dimensional collective oscillatory mode
- Deeper in oscillatory phase: collective mode fully suppresses chaos
- Mechanism reminiscent of **stimulus-induced suppression of chaos**, but here the oscillatory drive is generated **endogenously** by structured E/I feedback

## Chaos Quantification

### Largest Lyapunov Exponent (LLE)
- Positive LLE → chaotic regime
- Zero/negative LLE → non-chaotic (fixed point or periodic)
- AC-SC boundary identified by LLE analysis

### Kuramoto Order Parameter
- Measures phase synchronization across neurons
- COA regime: high Kuramoto parameter (synchronized)
- AC regime: low Kuramoto parameter (desynchronized)

## Stability Analysis

Two distinct routes out of quiescence:

### Type I: Mean-Driven Instability
- Governed by eigenvalue λₘ of M_{β,δ}
- Determines PA or COA transition
- Depends on target-specific inhibition parameters (β, δ)

### Type II: Fluctuation-Driven Instability
- Governed by autocorrelation stability condition
- Determines AC transition
- Analogous to classical SCS instability

## Phase Diagram Rescaling

After axis redefinition: (J₀/J)*, (1/gJ)* — quiescent-state stability boundaries collapse onto a common curve across different (β, δ). However, transitions between non-quiescent states depend explicitly on β and δ.

## Key Findings

1. **Target-specific inhibition reorganizes the phase diagram** — it selects which collective instability (chaotic vs. oscillatory) becomes dominant
2. **Oscillations suppress chaos** — COA transition eliminates chaotic fluctuations, not a phase of chaos around oscillatory mean
3. **Endogenous chaos suppression** — unlike stimulus-induced suppression, here the oscillatory drive is internally generated
4. **Three robust classes** of phase diagrams based on dominant eigenvalue properties of the inhibitory structure
5. **Unified DMFT framework** linking inhibitory architecture to large-scale dynamical regime organization

## Implications for Neuroscience

### Criticality Hypothesis
Cortical networks may operate near phase transitions where activity displays scale invariance and favorable computational properties. The E/I structure determines which transitions are accessible.

### Computational Regimes
- **Asynchronous chaos:** High-dimensional computation, rich internal dynamics
- **Persistent activity:** Working memory, sustained representations
- **Coherent oscillations:** Rhythmic coordination, synchronized processing
- **Structured chaos:** Complex computations with partial order

### Biological Relevance
- E/I balance breaking is ubiquitous in biological circuits
- Target-specific inhibition (different β, δ for different targets) is biologically realistic
- Phase diagram organization predicts which dynamical regimes are accessible given circuit architecture

## Mathematical Framework

### Model Equations
```
τ dxᵢ/dt = -xᵢ + Σⱼ Wᵢⱼ φ(xⱼ)
τ dyᵢ/dt = -yᵢ + Σⱼ W'ᵢⱼ φ(yⱼ)
```

Where W, W' are random connectivity matrices with E/I structure.

### DMFT Self-Consistency
```
Mₓ(t) = ∫ D[z] φ(√qₓ z + Mₓ(t))
Cₓ(τ) = ∫∫ Dz Dz' φ(·) φ(·)
```

With appropriate self-consistency conditions on qₓ, qᵧ.

## Applications

1. **Cortical circuit modeling:** Understanding E/I balance in cortical dynamics
2. **Neural computation theory:** Linking circuit architecture to computational regimes
3. **Brain state transitions:** Modeling transitions between dynamical regimes
4. **Neuromorphic design:** Architecture-guided dynamical regime selection
5. **E/I balance disorders:** Modeling pathological dynamics in schizophrenia, epilepsy

## Activation Keywords

- E/I network SCS theory
- chaos-synchrony transition
- DMFT neural networks
- target-specific inhibition
- E/I balance breaking
- neural phase diagram
- asynchronous chaos
- coherent oscillations
- structured chaos
- 兴奋抑制网络混沌理论

## Related Skills

- `ei-network-chaos-synchrony-theory` — Existing SCS E/I theory skill
- `neural-population-dynamics` — Neural population analysis methods
- `neural-critical-dynamics-theory` — Critical dynamics theory

## Limitations

- Firing-rate model (not spiking neurons)
- Random connectivity (not structured biological connectivity)
- Two-population simplification
- Mean-field approximation (thermodynamic limit N→∞)
- No external input dynamics considered

## Future Directions

1. Spiking neuron version of the framework
2. Structured (non-random) connectivity patterns
3. Multi-population extensions (>2 populations)
4. External input / sensory-driven dynamics
5. Learning rules that adapt (β, δ) dynamically
