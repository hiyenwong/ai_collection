---
name: anomaly-detection-dynamical-systems
description: "Log-likelihood ratio based real-time anomaly detection for dynamical systems with theoretical characterization of error rates. Identifies system anomalies from multiple possible plant models for linear Gaussian systems. Use for: anomaly detection, fault diagnosis, dynamical system monitoring, log-likelihood ratio testing, industrial control applications. Activation: anomaly detection, log-likelihood ratio, dynamical systems, industrial control, fault detection."
---

# Anomaly Detection for Dynamical Systems

Log-likelihood ratio based real-time anomaly detection with theoretical error rate characterization for linear Gaussian systems.

## Overview

This methodology provides:
- Real-time anomaly detection for industrial control applications
- Theoretical characterization of detection error rates
- Multiple plant model framework for different anomaly types
- Observer design leveraging error rate characterization

## Core Concepts

### Anomaly Detection Framework

```
System operates in modes:
├── Nominal mode (no anomaly)
├── Anomaly type 1
├── Anomaly type 2
└── ...

Each mode → Different plant model → Different likelihood
```

### Log-Likelihood Ratio Test

```
For each candidate model M_i:
LLR_i = log(p(y| M_i) / p(y| M_0))

Where:
- y: observations
- M_i: model with anomaly i
- M_0: nominal model

Decision: Select model with maximum LLR
```

### Error Rate Characterization

```
False alarm rate: P(choose M_i | M_0 true)
Miss detection rate: P(choose M_0 | M_i true)

These are characterized theoretically for linear Gaussian systems.
```

## Mathematical Framework

### Linear Gaussian System

```
x_{t+1} = A_i x_t + B_i u_t + w_t,  w_t ~ N(0, Q_i)
y_t = C_i x_t + D_i u_t + v_t,      v_t ~ N(0, R_i)

Where i indicates the operating mode (nominal or anomaly)
```

### Log-Likelihood Computation

```
For Kalman filter estimates (x̂_t, P_t):

Innovation: ν_t = y_t - C_i x̂_t - D_i u_t
Innovation covariance: S_t = C_i P_t C_i^T + R_i

Log-likelihood increment:
ΔLLR = -0.5 * [ν_t^T S_t^{-1} ν_t + log|S_t| + m*log(2π)]

Where m is measurement dimension
```

### Error Rate Analysis

```
For two models M_i and M_j:

KL divergence: D_{ij} = E_{M_i}[log(p(y|M_i)/p(y|M_j))]

This determines error rates:
- Lower KL divergence → Higher confusion probability
- Higher KL divergence → Better separability
```

## Algorithm

### Step 1: Model Bank Setup

```python
class ModelBank:
    def __init__(self):
        self.models = {
            'nominal': SystemModel(A0, B0, C0, D0, Q0, R0),
            'anomaly_1': SystemModel(A1, B1, C1, D1, Q1, R1),
            'anomaly_2': SystemModel(A2, B2, C2, D2, Q2, R2),
            # ...
        }
        self.kalman_filters = {
            name: KalmanFilter(model) 
            for name, model in self.models.items()
        }
```

### Step 2: Real-time Detection

```python
def detect_anomaly(observation, control_input):
    """
    Real-time anomaly detection using LLR.
    """
    llrs = {}
    
    for model_name, kf in kalman_filters.items():
        # Predict
        kf.predict(control_input)
        
        # Update with observation
        innovation = kf.compute_innovation(observation)
        
        # Compute log-likelihood increment
        ll_increment = compute_log_likelihood(innovation, kf.innovation_cov)
        
        # Accumulate LLR
        if model_name not in llrs:
            llrs[model_name] = 0
        llrs[model_name] += ll_increment
    
    # Select most likely model
    detected_model = max(llrs, key=llrs.get)
    confidence = compute_confidence(llrs)
    
    return detected_model, confidence, llrs
```

### Step 3: Error Rate Estimation

```python
def estimate_error_rates(model_i, model_j):
    """
    Theoretical error rate between two models.
    """
    # Compute steady-state Kalman gains
    K_i = steady_state_kalman_gain(model_i)
    K_j = steady_state_kalman_gain(model_j)
    
    # Compute asymptotic covariance
    Σ_i = asymptotic_innovation_covariance(model_i)
    Σ_j = asymptotic_innovation_covariance(model_j)
    
    # KL divergence approximation
    D_ij = 0.5 * (trace(Σ_j^{-1} Σ_i) - dim + log(det(Σ_j)/det(Σ_i)))
    
    # Error rate (Chernoff bound approximation)
    error_rate = exp(-D_ij / 2)
    
    return error_rate
```

## Observer Design Leveraging Characterization

### Design Criterion

```
Given: Required error rates (P_FA, P_MD)
Find: Observer parameters (L, Q_observer, R_observer)

Such that:
- P(false alarm) ≤ P_FA
- P(miss detection) ≤ P_MD
```

### Optimization Problem

```python
def design_observer(models, requirements):
    """
    Design observer to meet error rate requirements.
    """
    def objective(observer_params):
        observer = build_observer(observer_params)
        
        # Simulate error rates
        fa_rate = simulate_false_alarms(observer, models)
        md_rate = simulate_miss_detections(observer, models)
        
        # Penalty for constraint violation
        penalty = max(0, fa_rate - requirements['P_FA']) + \
                  max(0, md_rate - requirements['P_MD'])
        
        return penalty
    
    # Optimize observer parameters
    optimal_params = minimize(objective, initial_guess)
    return build_observer(optimal_params)
```

## Use Cases

### 1. Industrial Process Monitoring

```
Application: Chemical plant fault detection
Models:
- Nominal: Normal operating conditions
- Anomaly 1: Sensor drift
- Anomaly 2: Valve malfunction
- Anomaly 3: Heat exchanger fouling

Benefit: Early detection enables prompt maintenance
```

### 2. Aerospace Systems

```
Application: Aircraft subsystem monitoring
Models:
- Nominal: Standard flight conditions
- Anomaly 1: Actuator degradation
- Anomaly 2: Sensor bias
- Anomaly 3: Structural damage indicators

Benefit: Safety-critical fault detection
```

### 3. Power Grid Monitoring

```
Application: Electrical grid anomaly detection
Models:
- Nominal: Stable operation
- Anomaly 1: Generator fault
- Anomaly 2: Transmission line issue
- Anomaly 3: Load anomaly

Benefit: Prevent cascading failures
```

## Parameters

| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| Window size | LLR accumulation window | 10-100 samples |
| Threshold | Detection threshold | Based on error rates |
| N_models | Number of candidate models | 2-10 |

## Performance Metrics

| Metric | Definition | Target |
|--------|-----------|--------|
| Detection delay | Time to detect anomaly | Minimize |
| False alarm rate | Incorrect anomaly claims | < 1% |
| Miss rate | Undetected anomalies | < 5% |
| Isolation accuracy | Correct anomaly type | > 95% |

## Activation Keywords

- anomaly detection
- log-likelihood ratio
- dynamical systems
- industrial control
- fault detection
- multiple model estimation
- hypothesis testing
- error rate characterization

## Related Skills

- `automated-cps-testing-act`: CPS testing framework
- `data-driven-moving-horizon-estimation`: State estimation
- `koopman-representation-learning`: Dynamical system analysis

## References

- Paper: arXiv:2604.11631 (April 2026)
- Authors: Riveiros, Barreau, Bastianello
- Theory: Log-likelihood ratio, Kalman filtering
- Application: Industrial control systems

## Example Usage

```
"Implement LLR-based anomaly detection for control systems"
"Characterize error rates for multi-model fault detection"
"Design observer for industrial process monitoring"
"Detect subtle anomalies in linear Gaussian systems"
```

## Code Template

```python
import numpy as np
from scipy.stats import multivariate_normal
from filterpy.kalman import KalmanFilter

class LLRAnomalyDetector:
    def __init__(self, models):
        """
        Initialize with dictionary of system models.
        
        Args:
            models: Dict of {'name': LinearSystemModel}
        """
        self.models = models
        self.filters = {
            name: self._build_kalman_filter(model)
            for name, model in models.items()
        }
        self.llr_accumulators = {name: 0 for name in models}
    
    def _build_kalman_filter(self, model):
        """Build Kalman filter from system model."""
        kf = KalmanFilter(dim_x=model.n_states, dim_z=model.n_outputs)
        kf.F = model.A
        kf.B = model.B
        kf.H = model.C
        kf.Q = model.Q
        kf.R = model.R
        return kf
    
    def update(self, observation, control):
        """
        Process new observation and detect anomalies.
        
        Returns:
            detected_model: Most likely model name
            llrs: Log-likelihood ratios for all models
            confidence: Detection confidence
        """
        llrs = {}
        
        for name, kf in self.filters.items():
            # Prediction step
            kf.predict(u=control)
            
            # Compute innovation
            innovation = observation - kf.H @ kf.x_prior
            innovation_cov = kf.H @ kf.P_prior @ kf.H.T + kf.R
            
            # Log-likelihood of observation
            ll = multivariate_normal.logpdf(
                innovation, 
                mean=np.zeros_like(innovation),
                cov=innovation_cov
            )
            
            # Update accumulator
            self.llr_accumulators[name] += ll
            llrs[name] = self.llr_accumulators[name]
            
            # Update Kalman filter
            kf.update(observation)
        
        # Detect most likely model
        detected_model = max(llrs, key=llrs.get)
        
        # Compute confidence
        llr_values = np.array(list(llrs.values()))
        confidence = np.max(llr_values) - np.mean(llr_values)
        
        return detected_model, llrs, confidence
    
    def reset(self):
        """Reset LLR accumulators."""
        self.llr_accumulators = {name: 0 for name in self.models}
```

## Notes

- Requires accurate system models for each anomaly type
- Linear Gaussian assumption enables theoretical analysis
- Real-time capable with Kalman filtering
- Error rate characterization aids observer design
- Multiple models enable anomaly isolation
