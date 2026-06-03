# Quantum Optimization Algorithms Comparison

## Algorithm Overview

### QAOA (Quantum Approximate Optimization Algorithm)

**Strengths**:
- Gate-based universal quantum computers
- Tunable depth (p layers)
- Good for general combinatorial problems

**Limitations**:
- Requires careful parameter tuning
- Performance depends on circuit depth
- NISQ noise affects results

**Implementation**:
```python
from qiskit_optimization.algorithms import QAOA
from qiskit.algorithms.optimizers import COBYLA

optimizer = COBYLA(maxiter=100)
qaoa = QAOA(optimizer=optimizer, reps=3, quantum_instance=backend)
```

### Quantum Annealing (D-Wave)

**Strengths**:
- Designed for QUBO problems
- Handles larger problem sizes (1000+ qubits)
- Natural fit for portfolio optimization

**Limitations**:
- Limited connectivity (Pegasus topology)
- Requires embedding for dense problems
- Access to D-Wave hardware needed

**Implementation**:
```python
from dwave.system import DWaveSampler, EmbeddingComposite

sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample_qubo(Q, num_reads=1000)
```

### VQE (Variational Quantum Eigensolver)

**Strengths**:
- Flexible ansatz design
- Can handle higher-order terms
- Works on NISQ devices

**Limitations**:
- Requires ansatz selection
- Parameter optimization overhead
- Less natural for QUBO than QAOA

### Hybrid Quantum-Classical

**Strengths**:
- Practical for real applications
- Leverages classical strengths
- Works around quantum limitations

**Workflow**:
1. Classical: Filter candidates, compute statistics
2. Quantum: Solve reduced optimization
3. Classical: Refine and validate solution

## Performance Comparison

| Algorithm | Problem Size | Accuracy | Hardware |
|-----------|--------------|----------|----------|
| QAOA | ≤ 20 vars | Medium | Gate-based QC |
| Annealing | ≤ 1000 vars | High | D-Wave |
| Hybrid | Any | High | Both |

## Selection Guidelines

**Choose QAOA**:
- General quantum computer access
- Smaller problem sizes
- Research and experimentation

**Choose Annealing**:
- D-Wave access available
- Larger problem sizes
- Production applications

**Choose Hybrid**:
- Real-world constraints
- Large candidate pools
- Need for reliability