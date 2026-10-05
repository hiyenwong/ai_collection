---
name: arxiv-2610-01887v1-trace-tackling-real-world-resource-assignment-prob
description: "arXiv paper: TRACE: Tackling Real-World Resource Assignment Problems via Agentic Heuristic Design"
tags: [arxiv, cs.NE, research]
created: 2026-10-04
utility: 1.0
---

# TRACE: Tackling Real-World Resource Assignment Problems via Agentic Heuristic Design

**arXiv ID:** 2610.01887v1
**Authors:** Jose A. Ayala-Romero, Andres Garcia-Saavedra, Xavier Costa-Perez
**Published:** 2026-10-01
**Category:** cs.NE
**Utility Score:** 1.0
**URL:** https://arxiv.org/abs/2610.01887v1

## Abstract

Dynamic resource assignment, the real-time allocation of task streams to heterogeneous processing nodes, is the backbone of modern computing infrastructure. While learning-based schedulers excel in research, industrial deployments still rely on hand-written rules that operators can read, audit, and execute within tight latency budgets. LLM-based Automatic Heuristic Design (AHD) promises to automate writing such rules. However, existing AHD frameworks were developed for combinatorial problems fully specified to the LLM, and they learn only from a scalar fitness score. In real systems, the behaviour that determines a good heuristic, such as processor speeds or power consumption, is unknown a priori: the score reveals which heuristic performs better, but not why. This missing information is recorded in the system logs that every evaluation produces. Exploiting it is non-trivial: logs are massive and noisy, the relevant signals depend on the objective, and their content and format vary across hardware and software stacks, so they can neither be fed to an LLM as is nor processed by a fixed parser. We propose TRACE, which couples an evolutionary AHD loop with an agentic knowledge-extraction workflow. A Reasoner agent analyzes the log schema in light of the objective and formulates hypotheses about the system dynamics; a Coder agent writes and executes schema-specific code to test them, producing insights or executable tools for the evolved heuristics. We evaluate TRACE on a synthetic cloud benchmark and a 5G vRAN scenario built from industrial testbed measurements and operational traffic traces. TRACE consistently outperforms state-of-the-art AHD methods in resource assignment problems and yields more auditable heuristics at under 2% overhead.

## Key Contributions

- Novel research in cs.NE
- Published on arXiv: 2026-10-01

## Related Work

See arXiv for citations and references.
