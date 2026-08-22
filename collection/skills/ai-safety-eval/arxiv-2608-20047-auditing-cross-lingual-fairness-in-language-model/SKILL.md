---
name: arxiv-2608-20047-auditing-cross-lingual-fairness-in-language-model
description: 'Auditing Cross-Lingual Fairness in Language Model Watermarking (arXiv: 2608.20047)'
category: ai-safety-eval
version: "1.0"
date: 2026-08-22
---

# Auditing Cross-Lingual Fairness in Language Model Watermarking

**Authors:** Alexander Nemecek, Osama Zafar, Debargha Ganguly, Vikash Singh, Vipin Chaudhary, Erman Ayday
**arXiv:** 2608.20047
**Utility:** 1.00
**Published:** 2026-08-20T13:48:12Z
**Link:** http://arxiv.org/abs/2608.20047

## Abstract

Watermarking schemes for large language model output are evaluated almost exclusively on English text using each scheme's detection threshold and a narrow set of quality measurements. Multilingual deployment exposes evaluation-design choices that are inconsequential on English but determine conclusions cross-lingually. We propose an evaluation framework with four components: detection thresholds calibrated empirically per deployment context, a threshold-independent companion measurement that distinguishes calibration failures from detection failures, three disjoint quality measurement paradigms (distributional, paired-semantic, and reference-perplexity), and a generalized-entropy decomposition of cross-language disparity over a typological family partition. Applied to six watermarking schemes, three open-weight generators, eleven languages spanning four scripts and eight typological families, and both base and instruction-tuned regimes, the framework reveals failure modes that single-language single-paradigm evaluation cannot surface. Across detection and quality, observed disparity is predominantly between-family on the typological partition, indicating that cross-lingual fairness gaps in watermarking are structural to language properties rather than idiosyncratic to particular languages.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Auditing Cross-Lingual Fairness in Language Model Watermarking". 
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

- arXiv:2608.20047
