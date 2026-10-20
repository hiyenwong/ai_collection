---
name: agentic-orchestration-of-edc-data-space
description: "Agentic Orchestration of EDC Data Space Retrieval ..."
tags: [cs.AI]
source: arxiv
arxiv_id: 2610.26548v1
utility: 1.0
published: 2026-10-19
---

# Agentic Orchestration of EDC Data Space Retrieval and Natural Language Driven Data Processing

**Authors:** Marla Grunewald, Fin Gentzen, Iulisloi Zacarias, Admela Jukan
**Published:** 2026-10-19
**arXiv:** [2610.26548v1](https://arxiv.org/abs/2610.26548v1)
**Categories:** cs.AI
**Utility Score:** 1.0

## Abstract

Participating in a data space still requires the Dataspace Protocol (DSP) negotiation flow to be hand-coded against each provider's access policy. We present a multi-agent architecture that automates this process using natural language requests. Built on LangGraph over an Eclipse Dataspace Components (EDC), the design separates concerns into cooperating agents. The orchestrator's role is to route and plan. The data extraction agent's role is to expose the DSP protocol's three composable tools (catalog discovery, contract negotiation and download). The agent also gates negotiations on the consumers' verifiable credentials, refusing assets rather than fabricating them. Furthermore, there are downstream Machine Learning (ML) and Visualization agents, as well as a final Verification agent, which confirms that the request was actually fulfilled and rechecks the intended operation against the contract's usage policy. In a primary benchmark involving 600 runs, the system achieved 89% task success with zero policy violations when evaluating multi-dimensional policy reasoning with a locally hosted open-weight model. It failed safely through refusal rather than misrouting. The reliability of the system is largely dependent on the phrasing of requests: technical and expert requests succeed up to 98% of the time, whereas casual and under-specified requests succeed 72% of the time. Furthermore, in a secondary evaluation of 600 runs isolating hierarchical geographic access control, the fra

## Key Contributions

- Novel research in cs.AI
- Published 2026-10-19

## Activation

agentic, orchestration, data, space, retrieval, natural, language, driven, data, processing
