---
name: mmao-cls-metabolic-multi-agent-optimization-for-jo
description: Skill derived from arXiv paper 2607.01539: MMAO-Cls: Metabolic Multi-Agent Optimization for Joint Feature Selection and Classifier Tuning
category: multi-agent-rl
created: 2026-07-23
arxiv_id: 2607.01539
utility: 0.97
---
# mmao-cls-metabolic-multi-agent-optimization-for-jo

Derived from arXiv paper [2607.01539]: MMAO-Cls: Metabolic Multi-Agent Optimization for Joint Feature Selection and Classifier Tuning

## Abstract
This paper studies whether the Metabolic Multi-Agent Optimizer (MMAO) can act as a credible outer-loop optimizer for classification model selection. We propose MMAO-Cls, a mixed-space realization in which each agent jointly encodes a binary feature mask and classifier hyperparameters, while private energy, communal budget, role drift, and lifecycle turnover are mapped to the accuracy-complexity tradeoff of wrapper learning. The implementation is strengthened by deriving feature-budget adaptation from feature-information priors and by regularizing validation reward with both subset compactness and train-validation overfitting gap. We evaluate MMAO-Cls on seven standard tabular benchmarks with three seeds each and compare it against RandomSearch, GA-lite, PSO-lite, and an endogenous no-sharing ablation. On the aggregate validation objective, MMAO-Cls ranks second ($0.9433$) behind GA-lite ($0.9446$). On held-out test performance, it reaches mean score $0.8882$, improving over RandomSearch ($0.8808$) and GA-lite ($0.8857$), remaining close to PSO-lite ($0.8874$) and the no-sharing ablation ($0.8900$), while using the most compact mean held-out feature subset among all compared methods (feature ratio $0.4881$). Pairwise tests show that these margins are not yet statistically significant. The resulting claim is therefore conservative: MMAO-Cls supports classification applicability and compact mixed-space search more clearly than it isolates communal sharing as a decisive standalone advantage.

## Authors
Jinliang Xu, Liping Ma

## Published
2026-07-01

## Categories
cs.NE, cs.LG, cs.MA

## Utility
0.97

## Note
This skill was automatically generated from the arXiv paper as part of the daily cron job.
