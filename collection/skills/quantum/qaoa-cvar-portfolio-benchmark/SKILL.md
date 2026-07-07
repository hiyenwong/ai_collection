# QAOA CVaR Portfolio Benchmark

## Description
Hardware benchmarking methodology for comparing quantum portfolio optimization algorithms (HE-VQNN vs WS-QAOA) on NISQ devices, focusing on CVaR (Conditional Value at Risk) portfolio optimization and the expressibility-coherence trade-off.

## Source
Paper: "Benchmarking Quantum Algorithmic Resilience for CVaR Portfolio Optimization: The Expressibility-Coherence Trade-off"
Authors: Prashik N. Somkuwar, K. Srinivasan, G. Raghavan
arXiv: 2606.07727

## Activation
arxiv:2606.07727, quantum portfolio optimization, CVaR, QAOA, HE-VQNN, quantum finance, NISQ benchmark, expressibility-coherence trade-off, SWAP tax, IBM quantum processor

## Usage Scenarios
- Benchmarking quantum vs classical portfolio optimization algorithms
- Evaluating NISQ device suitability for financial optimization
- Analyzing the expressibility-coherence trade-off in hybrid quantum-classical models
- Implementing CVaR-based portfolio optimization on quantum hardware
- Comparing HE-VQNN vs WS-QAOA approaches for constrained optimization

## Core Patterns

### 1. Classical-Quantum Hybrid Proxy Matrix Pattern
```python
# Bypass CVaR auxiliary qubit bottleneck using classical proxy matrix
# Instead of encoding all auxiliary qubits on quantum hardware,
# compute tail-risk correlations classically and use as proxy

def create_cvax_proxy_matrix(covariance_matrix, cvar_alpha=0.05):
    """Create classical proxy for CVaR computation on quantum hardware.
    
    Instead of encoding CVaR auxiliary variables (which require extra qubits),
    compute tail-risk weighted covariance classically and use as input to QPU.
    """
    # Compute tail scenarios
    sorted_returns = np.sort(returns)
    tail_idx = int(len(sorted_returns) * cvar_alpha)
    tail_scenarios = sorted_returns[:tail_idx]
    
    # Compute tail-risk weighted covariance
    tail_cov = np.cov(portfolio_returns[tail_scenarios].T)
    
    # Use as proxy matrix for quantum encoding
    return tail_cov
```

### 2. SWAP Tax Quantification Methodology
```python
def quantify_swap_tax(circuit_depth, qubit_map, hardware_topology):
    """Quantify SWAP gate overhead for routing quantum circuits on limited topology.
    
    The 'SWAP tax' is the performance degradation from additional SWAP gates
    needed to route non-adjacent qubits on hardware with limited connectivity.
    """
    # Count required SWAP operations for target circuit on given topology
    swap_count = count_required_swaps(circuit, hardware_topology)
    
    # Estimate decoherence impact
    additional_depth = swap_count * swap_gate_depth
    total_depth = original_depth + additional_depth
    
    # Predict fidelity degradation
    predicted_fidelity = base_fidelity ** total_depth
    
    return {
        'swap_count': swap_count,
        'depth_overhead': additional_depth / original_depth,
        'predicted_fidelity': predicted_fidelity
    }
```

### 3. Expressibility-Coherence Trade-off Analysis
```python
def analyze_expressibility_coherence_tradeoff(algorithm, hardware_specs):
    """Analyze the trade-off between algorithmic expressibility and hardware coherence.
    
    Key insight: WS-QAOA provides exact mathematical mapping but suffers
    catastrophic decoherence from nonlocal gate overhead.
    HE-VQNN preserves coherence but lacks expressibility for dense correlations.
    """
    metrics = {
        'expressibility': compute_expressibility(algorithm.circuit),
        'coherence_budget': hardware_specs['t1_time'] * hardware_specs['gate_fidelity'],
        'nonlocal_gate_overhead': count_nonlocal_gates(algorithm.circuit, hardware_specs['topology']),
        'predicted_success': predict_algorithm_success(algorithm, hardware_specs)
    }
    return metrics
```

## Implementation Guidelines

### Hardware-Aware Circuit Design
1. **Map asset count to qubit budget**: For N assets on heavy hex topology,
   maximum practical N ≈ 16-20 due to connectivity constraints
2. **Use warm-start QAOA** for exact theoretical mapping when qubit budget allows
3. **Use HE-VQNN** when circuit depth would exceed coherence time
4. **Hybrid proxy matrices** can extend practical asset count by offloading
   CVaR auxiliary variables to classical computation

### Benchmarking Protocol
1. **Define objective**: Mean Variance + CVaR hybrid objective
2. **Select benchmark assets**: Use index constituents (e.g., NIFTY 50, S&P 500)
3. **Map to QUBO**: Convert portfolio constraints to quadratic binary optimization
4. **Execute on hardware**: Run on target quantum processor (IBM, Rigetti, etc.)
5. **Compare with classical baselines**: Gurobi, simulated annealing, classical QNN
6. **Report SWAP tax**: Quantify routing overhead vs coherence budget

### Key Metrics to Report
- Algorithmic expressibility (Hilbert space coverage)
- Hardware coherence consumption (circuit depth / T1 time)
- SWAP gate overhead percentage
- Final portfolio quality (Sharpe ratio, CVaR, diversification)
- Wall-clock execution time
- Classical baseline comparison

## Pitfalls
- **Catastrophic decoherence**: WS-QAOA may produce meaningless results on NISQ
  hardware due to exponential nonlocal gate overhead
- **Expressibility gap**: HE-VQNN may miss important tail-risk correlations
  in dense asset covariance matrices
- **Topology mismatch**: Heavy hex topology significantly limits which asset
  pairs can be directly coupled without SWAP overhead
- **No quantum advantage**: Current NISQ devices cannot outperform classical
  solvers for this problem class; focus on methodology development

## Verification
1. Reproduce HE-VQNN vs WS-QAOA comparison on IBM quantum processor
2. Quantify SWAP tax for target asset universe size
3. Compare quantum results with classical Gurobi baseline
4. Validate CVaR proxy matrix approximation accuracy
