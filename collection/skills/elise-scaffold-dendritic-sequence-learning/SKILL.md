---
name: elise-scaffold-dendritic-sequence-learning
description: Scaffold+dendritic local plasticity learns long sequences.
category: neuroscience
metadata:
  arxiv_id: "2402.16763"
  published: "2026-09-24 (v3)"
  authors: "Laura Kriener, Ben von Hünerbein, Kristin Spicher, Federico Benitez, Timo Gierlich, Arno Granier, Walter Senn, Mihai A. Petrovici (University of Bern / UZH-ETH Neuroinformatics)"
  tags: [sequence-learning, dendritic-compartment, local-plasticity, scaffold, recurrent-network, birdsong, biological-plausibility]
---

# ELiSe: Efficient Learning of Sequences in Structured Recurrent Networks

**Paper:** ELiSe: Efficient Learning of Sequences in Structured Recurrent Networks
**arXiv:** 2402.16763v3 (q-bio.NC) — v3 updated 24 Sep 2026
**Authors:** Kriener, von Hünerbein, Spicher, Benitez, Gierlich, Granier, Senn, Petrovici

## Problem Statement

Sequence memory requires activity persisting far longer than single-neuron relaxation times. Existing solutions each fail on biological plausibility or efficiency:
- BPTT/RTRL: non-local gradients, implausible.
- Reservoir computing (train readout only): sensitive to initialization (fading/exploding transients), scales poorly with task complexity.
- RFLO: approximates RTRL but needs eligibility-trace time constants matched to afferents + weight copying for error transport.
- FORCE/FOLLOW: need near-instantaneous plasticity or global error broadcast.
- Clock-chain models (pre-learned "clock"): resource cost scales with pattern length.

## Key Innovation

Two structural features of cortex, combined, solve this:
1. **Developmental scaffold** — a sparse, static soma-targeting "nudging" connectivity grown stochastically BEFORE learning, which spatially+temporally distributes the teaching signal (with axonal delays) into the latent population.
2. **Two-compartment neurons** (dendrite + soma) — synapses get local access to all factors needed for learning: dendritic input, somatic error, presynaptic rate.

Result: complex **non-Markovian** sequences (Beethoven's Für Elise; birdsong mock-up) learned and replayed with **only local, always-on, phase-free three-factor plasticity**, using as few as **30 latent neurons**, robust to noise and mid-replay disruption.

## Model

### Populations
- **Visible** population: explicitly represents the target sequence (≈ motor cortex).
- **Latent** population: storage/recall substrate (≈ pre-motor / HVC→RA analogy).
- Development (phase 1): each visible neuron's soma receives nudging afferent; each soma-recipient forms n_out efferent soma-targeting scaffold connections (stochastically, controlled by params p, q) with **random transmission delays** into the latent pool. Scaffold is STATIC during learning.
- After development: weak all-to-all **dendrite-targeting** connections (visible+latent) are the ONLY plastic weights.

### Neuron dynamics (rate-based, two compartments)
```
Cm·v̇_den = −g_l·den(v−E_l) + I_syn^den           (dendrite, current-based input)
Cm·u̇_som = −g_l·som(u−E_l) + g_den(v−u) + I_syn^som  (soma, conductance coupling to dendrite)
```
Dendritic input drives activity (current-based approximates propagation along the tree); somatic input is weak nudging. Soma→dendrite coupling unidirectional for simplicity.

### Learning rule (local three-factor)
Weight updates minimize the gap between the **nudged somatic firing φ(u)** (target behavior, driven by scaffold) and the **dendritic prediction of somatic firing φ(v\*)**:
- factors available locally at each synapse: dendritic voltage (v), somatic error via compartment coupling, low-pass filtered presynaptic rate r̄
- learning rate η; dendrite learns to drive the soma to produce the nudged behavior
- convergence: latent population self-sustains the sequence; teacher removed with no effect
- strong-synapse minority emerges naturally → emulates dendritic pruning

### Learning protocol
Interleave training with validation: release nudging for one pattern duration, observe free activity. MSE + correlation coefficient between visible and target measure replay quality. After convergence, full replay phase (plasticity stays on, no teacher).

## Results

1. **Resource efficiency**: 30 latent neurons suffice for accurate stable replay (reservoir-style baselines need far more).
2. **Ablation (reservoir-mimic: random fixed latent weights, readout-only)**: converges FASTER during training but CANNOT self-sustain replay after teacher removal — diverges immediately. Plastic latent weights carve stable dynamical attractors; that is what makes replay possible.
3. **Timescale bridging**: same network (identical params/init) learns Für Elise at half and double speed — diverse delays/delay-chains give latent population multi-timescale representations of the past.
4. **Multi-pattern**: one shared latent pool learns two different patterns simultaneously via separate input populations.
5. **Pattern completion**: cued recall from short snippets.
6. **Robustness**: (a) noisy targets during training (correlated noise resampled every cycle) → replays the denoised pattern; (b) visible membrane potential clamped/rupted for a full cycle during replay → recovers; (c) wide stable range of scaffold params p, q.

## Implementation Guidance

- Scaffold construction: growth process seeded from nudged visible neurons, parameters p (nudging density) and q (efferent count/length distribution); include heterogeneous delays.
- Plasticity only on dendrite-targeting weights; keep scaffold frozen.
- Use validation-with-teacher-released as the training monitor (free-run MSE is the true objective; nudged error is misleadingly low).
- For SNN implementations: rate-based two-compartment dynamics map to conductance-based LIF pairs (somatic + dendritic).

## Pitfalls

- Without plastic latent weights (pure reservoir), replay collapses when the teacher is removed — do not ablate latent plasticity.
- Scaffold delay diversity is load-bearing for multi-timescale sequences; uniform delays kill half/double-speed transfer.
- Scaffold too dense → exploding activity via nudging amplification; keep sparse (p, q sweeps show robust mid-range).
- Training-error-only monitoring is deceptive: always evaluate free-running replay.

## Applications

1. Biologically plausible motor-sequence learning (birdsong HVC-RA model, cortical replay).
2. Neuromorphic deployment: local always-on plasticity, no backprop, no global error broadcast, small populations.
3. Robust sequence memory for agents: noise-tolerant recall, pattern completion, multi-pattern storage in one recurrent substrate.

## Related Skills

- `structured-recurrent-snn-backprop-free` (structured recurrence, local plasticity, WTA — complementary architecture), `dendrocentric-snn-event-classification` (dendritic computation in SNNs), `predictive-coding-exponential-family` (dendritic error propagation), `hippocampal-entorhinal-world-model` (sequence/replay biology).
