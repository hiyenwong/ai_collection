---
name: adaptive-bistable-qubit-control
description: >
  Adaptive feedback control methodology for operating bistable qubits in solid-state
  quantum processors. Uses 1-bit feedback protocol with FPGA-based classical controller
  to estimate and compensate for TLS-induced frequency shifts from single-shot measurements.
  Based on arXiv:2605.03187. Use when: designing adaptive quantum control systems,
  mitigating TLS defects in qubits, implementing real-time FPGA feedback for quantum
  processors, or building fault-tolerant control for large qubit arrays.
  Activation: bistable qubit, TLS mitigation, 1-bit feedback, adaptive qubit control,
  FPGA quantum control, frequency estimation, Ramsey beating suppression, qubit instability.
---

# Adaptive Bistable Qubit Control

## Core Concept

Parasitic two-level-system (TLS) defects in solid-state quantum processors cause
discrete, stochastic frequency shifts, making qubits **bistable** — switching between
two frequency states. Operating such qubits requires adaptive control that tracks
and compensates for these shifts in real time.

## Key Insight: 1-Bit Feedback Protocol

The minimal information needed to track a bistable qubit's frequency state can be
extracted from a **single single-shot measurement** — reaching the information limit
set by the qubit's intrinsic entropy. This enables fast, high-fidelity adaptive control
without extensive tomography or repeated measurements.

## Protocol Architecture

### Step 1: Single-Shot Frequency Estimation

```
Measurement → Binary outcome (|0⟩ or |1⟩)
             → Bayesian update of frequency state probability
             → Estimate most likely frequency configuration
```

The protocol maintains a belief state over the two possible frequency configurations:
- **State A**: Qubit at nominal frequency f₀
- **State B**: Qubit shifted by Δf due to TLS interaction

After each single-shot measurement:
```
P(state B | measurement) ∝ P(measurement | state B) × P(state B)
```

### Step 2: Adaptive Compensation

Once the frequency state is estimated:
1. **Adjust control pulse frequency** to match the estimated qubit frequency
2. **Apply phase correction** to compensate for accumulated phase error
3. **Proceed with gate operations** at the corrected frequency

### Step 3: FPGA Implementation

The protocol is designed for real-time execution on an FPGA:

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│ Qubit Readout│───▶│ 1-Bit State  │───▶│ Frequency   │
│ (single-shot)│    │ Estimator    │    │ Compensator │
└─────────────┘    └──────────────┘    └─────────────┘
                                            │
                                    ┌───────▼───────┐
                                    │ Gate Sequence │
                                    │ (corrected)   │
                                    └───────────────┘
```

Key parameters from experimental demonstration:
- **Estimation bandwidth**: ~136 kHz
- **Error reduction**: ~77%
- **Gate fidelity**: maintained above threshold despite TLS-induced shifts

## Application Scenarios

### 1. TLS-Induced Ramsey Beating Suppression

When a TLS defect couples to a qubit, it causes Ramsey fringes to oscillate between
two frequencies. The 1-bit feedback protocol:
1. Detects the current TLS state from a single measurement
2. Adjusts the qubit drive frequency accordingly
3. Suppresses the beating pattern, restoring coherent oscillations

### 2. Long-Term Gate Fidelity Stabilization

Over extended operation, TLS defects cause stochastic frequency jumps that degrade
gate fidelities. The adaptive protocol:
1. Monitors the qubit state before each gate sequence
2. Compensates for detected frequency shifts
3. Maintains stable gate fidelities over time

### 3. Scalability to Large Qubit Arrays

For future processors with many qubits, most TLS defects will be weakly coupled,
but a small number of strongly coupled defects will dominate error budgets. The
1-bit feedback approach is:
- **Lightweight**: Only 1 bit of classical information per measurement
- **Fast**: FPGA implementation enables ~136 kHz update rate
- **Scalable**: Can be deployed independently per qubit

## Design Tradeoffs

| Parameter | Tradeoff | Design Choice |
|-----------|----------|---------------|
| Measurement overhead | More shots → better accuracy but slower | 1-shot (minimal) |
| Estimation bandwidth | Higher bandwidth → faster tracking but more noise | ~136 kHz |
| Classical processing | More complex estimator → better but slower | Simple Bayesian |
| FPGA resources | More qubits → more parallel controllers | Independent per qubit |

## Mathematical Framework

### Bistable Qubit Model

The qubit Hamiltonian with TLS coupling:
```
H = (ω_q(t)/2) σ_z + Ω(t) σ_x
```
where ω_q(t) switches between two values: ω₀ and ω₀ + Δω.

### Information-Theoretic Bound

The minimum number of measurements needed to distinguish the two states is 1 bit:
```
I(state; measurement) = H(state) - H(state | measurement)
```
For a bistable system with equal prior, H(state) = 1 bit, achieved by a single
measurement in the optimal basis.

### Bayesian Update Rule

After measurement outcome m ∈ {0, 1}:
```
P(s=m | measurement) = P(measurement | s=m) × P(s=m) / P(measurement)
```
where P(measurement | s=m) depends on the readout fidelity and the state-dependent
phase accumulation.

## Implementation Checklist

- [ ] Characterize TLS defect: identify switching rate and frequency shift Δf
- [ ] Calibrate single-shot readout fidelity for both frequency states
- [ ] Implement Bayesian estimator on FPGA (simple lookup table suffices)
- [ ] Set measurement bandwidth based on TLS switching rate
- [ ] Validate: measure Ramsey beating suppression vs. open-loop
- [ ] Validate: measure gate fidelity stability over extended operation
- [ ] Deploy: integrate into gate compilation pipeline

## When to Use This Pattern

**Use when:**
- Qubit exhibits bistable frequency behavior (TLS-induced)
- Real-time FPGA control is available
- Gate fidelity degradation from TLS defects is limiting performance
- Scaling to larger qubit arrays where TLS defects are inevitable

**Do NOT use when:**
- Qubit frequency shifts are continuous (not bistable)
- TLS switching rate exceeds FPGA update bandwidth
- Readout fidelity is too low for reliable single-shot discrimination
- Defect is weakly coupled (frequency shift below readout resolution)

## References

- arXiv:2605.03187 — "Operating a bistable qubit"
- Related: TLS defect characterization, FPGA-based quantum control,
  adaptive quantum error mitigation
