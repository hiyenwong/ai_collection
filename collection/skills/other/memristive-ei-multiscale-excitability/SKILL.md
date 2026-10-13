---
name: memristive-ei-multiscale-excitability
description: "Unified mixed-feedback EI model linking Hodgkin-Huxley and Amari via memductances. Use across-scale design."
category: ai_collection
tags: [excitability, memristive-models, hodgkin-huxley, amari-neural-fields, mixed-feedback, population-spikes, lateral-inhibition, mean-field, multiscale]
---

# Excitability Across Scales: A Unifying Memristive EI Model

**Source**: arXiv:2610.13275 (Burger & Sepulchre, KU Leuven / Cambridge, q-bio.NC, Oct 2026)

## What It Is

A spatiotemporal excitatory-inhibitory (EI) model that **unifies cellular (Hodgkin-Huxley) and population (Amari neural field) excitability through one shared mixed-feedback circuit architecture**, where all modeling complexity is concentrated in "memductances" — voltage-history-dependent conductances (Chua & Kang memristive systems). Scale changes become a change of memductance resolution, not a change of modeling principle.

## The Core Idea: One Architecture, Two Memductance Types

The mixed-feedback motif: an RC membrane in feedback with two currents of opposite sign (fast excitatory `ge`, slow inhibitory `gi`).

| Scale | Excitatory feedback | Inhibitory feedback | Emergent threshold phenomenon |
|---|---|---|---|
| Temporal (HH) | fast Na activation `ge` (small τe) | slow K activation `gi` (large τi) | action potential + rebound (post-inhibitory) excitation |
| Spatial (Amari) | short-range E kernel σE | long-range I kernel σI (σE < σI) | spatially localized field event (lateral inhibition) |
| Spatiotemporal | internal pointwise e/i currents | synaptic spatially-filtered E/I currents | **population spike**: localized in BOTH space and time |

### Minimal memductance model (Eq. 2)
Each conductance = first-order lag + sigmoid:
```
τx v̇x = v(t) − vx        (voltage filter)
x(t) = σ(κx·vx − vx_th)   (activation)
gx(t) = ḡx·x(t)           (Ohmic current with memory)
```
Sodium inactivation is OMITTED — redundant with K activation. Temporal excitability requires only: (a) timescale separation τe/τi small; (b) activation overlap: σi(v) > σe(v) at/below rest (so inhibition is open at equilibrium and removable by hyperpolarization) but σe′(v) > σi′(v) near threshold.

### Synaptic (spatial) memductance (Eq. 5)
Temporal filter then spatial convolution then sigmoid:
```
τsyn v̇syn(T) = v(x,t) − vsyn(T)     (temporal lag)
vsyn(ST) = w ∗ vsyn(T),  w = e^(−|x|/σ)   (spatial kernel)
gsyn = ḡsyn · σ(κsyn·vsyn(ST) − vth_syn)
```
Lateral inhibition ↔ temporal excitability analogy: **σE/σI small ⟺ τe/τi small**.

## Key Results

### 1. Population spikes from strongly heterogeneous populations
- 2×901-unit E/I fields, x ∈ [−30,30]; intrinsic conductances vary **±40% uniformly** per point; coherent population event still emerges: spatially AND temporally localized recruitment (Tpop ≈ 3.3 ms, ℓpop ≈ 0.46, ~2.6× individual spike duration Tind ≈ 1.3 ms).
- The population spike is NOT a copy or sum of individual spikes — it has its own scales, set by recruitment, suppression, kernel ranges and heterogeneity.

### 2. Both feedback loops are REQUIRED (complementarity ablations)
- Remove spatial memductances (ḡE/I = 0): no spatial coherence — independent heterogeneous responses to shared input.
- Remove internal temporal memductances (replace with matched effective leak): spatial feedback alone cannot sustain temporal coherence; trial-averaged activity decays to baseline over 100 paired trials. Spatial-only feedback is localized by the short-range E kernel and too fragile to recruit heterogeneous neighbors.
- Mean-field metric: CP(t) = ⟨vE(x,t)⟩²x — full model shows robust decaying spike trains; either ablation gives NO mean-field events.

### 3. Heterogeneity is the tuning knob (across-scale design)
- Rescale (gl, ḡe, ḡi) → µ·(gl, ḡe, ḡi) for a central 10/20/30% subpopulation: population rhythm frequency shifts continuously DOWN as µ decreases (reduced cellular excitability brakes the whole field).
- **Robustness to heterogeneity is what makes heterogeneity usable as a continuous control knob** — a candidate mechanism for neuromodulation acting at cellular scale to reshape macroscopic rhythms (cf. Drion et al. 2018 brain-state switching).
- This cannot be expressed in classical Amari/Wilson-Cowan fields or LIF models, which lack the internal memductance loop.

## Analytical Criteria (Appendix A.3.1)

Positive-feedback (spike initiation): `gl + ḡe[σe(v) + (v−Ee)σe′(v)] < 0`, i.e. steep E sigmoid overcoming leak: σe′(v)(Ee−v) > σe(v) + gl/ḡe.

Rebound (post-inhibitory) excitation requires sign change in differential conductance:
```
Drise(v; vi,b) < 0 < Drec(v)
Drise = gl + ḡe[σe(v) + κe(v−Ee)σe(1−σe)] + ḡi·σi(vi,b)
Drec  = gl + ḡe[...] + ḡi[σi(v) + κi(v−Ei)σi(1−σi)]
```
Rebound favored when hyperpolarization deactivates slow inhibition (σi(vi,b) ≪ 1) while gi is active at rest. Recovery requires slow I activation to catch up during depolarization.

## How to Use / Protocol

1. **Model construction**: Build the membrane ODE with parallel currents (Cv̇ = −iint + isyn + iapp); implement each memductance as lag→sigmoid cascade (Eq. 2) and synaptic memductances as lag→conv→sigmoid (Eq. 5). Canonical params: τe=1, ḡe=3, κe=2, Ee=50, τi=10, ḡi=20, κi=1.2, Ei=−15, gl=0.3; spatial σE=1, σI=3, ḡEsyn=1.2, ḡIsyn=2.0, vEth=5, vIth=0, κE=1, κI=2, τE=τI=10 (Tables 2-3).
2. **Integration**: Tsit5 (adaptive RK), tolerances 1e-5; spatial domain via FFT circular convolution, self-coupling removed + kernels renormalized to unit integral.
3. **Robustness testing**: Inject ±40% uniform heterogeneity per site; verify coherent mean-field events survive (CP(t) peaks).
4. **Ablation check**: For any claimed population phenomenon, test both temporal-only and spatial-only ablations — population excitability requires BOTH loops.
5. **Frequency tuning**: Treat subpopulation conductance scaling µ as the macro-control; measure fpop via peak detection on CP(t) (min prominence 10% of range, CV of inter-peak intervals < 0.5).
6. **Scale selection**: To study a different scale, change ONLY memductance resolution (temporal models spatially average; spatial models temporally average) — never the circuit structure.

## Related Skills / Concepts

- [[neural-fields-nv-sensing]] / [[neural-fields-world-models]] — neural field modeling
- [[fixed-point-compositionality-low-rank-gluing]] — E/I network dynamics at circuit level
- [[multi-timescale-conductance-spiking-networks]] — multi-timescale conductance SNNs
- [[free-energy-principle-moe-routing]] — LIF-based alternatives that lose the internal loop
- Drion et al. 2018 (switchable slow conductances / brain states); Dethier et al. 2015 (positive feedback at cellular level); Chua & Kang 1976 (memristive systems).

## Citation

Burger, T.S.J. & Sepulchre, R. (2026). Excitability across scales: a unifying EI model. arXiv:2610.13275.
