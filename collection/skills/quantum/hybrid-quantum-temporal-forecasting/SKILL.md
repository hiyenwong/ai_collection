---
name: hybrid-quantum-temporal-forecasting
description: Hybrid quantum-classical temporal forecasting combining LSTM with Quantum Circuit Born Machines (QCBM) and QLSTM for financial time-series prediction, volatility forecasting, and temporal embedding learning. Use when working on: quantum finance, volatility forecasting, QCBM, QLSTM, hybrid quantum-classical financial models, temporal embeddings, NISQ financial applications, regime detection, or quantum-enhanced time series prediction.
---

# Hybrid Quantum Temporal Forecasting

Combine classical temporal deep learning (LSTM/Seq2Seq) with quantum machine learning components for financial time-series forecasting.

## Architecture 1: LSTM + QCBM (arXiv:2603.09789)

**Purpose**: Financial volatility forecasting via distribution learning.

### Workflow
1. Preprocess time series: log-returns, rolling statistics, sliding windows
2. Train LSTM encoder to extract temporal features
3. Feed LSTM hidden states as conditional parameters to QCBM
4. Train QCBM (parameterized quantum circuit, depth 2-4, 4-8 qubits) to learn conditional distribution of future volatility
5. Sample from QCBM to generate volatility distribution forecasts
6. Map quantum measurement outcomes to volatility estimates

### Key: Parameter-shift rule for quantum gradients; NISQ-compatible shallow circuits

## Architecture 2: QLSTM Seq2Seq Autoencoder (arXiv:2602.11578)

**Purpose**: Temporal embedding learning with smoother latent representations.

### Workflow
1. Replace standard LSTM gates with QLSTM gates containing depth-1 VQC
2. Build Seq2Seq encoder-decoder with QLSTM cells
3. Train with reconstruction objective on sequential data
4. Extract latent embeddings from encoder bottleneck
5. Use for regime detection, anomaly identification, downstream forecasting
6. Evaluate across rolling windows (e.g., 14 S&P 500 windows)

### Key: Depth-1 VQC minimizes noise; quantum layer shapes latent manifold geometry; benefits: smoother trajectories, clearer regime transitions

## Comparison

| Aspect | LSTM+QCBM | QLSTM Seq2Seq |
|--------|-----------|---------------|
| Task | Volatility forecasting | Temporal embedding |
| Quantum | QCBM (distribution) | QLSTM (feature transform) |
| Integration | Sequential: LSTM->QCBM | Embedded: VQC in gates |
| Best for | Risk management, VaR | Regime detection |

## Pitfalls
- Keep circuits shallow (depth <= 4) to avoid NISQ decoherence
- Normalize data before quantum circuit input
- Use larger batch sizes; quantum gradients are noisy
- Always compare against classical baselines
- Test on out-of-sample periods with different market regimes

## References
- Chen, Y. (2026). arXiv:2603.09789 - Hybrid QCBM for Volatility Forecasting
- Hsieh et al. (2026). arXiv:2602.11578 - QLSTM Seq2Seq Temporal Embeddings
