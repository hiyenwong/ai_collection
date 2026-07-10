# GSC-QEMit: Telemetry-Driven Adaptive Quantum Error Mitigation

**arXiv**: 2604.24551
**Authors**: Steven Szachara, Sheeraja Rajakrishnan, Dylan Jay Van Allen, Jason Pollack, Travis Desell
**Category**: quant-ph, cs.LG

## Architecture

Three coupled modules for adaptive QEM:

### (G) Growing Hierarchical Context Module
- Builds hierarchical representation of device noise telemetry
- Adaptive context windows based on noise correlation timescales
- Captures short-term fluctuations + long-term drift patterns
- Cross-correlates noise across qubits for shared noise source identification

### (S) State Forecast Module
- Time-series prediction of future noise states
- Anticipates noise regime transitions
- Proactive (not reactive) mitigation selection
- Confidence intervals for forecast uncertainty

### (C) Contextual Bandit Controller
- Multi-armed bandit for mitigation strategy selection
- Balances exploration vs exploitation
- Maps forecast state + context → bandit context vector
- Approaches oracle performance

## Mitigation Strategy Spectrum

| Level | Strategy | Overhead | Use Case |
|-------|----------|----------|----------|
| Light | ZNE (low-order) | Low | Stable noise |
| Medium | PEC | Medium | Moderate drift |
| Heavy | Full QEM suite | High | Severe noise, critical runs |

## Implementation Notes
- Most effective for iterative algorithms (VQA) where per-iteration adjustment matters
- Requires telemetry data (T1, T2, gate fidelities, readout errors)
- Bandit needs sufficient exploration phase before converging
- Forecast accuracy degrades with longer horizons
