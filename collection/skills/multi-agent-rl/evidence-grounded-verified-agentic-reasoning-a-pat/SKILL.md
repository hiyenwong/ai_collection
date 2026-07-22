---
name: evidence-grounded-verified-agentic-reasoning-a-pat
description: "Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM Hallucination in Empirical Inference via Tool-Attested Kernel Proofs - Tool access alone does not make LLM empirical reasoning governable: accepted outputs need not descend from attested evidence, and accepted deductions ..."
version: 1.0.0
author: Junyu Ren
arxiv_id: 2607.12650
created: 2026-07-14
category: multi-agent-rl
tags: [cs.LG, cs.AI, cs.CY, cs.SE]
activation_keywords: [evidence, grounded, verified, agentic, reasoning, path, toward, eliminating, hallucination, empirical]
---

# Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM Hallucination in Empirical Inference via Tool-Attested Kernel Proofs

## Overview

Tool access alone does not make LLM empirical reasoning governable: accepted outputs need not descend from attested evidence, and accepted deductions need not hold up under formal scrutiny. We present EG-VAR (Evidence-Grounded Verified Agentic Reasoning), a Lean 4-based tool-calling architecture in which the Lean kernel is the sole minter of Verified claims via tool-attestation axioms and declared source lifts. Every verified output structurally descends from an attested tool call (Thm. 3.1) and a kernel-checked chain of valid inference (Thm. 3.2); residual outputs are honest Abstain with a replayable audit trail. On a subcollection of TableBench numerical reasoning (n=120), EG-VAR attains 120/120 versus a 95% same-tool baseline; on counterfactual stress tests (5 domains x 2 models), EG-VAR stays 100% source-faithful while same-tool drops to 80-90% (no-tool 50-80%). With the LLM as deployment-time formalizer, residual semantic-formalization error is 3.3% on Sonnet and 1.7% on Opus. We position EG-VAR as a technical-governance interface for high-stakes empirical claims: a formal sidecar makes the target proposition, source scope, evidence boundary, proof obligation, and abstention condition auditable, eliminating unsupported Verified outputs today while turning formalization errors, lift and source-authority disputes, ambiguities, and abstentions into explicit audit targets. Over time, typed sidecars in datasets, APIs, public records, and AI-generated documents can amortize this formalization burden into reusable infrastructure.

## Key Insights

- TODO: Extract key insights from the paper

## Implementation Approach

- TODO: Describe how to implement the techniques from this paper

## Applications

- TODO: List potential applications

## Activation Keywords

evidence, grounded, verified, agentic, reasoning, path, toward, eliminating, hallucination, empirical

---
