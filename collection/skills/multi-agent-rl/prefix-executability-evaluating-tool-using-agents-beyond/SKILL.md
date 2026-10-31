---
name: prefix-executability-evaluating-tool-using-agents-beyond
description: "Prefix Executability: Evaluating Tool-Using Agents..."
tags: [cs.AI, cs.CL]
source: arxiv
arxiv_id: 2610.40444v1
utility: 0.85
published: 2026-10-29
---

# Prefix Executability: Evaluating Tool-Using Agents Beyond Final Success

**Authors:** Amir H. Rezaeian, Weiyi Sun, Yassine Benajiba, Dan Roth
**Published:** 2026-10-29
**arXiv:** [2610.40444v1](https://arxiv.org/abs/2610.40444v1)
**Categories:** cs.AI, cs.CL
**Utility Score:** 0.85

## Abstract

Tool-use benchmarks often score agents by final task success, but terminal outcomes can obscure whether the intermediate tool-call trajectory was executable. We propose prefix executability as a trajectory-level evaluation protocol for tool-using agents. The protocol measures whether every prefix of a predicted tool-call sequence remains executable under tool schemas, state preconditions, and data dependencies, and summarizes reliability using Prefix Executability Curves (PEC), First-Error Depth (FED), Trajectory Executability Rate (TER), horizon-normalized AUC-PEC, and Recovery Rate (RR). We instantiate the protocol on stratified samples from BFCL-v3 multi-turn and ToolSandbox, and on the complete Airline/Retail base splits of $τ^3$-bench. We observe that outcome-only and prefix-level rankings diverge: agents whose execution is conditioned on an unverified plan often achieve higher point-estimate final success than non-plan-conditioned baselines while substantially lowering TER and AUC-PEC. These divergences are precisely the failure modes that prefix executability is designed to expose: they reveal whether apparent success rests on an executable trajectory, where invalidity first enters, and whether success follows recovery from an earlier failure. As a validation intervention, explicit pre-execution plan checking can improve executable-prefix survival while maintaining competitive terminal success. These results show that final success alone is insufficient for evaluating 

## Key Contributions

- Novel research in cs.AI, cs.CL
- Published 2026-10-29

## Activation

prefix, executability, evaluating, toolusing, agents, beyond, final, success
