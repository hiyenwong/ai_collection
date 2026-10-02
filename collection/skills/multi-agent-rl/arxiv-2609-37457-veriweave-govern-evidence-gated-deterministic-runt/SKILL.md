---
name: arxiv-2609-37457-veriweave-govern-evidence-gated-deterministic-runt
description: 'VeriWeave Govern: Evidence-Gated Deterministic Runtime Governance for Enterprise AI Agents (arXiv: 2609.37457)'
metadata:
  {
    "arxiv_id": "2609.37457",
    "utility": 0.85,
    "title": "VeriWeave Govern: Evidence-Gated Deterministic Runtime Governance for Enterprise AI Agents",
    "authors": "Kabeh Mohsenzadegan, Vahid Tavakkoli, Kyandoghere Kyamakya",
    "url": "https://arxiv.org/abs/2609.37457"
  }
---

# VeriWeave Govern: Evidence-Gated Deterministic Runtime Governance for Enterprise AI Agents

**arXiv ID:** 2609.37457
**Authors:** Kabeh Mohsenzadegan, Vahid Tavakkoli, Kyandoghere Kyamakya
**URL:** https://arxiv.org/abs/2609.37457
**Utility Score:** 0.85

## Abstract

Enterprise artificial-intelligence agents increasingly call tools, modify infrastructure, and process protected data, creating a need to separate action generation from action authorization. This article presents VeriWeave Govern, a deterministic runtime governance layer that evaluates structured agent actions against versioned policies, validates typed evidence, applies fixed deny > review > allow precedence, routes consequential actions to accountable human review, and records replayable tamper-evident audit state. GovernBench evaluates the design over 30 independent seeds and 60,000 oracle-labelled cases spanning five enterprise domains, adversarial evidence, out-of-distribution actions, and temporal policy evolution. VeriWeave achieves 0.9888 mean accuracy, 0.9836 macro-F1, zero observed aggregate false allows, and zero observed Governance Attack Success Rate on the evaluated cases. Six ablations show that evidence gating, deny precedence, out-of-distribution fail-safe behavior, human review, contradiction handling, and temporal replay contribute complementary safety. The deployed API additionally passes 12/12 end-to-end scenarios and a 40,040-request concurrency matrix with zero failures. A separate 150-case EU/Austria regulation-grounded evaluation uses frozen predictions and two independent blinded human annotators, who agree on all decisions. On this set, deterministic engines remain conservative, while a Gemma 4 31B comparator aligns more closely with the human consensus. The results expose a measurable safety--utility trade-off and motivate evidence-aware, replayable governance as an independent control plane for enterprise agent execution.

## Usage

This skill references the paper's concepts and can be used in agent workflows for:
- Understanding the paper's methodology
- Referencing key findings
- Building on the research

## References

- arXiv: https://arxiv.org/abs/2609.37457
