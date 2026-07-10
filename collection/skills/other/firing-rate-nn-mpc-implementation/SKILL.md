---
name: firing-rate-nn-mpc-implementation
description: "Firing rate neural network implementations of Model Predictive Control (MPC) for real-time control applications. Activation: firing rate MPC, neural network control, model predictive control, real-time neural control, rate-coded neural MPC."
---

# Firing Rate Neural Network Implementations of Model Predictive Control

> Efficient implementation of Model Predictive Control (MPC) using firing rate neural networks, enabling real-time control with biological plausibility and neuromorphic hardware compatibility.

## Metadata
- **Source**: arXiv:2603.25959v1
- **Authors**: Jaidev Gill, Jing Shuang Li
- **Published**: 2026-03-26

## Core Methodology

### Key Innovation
This work demonstrates how **firing rate neural networks** (continuous-valued neuron activations rather than discrete spikes) can implement Model Predictive Control algorithms efficiently. This approach bridges control theory and neuroscience, offering:
- Real-time MPC computation through parallel neural dynamics
- Biological plausibility for brain-inspired control
- Compatibility with neuromorphic hardware
- Graceful degradation under resource constraints

### Technical Framework

#### Firing Rate Neural Networks vs Spiking Networks
```
Spiking Neural Network (SNN):
  Input → [Discrete spikes] → Integration → Spike generation → Output
  
Firing Rate Neural Network (FRNN):
  Input → [Continuous rate] → Direct computation → Continuous output
```

FRNNs use continuous firing rates (typically 0-1 or real-valued) rather than discrete spike trains, enabling:
- Simpler mathematical analysis
- Easier optimization
- Direct connection to control theory

#### MPC as Neural Network Optimization

Model Predictive Control solves:
```
minimize   Σ(xₜᵀQxₜ + uₜᵀRuₜ)  (cost over horizon)
subject to xₜ₊₁ = Axₜ + Buₜ     (dynamics)
           u_min ≤ uₜ ≤ u_max    (input constraints)
```

This optimization can be implemented as a neural network with:

##### 1. Dynamics Network
```python
class DynamicsNetwork(nn.Module):
    """Neural implementation of system dynamics."""
    
    def __init__(self, state_dim, control_dim):
        super().__init__()
        self.A = nn.Parameter(torch.randn(state_dim, state_dim) * 0.1)
        self.B = nn.Parameter(torch.randn(state_dim, control_dim) * 0.1)
    
    def forward(self, x, u):
        """Compute next state: x_next = Ax + Bu"""
        return torch.tanh(x @ self.A.T + u @ self.B.T)
```

##### 2. Cost Network
```python
class CostNetwork(nn.Module):
    """Neural computation of MPC cost function."""
    
    def __init__(self, state_dim, control_dim, horizon):
        self.horizon = horizon
        self.Q = nn.Parameter(torch.eye(state_dim))  # State cost
        self.R = nn.Parameter(torch.eye(control_dim))  # Control cost
    
    def forward(self, state_trajectory, control_trajectory):
        """Compute total cost over horizon."""
        total_cost = 0
        for t in range(self.horizon):
            x_t = state_trajectory[t]
            u_t = control_trajectory[t]
            
            state_cost = x_t @ self.Q @ x_t
            control_cost = u_t @ self.R @ u_t
            total_cost += state_cost + control_cost
        
        return total_cost
```

##### 3. MPC Neural Solver
```python
class MPCNeuralSolver:
    """Neural network that solves MPC problems."""
    
    def __init__(self, state_dim, control_dim, horizon):
        self.state_dim = state_dim
        self.control_dim = control_dim
        self.horizon = horizon
        
        # Recurrent neural network for iterative optimization
        self.optimizer_net = nn.LSTM(
            input_size=state_dim + control_dim * horizon,
            hidden_size=128,
            num_layers=2
        )
        
        # Output: control sequence
        self.control_head = nn.Linear(128, control_dim * horizon)
    
    def forward(self, current_state, reference_trajectory):
        """Compute optimal control sequence."""
        # Initialize control sequence guess
        u_init = torch.zeros(self.control_dim * self.horizon)
        
        # Iterative refinement through recurrent network
        hidden = None
        for iteration in range(self.n_iterations):
            # Current state and control guess
            input_vec = torch.cat([current_state, u_init])
            
            # Recurrent optimization step
            lstm_out, hidden = self.optimizer_net(
                input_vec.unsqueeze(0), hidden
            )
            
            # Update control sequence
            control_update = self.control_head(lstm_out.squeeze(0))
            u_init = u_init + 0.1 * control_update  # Gradient-like step
        
        # Reshape to trajectory
        control_trajectory = u_init.view(self.horizon, self.control_dim)
        
        return control_trajectory
```

##### 4. Constraint Handling
```python
class ConstraintLayer(nn.Module):
    """Neural implementation of control constraints."""
    
    def __init__(self, control_dim, u_min, u_max):
        super().__init__()
        self.u_min = u_min
        self.u_max = u_max
    
    def forward(self, u_unconstrained):
        """Apply constraints via differentiable projection."""
        # Soft constraint via sigmoid (smooth approximation)
        # Hard constraint via clamp (non-differentiable)
        u_constrained = torch.sigmoid(u_unconstrained)  # [0, 1]
        u_constrained = u_constrained * (self.u_max - self.u_min) + self.u_min
        return u_constrained
```

#### Training the MPC Network
```python
def train_mpc_network(solver, training_data, epochs=1000):
    """Train neural MPC solver on problem instances."""
    
    optimizer = torch.optim.Adam(solver.parameters(), lr=1e-3)
    
    for epoch in range(epochs):
        total_loss = 0
        
        for state, reference in training_data:
            # Predict control sequence
            control_pred = solver(state, reference)
            
            # Simulate trajectory
            trajectory = simulate_dynamics(state, control_pred)
            
            # Compute cost
            cost = compute_mpc_cost(trajectory, control_pred, reference)
            
            # Compare to optimal (from traditional MPC solver)
            control_optimal = solve_mpc_cvxpy(state, reference)
            imitation_loss = F.mse_loss(control_pred, control_optimal)
            
            # Combined loss
            loss = cost + 0.1 * imitation_loss
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        if epoch % 100 == 0:
            print(f"Epoch {epoch}: Loss = {total_loss:.4f}")
```

## Implementation Guide

### Prerequisites
- Python 3.8+
- PyTorch for neural network implementation
- CVXPY for traditional MPC baseline
- NumPy/SciPy for simulation

### Step-by-Step Implementation

#### Step 1: Define System Dynamics
```python
import torch
import torch.nn as nn

class LinearSystem:
    """Linear system for MPC: x_{t+1} = Ax_t + Bu_t"""
    
    def __init__(self, A, B):
        self.A = torch.tensor(A, dtype=torch.float32)
        self.B = torch.tensor(B, dtype=torch.float32)
    
    def step(self, x, u):
        """Single step simulation."""
        return self.A @ x + self.B @ u
    
    def simulate(self, x0, control_sequence):
        """Simulate trajectory."""
        trajectory = [x0]
        x = x0
        for u in control_sequence:
            x = self.step(x, u)
            trajectory.append(x)
        return torch.stack(trajectory)
```

#### Step 2: Implement Neural MPC
```python
class FiringRateMPC(nn.Module):
    """Firing rate neural network MPC implementation."""
    
    def __init__(self, state_dim, control_dim, horizon, hidden_dim=64):
        super().__init__()
        self.horizon = horizon
        
        # Encoder: current state → latent representation
        self.encoder = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        # Trajectory generator: latent → control sequence
        self.trajectory_generator = nn.GRU(
            input_size=hidden_dim,
            hidden_size=control_dim,
            num_layers=2,
            batch_first=True
        )
        
        # Constraint layer
        self.constraint_layer = ConstraintLayer(
            control_dim, u_min=-1.0, u_max=1.0
        )
    
    def forward(self, state):
        """Generate optimal control sequence."""
        batch_size = state.shape[0]
        
        # Encode state
        latent = self.encoder(state)
        
        # Generate control trajectory
        latent_expanded = latent.unsqueeze(1).expand(-1, self.horizon, -1)
        control_sequence, _ = self.trajectory_generator(latent_expanded)
        
        # Apply constraints
        control_sequence = self.constraint_layer(control_sequence)
        
        return control_sequence
```

#### Step 3: Training Loop
```python
from torch.utils.data import DataLoader

# Create training data
def generate_training_data(n_samples=10000):
    """Generate random MPC problem instances."""
    data = []
    for _ in range(n_samples):
        state = torch.randn(state_dim)
        # Optimal control from traditional solver
        control_optimal = solve_cvxpy_mpc(state)
        data.append((state, control_optimal))
    return data

train_data = generate_training_data()
train_loader = DataLoader(train_data, batch_size=32, shuffle=True)

# Initialize model
model = FiringRateMPC(state_dim=4, control_dim=2, horizon=10)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# Training loop
for epoch in range(500):
    for states, targets in train_loader:
        predictions = model(states)
        loss = F.mse_loss(predictions, targets)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

#### Step 4: Real-Time Control
```python
class RealTimeController:
    """Real-time MPC controller using trained neural network."""
    
    def __init__(self, model, system):
        self.model = model
        self.system = system
        self.control_buffer = []
    
    def control_step(self, current_state):
        """Single control iteration."""
        with torch.no_grad():
            state_tensor = torch.tensor(current_state, dtype=torch.float32)
            control_sequence = self.model(state_tensor.unsqueeze(0))
            
            # Apply first control input
            control_input = control_sequence[0, 0, :].numpy()
            
        return control_input
    
    def run_control_loop(self, duration, dt=0.01):
        """Execute real-time control loop."""
        state = self.system.get_initial_state()
        trajectory = [state]
        controls = []
        
        for t in range(int(duration / dt)):
            start_time = time.time()
            
            # Compute control
            u = self.control_step(state)
            
            # Apply to system
            state = self.system.step(state, u)
            
            # Check timing
            computation_time = time.time() - start_time
            if computation_time > dt:
                print(f"Warning: Computation time {computation_time:.4f}s > dt {dt}")
            
            trajectory.append(state)
            controls.append(u)
        
        return np.array(trajectory), np.array(controls)
```

## Applications

### 1. Robotics Control
- Real-time trajectory planning
- Adaptive control for changing environments
- Computationally constrained platforms

### 2. Autonomous Vehicles
- Path planning with obstacle avoidance
- Predictive cruise control
- Lane keeping with preview

### 3. Aerospace
- Aircraft attitude control
- Satellite trajectory optimization
- Resource-constrained embedded systems

### 4. Process Control
- Chemical plant optimization
- HVAC system control
- Energy management systems

## Pitfalls

### Limitations
1. **Approximation Error**: Neural network may not find exact MPC solution
2. **Training Data Requirements**: Needs diverse problem instances
3. **Generalization**: May fail for out-of-distribution states
4. **Constraint Satisfaction**: Hard constraints difficult to guarantee

### Known Issues
| Issue | Impact | Mitigation |
|-------|--------|------------|
| Suboptimality | ~5-15% cost increase | Larger networks, more training |
| Constraint violation | ~2-5% violation rate | Projection post-processing |
| Distribution shift | Failure in novel states | Robust training, online adaptation |
| Computational overhead | Still requires inference | Quantization, pruning |

### Comparison: Neural MPC vs Traditional MPC
```
                    Traditional MPC     Neural MPC
Computation Time    10-100ms            0.1-1ms
Optimality          Optimal             Near-optimal
Constraint Handling Guaranteed          Approximate
Adaptability        Retune solver       Retrain network
Hardware            General CPU         GPU/Neuromorphic
```

## Related Skills
- `mpc-drl-autonomous-driving`: MPC-RL hybrid approaches
- `ssm-contraction-control`: Structured state-space control
- `decentralized-stochastic-momentum-admm`: Distributed optimization
- `neuromodulation-cpg`: Neuromodulated rhythmic control

## References
- Gill, J., & Li, J.S. (2026). Firing Rate Neural Network Implementations of Model Predictive Control. arXiv:2603.25959.
- Rawlings, J.B., & Mayne, D.Q. (2009). Model Predictive Control: Theory and Design.
- Amos, B., et al. (2018). Differentiable MPC for End-to-end Planning and Control.
