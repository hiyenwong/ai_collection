---
name: lacuna-llm-unlearning-testbed
description: "LACUNA testbed methodology for evaluating LLM unlearning localization precision. Use when assessing whether unlearning truly erases knowledge from model parameters or merely obfuscates it, benchmarking unlearning methods, detecting resurfacing attacks, or implementing parameter-level knowledge removal in large language models. Activation: LLM unlearning, knowledge erasure, parameter localization, resurfacing attack, post-hoc removal, PII removal, gradient-based unlearning"
metadata:
  arxiv_id: "2607.02513"
  published: "2026-07-02"
  authors: "Matteo Boglioni, Thibault Rousset, Siva Reddy, Marius Mosbach, Verna Dankers"
  category: "cs.CL, cs.AI, cs.LG"
---

# LACUNA: LLM Unlearning Localization Testbed

## Core Problem

LLMs memorize sensitive training data (PII). Unlearning methods target specific model parameters but existing benchmarks only evaluate output-level performance, leaving open whether knowledge is truly erased or merely obfuscated (vulnerable to resurfacing attacks).

## LACUNA Methodology

### Ground-Truth Parameter Localization

1. **Inject** synthetic PII into predefined parameters of OLMo-based models (1B, 7B) via masked continual pretraining
2. **Evaluate** whether unlearning methods target the weights responsible for knowledge storage
3. **Benchmark** current SOTA unlearning methods against parameter-level ground truth

### Key Findings

- SOTA unlearning methods are highly imprecise at parameter level despite strong output-level performance
- Methods are susceptible to resurfacing attacks
- When localization is successful, even simple gradient-based unlearning achieves strong erasure and robustness to resurfacing

### Practical Workflow

1. **Identify** which model parameters store the target knowledge (localization phase)
2. **Apply** gradient-based unlearning to those specific parameters
3. **Verify** erasure at both output level AND parameter level
4. **Test** robustness against resurfacing attacks

### Activation Keywords

- `llm-unlearning`, `knowledge-erasure`, `parameter-localization`, `resurfacing-attack`, `pii-removal`, `gradient-unlearning`, `olmo`, `masked-continual-pretraining`