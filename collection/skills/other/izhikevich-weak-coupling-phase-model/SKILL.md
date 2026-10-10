---
name: izhikevich-weak-coupling-phase-model
description: Use when analyzing synchronization of coupled Izhikevich neurons or applying phase reduction to discontinuous (reset-based) spiking models. First phase model for chemically coupled Izhikevich pairs.
category: neuroscience
metadata:
  arxiv_id: "2610.04025"
  published: "2026-10-02"
  authors: "XinYe Cheng, Sue Ann Campbell"
  source: "arXiv q-bio.NC"
  tags: [izhikevich neuron, phase model, phase locking, iPRC, discontinuous dynamical system, weak coupling]
---

# Stability of Phase-locked States of Weakly Coupled Izhikevich Neurons

Cheng & Campbell (arXiv:2610.04025) compute the **first phase model for chemically coupled Izhikevich neurons**, extending weakly-coupled oscillator theory to a discontinuous dynamical system. The payoff: closed-form prediction of in-phase/anti-phase (and multi-lock) stability across the (b, I_app) parameter plane, plus a surprising dissociation between excitability class and iPRC type.

## Model

Standard Izhikevich with single-exponential chemical synapse:

```
C v̇_i = k(v_i − v_r)(v_i − v_t) − u_i + I_app(t) − g_syn·s_j·(v_i − v_syn)
u̇_i  = a(b(v_i − v_r) − u_i)
ṡ_i  = −β s_i
if v_i ≥ v_peak: u_i → u_i + d, v_i → c, s_i → 1
```

Weak coupling enforced by g_syn ≪ 1 (simulations used g_syn = 0.01). Presynaptic spike opens all channels instantaneously (s → 1), closing with time constant 1/β. Excitatory focus: v_syn = 0 mV.

## Why Standard Phase Reduction Fails — and the Fix

Izhikevich is discontinuous (state-dependent reset), so infinitesimal phase reduction for smooth flows does not apply directly. Treatment:
1. Analyze the **smooth subsystem** (v,u) with standard bifurcation software (XPPAUT).
2. Treat the **reset as re-injection** into the phase plane: solutions that would diverge are mapped back above the v-nullcline, creating large-amplitude **discontinuous limit cycles** (these ARE the spikes).
3. Compute the iPRC for the discontinuous cycle (adjoint with jump conditions at reset).
4. Interaction function via the coupling G = (G^v, 0), G^v = −s_j(v_i − v_syn):

```
H(φ) = (1/T) ∫₀ᵀ Z̄ᵛ(t) · [−exp(−β(t+φ)) · (v̄(t) − v_syn)] dt
```

(presynaptic neuron fired at t+φ, its gating variable decays as exp(−β(t+φ))). Numerically integrated with `scipy.integrate.simpson`. Phase-locked states: zeros of H_odd; stability from H_odd′.

## Spiking Onset Has THREE Routes (b, I_app) plane

Bogdanov–Takens point at b = b_BT = 3 nS (with the paper's parameter set), I_app ≈ 103 pA. Discontinuous saddle-node-homoclinic codimension-2 point numerically estimated at **b_dSNH ≈ 1.51** (XPPAUT manifold tracking, two decimals):

| Regime | Onset mechanism | Excitability |
|--------|----------------|--------------|
| b < b_dSNH (~1.51) | **discontinuous SNIC** (saddle-node on invariant circle analog): E₂ + invariant loop coalesce into the spiking cycle directly at I_sn | Class I |
| b_dSNH < b < b_BT | **discontinuous saddle-homoclinic** at I_dhom < I_sn: stable large-amplitude cycle appears *before* SN kills equilibrium → **bistability window** (E₂ + cycle coexist) | Class II |
| b > b_BT | **subcritical Hopf** destabilizes rest (SN curve already gone) | Class II |

Practical: the reset-induced homoclinic creates a hysteresis/bistability band absent from smooth-subsystem analysis — matters for any bistable-memory interpretation of Izhikevich networks.

## Key Dissociation: Excitability Class ≠ iPRC Type

- Near spiking onset: iPRC is Type I (purely positive) for small b, Type II (sign-changing) for large b — **but the Type I→II transition happens at much lower b than the Class I→II transition**.
- Therefore there is a **significant b-range with Class I excitability but Type II iPRC** — F-I curve says Class I while the phase response already sign-changes. Synchronization behavior follows the iPRC, not the F-I curve.
- As I_app moves away from onset, the negative portion of the iPRC shrinks (formally Type II but functionally Type I).

**Rule**: never infer synchronization properties from excitability class alone; compute the iPRC at the operating point.

## Phase-Locking Results

| Condition | Prediction |
|-----------|------------|
| b < 0.5 (all I_app) | Only in-phase (stable) + anti-phase (unstable) |
| b ≥ 0.6, I_app near onset | **Multiple phase-locked states; in-phase AND anti-phase both stable** (coexistence) |
| b ≥ 0.6, larger I_app | Anti-phase destabilizes; only in-phase stable |

- Lower β (slower synaptic decay = longer mutual influence) → larger |H| → faster convergence to locked states; existence/stability pattern unchanged for β ∈ [0.1, 0.8].
- Smaller reset jump d (20, 50 vs 100) extends the stable-anti-phase range in I_app but anti-phase still destabilizes for large I_app (d controls I_dhom, hence the bistability window).
- Full network simulations (g_syn=0.01, phase offset α via delayed step current) **agreed with phase-model predictions in all cases**.

Mechanistic summary: adaptation conductance b pushes the iPRC Type II near onset; anti-phase stability rides on the negative iPRC lobe. Away from onset the negative lobe collapses → anti-phase dies. Adaptation + excitatory coupling always leaves synchrony stable (consistent with smooth conductance-based results), but the anti-phase attractor is b- and distance-from-onset-conditional.

## Implementation Recipe

```python
# 1. Pick (b, I_app); identify onset route via XPPAUT manifold tracking
#    (b<1.51: dSNIC; 1.51<b<3: homoclinic window with bistability; b>3: subcrit Hopf)
# 2. Compute discontinuous limit cycle: integrate with event on v=v_peak,
#    apply reset map, continue until periodicity (v,u,s return)
# 3. iPRC: adjoint integration backward with jump condition at reset surface
#    (Z jumps by the saltation/jump matrix at the reset)
# 4. H(φ) = (1/T) ∫ Z̄ᵛ(t)·Gᵛ(X̄(t), X̄(t+φ)) dt   # simpson quadrature
# 5. Lock states = zeros of H_odd(φ); stable iff H_odd′(zero) < 0
# 6. Validate at g_syn=0.01 with phase-shifted step-current sims
```

## Pitfalls

- Do NOT apply smooth-flow phase reduction directly — the reset is not a perturbation; it reshapes topology (creates cycles that don't exist in the smooth subsystem).
- The iPRC type transition and excitability class transition are at DIFFERENT b values; the dissociation band is where naive Class-based intuition fails.
- Anti-phase stability is distance-from-onset sensitive: a network parameter sweep that varies I_app will cross the anti-phase destruction boundary even at fixed Type II iPRC.
- For b < 0 with small d, cycles become near-1D ultra-fast — numerically stiff; resolve with tighter tolerances or avoid.
- Saltation conditions at reset are mandatory in the adjoint; skipping them silently corrupts the iPRC negative lobe (and hence every stability claim).

## Applications

- Synchrony/anti-phase design in Izhikevich-based SNNs (choose b and operating current to get or avoid anti-phase attractors).
- Bistability-band exploitation: (b_dSNH, b_BT) × (I_dhom, I_sn) supports stable rest + spiking coexistence → working-memory-style states without auxiliary variables.
- Cross-check for any reset-based spiking model (adaptive LIF with spike-frequency adaptation shares the homoclinic mechanism).

## Cross-References

- `heterarchy-brain-control-spectrum` — control as configuration; here phase-locked states are the process-level constraints that fail to compose.
- `lyapunov-spectrum-random-neural-networks`, `predictable-mean-field-chaos-random-recurrent-networks` — stability tooling for larger coupled nets.
- Tamura et al. [54] — Poincaré-map bifurcation analysis of the same model, different parameters (the homoclinic precedent).
