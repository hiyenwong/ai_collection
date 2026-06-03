---
name: quantum-finance-pipeline
description: Hybrid quantum-classical financial analysis pipeline patterns combining VQC forecasting, QUBO optimization, penalty-free quantum annealing, and post-quantum security. Use when building end-to-end quantum financial systems for portfolio optimization, risk management, option pricing, or algorithmic trading. Covers HQFS pipeline, penalty-free annealing, qutrit neural networks, and PDE-based quantum option pricing.
---

# Quantum Finance Pipeline Patterns

End-to-end hybrid quantum-classical patterns for financial analysis combining prediction, optimization, and security layers.

## Key Architecture Patterns

### Pattern 1: HQFS Integrated Pipeline
Variational Quantum Circuit (VQC) forecasting → QUBO annealing optimization → Post-quantum signing.

```python
from qiskit import QuantumCircuit
from dimod import BinaryQuadraticModel

class HQFSPipeline:
    def __init__(self, n_qubits=4):
        self.vqc = VQCForecaster(n_qubits=n_qubits)
        self.qubo = QUBOOptimizer()
        self.pqc = PostQuantumSigner()
    
    def run(self, market_data):
        # 1. VQC forecasting - quantum feature maps for market prediction
        forecasts = self.vqc.predict(market_data)
        
        # 2. Convert forecasts to QUBO objective
        bqm = self._forecasts_to_qubo(forecasts, market_data)
        
        # 3. QUBO annealing with real market constraints
        solution = self.qubo.solve(bqm, constraints={
            'cardinality': 10,
            'budget': 1.0
        })
        
        # 4. Post-quantum signing for audit trail
        signed = self.pqc.sign(solution)
        return signed
```

**When to use**: Financial risk systems requiring end-to-end quantum advantage with audit-ready outputs.

### Pattern 2: Penalty-Free Quantum Annealing
Standard penalty-encoded QUBO fails on D-Wave hardware due to dense rank-one cardinality terms. Use penalty-free formulation instead.

**Problem**: Cardinality penalty `k*(Σx_i - C)²` creates all-ones matrix, making logical interaction graph complete → chain breaks reach 83%+ on Pegasus/Zephyr topologies.

**Solution**: Use constraint-native LeapHybridCQM or reformulate to avoid dense penalty terms.

```python
import dimod
from dwave.system import LeapHybridCQMSampler

def penalty_free_portfolio(cov_matrix, expected_returns, n_assets, k_assets):
    """Penalty-free portfolio optimization using CQM instead of QUBO."""
    x = dimod.Binary('x', n_assets)  # Binary variables
    
    cqm = dimod.ConstrainedQuadraticModel()
    
    # Objective: minimize risk (variance) - maximize return
    objective = x @ cov_matrix @ x - 2 * expected_returns @ x
    cqm.set_objective(objective)
    
    # Budget constraint (hard constraint, not penalty)
    cqm.add_constraint(sum(x) <= 1, label='budget')
    
    # Cardinality constraint (hard constraint, not penalty)
    cqm.add_constraint(sum(x) == k_assets, label='cardinality')
    
    sampler = LeapHybridCQMSampler()
    return sampler.sample_cqm(cqm)
```

**Key insight**: D-Wave hybrid QPU access time is only 0.7% of total runtime. Classical post-processing dominates. Use quantum primarily for solution space exploration, not final optimization.

### Pattern 3: Qutrit Neural Networks for Forecasting
Quantum Qutrit-based Neural Networks (QQTNs) outperform both ANN and Quantum Qubit Neural Networks (QQBNs) for financial time series.

**Advantages**:
- 3-state qutrits encode more information per quantum unit
- Faster training convergence vs qubit-based approaches
- Better generalization on noisy financial data

```python
# Conceptual qutrit encoding for financial features
def encode_features_qutrit(features):
    """Encode financial features into qutrit states (|0⟩, |1⟩, |2⟩)."""
    # |0⟩ = bearish signal
    # |1⟩ = neutral signal  
    # |2⟩ = bullish signal
    return [classify_signal(f) for f in features]
```

### Pattern 4: PDE-Based Quantum Option Pricing
End-to-end quantum PDE framework for multi-asset option pricing under local/stochastic volatility.

```python
def quantum_option_price(S, K, T, r, sigma, n_qubits):
    """Quantum algorithm for multi-asset option pricing via PDE discretization."""
    # 1. Discretize Black-Scholes PDE
    # 2. Encode into quantum state via amplitude encoding
    # 3. Apply quantum linear system algorithm (HHL variant)
    # 4. Measure expectation value for option price
    pass
```

## Implementation Checklist

- [ ] Use CQM (Constrained Quadratic Model) over QUBO for portfolio constraints
- [ ] Implement VQC with parameterized quantum circuits for feature extraction
- [ ] Add post-quantum cryptography (PQC) signatures for audit compliance
- [ ] Benchmark quantum contribution vs classical post-processing time
- [ ] Use qutrit encoding for multi-class financial signals
- [ ] Validate against classical baselines (Gurobi, CPLEX)

## Pitfalls

1. **Dense penalty matrices**: Cardinality penalties create all-ones interactions → embedding failure on quantum hardware
2. **Quantum overhead**: Current hybrid systems spend 99.3% time on classical processing
3. **Chain breaks**: >80% chain break rates on N>24 assets with naive QUBO formulation
4. **Data loading**: Quantum advantage assumes efficient state preparation; naive loading eliminates speedup

## Activation Keywords

quantum finance, portfolio optimization, quantum annealing, QUBO, VQC forecasting, financial quantum computing, HQFS pipeline, qutrit neural network, quantum option pricing, post-quantum finance
