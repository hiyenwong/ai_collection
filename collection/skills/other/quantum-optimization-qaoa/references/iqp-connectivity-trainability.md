# IQP Circuit Connectivity-Trainability Trade-off (arXiv: 2606.24264, June 2026)

## Paper Summary
Nguyen reveals a fundamental trade-off: IQP circuit connectivity determines optimization performance but inversely affects trainability.

## Key Findings

### Trade-off
| Connectivity | Optimization | Trainability |
|---|---|---|
| Low (local) | Poor (high energy) | Good (large gradients) |
| Medium | Balanced | Balanced |
| High (all-to-all) | Good (low energy) | Poor (barren plateaus) |

### Design Principle
Optimal connectivity should **match the Hamiltonian's interaction locality**, not exceed it.

### Training Strategy
Progressive connectivity: start low (easy gradients), gradually increase to reach optimal solutions.

## Activation
IQP circuit, connectivity trainability, Hamiltonian optimization, barren plateau IQP
