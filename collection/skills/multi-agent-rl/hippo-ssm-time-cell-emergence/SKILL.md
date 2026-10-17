---
name: hippo-ssm-time-cell-emergence
description: "Use when modeling time cells, ramping, oscillations as preconfigured basis. HiPPO SSM rotations generate them before training."
tags: [neuroscience, state-space-models, time-cells, hippocampus, computational-neuroscience]
category: ai_collection
---

# State Space Models Naturally Produce Time Cell and Oscillatory Behaviors and Scale to Abstract Cognitive Functions

**Source**: Sen Lu, Xiaoyu Zhang, Mingtao Hu, Eric Yeu-Jer Lee, Soohyeon Kim, Wei D. Lu (University of Michigan, EECS), arXiv:2507.13638 v4 (revised 14 Oct 2026), q-bio.NC + cs.LG.

## Core Claim

HiPPO-initialized diagonalized SSMs (S5-style, complex-valued Λ) are **mathematically sufficient and computationally plausible** to generate time cells, ramping activity, and oscillatory responses — even **before any training**. The multi-timescale complex rotational basis acts as a structural prior for optimal history compression; learning then exploits and adapts this pre-existing basis (input matrix B and readout C change; state-transition Λ barely moves) instead of constructing temporal codes de novo. This mirrors preconfigured intrinsic dynamics observed in biological circuits and human brain organoids (van der Molen et al.), and scales to abstract cognitive functions like event/lap counting with linearly separable state geometry.

## Mechanism Map

**1. Rotational basis → temporal response profiles**
- LTI SSM: h'(t) = Ah(t) + Bx(t), y(t) = Ch(t); diagonalized with complex Λ, discretized: h(t+Δt) = Λ̄h(t) + B̄x(t), Λ̄(Δt) = exp(ΛΔt).
- During delays (no input), each state evolves as h_i(t+1) = λ̄_i h_i(t); the network learns |λ̄_i| = 1 — pure rotation in the complex plane.
- **Unification**: time cell vs ramping cell are not distinct biological entities but different phases/projections of rotations onto the real axis. A rotation crossing the positive real axis mid-delay = time cell; a half-turn from +1 to −1 = ramping (up or down). Same math, different manifestation — matching biological reports that these classes co-emerge.
- HiPPO = optimal projection of continuous history onto orthogonal (Legendre) polynomial basis; the complex-diagonal variant provides the multi-timescale frequency ladder.

**2. Emergent cell census (three-stimuli temporal discrimination, actor-critic RL)**
- Task: identify the longest of 3 sequential stimuli (harder than the 2-stimuli ceiling task in prior LSTM work), with intermediate reward for the longer of the first two (dopamine-timing analogy). SSM output thresholded to spikes (surrogate gradient, sigmoid-shaped) feeding value/policy nets.
- Accuracy 88.1 ± 1.9% (10 seeds). Emergent census across 5000 episodes: **21.0% time cells, 61.8% ramping cells**, plus preserved high-frequency oscillatory modes (lesion studies show high-frequency units less critical for this task).

**3. Structural vs learned dissociation (the key experiment)**
- HiPPO-init vs random-init SSMs reach comparable accuracy, but dynamics differ drastically: HiPPO shows sequential time-cell structure **at initialization** (before training); random init produces unstructured high-entropy dynamics **even after extensive training**.
- Parameter plasticity (|θ_final − θ_init|/|θ_init|): HiPPO Λ changes ≈ 0.093 ± 0.003 vs random Λ ≈ 1.154 ± 0.038 (**12.4× less**); B and C change substantially in both (~1.0–2.2) — learning reconfigures input projection + readout, not the oscillatory basis.
- Freeze Λ & B, train readout only: HiPPO holds 50.4 ± 3.5% vs random collapse to 34.1 ± 2.3% — the basis quality, not plasticity, carries decodable temporal information.

**4. Retiming/remapping without retraining**
- Train on 30-step delay → test on 100-step delay with ALL parameters frozen: time-cell sequences don't reset; oscillatory modes continue rotating and tile the extended interval (units re-sorted by new peak times; indices NOT one-to-one — matching hippocampal population **remapping** rather than stretching, Taxidis et al.).
- Retrain ONLY the linear readout (Λ, B frozen): accuracy rapidly restores. Random-init network: chance-level at extended delay and fails to recover. HiPPO advantage grows with delay length.

**5. Scale-up to abstract cognition: lap counting**
- Repeating running sequence + landmark cue; agent must increment an internal lap counter (inspired by Sun et al. mouse hippocampus lap-event coding). 100.0% accuracy over 4 laps; normalized edit-distance score 0.999.
- Time-cell cascades re-emerge and reset within EVERY lap; yet lap identity (count) is **linearly separable** in state space (linear SVC near-perfect on held-out, LDA decision regions partition laps) — the rotational dynamics unroll repeated sensory streams into distinct state-space locations, so abstract count needs only a linear readout.
- Handles randomized lap durations (10–60 steps), 0–2 random pauses (0–25 steps), and extrapolates beyond 6 laps.

**6. Biological plausibility anchors**
- Complex-valued states = conjugate pairs of real variables — satisfies the minimum 2D requirement for oscillation (HH-model reduction: 1D is over-damped, cannot resonate).
- Aligns with: intrinsic sequential firing in CA1/CA3 without EC input (Heys & Dombeck); preconfigured dynamics independent of sensory experience; SMA/striatum/pre-SMA periodic state-space trajectories in timing tasks.
- Evolutionary framing: intrinsic dynamics as **meta-learned initialization** — proposed test: evolve SSM populations selecting only for memory capacity, check convergence toward HiPPO-like structures.

## Reusable Analysis Patterns

1. **Pre-config vs learned probe**: initialize with a structured basis (HiPPO) vs random; compare (a) pre-training dynamics structure, (b) post-training accuracy, (c) per-parameter-block relative change |Δθ|/|θ_init|, (d) frozen-internal/readout-only retraining. A 10×+ plasticity gap in the state-transition block is the signature of basis exploitation.
2. **Time/ramping cell classification** (Shikano et al. criteria): trial-averaged tuning curves → linear regression fit (ramp: p≤0.05 & Pearson ≥0.9) → Skaggs temporal information with ramp-subtracted residual (time cell: >99th percentile of 100 shuffles) → even/odd trial reliability check.
3. **Two-stage heatmap sorting**: group units by oscillatory frequency (local-maxima count above prominence threshold), then order by peak latency within group — separates low-frequency time cells from the high-frequency basis tail.
4. **Retiming test for temporal models**: extend delay 3× with frozen weights, re-sort by new peaks; one-to-one index correspondence ⇒ stretching; remapped indices ⇒ biological remapping analog.
5. **Abstract-variable separability**: randomize per-episode durations so absolute time can't aid decoding; decode at matched timesteps with linear SVC/LDA — linear separability of count/identity indicates the recurrence (not the readout) structures the abstraction.

## Caveats & Limitations (author-stated)

- Tasks may not fully exploit model capacity (random-init nets also reach high accuracy — tasks solvable by naïve designs).
- HiPPO is ONE of a class of suitable initializations; no biological guarantee the brain uses this specific orthogonal basis.
- Microarchitecture abstracted away (no hippocampal cell-type heterogeneity); inputs are artificially encoded, not real spiking data. Frequency spectrum vs biological bands (theta/gamma) not yet quantified.
- Framework offers sufficiency + plausibility, NOT proof that evolution produced an equivalent basis.

## Related Skills

- [[temporal-representation-degree-neural-networks]] — design/analysis space of temporal representations
- [[mamba-spike-population-forecaster]] — SSM + spike decoding
- [[preconfigured-brain-dynamics]] — preconfigured dynamics in organoids (related literature)
- [[ctm-fixed-point-curve-non-normal-thought]] — recurrent thought as moving fixed points (same-day companion analysis)

## Key References

- Darlow et al. 2025 (CTM); Gu et al. HiPPO; Smith et al. S5
- van der Molen et al. (human brain organoid intrinsic sequences); Taxidis et al. (hippocampal remapping); Sun et al. (lap-event coding); Heys & Dombeck (CA1 intrinsic sequences); Lin et al. (DRL time cells); Shikano/Mello (classification criteria); Skaggs (temporal information)

## Activation

state space model, HiPPO, time cells, ramping cells, oscillatory dynamics, complex rotation, temporal basis, preconfigured dynamics, remapping, retiming, lap counting, event counting, hippocampus, actor-critic, spiking readout, surrogate gradient, structural prior, meta-learned initialization
