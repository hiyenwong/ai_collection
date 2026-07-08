---
name: ai-adapter-security-analysis
description: "Methodology for analyzing security risks in fine-tuned LLM adapters (LoRA) and evaluating LLM-based penetration testing reliability. Covers: LoRA backdoor detection via behavioral probes and weight-level statistics, multi-model attack consistency measurement, and supply chain security for adapter distribution. Use when analyzing adapter security, LLM pentesting reliability, fine-tuned model trustworthiness, or AI attack evaluation."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.30189,2605.30096"
  published: "2026-05-28"
  authors: "Travis Lelle; Galip Tolga Erdem"
  tags: [ai-security, lora, backdoor, penetration-testing, adapter-safety, behavioral-detection]
---

# AI Adapter Security Analysis

## Overview

Security methodology for two critical LLM trust domains: (1) detecting backdoors in LoRA adapters distributed by third parties, and (2) measuring the reliability of LLMs as autonomous penetration testing agents. Both address the growing attack surface as LLM fine-tunes become commoditized and AI security agents proliferate.

## Core Components

### 1. LoRA Adapter Backdoor Detection (arXiv:2605.30189)

LoRA adapters can be reliably backdoored via training data poisoning while preserving baseline task performance. The attack generalizes at the **token feature level** rather than structural pattern level, making generic defense impossible.

#### Detection Routes

**Behavioral Detection** (operationally portable):
- Use probe batteries that overlap with trigger's token neighborhood
- Two key statistics: `outlier_gap` and `mean_attack_rate`
- Separates poisoned from clean adapters perfectly when probes overlap trigger
- High recall with zero false positives even when probes don't overlap

**Weight-Level Detection** (base-model dependent):
- Cross-module standard deviation of dimension-normalized Frobenius norms
- Separates cohort perfectly without running the model
- Calibration-bound to the base model

**Causal Patching** (for analysis):
- Backdoor localizes to MLP blocks at mid-to-late layers
- `down_proj` is the strongest single-projection cause
- Useful for understanding attack mechanism, not for production scanning

#### Key Findings
- Attack scales monotonically with LoRA rank
- Trigger-anchor token is both trigger-dependent and base-model-dependent
- Behavioral detection transfers across scale, family, and rank without retuning
- Small fraction of poisoned examples drives backdoor to saturation

### 2. LLM Penetration Testing Reliability (arXiv:2605.30096)

First large-scale empirical measurement (N=100 per model) of LLM attack consistency against identical multi-service targets.

#### Methodology
- 400 autonomous pentesting runs (4 models × 100 each)
- Identical honeypot with OWASP Juice Shop + 2 vulnerable services
- Constant prompt, orchestrator, and target across all runs

#### Key Findings
- Full exploitation rates: Gemini 2.5 Flash-Lite (85%), Claude Sonnet 4 (61%), GPT-4o-mini (56%), qwen2.5-coder:14b (25%)
- First-exploit timing: 15-30 second wall-clock range
- GPT-4o-mini deployed 98 unique attack strategies
- Cross-model differences statistically significant (p < 0.001, Cohen's h = 1.12)
- Cross-service credential reuse: qwen (57%), GPT-4o-mini (49%), cloud models (0% with 5-exchange windows)

#### Failure Modes (Model-Distinctive)
- Claude: API truncation from upstream 529 errors (39 runs)
- Qwen: Premature completion (52 runs)
- GPT-4o-mini: Iteration-budget exhaustion (23 runs)

## Methodology

### Evaluating Adapter Trustworthiness

1. **Behavioral probe battery**: Design probes covering diverse token neighborhoods
2. **Run outlier_gap analysis**: Measure statistical deviation from clean cohort
3. **Compute mean_attack_rate**: Average success rate across triggered behaviors
4. **Weight-level analysis**: Calculate cross-module Frobenius norm statistics
5. **Combine routes**: Behavioral + weight-level provides robustness to probe composition

### Measuring LLM Attack Consistency

1. **Fix all variables**: Same prompt, orchestrator, target, iteration budget
2. **Run ≥100 trials per model**: Statistical significance requires large N
3. **Track failure modes**: Categorize by type (truncation, completion, budget)
4. **Measure cross-service behavior**: Credential reuse, strategy diversity
5. **Report timing distributions**: First-exploit latency, not just success rate

## Pitfalls

- **Behavioral detectors require probe overlap**: Zero overlap = degraded recall
- **Weight detectors are calibration-bound**: Different base models need recalibration
- **Token-level ≠ structural generalization**: Backdoors activate on any RFC reference but NOT on structurally identical ISO/OWASP/NIST citations
- **N=100 minimum for reliability**: Small-N studies miss rare failure modes
- **API errors ≠ safety refusals**: HTTP 529 overloaded errors are infrastructure failures, not model-level refusals

## Related Skills

- `security-guardrails`: Mandatory security guardrails for Hermes Agent
- `systems-engineering-threat-modeling`: Automated threat modeling for CPS

---

*Reference: Lelle (2026) "Token-Level Generalization in LoRA Adapter Backdoors" arXiv:2605.30189; Erdem (2026) "How Reliable Are AI Attackers" arXiv:2605.30096*
