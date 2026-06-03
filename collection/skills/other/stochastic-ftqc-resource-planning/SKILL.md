---
name: stochastic-ftqc-resource-planning
description: "Stochastic-aware resource planning methodology for fault-tolerant quantum computing. Quantifies non-determinism in magic state production for optimal factory allocation. Reduces space-time volume by up to 27% compared to deterministic analysis. Activation: stochastic quantum planning, fault tolerant resource estimation, magic state provisioning, FTQC factory allocation."
category: quantum
---

# Stochastic FTQC Resource Planning

## Description

This methodology addresses the dual effect of non-determinism in fault-tolerant quantum computation (FTQC). Unlike deterministic analysis that provisions for worst-case peak demand (wasting resources) or average demand (increasing execution time), stochastic-aware analysis captures both the **price** (inflated execution time) and **payoff** (deflated peak resource demand) of non-deterministic magic state production.

**arXiv**: 2605.07983v1
**Authors**: Aditi Awasthi, Sayam Sethi, Sahil Khan, Gokul Subramanian Ravi, Jonathan Mark Baker

## Activation Keywords

- stochastic quantum planning
- fault tolerant resource estimation
- magic state provisioning
- FTQC factory allocation
- quantum resource optimization
- 随机量子资源规划
- 容错量子计算规划

## Core Methodology

### The Price-Payoff Duality

Non-determinism in magic state production has a dual effect that deterministic models cannot capture:

1. **Price**: Inflates total execution time due to random production delays
2. **Payoff**: Deflates peak per-cycle resource demand (demand smoothing)

This duality shifts the space-time-optimal provisioning point: fewer factories are needed to minimize space-time volume than deterministic analysis predicts.

### Key Results

| Finding | Impact |
|---------|--------|
| Stochastic-aware provisioning | Reduces space-time volume by up to **27%** vs deterministic optimum |
| Factory count reduction | Requires up to **30% fewer** factories than deterministic analysis |
| Distillation architectures | Most benefited by demand smoothing effect |

## Simulation Framework

### Components

1. **Circuit Scheduler**: Manages quantum gate execution order
2. **Magic State Production Models**: Stochastic models for different preparation mechanisms:
   - **Distillation**: Multi-round purification (highly variable)
   - **Cultivation**: Seeded growth (moderate variability)
   - **Rz Synthesis**: Direct synthesis (lower variability)
3. **Teleportation Engine**: Injects magic states into the circuit

### Implementation

```python
class StochasticMagicStateProducer:
    def __init__(self, mechanism, num_factories):
        self.mechanism = mechanism  # 'distillation', 'cultivation', 'rz_synthesis'
        self.num_factories = num_factories
        self.production_times = self._model_production_distribution()
    
    def _model_production_distribution(self):
        if self.mechanism == 'distillation':
            # Multi-round distillation: highly variable
            return self._distillation_distribution()
        elif self.mechanism == 'cultivation':
            # Seeded growth: moderate variability
            return self._cultivation_distribution()
        else:
            # Direct synthesis: lower variability
            return self._synthesis_distribution()
    
    def produce(self, num_states):
        """Sample production times for requested magic states."""
        return [random.choice(self.production_times) for _ in range(num_states)]

class FTCResourcePlanner:
    def __init__(self, circuit, production_model):
        self.circuit = circuit
        self.producer = production_model
    
    def simulate(self, num_factories):
        """Run stochastic simulation with given factory count."""
        self.producer.num_factories = num_factories
        total_time = 0
        peak_demand = 0
        
        for cycle in self.circuit.cycles():
            # Schedule gates
            ready_gates = cycle.get_ready_gates()
            
            # Request magic states for non-Clifford gates
            magic_requests = [g for g in ready_gates if g.requires_magic_state()]
            
            # Produce with stochastic timing
            production_times = self.producer.produce(len(magic_requests))
            
            # Track metrics
            cycle_time = max(production_times) if production_times else 0
            total_time += cycle_time
            peak_demand = max(peak_demand, len(magic_requests))
        
        return {
            'total_time': total_time,
            'peak_demand': peak_demand,
            'space_time_volume': total_time * num_factories
        }
    
    def find_optimal_factories(self, factory_range):
        """Find the factory count that minimizes space-time volume."""
        results = []
        for n in factory_range:
            # Run multiple stochastic trials
            volumes = [self.simulate(n)['space_time_volume'] for _ in range(100)]
            results.append({
                'factories': n,
                'mean_volume': mean(volumes),
                'std_volume': std(volumes)
            })
        return min(results, key=lambda r: r['mean_volume'])
```

## Design-Space Analysis

### Preparation Mechanisms

| Mechanism | Variability | Optimal Factories | Space-Time Impact |
|-----------|------------|-------------------|-------------------|
| Distillation | High | Fewer than deterministic | -27% volume |
| Cultivation | Moderate | Near deterministic | -15% volume |
| Rz Synthesis | Low | Near deterministic | -5% volume |

### Overload Policies

When demand exceeds factory capacity:

1. **Queue**: Wait for next available factory (increases latency)
2. **Drop**: Skip non-critical operations (reduces fidelity)
3. **Throttle**: Reduce parallelism (moderate impact)

### Capacity Scaling

The most effective optimization:
- Doubling capacity dramatically reduces miss rates
- More effective than queue management or admission control

## Best Practices

### 1. Replace Deterministic Heuristics

Static resource estimation systematically mis-characterizes the cost of fault-tolerant execution. Use stochastic-aware analysis as the standard methodology.

### 2. Right-Size Factory Allocation

The stochastic-optimal point typically requires fewer factories than the deterministic-optimal point. Don't over-provision based on worst-case analysis.

### 3. Characterize Preparation Mechanism Variability

Different preparation mechanisms have different variability profiles. Characterize each mechanism's production time distribution before optimization.

### 4. Benchmark Across Multiple Configurations

Test across:
- Different factory counts
- Different preparation mechanisms
- Different circuit benchmarks
- Different noise models

## Error Handling

### Insufficient Sampling
- Run at least 100 trials per configuration
- Check convergence of mean space-time volume
- Increase trials for high-variance mechanisms

### Production Model Mismatch
- Validate simulation against hardware measurements
- Update production distributions based on actual device performance
- Account for device-specific variability

## Related Papers

- DART-Q (2605.09142): Real-time QLDPC decoding under deadlines
- Lower overhead FT building blocks (2605.12385): Hardware-agnostic FTQC optimization

## Tools Used

- exec: Run resource planning simulations
- read: Load circuit descriptions, production models
- write: Save simulation results, resource plans

## References

- Paper: "Price and Payoff: Non-Determinism in Fault Tolerant Quantum Computation" (arXiv:2605.07983v1)
