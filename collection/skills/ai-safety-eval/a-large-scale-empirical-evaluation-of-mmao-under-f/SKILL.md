---
name: a-large-scale-empirical-evaluation-of-mmao-under-f
description: Skill derived from arXiv paper 2606.31584: A Large-Scale Empirical Evaluation of MMAO Under Fair-Budget Continuous and Discrete Benchmarks
category: ai-safety-eval
created: 2026-07-23
arxiv_id: 2606.31584
utility: 1.0
---
# a-large-scale-empirical-evaluation-of-mmao-under-f

Derived from arXiv paper [2606.31584]: A Large-Scale Empirical Evaluation of MMAO Under Fair-Budget Continuous and Discrete Benchmarks

## Abstract
This paper evaluates the Metabolic Multi-Agent Optimizer (MMAO) under a stricter empirical protocol rather than reintroducing the framework itself. The study asks whether MMAO's closed-loop resource-allocation principle remains credible under broader, more standard, and more explicitly budget-controlled continuous and discrete benchmarks. The main completed matrix covers eight CEC2017 functions at 10D and 30D with 20 seeds each, and five TSPLIB instances with 20 seeds each, together with stronger reproducible baselines including PSO-lite, ES-lite, and an iterated-greedy 2-opt route baseline. We further add trajectory-level diagnostics for communal budget, success rate, role evolution, and population turnover, plus an auxiliary OR-Library multiple-knapsack slice to extend the discrete evidence beyond routing. Under this protocol, MMAO clearly outperforms the external baseline set on the continuous side and on the TSPLIB side, while the ablation variants remain much closer to the full method than the external baselines are. We therefore position MMAO as a benchmark-backed cross-domain adaptive framework whose most clearly validated value is endogenous resource redistribution under evidence pressure, while also noting that the strongest remaining gap is not basic workability but sharper mechanism isolation and broader competition-grade comparison.

## Authors
Jinliang Xu, Liping Ma

## Published
2026-06-30

## Categories
cs.NE, cs.MA

## Utility
1.0

## Note
This skill was automatically generated from the arXiv paper as part of the daily cron job.
