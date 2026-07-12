# Tierkreis Dataflow Framework

## Overview

Tierkreis is a higher-order dataflow graph program representation and runtime designed for compositional, quantum-classical hybrid algorithms.

## Key Features

### 1. Dataflow Graph Representation

- **Higher-order**: Supports nested graphs and composition
- **Type-safe**: Strong typing for quantum and classical operations
- **Visual**: Graph-based visualization of algorithm flow

### 2. Runtime Architecture

```
┌─────────────────┐
│  Classical Node │────┐
└─────────────────┘    │
                       ↓
┌─────────────────┐  ┌─────────────────┐
│  Quantum Node   │──│  Dataflow Engine│
└─────────────────┘  └─────────────────┘
                       ↑
┌─────────────────┐    │
│  Cloud Interface│────┘
└─────────────────┘
```

### 3. Composition Patterns

**Sequential Composition**
```
Node A → Node B → Node C
```

**Parallel Composition**
```
Node A → [Node B, Node C] → Node D
```

**Nested Composition**
```
Node A → Graph(X → Y → Z) → Node B
```

## Use Cases

- **Cloud Quantum Access**: Remote quantum computer integration
- **Hybrid Algorithms**: VQE, QAOA with classical optimization
- **Distributed Computing**: Multi-node quantum clusters

## Reference

arXiv:2211.02350 - "Tierkreis: A Dataflow Framework for Hybrid Quantum-Classical Computing"