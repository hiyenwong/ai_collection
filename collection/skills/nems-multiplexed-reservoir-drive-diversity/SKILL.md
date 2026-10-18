---
name: nems-multiplexed-reservoir-drive-diversity
description: Use for multimode NEMS reservoir computing via drive-amplitude multiplexing.
category: ai_collection
---

# Dynamical Diversity via Drive Multiplexing in Multimode NEMS Reservoir Computing

Methodology from arXiv:2609.29532 (Ahmed, Garcia, ... Hanay, Sep 2026, Bilkent/CEOT).
Physical reservoir computing where a **single nanoelectromechanical (NEMS) resonator's two interacting flexural modes** are driven with complementary allocations of a fixed total drive amplitude; responses are replayed and **concatenated into one feature matrix** for a linear readout. On NARMA-2 this cuts variance-normalized error **28×** vs single-mode operation. Use when designing physical reservoirs, multimode MEMS/NEMS computing, feature-diversification via operating-point sweeps, or honest benchmarking of physical RC (feedthrough controls).

## Core Idea: Drive Diversity as a Multiplexer

Standard physical RC: one device, one drive setting, one response vector. This work fixes the total electrical drive budget (e.g., 140 mV) and **re-allocates it between two coupled modes** (V₁+V₂ = const). Each allocation (V₁,V₂) maps the SAME input stream to a different nonlinear composite state (inter-modal Duffing coupling α_ij shifts effective stiffness; drive assignment itself is a control knob). Replaying the input under N complementary amplitude pairs and concatenating per-symbol responses enlarges the representation **without new devices and without training internal dynamics** — only the linear ridge readout trains.

## Physics of the Reservoir

- **Nonlinearity**: geometric Duffing coefficients α_ii (self) + α_ij (inter-modal) — resonance curves bend/stiffen with drive amplitude; hysteresis onset ~20 mV for mode 1.
- **Fading memory**: mechanical ring-down. Free-decay lifetime scales with **Q/f, not Q alone** — mode 2 (Q≈812, f≈21.4 MHz) decays FASTER than mode 1 (Q≈516, f≈5.6 MHz) despite higher Q. Counter-intuitive: the "best" memory mode is not the highest-Q mode.
- **Encoding**: symbol u(t) → drive voltage; AWG tone at Ω_j ≈ ω_j/2 exploits **thermomechanical V² forcing** (tone outside bistable region); smallest symbol maps to half the per-mode drive.
- **Readout**: digital lock-in at **2nd harmonic (h2)** = mechanical response (quadratures X_j,Y_j per mode); **1st harmonic (h1)** = direct capacitive feedthrough — an internal LINEAR baseline computed from the same recording.

## Working Recipe

1. Fix total drive budget (e.g., 140 mV). Sweep amplitude pairs (V₁,V₂).
2. For each pair: inject full symbol sequence, record lock-in quadratures per mode (12 time bins per symbol at 100 mode-1 cycles/symbol).
3. Select complementary pairs on validation split (best stack: 10 pairs).
4. Concatenate per-symbol features across pairs → single feature matrix.
5. Train one ridge readout on the stack; test NMSE on held-out data.

## Key Results

| Task / Protocol | One-mode | Two-mode best pair | Multiplexed stack |
|---|---|---|---|
| NARMA-2 test NMSE | 0.615 | 0.068 (20,120 mV) | **0.021** |
| NARMA-3 | 0.690 | 0.192 | **0.138** |
| NARMA-5 | 0.704 | 0.515 | 0.424 |
| NARMA-10 | — | 0.686 | 0.724 (gain gone) |
| Linear memory capacity MC | ~0.4 (1 lag only) | up to ~2.4 | — |

- **MC ranking surprise**: max memory capacity at mode-2-dominated pairs (20–30 mV on mode 1, rest on mode 2) with mode 1 near onset of nonlinearity — attributed to **coupled operating regime** (residual motion changes effective modal frequencies → history leaks into amplitude/phase), NOT to mode-2 lifetime (which is shorter).
- **Feedthrough control (h1 vs h2)**: same recordings, matched pipeline. On hard nonlinear maps (b): 0.137 (h2) vs 0.991 (h1); (c): 0.081 vs 0.848; NARMA-2: 0.021 vs 0.143. On easy sin(x) feedthrough is competitive — **matched-input linear baselines are mandatory before claiming physical-reservoir value** (echoes their Mackey-Glass short-horizon critique: strong input autocorrelation alone yields low error).
- **Memory ceiling is honest**: MC_p collapses within a few symbols at 100-cycle symbol duration (mechanical dissipation); NARMA error rises with order; 40-symbol temporal window on stored features does NOT rescue r≥4 — the information is absent from observations, stacking cannot create it.
- Throughput bound: symbol rate ~5.6×10⁴/s (f₁/100 cycles); multiplexing multiplies acquisition time by number of pairs (trade: repeated acquisition + digital feature storage for performance).

## Reusable Patterns

1. **Operating-point multiplexing**: any physical reservoir with a tunable operating point (drive split, bias, coupling) can be "enlarged" by replaying the same input under complementary settings and stacking responses — a cheap alternative to device arrays.
2. **Fixed-budget allocation**: constraining ΣV = const isolates *allocation* effects from total-energy effects — a clean ablation axis for physical RC.
3. **Internal linear feedthrough as control**: when hardware has parasitic direct paths, demodulate them separately and train a matched baseline — the honest null model for "is the nonlinearity doing anything?"
4. **Q/f lifetime rule**: for fading-memory claims, compute free-decay lifetime Q/f, not Q; high-frequency modes lose usable memory faster.
5. **Order-scaling diagnostic**: report NARMA-r across orders AND linear MC vs delay; attribute performance limits to information absence, not algorithm failure.
6. **Onset-of-nonlinearity sweet spot**: placing one mode just past its linear regime (near hysteresis) while parking most drive in a coupled partner maximised MC — the coupling, not raw amplitude, carries history.

## Limitations

- Multiplexing gain vanishes at NARMA-10 (memory ceiling); readout windowing doesn't help r≥4.
- Each stack element = separate physical recording ⇒ wall-clock cost scales with stack size.
- Single device family (NEMS beam, two flexural modes, piezo transduction); generalisation to other multimode platforms asserted not shown.

## vs Related Physical-RC Approaches

- **Single-mode MEMS RC / Kartal et al. NEMS**: one nonlinear mode — this work shows allocation across modes is the dominant upgrade.
- **Coupled resonator arrays (multi-device)**: hardware complexity grows; here one device's internal modes provide the coupling substrate.
- **Delay-based RC**: uses long delay lines for memory; here short mechanical memory is accepted and characterised instead.
- **Quantum/photonic reservoirs**: same feature-stacking idea applies wherever repeated passes with different operating points are possible.

## Implementation Sketch (feature stacking)

```python
# R: recorded responses per drive pair; each [n_symbols, n_bins, n_modes*2]
# (lock-in quadratures X,Y per mode per bin)
stacked = np.concatenate([resp[pair] for pair in selected_pairs], axis=-1)  # [n_symbols, feat]
ridge = train_ridge(stacked[train_idx], y[train_idx], alpha=validate_alpha)
y_hat = ridge.predict(stacked[test_idx])  # test NMSE
# Control: re-demodulate same recordings at h1 → linear feedthrough features
# → identical ridge pipeline → compare NMSE h2 vs h1 on hard maps only.
```
