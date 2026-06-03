---
name: energy-regularized-neural-mpc
description: "Energy-based regularization for learning residual dynamics in Neural MPC for omnidirectional aerial robots. Use when: (1) Designing neural network dynamics models for physical systems, (2) Implementing Model Predictive Control with learned dynamics, (3) Building physics-informed neural networks for robotic control, (4) Ensuring physically plausible predictions in out-of-distribution scenarios. Activation: energy regularization, neural MPC, residual dynamics, aerial robots, energy-based learning, physics-informed control, omnidirectional robots, energy constraints."
---

# Energy-based Regularization for Neural MPC

Physics-informed approach to learning residual dynamics in Neural Model Predictive Control by incorporating energy conservation and dissipation as structural inductive biases, enabling safe and reliable control of omnidirectional aerial robots in complex environments.

## Core Innovation

**Energy-based regularization** as an inductive bias for learning residual dynamics models. Physical systems conserve or dissipate energy in structured ways — neural network dynamics models should respect these constraints. This ensures physically plausible predictions even in out-of-distribution (OOD) scenarios, dramatically improving safety and reliability for aerial robots operating in complex, unpredictable environments.

**Key insight**: Energy conservation/dissipation is a universal structural property of physical systems. Encoding this as a regularization term during dynamics learning constrains the neural network's hypothesis space toward physically meaningful models, reducing the risk of unphysical predictions that could destabilize the MPC controller.

## Problem Solved

Neural MPC relies on learned dynamics models to predict future states. Key failure modes of pure data-driven approaches:

- **Unphysical predictions**: Neural networks can predict dynamics that violate fundamental physics (e.g., energy creation from nowhere)
- **OOD instability**: Poor generalization outside training distribution leads to catastrophic prediction errors
- **Safety violations**: Unphysical dynamics models cause MPC to generate infeasible or dangerous control inputs
- **Cascading errors**: Small prediction errors compound over the MPC prediction horizon

Energy-based regularization addresses all four simultaneously by constraining the learned model to the physically feasible subspace.

## Technical Approach

### Residual Dynamics Modeling

Instead of learning the full dynamics, decompose into a known nominal model plus a learned residual:

$$
x_{k+1} = f_{\text{nominal}}(x_k, u_k) + g_{\text{neural}}(x_k, u_k; \theta)
$$

- **Nominal model** $f_{\text{nominal}}$: Physics-based model capturing dominant dynamics (rigid body equations, aerodynamic terms)
- **Residual model** $g_{\text{neural}}$: Neural network capturing unmodeled effects (complex aerodynamics, actuator dynamics, environmental disturbances)

**Why residual**: The nominal model already satisfies physical constraints by construction. The residual only needs to capture small corrections, making it easier to regularize and more sample-efficient to learn.

### Energy-Based Regularization Principle

The total energy of a physical system must satisfy:

$$
\frac{dE}{dt} \leq P_{\text{input}} - P_{\text{dissipation}}
$$

For the learned dynamics to be physically plausible, the energy change predicted by the residual model must be consistent with energy conservation:

$$
E(x_{k+1}) - E(x_k) \leq \text{work done by } u_k - \text{dissipated energy}
$$

**Regularization term**:

$$
\mathcal{L}_{\text{energy}} = \mathbb{E}_{(x, u) \sim \mathcal{D}} \left[ \max\left(0, \Delta E_{\text{predicted}} - \Delta E_{\text{physical\_bound}}\right)^2 \right]
$$

This penalizes predictions that would create energy beyond what is physically possible (energy input minus dissipation).

### Total Training Objective

$$
\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{MSE}}(x_{k+1}^{\text{true}}, \hat{x}_{k+1}) + \lambda \cdot \mathcal{L}_{\text{energy}}
$$

where $\lambda$ balances prediction accuracy against physical consistency.

### Energy Function Design for Aerial Robots

For an omnidirectional aerial robot, the relevant energy components include:

| Energy Component | Expression | Physical Meaning |
|---|---|---|
| **Kinetic (translational)** | $\frac{1}{2} m v^T v$ | Motion through space |
| **Kinetic (rotational)** | $\frac{1}{2} \omega^T I \omega$ | Rotation about body axes |
| **Potential (gravitational)** | $m g z$ | Height in gravitational field |
| **Dissipation (aerodynamic)** | $-v^T D(v) v$ | Air resistance drag |
| **Input work** | $u^T B(x) u$ | Thrust power from motors |

**Energy bound for one timestep**:

$$
\Delta E_{\text{bound}} = u_k^T B(x_k) u_k \cdot \Delta t - v_{k+1}^T D(v_{k+1}) v_{k+1} \cdot \Delta t
$$

### Neural MPC Formulation

The MPC problem with energy-constrained learned dynamics:

$$
\min_{u_{0:N-1}} \sum_{k=0}^{N-1} \ell(x_k, u_k, x_{\text{ref}}) + \ell_f(x_N, x_{\text{ref}})
$$

$$
\text{s.t. } x_{k+1} = f_{\text{nominal}}(x_k, u_k) + g_{\text{neural}}(x_k, u_k; \theta^*)
$$

$$
x_k \in \mathcal{X}, \quad u_k \in \mathcal{U}
$$

$$
E(x_{k+1}) - E(x_k) \leq \Delta E_{\text{bound}}(x_k, u_k) \quad \text{(energy constraint)}
$$

The energy constraint acts as a **soft safety barrier** — even if the neural dynamics model produces an unphysical prediction, the constraint ensures the optimizer only considers physically plausible trajectories.

## Implementation Patterns

### Pattern 1: Energy-Regularized Dynamics Training

```python
import torch
import torch.nn as nn

class EnergyRegularizedDynamicsModel(nn.Module):
    """
    Residual dynamics model with energy-based regularization.
    
    Learns g_neural(x, u; θ) such that:
    x_next = f_nominal(x, u) + g_neural(x, u; θ)
    and energy conservation is enforced via regularization.
    """
    
    def __init__(self, state_dim, action_dim, hidden_dim=128):
        super().__init__()
        self.state_dim = state_dim
        self.action_dim = action_dim
        
        # Residual dynamics network
        self.net = nn.Sequential(
            nn.Linear(state_dim + action_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, state_dim)
        )
    
    def forward(self, x, u):
        """Predict residual dynamics Δx = g(x, u)"""
        return self.net(torch.cat([x, u], dim=-1))
    
    def compute_energy_change(self, x, x_next, u, dt, params):
        """
        Compute the change in total energy between states.
        
        For omnidirectional aerial robot:
        E = KE_trans + KE_rot + PE_grav
        """
        m, g = params['mass'], params['gravity']
        I = params['inertia_matrix']
        
        # Extract velocity components from state
        v = x[..., 3:6]       # linear velocity
        v_next = x_next[..., 3:6]
        omega = x[..., 6:9]   # angular velocity
        omega_next = x_next[..., 6:9]
        z = x[..., 2]          # altitude
        z_next = x_next[..., 2]
        
        # Kinetic energy change (translational)
        KE_trans = 0.5 * m * (
            torch.sum(v_next**2, dim=-1) - torch.sum(v**2, dim=-1)
        )
        
        # Kinetic energy change (rotational)
        KE_rot = 0.5 * (
            (omega_next @ I).sum(dim=-1) * omega_next.sum(dim=-1) -
            (omega @ I).sum(dim=-1) * omega.sum(dim=-1)
        )
        
        # Potential energy change
        PE = m * g * (z_next - z)
        
        return KE_trans + KE_rot + PE
    
    def compute_energy_bound(self, x, u, dt, params):
        """
        Compute the maximum physically possible energy change.
        
        ΔE_bound = input_work - dissipation
        """
        B = params['input_matrix']
        D = params['drag_coefficients']
        v = x[..., 3:6]
        
        # Work done by control inputs
        input_work = (u @ B @ u).sum(dim=-1) * dt
        
        # Aerodynamic dissipation (quadratic drag)
        dissipation = (D * v.abs() * v).sum(dim=-1) * dt
        
        return input_work - dissipation
    
    def energy_regularization_loss(self, x, x_next_pred, u, dt, params):
        """
        Energy regularization loss: penalize energy creation beyond bound.
        
        L_energy = max(0, ΔE_predicted - ΔE_bound)²
        """
        ΔE_pred = self.compute_energy_change(x, x_next_pred, u, dt, params)
        ΔE_bound = self.compute_energy_bound(x, u, dt, params)
        
        violation = torch.relu(ΔE_pred - ΔE_bound)
        return torch.mean(violation ** 2)
    
    def train_step(self, x, u, x_next_true, optimizer, dt, params, 
                   lambda_energy=0.1):
        """Single training step with energy regularization."""
        optimizer.zero_grad()
        
        # Predict residual and full next state
        residual = self(x, u)
        x_next_pred = self.nominal_dynamics(x, u) + residual
        
        # MSE loss on prediction accuracy
        mse_loss = torch.mean((x_next_true - x_next_pred) ** 2)
        
        # Energy regularization loss
        energy_loss = self.energy_regularization_loss(
            x, x_next_pred, u, dt, params
        )
        
        # Combined loss
        total_loss = mse_loss + lambda_energy * energy_loss
        
        total_loss.backward()
        optimizer.step()
        
        return {
            'total': total_loss.item(),
            'mse': mse_loss.item(),
            'energy': energy_loss.item()
        }
```

### Pattern 2: Neural MPC with Energy Constraints

```python
import cvxpy as cp
import numpy as np

class EnergyConstrainedNeuralMPC:
    """
    Model Predictive Controller using energy-regularized dynamics.
    
    Uses the learned dynamics model within an MPC optimization,
    with explicit energy constraints for safety.
    """
    
    def __init__(self, dynamics_model, horizon, dt, params):
        self.model = dynamics_model
        self.N = horizon
        self.dt = dt
        self.params = params
        
    def compute_control(self, x_current, x_reference):
        """
        Solve MPC optimization with energy constraints.
        
        For real-time deployment, this typically uses:
        - Warm-starting from previous solution
        - Limited solver iterations
        - GPU-accelerated gradient computation
        """
        state_dim = self.model.state_dim
        action_dim = self.model.action_dim
        
        # Optimization variables
        X = cp.Variable((self.N + 1, state_dim))
        U = cp.Variable((self.N, action_dim))
        
        # Cost: tracking + control effort
        cost = 0
        for k in range(self.N):
            cost += cp.sum_squares(X[k] - x_reference)
            cost += 0.01 * cp.sum_squares(U[k])
        cost += 10 * cp.sum_squares(X[self.N] - x_reference)  # terminal cost
        
        constraints = []
        
        # Dynamics constraints (using linearized neural model)
        x_prev = x_current
        for k in range(self.N):
            # Linearized dynamics around current operating point
            A_k, B_k = self.model.linearize(x_prev, U[k])
            constraints.append(X[k+1] == A_k @ X[k] + B_k @ U[k])
            x_prev = X[k]
            
            # State constraints
            constraints.append(X[k] >= self.params['state_lower'])
            constraints.append(X[k] <= self.params['state_upper'])
            
            # Input constraints
            constraints.append(U[k] >= self.params['action_lower'])
            constraints.append(U[k] <= self.params['action_upper'])
        
        # Energy constraints at each step
        for k in range(self.N):
            energy_change = self._energy_change_cvx(X[k], X[k+1], U[k])
            energy_bound = self._energy_bound_cvx(X[k], U[k])
            constraints.append(energy_change <= energy_bound)
        
        prob = cp.Problem(cp.Minimize(cost), constraints)
        prob.solve(solver=cp.OSQP, verbose=False)
        
        if prob.status in ['optimal', 'optimal_inaccurate']:
            return U.value[0]
        else:
            # Fallback: nominal controller
            return self._nominal_control(x_current, x_reference)
    
    def _energy_change_cvx(self, x, x_next, u):
        """Energy change as CVXPY expression (simplified quadratic)."""
        m, g = self.params['mass'], self.params['gravity']
        I = self.params['inertia_matrix']
        
        # Simplified: translational KE + PE
        v = x[3:6]
        v_next = x_next[3:6]
        z = x[2]
        z_next = x_next[2]
        
        KE = 0.5 * m * cp.sum_squares(v_next) - 0.5 * m * cp.sum_squares(v)
        PE = m * g * (z_next - z)
        
        return KE + PE
    
    def _energy_bound_cvx(self, x, u):
        """Energy bound as CVXPY expression."""
        B = self.params['input_matrix']
        D = self.params['drag_coefficients']
        
        input_work = cp.quad_form(u, B) * self.dt
        dissipation = cp.sum(D * cp.multiply(x[3:6], x[3:6])) * self.dt
        
        return input_work - dissipation
```

### Pattern 3: Complete Aerial Robot Control Pipeline

```python
import torch
import numpy as np
from dataclasses import dataclass

@dataclass
class AerialRobotParams:
    """Omnidirectional aerial robot physical parameters."""
    mass: float = 2.5              # kg
    gravity: float = 9.81          # m/s²
    inertia_matrix: np.ndarray = None   # 3x3
    input_matrix: np.ndarray = None     # 6x6
    drag_coefficients: np.ndarray = None  # 3x1
    
    def __post_init__(self):
        if self.inertia_matrix is None:
            self.inertia_matrix = np.diag([0.03, 0.03, 0.05])
        if self.input_matrix is None:
            self.input_matrix = np.eye(6) * 10.0
        if self.drag_coefficients is None:
            self.drag_coefficients = np.array([0.5, 0.5, 0.3])


class OmniDroneController:
    """
    Complete control pipeline for omnidirectional aerial robot.
    
    Combines:
    1. Nominal physics model (rigid body dynamics)
    2. Energy-regularized neural residual model
    3. MPC with energy constraints
    """
    
    def __init__(self, params: AerialRobotParams):
        self.params = params
        self.dynamics_model = EnergyRegularizedDynamicsModel(
            state_dim=12,   # [pos(3), vel(3), quat(4), ang_vel(3)]
            action_dim=6    # [thrust(6) for omnidirectional]
        )
        self.mpc = EnergyConstrainedNeuralMPC(
            dynamics_model=self.dynamics_model,
            horizon=20,
            dt=0.02,
            params=params
        )
    
    def nominal_dynamics(self, x, u):
        """Rigid body dynamics for omnidirectional aerial robot."""
        m, g = self.params.mass, self.params.gravity
        I = self.params.inertia_matrix
        
        pos = x[0:3]
        vel = x[3:6]
        quat = x[6:10]
        omega = x[10:13]
        
        # Acceleration from forces (simplified)
        R = self._quat_to_rotation_matrix(quat)
        f_total = R @ u[0:3] - np.array([0, 0, m * g])
        accel = f_total / m
        
        # Angular acceleration from torques
        torque = u[3:6]
        alpha = np.linalg.inv(I) @ (torque - np.cross(omega, I @ omega))
        
        return np.array([*vel, *accel, *self._quat_derivative(quat, omega), *alpha])
    
    def step(self, x_current, x_reference, learn=True):
        """Single control loop iteration."""
        # Compute MPC control
        u = self.mpc.compute_control(x_current, x_reference)
        
        # Apply to system (simulation or real robot)
        x_next_nominal = self.nominal_dynamics(x_current, u)
        
        if learn:
            # Collect data for residual model training
            self._collect_training_data(x_current, u, x_next_nominal)
        
        return u, x_next_nominal
    
    def train_residual_model(self, dataset, epochs=100, lambda_energy=0.1):
        """Train the energy-regularized residual model."""
        optimizer = torch.optim.Adam(self.dynamics_model.parameters(), lr=1e-3)
        
        for epoch in range(epochs):
            for batch in dataset:
                x, u, x_next = batch
                losses = self.dynamics_model.train_step(
                    x, u, x_next, optimizer,
                    dt=0.02, params=self.params.__dict__,
                    lambda_energy=lambda_energy
                )
            
            if epoch % 10 == 0:
                print(f"Epoch {epoch}: MSE={losses['mse']:.4f}, "
                      f"Energy={losses['energy']:.4f}")
```

## Activation Keywords

### English
- energy regularization
- neural MPC
- residual dynamics learning
- energy-based learning
- physics-informed control
- omnidirectional aerial robots
- energy constraints
- physically plausible dynamics
- model predictive control neural
- dynamics learning regularization
- out-of-distribution safety
- aerial robot control
- energy conservation neural networks
- residual model predictive control
- learned dynamics MPC

### 中文 (Chinese)
- 能量正则化
- 神经模型预测控制
- 残差动力学学习
- 能量约束
- 物理信息控制
- 全向飞行机器人
- 动力学模型正则化
- 能量守恒学习
- 物理一致性预测
- 分布外安全
- 无人机控制
- 基于能量的神经网络
- 残差MPC
- 学习型动力学控制
- 能量正则化训练

## Pitfalls and Mitigations

### 1. Energy Function Design

**Problem**: Poorly designed energy functions lead to meaningless regularization.

**Common mistakes**:
- Using incomplete energy models (e.g., ignoring rotational energy for aerial robots)
- Mismatched units between energy terms
- Incorrect dissipation modeling (e.g., using linear instead of quadratic drag)
- Forgetting to include potential energy changes

**Mitigations**:
```python
# Always verify energy function consistency
def validate_energy_function(energy_fn, test_trajectories):
    """Check energy conservation on known conservative trajectories."""
    for traj in test_trajectories:
        total_energy = [energy_fn(state) for state in traj]
        # For frictionless conservative system, energy should be constant
        variation = np.std(total_energy) / np.mean(total_energy)
        assert variation < 0.01, f"Energy variation too high: {variation}"
```

**Best practices**:
- Derive energy function from first principles (Lagrangian/Hamiltonian mechanics)
- Validate against analytical solutions where available
- Start simple (translational KE + PE) and incrementally add complexity
- Test regularization sensitivity across $\lambda$ values

### 2. Constraint Violation in MPC

**Problem**: Even with energy regularization, the MPC optimizer may find trajectories near the constraint boundary where the neural model's uncertainty is high.

**Common mistakes**:
- Treating energy constraints as hard when the model has prediction uncertainty
- Not accounting for model uncertainty in the constraint
- Over-relying on regularization without explicit constraint handling

**Mitigations**:
```python
def energy_constraint_with_margin(x, u, model, params, safety_margin=1.1):
    """
    Add safety margin to energy constraint.
    
    Instead of: ΔE ≤ ΔE_bound
    Use: ΔE ≤ ΔE_bound / safety_margin
    """
    bound = compute_energy_bound(x, u, params)
    return bound / safety_margin  # More conservative bound

def ensemble_energy_check(x, u, models, params):
    """
    Use ensemble of dynamics models to estimate prediction uncertainty.
    Tighten energy constraint based on ensemble disagreement.
    """
    predictions = [model.predict_with_energy(x, u, params) for model in models]
    energy_mean = np.mean([p['energy'] for p in predictions])
    energy_std = np.std([p['energy'] for p in predictions])
    
    # Robust constraint: mean - k*std ≤ bound
    return energy_mean - 2.0 * energy_std
```

**Best practices**:
- Always use safety margins proportional to model uncertainty
- Implement fallback nominal controller when constraints are violated
- Monitor constraint violation rate during operation
- Use tube-MPC or robust MPC formulations for guaranteed safety

### 3. Simulation-to-Reality Gap

**Problem**: Dynamics models trained in simulation may not generalize to the real robot due to unmodeled effects (motor dynamics, sensor noise, environmental conditions).

**Common mistakes**:
- Training exclusively on clean simulation data
- Not including sensor noise in training
- Ignoring actuator delays and dynamics
- Testing only in nominal conditions

**Mitigations**:
```python
def simulate_to_real_transfer(sim_data, real_data_few_shot, params):
    """
    Adapt simulation-trained model to reality with limited real data.
    """
    # Step 1: Train on simulation data with energy regularization
    model = train_on_simulation(sim_data, lambda_energy=0.1)
    
    # Step 2: Fine-tune on limited real data
    # Keep energy regularization to prevent catastrophic forgetting
    model.fine_tune(
        real_data_few_shot,
        lambda_energy=0.5,  # Higher weight on real data
        freeze_layers=2,    # Keep early layers fixed
        lr=1e-4
    )
    
    # Step 3: Domain randomization during training
    def augment_with_domain_randomization(batch):
        x, u, x_next = batch
        # Randomize physical parameters
        x = x + torch.randn_like(x) * 0.01  # sensor noise
        u = u * (1 + torch.rand_like(u) * 0.1)  # actuator variation
        return x, u, x_next
    
    return model
```

**Best practices**:
- Collect even a small amount of real-world data for fine-tuning
- Use domain randomization during simulation training
- Deploy with conservative safety margins initially
- Implement online adaptation with energy constraints as safety guard
- Validate extensively on hardware-in-the-loop before flight

## Comparison with Alternatives

| Method | Physical Consistency | OOD Robustness | Sample Efficiency | Safety Guarantee |
|---|---|---|---|---|
| Pure neural dynamics | ✗ | ✗ | High | ✗ |
| Physics-only model | ✓ | ✓ | N/A (no learning) | ✓ |
| **Energy-regularized neural** | **✓** | **✓** | **Medium** | **Soft** |
| Constrained GP dynamics | ✓ | ✓ | Low | Soft |
| Hybrid physics-NN (no energy reg) | Partial | Partial | Medium | ✗ |

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   OmniDrone Control System               │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────┐    ┌──────────────┐    ┌────────────┐ │
│  │  Reference    │    │  Neural MPC  │    │  Energy    │ │
│  │  Generator    │───▶│  Optimizer   │───▶│  Checker   │ │
│  └──────────────┘    └──────┬───────┘    └─────┬──────┘ │
│                              │                   │       │
│  ┌──────────────┐    ┌───────▼───────┐    ┌─────▼──────┐ │
│  │  Nominal      │    │  Residual     │    │  Safety    │ │
│  │  Dynamics     │◀───│  Dynamics NN  │    │  Monitor   │ │
│  └──────────────┘    │  (Energy Reg) │    └────────────┘ │
│                      └───────────────┘                   │
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │              Training Pipeline                    │   │
│  │  ┌──────────┐  ┌────────────┐  ┌──────────────┐  │   │
│  │  │ Sim Data │─▶│ Energy Reg │─▶│ Fine-tune on │  │   │
│  │  │ Collection│ │ Training   │  │ Real Data    │  │   │
│  │  └──────────┘  └────────────┘  └──────────────┘  │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

## Practical Applications

### Omnidirectional Aerial Robots
- Complex aerodynamic environments (near walls, in tunnels)
- Payload handling with varying mass distribution
- Formation flying with interaction effects
- Aggressive maneuvering beyond linear regime

### General Physical Systems
- Robotic manipulators with unmodeled joint friction
- Autonomous vehicles on varying terrain
- Underwater vehicles with complex hydrodynamics
- Any system where energy conservation is a structural constraint

## Research Context

**arXiv**: 2604.14678v1  
**Title**: Energy-based Regularization for Learning Residual Dynamics in Neural MPC for Omnidirectional Aerial Robots  
**Published**: 2026-04-16  
**Subfield**: energy_dynamics / control

## Related Skills

- **bandwidth-reduction-packetized-mpc**: For networked MPC deployment with communication constraints
- **trajectory-controlled-invariants**: For computing invariant sets that guarantee recursive feasibility in MPC
- **sumo-whole-body-locomanipulation**: For whole-body control of legged robots with sim-to-real transfer
- **pinns-biomedical-modeling**: For physics-informed neural networks in other domains

## Further Reading

- Lagrangian and Hamiltonian mechanics for energy-based modeling
- Robust and tube MPC for guaranteed constraint satisfaction
- Domain randomization for sim-to-real transfer
- Ensemble methods for uncertainty quantification in neural dynamics

---

**Core lesson**: Energy conservation is a universal physical constraint. By regularizing learned dynamics models to respect energy bounds, you gain physically plausible predictions, improved OOD generalization, and safer MPC — especially critical for aerial robots operating in complex environments where prediction errors can be catastrophic.
