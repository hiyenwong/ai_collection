---
name: data-poisoning-control-security
description: "Data poisoning attacks on data-driven control systems - security analysis and defense strategies. Use for: securing data-driven control, attack detection, resilient control synthesis, adversarial robustness. Activation: data poisoning, control security, adversarial attacks, data-driven control vulnerabilities, resilient synthesis."
---

# Data Poisoning Control Security

Security analysis and defense strategies for data-driven control systems against poisoning attacks.

## Overview

Data-driven control enables controller synthesis directly from data without explicit model identification. However, this reliance on data introduces critical vulnerabilities. Attackers can systematically poison training data to destabilize the controlled system—even without knowledge of the system model or synthesis procedure.

**Key Threat Model:**
- Attacker poisons data at the collection level
- No knowledge of system dynamics required
- No knowledge of controller synthesis algorithm required
- Can deterministically destabilize any linear state-feedback controller

## Attack Mechanism

### Recursive Data Poisoning

The attacker generates falsified state trajectories that induce a precise geometric shift in the apparent system dynamics.

**Attack Vector:**
```
True system: x_{k+1} = A x_k + B u_k
Poisoned data: x̃_{k+1} = (A + ΔA) x_k + (B + ΔB) u_k
```

The perturbations ΔA, ΔB are carefully crafted to:
1. Appear consistent with nominal system behavior
2. Result in unstable closed-loop dynamics when used for synthesis

### Attack Algorithm

```python
class DataPoisoningAttack:
    def __init__(self, target_eigenvalue_shift=0.1):
        self.target_shift = target_eigenvalue_shift
    
    def craft_poisoned_trajectory(self, nominal_trajectory, control_sequence):
        """
        Generate poisoned state trajectory.
        
        Args:
            nominal_trajectory: True state sequence [x_0, x_1, ..., x_N]
            control_sequence: Applied controls [u_0, u_1, ..., u_{N-1}]
        
        Returns:
            poisoned_trajectory: Falsified state sequence
        """
        N = len(control_sequence)
        poisoned = [nominal_trajectory[0]]  # Keep initial state
        
        for k in range(N):
            # Compute falsified next state
            # Strategy: gradually shift dynamics to push poles to instability
            x_true = nominal_trajectory[k+1]
            
            # Add structured perturbation
            perturbation = self.compute_perturbation(
                poisoned[k], control_sequence[k], k, N
            )
            
            x_poisoned = x_true + perturbation
            poisoned.append(x_poisoned)
        
        return poisoned
    
    def compute_perturbation(self, x, u, k, N):
        """
        Compute state perturbation that appears natural but causes instability.
        
        The perturbation is designed to:
        1. Be within noise bounds (stealthy)
        2. Accumulate to shift identified dynamics
        3. Push closed-loop poles outside unit circle
        """
        # Progressive perturbation that compounds over horizon
        alpha = (k + 1) / N  # Increasing weight
        
        # Direction: align with unstable mode
        direction = self.estimate_unstable_direction(x)
        
        # Magnitude: within expected noise level
        magnitude = alpha * self.noise_magnitude * np.random.randn()
        
        return magnitude * direction
```

## Vulnerability Analysis

### Destabilization Conditions

**Theorem**: For any linear state-feedback synthesis procedure, there exists a data poisoning attack that causes the synthesized controller to destabilize the true system.

**Key Factors:**
1. **Data Quality**: Higher noise levels mask poisoned data
2. **Data Quantity**: More data requires more poisoning effort
3. **System Properties**: Unstable open-loop systems are more vulnerable
4. **Synthesis Method**: Direct vs. indirect methods have different vulnerabilities

### Attack Impact Assessment

```python
def assess_vulnerability(system, data_collection_setup):
    """
    Assess system vulnerability to data poisoning.
    
    Returns vulnerability score 0-1 (higher = more vulnerable)
    """
    scores = {
        'open_loop_stability': 0.3 if is_stable(system.A) else 0.8,
        'data_redundancy': 1.0 - min(data_collection_setup.n_samples / 1000, 1.0),
        'noise_level': data_collection_setup.noise_std / np.mean(np.abs(system.A)),
        'validation_gap': 0.5 if data_collection_setup.validation_ratio < 0.2 else 0.2
    }
    
    return np.mean(list(scores.values()))
```

## Defense Strategies

### 1. Data Validation

```python
class DataValidator:
    def __init__(self, confidence_threshold=0.95):
        self.threshold = confidence_threshold
    
    def validate_trajectory(self, trajectory, controls, system_estimate=None):
        """
        Validate if trajectory is consistent with expected dynamics.
        
        Returns:
            is_valid: Boolean indicating if trajectory passes validation
            confidence: Confidence score [0, 1]
        """
        checks = {
            'temporal_consistency': self.check_temporal_smoothness(trajectory),
            'physical_plausibility': self.check_physical_constraints(trajectory),
            'dynamics_consistency': self.check_dynamics_fit(trajectory, controls, system_estimate),
            'statistical_anomaly': self.check_statistical_outliers(trajectory)
        }
        
        confidence = np.mean(list(checks.values()))
        return confidence > self.threshold, confidence
    
    def check_temporal_smoothness(self, trajectory):
        """Check if state transitions are smooth."""
        velocities = np.diff(trajectory, axis=0)
        accelerations = np.diff(velocities, axis=0)
        
        # High acceleration indicates possible manipulation
        max_accel = np.max(np.abs(accelerations))
        expected_max = self.estimate_max_acceleration(trajectory)
        
        return 1.0 - min(max_accel / (2 * expected_max), 1.0)
    
    def check_dynamics_fit(self, trajectory, controls, system_estimate):
        """Check if trajectory fits estimated dynamics."""
        if system_estimate is None:
            return 0.5  # Neutral if no estimate available
        
        # Predict next states using estimated dynamics
        predicted = []
        for k in range(len(controls)):
            x_next = system_estimate.A @ trajectory[k] + \
                     system_estimate.B @ controls[k]
            predicted.append(x_next)
        
        predicted = np.array(predicted)
        actual = trajectory[1:]
        
        # Compute prediction error
        error = np.mean(np.linalg.norm(predicted - actual, axis=1))
        expected_error = self.estimate_prediction_noise(trajectory)
        
        return 1.0 - min(error / (2 * expected_error), 1.0)
```

### 2. Robust Synthesis

```python
class RobustDataDrivenControl:
    def __init__(self, uncertainty_bound=0.1):
        self.delta = uncertainty_bound
    
    def synthesize_with_uncertainty(self, data, confidence_level=0.95):
        """
        Synthesize controller robust to data uncertainty.
        
        Uses scenario-based optimization to guarantee performance
        under bounded uncertainty.
        """
        # Estimate nominal model
        A_nom, B_nom = self.estimate_model(data)
        
        # Estimate uncertainty bounds
        A_bounds, B_bounds = self.estimate_uncertainty_bounds(data)
        
        # Synthesize robust controller
        K = self.solve_robust_lqr(A_nom, B_nom, A_bounds, B_bounds)
        
        return K
    
    def solve_robust_lqr(self, A_nom, B_nom, A_bounds, B_bounds):
        """
        Solve robust LQR with polytopic uncertainty.
        
        min_K max_{A,B ∈ uncertainty_set} J(A, B, K)
        """
        # Formulate as semidefinite program
        # Use vertex enumeration or ellipsoidal uncertainty
        
        # Simplified: add robustness margin to nominal solution
        Q = np.eye(A_nom.shape[0])
        R = np.eye(B_nom.shape[1])
        
        # Nominal LQR
        K_nom = self.solve_lqr(A_nom, B_nom, Q, R)
        
        # Reduce gain for robustness
        K_robust = 0.8 * K_nom
        
        # Verify stability over uncertainty set
        if self.verify_robust_stability(K_robust, A_bounds, B_bounds):
            return K_robust
        else:
            # Iteratively reduce gain
            for alpha in np.linspace(0.7, 0.1, 10):
                K = alpha * K_nom
                if self.verify_robust_stability(K, A_bounds, B_bounds):
                    return K
            
            raise ValueError("Cannot find robust controller")
```

### 3. Online Detection

```python
class OnlineAttackDetector:
    def __init__(self, window_size=10, threshold=3.0):
        self.window_size = window_size
        self.threshold = threshold
        self.residual_history = []
    
    def detect(self, predicted_state, measured_state, control_input):
        """
        Detect anomalies in real-time.
        
        Returns:
            is_attack: Boolean indicating potential attack
            confidence: Detection confidence [0, 1]
        """
        # Compute prediction residual
        residual = measured_state - predicted_state
        residual_norm = np.linalg.norm(residual)
        
        self.residual_history.append(residual_norm)
        if len(self.residual_history) > self.window_size:
            self.residual_history.pop(0)
        
        # CUSUM detection
        if len(self.residual_history) >= self.window_size:
            mean_residual = np.mean(self.residual_history[:-1])
            std_residual = np.std(self.residual_history[:-1])
            
            if std_residual > 0:
                z_score = (residual_norm - mean_residual) / std_residual
                is_attack = z_score > self.threshold
                confidence = min(z_score / (2 * self.threshold), 1.0)
            else:
                is_attack = False
                confidence = 0.0
        else:
            is_attack = False
            confidence = 0.0
        
        return is_attack, confidence
```

### 4. Resilient Control Architecture

```python
class ResilientControlSystem:
    def __init__(self, n_redundant_estimators=3):
        self.estimators = [
            DataDrivenEstimator() for _ in range(n_redundant_estimators)
        ]
        self.validator = DataValidator()
        self.detector = OnlineAttackDetector()
        self.current_controller = None
    
    def update_controller(self, new_data_batch):
        """
        Safely update controller with new data.
        """
        # Validate data
        is_valid, confidence = self.validator.validate_trajectory(new_data_batch)
        
        if not is_valid:
            print(f"Warning: Data validation failed (confidence: {confidence:.2f})")
            return False
        
        # Train multiple estimators on different data subsets
        controllers = []
        for estimator in self.estimators:
            subset = self.sample_data_subset(new_data_batch)
            K = estimator.synthesize(subset)
            controllers.append(K)
        
        # Cross-validate controllers
        best_controller = self.select_by_consensus(controllers, new_data_batch)
        
        # Verify stability before deployment
        if self.verify_stability(best_controller):
            self.current_controller = best_controller
            return True
        else:
            print("Error: Synthesized controller unstable")
            return False
    
    def control_step(self, state, reference):
        """
        Execute control step with attack detection.
        """
        # Predict next state
        predicted = self.predict_next_state(state, self.last_control)
        
        # Compute control
        control = self.current_controller.compute(state, reference)
        self.last_control = control
        
        return control, predicted
    
    def measurement_update(self, measured_state):
        """
        Process new measurement and detect attacks.
        """
        is_attack, confidence = self.detector.detect(
            self.last_prediction, measured_state, self.last_control
        )
        
        if is_attack:
            self.handle_detected_attack(confidence)
        
        return is_attack
```

## Best Practices

### Data Collection

1. **Diverse Sources**: Collect from multiple sensors/instances
2. **Validation Split**: Reserve 20-30% for validation
3. **Temporal Distribution**: Spread collection over time
4. **Redundancy**: Multiple measurements of same trajectories

### Synthesis Pipeline

1. **Sanity Checks**: Verify identified model properties
2. **Cross-Validation**: Test on held-out data
3. **Stability Verification**: Check eigenvalues before deployment
4. **Gradual Deployment**: Start with conservative gains

### Monitoring

1. **Residual Monitoring**: Track prediction errors
2. **Performance Metrics**: Monitor control performance
3. **Anomaly Alerts**: Set up automated detection alerts
4. **Regular Audits**: Periodically re-validate data

## References

- Digge et al. (2026): "Data Poisoning Attacks Can Systematically Destabilize Data-Driven Control Synthesis", arXiv:2604.08392

## Related Skills

- `secure-control-systems`: General secure control design
- `adversarial-robustness`: Adversarial robustness in ML
- `resilient-control`: Fault-tolerant and resilient control

## Activation Keywords

- data poisoning
- control security
- adversarial attacks
- data-driven control vulnerabilities
- resilient synthesis
- attack detection
- secure data-driven control
