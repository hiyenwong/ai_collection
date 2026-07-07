---
name: dose-efficient-quantum-interferometry
description: "Dose-efficient quantum phase estimation methodology using sequential strategies in lossy optical interferometry for biological and medical imaging. Control-enhanced sequential strategies achieve superior quantum Fisher information per dose, approaching the quantum limit in dose-limited regimes."
triggered_by:
  - "dose-efficient quantum imaging"
  - "quantum phase estimation dose"
  - "lossy interferometry quantum"
  - "quantum Fisher information dose"
  - "biological imaging quantum metrology"
  - "sequential quantum strategy"
  - "dose-limited quantum sensing"
  - "quantum-enhanced medical imaging"
  - 量子剂量效率成像
  - 量子相位估计剂量
  - 生物成像量子计量
---

# Dose-Efficient Quantum Phase Estimation in Lossy Optical Interferometry

## Overview

In biological and medical imaging applications (fluorescence microscopy, OCT, optical biopsy), samples are light-sensitive and require stringent limits on light intensity — **dose-limited regimes**. Maximizing precision per photon dose is crucial. This methodology from arXiv:2606.14254 (June 2026) demonstrates that **sequential quantum strategies with feedback control** outperform classical parallel strategies for phase estimation under photon loss.

## Core Concepts

### Dose-Limited Regime
- Biological samples (cells, tissues) are damaged by excessive light exposure
- Total photon budget (dose) is constrained
- Precision must be maximized per photon, not per unit time
- Classical shot-noise limit: Δφ ≥ 1/√N where N = photon number

### Sequential vs Parallel Strategies
| Strategy | Description | Performance under Loss |
|----------|-------------|----------------------|
| **Parallel (classical)** | All photons sent simultaneously (e.g., N00N states) | Quantum advantage degrades rapidly with loss |
| **Sequential** | Photons sent one-by-one with adaptive feedback | More robust to loss |
| **Sequential + Control** | Sequential with active control operations | Superior QFI/dose, approaches quantum limit |

### Quantum Fisher Information (QFI) per Dose
- QFI bounds the achievable precision: Δφ ≥ 1/√(QFI × M) where M = measurements
- In dose-limited regime, maximize **QFI per photon** rather than total QFI
- Control-enhanced sequential strategy achieves QFI/dose → quantum limit
- Outperforms unbalanced N00N states even with significant photon loss

## Methodology

### Step 1: Identify Dose Constraints
Determine the maximum acceptable photon dose for the sample:
- Live cell imaging: typically < 10^4-10^5 photons/μm²
- Tissue samples: higher tolerance but still limited
- The constraint determines whether sequential or parallel strategies are optimal

### Step 2: Choose Strategy Based on Loss Rate
```
If loss_rate < 10%: Parallel (N00N) strategies viable
If 10% < loss_rate < 50%: Sequential strategies preferred
If loss_rate > 50%: Control-enhanced sequential essential
```

### Step 3: Implement Sequential Strategy
1. Send single photons through interferometer sequentially
2. After each photon detection, update phase estimate
3. Use Bayesian or adaptive feedback to optimize next photon's input state
4. Accumulate phase information across sequential measurements

### Step 4: Add Control Enhancement (Optimal)
1. Insert control operations between sequential passes
2. Control operations compensate for accumulated phase errors
3. Effectively "undo" the effect of loss on the quantum state
4. Achieve QFI per dose approaching the fundamental quantum limit

### Step 5: Evaluate via QFI per Dose
Compare strategies using:
- **QFI per dose**: Primary metric for dose-limited imaging
- **Robustness to loss**: How performance degrades with increasing loss
- **Implementation complexity**: Hardware requirements for each strategy

## Mathematical Framework

### QFI for Sequential Strategy (No Control)
```
QFI_seq/dose ≈ 4T / (1-T)
```
where T = transmission coefficient (1-T = loss rate)

### QFI for Sequential Strategy with Control
```
QFI_seq+ctrl/dose ≈ 4T / (1-T)²
```
The control enhancement provides a quadratic improvement in the denominator, significantly boosting performance under high loss.

### Classical Limit (Parallel Strategy with Loss)
```
QFI_parallel/dose ≈ 4T
```
Linear scaling with transmission — much worse than sequential under significant loss.

## Usage Patterns

### Pattern 1: Designing Quantum-Enhanced Biological Microscopy
When designing quantum-enhanced imaging for biological samples:
1. Determine dose limit for sample type
2. Estimate photon loss rate through sample
3. Choose sequential strategy with control if loss > 10%
4. Optimize control operations based on sample-specific loss profile

### Pattern 2: Quantum Sensor Calibration
For calibrating quantum sensors in lossy environments:
1. Characterize loss profile of the measurement setup
2. Use sequential QFI as benchmark for optimal performance
3. Compare actual sensor performance against sequential QFI bound
4. Identify whether losses are the limiting factor or other noise sources

### Pattern 3: Resource-Constrained Quantum Metrology
For any quantum measurement under resource constraints:
1. Define the resource constraint (photons, time, energy)
2. Formulate the problem as maximizing information per resource unit
3. Consider sequential strategies as they typically offer better resource efficiency
4. Add control/feedback operations to approach fundamental limits

## Error Handling

### When Sequential Strategy Fails to Outperform
- Check if loss rate is actually low enough that parallel strategies are better
- Verify that control operations are correctly implemented
- Ensure QFI calculation accounts for all noise sources, not just photon loss

### Implementation Challenges
- Sequential strategies require active feedback electronics
- Control operations add complexity to the optical setup
- For very high loss (>90%), even sequential strategies approach classical limits

## Related Skills
- `quantum-metrology-sensing-review` — Comprehensive quantum metrology methodology
- `quantum-biomedical-imaging-sensors` — Quantum biomedical sensing framework
- `quantum-picotesla-biomagnetism-sensing` — Quantum sensing for biomagnetism
- `neural-inverse-design-scintillator-medical` — AI-optimized medical imaging components

## References
- arXiv:2606.14254 — "Dose-efficient Quantum Phase Estimation in Lossy Optical Interferometry" (June 2026)
- PRX Quantum 4, 040337 (2023) — Classical shadows for quantum processes
