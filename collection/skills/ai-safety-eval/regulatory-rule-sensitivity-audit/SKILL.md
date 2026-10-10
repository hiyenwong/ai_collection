---
name: regulatory-rule-sensitivity-audit
description: Use when auditing LLM compliance systems by perturbing governing rules (delete, swap, negate). Tests whether verdicts depend on the actual rule.
tags: [compliance, rule-sensitivity, audit, regulation, faithfulness, governance]
---

# Regulatory Rule Sensitivity Audit

## Paper Metadata

- **arXiv ID**: 2610.12313
- **Authors**: arXiv authors
- **Categories**: cs.CL, cs.AI
- **Utility Score**: 0.87
- **Date**: 2026-10
- **Link**: https://arxiv.org/abs/2610.12313

## Key Contributions

- Audits LLM compliance by deleting, swapping, or negating governing rules
- Tests whether model verdicts actually depend on the specific rule text
- Covers five models across 20 regulatory domains
- Reveals that many compliance systems are insensitive to rule content

## Core Methodology

The audit tests LLM compliance systems by systematically perturbing the regulatory rules they're supposed to enforce. Three perturbation types: (1) delete the rule entirely, (2) swap it with an unrelated rule, (3) negate the rule's meaning. If the system is genuinely rule-following, these perturbations should change its verdicts; if verdicts remain unchanged, the system is not actually consulting the rules.

The study covers five major LLMs across 20 regulatory domains (financial compliance, data privacy, healthcare regulation, etc.), providing broad coverage of the compliance AI landscape. Each domain has specific rules that the model must apply to scenarios, and the audit measures how often the model's output changes when the underlying rule changes.

The results reveal a significant gap between apparent and actual rule-following: many models produce similar verdicts regardless of which rule they're given, suggesting they rely on surface-level patterns or prior knowledge rather than genuinely applying the specified regulation. This has direct implications for deploying LLMs in regulated industries.

## Relevance to ai-safety-eval

Essential safety evaluation for compliance AI: demonstrates that rule-following claims must be verified through perturbation testing, not just surface-level accuracy on held-out examples.

## Activation

compliance, rule-sensitivity, audit, regulation, faithfulness, governance
