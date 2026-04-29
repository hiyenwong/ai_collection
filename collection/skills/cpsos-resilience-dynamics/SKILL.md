---
name: cpsos-resilience-dynamics
description: "Resilience as a dynamical property of risk trajectories in Cyber-Physical Systems of Systems (CPSoS). Use for: resilience assessment, risk trajectory analysis, CPSoS design, recovery dynamics evaluation. Activation: resilience dynamics, risk trajectory, CPSoS resilience, dynamical resilience, recovery assessment."
---

# CPSoS Resilience Dynamics

Resilience assessment framework for Cyber-Physical Systems of Systems (CPSoS) based on dynamical properties of risk trajectories.

## Overview

Traditional resilience assessment uses static indices or point-in-time metrics that fail to capture the temporal evolution of risk following disruptions. This framework formalizes resilience as a functional of the risk trajectory, modeling risk as a dynamic state variable.

**Key Insight**: Resilience properties are structurally determined by:
- **Maximum deviation (peak)**: Worst-case risk exposure
- **Effective damping**: Rate of risk recovery
- Their ratio determines cumulative risk exposure

## Theoretical Framework

### Risk as Dynamic State Variable

Risk r(t) evolves according to:
```
dr/dt = f(r, d, u, t)
```

where:
- r: Risk level
- d: Disruption/perturbation
- u: Control/recovery actions
- t: Time

### Resilience Functional

Resilience R is defined as a functional of the risk trajectory:
```
R[r(·)] = Φ(r_peak, t_recovery, ∫r(t)dt)
```

Key components:
1. **Peak Risk**: r_peak = max_t r(t)
2. **Recovery Time**: t_recovery = min{t : r(t) ≤ r_threshold}
3. **Cumulative Risk**: R_cumulative = ∫_{t_0}^{t_f} r(t) dt

### Structural Properties

**Theorem**: For second-order risk dynamics:
```
d²r/dt² + 2ζω_n dr/dt + ω_n² r = disturbance
```

Resilience properties depend on:
- **Damping ratio ζ**: Determines oscillation and decay
- **Natural frequency ω_n**: Determines response speed

**Peak Magnitude**:
```
r_peak ≈ r_ss + (r_0 - r_ss) * exp(-ζπ/√(1-ζ²))  (for ζ < 1)
```

**Recovery Dynamics**:
```
r(t) = r_ss + (r_0 - r_ss) * e^(-ζω_n t) * cos(ω_d t + φ)
```

where ω_d = ω_n√(1-ζ²) is the damped frequency.

## Resilience Metrics

### 1. Peak Deviation Metric

```python
def compute_peak_deviation(risk_trajectory, baseline_risk):
    """
    Compute maximum risk deviation from baseline.
    
    Args:
        risk_trajectory: Array of risk values over time
        baseline_risk: Nominal risk level
    
    Returns:
        peak_deviation: Maximum (risk - baseline)
        time_to_peak: Time when peak occurs
    """
    deviations = risk_trajectory - baseline_risk
    peak_idx = np.argmax(deviations)
    
    return {
        'peak_deviation': deviations[peak_idx],
        'time_to_peak': peak_idx,
        'relative_peak': deviations[peak_idx] / baseline_risk if baseline_risk > 0 else float('inf')
    }
```

### 2. Effective Damping Metric

```python
def estimate_effective_damping(risk_trajectory, time_points):
    """
    Estimate effective damping from risk trajectory.
    
    Fits exponential decay to envelope of risk trajectory.
    """
    from scipy.optimize import curve_fit
    
    # Extract peaks (local maxima)
    from scipy.signal import find_peaks
    peaks, _ = find_peaks(risk_trajectory)
    
    if len(peaks) < 2:
        return {'damping': None, 'confidence': 0.0}
    
    peak_times = time_points[peaks]
    peak_values = risk_trajectory[peaks]
    
    # Fit exponential decay: A * exp(-ζ*ω*t)
    def decay_func(t, A, zeta_omega):
        return A * np.exp(-zeta_omega * t)
    
    try:
        popt, _ = curve_fit(decay_func, peak_times, peak_values, 
                           p0=[peak_values[0], 0.1])
        zeta_omega = popt[1]
        
        return {
            'damping_rate': zeta_omega,
            'time_constant': 1.0 / zeta_omega if zeta_omega > 0 else float('inf'),
            'confidence': min(len(peaks) / 5, 1.0)
        }
    except:
        return {'damping': None, 'confidence': 0.0}
```

### 3. Cumulative Risk Exposure

```python
def compute_cumulative_risk(risk_trajectory, time_points, baseline=None):
    """
    Compute cumulative risk exposure using trapezoidal integration.
    
    Args:
        risk_trajectory: Risk values over time
        time_points: Time stamps
        baseline: Risk level to subtract (default: min risk)
    
    Returns:
        cumulative: Total risk exposure
        normalized: Cumulative risk normalized by time
    """
    if baseline is None:
        baseline = np.min(risk_trajectory)
    
    adjusted_risk = risk_trajectory - baseline
    
    # Trapezoidal integration
    dt = np.diff(time_points)
    cumulative = np.sum(0.5 * (adjusted_risk[:-1] + adjusted_risk[1:]) * dt)
    
    duration = time_points[-1] - time_points[0]
    
    return {
        'cumulative_risk': cumulative,
        'normalized_risk': cumulative / duration if duration > 0 else 0,
        'duration': duration
    }
```

### 4. Integrated Resilience Index

```python
def compute_resilience_index(risk_trajectory, time_points, baseline_risk, 
                             disruption_time, recovery_threshold=0.1):
    """
    Compute comprehensive resilience index.
    
    Combines peak, damping, and cumulative metrics into single index.
    """
    # Peak metrics
    peak_info = compute_peak_deviation(risk_trajectory, baseline_risk)
    
    # Damping metrics
    damping_info = estimate_effective_damping(risk_trajectory, time_points)
    
    # Cumulative metrics
    cumulative_info = compute_cumulative_risk(risk_trajectory, time_points, baseline_risk)
    
    # Recovery time
    recovery_idx = np.where(risk_trajectory <= baseline_risk * (1 + recovery_threshold))[0]
    if len(recovery_idx) > 0:
        recovery_time = time_points[recovery_idx[0]] - disruption_time
    else:
        recovery_time = time_points[-1] - disruption_time
    
    # Composite index (higher = more resilient)
    # Normalize each component to [0, 1]
    peak_score = 1.0 / (1.0 + peak_info['relative_peak'])
    
    if damping_info['damping_rate'] is not None:
        damping_score = min(damping_info['damping_rate'] / 0.5, 1.0)
    else:
        damping_score = 0.5
    
    recovery_score = 1.0 / (1.0 + recovery_time / 100)  # Normalize to ~100s
    
    # Weighted combination
    weights = {'peak': 0.3, 'damping': 0.3, 'recovery': 0.4}
    resilience_index = (
        weights['peak'] * peak_score +
        weights['damping'] * damping_score +
        weights['recovery'] * recovery_score
    )
    
    return {
        'resilience_index': resilience_index,
        'peak_score': peak_score,
        'damping_score': damping_score,
        'recovery_score': recovery_score,
        'peak_info': peak_info,
        'damping_info': damping_info,
        'recovery_time': recovery_time,
        'cumulative_info': cumulative_info
    }
```

## Risk Trajectory Modeling

### Energy-Dependent System Example

```python
class EnergyDependentRiskSystem:
    """
    Example system where risk depends on energy state.
    """
    
    def __init__(self, critical_energy=100, recovery_rate=0.1):
        self.E_critical = critical_energy
        self.alpha = recovery_rate
        self.energy = 0
        self.risk = 0
    
    def dynamics(self, state, t, disturbance):
        """
        Risk dynamics with energy coupling.
        
        dE/dt = -disturbance + recovery
        dr/dt = f(E) - damping * r
        """
        E, r = state
        
        # Energy dynamics
        dE = -disturbance + self.alpha * (self.E_critical - E)
        
        # Risk depends on energy deficit
        energy_factor = max(0, 1 - E / self.E_critical)
        dr = energy_factor * (1 + 0.5 * np.sin(2 * np.pi * t / 10)) - 0.2 * r
        
        return [dE, dr]
    
    def simulate(self, initial_state, disturbance_profile, T, dt=0.1):
        """Simulate risk trajectory under disturbance."""
        from scipy.integrate import odeint
        
        times = np.arange(0, T, dt)
        
        def dyn(state, t):
            d = disturbance_profile(t)
            return self.dynamics(state, t, d)
        
        trajectory = odeint(dyn, initial_state, times)
        
        return times, trajectory
```

### Comparison of Resilience Profiles

```python
def compare_resilience_profiles(systems, disturbance, T=200):
    """
    Compare resilience of multiple system configurations.
    
    Args:
        systems: List of (name, system_instance, initial_state)
        disturbance: Disturbance function
        T: Simulation time
    """
    results = {}
    
    for name, system, x0 in systems:
        times, traj = system.simulate(x0, disturbance, T)
        E_traj, r_traj = traj[:, 0], traj[:, 1]
        
        # Compute resilience metrics
        metrics = compute_resilience_index(
            r_traj, times, baseline_risk=0.1, 
            disruption_time=50
        )
        
        results[name] = {
            'times': times,
            'risk': r_traj,
            'energy': E_traj,
            'metrics': metrics
        }
    
    return results
```

## CPSoS Application

### Multi-Layer Risk Propagation

```python
class CPSoSRiskModel:
    """
    Risk model for Cyber-Physical Systems of Systems.
    """
    
    def __init__(self, n_systems, coupling_matrix):
        self.n = n_systems
        self.C = coupling_matrix  # Risk coupling between systems
        
        # Each system has local risk dynamics
        self.local_dynamics = [
            self.create_local_dynamics(i)
            for i in range(n_systems)
        ]
    
    def global_dynamics(self, r_vector, t, disturbances):
        """
        Global risk dynamics with coupling.
        
        dr_i/dt = f_i(r_i, d_i) + Σ_j C_ij * (r_j - r_i)
        """
        dr = np.zeros(self.n)
        
        for i in range(self.n):
            # Local dynamics
            dr[i] += self.local_dynamics[i](r_vector[i], disturbances[i])
            
            # Coupling from other systems
            for j in range(self.n):
                if i != j:
                    dr[i] += self.C[i, j] * (r_vector[j] - r_vector[i])
        
        return dr
    
    def simulate_cascading_failure(self, initial_risks, failure_sequence):
        """
        Simulate cascading failure scenario.
        
        Args:
            initial_risks: Initial risk levels for all systems
            failure_sequence: List of (time, system_id, impact)
        """
        # Implementation of cascading failure simulation
        pass
```

## Design Guidelines

### Improving Resilience

1. **Reduce Peak Risk**:
   - Add redundancy to critical components
   - Implement graceful degradation
   - Use predictive maintenance

2. **Increase Damping**:
   - Implement feedback control for risk
   - Add recovery mechanisms
   - Design for fast reconfiguration

3. **Minimize Cumulative Exposure**:
   - Reduce time to recovery
   - Implement parallel recovery
   - Pre-position resources

### Trade-offs

| Design Choice | Peak Risk | Recovery Time | Complexity |
|--------------|-----------|---------------|------------|
| High Redundancy | Lower | Faster | Higher |
| Fast Recovery | Similar | Faster | Higher |
| Graceful Degradation | Lower | Slower | Medium |
| Predictive Control | Lower | Faster | Higher |

## References

- Vogel & Langendörfer (2026): "Resilience as a Dynamical Property of Risk Trajectories in CPSoS", arXiv:2604.08112

## Related Skills

- `system-resilience-design-patterns`: Resilience design patterns
- `complex-system-robustness-collapse`: Complex system robustness
- `mpc-stability-suboptimality`: MPC stability analysis

## Activation Keywords

- resilience dynamics
- risk trajectory
- CPSoS resilience
- dynamical resilience
- recovery assessment
- risk evolution
- resilience metrics
