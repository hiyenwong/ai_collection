# Tensor Network Basics

## Matrix Product State (MPS)

### Structure
```
|ψ⟩ = Σ_{i1,...,in} A^{[1]}_{i1} A^{[2]}_{i2} ... A^{[n]}_{in} |i1...in⟩
```

Each A^{[k]} is a rank-3 tensor:
- Left bond dimension: χ_{k-1}
- Right bond dimension: χ_k
- Physical dimension: d (typically d=2 for qubits)

### Canonical Form
- Left-canonical: Σ_{i_k,α} A_{α,i_k,β}^* A_{α,i_k,β'} = δ_{β,β'}
- Right-canonical: Σ_{i_k,β} B_{α,i_k,β}^* B_{α',i_k,β} = δ_{α,α'}
- Mixed-canonical: Combination for efficient operations

### Entanglement Bound
Maximum bond dimension χ:
```
χ ≤ min(d^{k}, d^{n-k})
```

For ground states: χ grows exponentially with entanglement entropy S:
```
χ ~ exp(S)
```

### Operations

**Apply local operator O_k:**
```
A^{[k]}_{i_k} → Σ_{j_k} O_{i_k,j_k} A^{[k]}_{j_k}
```

**Apply two-site operator O_{k,k+1}:**
1. Contract bond between sites k and k+1
2. Apply operator on combined tensor
3. Split via SVD, truncate to χ

## Projected Entangled Pair State (PEPS)

### Structure (2D)
```
|ψ⟩ = Σ_{i_{mn}} A^{[mn]}_{i_{mn}} |i_{mn}⟩
```

Each A^{[mn]} connects to 4 neighbors (up, down, left, right).

### Bond Dimensions
- Typical: χ ~ 10-20 for practical simulations
- Exponential scaling with system size

### Challenges
- Contraction complexity: O(χ^{10}) for naive approach
- Boundary contraction methods needed
- Corner transfer matrix renormalization group

## Tree Tensor Networks

### Structure
Hierarchical tensor network with tree topology:
- Root at top
- Leaves at physical indices
- Branches connect nodes

### Advantages
- Efficient contraction: O(χ^3 log n)
- Natural for certain Hamiltonians
- Good for adaptive basis selection

## Practical Tips

1. **Bond dimension selection**: Start with χ=10, increase until convergence
2. **SVD truncation**: Use singular value spectrum to monitor entanglement
3. **Parallelization**: Contract independent tensors simultaneously
4. **Memory optimization**: Store tensors in compressed format

## Software Libraries

- **ITensor**: Julia tensor network library
- **QuTiP**: Python quantum simulation (includes MPS)
- **TenPy**: Python tensor network for physics
- **TensorFlow/PyTorch**: General tensor operations with batching