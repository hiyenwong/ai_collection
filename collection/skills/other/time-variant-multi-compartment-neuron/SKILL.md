---
name: time-variant-multi-compartment-neuron
description: Time-variant spiking neuron design for selective retention.
trigger: spiking neuron design, time-variant dynamics, TV-MCN, internal time, multi-compartment neuron, unified state-dynamics framework, selective copying, MAD ICR, STORE-RECALL, input-dependent readout, input integration modulation, spiking sequence modeling, SNN temporal processing, resonant compartments, ZOH discretization
category: ai_collection
---

# TV-MCN — Time-Variant Multi-Compartment Spiking Neuron

Source: arXiv:2610.23981 (Jing Yang, Qianhui Liu, Gang Pan, Zhanglu Yan — Shandong U / Zhejiang U / NUS; cs.NE, 14 Oct 2026). A unified state-dynamics framework that exposes a common limitation of all existing spiking neurons — TIME-INVARIANT dynamical rules — plus TV-MCN, which makes input integration, state evolution, and state readout input-dependent.

## Unified state-dynamics framework

Abstract any spiking neuron as a three-stage state-dynamics model:

```
ḣ(t) = A·h(t) + B·x(t)        # (1) input integration & state evolution
u(t) = C·h(t)                  # (2) state readout -> membrane potential
s(t) = H(u(t)−θ),  h(t+) = R(h(t−), s(t))   # (3) spike generation & recovery
```

- h = internal states carrying information; A governs decay/oscillation of state evolution; B determines how the current input is integrated into states; C specifies how states are read out.
- Existing neurons are parameterizations of (h, A, B, C): LIF (h=u, A=−τm⁻¹), ad-LIF (adaptation state), TC-LIF (two compartments), DGN (gated), DH-LIF (heterogeneous time constants), HetSyn (multi-timescale synaptic-current states), D-RF (resonant complex modes −τi⁻¹+jωi), PMSN (coupled compartments). **All share time-invariant A, B, C** — richer states and richer A-structures do not let the neuron adapt HOW information is processed as relevance changes over time.
- Biological contrast (the design motivation): membrane conductance changes modulate the effective membrane time constant (state-evolution rate, Cavallari 2014); NMDA receptors modulate input integration (Li & Gulledge 2021); dendritic/somatic inhibition modulates state contributions to the somatic response (Jadi 2012) — biological rules are continuously regulated during processing (Schulz 2006).

## TV-MCN design

1. **Input-dependent internal time**: introduce internal time τ with progression coefficient `dτ/dt = ∆t > 0`, where `∆t = softplus(b∆ + W∆·qt)`, `qt = SiLU(Wq·xt)`. State dynamics in internal time dh/dτ = A·h + Bt·x become, by the chain rule, `dh/dt = ∆t·A·h + ∆t·Bt·x` in external time. Small ∆t slows internal time → information preserved longer; large ∆t accelerates evolution → stored information changes/decays faster.
2. **Multiscale complex compartments**: `A = diag(−e^{a1}+jω1, …, −e^{aN}+jωN)` with learnable (ai, ωi). The parameterization −e^{ai} < 0 keeps every decay rate negative by construction; ωi sets each compartment's oscillation frequency (multiscale retention + resonant frequency response).
3. **Dynamic integration & readout**: `Bt = WB·xt` (which parts of the current input are written into states) and `Ctᵀ = WC·xt` (which stored states contribute to the membrane potential `u = Ctᵀ·h`).
4. **Discrete-time (ZOH, exact under constant input per step; identity verified numerically)**:
   `Āt = exp(∆t·A)`, `B̄t = A⁻¹(exp(∆t·A) − I)·Bt`;
   `ht = Āt·h_{t−1} + B̄t·xt`; `ut = Ct·ht`; spike when Re(u) crosses θ; soft reset after firing.

## Results

- **Temporal classification** (accuracy %, same FC architecture): GSC 90.56 / SSC 70.98 / DVS128 Gesture 93.75 — all best; SHD 88.30 (2nd; HetSyn 88.60). Baselines: LIF 78.97/53.98/74.73/87.85; HetSyn 90.00/66.76/88.60/89.58; D-RF 87.44/61.85/86.13/92.01.
- **Synthetic sequence tasks** (best on ALL six): Adding MSE 0.0022×10⁻¹ (D-RF 0.0161); Selective Copying 93.46% (2nd: D-RF 19.24 — 4.9× gap); MAD ICR 100.00 (HetSyn 97.44); MAD Noisy ICR 99.99 (HetSyn 85.43, D-RF 40.15); 20D STORE-RECALL 99.92 (DH-LIF 99.27); Induction 97.71 (D-RF 21.04, DH-LIF 21.15).
- **Ablations** (Selective Copying, multiscale states retained): full model 93.46% token / 37.72% exact; without internal-time modulation 7.20% / 0.00% (output collapses to a repeated single token); without dynamic B/C (static learnable B0, C0) 61.24% / 0.02%.
- **Interference robustness** (+2048 irrelevant inputs before recall, no retraining): full model drops only 0.88 pp; static B/C drops 9.33 pp.
- **Mechanism demo** (STORE-RECALL, identical content stream, only the STORE instruction selects A or B): the full model LOWERS ∆t during the instructed STORE window — slowing state evolution precisely then — so the selected content persists until recall while the unselected content decays. Without internal-time modulation both decay regardless of instruction.

## When to use

- SNN sequence tasks requiring selective retention/retrieval under distractors: selective copying, instruction-dependent store/recall, associative recall with noisy/irrelevant inputs, induction.
- Designing or auditing spiking neurons: use the (A, B, C) parameterization to place any neuron in one table and check whether its dynamical rules are time-invariant — that is the axis along which TV-MCN improves.
- Input-adaptive temporal processing — the three time-variant levers: WHAT gets written (Bt), WHAT is read out (Ct), and HOW FAST states evolve (∆t).
- Building surrogate mechanistic accounts of biological regulation: conductance→time-constant, NMDA→integration, inhibition→readout map onto ∆t, Bt, Ct respectively.
