---
name: coflow-scheduling-ocs
description: Coflow Scheduling in Multi-Core Optical Circuit Switching Networks with Performance Guarantees
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: ['coflow', 'optical-circuit-switching', 'data-center', 'scheduling', 'distributed-systems', 'networking']
    source_paper: "Scheduling Coflows in Multi-Core OCS Networks with Performance Guarantee (arXiv:2604.08242v1)"
    citations: 0
    category: systems-engineering
---

# Coflow Scheduling in Multi-Core OCS Networks

## Overview
Coflow provides a key application-layer abstraction for capturing communication patterns in distributed systems. Modern data centers employ multiple independent optical circuit switching (OCS) cores operating concurrently to meet massive bandwidth demands. This paper addresses coflow scheduling in multi-core OCS fabrics, extending beyond single-core and electrical packet switching (EPS) approaches.

## Core Concepts
- **Coflow Abstraction**: Application-level communication pattern representation
- **Multi-Core OCS**: Multiple independent optical circuit switching cores
- **Performance Guarantees**: Bounded completion times for coflow scheduling
- **Circuit Switching**: Optical circuits for high-bandwidth, low-latency communication
- **Job Completion Time**: Optimizing end-to-end application performance

## Implementation Pattern
```python
# Coflow Scheduling for Multi-Core OCS Networks
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Flow:
    src: int
    dst: int
    size: int

@dataclass  
class Coflow:
    id: int
    flows: List[Flow]
    arrival_time: float

class MultiCoreOCSScheduler:
    def __init__(self, num_cores: int, core_capacity: float):
        self.num_cores = num_cores
        self.core_capacity = core_capacity
        self.circuit_duration = 10e-6
    
    def schedule_coflow(self, coflow: Coflow) -> Dict[int, List]:
        schedule = {i: [] for i in range(self.num_cores)}
        sorted_flows = sorted(coflow.flows, key=lambda f: f.size, reverse=True)
        
        for i, flow in enumerate(sorted_flows):
            core_id = i % self.num_cores
            duration = flow.size / (self.core_capacity / 8)
            start_time = self._find_earliest_slot(core_id, flow, duration)
            schedule[core_id].append((flow, start_time, duration))
        
        return schedule
```

## Key Insights
- Coflow abstraction captures application communication patterns
- Multi-core OCS requires new scheduling approaches beyond single-core
- Performance guarantees require careful circuit allocation
- Optical circuit setup time impacts scheduling decisions

## Applications
- Data center networks
- High-performance computing
- Distributed machine learning training
- Big data analytics platforms

## References
- Scheduling Coflows in Multi-Core OCS Networks with Performance Guarantee (arXiv:2604.08242v1)
- arXiv: https://arxiv.org/abs/2604.08242v1


## Description

This skill provides specialized capabilities for its domain.

## Activation Keywords

- keyword1
- keyword2
- keyword3

## Tools Used

- read: Read files
- write: Write files
- exec: Execute commands

## Instructions for Agents

When this skill is activated:

1. Identify the user's specific need
2. Apply the specialized knowledge
3. Provide clear guidance

## Examples

```
User: How do I use this skill?
Agent: I'll help you with this skill...
```