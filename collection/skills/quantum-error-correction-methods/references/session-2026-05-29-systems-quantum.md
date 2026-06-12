# 2026-05-29 Session Notes: Systems Engineering × Quantum

## Dynamic Entanglement Packet Scheduling (arxiv:2605.28795)

### Static vs Dynamic Scheduler Comparison
| Metric | Static TDMA/EDF | Dynamic Online |
|--------|----------------|----------------|
| Completion Time | Higher | Lower |
| Completion Ratio | Lower | Higher |
| Throughput | Lower | Higher |
| Overload Behavior | Cascading failure | Graceful degradation |
| Adaptivity | Periodic recomputation | Per-slot real-time |

### Decision State Machine
```
Request Arrived → Evaluate Feasibility (time + resources)
  ├── Feasible → Schedule → Execute
  │               ├── Success → Complete
  │               └── Failure → Retry (if deadline permits)
  │                              └── Retry limit reached → Drop
  └── Infeasible → Defer (if deadline allows)
                      └── Still infeasible next slot → Drop
```

### Key Design Parameters
- Time slot duration: constrained by physical layer (entanglement generation time)
- Deadline enforcement strictness
- Priority assignment policy
- Retry limit per request
- Network heterogeneity: different links have different success probabilities

## VarEFTQC: Learning Logical Operations (arxiv:2605.28162)

### Pipeline
```
Encoding Circuit → Ansatz Selection → Loss Construction → Optimization
  ↓                    ↓                    ↓                  ↓
Gate parameterization  Fidelity +         Gradient-based
                       structural         or gradient-free
                       constraints        optimization
```

### Loss Components
- Fidelity loss: Does the operation implement the correct logical transformation?
- Structural loss: Is the circuit transversal? Is depth below threshold?
- Noise-aware loss: Does the operation work under the target noise model?

### Gate Sets Supported
- Transversal IQP-type families
- Low-depth universal gate sets
- Hardware-native gate sets (ion trap, superconducting)

## Quantum Annealing Benchmark for Control QUBOs (arxiv:2605.27670)

### Results Summary (Greenhouse Heater Scheduling)
| Solver | H=10 | H=12 | H=14 | H=24 |
|--------|------|------|------|------|
| Classical SA | Near-optimal | Near-optimal | Near-optimal | Near-optimal |
| PISQA | Near-optimal | Near-optimal | Near-optimal | Near-optimal |
| D-Wave Leap Hybrid | - | - | - | Less reliable |
| D-Wave QPU | 5/10 exact | 5/10 exact | 2/10 exact | 0/10 exact |

### Key Takeaway
No quantum advantage for structured control QUBOs. Classical baselines more reliable.
Provides reproducible, physically decoded benchmark for future comparisons.
