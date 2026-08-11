---
name: qubo-alns-hurricane-restoration
description: "Quantum Inspired QUBO Assisted ALNS framework for reliability-driven hurricane restoration of distribution networks. Combines quantum-inspired quadratic unconstrained binary optimization with adaptive large neighborhood search for power grid repair scheduling. Use when optimizing post-disaster power system restoration with crew logistics, feeder topology, and electrical feasibility constraints."
metadata:
  arxiv_id: "2607.29544"
  published: "2026-07-31"
  authors: "Hooman Torkaman, Jignesh Solanki, Anurag Srivastava"
  subjects: "Systems and Control (eess.SY)"
  conference: "24th National Power System Conference (NPSC 2026), Track T8: Grid Flexibility and Resiliency"
license: Complete terms in LICENSE.txt
---

# Quantum Inspired QUBO Assisted ALNS for Hurricane Restoration

## Overview

This methodology presents a quantum-inspired quadratic unconstrained binary optimization (QUBO) assisted adaptive large neighborhood search (ALNS) framework for post-hurricane distribution system restoration. The approach addresses rapid repair scheduling subject to feeder topology, field logistics, and electrical feasibility constraints.

## Core Components

### 1. QUBO-Assisted Local Search
- At each restoration stage, uses a local CPU simulated annealing sampler to rank individual repairs and multi-job combinations near the energized frontier
- Leverages quantum-inspired QUBO formulation to evaluate combinatorial repair options efficiently
- Focuses on areas near the energized frontier where decisions have the highest impact

### 2. Deterministic Decoder
- Preserves crew truck logistics constraints
- Enforces full useful crew utilization 
- Rejects infeasible repair batches that violate operational constraints
- Maintains electrical feasibility throughout the restoration process

### 3. Validation Framework
- Final schedules are validated through OpenDSS replay simulation
- Uses IEEE test feeders for standardized evaluation
- Evaluates under multiple wind scenario stress tests (80, 90, 100 m/s)

## Performance Metrics

The framework demonstrates significant improvements over classical energized ALNS:
- **2.24% reduction** in mean system average interruption duration index (SAIDI)
- **2.24% reduction** in energy not supplied (ENS)
- **50.71% reduction** in restoration makespan (in 100 m/s stress test)

## Implementation Guidelines

### When to Apply
- Post-hurricane or post-disaster power system restoration scenarios
- Distribution networks with distributed generation considerations
- Scenarios with severe damage creating large combinatorial repair spaces
- Systems requiring crew logistics coordination with electrical constraints

### Key Parameters
- Wind scenario severity (affects damage extent and combinatorial complexity)
- Number of available repair crews and their capabilities
- Feeder topology and switching constraints
- Distributed generation availability and constraints

### Validation Requirements
- OpenDSS simulation environment for electrical validation
- IEEE standard test feeders (e.g., IEEE 123 node test feeder)
- Multiple stress test scenarios to evaluate robustness

## Pitfalls and Considerations

### Computational Complexity
- QUBO assistance provides most value when severe damage creates larger combinatorial repair spaces
- For minor damage scenarios, classical ALNS may be sufficient
- Balance between solution quality and computational time based on urgency

### Integration Challenges
- Requires integration between optimization framework and power system simulation tools
- Crew logistics modeling must accurately reflect real-world constraints
- Electrical feasibility validation is critical for practical deployment

### Scalability
- Framework tested on IEEE 123 node system
- Larger systems may require additional decomposition strategies
- Consider parallel processing for real-time applications

## References

- Original paper: arXiv:2607.29544 [eess.SY]
- IEEE 123 Node Test Feeder documentation
- OpenDSS simulation platform documentation
- Adaptive Large Neighborhood Search (ALNS) literature
- Quantum-inspired optimization and QUBO formulations

## Activation Keywords

- hurricane restoration
- power grid repair
- distribution system restoration  
- QUBO optimization
- ALNS framework
- quantum-inspired optimization
- crew scheduling
- electrical feasibility
- OpenDSS validation
- SAIDI reduction