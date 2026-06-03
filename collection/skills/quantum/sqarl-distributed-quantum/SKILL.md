---
name: sqarl-distributed-quantum
description: "SQARL (Size-Agnostic Reinforcement Learning) for distributed quantum circuit allocation. Transformer-based approach handling arbitrary qubit/core counts without retraining. Outperforms RL SOTA and matches Hungarian Qubit Allocation (HQA). From arXiv:2605.27027."
category: quantum-computing
tags:
  - quantum-computing
  - distributed-systems
  - reinforcement-learning
  - circuit-compilation
  - qubit-allocation
source: "arXiv:2605.27027"
---

# SQARL: Size-Agnostic RL for Distributed Quantum Circuit Allocation

## Overview

Methodology from arXiv:2605.27027 (May 2026) introducing SQARL - a transformer-based reinforcement learning approach for distributing quantum circuits across multiple QPU cores while minimizing inter-core communication costs.

**Problem**: Scaling quantum processors is limited by decoherence and crosstalk. Distributed quantum computing connects smaller cores, but requires minimizing slow, error-prone inter-core communication. Current RL approaches require retraining per hardware configuration.

**Results**: 33% cost reduction vs HQA on Cuccaro Adder, 25% average reduction on random circuits.

## Architecture

### Transformer-Based Size-Agnostic Design
- Handles arbitrary numbers of qubits and cores without retraining
- Attention mechanism learns structural patterns independent of scale
- Single trained policy works across different quantum hardware topologies

### Qubit Allocation Problem Formulation
```
Input: 
  - Quantum circuit (gates, qubit dependencies)
  - Hardware topology (cores, connectivity, capacities)
Output:
  - Assignment of each qubit to a core
Objective:
  - Minimize inter-core communication (SWAP overhead)
```

## Key Results

| Benchmark | vs HQA | vs Prior RL |
|-----------|--------|-------------|
| Cuccaro Adder | -33% cost | Outperformed |
| Random circuits | -25% avg cost | Outperformed |
| Flexibility | ✓ No retraining | ✗ Requires retraining |

## Implementation Patterns

### Pattern 1: Size-Agnostic Circuit Representation
```python
class CircuitGraph:
    """Represent quantum circuits as graphs for transformer input."""
    def __init__(self, circuit):
        self.qubits = circuit.num_qubits
        self.gates = circuit.gates  # [(gate_type, qubit_a, qubit_b), ...]
        self.dependency_graph = self._build_dependency_graph()
    
    def to_transformer_input(self, max_qubits):
        """Pad/truncate to fixed-size tensor for transformer."""
        # Node features: qubit connectivity degree, gate frequency
        # Edge features: gate type, frequency of 2-qubit gates
        # Positional encoding: relative position in circuit depth
        ...
```

### Pattern 2: Transformer Policy Network
```python
class SQARLPolicy(nn.Module):
    def __init__(self, d_model=256, nhead=8):
        self.encoder = CircuitEncoder(d_model)
        self.transformer = nn.TransformerEncoder(
            encoder_layer=nn.TransformerEncoderLayer(d_model, nhead),
            num_layers=6
        )
        self.allocation_head = nn.Linear(d_model, num_cores)
    
    def forward(self, circuit, hardware):
        # Encode circuit and hardware topology
        circuit_emb = self.encoder(circuit)
        hardware_emb = self.encoder(hardware)
        
        # Cross-attention between circuit and hardware
        combined = self.cross_attention(circuit_emb, hardware_emb)
        
        # Output: allocation decision per qubit
        return self.allocation_head(combined)
```

### Pattern 3: Communication Cost Objective
```python
def compute_communication_cost(allocation, circuit_gates, hardware_topology):
    """Calculate inter-core communication cost for an allocation."""
    cost = 0
    for gate in circuit_gates:
        if gate.is_two_qubit():
            core_a = allocation[gate.qubit_a]
            core_b = allocation[gate.qubit_b]
            if core_a != core_b:
                # Inter-core gate requires communication
                cost += hardware_topology.distance(core_a, core_b)
    return cost
```

### Pattern 4: RL Training Loop
```python
def train_sqarl(agent, environment, episodes=10000):
    for episode in range(episodes):
        circuit = environment.sample_circuit()
        hardware = environment.sample_hardware()
        
        state = CircuitGraph(circuit)
        allocation = agent(state, hardware)
        
        cost = compute_communication_cost(allocation, circuit.gates, hardware)
        reward = -cost  # Minimize cost = maximize reward
        
        # Advantage estimation using HQA baseline
        hqa_cost = hua_qubit_allocation(circuit, hardware)
        advantage = hqa_cost - cost  # Positive = better than HQA
        
        agent.update(state, allocation, advantage)
```

## When to Use

- Distributed quantum computing architectures
- Multi-core quantum processor compilation
- Qubit allocation for NISQ-era devices
- Reducing SWAP overhead in compiled quantum circuits
- Hardware-agnostic quantum compilation pipelines

## Key References

- arXiv: 2605.27027 - "SQARL: A Size-Agnostic Reinforcement Learning approach for Circuit Allocation in Distributed Quantum Architectures"
- HQA (Hungarian Qubit Allocation): Current state-of-the-art heuristic

## Activation Keywords

- distributed quantum, qubit allocation, circuit compilation,
- SQARL, multi-core quantum, SWAP optimization,
- transformer quantum, RL quantum compiler, 分布式量子
