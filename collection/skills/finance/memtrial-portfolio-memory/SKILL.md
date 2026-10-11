---
name: memtrial-portfolio-memory
description: "MemTrial: Learning when to trust memory in LLM portfolio agents. Credits experiences with what they change via Banzhaf value and hierarchical Bayesian pooling. Improves best experience-learning agent utility by 21.2%."
tags: [portfolio-management, llm-agents, memory-credit, banzhaf-value, hierarchical-bayesian, financial-markets]
source: "arXiv:2610.11732"
utility_score: 0.87
---

# MemTrial: Learning When to Trust Memory in LLM Portfolio Agents

## Paper Metadata

- **arXiv ID**: 2610.11732
- **Title**: MemTrial: Learning When to Trust Memory in LLM Portfolio Agents
- **Authors**: Guanghao Wu, Zhuo Cai, Shoujin Wang, et al.
- **Published**: 2026-10-08
- **Categories**: cs.AI
- **Link**: https://arxiv.org/abs/2610.11732

## Abstract Summary

Large language model (LLM) agents for portfolio management learn from experience: they credit each experience in their memory with the outcome of the decisions that used it. In financial markets, however, this outcome mostly reflects the market move shared by all decisions on that date, so the credit tracks the market rather than the experience, and these agents often do worse than simply holding the equal-weight (1/N) portfolio. MemTrial asks how an agent can credit an experience with what it changes, and answers it by putting memory on trial: drafts of the same decision with and without an experience face the same market, so the outcome they share cancels in their difference. The agent drafts each decision with eight combinations of its retrieved experiences, chosen by a fractional factorial design, and credits each experience with its Banzhaf value. MemTrial pools credits across dates and similar experiences with a hierarchical Bayesian model, acts on them only after they have predicted unseen dates, and otherwise stays anchored at a conservative reference such as 1/N. On four benchmarks, MemTrial improves the utility of the best experience-learning agent by 21.2%, and with eight LLMs it beats every LLM-based baseline on InvestorBench.

## Key Contributions

1. **Memory-on-trial framework**: Credits experiences with what they change, not shared market outcomes
2. **Banzhaf value**: Averages differences across eight experience combinations (fractional factorial design)
3. **Hierarchical Bayesian pooling**: Pools credits across dates and similar experiences to reduce noise
4. **Conservative anchoring**: Stays at 1/N reference when credits haven't predicted unseen dates
5. **Empirical success**: 21.2% utility improvement over best experience-learning agent; beats all baselines on InvestorBench

## Research Implications

- **Credit assignment**: Solves credit assignment problem in financial markets where outcomes are shared
- **Causal reasoning**: Isolates effect of individual experiences by controlling for market conditions
- **Uncertainty quantification**: Hierarchical Bayesian model provides calibrated confidence
- **Risk management**: Conservative anchoring prevents overconfidence in unreliable memories
- **Multi-LLM ensembles**: Combining multiple LLMs improves robustness

## Practical Applications

- Build LLM agents for portfolio management with reliable memory
- Credit experiences based on their marginal contribution, not shared outcomes
- Deploy hierarchical Bayesian models for experience valuation
- Implement conservative anchoring when experience value is uncertain
- Create ensemble systems combining multiple LLMs for financial decisions

## Related Work

- LLM agents for finance
- Experience replay in RL
- Portfolio optimization
- Bayesian methods in finance
- Multi-agent systems for trading
