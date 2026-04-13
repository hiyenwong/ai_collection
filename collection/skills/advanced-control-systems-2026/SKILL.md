---
name: advanced-control-systems-2026
description: "Advanced control systems methodologies from April 2026 research. Covers discounted MPC under plant-model mismatch, density-driven multi-agent optimal control, data-driven moving horizon estimation, finite-time reachability for constrained systems, and game-theoretic MPC stability analysis. Activation: advanced control, MPC, multi-agent control, state estimation, reachability, game-theoretic control, robust control."
tags: ["control-systems", "MPC", "multi-agent", "state-estimation", "robust-control", "game-theory"]
---

# Advanced Control Systems 2026

Cutting-edge control theory methodologies from April 2026 research, providing practical patterns for robust, adaptive, and scalable control system design.

## Overview

This skill synthesizes five advanced research directions in control systems engineering:

1. **Discounted MPC with Plant-Model Mismatch** - Robust control under model uncertainty using discount factor tuning
2. **Density-Driven Multi-Agent Control** - Scalable coverage and coordination via probability density control
3. **Data-Driven Moving Horizon Estimation** - Learning-based state estimation without system models
4. **Finite-Time Reachability** - Safety-critical control with actuator failure handling
5. **Game-Theoretic MPC Stability Analysis** - Multi-agent strategic decision-making with misspecification robustness

---

## Pattern 1: Discounted MPC Under Plant-Model Mismatch

### Problem Statement

Model Predictive Control (MPC) relies on a surrogate model to predict future behavior. In practice, the model differs from the real plant due to:
- Unmodeled dynamics
- Parameter uncertainties
- Environmental variations
- Simplification for computational tractability

### Core Insight

The discount factor γ ∈ (0, 1] serves as a tuning knob trading off robustness against performance. Lower γ increases robustness to model mismatch but may reduce performance.

### Mathematical Framework

**Finite-horizon discounted MPC:**
```
minimize Σ_{k=0}^{N-1} γ^k * (x_k^T Q x_k + u_k^T R u_k) + γ^N * x_N^T P x_N
subject to:
  x_{k+1} = f_model(x_k, u_k)  [surrogate model]
  x_k ∈ X, u_k ∈ U  [state and input constraints]
```

### Key Theoretical Results

| Discount Factor | Stability Guarantee | Suboptimality Bound |
|----------------|---------------------|---------------------|
| γ = 1 (undiscounted) | Robust stability (standard) | O(ε) where ε is model error |
| γ < 1 (discounted) | Extended stability region | Trade-off: lower γ → more robust |

**Explicit stability bound:**
```
γ ≥ γ_min(ε, L_f, L_V)
```
where:
- ε = model error bound
- L_f = Lipschitz constant of dynamics
- L_V = Lipschitz constant of value function

### Design Guidelines

1. **Start with γ = 1** (standard MPC) if model accuracy is high (< 5% error)
2. **Reduce γ gradually** if instability observed under mismatch
3. **Practical tuning procedure**:
   - Begin with γ = 0.95 for uncertain systems
   - Decrease by 0.05 if instability persists
   - Monitor closed-loop cost increase
4. **Theoretical lower bound**: γ_min = max(0.5, 1 - c·ε) where c is system-dependent

### Implementation

```python
import numpy as np
from scipy.optimize import minimize

class DiscountedMPC:
    """
    Discounted MPC with automatic tuning for plant-model mismatch.
    
    Based on: Moldenhauer et al. (2026). "Discounted MPC and infinite-horizon 
    optimal control under plant-model mismatch." arXiv:2604.08521
    """
    
    def __init__(self, model, horizon=10, discount_factor=0.95, 
                 Q=None, R=None, P=None):
        """
        Args:
            model: Surrogate model with predict(x, u) method
            horizon: Prediction horizon N
            discount_factor: Initial γ value
            Q: State cost matrix
            R: Input cost matrix  
            P: Terminal cost matrix
        """
        self.model = model
        self.N = horizon
        self.gamma = discount_factor
        self.Q = Q if Q is not None else np.eye(model.nx)
        self.R = R if R is not None else np.eye(model.nu)
        self.P = P if P is not None else self.Q
        
    def stage_cost(self, x, u):
        """Quadratic stage cost."""
        return x.T @ self.Q @ x + u.T @ self.R @ u
    
    def terminal_cost(self, x):
        """Quadratic terminal cost."""
        return x.T @ self.P @ x
    
    def solve(self, x0, u_bounds=None):
        """
        Solve discounted MPC problem.
        
        Args:
            x0: Initial state
            u_bounds: Tuple (u_min, u_max) or None
            
        Returns:
            u_opt: Optimal control input
        """
        nu = self.model.nu
        
        # Decision variables: [u_0, u_1, ..., u_{N-1}]
        def objective(U):
            U = U.reshape(self.N, nu)
            cost = 0
            x = x0
            for k in range(self.N):
                cost += (self.gamma ** k) * self.stage_cost(x, U[k])
                x = self.model.predict(x, U[k])
            cost += (self.gamma ** self.N) * self.terminal_cost(x)
            return cost
        
        # Initial guess
        U0 = np.zeros(self.N * nu)
        
        # Bounds
        bounds = None
        if u_bounds is not None:
            u_min, u_max = u_bounds
            bounds = [(u_min, u_max) for _ in range(self.N * nu)]
        
        # Solve
        result = minimize(objective, U0, bounds=bounds, method='SLSQP')
        
        if result.success:
            U_opt = result.x.reshape(self.N, nu)
            return U_opt[0]  # Return first control action
        else:
            raise RuntimeError(f"MPC optimization failed: {result.message}")
    
    def tune_discount_factor(self, model_error_bound, lipschitz_f=None, lipschitz_v=None):
        """
        Auto-tune gamma based on model uncertainty.
        
        Args:
            model_error_bound: Upper bound on model error ε
            lipschitz_f: Lipschitz constant of dynamics (estimated)
            lipschitz_v: Lipschitz constant of value function (estimated)
        """
        # Theoretical bound: gamma >= 1 - c * epsilon
        # Conservative estimate: c ≈ 0.1 for typical systems
        c = 0.1 if lipschitz_f is None else 1.0 / (2 * lipschitz_f)
        
        gamma_min = max(0.5, 1 - c * model_error_bound)
        self.gamma = min(1.0, gamma_min + 0.1)  # Add 10% margin
        
        return self.gamma
    
    def simulate_closed_loop(self, x0, true_dynamics, T_sim):
        """
        Simulate closed-loop with plant-model mismatch.
        
        Args:
            x0: Initial state
            true_dynamics: Function true_dynamics(x, u) for real plant
            T_sim: Simulation horizon
            
        Returns:
            X: State trajectory
            U: Control trajectory
            costs: Stage costs
        """
        X = [x0]
        U = []
        costs = []
        
        x = x0
        for t in range(T_sim):
            u = self.solve(x)
            U.append(u)
            costs.append(self.stage_cost(x, u))
            
            # Apply to true dynamics (with mismatch)
            x = true_dynamics(x, u)
            X.append(x)
        
        return np.array(X), np.array(U), np.array(costs)
```

### When to Apply

- **Model uncertainty > 10%**: Significant parameter error or unmodeled dynamics
- **Computational constraints**: Cannot afford robust MPC formulations
- **Adaptive control**: Model updated online, uncertainty varies
- **Safety-critical systems**: Require stability guarantees despite mismatch

### References

- Moldenhauer, R. H., Worthmann, K., Postoyan, R., et al. (2026). "Discounted MPC and infinite-horizon optimal control under plant-model mismatch: Stability and suboptimality." *arXiv:2604.08521*

---

## Pattern 2: Density-Driven Optimal Control for Multi-Agent Systems

### Problem Statement

Multi-agent area coverage and coordination face:
- Curse of dimensionality with many agents
- Need for decentralized computation
- Stochastic disturbances (wind, sensor noise)
- Non-uniform priority regions

### Core Insight

Control the probability density of agents rather than individual trajectories. The Fokker-Planck equation governs density evolution under stochastic dynamics.

### Mathematical Framework

**Agent dynamics** (stochastic LTI):
```
dx_i = A x_i dt + B u_i dt + σ dW_i
```

**Fokker-Planck equation** for density evolution:
```
∂ρ/∂t = -∇·(ρ(Ax + Bu)) + (σ²/2)Δρ
```

**Optimal control problem**:
```
minimize ∫_0^T ∫ ||ρ(x,t) - ρ_desired(x)||² dx dt + ∫_0^T ||u||²_R dt
```

### Key Advantages

| Aspect | Traditional Methods | Density-Driven |
|--------|---------------------|----------------|
| Scalability | O(n^d) with n agents | O(1) - density field |
| Decentralization | Central planner | Local density feedback |
| Stochastic handling | Scenario-based | Natural via Fokker-Planck |
| Convergence | Heuristic | Provable guarantees |

### Convergence Guarantees

For stochastic LTI systems with control-affine dynamics:

1. **Global convergence**: ρ(x,t) → ρ_desired(x) as t → ∞
2. **Convergence rate**: Exponential with rate λ_min(Q) / (2σ²)
3. **Bounded control**: ||u|| ≤ u_max ensures feasibility

### Implementation

```python
import numpy as np
from scipy.stats import gaussian_kde
from scipy.ndimage import gaussian_filter

class DensityDrivenControl:
    """
    Density-driven optimal control for multi-agent coverage.
    
    Based on: Lee (2026). "Density-Driven Optimal Control: Convergence Guarantees 
    for Stochastic LTI Multi-Agent Systems." arXiv:2604.08495
    """
    
    def __init__(self, A, B, sigma, desired_density_func, 
                 control_gain=1.0, u_max=1.0):
        """
        Args:
            A: System matrix (nx x nx)
            B: Input matrix (nx x nu)
            sigma: Noise intensity (scalar or vector)
            desired_density_func: Function ρ_des(x) returning desired density
            control_gain: Gain matrix or scalar
            u_max: Control input bound
        """
        self.A = A
        self.B = B
        self.sigma = sigma
        self.rho_desired = desired_density_func
        self.u_max = u_max
        
        if np.isscalar(control_gain):
            self.K = control_gain * np.eye(B.shape[1])
        else:
            self.K = control_gain
    
    def compute_density(self, agent_positions, grid_points=None, bandwidth=None):
        """
        Estimate current density field from agent positions.
        
        Args:
            agent_positions: Array of shape (n_agents, n_dims)
            grid_points: Grid for density evaluation (optional)
            bandwidth: KDE bandwidth (default: Scott's rule)
            
        Returns:
            rho: Density field evaluated at grid_points
            grid: Grid coordinates
        """
        if bandwidth is None:
            # Scott's rule: bandwidth ∝ n^(-1/(d+4))
            n, d = agent_positions.shape
            bandwidth = n ** (-1.0 / (d + 4))
        
        if grid_points is None:
            # Create grid based on data range
            mins = agent_positions.min(axis=0) - 2 * bandwidth
            maxs = agent_positions.max(axis=0) + 2 * bandwidth
            grids = [np.linspace(mins[i], maxs[i], 50) for i in range(agent_positions.shape[1])]
            grid_points = np.stack(np.meshgrid(*grids), axis=-1)
        
        # Kernel density estimation
        kde = gaussian_kde(agent_positions.T, bw_method=bandwidth)
        
        # Evaluate on grid
        shape = grid_points.shape[:-1]
        flat_grid = grid_points.reshape(-1, grid_points.shape[-1])
        rho = kde(flat_grid.T).reshape(shape)
        
        return rho, grid_points
    
    def compute_density_gradient(self, rho, grid_spacing):
        """Compute gradient of density field."""
        return np.gradient(rho, *grid_spacing)
    
    def optimal_control_law(self, x, rho_x, grad_rho_x):
        """
        Compute control using density gradient.
        
        Control law: u = -K * ∇(log ρ - log ρ_des)
        """
        # Evaluate desired density at current position
        rho_des_x = self.rho_desired(x)
        
        # Density error in log space
        density_error = np.log(rho_x + 1e-10) - np.log(rho_des_x + 1e-10)
        
        # Control law
        u = -self.K @ (grad_rho_x * density_error)
        
        # Clip to bounds
        return np.clip(u, -self.u_max, self.u_max)
    
    def coverage_controller(self, agents, dt=0.01):
        """
        Main control loop for coverage.
        
        Args:
            agents: List of agent objects with position attribute
            dt: Time step
            
        Returns:
            controls: Control inputs for each agent
        """
        positions = np.array([agent.position for agent in agents])
        
        # Compute density field
        rho, grid = self.compute_density(positions)
        
        # Compute gradient
        grid_spacing = [grid[1, 0, 0] - grid[0, 0, 0] if grid.ndim > 2 
                       else grid[1] - grid[0]]
        grad_rho = self.compute_density_gradient(rho, grid_spacing)
        
        # Compute control for each agent
        controls = []
        for agent in agents:
            # Interpolate density and gradient at agent position
            rho_x = self.interpolate_field(rho, grid, agent.position)
            grad_rho_x = self.interpolate_field(grad_rho, grid, agent.position)
            
            u = self.optimal_control_law(agent.position, rho_x, grad_rho_x)
            controls.append(u)
        
        return controls
    
    def interpolate_field(self, field, grid, position):
        """Interpolate field value at position."""
        from scipy.interpolate import interpn
        
        # Create coordinate arrays
        if grid.ndim == 2:
            coords = (grid,)
        else:
            coords = tuple(grid[..., i] for i in range(grid.shape[-1]))
        
        return interpn(coords, field, position, bounds_error=False, fill_value=0)
    
    def simulate_coverage(self, initial_positions, T_final, dt=0.01):
        """
        Simulate coverage control.
        
        Args:
            initial_positions: Initial agent positions (n_agents, n_dims)
            T_final: Final simulation time
            dt: Time step
            
        Returns:
            trajectory: Agent positions over time
        """
        positions = np.array(initial_positions)
        n_agents, n_dims = positions.shape
        n_steps = int(T_final / dt)
        
        trajectory = np.zeros((n_steps, n_agents, n_dims))
        
        for t in range(n_steps):
            trajectory[t] = positions.copy()
            
            # Compute controls
            rho, grid = self.compute_density(positions)
            grid_spacing = [grid[1, 0] - grid[0, 0] if grid.ndim > 1 else grid[1] - grid[0]]
            grad_rho = self.compute_density_gradient(rho, grid_spacing)
            
            # Update positions
            for i in range(n_agents):
                rho_x = self.interpolate_field(rho, grid, positions[i])
                grad_rho_x = self.interpolate_field(grad_rho, grid, positions[i])
                
                u = self.optimal_control_law(positions[i], rho_x, grad_rho_x)
                
                # Euler integration with noise
                dx = self.A @ positions[i] + self.B @ u
                if np.isscalar(self.sigma):
                    noise = self.sigma * np.sqrt(dt) * np.random.randn(n_dims)
                else:
                    noise = self.sigma * np.sqrt(dt) * np.random.randn(n_dims)
                
                positions[i] += dx * dt + noise
        
        return trajectory
```

### Use Cases

- **Search and rescue**: Non-uniform coverage of priority areas
- **Environmental monitoring**: Adaptive sampling with varying importance
- **Warehouse robotics**: Distributed coordination without central planner
- **Drone swarms**: Formation control with collision avoidance

### References

- Lee, K. (2026). "Density-Driven Optimal Control: Convergence Guarantees for Stochastic LTI Multi-Agent Systems." *arXiv:2604.08495*

---

## Pattern 3: Data-Driven Moving Horizon Estimation

### Problem Statement

State estimation traditionally requires:
- Accurate system model (A, B, C matrices)
- Knowledge of noise statistics
- Offline system identification

In many applications, models are unavailable or inaccurate.

### Core Insight

Use historical input-output data to learn the estimation mapping directly, without explicit system identification.

### Mathematical Framework

**Data-driven MHE optimization**:
```
minimize Σ_{k=t-N}^{t} ||y_k - ŷ_k||²_Q + ||u_k - û_k||²_R
subject to:
  [ŷ; û] = Φ([past inputs/outputs])  [learned mapping]
```

### Sample Complexity

For N offline samples and horizon T:
- **Estimation error**: O(1/√N + σ√(T/N))
- **Sample requirement**: N = O(T/ε²) for ε-accuracy
- **Convergence rate**: Non-asymptotic bounds available

### Implementation

```python
import numpy as np
from scipy.linalg import solve

class DataDrivenMHE:
    """
    Data-Driven Moving Horizon Estimator.
    
    Based on: Duan et al. (2026). "Data-Driven Moving Horizon Estimators 
    for Linear Systems with Sample Complexity Analysis." arXiv:2604.08328
    """
    
    def __init__(self, horizon, feature_dim=None, regularization=0.01):
        """
        Args:
            horizon: Estimation horizon T
            feature_dim: Feature dimension (auto-detected if None)
            regularization: Ridge regularization parameter
        """
        self.T = horizon
        self.d = feature_dim
        self.lambda_reg = regularization
        self.Theta = None  # Learned parameters
        self.is_trained = False
    
    def build_feature_matrix(self, inputs, outputs, T_window=None):
        """
        Build feature matrix from I/O data.
        
        Features: [u_{t-T}, ..., u_t, y_{t-T}, ..., y_t]
        
        Args:
            inputs: Input sequence (n_samples, nu)
            outputs: Output sequence (n_samples, ny)
            T_window: Feature window (default: self.T)
            
        Returns:
            X: Feature matrix (n_samples - T, d)
            Y: Target outputs (n_samples - T, ny)
        """
        if T_window is None:
            T_window = self.T
        
        n_samples = len(inputs)
        nu = inputs.shape[1] if inputs.ndim > 1 else 1
        ny = outputs.shape[1] if outputs.ndim > 1 else 1
        
        self.d = 2 * T_window * nu  # Feature dimension
        
        X = []
        Y = []
        
        for t in range(T_window, n_samples):
            # Feature: past T inputs and outputs
            u_feat = inputs[t-T_window:t].flatten()
            y_feat = outputs[t-T_window:t].flatten()
            feature = np.concatenate([u_feat, y_feat])
            
            X.append(feature)
            Y.append(outputs[t])
        
        return np.array(X), np.array(Y)
    
    def train(self, inputs, outputs, validation_split=0.2):
        """
        Learn estimation mapping from data.
        
        Args:
            inputs: Training inputs (n_samples, nu)
            outputs: Training outputs (n_samples, ny)
            validation_split: Fraction for validation
        """
        # Build feature matrix
        X, Y = self.build_feature_matrix(inputs, outputs)
        
        # Split data
        n_val = int(len(X) * validation_split)
        X_train, X_val = X[:-n_val], X[-n_val:]
        Y_train, Y_val = Y[:-n_val], Y[-n_val:]
        
        # Ridge regression
        XtX = X_train.T @ X_train
        XtY = X_train.T @ Y_train
        
        self.Theta = solve(XtX + self.lambda_reg * np.eye(XtX.shape[0]), 
                          XtY, assume_a='pos')
        
        # Validate
        Y_pred = X_val @ self.Theta
        self.validation_error = np.mean((Y_val - Y_pred) ** 2)
        
        self.is_trained = True
        
        return self.validation_error
    
    def estimate(self, recent_inputs, recent_outputs):
        """
        Online state/output estimation.
        
        Args:
            recent_inputs: Recent T inputs
            recent_outputs: Recent T outputs
            
        Returns:
            y_hat: Predicted output
        """
        if not self.is_trained:
            raise RuntimeError("Estimator not trained. Call train() first.")
        
        # Form feature vector
        feature = np.concatenate([
            np.array(recent_inputs).flatten(),
            np.array(recent_outputs).flatten()
        ])
        
        # Predict
        y_hat = self.Theta.T @ feature
        
        return y_hat
    
    def moving_horizon_estimate(self, data_buffer, refine_online=True):
        """
        Full MHE with learned model.
        
        Args:
            data_buffer: Buffer containing recent I/O data
            refine_online: Whether to refine with online data
            
        Returns:
            x_hat: Estimated state/output
        """
        # Extract recent window
        window = data_buffer[-self.T:]
        
        # Solve optimization using learned mapping
        y_hat = self.estimate(window.inputs, window.outputs)
        
        if refine_online:
            # Refine with online data
            y_hat = self.online_update(y_hat, window)
        
        return y_hat
    
    def online_update(self, y_hat, window, learning_rate=0.01):
        """
        Online refinement of estimate.
        
        Args:
            y_hat: Initial estimate
            window: Recent data window
            learning_rate: Update rate
            
        Returns:
            y_refined: Refined estimate
        """
        # Simple gradient descent refinement
        # In practice, use more sophisticated methods
        prediction_error = window.outputs[-1] - y_hat
        y_refined = y_hat + learning_rate * prediction_error
        
        return y_refined
    
    def sample_complexity_bound(self, epsilon, delta, sigma_noise):
        """
        Compute sample complexity bound.
        
        Args:
            epsilon: Desired accuracy
            delta: Confidence level
            sigma_noise: Noise standard deviation
            
        Returns:
            N_min: Minimum number of samples required
        """
        # From theory: N = O(T/ε²)
        d = self.d if self.d is not None else 2 * self.T
        
        # Conservative bound
        N_min = int(np.ceil(
            (sigma_noise ** 2 * d * np.log(1/delta)) / (epsilon ** 2)
        ))
        
        return N_min
```

### When to Apply

- **Unknown dynamics**: System model unavailable
- **Time-varying systems**: Model changes over time
- **Complex systems**: First-principles modeling intractable
- **Data-rich environments**: Abundant historical data available

### References

- Duan, P., He, J., Lv, Y., et al. (2026). "Data-Driven Moving Horizon Estimators for Linear Systems with Sample Complexity Analysis." *arXiv:2604.08328*

---

## Pattern 4: Finite-Time Reachability for Constrained Systems

### Problem Statement

Safety-critical control requires:
- Guaranteed reachability to safe states
- Handling actuator failures (partial control loss)
- State and input constraints
- Real-time computation

### Core Insight

Use constrained controllability Gramian to characterize reachable set and plan recovery trajectories. Linear programs over the Gramian enable efficient computation.

### Mathematical Framework

**Constrained controllability Gramian**:
```
W_c(T) = ∫_0^T e^{Aτ} B R^{-1} B^T e^{A^T τ} dτ
```

**Reachability condition**:
```
x_target ∈ R(x0, T) iff 
  (x_target - e^{AT}x0)^T W_c(T)^{-1} (x_target - e^{AT}x0) ≤ 1
  AND
  constraints satisfied along trajectory
```

**With partial control loss**: Partition B = [B_available | B_failed]
```
W_c_available(T) = ∫_0^T e^{Aτ} B_available R^{-1} B_available^T e^{A^T τ} dτ
```

### Key Results

1. **Finite-time guarantee**: If reachable, time bound T* is explicit
2. **Constraint satisfaction**: Linear program ensures feasibility
3. **Partial control**: Reduced reachable set characterized analytically

### Implementation

```python
import numpy as np
from scipy.linalg import expm, solve
from scipy.optimize import linprog

class FiniteTimeReachability:
    """
    Finite-time reachability control for constrained systems with partial control loss.
    
    Based on: Padmanabhan & Ornik (2026). "Finite-time Reachability for Constrained, 
    Partially Uncontrolled Nonlinear Systems." arXiv:2604.08327
    """
    
    def __init__(self, A, B, Q=None, R=None, 
                 state_constraints=None, input_constraints=None):
        """
        Args:
            A: System matrix (nx x nx)
            B: Input matrix (nx x nu)
            Q: State weighting matrix
            R: Input weighting matrix
            state_constraints: Tuple (x_min, x_max) or None
            input_constraints: Tuple (u_min, u_max) or None
        """
        self.A = A
        self.B = B
        self.nx = A.shape[0]
        self.nu = B.shape[1]
        
        self.Q = Q if Q is not None else np.eye(self.nx)
        self.R = R if R is not None else np.eye(self.nu)
        
        self.state_constraints = state_constraints
        self.input_constraints = input_constraints
    
    def compute_gramian(self, T, B_subset=None, n_points=100):
        """
        Compute controllability Gramian.
        
        Args:
            T: Time horizon
            B_subset: Subset of input matrix (for partial control)
            n_points: Integration points
            
        Returns:
            W: Controllability Gramian
        """
        B_eff = B_subset if B_subset is not None else self.B
        
        # Numerical integration
        W = np.zeros((self.nx, self.nx))
        dt = T / n_points
        
        for i in range(n_points):
            tau = i * dt
            eAt = expm(self.A * tau)
            integrand = eAt @ B_eff @ np.linalg.inv(self.R) @ B_eff.T @ eAt.T
            W += integrand * dt
        
        return W
    
    def check_reachability(self, x0, x_target, T, failed_actuators=None):
        """
        Check if x_target is reachable from x0 in time T.
        
        Args:
            x0: Initial state
            x_target: Target state
            T: Time horizon
            failed_actuators: List of failed actuator indices
            
        Returns:
            reachable: Boolean
            control: Control function u(t) or None
        """
        # Handle partial control loss
        if failed_actuators is not None and len(failed_actuators) > 0:
            B_available = np.delete(self.B, failed_actuators, axis=1)
            R_available = np.delete(np.delete(self.R, failed_actuators, axis=0), 
                                   failed_actuators, axis=1)
        else:
            B_available = self.B
            R_available = self.R
        
        # Compute reduced Gramian
        W = self.compute_gramian(T, B_available)
        
        # Check reachability condition
        eAT = expm(self.A * T)
        delta = x_target - eAT @ x0
        
        # Ellipsoid condition: delta^T W^{-1} delta <= 1
        try:
            W_inv = np.linalg.inv(W)
            reachability_metric = delta.T @ W_inv @ delta
            
            if reachability_metric <= 1.0:
                # Compute optimal control
                control = self._compute_control_function(
                    x0, x_target, T, W, B_available, R_available
                )
                return True, control
        except np.linalg.LinAlgError:
            pass
        
        return False, None
    
    def _compute_control_function(self, x0, x_target, T, W, B_avail, R_avail):
        """
        Compute minimum-energy control as a function of time.
        
        Returns a function u(t) that can be evaluated at any time.
        """
        eAT = expm(self.A * T)
        delta = x_target - eAT @ x0
        W_inv = np.linalg.inv(W)
        
        def u_optimal(t):
            """Optimal control at time t."""
            eA_T_t = expm(self.A.T * (T - t))
            u = np.linalg.inv(R_avail) @ B_avail.T @ eA_T_t @ W_inv @ delta
            
            # Apply input constraints if provided
            if self.input_constraints is not None:
                u_min, u_max = self.input_constraints
                u = np.clip(u, u_min, u_max)
            
            return u
        
        return u_optimal
    
    def find_minimum_time(self, x0, x_target, T_max=100, tolerance=0.1, 
                         failed_actuators=None):
        """
        Find minimum time to reach target using binary search.
        
        Args:
            x0: Initial state
            x_target: Target state
            T_max: Maximum time to search
            tolerance: Time precision
            failed_actuators: List of failed actuator indices
            
        Returns:
            T_min: Minimum time (None if not reachable within T_max)
            control: Optimal control function
        """
        T_low, T_high = 0, T_max
        
        while T_high - T_low > tolerance:
            T = (T_low + T_high) / 2
            reachable, control = self.check_reachability(
                x0, x_target, T, failed_actuators
            )
            
            if reachable:
                T_high = T
                best_control = control
            else:
                T_low = T
        
        # Final check
        reachable, control = self.check_reachability(
            x0, x_target, T_high, failed_actuators
        )
        
        if reachable:
            return T_high, control
        else:
            return None, None
    
    def generate_recovery_plan(self, x0, safe_states, failed_actuators=None):
        """
        Generate recovery plan to nearest safe state.
        
        Args:
            x0: Current state (after failure)
            safe_states: List of safe target states
            failed_actuators: List of failed actuator indices
            
        Returns:
            plan: Dict with target, time, and control function
        """
        best_plan = None
        min_time = float('inf')
        
        for x_safe in safe_states:
            T, control = self.find_minimum_time(x0, x_safe, 
                                               failed_actuators=failed_actuators)
            if T is not None and T < min_time:
                min_time = T
                best_plan = {
                    'target': x_safe,
                    'time': T,
                    'control': control
                }
        
        return best_plan
    
    def simulate_recovery(self, x0, x_target, T, control_func, 
                         true_dynamics=None, dt=0.01):
        """
        Simulate recovery trajectory.
        
        Args:
            x0: Initial state
            x_target: Target state
            T: Time horizon
            control_func: Control function u(t)
            true_dynamics: True dynamics (if different from model)
            dt: Time step
            
        Returns:
            trajectory: State trajectory
            controls: Control inputs
        """
        if true_dynamics is None:
            true_dynamics = lambda x, u: self.A @ x + self.B @ u
        
        n_steps = int(T / dt)
        trajectory = [x0]
        controls = []
        
        x = x0
        for i in range(n_steps):
            t = i * dt
            u = control_func(t)
            controls.append(u)
            
            # Integrate
            dx = true_dynamics(x, u)
            x = x + dx * dt
            trajectory.append(x)
        
        return np.array(trajectory), np.array(controls)
```

### Applications

- **Aircraft control**: Recovery from actuator failures
- **Autonomous vehicles**: Emergency maneuvering
- **Robotic systems**: Fault-tolerant operation
- **Process control**: Safe shutdown procedures

### References

- Padmanabhan, R., & Ornik, M. (2026). "Finite-time Reachability for Constrained, Partially Uncontrolled Nonlinear Systems." *arXiv:2604.08327*

---

## Pattern 5: Game-Theoretic MPC Stability Analysis

### Problem Statement

Multi-agent systems with self-interested agents require:
- Strategic decision-making under objective uncertainty
- Stability guarantees despite model misspecification
- Handling of emergent collective behavior
- Robustness to adversarial behavior

### Core Insight

Quantify and bound the impact of objective misspecification on closed-loop stability using sensitivity analysis and small-gain conditions.

### Mathematical Framework

**Agent i's MPC problem**:
```
minimize J_i(x, u_i, u_{-i}^predicted)
subject to: dynamics and constraints
```

**Objective misspecification**: Agent j's true objective J_j differs from agent i's prediction Ĵ_j

**Sensitivity bound**:
```
||u_j^actual - u_j^predicted|| ≤ L * ||J_j - Ĵ_j||
```

where L is the Lipschitz constant of the Nash equilibrium mapping.

### Stability Conditions

For stability under objective misspecification:

1. **Small-gain condition**: 
   ```
   γ_1 * γ_2 * ... * γ_n < 1
   ```
   where γ_i is the sensitivity of agent i to prediction errors

2. **Bounded misspecification**:
   ```
   ||J_j - Ĵ_j|| ≤ ε_max for all j
   ```

3. **Robustness margin**:
   ```
   ε_max < (1 - Π γ_i) / (Σ L_i)
   ```

### Implementation

```python
import numpy as np
from scipy.optimize import minimize

class GameTheoreticMPC:
    """
    Game-theoretic MPC with stability analysis under objective misspecification.
    
    Based on: Yildirim & Ferguson (2026). "Stability and Sensitivity Analysis 
    for Objective Misspecifications Among Model Predictive Game Controllers." 
    arXiv:2604.08303
    """
    
    def __init__(self, agents, horizon=10, max_iterations=100, tolerance=1e-3):
        """
        Args:
            agents: List of Agent objects
            horizon: MPC prediction horizon
            max_iterations: Max iterations for Nash equilibrium
            tolerance: Convergence tolerance
        """
        self.agents = agents
        self.N = horizon
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.sensitivity_bounds = {}
        self.lipschitz_constants = {}
    
    def solve_agent_mpc(self, agent, predicted_others):
        """
        Solve MPC for a single agent given predictions of other agents.
        
        Args:
            agent: Agent object
            predicted_others: Dict {agent_id: predicted_trajectory}
            
        Returns:
            u_opt: Optimal control for agent
        """
        def objective(u):
            return agent.cost_function(u, predicted_others)
        
        def constraint(u):
            return agent.dynamics_constraint(u, predicted_others)
        
        # Solve
        u0 = np.zeros(agent.nu * self.N)
        result = minimize(objective, u0, method='SLSQP',
                         constraints={'type': 'eq', 'fun': constraint},
                         bounds=agent.control_bounds)
        
        return result.x[:agent.nu] if result.success else None
    
    def compute_nash_equilibrium(self, initial_predictions=None):
        """
        Solve for Nash equilibrium via iterative best response.
        
        Args:
            initial_predictions: Initial strategy guesses
            
        Returns:
            equilibrium: Dict {agent_id: optimal_control}
            converged: Boolean
        """
        if initial_predictions is None:
            predictions = {agent.id: np.zeros(agent.nu) for agent in self.agents}
        else:
            predictions = initial_predictions.copy()
        
        for iteration in range(self.max_iterations):
            new_strategies = {}
            
            for agent in self.agents:
                # Get predictions for other agents
                others_pred = {k: v for k, v in predictions.items() if k != agent.id}
                
                # Solve best response
                u_i = self.solve_agent_mpc(agent, others_pred)
                new_strategies[agent.id] = u_i
            
            # Check convergence
            converged = True
            for agent in self.agents:
                if predictions[agent.id] is None or new_strategies[agent.id] is None:
                    converged = False
                    break
                diff = np.linalg.norm(new_strategies[agent.id] - predictions[agent.id])
                if diff > self.tolerance:
                    converged = False
                    break
            
            if converged:
                return new_strategies, True
            
            predictions = new_strategies
        
        return predictions, False
    
    def compute_sensitivity(self, agent):
        """
        Compute sensitivity bound γ_i for an agent.
        
        Sensitivity measures how much agent's control changes
        in response to prediction errors.
        """
        # Estimate via finite differences
        epsilon = 1e-4
        
        # Baseline
        baseline_pred = {a.id: np.zeros(a.nu) for a in self.agents if a.id != agent.id}
        u_baseline = self.solve_agent_mpc(agent, baseline_pred)
        
        # Perturb each other agent
        max_sensitivity = 0
        for other in self.agents:
            if other.id == agent.id:
                continue
            
            perturbed_pred = baseline_pred.copy()
            perturbed_pred[other.id] = epsilon * np.ones(other.nu)
            
            u_perturbed = self.solve_agent_mpc(agent, perturbed_pred)
            
            if u_baseline is not None and u_perturbed is not None:
                sensitivity = np.linalg.norm(u_perturbed - u_baseline) / epsilon
                max_sensitivity = max(max_sensitivity, sensitivity)
        
        self.sensitivity_bounds[agent.id] = max_sensitivity
        return max_sensitivity
    
    def compute_all_sensitivities(self):
        """Compute sensitivity bounds for all agents."""
        for agent in self.agents:
            self.compute_sensitivity(agent)
        return self.sensitivity_bounds
    
    def check_stability(self, objective_errors):
        """
        Check stability under objective misspecification.
        
        Args:
            objective_errors: Dict {agent_id: error_magnitude}
            
        Returns:
            stable: Boolean
            margin: Robustness margin
            message: Description
        """
        # Compute sensitivities if not already done
        if not self.sensitivity_bounds:
            self.compute_all_sensitivities()
        
        # Check small-gain condition
        gamma_product = 1
        for gamma in self.sensitivity_bounds.values():
            gamma_product *= gamma
        
        if gamma_product >= 1:
            return False, 0, "Small-gain condition violated: γ_product >= 1"
        
        # Compute robustness margin
        L_sum = sum(self.lipschitz_constants.values()) if self.lipschitz_constants else 1.0
        epsilon_max = (1 - gamma_product) / max(L_sum, 1e-6)
        
        # Check if actual errors are within bounds
        max_error = max(objective_errors.values())
        
        if max_error <= epsilon_max:
            return True, epsilon_max - max_error, (
                f"Stable: error {max_error:.4f} <= margin {epsilon_max:.4f}"
            )
        else:
            return False, epsilon_max - max_error, (
                f"Unstable: error {max_error:.4f} > margin {epsilon_max:.4f}"
            )
    
    def robust_mpc_step(self, state, objective_uncertainty):
        """
        Execute MPC step with robustness check.
        
        Args:
            state: Current system state
            objective_uncertainty: Dict {agent_id: uncertainty_estimate}
            
        Returns:
            controls: Dict {agent_id: control}
            stable: Whether system is stable
        """
        # Check stability
        stable, margin, msg = self.check_stability(objective_uncertainty)
        
        if not stable:
            # Fall back to conservative control
            return self.conservative_control(state), False
        
        # Compute Nash equilibrium
        equilibrium, converged = self.compute_nash_equilibrium()
        
        if not converged:
            return self.conservative_control(state), False
        
        return equilibrium, True
    
    def conservative_control(self, state):
        """Fallback conservative control when stability uncertain."""
        # Simple proportional control to origin
        controls = {}
        for agent in self.agents:
            K = agent.conservative_gain if hasattr(agent, 'conservative_gain') else 0.1
            controls[agent.id] = -K * state[:agent.nu]
        return controls
```

### Applications

- **Autonomous intersection management**: Vehicles with private objectives
- **Robotic warehouse coordination**: Agents optimizing individual tasks
- **Traffic flow control**: Self-interested drivers
- **Economic dispatch**: Power generators with private cost functions

### References

- Yildirim, A., & Ferguson, B. L. (2026). "Stability and Sensitivity Analysis for Objective Misspecifications Among Model Predictive Game Controllers." *arXiv:2604.08303*

---

## Cross-Cutting Principles

### 1. Robustness-Performance Trade-offs

All patterns involve explicit trade-offs:
- **Discounted MPC**: γ controls robustness vs. performance
- **Density-driven**: Exploration vs. exploitation in coverage
- **Data-driven**: Bias vs. variance in estimation
- **Reachability**: Time vs. energy optimality
- **Game-theoretic**: Individual vs. collective optimality

### 2. Computational Tractability

Each pattern provides computational advantages:
- Linear programs instead of nonlinear optimization
- Decentralized computation vs. centralized
- Learning-based approximations
- Analytical bounds vs. numerical search

### 3. Theoretical Guarantees

All patterns come with provable properties:
- Stability under specified conditions
- Convergence rates
- Sample complexity bounds
- Robustness margins

---

## Selection Guide

| Problem Characteristic | Recommended Pattern |
|------------------------|---------------------|
| Model uncertainty > 10% | Discounted MPC |
| Many agents (>10) | Density-driven control |
| Unknown dynamics | Data-driven MHE |
| Actuator failures | Finite-time reachability |
| Strategic agents | Game-theoretic MPC |
| Safety-critical + uncertain | Combine: Discounted MPC + Reachability |
| Distributed + data-limited | Combine: Density-driven + Data-driven |

---

## Implementation Checklist

Before applying any pattern:

- [ ] Identify system characteristics (linearity, constraints, uncertainty)
- [ ] Verify assumptions match pattern requirements
- [ ] Check computational resources vs. real-time requirements
- [ ] Validate theoretical guarantees apply to your problem
- [ ] Plan for fallback strategies if assumptions violated
- [ ] Test on simulation before deployment
- [ ] Monitor performance metrics and stability indicators

---

## References

### Papers Synthesized

1. Moldenhauer, R. H., Worthmann, K., Postoyan, R., et al. (2026). "Discounted MPC and infinite-horizon optimal control under plant-model mismatch: Stability and suboptimality." *arXiv:2604.08521*

2. Lee, K. (2026). "Density-Driven Optimal Control: Convergence Guarantees for Stochastic LTI Multi-Agent Systems." *arXiv:2604.08495*

3. Duan, P., He, J., Lv, Y., et al. (2026). "Data-Driven Moving Horizon Estimators for Linear Systems with Sample Complexity Analysis." *arXiv:2604.08328*

4. Padmanabhan, R., & Ornik, M. (2026). "Finite-time Reachability for Constrained, Partially Uncontrolled Nonlinear Systems." *arXiv:2604.08327*

5. Yildirim, A., & Ferguson, B. L. (2026). "Stability and Sensitivity Analysis for Objective Misspecifications Among Model Predictive Game Controllers." *arXiv:2604.08303*

### Foundational Texts

- Rawlings, J. B., & Mayne, D. Q. (2017). *Model Predictive Control: Theory and Design*. Nob Hill Publishing.
- Bullo, F. (2022). *Lectures on Network Systems*. Kindle Direct Publishing.
- Bertsekas, D. P. (2017). *Dynamic Programming and Optimal Control* (4th ed.). Athena Scientific.

---

## Activation Keywords

- advanced control
- model predictive control
- MPC
- multi-agent control
- distributed control
- state estimation
- reachability analysis
- game-theoretic control
- robust control
- optimal control
- constrained systems
- actuator failure
- data-driven control
- density-based control
- plant-model mismatch
- moving horizon estimation

## Tools Used

- `execute_code`: Numerical computation and simulation
- `web_search`: Background research and validation
- `read`: Load paper PDFs and documentation
- `write`: Generate implementation code

## Dependencies

```python
numpy       # Linear algebra
scipy       # Optimization, matrix exponentials
cvxpy       # Convex optimization (optional)
matplotlib  # Visualization
```

## Notes

- These patterns represent cutting-edge research from April 2026
- Implementation requires domain expertise in control theory
- Always validate on test cases before production deployment
- Consider computational constraints for real-time applications
- Sample code provided for illustration; production use requires additional error handling and optimization
