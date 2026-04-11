---
name: coflow-scheduling-ocs
description: "Coflow scheduling in multi-core optical circuit switching (OCS) networks with performance guarantees. Optimizes parallel data flow coordination to reduce job completion times in distributed data center networks. Activation: coflow scheduling, OCS network optimization, data center networking."
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [coflow-scheduling, optical-circuit-switching, data-center-networks, distributed-systems]
    source_paper: "Scheduling Coflows in Multi-Core OCS Networks with Performance Guarantee (arXiv:2604.08242)"
    citations: 0
    category: systems-engineering
---

# Coflow Scheduling in Multi-Core OCS Networks

## Overview

Coflow provides a key application-layer abstraction for capturing communication patterns, enabling efficient coordination of parallel data flows to reduce job completion times in distributed systems. Modern data center networks employ multiple independent optical circuit switching (OCS) cores to scale network capacity.

## Core Concepts

### Coflow Abstraction
- **Definition**: A collection of flows that share a common performance goal
- **Characteristics**: All flows must complete for the coflow to complete
- **Optimization Objective**: Minimize coflow completion time (CCT)

### Optical Circuit Switching (OCS)
- **Technology**: Circuit-switched optical connections with high bandwidth
- **Reconfiguration**: Non-negligible reconfiguration delay
- **Multi-Core**: Multiple independent OCS switches for scalability

## Implementation

```python
from typing import List, Dict, Tuple
from dataclasses import dataclass
from enum import Enum

class FlowStatus(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"

@dataclass
class Flow:
    flow_id: str
    source: str
    destination: str
    volume: int
    status: FlowStatus = FlowStatus.PENDING

@dataclass
class Coflow:
    coflow_id: str
    flows: List[Flow]
    arrival_time: float
    
    @property
    def total_volume(self) -> int:
        return sum(f.volume for f in self.flows)
    
    @property
    def width(self) -> int:
        return len(self.flows)

class MultiCoreOCSScheduler:
    def __init__(self, num_cores: int, reconfig_delay: float, port_capacity: float):
        self.num_cores = num_cores
        self.reconfig_delay = reconfig_delay
        self.port_capacity = port_capacity
        self.pending_coflows: List[Coflow] = []
        self.completed_coflows: List[Coflow] = []
        
    def calculate_sebf_priority(self, coflow: Coflow) -> float:
        src_volumes = {}
        dst_volumes = {}
        for flow in coflow.flows:
            src_volumes[flow.source] = src_volumes.get(flow.source, 0) + flow.volume
            dst_volumes[flow.destination] = dst_volumes.get(flow.destination, 0) + flow.volume
        max_src = max(src_volumes.values()) if src_volumes else 0
        max_dst = max(dst_volumes.values()) if dst_volumes else 0
        bottleneck_time = max(max_src, max_dst) / (self.port_capacity * 1e9 / 8)
        return bottleneck_time
    
    def schedule(self, current_time: float):
        self.pending_coflows.sort(key=lambda c: self.calculate_sebf_priority(c))
        # Schedule logic here
```

## Key Insights

1. **Coflow Abstraction**: Treating related flows as a single unit enables better scheduling
2. **Multi-Core Coordination**: Distributing coflows across OCS cores requires careful coordination
3. **Performance Guarantees**: SEBF provides bounded competitive ratios

## References

- Wang, X., Shen, H., Tian, H., & Wang, D. (2026). Scheduling Coflows in Multi-Core OCS Networks. arXiv:2604.08242.
