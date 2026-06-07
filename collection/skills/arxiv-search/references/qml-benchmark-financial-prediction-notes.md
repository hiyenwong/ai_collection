# QML Benchmark Financial Prediction — Key Data Points

Collected from arXiv: 2601.03802 (2026-01-07). Authors: Rehan Ahmad, Muhammad Kashif, Nouhaila Innan, Muhammad Shafique.

## Performance Numbers

| Task | Model | Stock | Metric | QML | Classical | Delta |
|------|-------|-------|--------|-----|-----------|-------|
| Directional Classification | Hybrid QNN vs ANN | AAPL | AUC | +3.8 | baseline | +3.8 |
| Directional Classification | Hybrid QNN vs ANN | AAPL | Accuracy | +3.4 | baseline | +3.4 |
| Directional Classification | Hybrid QNN vs ANN | KCHOL | AUC | +4.9 | baseline | +4.9 |
| Directional Classification | Hybrid QNN vs ANN | KCHOL | Accuracy | +3.6 | baseline | +3.6 |
| Live Trading | QLSTM vs LSTM | S&P 500 | Risk-adjusted returns | Higher in 2/4 regimes | Higher in 2/4 regimes | Regime-dependent |
| Volatility Forecasting | QSVR (angle-encoded) vs SVR | KCHOL | QLIKE | Lowest | Higher | QML wins |
| Volatility Forecasting | QSVR (angle-encoded) vs SVR | S&P500/AAPL | QLIKE | Within 0.02-0.04 of best classical | Best classical | Classical wins narrowly |

## Key Insight
QML advantage emerges when data structure and circuit design are well-aligned. Not a universal advantage — scenario-dependent.

## Credit Scoring — IQNN-CS (arXiv: 2510.15044)
- Framework: Variational QNN + post-hoc explanation for structured financial data
- Novel metric: ICAA (Inter-Class Attribution Alignment) — quantifies attribution divergence across predicted classes
- Goal: Transparent QML for regulated financial decision-making (credit scoring)
