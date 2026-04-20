---
name: dual-timescale-neuron-astrocyte-memory
description: "Biological agents navigate complex environments by combining long-term memory of successful actions with short-term suppression of recently visited locations-a capability that remains difficult to rep"
---

# Dual-Timescale Memory in Spiking Neuron-Astrocyte Network

## Source
- **arXiv**: 2604.15391

## Abstract
Biological agents navigate complex environments by combining long-term memory of successful actions with short-term suppression of recently visited locations-a capability that remains difficult to replicate in artificial systems, especially under partial observability. Inspired by the complementary timescales of neural and astrocytic dynamics, we introduce a spiking neuron-astrocyte network (SNAN) where spike-timing-dependent plasticity (STDP) reinforces successful action sequences on a distant time scale, while astrocytic calcium transients suppress recently visited states on a short-term time scale, effectively blocking locations already explored. This dual-timescale memory mechanism biases the agent toward unexplored regions, accelerating goal finding without requiring explicit global statistics. We show that in grid-world navigation tasks with extreme partial observability, SNAN reduces median path length by up to sixfold and drastically improves goal completion rates compared to baseline agents. The astrocytic modulation inherently mitigates the exploration-exploitation trade-off as an emergent consequence of local state suppression. This kind of local sensory data modulation can be considered as a new type of working memory referred to as a &#34;Topological-Context Memory&#34;. To validate hardware feasibility using neuromorphic approaches, we map STDP to a memristive VTEAM model and implement a subset of the network on a crossbar array, achieving order-of-magnitude gains in speed per area and energy per decision over CPU implementations. Our results establish astrocyte-inspired dual-timescale memory as a scalable, hardware-realizable principle for neuromorphic robotics and edge-AI systems.
