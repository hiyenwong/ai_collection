---
name: quantum-neuroplastic-learning
description: Use when quantum reservoirs need structural plasticity.
category: ai_collection
tags: [quantum-reservoir-computing, neuroplasticity, eligibility-traces, structural-plasticity, reservoir-computing, quantum-machine-learning]
---

# Quantum Neuroplastic Learning (QNL)

**Source**: Laskar, M.R., "Quantum neuroplastic learning for time-series processing", arXiv:2610.34055 (KTH Royal Institute of Technology, Oct 2026). Validated on IBM ibm_fez (Heron r2, 42 qubits, 1.28M shots).

## Core Idea

Two-level learning for quantum reservoir computing (QRC), modeled on biological memory consolidation:
- **Fast level** (analogous to synaptic weight changes / short-term memory): linear readout `w` trained per task, as in conventional QRC.
- **Slow level** (analogous to synapse formation/elimination/pruning / structural plasticity): the physical configuration `θ` itself — active couplers + strengths, local fields, gate angles, evolution time — is reorganized through discrete local edits, one per plasticity block.

Key payoff: plasticity helps most where the task demands **more memory than the fixed reservoir provides** (long-term recall, high-order NARMA, forecasting, channel equalization). No additional qubits; measurement protocol and readout architecture unchanged.

## The Learning Rule

Reservoir dynamics: `ρ_k = Φ_θ(s_k)[ρ_{k−1}]`, features `x_k = M(ρ_k)`, output `ŷ_k = w^T x_k`. Loss `L(θ; ξ)` is evaluated on stream segments not used to train the readout.

Each plasticity block b:

1. **Nominate** K candidates `θ_c`, each differing from `θ^(b)` by ONE local edit (add coupler / remove coupler / change field / change gate angle / change clock). Edit type κ drawn with probability `p_κ` (below); target coupler/qubit uniform; value uniform from an alphabet.
2. **Paired evaluation**: run current θ AND all K candidates on the SAME `N_str` freshly drawn streams ξ_r → paired loss reductions `g_{c,r} = L(θ; ξ_r) − L(θ_c; ξ_r)`, mean `ḡ_c`, std `s_c`. Pairing kills stream-difficulty variance.
3. **Statistical admission gate** (Student-t lower confidence bound, one-sided, Bonferroni-corrected over K candidates and B blocks, δ' = 0.05/(KB)):
   `LCB_c = ḡ_c − t_{1−δ', N_str−1} · s_c/√N_str`  (S1)
4. **Complexity cost**: admission margin
   `Γ(θ_c; θ) = LCB_c − α·[ΔN_c]+`  (S2)
   where `ΔN_c` = number of ADDED couplers, `[z]+ = max(z,0)`, α = 0.002. Removal is free (bounded-connectivity prior, cf. cortical rewiring limits).
5. **Admit** the maximizing candidate `c*` iff `Γ(θ_{c*}; θ) > 0`; else keep θ. Readout is refit during every loss evaluation.
6. **Eligibility traces** over edit types (synaptic-tag / three-factor analogy — Γ is the global consolidation signal):
   `e_κ ← λ·e_κ + [Γ(θ_{c*}; θ)]+ + 1{κ=κ(c*)}`  (S3, accumulating trace, decay λ)
7. **Edit-type selection** (Boltzmann softmax mixed 50/50 with uniform exploration):
   `p_κ = ½·e^{e_κ/T} / Σ_{κ'} e^{e_{κ'}/T} + ½·1/|K|`  (S4)
   Uniform floor ≥ 1/(2|K|) keeps every edit type reachable.

Settings used: K=4 candidates/block, N_str=8 paired streams, B=10 blocks/run, α=0.002.

QNL requires only forward loss evaluations (which a reservoir computer produces in normal operation) → applicable to physical reservoirs with measurement back-action and sampling noise. Once frozen, a QNL configuration runs with the same protocol as the base reservoir.

## Distinction from Adjacent Methods

- vs. **variational quantum algorithms (VQA)**: VQA optimizes continuous parameters of a FIXED circuit structure via gradients; QNL makes discrete, gradient-free structural edits (coupler add/remove) admitted by a statistical bound. Structure changes, not just parameters.
- vs. **offline random search / tuning**: matched-budget tuned baseline (same 80 candidate evaluations) matched QNL in simulation on single tasks; QNL's advantages are (a) incremental improvement of the configuration IN USE, (b) interpretable local edits, (c) continued adaptation across task switches without restarting search, (d) operation under deployed back-action/sampling noise.
- vs. **EARLY/evolutionary reservoir search**: no population, no generations — one-edit-at-a-time hill climbing gated by paired statistics, directed by eligibility traces.

## Algorithm (pseudocode)

```
initialize θ (base reservoir), eligibility traces e_κ = 0 for all edit types
for b = 1..B:                       # plasticity blocks
    C = [draw K candidate edits via p_κ (eq S4), apply each to θ]
    for r = 1..N_str:               # paired fresh streams
        ξ_r = fresh_input_stream()
        L_cur[r]  = eval_loss(θ,  ξ_r, refit_readout=True)
        for c in C: L_cand[c][r] = eval_loss(θ_c, ξ_r, refit_readout=True)
    for c in C:
        g_c = [L_cur[r] - L_cand[c][r] for r]      # paired reductions
        LCB_c = mean(g_c) - t_quantile(1-δ', N_str-1) * std(g_c)/sqrt(N_str)
        Γ_c = LCB_c - α * max(0, added_couplers(θ_c) - added_couplers(θ))
    c* = argmax_c Γ_c
    if Γ_{c*} > 0:
        θ = θ_{c*}
        e_κ ← λ·e_κ + [Γ_{c*}]+ + (1 if κ(c*)==κ else 0)
    else:
        e_κ ← λ·e_κ for all κ     # pure decay
return θ (frozen config; execute with base protocol)
```

## Results Summary

- Monitored erase-and-write 5-qubit Ising reservoirs (RSP / OLP-int / OLP-weak): summed short-term-memory capacity +0.99 (RSP); long-term recall gains largest for high-memory tasks.
- Continual adaptation: through sequences of 16 task switches (4 STM windows × 3 NARMA orders), QNL continues adapting from its current configuration (no restart); mean post-switch capacity 0.87 vs 0.69 fixed.
- NISQRC channel equalization (2+4 qubit ansatz, 20 dB): error 6.7e-3 → 1.5e-3 (exact); 2.1e-2 → 3.1e-3 (105-shot sampling); beats matched-budget tuned baseline.
- **Hardware transfer** (ibm_fez): 6× seven-qubit reservoirs in parallel on 42 qubits, 1.28M shots; simulation-learned frozen configs cut symbol error rate 9.7% → 2.2%, below matched-budget tuned baseline.

## Reusable Design Principles (beyond quantum)

1. **Structural edits on top of parametric readout**: when a dynamical-system learner underperforms on memory-heavy tasks, edit its TOPOLOGY (add/remove connections, change timescales), not just its readout.
2. **Paired-stream statistical gating**: admit a change only when a Student-t LCB on the PAIRED improvement over shared fresh data clears zero — controls false admissions under noise, at modest N_str (~8).
3. **Complexity cost on additions**: charge α per added connection; removal free → drives toward minimal sufficient connectivity (structural simplicity emerges, not imposed).
4. **Eligibility traces as credit assignment across edit types**: accumulate positive admission margins per edit TYPE (not per edit instance), mix Boltzmann exploitation with a uniform exploration floor — adapts the SEARCH DISTRIBUTION, not just the solution.
5. **Continual re-adaptation**: keep the learned config as the starting point at task switch; sequential statistical gates protect against catastrophic drift.
6. **Sim-learned, frozen-transfer**: learn structure in simulation where shot budget is cheap (~1e9 shots), freeze, then execute on hardware with the base protocol — bridges the noise gap without hardware-in-the-loop cost.

Applies to: physical reservoirs (photonic, mechanical, analog RC), neuromorphic hardware re-adaptation after calibration drift, hyperparameter/structure search with noisy evaluations, any black-box discrete structure optimization where each evaluation is expensive and noisy.

## Pitfalls

- Admission bound is nominal: assumes paired gains across independent streams are t-distributed; violations (correlated streams) inflate false admissions.
- QNL re-evaluates the current config every block (~25% extra stream evaluations vs. pure candidate budget) — budget comparisons must match this.
- Strong measurement back-action limits what reorganized configurations can retain — plasticity cannot beat the information-disturbance trade-off of monitored reservoirs.
- Retention of earlier tasks after switches was NOT tested (open limitation).
- Learning cost ~1e9 simulated shots → learning on-device needs early-stopping sequential tests or parallel candidate evaluation.

## Key References
- Synaptic tagging & capture, three-factor learning rules (eligibility trace + global consolidation signal) — the biological template for eqs (S3)-(S4).
- Monitored reservoir computing (information-disturbance trade-off), NISQRC (reset-readout reservoirs).
- arXiv:2610.34055 — full derivations in Supplementary Notes 1 (rule), 2-3 (reservoir models), 10 (statistics).