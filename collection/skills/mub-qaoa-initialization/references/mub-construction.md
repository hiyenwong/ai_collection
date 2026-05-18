# MUB Construction Details

## Complete MUB Construction

### Single Qubit (d=2)
Three MUBs corresponding to X, Y, Z Pauli bases:
- Z basis: |0⟩, |1⟩
- X basis: |+⟩, |-⟩
- Y basis: |+i⟩, |-i⟩

### Prime Dimension d=p
For prime p, construct using discrete Fourier transform:

```
|ψ_j^k⟩ = (1/√p) Σ_l ω^(jl+kl²) |l⟩
```

where ω = e^(2πi/p), j=0,...,p-1, k=0,...,p-1

### Prime Power Dimension d=p^n
Tensor product of prime constructions.

## Gaussian Correlation Inequality

The proof of MUB optimality uses a centered-convex Gaussian correlation inequality
to show that the independent-block case (complete MUBs) is stochastically extremal.

## Bloch Sphere Argument (d=2)
For qubits, complete MUBs are globally optimal among arbitrary six-state ensembles
by a Bloch-sphere/octahedron mean-width argument.
