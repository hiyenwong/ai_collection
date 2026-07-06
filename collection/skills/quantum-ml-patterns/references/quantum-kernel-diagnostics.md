# Quantum Kernel Diagnostics (2026-06-02 Update)

## Hamming Quantum Kernel (arXiv: 2605.31449)

**Problem**: Fidelity quantum kernel $K(x,x') = |\langle\psi(x)|\psi(x')\rangle|^2$ suffers from exponential concentration as system size increases.

**Solution**: Hamming kernel uses full measurement statistics instead of single fidelity value.

### Implementation
```python
def hamming_kernel(measurements_x, measurements_x_prime):
    """Hamming similarity of measurement bitstring distributions."""
    matching = count_hamming_similar(measurements_x, measurements_x_prime)
    return matching / (len(measurements_x) * len(measurements_x_prime))
```

### Performance
- Outperforms fidelity kernel at ≥15 qubits
- Outperforms classical Gaussian kernel on synthetic quantum data
- Scales to 27 qubits (simulation)
- Zero additional quantum resources needed

## Spectral Entropy Diagnostic (arXiv: 2605.30952)

**Core quantity**: Normalized spectral entropy $S(K)/\log n = -\frac{1}{\log n}\sum_i \lambda_i \log \lambda_i$

### Diagnostic rules
- **High entropy** → optimal for smooth targets
- **Low entropy** → optimal for band-limited quantum data
- All kernel families (hardware-efficient, matchgate, IQP, RBF/Matern) collapse onto identical $S/\log n$ curves
- Verified on IBM Heron: median error 3.2% across 24 configs at n_q=4

### When to apply
- Before expensive quantum circuit execution
- Diagnosing why quantum kernel underperforms classical alternatives
- Selecting kernel family based on target function characteristics
