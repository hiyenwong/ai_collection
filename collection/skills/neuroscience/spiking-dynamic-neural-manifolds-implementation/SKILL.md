---
name: spiking-dynamic-neural-manifolds-implementation
description: Concrete implementation recipe for dynamic neural manifold control on neuromorphic hardware (SpiNNaker 2), derived from arXiv 2607.07373. Covers rate→spike conversion, sparse circulant weight memory, three control knobs (gain/speed, additive current/shape, subspace inhibition/selection), PCA-based manifold validation, and closed-loop maze navigation with linear readout training. Use when porting ring-attractor sequential SNNs to spike-based neuromorphic chips or building explainable low-dimensional control substrates.
version: 1.0.0
date: 2026-07-14
arxiv_id: 2607.07373
source_skill: dynamic-neural-manifolds-neuromorphic-control
tags: [spiking neural network, ring attractor, neural manifold, subspace rotation, SpiNNaker 2, closed-loop control, low-dimensional dynamics, explainable neuromorphic, PCA validation]
activation_keywords: [dynamic neural manifold implementation, ring attractor spiking, rate to spike conversion, sparse circulant weights, subspace inhibition, SpiNNaker 2 ring network, closed-loop SNN control, neural trajectory PCA, manifold control knobs]
---

# Spiking Dynamic Neural Manifolds — Implementation Recipe (arXiv 2607.07373)

Companion to `dynamic-neural-manifolds-neuromorphic-control`. This skill is the **how-to**: the exact transformations and validation steps to deploy a rate-based ring-attractor manifold model on a spike-based neuromorphic chip. The conceptual overview lives in the sibling skill; here we give the engineering primitives.

## When to use this skill

- Porting a rate-based sequential neural model to SpiNNaker 2 / Loihi / BrainScaleS (spike-based hardware).
- Building an explainable low-dimensional control substrate where geometry = behavior.
- Validating that a sparse/spiking implementation matches the rate-based baseline.

## Architecture (always start here)

1. **Ring network** of N neurons (paper uses N=500) with **asymmetric recurrent weights** → stable bump of activity travels around the ring → oscillatory sequence.
2. **Connectivity**: circulant weight matrix, **20–50% sparsity** (paper uses 50% in core figures, 20% in comparison sweeps). Scale kept weights by ×2 to compensate for lost synapses.
3. **Three control inputs** (the "control knobs"):
   - `S` multiplicative gain → **trajectory SPEED** (rotations/sec around ring).
   - `I(t)` additive (Gaussian) current → **trajectory SHAPE / bump RADIUS** (number of co-active neurons).
   - `p_inh ∈ [0,1]` subspace inhibition fraction → **subspace SELECTION / ROTATION** (switch behavioral state).
4. **Readout**: linear decoder trained from ring spikes → motor/control outputs.

## Step 1 — Rate → Spike conversion (critical for performance)

The original model (Lehr et al. 2024,2025) is **rate-based**. SpiNNaker 2 is spike-optimized, so:

- Add a **probabilistic rate→spike layer**: treat each neuron's rate `r_i` as the probability of spiking in the current timestep. `spike_i ~ Bernoulli(r_i)`.
- This **drastically cuts inter-neuron communication** (spikes only when active) vs. broadcasting continuous rates.
- Timestep: `dt = 1 ms` (real-time threshold on SpiNNaker 2).

## Step 2 — Sparse circulant weight memory trick

On-chip SRAM is tiny (128 KB/core). Recording 32 neurons' rates fills 128 KB in ~1000 steps (1 s). Mitigations:

- Exploit **circulant structure**: store only ONE row of the weight matrix + a 1-bit sparsity mask (synapse present / absent). Do NOT store the full N×N matrix.
- **Stream control parameters IN** and **stream output spikes OUT** to a host; avoid storing parameter sequences or recordings on-chip.
- Smaller bumps (more inhibition) → fewer spikes → lower runtime (linear scaling with spike count).

## Step 3 — Three control knobs → manifold geometry map

| Knob | Mechanism | Manifold effect | Validation metric |
|------|-----------|-----------------|-------------------|
| `I(t)` shape | transient Gaussian exc/inh current | bump width / trajectory **radius** | # spikes (impl) vs Σ rates (baseline) |
| `S` speed | multiplicative gain amplifies input | bump **velocity** (rotations/s) | rotations counted in 1 s |
| `p_inh` selection | random inhibitory ensemble silences fraction `p_inh` | **subspace rotation** by angle `θ = arccos(1 − p_inh)` | 1st principal angle between PCA subspaces |

- **Subspace rotation** is the key behavioral-switch primitive: switching inhibitory ensembles rotates the active hyperplane; downstream readouts disambiguate each orientation. Sequence dynamics are preserved (unlike full reset).
- Acceptable parameter ranges validated on chip: `p_inh ∈ [0, 0.95]`, `S ∈ [1, 2]`, `I ∈ [0, 2]`. Runtime stays **well below 1 ms/step** for N=500, 20% connectivity.

## Step 4 — PCA validation procedure (reproduce before trusting)

1. Run sequence under each of K=10 inhibitory ensembles (vary `p_inh`).
2. For each, record internal rates → PCA, retain first `k=2` components.
3. Compute **first principal angle** between every pair of 2-D subspaces.
4. Compare to analytical `θ = arccos(1 − p_inh)`. Match = faithful implementation.
5. For speed/shape: sweep `S` and `I` independently; compare bump size (spike count) and rotation count to CPU rate-based baseline.

## Step 5 — Closed-loop maze application

- **Two-wheeled agent**, three subspaces (each 40% / 200 of 500 neurons active) encode: forward / turn-in-place / jump.
- **External program** (not on chip) holds world model + plan; translates plan + local sensory cues (wall distances, ground type) → control params `(S, I, p_inh)` for the ring.
- **Readout training**: 200 random actions, each held 250 ms; map ring activity → target motor controls via linear regression on recorded spikes. Then deploy: ring spikes → learned readout → motors.
- Result: agent integrates high-level plan into a single manifold representation; "hidden code" is visible only from the geometric (PCA) perspective, not raw spike raster.

## Pitfalls

- **Do NOT store long recordings on-chip** — SRAM exhausts in ~1 s. Stream instead.
- **Rate→spike conversion is approximate**: at very high `S` (>30 in some sweeps) SpiNNaker 2 ran marginally faster than baseline; re-tune gain if speed fidelity matters.
- **Circulant assumption** only holds for ring topology; 2-D cortical sheets (Ye et al. 2026) need correlated asymmetric weights → traveling waves, different implementation.
- **External planner off-chip** in the paper; for full autonomy, move planning/readout on-chip (future work).

## Verification checklist

- [ ] Bump travels smoothly around ring (no fragmentation) at `p_inh=0`.
- [ ] Increasing `I` increases spike count / bump radius vs baseline.
- [ ] Increasing `S` increases rotations/s, matches baseline until ~S=30.
- [ ] First principal angle ≈ `arccos(1−p_inh)` across ensemble pairs.
- [ ] Readout trained on random exploration reproduces target motor controls (R² check).
- [ ] Runtime < 1 ms/step at target N and sparsity.

## References

- von Seeler, Tetzlaff, Lehr. "Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware." arXiv:2607.07373 (2026).
- Lehr et al. 2024, 2025 — rate-based dynamic manifold framework (control knobs derivation).
- Mayr et al. 2019; Höppner et al. 2022 — SpiNNaker 2 architecture.
