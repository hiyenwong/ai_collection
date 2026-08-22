---
name: arxiv-2608-19899-the-impact-of-feature-engineering-and-an-optimisat
description: 'The impact of feature engineering and an optimisation framework for ocean colour machine learning (arXiv: 2608.19899)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# The impact of feature engineering and an optimisation framework for ocean colour machine learning

**Authors:** Edson Silva, Julien Brajard, Simon Cappe, Lasse H. Pettersson, François Counillon
**arXiv:** 2608.19899
**Utility:** 1.00
**Published:** 2026-08-20T11:07:54Z
**Link:** http://arxiv.org/abs/2608.19899

## Abstract

Machine learning (ML) is widely used for the development of ocean colour algorithms, but most studies focus on model parameter training and hyperparameter tuning. The optimisation of the data that feeds the models - i.e., Feature Engineering (FE) - is not fully explored. We assess the impact of FE in ocean colour machine learning models and we propose an optimisation framework that includes seven sequenced levels of data transformation: i. band choice, ii. log scaling, iii. spectral shape normalisation, iv. index extraction, v. principal component analysis, vi. feature scaling, and vii. zero-to-one scaling. We demonstrate the application for Multi-layer perceptron, Support Vector Machines, and eXtreme Gradient Boosting Trees on Sentinel-3 OLCI observations in the Norwegian coastal waters. The models are trained to estimate Chlorophyll-a concentration [Chl-a] and Secchi disk depth (Zsd). Results show that accuracy is highly variable among FE found in six studies using Sentinel-3 OLCI and the ones that we optimise. The R range from 0.01 to 0.55 for [Chl-a] and from 0.15 to 0.68 for Zsd, where the optimised FE shows the top results. The ML models with optimised FE could also improve by two times the R and reduce up to 63% of the mean absolute error when compared to CHL_OC4ME and CHL_NN standard algorithms. Nevertheless, no common optimised FE is found for all target variables and ML models, suggesting that FE optimisation is necessary for each application. Therefore, our proposed framework can be key for improving the accuracy of water quality monitoring in coastal waters.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "The impact of feature engineering and an optimisation framework for ocean colour machine learning". 
The paper presents novel ideas in multi-agent-rl that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.19899
