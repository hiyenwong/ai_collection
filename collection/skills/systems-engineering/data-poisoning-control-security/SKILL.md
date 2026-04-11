---
name: data-poisoning-control-security
description: "Data poisoning attacks on data-driven control systems. Analyzes vulnerabilities where attackers systematically poison training data to destabilize control synthesis. Activation: data poisoning, control security, adversarial attacks, data-driven control."
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [data-poisoning, control-security, adversarial-attacks, data-driven-control, robustness]
    source_paper: "Data Poisoning Attacks Can Systematically Destabilize Data-Driven Control Synthesis (arXiv:2604.08392)"
    citations: 0
    category: systems-engineering
---

# Data Poisoning Attacks on Data-Driven Control Systems

## Overview

Data-driven control has emerged as a powerful paradigm for synthesizing controllers directly from data, bypassing explicit model identification. However, this reliance on data introduces new vulnerabilities. This paper shows that attackers can systematically poison the training data to destabilize control synthesis.

## Core Concepts

### Data-Driven Control
- **Direct Synthesis**: Controllers learned from data without explicit models
- **Methods**: System identification, reinforcement learning, behavioral approaches
- **Vulnerability**: Dependence on data quality and integrity

### Data Poisoning Attacks
- **Attack Model**: Attacker modifies training data
- **Objective**: Cause controller instability or performance degradation
- **Stealth**: Attacks may be subtle and hard to detect

### Security Analysis
- **Attack Feasibility**: Conditions under which attacks succeed
- **Impact Assessment**: Quantifying destabilization effects
- **Defense Strategies**: Detection and mitigation approaches

## Implementation

```python
import numpy as np
from typing import Tuple, List, Optional
from scipy.linalg import solve_discrete_are

class DataDrivenController:
    def __init__(self, n_states: int, n_inputs: int):
        self.n = n_states
        self.m = n_inputs
        self.A_est = None
        self.B_est = None
        self.K = None
        
    def identify_system(self, states: np.ndarray, inputs: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        N = states.shape[1] - 1
        X = states[:, :-1]
        U = inputs[:, :-1]
        X_next = states[:, 1:]
        
        # Least squares identification
        Theta = np.vstack([X, U])
        AB = X_next @ np.linalg.pinv(Theta)
        self.A_est = AB[:, :self.n]
        self.B_est = AB[:, self.n:]
        
        return self.A_est, self.B_est
    
    def synthesize_controller(self, Q: np.ndarray, R: np.ndarray) -> np.ndarray:
        if self.A_est is None or self.B_est is None:
            raise ValueError("System not identified")
        
        # LQR design
        P = solve_discrete_are(self.A_est, self.B_est, Q, R)
        self.K = np.linalg.inv(R + self.B_est.T @ P @ self.B_est) @ self.B_est.T @ P @ self.A_est
        return self.K
    
    def compute_control(self, x: np.ndarray) -> np.ndarray:
        if self.K is None:
            raise ValueError("Controller not synthesized")
        return -self.K @ x


class DataPoisoningAttacker:
    def __init__(self, attack_budget: float, attack_type: str = "stealthy"):
        self.budget = attack_budget
        self.attack_type = attack_type
        
    def craft_attack(self, 
                     states: np.ndarray, 
                     inputs: np.ndarray,
                     target_system: Optional[Tuple[np.ndarray, np.ndarray]] = None) -> Tuple[np.ndarray, np.ndarray]:
        if self.attack_type == "stealthy":
            return self._stealthy_attack(states, inputs, target_system)
        elif self.attack_type == "aggressive":
            return self._aggressive_attack(states, inputs)
        else:
            return states, inputs
    
    def _stealthy_attack(self, states: np.ndarray, inputs: np.ndarray,
                        target_system: Tuple[np.ndarray, np.ndarray]) -> Tuple[np.ndarray, np.ndarray]:
        A_target, B_target = target_system
        N = states.shape[1] - 1
        
        # Perturb states to bias identification toward unstable system
        states_poisoned = states.copy()
        
        for i in range(N):
            x = states[:, i]
            u = inputs[:, i]
            
            # Compute what the next state should be under target system
            x_next_target = A_target @ x + B_target @ u
            
            # Add small perturbation toward target
            noise = np.random.randn(self.n) * 0.01
            perturbation = (x_next_target - states[:, i+1]) * 0.1 + noise
            
            if np.linalg.norm(perturbation) < self.budget:
                states_poisoned[:, i+1] += perturbation
        
        return states_poisoned, inputs
    
    def _aggressive_attack(self, states: np.ndarray, inputs: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        # Add large perturbations
        noise = np.random.randn(*states.shape) * self.budget
        return states + noise, inputs


class SecurityAnalyzer:
    def __init__(self, true_system: Tuple[np.ndarray, np.ndarray]):
        self.A_true, self.B_true = true_system
        
    def evaluate_stability(self, A_cl: np.ndarray) -> bool:
        eigenvalues = np.linalg.eigvals(A_cl)
        return all(np.abs(ev) < 1 for ev in eigenvalues)
    
    def compute_performance_degradation(self, 
                                       K_clean: np.ndarray,
                                       K_poisoned: np.ndarray,
                                       Q: np.ndarray, R: np.ndarray) -> float:
        # Compute cost difference
        A_cl_clean = self.A_true - self.B_true @ K_clean
        A_cl_poisoned = self.A_true - self.B_true @ K_poisoned
        
        # Solve Lyapunov equation for cost
        P_clean = self._solve_lyapunov(A_cl_clean, Q + K_clean.T @ R @ K_clean)
        P_poisoned = self._solve_lyapunov(A_cl_poisoned, Q + K_poisoned.T @ R @ K_poisoned)
        
        return np.trace(P_poisoned - P_clean)
    
    def _solve_lyapunov(self, A: np.ndarray, Q: np.ndarray) -> np.ndarray:
        from scipy.linalg import solve_discrete_lyapunov
        return solve_discrete_lyapunov(A, Q)


# Example: Attack demonstration
def demonstrate_attack():
    # True system: stable
    A_true = np.array([[0.9, 0.1],
                       [0.0, 0.8]])
    B_true = np.array([[0.1],
                       [0.2]])
    
    # Generate clean data
    n_steps = 100
    x0 = np.array([1.0, 0.5])
    states = [x0]
    inputs = []
    
    x = x0.copy()
    for _ in range(n_steps):
        u = np.random.randn() * 0.1
        x = A_true @ x + B_true @ u + np.random.randn(2) * 0.01
        states.append(x.copy())
        inputs.append([u])
    
    states = np.array(states).T
    inputs = np.array(inputs).T
    
    # Clean controller
    controller_clean = DataDrivenController(2, 1)
    controller_clean.identify_system(states, inputs)
    K_clean = controller_clean.synthesize_controller(np.eye(2), np.eye(1))
    
    # Poison data
    A_target = np.array([[1.1, 0.1],  # Unstable
                         [0.0, 0.8]])
    attacker = DataPoisoningAttacker(attack_budget=0.5, attack_type="stealthy")
    states_poisoned, inputs_poisoned = attacker.craft_attack(
        states, inputs, target_system=(A_target, B_true)
    )
    
    # Poisoned controller
    controller_poisoned = DataDrivenController(2, 1)
    controller_poisoned.identify_system(states_poisoned, inputs_poisoned)
    K_poisoned = controller_poisoned.synthesize_controller(np.eye(2), np.eye(1))
    
    # Analyze
    analyzer = SecurityAnalyzer((A_true, B_true))
    
    A_cl_clean = A_true - B_true @ K_clean
    A_cl_poisoned = A_true - B_true @ K_poisoned
    
    print("Clean controller stable:", analyzer.evaluate_stability(A_cl_clean))
    print("Poisoned controller stable:", analyzer.evaluate_stability(A_cl_poisoned))
    print("Performance degradation:", 
          analyzer.compute_performance_degradation(K_clean, K_poisoned, np.eye(2), np.eye(1)))


if __name__ == "__main__":
    demonstrate_attack()
```

## Key Insights

1. **Systematic Vulnerability**: Data-driven control is systematically vulnerable to poisoning
2. **Stealthy Attacks**: Subtle perturbations can cause significant destabilization
3. **Defense Need**: Robust identification and anomaly detection are critical

## Defense Strategies

- **Data Validation**: Outlier detection and data cleaning
- **Robust Identification**: Methods resistant to outliers
- **Online Monitoring**: Real-time stability checking
- **Adversarial Training**: Train with poisoned data

## References

- Digge, V., Vanelli, M., Al-Dabbagh, A. W., Hendrickx, J. M., & Bianchin, G. (2026). Data Poisoning Attacks Can Systematically Destabilize Data-Driven Control Synthesis. arXiv:2604.08392.
