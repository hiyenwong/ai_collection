---
name: recap-regime-adaptive-portfolio
description: "Regime-aware Continual Adaptive Portfolio management (ReCAP) — integrating continual learning into portfolio management via adaptive regime detection, policy libraries, and regime-gated policy combination. Accepted by KDD 2026. Activation: regime detection, portfolio management, continual learning, adaptive trading, ReCAP, market regime, policy library, regime shift."
category: finance
---

## Context

Financial markets exhibit frequent regime shifts (bull/bear, high/low volatility) that render static portfolio optimization ineffective. ReCAP (Regime-aware Continual Adaptive Portfolio management) addresses this by combining regime detection with continual learning, enabling trading agents to accumulate and transfer knowledge across sequential market regimes. Paper: arXiv:2606.00143, accepted by KDD 2026.

## Core Methodology

1. **Adaptive Regime Detection**: Segment historical market data into variable-length regimes using statistical change-point detection. Each regime represents a distinct market state (volatility level, trend direction, correlation structure).

2. **Policy Library Construction**: For each detected regime, learn and store a regime-specific policy vector. The policy library serves as a knowledge repository that grows as new regimes are encountered.

3. **Regime-Gate Module**: During live trading, a regime-gate adaptively combines policy vectors from the library based on the current market state. The gate weights determine which historical regimes are most relevant to current conditions.

4. **Selective Continual Update**: Only the regime-gate and the current regime's policy vector are continually updated. Historical policies are frozen to prevent catastrophic forgetting. This preserves accumulated knowledge while allowing rapid adaptation.

## Implementation Steps

1. Collect historical market data (prices, volumes, features) and compute regime-sensitive indicators
2. Apply change-point detection algorithm (e.g., PELT, binary segmentation) to identify regime boundaries
3. For each regime, train a policy vector (e.g., portfolio weights) using the regime-specific data
4. Store policies in a dictionary: `{regime_id: policy_vector}`
5. In live trading:
   - Detect current regime using recent window of data
   - Query policy library for similar historical regimes
   - Regime-gate computes weighted combination of policy vectors
   - Execute combined portfolio allocation
   - Update only current regime's policy and gate weights

## Key Results

- Outperforms rolling-window retraining and naive online fine-tuning across 5 real-world datasets
- Superior returns in long-term investment horizons
- Rapid adaptation to regime shifts without catastrophic forgetting
- Lower computational cost than full retraining approaches

## Pitfalls

- **Regime Detection Latency**: Change-point detection operates on historical data; real-time regime identification has inherent lag. Use shorter detection windows for faster response but risk false positives.
- **Policy Library Explosion**: Too many detected regimes create an unmanageably large policy library. Consider merging similar regimes using clustering or similarity thresholds.
- **Overfitting to Historical Regimes**: Policies trained on specific regimes may not generalize to novel market conditions. Include regularization or policy smoothing.
- **Gate Training Instability**: The regime-gate module can become unstable during extreme market events. Use gradient clipping and learning rate scheduling.

## Verification

- Compare ReCAP performance against: (1) rolling-window baseline, (2) naive online fine-tuning, (3) buy-and-hold benchmark
- Measure regime detection accuracy using held-out labeled regime data
- Verify that historical policy vectors remain stable (frozen) during continual updates
- Test adaptation speed after synthetic regime shifts in backtest

## Activation

regime detection, portfolio management, continual learning, adaptive trading, ReCAP, market regime, policy library, regime shift, catastrophic forgetting, online learning, financial time series, dynamic allocation
