---
name: quantum-safe-control-systems
category: systems-engineering
description: Safe deployment patterns for quantum control policies in cyber-physical systems. Covers Q-DASC discrepancy-attributed safe quantum control framework, Simplex architecture for quantum-classical switching, and certified safety layers for variational quantum circuit controllers. Based on arXiv:2606.28834 (Q-DASC) and arXiv:2606.31056 (Simplex Q-CPS).
trigger_words:
  - quantum control safety
  - safe quantum control
  - quantum policy deployment
  - variational quantum control
  - Q-DASC
  - simplex quantum architecture
  - quantum cyber-physical systems
  - QA-HSGPR
  - certified quantum safety
  - quantum model misspecification
  - quantum HVAC control
---

# Quantum-Safe Control Systems

Safe deployment patterns for quantum control policies in cyber-physical systems, integrating certified classical safety layers with variational quantum circuit (VQC) controllers.

## Core Papers

- **Q-DASC** (arXiv:2606.28834): Discrepancy-Attributed Safe Quantum Control — wraps VQC policies with certified classical safety layers
- **Simplex Q-CPS** (arXiv:2606.31056): Simplex-inspired architecture integrating quantum-assisted GPR with classical GPR for CPS

## Q-DASC Framework

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Q-DASC Safety Wrapper                     │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐    ┌──────────────┐    ┌───────────────┐  │
│  │ VQC Policy   │───▶│ Discrepancy  │───▶│ Classical     │  │
│  │ (Quantum)    │    │ Detection    │    │ Safety Layer  │  │
│  └──────────────┘    └──────────────┘    └───────┬───────┘  │
│                                                  │          │
│                                    ┌─────────────▼───────┐  │
│                                    │ Violation           │  │
│                                    │ Attribution Engine  │  │
│                                    │ - Policy error      │  │
│                                    │ - Model error       │  │
│                                    │ - Physical limits   │  │
│                                    └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Key Components

1. **Discrepancy Detection**: Uses false-discovery-rate (FDR) control to identify operating regimes where the thermal model is misspecified
2. **Model Repair**: Applies shrinkage to repair local thermal gains in misspecified regions
3. **Safety Projection**: Projects the quantum policy output onto the repaired comfort-feasible set
4. **Violation Attribution**: Classifies residual violations into policy error, model error, or physical limits

### Performance Results

| Metric | Raw VQC | Model-Trusting | Q-DASC |
|--------|---------|----------------|--------|
| Comfort violation | 26.0% | 55.3% | **0.02%** |
| Under NISQ noise | — | — | **0.24%** |
| Repair-aware variant | — | — | **0.00%** |

## Simplex Architecture for Quantum CPS

### Design Pattern

```
                    ┌──────────────────┐
                    │  Runtime Monitor  │
                    │  (Safety Check)   │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
    ┌─────────▼─────┐  ┌────▼────────┐    │
    │ High-Perform.  │  │ High-Assur. │    │
    │ QA-HSGPR       │  │ Classical   │    │
    │ (Quantum)      │  │ GPR         │    │
    └───────────────┘  └─────────────┘    │
              │              │             │
              └──────┬───────┘             │
                     │                     │
              ┌──────▼───────┐             │
              │  Output to   │             │
              │  CPS Plant   │             │
              └──────────────┘             │
```

### Principles

1. **Dual-Module Design**: High-performance quantum module + high-assurance classical module
2. **Runtime Monitoring**: Continuous safety evaluation during operation
3. **Dynamic Switching**: Automatic failover based on safety certification
4. **Controllable Trade-off**: Tunable balance between performance and safety assurance

## Implementation Steps

### Step 1: Train VQC Policy
- Use variational quantum circuits for the control policy
- Optimize on nominal model data
- Validate on held-out scenarios

### Step 2: Build Discrepancy Detector
- Collect residuals between model predictions and observations
- Apply FDR control to identify statistically significant discrepancies
- Map discrepancy regions in the operating space

### Step 3: Model Repair
- Apply shrinkage estimation to local model parameters
- Use historical data to repair misspecified thermal gains
- Maintain repair history for attribution

### Step 4: Safety Projection
- Define comfort-feasible set based on physical constraints
- Project VQC policy output onto feasible set
- Measure projection distance as safety margin

### Step 5: Attribution Engine
- Track violations after projection
- Classify into: policy error (VQC suboptimal), model error (unrepairable), or physical limits (infeasible)
- Use classification to guide system improvement

## Pitfalls

- **NISQ Noise**: Finite-shot and depolarizing read-out noise can corrupt quantum policy outputs; the safety layer's classical projection is noise-invariant
- **Model Trusting**: Never deploy VQC policies without safety wrappers — raw VQC shows 26% comfort violation
- **Over-Repair**: Excessive shrinkage can over-smooth legitimate dynamics; use FDR to control false positives
- **Energy Trade-off**: Safety projection may increase energy consumption; optimize repair-aware VQC to minimize interventions

## When to Use

- Deploying quantum reinforcement learning policies in safety-critical CPS
- Building energy management (HVAC) with quantum control
- Any scenario where model misspecification can cause safety violations
- NISQ-era quantum policy deployment where read-out noise is significant

## References

- arXiv:2606.28834 — Q-DASC: State-of-the-Art Safe Quantum Control for HVAC under Local Model Misspecification
- arXiv:2606.31056 — A Simplex-Inspired Architecture for Integrating Quantum Capabilities into Cyber-Physical Systems
- arXiv:2606.31321 — Projection Operator Stochastic Equations for Non-Markovian Quantum Systems Under Continuous Measurement-Based Feedback
