---
name: auditing-llm-as-judge-reliability-measurement-validity
description: "Treats LLM-as-judge evaluator-replacement ambiguity as a measurement-validity problem. Judge upgrades are not interchangeable. Stronger judges reduce but don't remove position/verbosity bias. Proposes audit trails including dataset slices, bias probes, and error-dependence estimates. Activation: LLM-as-judge, evaluation reliability, measurement validity, evaluator bias, AI evaluation."
metadata:
  arxiv_id: "2607.08535"
  published: "2026-07-09"
  authors: "Zongyou Yang, Yinghan Hou, Xiaokun Yang"
  tags: [llm-as-judge, evaluation-reliability, measurement-validity, evaluator-bias, ai-evaluation]
---

# When the Judge Changes, So Does the Measurement: Auditing LLM-as-Judge Reliability

## Overview

An LLM-as-judge score can move even when candidate responses stay fixed, simply because the evaluator has changed. This paper treats evaluator-replacement ambiguity as a measurement-validity problem, systematically comparing two upgrade paths: scaling Qwen3 dense judges (1.7B to 32B) and moving across MiniMax M2-M2.7 APIs.

## Key Innovations

### Measurement-Validity Framework
- Frames evaluator changes as measurement validity problems
- Shows that judge upgrades are not interchangeable
- Only Qwen3 1.7B→4B gives robust adjacent gain; MiniMax adjacent releases do not

### Bias Persistence Analysis
- Stronger judges reduce but do not remove position and verbosity bias
- Repeated-sample juries add little when errors are correlated
- Structured debate can shift decisions but attribution requires protocol logs

### Audit Trail Requirements
- Proposes LLM-as-judge reports include: dataset slices, bias probes, error-dependence estimates, and protocol audit trails
- Enables reproducible and verifiable evaluation

## Methodology

1. **Upgrade Paths**: Compare Qwen3 scaling (1.7B→32B) and MiniMax API changes
2. **Bias Probes**: Measure position and verbosity bias across judges
3. **Jury Analysis**: Evaluate repeated-sample juries under correlated errors
4. **Structured Debate**: Analyze decision shifts and attribution requirements

## Implications

- LLM-as-judge is not a stable measurement instrument across evaluator versions
- Evaluation reports must include bias and reliability metadata
- Structured debate helps but requires careful logging
- Judge selection impacts research conclusions

## Pitfalls

- Findings are specific to Qwen3 and MiniMax — other models may differ
- Bias probes may not capture all forms of evaluator bias
- Correlated errors make juries less effective than expected
- Protocol audit trails add complexity to evaluation pipelines

## Activation Keywords

LLM-as-judge, evaluation reliability, measurement validity, evaluator replacement, position bias, verbosity bias, juries, structured debate, audit trail

## Paper Reference

arXiv:2607.08535 - "When the Judge Changes, So Does the Measurement: Auditing LLM-as-Judge Reliability" (Jul 2026)
