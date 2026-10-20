---
name: bidirectionality-is-necessary-in-cellular-machines
description: "Bidirectionality is Necessary in Cellular Machines..."
tags: [cs.ET, cs.CC, cs.DC]
source: arxiv
arxiv_id: 2610.26272v1
utility: 1.0
published: 2026-10-19
---

# Bidirectionality is Necessary in Cellular Machines for Exact-Arrival Multi-Agent Path Finding

**Authors:** Masashi Aono
**Published:** 2026-10-19
**arXiv:** [2610.26272v1](https://arxiv.org/abs/2610.26272v1)
**Categories:** cs.ET, cs.CC, cs.DC, cs.MA
**Utility Score:** 1.0

## Abstract

On ranked directed acyclic graphs coupled by vertex conflicts we study exact-arrival multi-agent path finding (departure and arrival pinned in place and time) posed as a distributed output task: every cell must emit its own bit of a valid joint path-support mask. The machines are cellular: one automaton per cell, state factored over cells, communication only along a fixed local fabric, synchronous rounds, a query-independent output round, no central decoder, and a per-topology transition code. "Necessary" here means: on an explicit hard topology, over all its feasible queries, no universally correct local-only architecture can renounce either temporal orientation; with global flags, impossibility becomes a bandwidth-round trade-off. The class is not vacuous: a flooding machine solves every instance in as many rounds as the diameter of the local fabric. The bound survives two concessions: we supply every agent's exact individual cavity, which alone solves the single-agent problem in zero rounds and makes the single-agent direction theorem vacuous; and we allow $k$ one-bit global aggregate flags. On a twelve-cell, two-agent, depth-three topology no forward-only machine with $k=0$ is correct on two feasible queries, for any number of rounds; the time-reversed topology does the same to backward-only machines. Placing $p$ copies side by side gives, for forward-only machines, $J_R+kR\ge p$ at constant depth, where $J_R$ measures how much of the query reaches the targets' cones and 

## Key Contributions

- Novel research in cs.ET, cs.CC
- Published 2026-10-19

## Activation

bidirectionality, necessary, cellular, machines, exactarrival, multiagent, path, finding
