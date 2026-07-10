---
name: online-safety-monitoring-llm
description: "Online safety monitoring methodology for LLMs at deployment time. Uses verifier signals from external models with calibrated thresholding via risk control to raise alarms when safety can no longer be assumed. Use when deploying LLMs and needing real-time safety monitoring, calibrating safety thresholds, or designing deployment-time guardrails. Simpler than sequential hypothesis testing approaches. Activation: LLM safety monitoring, deployment safety, real-time alarm, verifier thresholding, risk control, unsafe output detection, sequential hypothesis testing"
metadata:
  arxiv_id: "2607.02510"
  published: "2026-07-02"
  authors: "Mona Schirmer, Metod Jazbec, Alexander Timans, Christian Naesseth, Maja Waldron, Eric Nalisnick"
  category: "cs.AI, cs.CL, cs.LG, stat.AP, stat.ML"
  conference: "ICML 2026 Hypothesis Testing Workshop"
---

# Online Safety Monitoring for LLMs

## Core Problem

Despite alignment training, LLMs remain prone to generating unsafe outputs at deployment time. Monitoring outputs online and raising alarms when safety can no longer be assumed is critical.

## Methodology

### Simple Real-Time Monitor Design

1. **Verifier signal**: Use an external model to score outputs for safety
2. **Threshold calibration**: Calibrate the alarm threshold via risk control
3. **Alarm decision**: Threshold the verifier signal to raise an alarm when safety degrades

### Key Finding

This simple design (verifier + thresholding with risk-calibrated threshold) is competitive with more advanced monitors based on sequential hypothesis testing on mathematical reasoning and red teaming datasets.

### Deployment Workflow

1. Deploy an external verifier model alongside the LLM
2. Score each output in real-time
3. Use risk-controlled threshold to decide when to alarm
4. Simpler and more practical than sequential hypothesis testing approaches

### Activation Keywords

- `llm-safety-monitoring`, `deployment-safety`, `verifier-thresholding`, `risk-control`, `unsafe-output-detection`, `sequential-hypothesis-testing`, `real-time-alarm`, `safety-guardrails`