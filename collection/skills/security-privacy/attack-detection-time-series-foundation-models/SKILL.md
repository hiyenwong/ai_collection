---
name: attack-detection-time-series-foundation-models
description: "Model-structure-free attack detection for cyber-physical systems using TimesFM time-series foundation model as surrogate residual generator. Zero-shot detection without plant model knowledge, handling both model-free replay attacks and model-based stealthy attacks. Foundation models as corrupted measurement substitutes when redundancy assumptions fail. Applications: CPS security, power systems, network attack detection. Activation: attack detection, cyber-physical security, TimesFM, foundation model CPS, stealthy attack, replay attack, χ² detector, IEEE 14-bus, model-free detection, zero-shot detection."
---

## Context

From arXiv:2606.06347 (June 2026) - "Attack Detection using Time Series Foundation Models" by Sribalaji C. Anand, Anh Tung Nguyen, George J. Pappas.

Addresses attack detection in cyber-physical systems WITHOUT plant model knowledge. Uses Google's TimesFM foundation model as zero-shot residual generator, achieving comparable/superior detection to model-based methods on IEEE 14-bus power system.

## Core Methodology

### 1. Attack Taxonomy

**Two attack classes**:
1. **Model-free replay attacks**: Replay past sensor measurements, no knowledge of system dynamics
2. **Model-based stealthy attacks**: Optimal attack policy derived from system model, designed to evade χ² detector

**Attack setting**: Remote plant transmits sensor measurements to operator over compromised network.

### 2. Stealthy Attack Policy Derivation

**Optimal stealthy attack against χ² detector**:

For **linear systems**: dx/dt = Ax + Bu, y = Cx
```
Attack policy: u_attack = argmax ||y_attack||² 
               subject to: residual ∈ acceptable range (χ² test passes)

Closed-form solution exists for linear Gaussian systems
```

For **nonlinear systems**: dx/dt = f(x) + g(x)u, y = h(x)
```
Attack policy: Linearize around operating point
               Derive local stealthy attack strategy
               Extended to nonlinear via Taylor expansion
```

**Key insight**: Attack policy depends on:
- System matrices A, B, C (for linear)
- Jacobians ∂f/∂x, ∂h/∂x (for nonlinear)
- Attack budget (magnitude constraint)

### 3. TimesFM Foundation Model Approach

**TimesFM characteristics**:
- Pre-trained time-series foundation model (Google Research)
- Zero-shot prediction capability (no task-specific training)
- Handles multivariate time series
- Captures temporal patterns without explicit model

**Application to attack detection**:
```
1. Train TimesFM on nominal (attack-free) sensor data
2. For new measurements y_new:
   - TimesFM predicts: y_pred = TimesFM(y_history)
   - Compute residual: r = y_new - y_pred
   - χ² test: if ||r||² > threshold → attack detected
3. Zero-shot: No plant model (A, B, C) needed
```

### 4. Model-Structure-Free Detector Design

**Architecture**:
```python
class TimesFM_AttackDetector:
    def __init__(self, foundation_model):
        self.fm = foundation_model  # TimesFM
        self.threshold = None       # χ² threshold
        
    def calibrate(self, nominal_data):
        """
        Offline calibration on attack-free data
        
        Steps:
        1. Generate residuals: r = y - TimesFM(y_history)
        2. Compute residual statistics (mean, covariance)
        3. Set χ² threshold for desired false alarm rate
        """
        residuals = self.compute_residuals(nominal_data)
        self.threshold = chi2_threshold(residuals, alpha=0.05)
    
    def detect(self, current_measurement, history):
        """
        Online detection
        
        1. TimesFM prediction from history
        2. Compute residual
        3. χ² test
        """
        y_pred = self.fm.predict(history)
        residual = current_measurement - y_pred
        test_statistic = np.sum(residual**2)
        
        return test_statistic > self.threshold  # Attack detected
    
    def mitigation(self, current_measurement, history):
        """
        Use TimesFM prediction as substitute for corrupted measurements
        
        When classical redundancy fails, foundation model provides:
        - Clean estimate from temporal patterns
        - Practical mitigation without backup sensors
        """
        y_pred = self.fm.predict(history)
        return y_pred  # Substitute for compromised measurement
```

### 5. Implementation Steps

**Step 1: Foundation Model Setup**
```python
# Load TimesFM (Google Research pre-trained model)
from timesfm import TimesFM

model = TimesFM(
    model_size='large',  # or 'small' for faster inference
    context_length=512,  # History window
    prediction_length=1   # Next-step prediction
)
```

**Step 2: Offline Calibration**
```python
def calibrate_detector(nominal_sensor_data):
    """
    Input: Time series of nominal (attack-free) sensor measurements
    Output: Residual statistics and χ² threshold
    
    Process:
    1. Split data into history windows
    2. For each window:
       - TimesFM predicts next measurement
       - Compute residual
    3. Fit residual distribution
    4. Set threshold for α = 0.05 false alarm rate
    """
    residuals = []
    
    for i in range(len(data) - context_length):
        history = data[i:i+context_length]
        true_next = data[i+context_length]
        pred_next = model.predict(history)
        
        residual = true_next - pred_next
        residuals.append(residual)
    
    # Fit Gaussian to residuals
    residual_mean = np.mean(residuals)
    residual_cov = np.cov(residuals.T)
    
    # χ² threshold
    threshold = chi2.ppf(0.95, df=len(residuals[0]))
    
    return threshold
```

**Step 3: Online Detection**
```python
def detect_attack_stream(sensor_stream):
    """
    Real-time detection
    
    For each new measurement:
    1. Update history buffer
    2. TimesFM prediction
    3. Residual computation
    4. χ² test
    
    Return: Attack flag + residual magnitude
    """
    history_buffer = []
    
    for measurement in sensor_stream:
        history_buffer.append(measurement)
        
        if len(history_buffer) > context_length:
            history = history_buffer[-context_length:]
            prediction = model.predict(history)
            residual = measurement - prediction
            
            test_stat = np.sum(residual**2)
            
            if test_stat > threshold:
                return {
                    'attack_detected': True,
                    'residual_norm': test_stat,
                    'prediction': prediction  # For mitigation
                }
```

### 6. Attack Policy Computation (for comparison)

**Linear system optimal stealthy attack**:
```python
def optimal_stealthy_attack_linear(A, B, C, Q, R):
    """
    Derive optimal attack policy against χ² detector
    
    System: dx = Ax + Bu, y = Cx
    Detector residual: r = y - C*x_est (Kalman filter)
    
    Attack: Inject y_attack = y + a
    Stealthy: Residual r = Ca should pass χ² test
    
    Optimal policy: Maximize attack impact while staying stealthy
    """
    # Kalman filter matrices
    P = kalman_covariance(A, B, C, Q, R)
    K = kalman_gain(P, C, R)
    
    # Attack influence matrix
    attack_matrix = C - C*K*C
    
    # Stealthy attack: ||attack_matrix * a||² ≤ threshold
    # Maximize ||a||² subject to constraint
    
    optimal_attack = solve_stealthy_optimization(attack_matrix, threshold)
    
    return optimal_attack
```

**Nonlinear system attack**:
```python
def optimal_stealthy_attack_nonlinear(f, g, h, x_op):
    """
    Attack policy for nonlinear system
    
    Linearize around operating point x_op:
    A = ∂f/∂x @ x_op
    C = ∂h/∂x @ x_op
    
    Apply linear attack policy to Jacobians
    """
    A_lin = jacobian(f, x_op)
    C_lin = jacobian(h, x_op)
    
    return optimal_stealthy_attack_linear(A_lin, B, C_lin, Q, R)
```

## Pitfalls

1. **Foundation model generalization**: TimesFM must generalize to specific CPS dynamics. Pre-training on generic time series may not capture domain-specific patterns.

2. **History window length**: Too short → insufficient context; too long → outdated patterns. Must tune context_length.

3. **Calibration data quality**: Nominal data must be attack-free. Contaminated calibration data degrades detector.

4. **Threshold setting**: χ² threshold must balance false alarm rate vs detection sensitivity. Too tight → false alarms; too loose → missed attacks.

5. **Model-free vs model-based attacks**: TimesFM works well for model-free replay attacks. Stealthy attacks require more sophisticated detection.

6. **Mitigation reliability**: Using TimesFM predictions as substitutes works when model is accurate. Prediction errors accumulate over time.

7. **Computational cost**: Foundation model inference must be fast enough for real-time detection. Latency impacts detection speed.

## Verification

1. **Detection performance**: Compare detection rate vs false alarm rate against χ² baseline
2. **Stealthy attack detection**: Test against optimal stealthy attack policy (derived in paper)
3. **Robustness**: Vary attack magnitude, timing, patterns
4. **Mitigation effectiveness**: Test prediction-based substitution on corrupted data
5. **Computational latency**: Measure inference time for real-time feasibility
6. **Cross-system transfer**: Test on different CPS (power grid vs process control)

## Key Applications

1. **Power systems**: IEEE 14-bus test case validated in paper
2. **Process control**: Chemical plant sensor networks
3. **Transportation**: Vehicle sensor systems
4. **Industrial IoT**: Manufacturing sensor arrays
5. **Smart grids**: Distributed energy resource monitoring

## Experimental Validation (Paper)

**Test system**: IEEE 14-bus power network

**Attack types tested**:
1. Replay attacks (model-free)
2. Optimal stealthy attacks (model-based)

**Results**:
- TimesFM detector: Comparable/superior to model-based χ² detector
- Zero-shot: No plant model (A, B, C) required
- Mitigation: TimesFM predictions substitute corrupted measurements when redundancy fails

**Detection metrics**:
- Detection rate vs false alarm curve
- Comparison against Kalman filter + χ² baseline
- Robustness to attack variations

## Key Innovation

**Foundation model as surrogate residual generator**:
- Traditional approach: Kalman filter requires system model (A, B, C)
- TimesFM approach: Learn temporal patterns from data, no model needed
- Zero-shot: Apply pre-trained model directly, no task-specific training

**Practical mitigation**:
- Classical approach: Redundant sensors for corrupted measurement substitution
- TimesFM approach: Use foundation model prediction when redundancy unavailable
- Temporal patterns provide clean estimates

## Mathematical Details

**χ² detector theory**:
```
Residual: r = y - y_pred
Test statistic: T = r^T Σ^{-1} r
Threshold: T > χ²_{n,α} → attack detected
          where n = measurement dimension, α = false alarm rate
```

**Stealthy attack constraints**:
```
Attack: y_attack = y + a
Residual after attack: r = (y + a) - y_pred = r_nominal + a

Stealthy condition: ||r||² ≤ χ² threshold
Optimal attack: max ||a||² s.t. ||r||² ≤ threshold
```

**TimesFM residual generation**:
```
y_pred = TimesFM(y_history)
r = y_new - y_pred

No explicit model needed
Temporal patterns captured by foundation model
```

## Connection to Prior Work

- **Kalman filter + χ² detector**: Classic approach, requires system model
- **Model-free anomaly detection**: Statistical methods, limited temporal context
- **Learning-based detection**: Train on attack patterns, requires labeled data
- **TimesFM approach**: Zero-shot, no model, no labeled attack data, pre-trained foundation

## Practical Deployment

1. **Model loading**: Download pre-trained TimesFM weights
2. **Calibration**: Run on nominal data (hours)
3. **Deployment**: Real-time detection + mitigation (milliseconds)
4. **Hardware**: GPU inference for speed, CPU for edge deployment
5. **Integration**: Standalone detector or augmentation to existing monitoring

**Advantages**:
- No system model engineering
- Zero-shot deployment
- Cross-domain transfer potential
- Practical mitigation when sensors fail

**Limitations**:
- Requires sufficient history window
- Calibration data must be attack-free
- Foundation model inference latency
- Generalization to novel dynamics uncertain

## Future Directions

1. **Domain-specific foundation models**: Train TimesFM variants for CPS time series
2. **Multi-modal detection**: Combine sensor measurements with network traffic analysis
3. **Adaptive thresholds**: Online threshold adjustment based on residual statistics
4. **Attack classification**: Identify attack type (replay vs stealthy) from residual patterns
5. **Hybrid detection**: Combine model-based and model-free detectors

**Activation**: TimesFM attack detection, CPS security, foundation model CPS, stealthy attack optimal policy, χ² detector, IEEE 14-bus validation, replay attack, model-free anomaly detection, zero-shot CPS security, sensor corruption mitigation