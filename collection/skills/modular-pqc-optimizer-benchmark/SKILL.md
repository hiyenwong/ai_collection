---
name: modular-pqc-optimizer-benchmark
description: Use when choosing VQA optimizer direction/update pairs.
category: ai_collection
version: "1.0.0"
source: arXiv:2610.10254
source_title: "Benchmarking Modular Optimization Strategies for Parameterized Quantum Circuits"
authors: "Carla Cotea, Stefan Balauca, Andreea Arusoaie (Alexandru Ioan Cuza University Iasi, FreeYa Mind Campus)"
published: 2026-10-07
categories: quant-ph, quantum-machine-learning
trigger_words:
  - parameterized quantum circuit optimization
  - search-direction estimator
  - parameter-shift rule
  - SPSA
  - PGPE
  - observable curvature preconditioning
  - VQA benchmark
  - QAOA optimizer
  - VQE optimizer
  - finite-shot cost accounting
---

# Modular PQC Optimizer Benchmark: Separating Search Direction from Update Rule

## Core Method

VQA optimization loop factorizes into two independent, composable components:

```
(p_k, s_k+1) = Update(d̂_k, s_k)    # classical update rule
θ_k+1 = θ_k − η_k · p_k              # parameter step
```

- **Search-direction estimators** (quantum side): PSR (parameter-shift, analytic), FiniteDiff, SPSA (simultaneous perturbation), PGPE (parameter-space exploration / smoothed-objective gradient), OCP (diagonal observable-curvature preconditioning).
- **Update rules** (classical side): SGD, Adam, RMSprop.
- **Derivative-free baselines** (native proposal+update coupled): COBYLA, Nelder–Mead, Bayesian optimization — NOT decomposed.

Pairing them independently (5×3 = 15 modular + 3 baselines) exposes whether a poor trajectory comes from direction-estimator bias/variance, classical update dynamics, or their interaction — something monolithic optimizer comparisons cannot show.

## Four Workloads (parameter count deliberately varied)

| Workload | Qubits | Params | Notes |
|---|---|---|---|
| MaxCut QAOA (p=2) | 5 | 4 | graph seed 42 fixed separately from optimizer seed |
| Iris classifier | 4 | 16 | MSE, minibatch 16 |
| Binary-MNIST QCNN | 8 | 63 | Z7 observable |
| H₂ VQE (STO-3G) | 4 | 3 | FCI ref −1.13727 Ha |

Settings: noiseless evolution + 256-shot sampling; 3 seeds (42/123/1234); selected configs on 156-qubit ibm_aachen hardware.

## Key Findings

1. **No component dominates alone**: peak vs mean ranking flips per task —
   - MaxCut: SPSA-SGD and PSR-Adam share peak (−4.3789) but **PGPE-SGD best mean** (−4.3451, most seed-stable); SPSA-SGD drops to −4.0625 at one seed → ranks 6th on mean.
   - VQE: PGPE-SGD best individual (0.0107 mHa at seed 42) but 13.7 mHa at another → 9th on mean; **FiniteDiff-RMSprop best mean** (2.69 mHa).
   - Both classifiers: **OCP-RMSprop best mean accuracy** (Iris 100% at all seeds; QCNN 96.67%) — advantage is consistency across seeds, not exclusive peaks.
2. **Update rule changes outcome at fixed estimator**: Iris at matched 52,800 circuits — RMSprop 100% vs SGD 75–80% (FiniteDiff/PSR). QCNN at 4,800 circuits — SPSA-Adam/RMSprop 90% vs SPSA-SGD 47.5%.
3. **Cost ≠ quality**: PGPE-RMSprop improves MaxCut objective 0.0039 over SPSA-SGD using **3.67× circuits**; OCP reaches 100% QCNN test with 404,800 circuits vs PGPE-Adam 97.5% at 17,600 (**23× more** for one extra correct of 40).
4. **Terminal vs best-observed divergence**: hardware minimum occurs before final step in 3/4 case studies (H₂ min at step 22 then deteriorates to 156.8 mHa terminal error). Terminal value alone hides achieved improvement; minimum-of-noisy-observations is downward-biased (simulator min −1.138991 Ha sits *below* FCI — finite-shot artifact, not physical).
5. **Hardware runs are case studies, not rankings**: 24 recorded parameter transitions verified to match implemented updates (SPSA σ, PGPE σ=0.1 lr=0.05 decay=0.01) — trajectory-level verification, single runs, no noise isolation.

## Reusable Patterns

1. **Factorize hybrid loops before benchmarking**: any classical-quantum iterative system (VQA, RL, Bayesian-opt) — separate "information acquisition" (direction estimator) from "state update dynamics" (learning-rate/momentum machinery), pair independently, report interaction effects. Monolithic comparisons only say which package won.
2. **Three-level cost accounting**: objective evaluation (one complete loss/energy at one θ) ≠ logical circuit execution (per sample × per observable setting) ≠ shots. Equal step counts do NOT mean equal budgets: PSR/OCP need 2 evaluations/parameter (63-param QCNN → 404,800 circuits), SPSA needs 3/step (4,800), PGPE needs 11-batch (center + 5 antithetic pairs). Report all three counts or comparisons are meaningless.
3. **Peak vs mean vs stability across seeds**: report all three separately; single-seed perfection (COBYLA 100% Iris on seed 42 with only 1,600 circuits, mean 81.67%) is one recorded outcome, not superiority.
4. **Fix the problem instance separately from the optimizer seed** (MaxCut graph seed 42 ≠ optimizer seeds) — otherwise the target objective changes per run and rankings are meaningless.
5. **Verify update-rule reproduction from logs**: recompute parameter transitions from recorded evaluations to confirm which optimizer actually ran (Runtime optimizer-name fields are often absent) — trajectory-level provenance.
6. **Honest hardware claims**: hardware runs demonstrate "improvement occurred on-device", not sim-to-real transfer, not noise attribution; matched simulator-hardware pairs give descriptive terminal/best deltas only.
7. **Finite-shot VQE below FCI ≠ better ground state** — selection under noise favors downward fluctuations; chemical-accuracy claims need independent reevaluation of the selected parameter state.

## Selection Heuristics (from this benchmark, descriptive not universal)

- Small param count + tight budget → SPSA-SGD (3 evals/step, near-peak quality)
- Mean-case robustness on combinatorial → PGPE-SGD
- Mean energy error on chemistry → FiniteDiff-RMSprop
- Classifier accuracy + seed consistency → OCP-RMSprop
- Very few queries, small problems → COBYLA (but check seed stability)
- Never conclude from terminal value alone; store best-θ checkpoint separately from final θ
