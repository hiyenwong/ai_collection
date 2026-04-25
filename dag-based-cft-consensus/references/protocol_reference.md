# Nemo-Nemo Protocol Reference

## Key Concepts

### DAG Structure
The Directed Acyclic Graph (DAG) is the core data structure in Nemo-Nemo.
- **Node**: Represents a proposed command
- **Edges**: Represent causal dependencies
- **Tips**: Nodes without children (current frontier)

### Multi-Leader Design
Unlike Paxos/Raft which use a single leader, Nemo-Nemo allows all replicas to propose commands simultaneously.

### Two-Hop Commit
Nemo-Nemo achieves commit in just two network hops:
1. Broadcast proposal to all replicas
2. Collect acknowledgments from quorum

## Protocol Correctness

### Safety Properties
- **Agreement**: No two replicas commit different values
- **Validity**: Only proposed values can be committed
- **Integrity**: Each replica commits at most once per command

### Liveness Properties
- **Termination**: Eventually, every correct replica commits
- **Deferred Execution**: Proposals not dropped on timeout

## Comparison with Other Protocols

| Protocol | Throughput | Latency | Leader | DAG |
|----------|-----------|---------|--------|-----|
| Paxos | Low | 2 RTT | Single | No |
| Raft | Medium | 2 RTT | Single | No |
| PBFT | Medium | 3 RTT | Rotating | No |
| Nemo-Nemo | High | 2 RTT | Multi | Yes |

## Use Cases

1. **Wide-Area Networks**: Optimized for high-latency environments
2. **Multi-Region Systems**: Distributed across geographic regions
3. **High-Throughput Applications**: Financial systems, IoT networks
4. **Blockchain Sidechains**: Fast consensus for off-chain transactions

## Performance Optimization

### Parameter Tuning
- **max_parents**: Balance between DAG width and depth
- **deadline_ms**: Adapt to network RTT
- **gossip_interval**: Control background traffic

### Network Optimizations
- Batch multiple commands per proposal
- Compress DAG node references
- Use UDP for dissemination, TCP for consensus
