---
name: prediction-markets-option-arbitrage
description: "Prediction market pricing benchmark methodology — comparing prediction market prices (Polymarket) with option-implied risk-neutral probabilities from centralized exchanges (Binance/Deribit). Use when analyzing prediction market efficiency, cross-venue price discovery, crypto derivatives pricing, market fragmentation effects, and speculative demand wedges."
metadata:
  arxiv_id: "2606.19517"
  published: "2026-06-19"
  category: "q-fin.TR"
---

# Prediction Market Option Arbitrage

## Core Methodology

First benchmark test of prediction-market pricing efficiency by comparing Polymarket Yes prices with discounted risk-neutral binary values from listed call options on the same underlying, strike, and maturity.

### Key Findings
- **Mean pricing gap**: 5.6pp (Polymarket vs Binance) across 214 hourly observations (t=6.46, p<10^-9)
- **Pooled gap**: 6.3pp across three Binance-compatible Bitcoin threshold markets (287 observations)
- **Persistence**: AR(1) half-life ~4 hours, yet mean-reverting → slow info transmission between segmented venues
- **Cross-sectional pattern**: Wedge largest at low option-implied probabilities and long maturities → speculative demand, not measurement error
- **Deribit extension**: Larger pooled gap of 11pp on same contracts; Ethereum exercise yields mixed evidence
- **Arbitrage viability**: Delta-hedged arbitrage proxy profitable after conservative transaction costs (marginal statistical precision)

### Analysis Framework

1. **Match sampling**: Identify identical payoffs across prediction markets and option exchanges
2. **Risk-neutral extraction**: Compute binary option values from vanilla option surfaces
3. **Statistical inference**: HAC and block-bootstrap for time-series correlation
4. **Cross-sectional analysis**: Regress gap on probability level, maturity, volatility regime
5. **Arbitrage test**: Delta-hedged proxy with transaction cost bounds

### Economic Interpretation
Persistent pricing wedges indicate **market fragmentation** rather than mechanical noise. Speculative demand for prediction market contracts (narrative-driven trading) creates systematic overpricing relative to professional derivatives venues.

## Activation Keywords
- prediction market pricing, option-implied probabilities, market fragmentation, Polymarket, Binance options, price discovery, speculative demand wedge, crypto derivatives, cross-venue arbitrage
