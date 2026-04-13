#!/usr/bin/env python3
"""
Nemo-Nemo DAG-based Consensus - Example Implementation

This script demonstrates the core concepts of the Nemo-Nemo consensus protocol.
"""

import asyncio
import hashlib
import time
from collections import defaultdict
from typing import Set, Dict, List, Optional
from dataclasses import dataclass, field

@dataclass
class DAGNode:
    """Represents a node in the command DAG."""
    command: bytes
    parents: List[str]  # References to parent node hashes
    author: str
    timestamp: float
    
    @property
    def hash(self) -> str:
        """Compute deterministic hash of this node."""
        content = f"{self.command.hex()}:{':'.join(self.parents)}:{self.author}:{self.timestamp}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]

class CommandDAG:
    """Directed Acyclic Graph for command propagation."""
    
    def __init__(self, max_parents: int = 4):
        self.nodes: Dict[str, DAGNode] = {}
        self.edges: Dict[str, Set[str]] = defaultdict(set)
        self.tips: Set[str] = set()
        self.max_parents = max_parents
    
    def add_node(self, node: DAGNode) -> str:
        """Add a node to the DAG and return its hash."""
        node_hash = node.hash
        
        if node_hash in self.nodes:
            return node_hash
        
        self.nodes[node_hash] = node
        
        # Update edges and tips
        for parent in node.parents:
            self.edges[node_hash].add(parent)
            if parent in self.tips:
                self.tips.remove(parent)
        
        self.tips.add(node_hash)
        return node_hash
    
    def select_parents(self) -> List[str]:
        """Select parents for a new node from current tips."""
        return list(self.tips)[:self.max_parents]
    
    def get_ancestors(self, node_hash: str) -> Set[str]:
        """Get all ancestors of a node (transitive closure)."""
        visited = set()
        stack = [node_hash]
        
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                stack.extend(self.edges[current])
        
        return visited

class NemoNemoReplica:
    """Single replica in the Nemo-Nemo consensus protocol."""
    
    def __init__(self, replica_id: str, all_replicas: List[str], max_faulty: int):
        self.replica_id = replica_id
        self.all_replicas = all_replicas
        self.f = max_faulty
        self.quorum = 2 * max_faulty + 1
        self.dag = CommandDAG()
        self.acks: Dict[str, Set[str]] = defaultdict(set)
        self.committed: Set[str] = set()
    
    async def propose(self, command: bytes) -> str:
        """Propose a new command to the consensus."""
        parents = self.dag.select_parents()
        node = DAGNode(command, parents, self.replica_id, time.time())
        node_hash = self.dag.add_node(node)
        
        # Broadcast to all replicas
        await self.broadcast_proposal(node)
        return node_hash
    
    async def broadcast_proposal(self, node: DAGNode):
        """Broadcast proposal to all replicas."""
        print(f"[{self.replica_id}] Broadcasting proposal: {node.hash}")
        # In real implementation: network broadcast
    
    def receive_ack(self, node_hash: str, from_replica: str):
        """Receive acknowledgment from another replica."""
        self.acks[node_hash].add(from_replica)
        
        # Check if we can commit
        if len(self.acks[node_hash]) >= self.quorum:
            asyncio.create_task(self.commit(node_hash))
    
    async def commit(self, node_hash: str):
        """Commit a DAG node."""
        if node_hash in self.committed:
            return
        
        # Ensure all ancestors are committed first
        ancestors = self.dag.get_ancestors(node_hash)
        for ancestor in ancestors:
            if ancestor not in self.committed:
                await self.commit(ancestor)
        
        self.committed.add(node_hash)
        node = self.dag.nodes[node_hash]
        print(f"[{self.replica_id}] Committed: {node_hash} (author={node.author})")
    
    async def run_consensus(self):
        """Main consensus loop."""
        print(f"[{self.replica_id}] Starting consensus loop")
        # In real implementation: handle incoming messages

async def demo():
    """Demonstrate Nemo-Nemo consensus with 4 replicas, 1 faulty allowed."""
    replicas = [f"R{i}" for i in range(4)]
    f = 1  # Max 1 faulty replica
    
    # Create replicas
    nodes = {r: NemoNemoReplica(r, replicas, f) for r in replicas}
    
    # Simulate proposals from multiple leaders
    print("=== Multi-Leader Proposal Phase ===")
    
    # R0 proposes command 1
    hash1 = await nodes["R0"].propose(b"Transfer $100: Alice -> Bob")
    
    # R1 proposes command 2 (simultaneously)
    hash2 = await nodes["R1"].propose(b"Transfer $50: Charlie -> Dave")
    
    # R2 proposes command 3
    hash3 = await nodes["R2"].propose(b"Read balance: Alice")
    
    print("\n=== Simulating Acknowledgments ===")
    
    # Simulate replicas acknowledging proposals
    for node_hash in [hash1, hash2, hash3]:
        for replica in replicas[:3]:  # 3 acks = quorum
            nodes[replica].receive_ack(node_hash, replica)
    
    # Wait for commits
    await asyncio.sleep(0.1)
    
    print("\n=== DAG State ===")
    for r_id, node in nodes.items():
        print(f"{r_id}: {len(node.dag.nodes)} nodes, {len(node.committed)} committed")

if __name__ == "__main__":
    asyncio.run(demo())
