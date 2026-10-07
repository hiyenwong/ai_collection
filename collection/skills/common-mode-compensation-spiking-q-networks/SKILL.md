---
name: common-mode-compensation-spiking-q-networks
description: Use when low-timestep spiking Q-networks underperform; diagnose and fix common-mode Q errors.
category: ai_collection
---

# Common-Mode Error Compensation for Deep Spiking Q-Networks (CMC-DSQN)

**Source**: Xu, Guo, Sun, Dong, Yang & Yu (Peking University), "Common-Mode Errors Limit Low-Timestep Deep Spiking Q-Networks", arXiv:2610.07808 (Oct 2026, cs.NE).

## Problem

Deep spiking Q-networks (DSQNs) need many simulation timesteps T for competitive performance; cutting T (for energy) causes severe degradation. Why? Low-timestep SNNs suffer **disproportionate common-mode errors** — errors shared across all action Q-values — which are especially damaging to TD learning through bootstrapped targets.

## Error Decomposition (the diagnostic)

For action space A, given reference Q* and estimate Q, decompose per-state estimation error across actions:

```
common-mode error:     e_cm(s) = (1/|A|) Σ_a [Q(s,a) − Q*(s,a)]     # shared across actions
differential-mode err: e_dm(s,a) = [Q(s,a) − Q*(s,a)] − e_cm(s)      # relative-difference error
common-mode ratio:     ρ(s) = |e_cm(s)| / (|e_cm(s)| + |e_dm(s)|)
```

**Finding**: in low-T SNNs, common-mode RMSE ≫ differential-mode RMSE (ANNs are balanced). Common-mode errors corrupt TD targets `y = r + γ max_a' Q(s',a')` because the max operation propagates the shared bias into every bootstrap target — systematic, self-reinforcing value distortion. Removing common-mode errors (verified on CliffWalking with exact Q*) is far more effective than removing differential-mode errors.

## CMC-DSQN (the fix)

Auxiliary ANN `Q_ANN` estimates the common-mode Q component; final Q = action-wise mean-removed SNN output + ANN common-mode estimate:

```
CMC Q-value:  Q_CMC(s,a) = Q_SNN(s,a) − mean_a'[Q_SNN(s,a')] + Q_ANN(s)     (common-mode replaced)
```

Key properties:
- ANN and SNN process observations **independently** (no shared encoder), jointly optimized by the standard DQN TD loss. The ANN learns the shared component implicitly through TD — no ground-truth Q* needed.
- Greedy action selection is invariant to adding a per-state constant ⇒ **auxiliary ANN removed entirely at inference**; actions read directly from SNN outputs. Zero deployment overhead, SNN energy efficiency preserved.
- Don't train the ANN to predict the residual error directly (moving target); let TD learning shape the common-mode estimate.

## Results

- MiniAtar/Atari, low-timestep settings: outperforms SOTA DSQN baselines (DSQN, pbLN, DATSQN, CaRe-BN, TP-DSQN) by ~20% at T=2; surpasses the ANN baseline at T=4.
- CliffWalking case study: nearly all seeds stabilize; both common- and differential-mode RMSE drop markedly.

## When to Apply

- Deploying SNN-based value-based RL (DQN-family) on edge/neuromorphic hardware where timesteps are budget-limited
- Diagnosing unexplained instability of spiking value estimators (oscillating seeds, value drift)
- Any Q-estimator whose per-state errors are strongly correlated across actions — e.g., rate-coded outputs with shared membrane/bias states, quantized value heads. The decomposition + common-mode replacement generalizes beyond SNNs.
- Contrast with mean-based fixes (e.g., population/batch normalization of outputs): those only remove the empirical mean, not the TD-propagated common-mode component.

## Procedure

1. Measure: log Q(s,·) vs a reference (exact Q* on small envs, or ANN teacher); compute e_cm, e_dm, ρ per state.
2. If common-mode dominant (ρ high), attach auxiliary ANN producing scalar Q_ANN(s); form Q_CMC per the formula; train both nets with the DQN loss.
3. Evaluate stability across seeds (fraction of successful/stable seeds per eval point), not just mean return.
4. At deployment, drop the ANN; use SNN outputs for greedy action.

## Limitations

- Auxiliary ANN costs extra compute during training (not inference).
- Verified on value-based RL; policy-gradient SNN error structure may differ.
- Gains concentrate in low-timestep regime; at large T the vanilla DSQN error balance is closer to ANN.
