# Quantum Error Correction Methods

## Description
Quantum Error Correction (QEC) methodologies covering syndrome resampling, affine subcode ensemble decoding, FPGA-based neural network decoding, and distributed bivariate bicycle codes. Use when researching, implementing, or analyzing QEC decoding strategies, logical error rate optimization, fault-tolerant quantum computing architectures, or syndrome-based error mitigation.

## Activation Keywords
- quantum error correction
- QEC decoding
- syndrome resampling
- affine subcode ensemble decoding
- neural network decoder
- bivariate bicycle codes
- surface code decoding
- logical error rate optimization
- fault-tolerant quantum computing
- QEC threshold improvement
- 量子纠错
- syndrome decoding
- BP+OSD decoding
- distributed quantum error correction
- degenerate solution search

## Core Methodologies

### 1. Syndrome Resampling for Threshold Enhancement
**Paper**: Colmenarez et al. (2605.06101)

**Key Insight**: Biasing syndrome averages toward high-probability syndromes increases logical fidelities without hardware modifications or decoder changes.

**Algorithm**:
1. Collect syndrome statistics from QEC cycles
2. Compute syndrome probability distribution P(s)
3. Resample syndromes according to P(s)^α where α > 1
4. Apply maximum likelihood decoding (MLD) on resampled syndromes
5. The α parameter creates a family of optimal thresholds linked to Rényi coherent information phase transitions

**Results**:
- Reduces logical error rates by up to 4 orders of magnitude
- Decoder-agnostic: works with any QEC decoder
- Effective from finite syndrome data
- Can combine with decoding-based post-selection
- Applied to existing experimental data: 2 orders of magnitude reduction without additional measurements

**Implementation**:
```python
import numpy as np

def syndrome_resampling(syndromes, alpha=2.0, n_samples=1000):
    """Resample syndromes biased toward high-probability ones."""
    unique, counts = np.unique(syndromes, axis=0, return_counts=True)
    probs = counts / counts.sum()
    biased_probs = probs ** alpha
    biased_probs /= biased_probs.sum()
    indices = np.random.choice(len(unique), size=n_samples, p=biased_probs)
    return unique[indices]
```

### 2. Affine Subcode Ensemble Decoding
**Paper**: Wursthorn et al. (2605.06547)

**Key Insight**: Appending linearly independent rows to stabilizer code check matrices reduces search space for degenerate solutions, improving BP decoding convergence.

**Algorithm**:
1. Start with parity check matrix H of stabilizer code
2. Generate overcomplete matrices by appending linearly independent rows
3. Create multiple affine subcode decoding paths
4. Run classical BP decoding on each path
5. Combine results to find optimal degenerate solution

**Results**:
- Improved convergence for toric and generalized bicycle codes
- Reduced logical error rate vs. standard BP decoding
- Specifically addresses degeneracy impairment in qLDPC codes

**Implementation Pattern**:
```python
def affine_subcode_decode(syndromes, H, n_paths=8):
    """Ensemble decoding using affine subcode paths."""
    results = []
    for _ in range(n_paths):
        H_ext = extend_with_independent_rows(H)
        decoded = belief_propagation(syndromes, H_ext)
        results.append(decoded)
    return select_best_degenerate_solution(results, syndromes, H)
```

### 3. FPGA-based Neural Network Decoder
**Paper**: Yang et al. (2605.04892)

**Key Architecture**:
- Neural network decoder on FPGA for surface code
- Deterministic closed-loop latency: 550 ns (124 ns NN decoding)
- QEC cycle: 1.25 μs
- Distance-3 surface code on superconducting processor
- Supports mid-circuit feedback for non-Clifford operations

**Design Considerations**:
- Throughput must exceed syndrome generation rate
- Latency must be < QEC cycle time to prevent error accumulation
- Real-time performance matches offline decoding
- Handles varying error conditions robustly

### 4. Distributed Bivariate Bicycle Codes
**Paper**: Chandra et al. (2605.04663)

**Key Architecture**:
- BB code [[144,12,12]] partitioned across modular processors
- Star network interconnect via shared Bell pairs
- All-to-all internal connectivity (trapped ion/neutral atom)
- Inter-processor gates mediated by entanglement

**Scaling Analysis**:
- Partition across 4, 6, or 12 processors
- Vary nonlocal operation noise scaling factor
- Use BP+OSD decoding with Monte Carlo simulation
- Extended BB code ansatz for distributed setting

## QEC Decoder Comparison

| Decoder Type | Latency | Hardware | Threshold | Scalability |
|-------------|---------|----------|-----------|-------------|
| Syndrome Resampling | Software-only | Any | ↑↑↑ | High |
| Affine Subcode Ensemble | Software-only | Any | ↑↑ | High |
| FPGA Neural Network | 550 ns | FPGA | ↑↑ | Medium |
| BP+OSD (Standard) | Software | Any | Baseline | High |
| Distributed BB | Depends on interconnect | Modular | Competitive | High |

## Implementation Workflow

### Step 1: Syndrome Collection
```python
def collect_syndromes(qec_cycles, measurement_results):
    """Extract syndrome history from QEC cycles."""
    syndromes = []
    for cycle in qec_cycles:
        syndrome = compute_syndrome(measurement_results[cycle])
        syndromes.append(syndrome)
    return np.array(syndromes)
```

### Step 2: Probability Estimation
```python
def estimate_syndrome_distribution(syndromes):
    """Estimate P(s) from syndrome history."""
    unique, counts = np.unique(syndromes, axis=0, return_counts=True)
    return unique, counts / counts.sum()
```

### Step 3: Apply Enhancement Method
Choose based on constraints:
- **No hardware changes needed**: Syndrome Resampling (α=2-4)
- **qLDPC codes with degeneracy**: Affine Subcode Ensemble
- **Real-time requirement**: FPGA Neural Network
- **Modular architecture**: Distributed BB Codes

### Step 4: Evaluate Performance
```python
def evaluate_qec_improvement(logical_errors_before, logical_errors_after):
    """Compute improvement metrics."""
    reduction = logical_errors_before / logical_errors_after
    print(f"Logical error rate reduction: {reduction:.1f}x")
    return reduction
```

## Key Parameters

### Syndrome Resampling
- **α (power parameter)**: Controls bias strength (typically 2-4)
- **n_samples**: Number of resampled syndromes (≥1000 for stable results)
- **Data requirement**: Finite syndrome statistics sufficient

### Affine Subcode Decoding
- **n_paths**: Number of decoding paths (typically 4-16)
- **Row extension**: Number of independent rows to append
- **Overcompleteness**: Balance between search space reduction and computational cost

### FPGA NN Decoder
- **Latency budget**: < QEC cycle time
- **Network size**: Trade-off between accuracy and latency
- **Feedback path**: Must include Pauli-frame update for non-Clifford operations

## Error Handling

### Degeneracy Issues
- If BP fails to converge: Apply affine subcode ensemble
- If multiple degenerate solutions: Use syndrome resampling to bias toward likely syndromes

### Hardware Constraints
- If latency too high for real-time: Use syndrome resampling (software-only)
- If limited qubit connectivity: Use distributed BB code architecture

### Data Limitations
- If syndrome statistics insufficient: Combine with post-selection
- If finite data regime: Use resampling with conservative α values

## Best Practices

1. **Start with syndrome resampling**: Decoder-agnostic, no hardware changes, proven results
2. **Combine methods**: Syndrome resampling + affine subcode ensemble for maximum improvement
3. **Monitor Rényi coherent information**: Track phase transitions to optimize α parameter
4. **Validate on surface codes first**: Well-understood benchmark before moving to qLDPC/BB codes
5. **Consider architecture constraints**: Match decoding method to hardware capabilities

## Resources
- Paper 1: https://arxiv.org/abs/2605.06547 (Affine Subcode Ensemble Decoding)
- Paper 2: https://arxiv.org/abs/2605.06101 (Syndrome Resampling)
- Paper 3: https://arxiv.org/abs/2605.04892 (FPGA Neural Network Decoder)
- Paper 4: https://arxiv.org/abs/2605.04663 (Distributed BB Codes)
- Paper 5: https://arxiv.org/abs/2605.04582 (Post-Quantum Cryptographic Limitations)

## Related Codes
- Surface codes (distance-3 demonstrated)
- Toric codes
- Generalized bicycle codes
- Bivariate bicycle (BB) codes [[144,12,12]]
- Quantum LDPC codes

## Related Methods
- Belief Propagation (BP)
- Ordered Statistic Decoding (OSD)
- Maximum Likelihood Decoding (MLD)
- Rényi Coherent Information (RCI)
- Pauli-frame updating