---
name: physical-learning-transformer-dyadic-circuits
description: Use when building physical/analog learning circuits or translating attention to hardware. All-transistor physical-learning transformer via dyadic double circuits.
category: ai_collection
---

# Physical-Learning Transformer via Dyadic Double Circuits

**Paper**: An all-transistor physical-learning transformer can be trained to perform in-context learning (arXiv:2610.12571, Abbott & Machta, Yale Physics & QBio, 8 Oct 2026)

## Core Problem
Equilibrium propagation / coupled learning only trains reciprocal physical systems (energy-minimizing: resistor+diode MLPs, springs, pipe networks). But transformers need **multiplication** (dot-product attention), which is non-reciprocal — an ideal voltage multiplier (VCCS) completely blocks error signals from flowing backward. Physical learning was stuck at the MLP level; ICL-style associative tasks were out of reach.

## Methodology

### 1. Dyadic double circuit (the key innovation)
- Duplicate every node and component: voltages `va` and `va'`.
- **Forward signal = mean** `(va+va')/2`; **error signal = difference** `va - va' ∝ β`.
- Free and nudged states run SIMULTANEOUSLY (unlike two-phase equilibrium propagation or Dillavou's twin-circuit hardware copies).
- Gradient read locally per resistor: `dL/dg_ab ≈ [(∆v_ab)² − (∆v_a'b')²]/4β` — exact for small β.
- Theoretical basis: dyadic potential H(v,v') of Scurria et al. (arXiv:2602.03670) — steady state is a saddle point of H, not an energy minimum. Each component contributes a term; backward currents = ∂H/∂v.
- Connection to autodiff: backward elements implement the **pullback** f*(ȳ) of each forward element. Multiplication's pullback is multiplication again (`x̄₁ = ȳ·x₂`), which is why one extra Gilbert cell suffices per multiplier.

### 2. Reverse elements per block (3 forward + 1 backward multipliers)
For a Gilbert cell `i = K·v₃·v₄`, the dyadic version needs:
- Forward: `i₀→₅ = K·v₃·v₄`, `i₀→₅' = K·v₃·v₄'`, plus correction `i₅→₅' = (K/2)·v₃·∆v₄₄'`
- Backward: `i₄'→₄ = (K/2)·v₃·∆v₅₅'` — carries gradient to earlier layers.
- Component cost: double circuit is O(1)× the original (1155→3217 components), mirroring reverse-mode AD's O(1) complexity result.

### 3. MOSFET sub-threshold attention blocks
- **Bump circuit (Delbrück)**: 4 transistors replace dot-product score with Bahdanau-like similarity `I_tail / (1 + 4·cosh²[(v₁−v₂)/(2·nV_T)])`. Peak when key≈query; never negative.
- **Bank circuit**: fixed tail current distributed among T outputs by gate voltages = hardware softmax, `i_s = I_tail·e^(v_s/τ)/Σe^(v_b/τ)`, τ = nV_T ≈ 39mV.
- **Differential pair mixer**: tail current from bank output splits by token voltages → value mixing, output `v₊−v₋ = −R_load·Σ_i_s·tanh(X_μs/τ)`.
- **Current-to-voltage amplifier** (resistor-feedback OTA): `v₂ = i₁·R_eff` — interconnects current-output blocks to voltage-input blocks.
- Learned parameters remain **adjustable resistors** (444 of them: key array 12, query 288, value 144) in crossbar arrays with inverted inputs.

### 4. Loss as a floating circuit element
- MSE: one differential OTA (VCCS) comparing output mean to target.
- **Logit cross-entropy (LCE)**: built from the SAME MOSFET bank sub-circuit implementing softmax; nudge current `i_c→c' = (β/τ)[softmax(y/τ)_c − p_target_c]`. Single-phase training — input+target applied simultaneously.
- LCE is REQUIRED, MSE fails for the ICL task.

### 5. Local adaptive optimizers
- Lion: one number memory per parameter — physically one **capacitor per resistor** storing past gradient estimates. Learning rate has units of conductance (not conductance²), making it scale-invariant — essential under exponential voltage dependence.
- Gradient descent with plain conductance units fails; adaptive rules survive the exponential dynamic range.

### 6. ICL test task
- Associative recall: strings like "h2 u6 n4 c3 h?" — match last character backward, copy companion number. Single attention layer suffices when letter+number embeddings are concatenated (D=12, T=5, D_out=6).
- K=100 distinct letters (unit vectors in R⁶) forces ICL over memorization.
- Both exact-dyadic and crude-approximate reverse elements train to high test accuracy on unseen letters (256 test examples).

## Key Conjecture
**No reciprocal physical learning system can efficiently learn ICL tasks.** Reciprocal = state minimizes an energy = equivalent to MLP-class circuits. ICL requires non-reciprocal interactions (multiplication). Tested numerically: the CET energy transformer (equilibrium-propagation-trained attention) learns memorization but NOT ICL. Expressivity (universal approximation) is an extremely loose upper bound on learnability.

## Pitfalls
- Diode doubles must be LOCKED (both on or both off per mean voltage) for exact dyadic behavior — independent diodes introduce O(β²) error (still trainable).
- Crude Gilbert-cell approximations of the bump reverse element produce large errors far from the bump but still allow optimization to find the peak.
- Bank reverse block needed the elaborate near-ideal dyadic construction (2T-wide forward bank on voltage-divider means + OTA-sensed reversed banks) — crude versions failed.
- Numerous fixed tail currents/resistances tuned by hand to match layer impedances — not yet an engineering-ready design.

## Applications
1. Analog in-hardware sequence learning: attention without digital backprop, no processor.
2. Neuromorphic substrate design: which non-reciprocal device primitives (multipliers, exponential transconductance) suffice for transformer-class learning.
3. Theoretical yardstick: ICL as the diagnostic separating post-MLP learning abilities in physical substrates (including biology — the brain is definitely non-reciprocal).

## Related Skills
- [[equilibrium-propagation-lif-snn]] — reciprocal-only regime
- [[inhibitory-neuristor-mit]] — non-reciprocal device primitives
- [[stdp-bernoulli-message-passing]] — biological message-passing alternative
