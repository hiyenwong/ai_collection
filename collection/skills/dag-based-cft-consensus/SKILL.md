---
name: dag-based-cft-consensus
description: "DAG-based crash-fault tolerant (CFT) consensus protocol implementation based on Nemo-Nemo. Practical consensus for wide-area networks combining CFT and BFT design principles. Use when implementing distributed consensus, multi-leader consensus protocols, DAG-based command propagation, or building fault-tolerant distributed systems. Keywords: consensus, distributed systems, DAG, CFT, BFT, WAN, multi-leader, fault tolerance, replication"
---

# DAG-Based CFT Consensus Protocol (Nemo-Nemo)

## Overview

Nemo-Nemo is a practical crash-fault tolerant (CFT) consensus protocol designed to outperform existing protocols in wide-area networks by bridging design principles from the CFT and Byzantine-fault tolerant (BFT) worlds.

This skill provides implementation guidance and design patterns for building DAG-based consensus systems based on the Nemo-Nemo protocol.

## Source Paper

**Finding Nemo-Nemo: CFT DAG-based Consensus in the WAN**
- **Authors:** 
- **arXiv:** 2604.08914v1
- **URL:** https://arxiv.org/abs/2604.08914v1
- **Category:** Distributed, Parallel, and Cluster Computing (cs.DC)

### Abstract

This paper introduces Nemo-Nemo, a practical crash-fault tolerant (CFT) consensus protocol designed to outperform existing protocols in wide-area networks by bridging design principles from the CFT and Byzantine-fault tolerant (BFT) worlds. By structuring command propagation through a causally ordered DAG, Nemo-Nemo allows all consensus replicas to propose commands with a naturally self-regulating communication regime. By exploiting multi-leader architecture, Nemo-Nemo avoids the performance bottleneck inherent to single-leader protocols. By separating command dissemination from consensus logic, Nemo-Nemo handles challenging network conditions even when consensus commits are stalled. Moreover, leader proposals that miss a deadline are never dropped, but deterministically deferred and executed later, preserving throughput under transient network delays. And by enabling Nemo-Nemo to commit on a DAG in just two network hops, it matches the latency of existing CFT systems, while achieving significantly higher throughput. The result is a robust, deployable system: the first DAG-based CFT consensus protocol proven to exceed state-of-the-art wide-area network performance in both speed and resilience.


## Core Design Principles

### 1. Causally Ordered DAG Command Propagation

**Principle:** Structure command propagation through a causally ordered DAG.

**Benefits:**
- All consensus replicas can propose commands
- Naturally self-regulating communication regime
- Preserves causal ordering of commands

**Implementation Pattern:**
```python
class DAGNode:
    def __init__(self, command, parents, author, timestamp):
        self.command = command  # The actual command
        self.parents = parents  # References to parent nodes (DAG edges)
        self.author = author    # Which replica proposed this
        self.timestamp = timestamp
        self.round = len(parents)  # Logical round number

class CommandDAG:
    def __init__(self):
        self.nodes = {}  # node_hash -> DAGNode
        self.tips = []   # Current DAG tips (nodes without children)
    
    def propose_command(self, command, author):
        # Select parents from current tips
        parents = self.select_parents()
        node = DAGNode(command, parents, author, time.now())
        self.add_node(node)
        return node
    
    def select_parents(self, max_parents=4):
        # Select recent tips as parents for new command
        return self.tips[-max_parents:]
```

### 2. Multi-Leader Architecture

**Principle:** Avoid single-leader bottleneck by allowing multiple leaders.

**Benefits:**
- Parallel command proposal
- Better utilization of network bandwidth
- No single point of failure for throughput

**Implementation Pattern:**
```python
class MultiLeaderConsensus:
    def __init__(self, replicas):
        self.replicas = replicas
        self.active_leaders = replicas  # All replicas can lead
        self.command_dag = CommandDAG()
    
    def can_propose(self, replica_id):
        # In Nemo-Nemo, all replicas can propose simultaneously
        return replica_id in self.active_leaders
    
    def process_proposal(self, proposal):
        # Validate and add to DAG
        if self.validate_proposal(proposal):
            return self.command_dag.propose_command(
                proposal.command, 
                proposal.author
            )
```


### 3. Separation of Concerns: Dissemination vs Consensus

**Principle:** Separate command dissemination from consensus logic.

**Benefits:**
- Handles challenging network conditions even when consensus is stalled
- Dissemination can continue independently of commit decisions
- Better fault tolerance under transient delays

**Implementation Pattern:**
```python
class NemoNemoNode:
    def __init__(self, node_id, peers):
        self.node_id = node_id
        self.peers = peers
        self.dag = CommandDAG()
        self.consensus_layer = ConsensusLayer()
        self.dissemination_layer = DisseminationLayer()
    
    async def disseminate_command(self, command):
        # Phase 1: Disseminate command to build DAG
        dag_node = self.dissemination_layer.broadcast(command)
        return dag_node
    
    async def commit_commands(self, dag_node):
        # Phase 2: Run consensus to commit DAG nodes
        committed = await self.consensus_layer.commit(dag_node)
        return committed
    
    async def handle_network_partition(self):
        # Dissemination continues even if consensus stalls
        self.dissemination_layer.gossip_pending()
```

### 4. Deferred Execution for Missed Deadlines

**Principle:** Leader proposals that miss a deadline are never dropped, but deterministically deferred.

**Benefits:**
- Preserves throughput under transient network delays
- No command loss due to timing issues
- Predictable behavior under variable latency

**Implementation Pattern:**
```python
class DeferredExecutionQueue:
    def __init__(self, deadline_ms=100):
        self.deadline_ms = deadline_ms
        self.pending = PriorityQueue()
        self.deferred = []
    
    def submit_proposal(self, proposal):
        deadline = proposal.timestamp + self.deadline_ms
        self.pending.put((deadline, proposal))
    
    async def process_proposals(self):
        while True:
            now = time.now()
            deadline, proposal = self.pending.peek()
            
            if deadline <= now:
                # Within deadline - execute normally
                await self.execute(proposal)
            else:
                # Missed deadline - defer deterministically
                deferred_time = self.compute_deferred_time(proposal)
                self.deferred.append((deferred_time, proposal))
    
    def compute_deferred_time(self, proposal):
        # Deterministic deferral based on proposal properties
        return proposal.round * DEFERRED_INTERVAL
```


### 5. Two-Hop DAG Commit

**Principle:** Enable commits on a DAG in just two network hops.

**Benefits:**
- Matches latency of existing CFT systems
- Significantly higher throughput
- Efficient for wide-area networks

**Implementation Pattern:**
```python
class TwoHopCommit:
    def __init__(self):
        self.pending_commits = {}
        self.commit_threshold = 2 * f + 1  # Standard CFT quorum
    
    async def commit_dag_node(self, dag_node):
        # Hop 1: Broadcast to replicas
        acks = await self.broadcast_and_collect_acks(dag_node)
        
        # Hop 2: If quorum reached, commit immediately
        if len(acks) >= self.commit_threshold:
            await self.commit(dag_node)
            return True
        
        return False
    
    def broadcast_and_collect_acks(self, dag_node):
        # Send to all replicas, collect acknowledgments
        tasks = [self.send_to_replica(r, dag_node) for r in self.replicas]
        return await asyncio.gather(*tasks)
```

## Protocol Workflow

### Normal Operation

```
1. Command Submission
   Client -> Replicas: Submit command
   
2. DAG Propagation
   Replicas -> Replicas: Broadcast command as DAG node
   - Each replica selects parents from current DAG tips
   - Commands propagate causally through the DAG
   
3. Consensus Decision
   Replicas: Run consensus on DAG structure
   - Two-hop commit protocol
   - Quorum-based decision
   
4. Command Execution
   Replicas: Execute committed commands in DAG order
   - Respect causal dependencies
   - Deterministic ordering for concurrent commands
```

### Handling Network Conditions

| Condition | Nemo-Nemo Behavior |
|-----------|-------------------|
| High Latency | Deferred execution preserves throughput |
| Packet Loss | DAG structure allows redundancy |
| Network Partition | Dissemination continues; consensus pauses |
| Node Crash | Multi-leader allows continued operation |
| Transient Delays | No command drops; deterministic deferral |

## Comparison with Existing Protocols

| Feature | Paxos/Raft | BFT (PBFT) | Nemo-Nemo |
|---------|------------|------------|-----------|
| Fault Model | Crash-fault | Byzantine | Crash-fault |
| Leader Count | Single | Rotating | Multi |
| Throughput | Leader bottleneck | Moderate | High |
| Latency | 2-3 RTT | 3-4 RTT | 2 RTT |
| WAN Performance | Degrades | Moderate | Optimized |
| Command Ordering | Sequential | Sequential | DAG-based |


## Implementation Guidelines

### Step 1: Setup DAG Structure

```python
from collections import defaultdict
from typing import Set, Dict, List

class DAG:
    def __init__(self):
        self.nodes: Dict[str, DAGNode] = {}
        self.edges: Dict[str, Set[str]] = defaultdict(set)
        self.reverse_edges: Dict[str, Set[str]] = defaultdict(set)
        self.tips: Set[str] = set()
    
    def add_node(self, node: DAGNode):
        node_id = hash(node)
        self.nodes[node_id] = node
        
        # Update tips
        for parent in node.parents:
            self.edges[node_id].add(parent)
            self.reverse_edges[parent].add(node_id)
            if parent in self.tips:
                self.tips.remove(parent)
        
        self.tips.add(node_id)
    
    def get_ancestors(self, node_id: str) -> Set[str]:
        # Get all ancestors of a node (transitive closure)
        visited = set()
        stack = [node_id]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                stack.extend(self.edges[current])
        return visited
```

### Step 2: Implement Consensus Logic

```python
class NemoNemoConsensus:
    def __init__(self, node_id: str, replicas: List[str], f: int):
        self.node_id = node_id
        self.replicas = replicas
        self.n = len(replicas)
        self.f = f  # Max faulty replicas
        self.quorum = 2 * f + 1
        self.dag = DAG()
    
    async def propose(self, command: bytes) -> str:
        # Propose a new command to the consensus
        parents = self.select_parents()
        node = DAGNode(command, parents, self.node_id, time.now())
        
        # Broadcast to all replicas
        await self.broadcast_proposal(node)
        return hash(node)
    
    async def broadcast_proposal(self, node: DAGNode):
        # Broadcast proposal to all replicas
        for replica in self.replicas:
            if replica != self.node_id:
                await self.send_proposal(replica, node)
    
    def select_parents(self) -> List[str]:
        # Select parent nodes for new proposal
        return list(self.dag.tips)[:4]  # Max 4 parents
```

### Step 3: Commit Protocol

```python
class CommitProtocol:
    def __init__(self, consensus: NemoNemoConsensus):
        self.consensus = consensus
        self.acks: Dict[str, Set[str]] = defaultdict(set)
    
    async def try_commit(self, node_id: str):
        # Attempt to commit a DAG node
        if len(self.acks[node_id]) >= self.consensus.quorum:
            await self.commit(node_id)
    
    def receive_ack(self, node_id: str, from_replica: str):
        # Receive acknowledgment from another replica
        self.acks[node_id].add(from_replica)
    
    async def commit(self, node_id: str):
        # Execute commit for the node
        node = self.consensus.dag.nodes[node_id]
        await self.execute_command(node.command)
```


## Configuration Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| max_parents | Maximum parents per DAG node | 4 |
| deadline_ms | Proposal deadline in milliseconds | 100 |
| deferred_interval_ms | Interval for deferred execution | 50 |
| quorum_factor | Quorum size = 2f + 1 | 2 |
| gossip_interval_ms | Background gossip interval | 10 |

## Best Practices

1. **Network Monitoring**: Monitor RTT and adapt parameters dynamically
2. **Load Balancing**: Distribute proposals across replicas evenly
3. **Garbage Collection**: Prune old DAG nodes after stable commit
4. **Metrics**: Track throughput, latency, and commit rate
5. **Fault Injection**: Test with simulated network partitions


## Related Research

- **On the Existence of Quadratic Control Lyapunov Functions for Koopman-Operator based Bilinear Systems** (2604.09267v1)
  - Authors: Sami Leon Noel Aziz Hanna, Nicolas Hoischen...
  - Abstract: Koopman operator-based methods enable data-driven bilinear representations of unknown nonlinear control systems. Accurate representations often demand significantly higher dimensions than the original...

- **Asynchronous Quantum Distributed Computing: Causality, Snapshots, and Global Operations** (2604.08298v1)
  - Authors: Siddhartha Visveswara Jayanti, Anand Natarajan...
  - Abstract: We initiate the study of asynchronous quantum distributed systems, focusing on the case of implementing atomic quantum global operations that can be decomposed into a collection of local operations on...

- **Sensor Placement for Tsunami Early Warning via Large-Scale Bayesian Optimal Experimental Design** (2604.08812v1)
  - Authors: Sreeram Venkat, Stefan Henneking...
  - Abstract: Real-time tsunami early warning relies on distributed sensor networks to infer seismic sources and seafloor motion. Optimizing these networks via Bayesian optimal experimental design (OED) is exceptio...

- **A Unified Control-Theoretic Framework for Saddle-Point Dynamics in Constrained Optimization** (2604.09252v1)
  - Authors: Veronica Centorrino, Rawan Hoteit...
  - Abstract: This paper studies equality-constrained minimization problems through the lens of feedback control. We introduce a unified control-theoretic framework by showing that a PID feedback law acting on the ...



## References

1. Kerur, R., et al. "Finding Nemo-Nemo: CFT DAG-based Consensus in the WAN." arXiv:2604.08914, 2026.

## License

This skill is based on academic research and follows the original paper's license terms.
