---
name: coflow-scheduling-ocs
description: "Coflow scheduling in multi-core Optical Circuit Switching (OCS) networks with performance guarantees. Addresses bandwidth allocation and scheduling for data-intensive distributed applications. Activation: coflow scheduling, OCS networks, optical circuit switching, multi-core scheduling."
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [coflow-scheduling, optical-circuit-switching, multi-core-networks, bandwidth-allocation, distributed-systems, performance-guarantees]
    source_paper: "Scheduling Coflows in Multi-Core OCS Networks with Performance Guarantee (arXiv:2604.08242v1)"
    citations: 0
    published: "2026-04-09"
    category: "distributed computing"
---

# Coflow Scheduling in Multi-Core OCS Networks

## Overview
This skill provides methodologies for scheduling coflows in multi-core Optical Circuit Switching (OCS) networks. Coflows represent collections of flows that share a common performance goal, common in data-intensive distributed applications like MapReduce and Spark. This work addresses the gap in coflow scheduling research for multi-core OCS fabrics under the not-all-stop reconfiguration model.

## Key Insights

### Problem Statement
- Existing coflow scheduling focuses on single-core settings
- Multi-core OCS fabrics require different scheduling approaches
- Not-all-stop reconfiguration: one circuit's reconfiguration doesn't interrupt others
- Need for performance guarantees in multi-core OCS networks

### Core Innovation
- **Multi-Core OCS Model**: Scheduling for multiple independent OCS cores
- **Not-All-Stop Reconfiguration**: Efficient circuit reconfiguration without full stops
- **Performance Guarantees**: Theoretical bounds on coflow completion times

## Implementation Pattern

### Coflow Scheduling Framework
```python
from typing import List, Dict, Tuple, Set
from dataclasses import dataclass
from enum import Enum
import heapq

class FlowStatus(Enum):
    PENDING = "pending"
    SCHEDULED = "scheduled"
    ACTIVE = "active"
    COMPLETED = "completed"

@dataclass
class Flow:
    """Represents a single flow within a coflow."""
    id: str
    src: str
    dst: str
    size: int  # bytes
    status: FlowStatus = FlowStatus.PENDING
    start_time: float = None
    completion_time: float = None

@dataclass
class Coflow:
    """Represents a coflow - collection of flows with shared goal."""
    id: str
    flows: List[Flow]
    arrival_time: float
    deadline: float = None
    priority: int = 0
    
    @property
    def total_size(self) -> int:
        return sum(f.size for f in self.flows)
    
    @property
    def width(self) -> int:
        """Number of unique source-destination pairs."""
        return len(set((f.src, f.dst) for f in self.flows))
    
    @property
    def bottleneck(self) -> int:
        """Maximum traffic on any link."""
        link_traffic = {}
        for f in self.flows:
            link = (f.src, f.dst)
            link_traffic[link] = link_traffic.get(link, 0) + f.size
        return max(link_traffic.values()) if link_traffic else 0

@dataclass
class OCSCore:
    """Represents an Optical Circuit Switching core."""
    id: str
    capacity: float  # Gbps
    circuits: Dict[Tuple[str, str], Dict]  # (src, dst) -> circuit info
    reconfiguration_time: float  # seconds
    
    def can_establish_circuit(self, src: str, dst: str) -> bool:
        """Check if a new circuit can be established."""
        return (src, dst) not in self.circuits
    
    def establish_circuit(self, src: str, dst: str, bandwidth: float):
        """Establish a new optical circuit."""
        self.circuits[(src, dst)] = {
            'bandwidth': bandwidth,
            'established_at': time.time(),
            'active': True
        }
    
    def reconfigure_circuit(self, src: str, dst: str, new_bandwidth: float):
        """Reconfigure existing circuit (not-all-stop model)."""
        if (src, dst) in self.circuits:
            self.circuits[(src, dst)]['bandwidth'] = new_bandwidth
            self.circuits[(src, dst)]['reconfigured_at'] = time.time()

class MultiCoreOCSNetwork:
    """Represents a multi-core OCS network."""
    
    def __init__(self, num_cores: int, core_capacity: float):
        self.cores = [
            OCSCore(
                id=f"core_{i}",
                capacity=core_capacity,
                circuits={},
                reconfiguration_time=0.01
            )
            for i in range(num_cores)
        ]
        self.core_assignment = {}  # flow_id -> core_id
    
    def get_available_core(self, src: str, dst: str) -> OCSCore:
        """Find an available core for a new circuit."""
        for core in self.cores:
            if core.can_establish_circuit(src, dst):
                return core
        return None
    
    def get_core_for_flow(self, flow_id: str) -> OCSCore:
        """Get the core assigned to a flow."""
        core_id = self.core_assignment.get(flow_id)
        if core_id:
            return next(c for c in self.cores if c.id == core_id)
        return None

class CoflowScheduler:
    """
    Scheduler for coflows in multi-core OCS networks.
    
    Implements scheduling algorithms with performance guarantees
    for the not-all-stop reconfiguration model.
    """
    
    def __init__(self, network: MultiCoreOCSNetwork):
        self.network = network
        self.pending_coflows: List[Coflow] = []
        self.active_coflows: Dict[str, Coflow] = {}
        self.completed_coflows: List[Coflow] = []
        self.current_time = 0.0
    
    def add_coflow(self, coflow: Coflow):
        """Add a new coflow to the pending queue."""
        self.pending_coflows.append(coflow)
        self._sort_pending_coflows()
    
    def _sort_pending_coflows(self):
        """Sort pending coflows by scheduling policy."""
        # Shortest Remaining Time First (SRTF) variant
        self.pending_coflows.sort(
            key=lambda c: (c.total_size / max(c.width, 1), c.arrival_time)
        )
    
    def schedule_coflows(self):
        """Schedule pending coflows onto available cores."""
        scheduled = []
        
        for coflow in self.pending_coflows[:]:
            if self._can_schedule_coflow(coflow):
                success = self._schedule_coflow(coflow)
                if success:
                    scheduled.append(coflow)
                    self.pending_coflows.remove(coflow)
                    self.active_coflows[coflow.id] = coflow
        
        return scheduled
    
    def _can_schedule_coflow(self, coflow: Coflow) -> bool:
        """Check if a coflow can be scheduled given current network state."""
        # Check if all required circuits can be established
        unique_links = set((f.src, f.dst) for f in coflow.flows)
        
        for src, dst in unique_links:
            available = self.network.get_available_core(src, dst)
            if not available:
                return False
        
        return True
    
    def _schedule_coflow(self, coflow: Coflow) -> bool:
        """Schedule a coflow by establishing necessary circuits."""
        try:
            unique_links = set((f.src, f.dst) for f in coflow.flows)
            
            for src, dst in unique_links:
                core = self.network.get_available_core(src, dst)
                if core:
                    # Calculate required bandwidth
                    total_flow_size = sum(
                        f.size for f in coflow.flows
                        if f.src == src and f.dst == dst
                    )
                    required_bw = total_flow_size / self._estimate_completion_time(coflow)
                    
                    # Establish circuit
                    core.establish_circuit(src, dst, min(required_bw, core.capacity))
                    
                    # Assign flows to this core
                    for f in coflow.flows:
                        if f.src == src and f.dst == dst:
                            self.network.core_assignment[f.id] = core.id
                            f.status = FlowStatus.SCHEDULED
                            f.start_time = self.current_time
            
            return True
        except Exception as e:
            print(f"Error scheduling coflow {coflow.id}: {e}")
            return False
    
    def _estimate_completion_time(self, coflow: Coflow) -> float:
        """Estimate completion time for a coflow."""
        # Simple estimation based on bottleneck link
        bottleneck = coflow.bottleneck
        avg_capacity = sum(c.capacity for c in self.network.cores) / len(self.network.cores)
        return bottleneck / avg_capacity if avg_capacity > 0 else float('inf')
    
    def update_progress(self, time_delta: float):
        """Update flow progress and complete finished flows."""
        self.current_time += time_delta
        
        for coflow_id, coflow in list(self.active_coflows.items()):
            all_completed = True
            
            for flow in coflow.flows:
                if flow.status == FlowStatus.SCHEDULED:
                    core = self.network.get_core_for_flow(flow.id)
                    if core:
                        circuit = core.circuits.get((flow.src, flow.dst))
                        if circuit:
                            # Simulate data transfer
                            transferred = circuit['bandwidth'] * time_delta
                            flow.size -= transferred
                            
                            if flow.size <= 0:
                                flow.status = FlowStatus.COMPLETED
                                flow.completion_time = self.current_time
                                flow.size = 0
                            else:
                                all_completed = False
                elif flow.status != FlowStatus.COMPLETED:
                    all_completed = False
            
            if all_completed:
                self.completed_coflows.append(coflow)
                del self.active_coflows[coflow_id]
    
    def get_performance_metrics(self) -> Dict:
        """Calculate performance metrics for completed coflows."""
        if not self.completed_coflows:
            return {}
        
        completion_times = [
            c.flows[0].completion_time - c.arrival_time
            for c in self.completed_coflows
            if c.flows and c.flows[0].completion_time
        ]
        
        return {
            'total_coflows': len(self.completed_coflows),
            'avg_completion_time': sum(completion_times) / len(completion_times) if completion_times else 0,
            'max_completion_time': max(completion_times) if completion_times else 0,
            'min_completion_time': min(completion_times) if completion_times else 0,
            'pending_coflows': len(self.pending_coflows),
            'active_coflows': len(self.active_coflows)
        }


# Example usage
if __name__ == "__main__":
    # Create multi-core OCS network
    network = MultiCoreOCSNetwork(num_cores=4, core_capacity=100.0)  # 100 Gbps per core
    
    # Create scheduler
    scheduler = CoflowScheduler(network)
    
    # Add sample coflows
    coflow1 = Coflow(
        id="coflow_1",
        flows=[
            Flow(id="f1", src="A", dst="B", size=1e9),  # 1 GB
            Flow(id="f2", src="A", dst="C", size=2e9),  # 2 GB
            Flow(id="f3", src="B", dst="D", size=1.5e9),  # 1.5 GB
        ],
        arrival_time=0.0
    )
    
    scheduler.add_coflow(coflow1)
    
    # Schedule and simulate
    scheduled = scheduler.schedule_coflows()
    print(f"Scheduled {len(scheduled)} coflows")
```

## Best Practices

### 1. Coflow Characterization
- Analyze coflow width (number of parallel flows)
- Identify bottleneck links
- Consider deadline requirements

### 2. Multi-Core Assignment
- Balance load across OCS cores
- Minimize reconfiguration overhead
- Consider circuit locality

### 3. Performance Monitoring
- Track coflow completion times
- Monitor core utilization
- Measure reconfiguration frequency

## References
- Wang, X., Shen, H., Tian, H., & Wang, D. (2026). Scheduling Coflows in Multi-Core OCS Networks with Performance Guarantee. arXiv:2604.08242v1.

## Related Skills
- distributed-systems-scheduling
- optical-networking
- data-center-networking
- performance-modeling
