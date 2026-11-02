---
name: rama-retrieval-augmented-multi-agent-routing-with-episodic
description: "RAMA: Retrieval-Augmented Multi-Agent Routing with..."
tags: [cs.NI, cs.LG]
source: arxiv
arxiv_id: 2610.42068v1
utility: 0.85
published: 2026-10-30
---

# RAMA: Retrieval-Augmented Multi-Agent Routing with Episodic Memory for LEO Satellite Networks

**Authors:** Xin Ming Li, Peng Hu
**Published:** 2026-10-30
**arXiv:** [2610.42068v1](https://arxiv.org/abs/2610.42068v1)
**Categories:** cs.NI, cs.LG
**Utility Score:** 0.85

## Abstract

Low-Earth orbit (LEO) satellite networks present a challenging routing environment due to rapidly changing topology, traffic, and link conditions. Existing deep reinforcement learning (DRL) routing methods typically rely on current observations and information encoded in network weights, limiting their ability to exploit successful past experiences. We propose RAMA, a retrieval-augmented multi-agent DRL framework with Approximate Information State (AIS), in which each satellite combines its local observation, recent routing history, neighboring state information, and retrieved entries from a per-satellite episodic memory. Retrieved experiences are integrated through a Transformer-based decision network trained with AIS-based auxiliary objectives. With weights frozen in a 140-satellite Kepler constellation, RAMA reduces mean end-to-end latency by 13.4% and 99th-percentile latency by 66.7% relative to the state-of-theart double deep Q-network (DDQN) routing method, mainly by avoiding long detours. Updated online, RAMA remains stable while DDQN degrades. On the 1,584-satellite Starlink shell 1, the reduction in mean latency grows to 93.2%, and updating RAMA online lowers its mean latency by a further 25.5%. These results demonstrate the effectiveness of retrieval-augmented memory for scalable decentralized routing in LEO satellite networks.

## Key Contributions

- Novel research in cs.NI, cs.LG
- Published 2026-10-30

## Activation

rama, retrievalaugmented, multiagent, routing, episodic, memory, satellite, networks
