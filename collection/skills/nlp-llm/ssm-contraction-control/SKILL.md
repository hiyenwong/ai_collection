---
name: ssm-contraction-control
description: "Controller design for Structured State-space Models (SSMs) using contraction theory with indirect data-driven output feedback. Use when: (1) designing controllers for nonlinear systems identified via SSM surrogate models, (2) implementing contraction-based stabilization with Linear Matrix Inequality (LMI) conditions, (3) establishing separation principle for observer-controller design, (4) applying scalable control design to time-series and dynamical systems. First controllability/observability analysis of SSMs with contraction theory framework."
---

# SSM Controller Design via Contraction Theory

Indirect data-driven output feedback controller synthesis for nonlinear systems using Structured State-space Models (SSMs) as surrogate models.

## Why SSMs?

### Advantages over Transformers
- **Linear computational complexity**: O(L) vs O(L²) for sequence length L
- **Long-term dependency capture**: Efficient modeling of extended sequences
- **Scalable control design**: LMI-based synthesis with tractable computation

### State-space Structure
```
h_t = A h_{t-1} + B x_t
y_t = C h_t + D x_t
```

where:
- h_t = hidden state (continuous-time dynamics)
- x_t = input
- y_t = output
- A, B, C, D = learnable parameters

## Core Contributions

### 1. Controllability Analysis
**First SSM controllability characterization:**
- Linear-time-invariant (LTI) structure
- Reachability condition: rank([B, AB, ..., A^(n-1)B]) = n
- Connection to sequence learning capacity

### 2. Observability Analysis
**First SSM observability characterization:**
- Output injectivity condition
- rank([C^T, A^T C^T, ..., (A^T)^(n-1) C^T]) = n
- Relation to state reconstruction

### 3. Separation Principle
**Independent observer + controller design:**
- Observer: State estimation from outputs
- Controller: State-feedback stabilization
- Closed-loop stability preserved when designed independently

### 4. Contraction-Based Design
**LMI conditions for exponential stability:**
- Incremental stability via contraction metric
- Scalable synthesis: solve LMIs per subsystem
- Robustness to bounded disturbances

## Control Framework

### Surrogate Model Learning
1. Collect data from nonlinear system
2. Train SSM as surrogate model
3. Extract learned parameters (A, B, C, D)
4. Apply control design to SSM

### Contraction Theory Basics
**Definition:** System is contracting if all trajectories converge exponentially.

**Metric condition:**
```
M > 0,  A^T M A - M ≤ -Q (Q > 0)
```

**Incremental stability:**
```
|x(t) - y(t)| ≤ e^(-λt) |x(0) - y(0)|
```

### LMI Controller Synthesis
**Objective:** Find K such that (A + BK) is contracting.

**LMI formulation:**
```
Find: M > 0, K, Y
Subject to:
  (A + BK)^T M (A + BK) - M < 0
  Y = K M
```

Scalable: Solve per subsystem, aggregate via contraction theory.

### Observer Design
**Luenberger observer:**
```
ĥ_t = A ĥ_{t-1} + B x_t + L(y_t - C ĥ_t)
```

**LMI condition:**
```
(A - LC)^T M (A - LC) - M < 0
```

## Implementation Workflow

### Step 1: System Identification
- Collect input-output trajectories
- Train SSM via gradient descent
- Validate model accuracy

### Step 2: Controllability/Observability Check
- Compute controllability matrix
- Compute observability matrix
- Verify rank conditions

### Step 3: Controller Synthesis
- Formulate contraction LMI
- Solve for feedback gain K
- Verify closed-loop contraction

### Step 4: Observer Synthesis
- Formulate observer LMI
- Solve for observer gain L
- Verify estimation contraction

### Step 5: Output Feedback Control
- Combine observer + controller
- Apply separation principle
- Verify exponential stability

## Key Results

**Theorem 1 (Controllability):** SSM is controllable iff controllability matrix has full rank.

**Theorem 2 (Observability):** SSM is observable iff observability matrix has full rank.

**Theorem 3 (Separation):** Independent observer-controller design preserves exponential stability when both are contracting.

**Theorem 4 (Scalability):** Large-scale SSMs decompose into subsystems with local LMIs → tractable synthesis.

## Advantages

- **Data-driven:** No explicit physics model required
- **Scalable:** Linear complexity for long sequences
- **Systematic:** LMI-based with guaranteed stability
- **Robust:** Contraction implies disturbance rejection

## Applications

- **Time-series control:** Regulate dynamical sequences
- **Robotics:** Motion planning with learned dynamics
- **Process control:** Chemical plant regulation
- **Economic systems:** Market stabilization
- **Network control:** Multi-agent coordination

## References

- arXiv: 2604.07069v1 - "Controller Design for Structured State-space Models via Contraction Theory"
- Authors: Muhammad Zakwan, Vaibhav Gupta, Alireza Karimi, Efe C. Balta, Giancarlo Ferrari-Trecate
- Published: 2026-04-08
- PDF: papers/2026-04-09/ssm-contraction.pdf

## Further Reading

See `references/lmi_formulation.md` for detailed LMI derivations and solver implementations.