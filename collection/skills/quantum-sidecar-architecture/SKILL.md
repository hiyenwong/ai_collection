---
name: quantum-sidecar-architecture
description: "Quantum sidecar architecture patterns for hybrid AI training and inference - stateful protected registers, stateless reset-and-reprepare circuits, and quantum weight-state sidecars"
version: 1.0.0
author: Hermes Agent (Cron Job)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Quantum, AI Architecture, Hybrid Computing, Systems Engineering, ML Infrastructure]
    related_skills: [quantum-system-engineering, quantum-ml-patterns]
  paper:
    arxiv_id: "2605.18031"
    title: "Quantum Sidecar Architectures for Hybrid AI Training and Inference"
    authors: "Y. Mo, G. D. Su"
    published: "2026-05-18"
    categories: "quant-ph, cs.AI"
---

# Quantum Sidecar Architecture

## Overview

Architecture patterns for integrating quantum co-processors as sidecars in classical AI training and inference pipelines. Instead of storing entire models in quantum memory, quantum sidecars act as bounded signal generators for optimizer-side operations.

**Key insight**: Don't try to replace classical transformers with quantum models. Instead, attach quantum co-processors as sidecars that generate signals for specific sub-problems: sampling, routing, expert selection, and reasoning-path proposal.

## Two Operating Modes

### Mode 1: Stateful Protected Register

**Architecture**: Protected register + Ancilla/Temporary register

```
┌─────────────────────────────────────┐
│  Classical AI Pipeline              │
│  (Transformer / LLM)                │
│                                     │
│         │ requests signal           │
│         ▼                           │
│  ┌─────────────────────┐            │
│  │ Quantum Sidecar     │            │
│  │                     │            │
│  │  Protected Register │◄── State   │
│  │  (reusable resource)│            │
│  │         │           │            │
│  │  Ancilla Register   │──► QND     │
│  │  (temporary)        │    readout │
│  └─────────────────────┘            │
│         │ returns signal            │
│         ▼                           │
│  Continue classical processing      │
└─────────────────────────────────────┘
```

**Key characteristics**:
- Protected register stores reusable quantum resource state
- Ancilla performs QND-style (Quantum Non-Demolition) readout
- State persists across multiple queries
- Useful for: optimizer-side sampling, adapter selection, expert routing

**Implementation**:
```python
class StatefulQuantumSidecar:
    def __init__(self, n_protected_qubits, circuit_depth=4):
        self.n_protected = n_protected_qubits  # 2/4/6/8
        self.circuit = self._build_parity_readout_circuit()
        self.protected_state = None
    
    def prepare_protected_state(self):
        """Initialize protected register with reusable resource"""
        self.protected_state = self._create_entangled_state()
    
    def qnd_readout(self, ancilla_state):
        """QND-style parity readout using ancilla"""
        # Apply controlled operations from protected to ancilla
        # Measure ancilla without disturbing protected state
        result = self._measure_ancilla()
        return result
    
    def _build_parity_readout_circuit(self):
        """Build circuit for parity-based readout"""
        # Qiskit implementation
        pass
```

### Mode 2: Stateless Reset-and-Reprepare

**Architecture**: Prepare → Evolve → Measure → Reset → Repeat

```
┌─────────────────────────────────────┐
│  Classical AI Pipeline              │
│                                     │
│  For each query:                    │
│    1. Prepare task-conditioned      │
│       quantum circuit               │
│    2. Evolve over control variables │
│    3. Measure candidate signals     │
│    4. Reset qubits                  │
│    5. Repeat as needed              │
│                                     │
│  Return aggregated signal           │
└─────────────────────────────────────┘
```

**Key characteristics**:
- Each query prepares fresh task-conditioned circuit
- Bounded evolution over training/inference control variables
- Measurement produces candidate signals
- Qubits reset after each iteration
- Useful for: candidate-update sampling, QAOA-style optimization

**Implementation**:
```python
class StatelessQuantumSidecar:
    def __init__(self, n_qubits):
        self.n_qubits = n_qubits
        self.reset_overhead = self._measure_reset_cost()
    
    def query(self, task_variables, n_iterations=10):
        """Stateless query: prepare, evolve, measure, reset"""
        results = []
        for _ in range(n_iterations):
            # Prepare task-conditioned circuit
            circuit = self._prepare_circuit(task_variables)
            
            # Evolve over control variables
            circuit = self._evolve(circuit, task_variables)
            
            # Measure candidate signals
            result = self._measure(circuit)
            results.append(result)
            
            # Reset qubits (overhead consideration)
            self._reset_qubits()
        
        return self._aggregate(results)
    
    def qaoa_sampler(self, problem_hamiltonian, p_layers=2):
        """QAOA-style statevector sampling over candidate landscapes"""
        # Build QAOA circuit with problem + mixer Hamiltonians
        # Sample candidate solutions
        pass
```

## Application Patterns

### 1. Optimizer-Side Sampling
- Quantum sidecar generates candidate parameter updates
- Classical optimizer selects from candidates
- Hybrid: quantum explores, classical exploits

### 2. Expert/Adapter Selection
- Sidecar evaluates which MoE expert or adapter to use
- Parity readout produces selection signal
- Reduces routing computation on classical side

### 3. Retrieval Augmentation
- Sidecar generates relevance signals for RAG
- Quantum amplitude amplification for similarity search
- Classical side handles document storage

### 4. Reasoning-Path Proposal
- Sidecar proposes reasoning paths for chain-of-thought
- QAOA-style sampling over path space
- Classical side validates and executes selected path

## Quantum Weight-State Sidecars (Speculative)

**Concept**: Restricted quantum representations over model-control variables, not complete weight tensors.

- **NOT**: Encoding full classical weight matrices in qubits
- **IS**: Quantum representation of control knobs (learning rates, regularization, architecture choices)
- Quantum sidecar suggests control variable adjustments
- Classical pipeline applies adjustments to model

## Design Principles

1. **Bounded Scope**: Quantum sidecars handle specific sub-problems, not entire models
2. **Physical Realism**: Respect qubit count limits, decoherence times, gate fidelities
3. **Signal Generation**: Sidecars produce signals, not answers
4. **Reset Overhead Awareness**: Stateless mode must account for qubit reset costs
5. **Complementary**: Classical and quantum components complement, not compete

## Pitfalls

- **Overpromising**: Don't claim quantum stores full transformer models
- **Ignoring Reset Costs**: Stateless mode qubit reset has real overhead
- **Direct Weight Encoding**: Don't encode full weight tensors; use control variables instead
- **No Benchmarking**: Always cross-check quantum sidecar output against classical baseline

## When to Use

- Designing hybrid quantum-classical AI infrastructure
- Need bounded quantum assistance for specific ML sub-problems
- Exploring quantum co-processor integration patterns
- Building optimizer-side sampling, routing, or retrieval augmentation

## Activation

Trigger words: quantum sidecar, hybrid AI architecture, quantum co-processor, QND readout, reset-and-reprepare, quantum sampling for ML, quantum routing
