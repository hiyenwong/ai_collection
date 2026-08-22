---
name: arxiv-2608-20024-systematic-evaluation-of-tabpfn-ts-for-zero-shot-p
description: 'Systematic Evaluation of TabPFN-TS for Zero-Shot Probabilistic Heat Load Forecasting in District Heating Networks (arXiv: 2608.20024)'
category: ai-safety-eval
version: "1.0"
date: 2026-08-22
---

# Systematic Evaluation of TabPFN-TS for Zero-Shot Probabilistic Heat Load Forecasting in District Heating Networks

**Authors:** Ben Spoek, Karim K. Ben Hicham, Kai Derzsi, Philipp Althaus, Alexander Mitsos, Dirk Müller
**arXiv:** 2608.20024
**Utility:** 1.00
**Published:** 2026-08-20T13:33:37Z
**Link:** http://arxiv.org/abs/2608.20024

## Abstract

District heating energy hubs require reliable heat load forecasts for efficient operational scheduling. Conventional forecasting workflows train system-specific models on historical data, which can become burdensome when networks change through new consumers, retrofits, or changing operating regimes. Zero-shot time-series foundation models and in-context forecasting offer a promising alternative: they can adapt at inference time from recent observations rather than by repeated retraining. This study systematically evaluates TabPFN-TS against time-series foundation models and trained machine-learning baselines for probabilistic heat load forecasting in district heating networks. Unlike foundation models pretrained on large collections of real time series, TabPFN-TS relies on synthetic pretraining data, which avoids direct pretraining-test overlap but raises the question of whether the learned prior captures district heating dynamics. We analyze covariate choice, context length, temporal resolution, and prediction horizon on representative operating weeks, validate the selected configuration over a full year, and test transferability on a second network. The results identify hourly 24-hour forecasting with a 12-week rolling context and ambient temperature as a parsimonious high-performing configuration; longer context windows do not improve accuracy. TabPFN-TS remains close to Chronos-2 in deterministic accuracy, reaching CVRMSE values of 13.06% versus 12.48% on the main dataset, and lies within the critical-difference threshold in the daily-rank comparison. Although Chronos-2 achieves the lowest aggregate full-year error, TabPFN-TS shows better empirical calibration. Finally, the diagnostic findings motivate a Multi-Resolution Residual-Correction Forecaster that combines a low-frequency Base Forecaster with a short-horizon Residual Forecaster to improve longer-horizon planning accuracy.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Systematic Evaluation of TabPFN-TS for Zero-Shot Probabilistic Heat Load Forecasting in District Heating Networks". 
The paper presents novel ideas in ai-safety-eval that can be applied to agent systems.

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

- arXiv:2608.20024
