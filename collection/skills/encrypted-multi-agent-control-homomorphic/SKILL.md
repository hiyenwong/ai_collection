---
name: encrypted-multi-agent-control-homomorphic
description: "End-to-End Encrypted Control Pipeline for Multi-Agent Coordination via CKKS Homomorphic Encryption. Enables privacy-preserving cloud-based coordination by redesigning control loops for FHE constraints. Activation: encrypted control, homomorphic encryption, multi-agent coordination, CKKS, privacy-preserving control, federated control."
---

## Context

Cloud-based multi-agent coordination requires sharing state with central servers, creating a fundamental tension between coordination needs and privacy requirements. Fully Homomorphic Encryption (FHE) resolves this conflict theoretically but imposes severe arithmetic constraints—only addition, multiplication, and cyclic rotation are permitted on encrypted data.

This skill provides a complete methodology for redesigning every stage of the control loop (sensing, state estimation, state propagation, consensus control) to operate on CKKS-encrypted data, with formal bounds on cumulative encryption noise and privacy-accuracy tradeoffs.

## Core Methodology

### 1. CKKS-Encrypted State Estimation

**Steady-State Kalman Gains Instead of Online Computation**
- Precompute Kalman gains offline: `K∞ = P∞ * C^T * (C * P∞ * C^T + R)^{-1}`
- Avoid matrix inversion on encrypted data (computationally expensive)
- State update becomes linear: `x̂_{k+1} = A * x̂_k + K∞ * (y_k - C * x̂_k)`
- All operations (matrix multiply, subtraction) are CKKS-compatible

**Implementation Pattern**:
```python
# Offline: compute steady-state Kalman gain
K_ss = compute_steady_state_kalman(A, C, Q, R)

# Online (on encrypted data):
# y_enc = encrypt(sensor_reading)
# x_est_enc = A_enc * x_est_prev_enc + K_ss_enc * (y_enc - C_enc * x_est_prev_enc)
```

### 2. Graph Laplacian via Diagonal Method

**Unified Topology Handling (Ring, Torus, Complete Graph)**
- Standard Laplacian: `L = D - A` (degree matrix minus adjacency)
- Diagonal method: represent `L` as sum of cyclic diagonal matrices
- Cost proportional to number of nonzero cyclic diagonals
- Ring topology: 2 diagonals → cost = 2 rotations + additions
- Complete graph: N diagonals → cost = N rotations

**Example for Ring Topology**:
```
L_ring = diag([1, 1, ..., 1]) + cyclic_shift_left(diag([-1, 0, ..., 0])) 
         + cyclic_shift_right(diag([-1, 0, ..., 0]))
```

**CKKS-Compatible Consensus Update**:
```python
# x_enc = state vector (encrypted)
# For ring topology (N agents):
diag_enc = encrypt([1, 1, ..., 1])  # degree matrix diagonal
shift_left_enc = cyclic_rotate_left(encrypt([-1, 0, ..., 0]))
shift_right_enc = cyclic_rotate_right(encrypt([-1, 0, ..., 0]))
L_enc = diag_enc + shift_left_enc + shift_right_enc
x_next_enc = x_enc - dt * L_enc * x_enc  # consensus dynamics
```

### 3. Separation Principle for Noise Analysis

**Decouple Controller and Observer Errors**
- Closed-loop system: `e_c = controller error, e_o = observer error`
- Separation principle: errors evolve independently
- Controller error: `e_c(k+1) = A_cl * e_c(k)` where `A_cl = A - B*K`
- Observer error: `e_o(k+1) = A_obs * e_o(k)` where `A_obs = A - K*C`

**Privacy-Accuracy Tradeoff Bound**:
```
Steady-state error ball: ||e_ss|| ≤ ρ(L_cl) * ε_bootstrap / (1 - ρ(L_cl))
where:
- ρ(L_cl) = spectral radius of closed-loop system
- ε_bootstrap = CKKS bootstrapping precision (noise level)
```

**Design Equation**:
- Given privacy requirement → choose ε_bootstrap
- Compute required controller gain K to ensure ρ(L_cl) < 1 - ε_bootstrap / ||e_target||
- Direct equation for privacy-accuracy tradeoff

### 4. Periodic Bootstrapping as Impulsive Disturbance

**CKKS Bootstrapping Noise Model**
- Bootstrapping occurs every N cycles (to refresh ciphertext precision)
- Model as impulsive disturbance: `e_bootstrap = δ(t - t_bootstrap) * ε_bootstrap`
- Cumulative effect: bounded steady-state error ball (not diverging)
- Periodic reset prevents noise accumulation

**Timing Optimization**:
```
Bootstrap frequency: every T_bootstrap cycles
T_bootstrap = ceil(log(ε_acceptable / ε_bootstrap) / log(ρ(L_cl)))
```

### 5. Formation Control Validation

**Multi-Agent Formation Scenario**
- N agents, ring/torus topology
- Desired formation: relative distances maintained
- Control: `u_i = -K * (x_i - x_i_desired) + consensus term`
- All computations on encrypted state

**Experimental Results (Paper)**:
- Stable closed-loop operation under encryption
- Bounded tracking error within theoretical bound
- Privacy: server learns NOTHING about agent states (all encrypted)
- Coordination: agents converge to formation via encrypted consensus

## Implementation Steps

### Step 1: Design Control Law for CKKS Compatibility
1. Ensure controller uses only linear operations: `u = K*x + feedforward`
2. Avoid nonlinearities (saturation, sigmoid, etc.)—not CKKS-compatible
3. If nonlinear control needed → approximate with polynomial (degree ≤ CKKS limit)

### Step 2: Compute Steady-State Gains Offline
1. Solve Riccati equation for Kalman gain: `P_{k+1} = A*P_k*A^T + Q - K*R*K^T`
2. Iterate until convergence → `P∞, K∞`
3. Compute controller gain: `K_control = place(A, B, desired_eigenvalues)` or LQR

### Step 3: Encode Graph Laplacian as Cyclic Diagonals
1. Identify agent topology (ring, torus, grid, complete)
2. Count nonzero cyclic diagonals in Laplacian
3. Precompute diagonal encoding: `L = sum_i (shift_i * diag_i)`
4. Verify: each shift operation is CKKS rotation primitive

### Step 4: Set Bootstrap Frequency
1. Estimate closed-loop spectral radius: `ρ = max|eigenvalues(A - B*K)|`
2. Set bootstrap precision: `ε_bootstrap = 10^{-precision_bits}`
3. Compute bootstrap interval: `T = log(ε_target/ε_bootstrap) / log(ρ)`
4. Schedule periodic bootstrapping every T cycles

### Step 5: Deploy Encrypted Pipeline
1. Initialize CKKS context (poly modulus degree, coefficient modulus)
2. Encrypt initial state: `x_enc = CKKS.encrypt(x_0)`
3. Loop: (a) sense → encrypt, (b) update estimate, (c) compute control, (d) bootstrap if needed
4. Decrypt control signal ONLY at agent side (server never decrypts)

## Pitfalls

- **Matrix Inversion on Encrypted Data**: CKKS cannot invert matrices efficiently—use precomputed steady-state gains
- **Nonlinear Control Laws**: Polynomial approximation required; degree limited by CKKS modulus chain
- **Bootstrap Overhead**: Bootstrapping is expensive (ms to seconds); balance frequency vs noise
- **Topology Complexity**: Complete graph Laplacian requires N rotations—may exceed practical limits
- **Spectral Radius > 1**: Unstable closed-loop → error diverges despite bootstrapping; ensure ρ(A_cl) < 1
- **Scale Mismatch**: CKKS has limited dynamic range; normalize state before encryption

## Verification

1. **Noise Bound Test**: Run encrypted pipeline for N cycles; measure steady-state error; compare with theoretical bound
2. **Privacy Test**: Server ciphertext should reveal NO information (formal indistinguishability)
3. **Formation Test**: Agents converge to desired formation under encryption
4. **Spectral Radius**: Compute eigenvalues of `A - B*K` → ensure all |λ| < 1

## References

- arXiv:2606.07375 (June 2026)
- CKKS homomorphic encryption scheme (Cheon-Kim-Kim-Song)
- Multi-agent consensus protocols (Olfati-Saber, Murray)
- Separation principle for observer-controller design