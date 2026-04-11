---
name: coflow-scheduling-ocs-networks
description: Scheduling Coflows in Multi-Core Optical Circuit Switching Networks with Performance Guarantee. Optimize parallel data flow coordination in distributed systems using optical circuit switching.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [coflow, scheduling, optical-circuit-switching, data-center, distributed-systems]
    source_paper: "Scheduling Coflows in Multi-Core OCS Networks with Performance Guarantee (arXiv:2604.08242)"
    citations: 0
    category: distributed computing
---

# Coflow Scheduling in Multi-Core OCS Networks

## Overview

This skill provides methodologies for scheduling coflows in multi-core optical circuit switching (OCS) networks with performance guarantees. Coflows capture application-layer communication patterns, enabling efficient coordination of parallel data flows to reduce job completion times.

## Core Concepts

### Coflow Abstraction
- **Definition**: A collection of flows that share a common performance goal
- **Characteristics**: All-or-nothing semantics, collective completion time
- **Importance**: Critical for data-intensive applications (MapReduce, Spark, ML training)

### Multi-Core OCS Networks
- **Architecture**: Multiple independent OCS cores operating concurrently
- **Advantages**: Massive bandwidth, low latency, energy efficiency
- **Challenge**: Coordinating coflows across multiple switching cores

## Implementation Pattern

```python
from typing import List, Dict, Tuple
from dataclasses import dataclass
import heapq

@dataclass
class Flow:
    src: str
    dst: str
    volume: int  # Bytes
    deadline: float

@dataclass
class Coflow:
    id: str
    flows: List[Flow]
    priority: int
    arrival_time: float
    
    @property
    def total_volume(self) -> int:
        return sum(f.volume for f in self.flows)
    
    @property
    def width(self) -> int:
        return len(self.flows)

class MultiCoreOCSScheduler:
    """
    Scheduler for coflows in multi-core OCS networks
    """
    
    def __init__(self, num_cores: int, core_capacity: int):
        self.num_cores = num_cores
        self.core_capacity = core_capacity
        self.cores = [[] for _ in range(num_cores)]  # Active circuits per core
        self.waiting_coflows = []
        
    def schedule_coflow(self, coflow: Coflow) -> Dict:
        """
        Schedule a coflow across multiple OCS cores
        
        Returns:
            Scheduling decision with core assignments
        """
        # Sort flows by volume (largest first)
        sorted_flows = sorted(coflow.flows, key=lambda f: f.volume, reverse=True)
        
        assignments = {}
        for flow in sorted_flows:
            best_core = self._select_best_core(flow, coflow)
            if best_core is not None:
                assignments[flow] = best_core
                self._allocate_circuit(best_core, flow)
        
        return {
            'coflow_id': coflow.id,
            'assignments': assignments,
            'estimated_completion': self._estimate_completion(coflow, assignments)
        }
    
    def _select_best_core(self, flow: Flow, coflow: Coflow) -> int:
        """
        Select the best OCS core for a flow based on:
        - Available capacity
        - Existing circuits (reuse if possible)
        - Load balancing
        """
        best_core = None
        best_score = float('-inf')
        
        for core_id in range(self.num_cores):
            score = self._compute_core_score(core_id, flow, coflow)
            if score > best_score:
                best_score = score
                best_core = core_id
        
        return best_core
    
    def _compute_core_score(self, core_id: int, flow: Flow, coflow: Coflow) -> float:
        """
        Compute a score for assigning a flow to a core
        Higher is better
        """
        # Capacity score
        used_capacity = sum(f.volume for f in self.cores[core_id])
        capacity_score = 1.0 - (used_capacity / self.core_capacity)
        
        # Reuse score (prefer cores with existing circuits to same destination)
        reuse_score = sum(1.0 for f in self.cores[core_id] if f.dst == flow.dst)
        
        # Load balance score
        load_score = 1.0 / (1.0 + len(self.cores[core_id]))
        
        return 0.5 * capacity_score + 0.3 * reuse_score + 0.2 * load_score
    
    def _allocate_circuit(self, core_id: int, flow: Flow):
        """Allocate circuit on a core for a flow"""
        self.cores[core_id].append(flow)
    
    def _estimate_completion(self, coflow: Coflow, assignments: Dict) -> float:
        """Estimate completion time for a coflow"""
        if not assignments:
            return float('inf')
        
        max_time = 0
        for flow, core_id in assignments.items():
            # Simplified: time = volume / capacity
            time_needed = flow.volume / self.core_capacity
            max_time = max(max_time, time_needed)
        
        return max_time

# Usage Example
scheduler = MultiCoreOCSScheduler(num_cores=4, core_capacity=100e9)  # 100 Gbps per core
```

## Key Insights

1. **Coflow-Aware Scheduling**: Consider collective completion time, not individual flows
2. **Core Selection**: Balance load while maximizing circuit reuse
3. **Performance Guarantee**: Ensure deadlines are met through admission control
4. **Scalability**: Multi-core architecture enables massive bandwidth aggregation

## Best Practices

- Sort flows by volume (largest first) to minimize coflow completion time
- Reuse existing circuits when possible to reduce setup overhead
- Implement admission control to guarantee performance for admitted coflows
- Monitor core utilization and rebalance periodically

## References

- Wang, X., Shen, H., Tian, H., & Wang, D. (2025). Scheduling Coflows in Multi-Core OCS Networks with Performance Guarantee. arXiv:2604.08242.

## Trigger Words

- coflow scheduling
- optical circuit switching
- data center network
- multi-core OCS
- flow coordination
