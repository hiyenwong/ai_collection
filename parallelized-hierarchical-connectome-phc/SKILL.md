---
name: parallelized-hierarchical-connectome-phc
description: "Parallelized Hierarchical Connectome (PHC) framework upgrading temporal-only State-Space Models (SSMs) into spatiotemporal recurrent networks. Maps diagonal SSM core to shared Neuron Layer with hierarchical regions governed by connectome topology. Activation: PHC framework, spatiotemporal SSM, spiking state-space model, hierarchical connectome."
---

# Parallelized Hierarchical Connectome: A Spatiotemporal Recurrent Framework for Spiking State-Space Models

## Paper Information
- **Title:** Parallelized Hierarchical Connectome: A Spatiotemporal Recurrent Framework for Spiking State-Space Models
- **Authors:** Po-Han Chiang
- **arXiv ID:** 2604.01295v1
- **Published:** April 1, 2026
- **Categories:** q-bio.NC
- **PDF:** https://arxiv.org/pdf/2604.01295v1

## Abstract

This work presents the Parallelized Hierarchical Connectome (PHC), a general framework that upgrades temporal-only State-Space Models (SSMs) into spatiotemporal recurrent networks. Conventional SSMs achieve high-speed sequence processing through parallel scans, yet are limited to temporal recurrence without lateral or feedback interactions within a single timestep. PHC maps the diagonal SSM core to a shared Neuron Layer and inter-neuronal communication to a shared Synapse Layer, where neurons are partitioned into hierarchical regions governed by the connectome topology.

## Core Contributions

1. **PHC Framework:** Spatiotemporal upgrade for temporal-only SSMs
2. **Connectome-Governed Architecture:** Neurons partitioned by brain connectivity topology
3. **Multi-Transmission Loop:** Intra-slice spatial recurrence mechanism
4. **Spiking SSM Integration:** Combines efficient SSMs with biological spiking dynamics

## Methodology

### Architecture Components
- **Neuron Layer:** Shared layer mapping diagonal SSM core
- **Synapse Layer:** Shared layer for inter-neuronal communication
- **Hierarchical Regions:** Neurons partitioned by connectome topology
- **Multi-Transmission Loop:** Enables intra-slice spatial recurrence

### Key Innovations
1. **From Temporal to Spatiotemporal:** Extends SSMs with spatial interactions
2. **Connectome Topology:** Brain-inspired hierarchical organization
3. **Parallel Efficiency:** Maintains O(log T) parallelism of SSMs
4. **Biological Plausibility:** Spiking dynamics with connectome constraints

### Implementation
- State-space model core (diagonal structured matrix)
- Spatial connectivity via connectome topology
- Hierarchical partitioning of neuron populations
- Multi-step transmission for spatial recurrence

## Applications

- Brain-inspired sequence modeling
- Neural population dynamics simulation
- Connectome-constrained neural networks
- Spatiotemporal pattern processing
- Large-scale brain network modeling

## Activation Keywords

- PHC framework
- spatiotemporal SSM
- spiking state-space model
- hierarchical connectome
- multi-transmission loop
- connectome topology

## References

- Paper: https://arxiv.org/abs/2604.01295v1
- arXiv: 2604.01295v1 (April 2026)
