---
name: strc-mean-field-alternating-populations
description: "Use when predicting gamma/ripple oscillation stability in E-I oscillator populations with biexponential synapses and delays. Tonic/phasic decomposition replaces phase response curves at high frequency."
category: ai_collection
trigger: spike time response curve, STRC mean field, biexponential synapse, pulse summation, gamma oscillation, ripple oscillation, alternating firing, E-I population locking, conduction delay, synchrony stability, interval response curve
source: arXiv:2610.10977 (Ananth Vedururu Srinivas & Carmen C. Canavier, LSU Health New Orleans, v1 7 Oct 2026)
---

# STRC Mean Field Theory for Two Alternating Synchronous Populations

## Core Contribution

Extends the STRC (spike time response curve) mean-field approach from a single synchronous population (Canavier 2025) to **two alternating populations** coupled by delayed biexponential synapses. Solves the central failure of pulsatile phase-resetting theory at high frequencies: when synaptic conductance duration exceeds the network period, received pulses **summate across multiple cycles**, and the concept of instantaneous phase response breaks down. The method **drops phase entirely** and works with time-interval perturbations, correctly predicting existence AND stability of 1:1 alternating locking in fast gamma (110–120 Hz) and ripple (~190 Hz) regimes where the classic pulsatile PRC approach fails.

## When Classical Pulsatile Coupling Fails

Pulsatile coupling theory (Mirollo–Strogatz lineage) assumes each pulse is an instantaneous phase shift (with optional conduction delay). This breaks when:
- Each spike activates a **biexponential synapse** (rise τ_R, decay τ_d)
- High frequency ⇒ conductance duration > network period ⇒ pulses **summating over several cycles**
- No autonomous limit cycle interpretation; phase undefined during the stimulus interval

## Method: Tonic/Phasic Decomposition

1. **Tonic component**: minimum of the infinite train sum of biexponential conductances — sets a new free-running period P^E for the embedded oscillator
   - Tonic conductance (τ_R >> τ_d approx): `g_tonic(t) = f·(e^{-t/τ_d} − e^{-t/τ_R})/(1 − e^{-P/τ_d})` style closed forms from Canavier 2025
2. **Phasic component**: single-cycle waveform of the deviation from tonic, with a **trough at input receipt** (phasic part = 0 at t_s)
3. **Mean field response**: M(t_s) = P^E − P₁, difference between tonic-embedded cycle length and perturbed cycle length. Measured by shifting the oscillator's firing within the network pattern relative to the input
4. **Key caveat**: neglects residual state effects of previous phasic cycles at spike time — validated by simulations

## Existence Criterion (1:1 locking, two clusters)

Alternating firing pattern with symmetric reciprocal external delays δ_ext:

- Algebraic constraint: stimulus interval of one cluster = response interval of other + 2δ_ext (and vice versa): `t_s* = t_r* + 2δ_ext`, network period `P_N = t_s* + t_r*`
- Scan forcing periods P_F: for each candidate t_s, the mean-field-perturbed period P₁(t_s, P_F) is the **predicted network period P_N**
- **Existence** ⇔ intersection of P_N(P_F) curve with the diagonal (self-consistency), then phasic relationships fixed by the second constraint
- Two intersections typically ⇒ only one can be stable

## Stability Criteria (no phase, pure time units)

**Within-cluster synchrony** (all-to-all, J perturbed out of N-J cluster; M' = dM/dt_s):
```
|1 − M'_J(δ) − M'_{N-J-1}(δ)| < 1          (cluster A internal, conduction delay δ)
```

**Two-cluster alternating locking** (cluster A self-connected, cluster B not; short-delay regime δ_ext < min(t_l1, t_l2)):
```
λ₁ = (1 − M'_{A,B}(t_sA*)) · (1 − M'_{1,A-1,B}(δ) − M_{A-1,1,B}(δ))
λ₂ = (1 − M'_{A,B}(t_sA*)) · (1 − M'_{B,A-1,1}(t_sB*)) · (1 − M_{B,1,A-1}(t_sB*))
```
Six mean-field responses with triple subscripts needed in general, but dual-embedding makes M'_{A,B}(t_sA*) = M'_{A-1,B,1}(t_sA*) — measure the cross-population response once. Stability ⇔ |λ₁|,|λ₂| < 1.

**Sign intuition**: positive slope M' < 1 at the locking point is stabilizing; negative slope is destabilizing (selects which of the two intersections is stable).

## Validated Regimes

| Regime | Synapses | Result |
|---|---|---|
| Fast gamma 110–120 Hz | I-I hyperpolarizing (E_REV −75 mV), δ=0.3 ms, E↔I delays 0.1–2.15 ms | Predicted lags + stability match simulation; above δ_ext=1.65 ms no locking predicted or observed |
| Ripple ~190 Hz | I-I shunting (E_REV −55 mV) | I cluster alone CANNOT synchronize (eigenvalue 1.511 > 1); **reciprocal E coupling stabilizes it** — coupling factor (1−M'_{A,B}) ≈ 0.5 reduces eigenvalue below 1; mean-field lag predictions beat pulsatile PRC predictions substantially |

Setup: 100 homogeneous inhibitory PV interneurons (36 fixed synapses each) + 1 RTM excitatory neuron (E population has no recurrent connectivity — models stellate cells in medial entorhinal cortex layer 2, motivated by Pastoll et al. 2013 observation that interneurons synchronize at gamma only with reciprocal E connectivity). Conductance-based Hodgkin-Huxley, BRIAN2 simulator.

## Key Mechanistic Insight: E-Coupling Rescues Unstable I-Synchrony

In the shunting regime, within-cluster synchrony is unstable in isolation. Coupling to the E population multiplies the within-cluster eigenvalue by |1 − M'_{A,B}(t_sA*)|: at the **stable** intersection the slope is positive (<1 ⇒ shrinking factor ~0.5), at the unstable intersection negative (⇒ 1.72). The E cell acts as a stabilizing surrogate — a mechanism for how E-I reciprocity generates fast rhythms even when inhibition alone cannot synchronize.

## Scope & Failure Modes

- Valid in **mean-driven regime** (oscillators fire periodically), NOT fluctuation-driven (contrasts Brunel–Hansel noisy population framework, Dumont et al. refractory-density macroscopic PRCs)
- Breaks with overly strong inhibition (shunting clamp at reversal potential; late hyperpolarizing input missing a spike and summating into next interval) or strong excitation (1:n locking, I cells fire multiple times per E spike)
- Short-delay regime only: δ_ext < min(t_l1, t_l2); longer delays decrease stability (Woodman & Canavier 2011 criteria)
- Synaptic conductances with the same reversal potential add; different reversal potentials require separate measurement protocols (dual tonic + single shifted phasic input)
- Applicable to intrinsic pacemaker populations (basal ganglia, cerebellar, cholinergic, suprachiasmatic) and possibly non-neural oscillators with continuous coupling

## Relevant to in vivo data

Huang et al. 2024 (optogenetics): PV+ interneurons during ripples fire precisely timed, locked to ripple cycles in synchronized assemblies — supports oscillator (vs fluctuation-driven) interpretation of fast rhythms.

## Code

git@github.com:AnanthVS23/Meanfield_EI.git (BRIAN2 notebooks)

## Related Skills

- [[arithmetic-sync-basin-pulse-coupled-oscillators]] — pulse-coupled sync basins via number theory
- [[bipartite-oscillator-synchronization-modes]] — Kuramoto-Sakaguchi E-I collective states
- [[kuramoto-control-theory]] — complex-valued Kuramoto control
