---
name: emotions-intrinsic-colored-noise
description: "Use when modeling emotion-driven decisions or affective networks. Emotions as colored noise framework."
category: ai_collection
tags: [neuroscience, decision-theory, colored-noise, affective-computing, biological-networks, dynamical-systems]
---

# Emotions as Intrinsic Colored Noise in Biological Systems

Methodology from arXiv:2609.25970 (Yukalov & Yukalova, 2026, JINR Dubna / USP São Carlos, physics.soc-ph).

**Core thesis**: Emotions in biological networks (neuronal networks, animal/human societies, affective AI nodes) are mathematically analogous to *intrinsic colored noise* superimposed on rational decision-making. Unlike white noise, colored noise has non-uniform distribution over attraction factors with nonzero most-probable values — hence average emotional bias is measurable and systematic.

## Framework: Quantum-Probability-Inspired Decision Model

### 1. Probability decomposition (Axiom 5 — core additivity)

The probability of choosing alternative π_j decomposes additively:

    p(π_j) = f(π_j) + q(π_j)

- **f(π_j)** — utility factor: probability of rational choice (Kolmogorov measure over alternative lattice, normalized Σf=1)
- **q(π_j)** — attraction factor: emotional bias, range −1 ≤ q ≤ 1, NOT required to sum to zero (this is what makes the noise "colored")
- Limiting consistency: p → f when emotions vanish (q → 0)

The alternative set π = {π₁...π_N} forms a **complete lattice** ordered by probabilities, with linear order, transitivity, minimal/maximal elements.

### 2. Utility factor from information theory (Shore-Johnson)

Utility factors are derived by minimizing a Kullback-Leibler information functional under normalization + uniqueness constraints:

    f(π_j) ∝ prior(π_j) · exp(β·U_j)

with **belief parameter β** and Luce-rule trial distribution over value-function attributes U_j (vNM expected utility or any value function). Semi-positive and negative utilities handled by separate attribute mappings.

### 3. Attraction factors and the "quarter law"

Average attraction factors follow the **quarter law** (empirical regularity from quantum decision theory):

    ⟨q⟩ = ±1/4  (positive emotions: +1/4; negative emotions: −1/4)

Aggregate probabilities:
    p(π_j) = f(π_j) ± 1/4, retracted to [0,1] via retraction mapping (Eq. 15)

**Colored noise definition**: attraction factors are random variables with agent/time-varying distributions, but with *nonzero most-probable values* — that is the color. White noise would give ⟨q⟩=0 uniformly.

### 4. Network dynamics: information exchange + imitation

After individual decisions (initial condition), agents exchange information and imitate → coupled opinion dynamics. Groups are indexed by memory type:

- **Long-range memory agents**: fractional/power-law memory kernels (heterogeneous society)
- **Short-range memory agents**: standard exponential memory
- **Super-rational agents**: q ≡ 0, pure utility (emotionless reference class)

Decision-probability dynamics couple groups through information gain terms and imitation strength. Time measured in units of information-exchange time.

## Dynamic Regimes (Eight Types of Operation)

Classification via dynamical-systems fixed-point analysis of the two-group system (p₁ = long-range memory group, p₂ = short-range memory group):

1. **Node + Node** — both groups converge to stable fixed points (different if initial attraction signs differ; coinciding if same sign)
2. **Node + Focus** — group 1 → node, group 2 → damped oscillations (agent "hesitations")
3. **Node + Limit cycle** — persistent oscillations in group 2
4. **Focus + Focus** — both oscillate and damp
5. **Focus + Limit cycle** — mixed
6. **Limit cycle + Limit cycle** — both oscillate persistently
7. **Node + Chaotic attractor** — chaos in one group
8. **Chaotic + Chaotic** — **strong imitation effect produces chaotic decision evolution** (key finding)

**Design rule**: imitation strength is the bifurcation control parameter — strong imitation → chaos in decision evolution, even with all-rational utility inputs.

## Ellsberg Paradox Resolution (validation case)

Classic Ellsberg urn paradox (uncertainty aversion violating expected utility) dissolves naturally:
- Uncertain lottery gets negative emotion → q(A₂) = −1/4
- Certain lottery gets positive emotion → q(A₁) = +1/4
- Then p(A₁) > p(A₂) for BOTH red-payoff and black-payoff questions with NO contradiction — because probabilities are not forced through a single expected-utility ranking.
- Dynamics version: with information exchange, the preference gap widens/narrows depending on imitation strength — measurable in opinion-dynamics experiments.

## When to Use

- Modeling affective decision-making where emotional bias must be *quantified*, not just described
- Multi-agent social/neuronal network simulations needing heterogeneous agent classes (memory types, emotion/no-emotion)
- Resolving "irrational" choice paradoxes (Ellsberg, Allais) without abandoning probability formalism
- Designing affective AI: emotion as a *tunable colored-noise channel* on top of rational policy — ⟨q⟩ is the tuning knob
- Neuronal population decision models: intrinsic noise is empirically documented (Werner-Mountcastle, Gold-Shadlen); this framework gives it emotional semantics

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Choice probability | p = f + q (additive emotion) |
| Utility factor | f ∝ prior·exp(βU) (KL minimization) |
| Mean attraction | ⟨q⟩ = ±1/4 (quarter law) |
| Aggregate prob | p = f ± 1/4, retracted to [0,1] |
| Imitation → chaos | strong imitation ⇒ chaotic decision trajectories |

## Reusable Patterns

1. **Additive affect decomposition**: any probabilistic choice model can be extended with a bounded attraction term q ∈ [−1,1] without breaking normalization (use retraction mapping)
2. **Heterogeneous memory groups**: long-range (fractional) vs short-range (exponential) memory kernels as agent classes — directly applicable to SNN/neuromorphic societies
3. **Imitation-as-bifurcation-parameter**: treat social coupling strength as chaos control knob; scan it to map regime boundaries
4. **Emotionless reference class**: include super-rational agents as experimental control group within the same network

## Limitations

- Attraction-factor distributions are phenomenological (quarter law is empirical, not derived)
- Lattice structure assumes finite, discrete alternatives
- Dynamics validated numerically for 2-3 groups only; scalability to large networks open

## Source

- arXiv:2609.25970 — Yukalov & Yukalova, "Emotions as intrinsic colored noise in biological systems" (22 Sep 2026)
- Related: [[llm-emotion-dynamics-decoding]], [[eeg-hopfield-emotion-energy-landscapes]], [[hormone-t5-emotion-layer]]
