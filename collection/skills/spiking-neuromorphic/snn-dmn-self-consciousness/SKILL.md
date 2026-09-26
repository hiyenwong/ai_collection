---
name: snn-dmn-self-consciousness
description: Use for DMN self-consciousness SNN modeling with IIT phi.
category: ai_collection
---

# SNN Model of Elementary Self-Consciousness via Endogenous DMN Dynamics

Methodology from arXiv:2609.29984 (Lahoz-Beltra, 2026, Complutense University of Madrid).
A 10,000-neuron Izhikevich spiking network where an endogenous Default Mode Network (DMN) pacemaker subsystem maintains autonomous bioelectric rhythms (the "pulse of the Self"), interacting with a sensory layer. Consciousness proxy φ computed via IIT covariance decomposition. Use when modeling self-referential cognition, baseline self-awareness, DMN dynamics, or integrated information in spiking networks.

## Core Architecture

**Two interacting subsystems (N = 10,000 total):**

1. **Sensory Processing Layer** (i = 0…4,999): cortical excitatory pyramidal neurons, regular-spiking (RS) dynamics. Heterogeneous reset parameters drawn from uniform distributions:
   - `c_i = -65.0 + 15.0·r_i²`, `d_i = -8.0 + 6.0·r_i²`, where `r_i ~ U(0,1)`
2. **DMN Pacemaker Subsystem** (i = 5,000…9,999): intrinsically bursting (IB) units modeling thalamocortical/posterior cingulate assemblies. Core pacemaker subset (i = 5,000…5,999) uses deterministic parameters `c = -55.0 mV, d = 4.0` — elevated c shortens refractory period, inducing intrinsic bursting.

**Connectivity**: sparse, K = 1,000 random outgoing projections per neuron (10⁷ total synapses). Synaptic weight `S_ij = U(0,1) · w_ij` with **hierarchical top-down asymmetry**:

```
w_ij = 0.6  if presynaptic j ≥ 5000 (DMN projections — functional supremacy)
w_ij = 0.4  if presynaptic j < 5000 (sensory projections)
```

This asymmetry encodes top-down modulatory dominance of self-referential assemblies over sensory cortex.

## Izhikevich Dynamics

```
dv/dt = 0.04v² + 5v + 140 − u + I

du/dt = a(bv − u)
if v ≥ 30 mV: v ← c, u ← u + d
```

- v = membrane potential, u = membrane recovery (pA), I = total input current (pA)
- a = recovery timescale, b = subthreshold sensitivity, c/d = reset parameters
- RS regime (sensory): standard cortical profile; IB regime (DMN core): c = -55, d = 4

## Input Current Decomposition (per ms)

```
I_i(t) = I_i,tonic + I_i,ext + Σ_j I_i,syn + η_i(t)
```

1. **Endogenous tonic current** (ascending brainstem neuromodulation proxy): `I_tonic = 7.0 pA` applied continuously ONLY to core DMN pacemakers (i = 5,000–5,999). Maintains intrinsic rhythms independent of external input — the biological basis of the autonomous Self.
2. **Exogenous stimuli**: step current `16.0 pA` to 1,500 sensory neurons during a window (e.g., 300 ms < t < 600 ms).
3. **Synaptic current**: `I_syn = Σ_j S_ij` summed over presynaptic neurons j that fired within the current ms (`v_j(t) ≥ 30 mV`).
4. **Cognitive noise**: uncorrelated Gaussian `N(0, σ²)` with σ = 3 (thermal/stochastic brain noise).

## Numerical Integration: Half-Step Euler

Two-step (half-step) Euler, fixed Δt = 1.0 ms — avoids RK4 overhead while maintaining stability:

```
v_i½ = v_i(t) + 0.5·(0.04·v_i(t)² + 5·v_i(t) + 140 − u_i(t) + I_i(t))

v_i(t+1) = v_i½ + 0.5·(0.04·v_i½² + 5·v_i½ + 140 − u_i(t) + I_i(t))

u_i(t+1) = u_i(t) + a_i·(b_i·v_i(t+1) − u_i(t))
```

## IIT φ Quantification (Covariance Determinant Ratio)

Barrett-Seth / Mediano-style Gaussian approximation of integrated information:

1. **Temporal window** τ ms (e.g., τ = 5 or 80 ms). Select M most active neurons (M ≤ 200).
2. **Binary spike matrix** `X ∈ {0,1}^{M×τ}`: `X_{i,t} = 1` iff neuron i spiked at time t.
3. **Firing rates**: `μ_i = (1/τ)·Σ_t X_{i,t}`
4. **Cross-covariance**: `Σ_ij = (1/τ)·Σ_t (X_{i,t} − μ_i)(X_{j,t} − μ_j)` → global matrix `Σ_Global ∈ R^{M×M}`
5. **Bipartition** by anatomical subsystem into block-diagonal `Σ_Part = diag(Σ_Sensory, Σ_DMN)`
6. **Integrated information**:

```
φ = (1/2)·ln( det(Σ_Part) / det(Σ_Global) )
```

- Independent subsystems (zero cross-correlation): `det(Σ_Global) = det(Σ_Part)` → φ = 0, no integrated experience.
- Strong sensory-DMN co-activation: `det(Σ_Global) < det(Σ_Part)` → φ rises, signaling Qualia emergence.

## Observed Dynamical States (900 ms simulation)

| State | φ (bits) | Dynamics |
|-------|----------|----------|
| Quiescent/isolated | ≈ 0 | Sensory silent; DMN pacemakers fire asynchronously at low freq driven by tonic 7 pA; Σ_Global ≈ Σ_Part |
| Pre-burst priming | 1–2.5 | Sparse spiking bridges sensory-DMN boundary; φ ramps before ignition |
| Peak integrated | 12.5–15.0 | Population bursts saturate (~1000 Hz); maximal sensory-DMN mutual information |

Population bursts (~4 per 900 ms) ignite via recurrent DMN excitation + top-down (w=0.6) recruitment of sensory layer.

## Key Results

- Endogenous activity ALONE (no cross-network interaction) yields φ ≈ 0 — unified information requires dynamic coupling between internal self-referential dynamics and sensory input, not static architecture.
- Qualia emerges from the non-linear interaction of endogenous DMN rhythms with transient sensory perturbations.

## Implementation Notes

- Python 3.13, MacBook Air M2 (16 GB) — the full 10k-neuron/10M-synapse simulation runs on a laptop.
- Sparse matrix format essential for the 10⁷ synapses.

## Theoretical Caveats (P-zombie)

The simulation is a **functional "philosophical zombie"**: it exhibits access consciousness (algorithmic state integration) without phenomenal consciousness (subjective "what-it-is-like"). φ on silicon ≠ subjective feel. Under Chalmers' organizational invariance, faithful causal topology replication could instantiate experience; under Searle's biological naturalism, simulation ≠ duplication. Non-zero φ is an informational proxy only.

## Extensions
- Port to neuromorphic hardware (Intel Loihi, BrainScaleS) for physical voltage dynamics/continuous-time substrate
- Add STDP so synaptic weights self-organize over prolonged sensory exposure → long-term memory traces
- Closed-loop validation against cortical organoids + microelectrode arrays (organoid intelligence)

## References
- Izhikevich (2003) IEEE TNN 14(6):1569-1572 — spiking neuron model
- Barrett & Seth (2011) PLoS Comput Biol — practical φ measures from time series
- Raichle et al. (2001) PNAS — default mode of brain function
- Tononi (2004) BMC Neuroscience — information integration theory

Source: arXiv:2609.29984 — Lahoz-Beltra, "A Spiking Neural Network Model of Elementary Self-Consciousness via Endogenous Default Mode Network Dynamics"