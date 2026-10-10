---
name: legal-cot-faithfulness-audit
description: Use when auditing whether LLM chain-of-thought reasoning is faithful or merely post-hoc rationalization. Counterfactual substitution of cited authorities.
tags: [faithfulness, chain-of-thought, legal-reasoning, counterfactual-audit, attribution, hallucination]
---

# Legal CoT Faithfulness Audit

## Paper Metadata

- **arXiv ID**: 2610.12361
- **Authors**: arXiv authors
- **Categories**: cs.CL, cs.AI
- **Utility Score**: 0.86
- **Date**: 2026-10
- **Link**: https://arxiv.org/abs/2610.12361

## Key Contributions

- Introduces counterfactual audit: substitute named legal authority with unrelated one and check if verdict changes
- Decodes verdict from hidden states (probing) to separate what the model 'actually believes' from what it cites
- Shows models cite but don't consult authorities — chain-of-thought references are post-hoc rationalizations
- Provides a methodology for testing reasoning faithfulness across any domain with named references

## Core Methodology

The audit works by counterfactual substitution: take a legal reasoning trace that cites a specific authority (e.g., a case or statute), replace that authority with an unrelated one, and observe whether the model's verdict changes. If the reasoning were faithful, changing the cited authority should change the outcome; if it doesn't, the citation was decorative.

To separate the model's 'true' prediction from its stated reasoning, the method probes hidden states to decode the verdict before the chain-of-thought is generated. This reveals whether the model had already 'decided' before producing the reasoning trace, making the CoT a post-hoc rationalization rather than a genuine reasoning process.

The combination of counterfactual substitution + hidden-state probing provides a two-pronged test of faithfulness: (1) does the output depend on the cited references? (2) does the internal state already encode the answer before reasoning begins? Both tests together reveal the gap between apparent and actual reasoning.

## Relevance to ai-safety-eval

Critical for AI safety in high-stakes domains (legal, medical, financial) where reasoning transparency is required. Shows that CoT may not be trustworthy even when it looks rigorous.

## Activation

faithfulness, chain-of-thought, legal-reasoning, counterfactual-audit, attribution, hallucination
