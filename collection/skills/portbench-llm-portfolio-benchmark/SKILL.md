---
name: portbench-llm-portfolio-benchmark
description: "PortBench: correlation-aware full-pipeline benchmark for LLM-driven portfolio management. Dual-layer evaluation (static QA + dynamic allocation pipeline) with CEPS metric for compounding reasoning errors. 90% of LLMs fail to beat equal-weight. arXiv:2605.27887"
tags: ["portfolio-management", "llm-benchmark", "finance", "quantitative-finance"]
arxiv_id: "2605.27887"
---

# PortBench: LLM-Driven Portfolio Management Benchmark

Correlation-aware, full-pipeline benchmark for evaluating LLM performance in portfolio management. Published 2026-05-27 (arXiv:2605.27887).

## Core Problem

LLMs show strong performance on financial QA tasks, but portfolio management (PM) remains poorly benchmarked. Two main gaps in existing benchmarks:

1. **Ignore cross-asset correlations** — cannot distinguish genuinely diversified portfolios from concentrated ones
2. **Fail to evaluate complete PM pipeline** — don't test the real-world decision cycle

## Methodology

### Benchmark Design

**Six heterogeneous asset classes** over 10 years of historical data.

**Two complementary evaluation layers:**

1. **Static QA layer**: 6,269 correlation-based questions across 7 task templates
2. **Dynamic pipeline layer**: 5-stage allocation pipeline mirroring real PM decision cycle
   - Stage 1: Market regime assessment
   - Stage 2: Asset selection
   - Stage 3: Weight allocation
   - Stage 4: Risk constraint check
   - Stage 5: Rebalancing decision

### Novel Metrics

**Dual-Layer Correlation Score**: Measures whether proposed portfolios exploit inter-class hedging and avoid intra-class concentration.

**CEPS (Compounding Error Propagation Score)**: Quantifies how reasoning errors compound across pipeline stages. Critical insight: errors at early stages amplify through the decision chain.

### Evaluation Protocol

- **10 frontier LLMs** evaluated
- **3 historical stress regimes**: market crashes, volatility spikes, liquidity crises
- **3 risk profiles**: conservative, moderate, aggressive
- **Strategy robustness** and **investor alignment** assessment

## Key Findings

1. **90% of LLM-profile combinations fail to outperform equal-weight allocation** — despite strong performance on static financial QA
2. **Procedural compliance ≠ performance** — models satisfying every constraint still suffer catastrophic drawdowns under stress
3. **Static QA performance does not transfer to portfolio decisions** — the gap between knowledge and action is large
4. **Cross-asset correlation awareness is the key differentiator** — portfolios that don't account for hedging relationships underperform systematically

## Reusable Skill Patterns

### Pattern 1: Correlation-Aware Benchmarking
```
When evaluating financial AI systems:
1. Test cross-asset correlation structures, not just single-asset predictions
2. Measure hedging effectiveness and diversification quality
3. Compare against naive baselines (equal-weight, market-cap weighted)
```

### Pattern 2: Pipeline-Stage Error Analysis
```
For multi-stage decision systems:
1. Decompose the decision pipeline into discrete stages
2. Track error propagation: CEPS measures compounding effects
3. Identify which stages contribute most to final performance degradation
```

### Pattern 3: Stress Regime Testing
```
Robust financial evaluation requires:
1. Testing under multiple historical stress scenarios
2. Separate evaluation for different risk profiles
3. Measuring drawdown severity, not just returns
```

### Pattern 4: Procedural vs Performance Decoupling
```
Constraint satisfaction does not guarantee performance:
1. Evaluate both procedural compliance AND outcome quality
2. Models can follow all rules and still underperform
3. Need outcome-based metrics beyond checklist validation
```

## Application Areas

- LLM evaluation for financial tasks
- Portfolio management system benchmarking
- Multi-stage decision pipeline analysis
- Cross-asset correlation modeling
- Stress testing of AI financial advisors
- Quantitative finance research

## Pitfalls

- **LLM QA ≠ portfolio skill**: Strong financial knowledge doesn't translate to good portfolio decisions
- **Correlation blindness**: Many models ignore cross-asset relationships
- **Stress regime fragility**: Models perform well in normal conditions but fail catastrophically under stress
- **Equal-weight is a strong baseline**: Any portfolio strategy must beat 1/N allocation to be useful
