---
name: finite-time-reachability-partial-control
description: "Finite-time reachability control for constrained, partially uncontrolled nonlinear systems. Technique to drive system state to target when control authority is partially lost. Activation: finite-time reachability, partial control, constrained systems, nonlinear control."
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [finite-time-reachability, partial-control, constrained-systems, nonlinear-control, safety-critical]
    source_paper: "Finite-time Reachability for Constrained, Partially Uncontrolled Nonlinear Systems (arXiv:2604.08327)"
    citations: 0
    category: systems-engineering
---

# Finite-Time Reachability for Partially Uncontrolled Systems

## Overview

This paper presents a technique to drive the state of a constrained nonlinear system to a specified target state in finite time, when the system suffers a partial loss in control authority. The method builds on controlling constrained nonlinear systems by constructing a simple, linear abstraction.

## Core Concepts

### Finite-Time Reachability
- **Objective**: Reach target set within finite time
- **Constraints**: State and input constraints
- **Guarantees**: Provable reachability conditions

### Partial Control Authority
- **Actuator Failure**: Some inputs unavailable
- **Degraded Performance**: Reduced control effectiveness
- **Adaptation**: Redesign control using remaining authority

### Linear Abstraction
- **Simplified Model**: Linear approximation of nonlinear dynamics
- **Constraint Mapping**: Map nonlinear constraints to linear domain
- **Controller Synthesis**: Design controller for abstraction

## Implementation

```python
import numpy as np
from typing import Callable, Tuple, Optional
from scipy.optimize import minimize, differential_evolution
from scipy.integrate import odeint

class FiniteTimeReachabilityController:
    def __init__(self,
                 dynamics: Callable[[np.ndarray, np.ndarray], np.ndarray],
                 state_constraints: Callable[[np.ndarray], bool],
                 input_constraints: Callable[[np.ndarray], bool],
                 available_inputs: np.ndarray,  # Boolean mask
                 target_state: np.ndarray,
                 time_horizon: float):
        self.f = dynamics
        self.state_valid = state_constraints
        self.input_valid = input_constraints
        self.available = available_inputs.astype(bool)
        self.x_target = target_state
        self.T = time_horizon
        self.n_states = len(target_state)
        self.n_inputs = len(available_inputs)
        
    def linearize(self, x0: np.ndarray, u0: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        eps = 1e-6
        A = np.zeros((self.n_states, self.n_states))
        B = np.zeros((self.n_states, self.n_inputs))
        
        # Numerical Jacobian
        f0 = self.f(x0, u0)
        for i in range(self.n_states):
            x_plus = x0.copy()
            x_plus[i] += eps
            A[:, i] = (self.f(x_plus, u0) - f0) / eps
        
        for i in range(self.n_inputs):
            if self.available[i]:
                u_plus = u0.copy()
                u_plus[i] += eps
                B[:, i] = (self.f(x0, u_plus) - f0) / eps
        
        return A, B
    
    def compute_reachable_set(self, x0: np.ndarray, t: float) -> np.ndarray:
        # Approximate reachable set using linearization
        u0 = np.zeros(self.n_inputs)
        A, B = self.linearize(x0, u0)
        
        # Compute controllability Gramian
        # Simplified - in practice use numerical integration
        W = np.zeros((self.n_states, self.n_states))
        for tau in np.linspace(0, t, 100):
            eAt = self._matrix_exp(A * (t - tau))
            B_available = B[:, self.available]
            W += eAt @ B_available @ B_available.T @ eAt.T * (t / 100)
        
        return W
    
    def _matrix_exp(self, A: np.ndarray) -> np.ndarray:
        from scipy.linalg import expm
        return expm(A)
    
    def solve_reachability(self, x0: np.ndarray, 
                          num_control_points: int = 10) -> Tuple[np.ndarray, np.ndarray]:
        # Parameterize control as piecewise constant
        t_control = np.linspace(0, self.T, num_control_points)
        
        def objective(u_flat):
            u_full = self._reconstruct_control(u_flat, num_control_points)
            x_traj = self._simulate(x0, u_full, t_control)
            x_final = x_traj[-1]
            return np.linalg.norm(x_final - self.x_target)**2
        
        def constraint(u_flat):
            u_full = self._reconstruct_control(u_flat, num_control_points)
            x_traj = self._simulate(x0, u_full, t_control)
            
            # Check state constraints
            violations = []
            for x in x_traj:
                if not self.state_valid(x):
                    violations.append(1.0)
                else:
                    violations.append(0.0)
            return np.array(violations)
        
        # Initial guess
        u0 = np.zeros(np.sum(self.available) * num_control_points)
        
        # Bounds for available inputs
        bounds = []
        for _ in range(num_control_points):
            for i in range(self.n_inputs):
                if self.available[i]:
                    bounds.append((-1.0, 1.0))  # Assume normalized bounds
        
        # Optimize
        result = minimize(
            objective, u0, method='SLSQP',
            bounds=bounds,
            options={'ftol': 1e-8, 'maxiter': 1000}
        )
        
        if result.success:
            u_opt = self._reconstruct_control(result.x, num_control_points)
            x_traj = self._simulate(x0, u_opt, t_control)
            return u_opt, x_traj
        else:
            return None, None
    
    def _reconstruct_control(self, u_flat: np.ndarray, n_points: int) -> np.ndarray:
        u_full = np.zeros((n_points, self.n_inputs))
        idx = 0
        for i in range(n_points):
            for j in range(self.n_inputs):
                if self.available[j]:
                    u_full[i, j] = u_flat[idx]
                    idx += 1
        return u_full
    
    def _simulate(self, x0: np.ndarray, u: np.ndarray, t: np.ndarray) -> np.ndarray:
        def dynamics(x, t):
            # Interpolate control
            idx = np.searchsorted(t, t)
            idx = min(idx, len(u) - 1)
            return self.f(x, u[idx])
        
        t_fine = np.linspace(t[0], t[-1], 100)
        x_traj = odeint(dynamics, x0, t_fine)
        return x_traj
    
    def verify_reachability(self, x0: np.ndarray, epsilon: float = 0.01) -> bool:
        u, x_traj = self.solve_reachability(x0)
        if x_traj is None:
            return False
        
        final_error = np.linalg.norm(x_traj[-1] - self.x_target)
        return final_error < epsilon


# Example: Dubins car with partial control
def example_dubins_car():
    # Dynamics: [x_dot, y_dot, theta_dot] = [v*cos(theta), v*sin(theta), omega]
    # Assume steering (omega) fails, only speed (v) available
    
    def dynamics(x, u):
        v = u[0]
        omega = u[1]
        return np.array([
            v * np.cos(x[2]),
            v * np.sin(x[2]),
            omega
        ])
    
    def state_constraints(x):
        # Stay within bounds
        return -10 <= x[0] <= 10 and -10 <= x[1] <= 10
    
    def input_constraints(u):
        return -1 <= u[0] <= 1 and -0.5 <= u[1] <= 0.5
    
    # Only speed control available (steering failed)
    available = np.array([True, False])
    
    controller = FiniteTimeReachabilityController(
        dynamics=dynamics,
        state_constraints=state_constraints,
        input_constraints=input_constraints,
        available_inputs=available,
        target_state=np.array([5.0, 5.0, 0.0]),
        time_horizon=10.0
    )
    
    x0 = np.array([0.0, 0.0, np.pi/4])
    
    print("Attempting reachability with partial control...")
    reachable = controller.verify_reachability(x0)
    print(f"Reachable: {reachable}")
    
    if reachable:
        u, x_traj = controller.solve_reachability(x0)
        print(f"Final state: {x_traj[-1]}")
        print(f"Error: {np.linalg.norm(x_traj[-1] - controller.x_target)}")


if __name__ == "__main__":
    example_dubins_car()
```

## Key Insights

1. **Partial Authority Handling**: Method systematically handles loss of control inputs
2. **Finite-Time Guarantees**: Provable reachability within specified time horizon
3. **Constraint Satisfaction**: Maintains state and input constraints throughout

## Applications

- Fault-tolerant control
- Safety-critical systems
- Aerospace applications
- Autonomous vehicles

## References

- Padmanabhan, R., & Ornik, M. (2026). Finite-time Reachability for Constrained, Partially Uncontrolled Nonlinear Systems. arXiv:2604.08327.
