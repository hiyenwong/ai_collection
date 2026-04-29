---
name: cps-security-anomaly-detection
description: "Comprehensive framework for anomaly detection in Cyber-Physical Systems (CPS) security. Covers model-based, data-driven, statistical, and hybrid approaches for detecting cyber threats in critical infrastructure. Activation: CPS security, anomaly detection, cyber-physical systems, intrusion detection, industrial control system security."
---

# CPS Security: Anomaly Detection Techniques

Comprehensive framework for detecting cyber threats in Cyber-Physical Systems (CPS) through anomaly detection, covering model-based, data-driven, statistical, and hybrid approaches.

## Overview

Cyber-Physical Systems (CPS) merge physical processes with computational elements, making them vulnerable to cyber attacks that can cause physical damage. Anomaly detection is a critical defense mechanism.

### CPS Security Challenges

| Challenge | Description |
|-----------|-------------|
| Physical Impact | Attacks can cause real-world damage |
| Real-time Constraints | Detection must be fast enough to prevent harm |
| Legacy Systems | Many CPS use outdated, insecure protocols |
| Safety-Critical | False positives can be as dangerous as missed attacks |
| Limited Resources | Edge devices have constrained compute/memory |
| Network Complexity | Heterogeneous communication protocols |

## Anomaly Detection Taxonomy

### 1. Model-Based Approaches

**Principle**: Use mathematical models of system dynamics to predict expected behavior.

**Techniques**:

#### State Estimation
```
Predicted: x̂(k+1) = Ax(k) + Bu(k)
Residual: r(k) = y(k) - Cx̂(k)
Anomaly: ||r(k)|| > threshold
```

**Methods**:
- Kalman Filter (linear systems)
- Extended Kalman Filter (nonlinear)
- Unscented Kalman Filter (highly nonlinear)
- Particle Filter (non-Gaussian noise)

#### Observer-Based Detection
- Luenberger observer
- Unknown Input Observer (UIO)
- Sliding mode observer

**Strengths**:
- Interpretable results
- Can detect stealthy attacks
- Low computational cost

**Limitations**:
- Requires accurate system model
- Sensitive to model uncertainty
- May miss novel attack patterns

### 2. Data-Driven Approaches

**Principle**: Learn normal behavior from data without explicit models.

#### Machine Learning Methods

**Supervised Learning** (requires labeled attack data):
- Support Vector Machines (SVM)
- Random Forests
- Gradient Boosting
- Neural Networks

**Unsupervised Learning** (no attack labels needed):
- Clustering (K-means, DBSCAN)
- One-Class SVM
- Isolation Forest
- Autoencoders

**Deep Learning**:
- LSTM/GRU for temporal patterns
- CNN for spatial patterns
- Transformer for long-range dependencies
- GAN for anomaly generation

#### Feature Engineering

**Physical Features**:
- Sensor readings
- Actuator commands
- Physical state variables
- Power consumption

**Network Features**:
- Packet timing
- Protocol anomalies
- Traffic volume
- Communication patterns

**Temporal Features**:
- Rate of change
- Moving averages
- Frequency domain features
- Wavelet coefficients

**Strengths**:
- No need for system model
- Can detect novel attacks
- Scalable to large systems

**Limitations**:
- Requires training data
- May overfit to normal patterns
- Black-box nature
- Computationally expensive

### 3. Statistical Approaches

**Principle**: Use statistical properties to detect deviations.

#### Change Detection

**CUSUM (Cumulative Sum)**:
```
S_t = max(0, S_{t-1} + log(p(x_t|H₁)/p(x_t|H₀)))
Anomaly if S_t > threshold
```

**EWMA (Exponentially Weighted Moving Average)**:
```
z_t = λx_t + (1-λ)z_{t-1}
Anomaly if |z_t - μ| > Lσ
```

**Sequential Probability Ratio Test (SPRT)**:
- Optimal for detecting changes
- Minimizes detection delay

#### Multivariate Statistics

- Hotelling's T²
- Principal Component Analysis (PCA)
- Independent Component Analysis (ICA)
- Mahalanobis distance

**Strengths**:
- Theoretically grounded
- Low computational cost
- Easy to implement

**Limitations**:
- Assumes specific distributions
- May miss complex attacks
- Threshold tuning required

### 4. Hybrid Approaches

**Principle**: Combine multiple paradigms for robust detection.

#### Model + Data-Driven
- Use model residuals as features for ML
- Physics-informed neural networks
- Hybrid state estimation

#### Statistical + ML
- Use statistical features in ML models
- Bayesian neural networks
- Probabilistic ML

#### Multi-Layer Detection
```
Layer 1: Physical (model-based) - Fast, low false positive
Layer 2: Network (statistical) - Protocol anomalies
Layer 3: System (ML) - Complex attack patterns
```

**Strengths**:
- Combines advantages of multiple approaches
- More robust to different attack types
- Can balance speed and accuracy

**Limitations**:
- Increased complexity
- More parameters to tune
- Integration challenges

### 5. Distributed Detection

**Principle**: Detect anomalies across networked CPS.

#### Consensus-Based Detection
- Distributed state estimation
- Collaborative anomaly detection
- Byzantine fault tolerance

#### Federated Learning
- Train models across distributed nodes
- Preserve data privacy
- Share only model updates

**Strengths**:
- Scalable to large networks
- Privacy preserving
- Robust to single-point failures

**Limitations**:
- Communication overhead
- Synchronization challenges
- Byzantine attacks on consensus

## Evaluation Metrics

### Detection Performance

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| True Positive Rate | TP/(TP+FN) | Fraction of attacks detected |
| False Positive Rate | FP/(FP+TN) | Fraction of normal flagged as attack |
| Precision | TP/(TP+FP) | Reliability of alerts |
| F1 Score | 2·Precision·Recall/(Precision+Recall) | Balanced measure |
| AUC-ROC | Area under ROC curve | Overall discriminative ability |

### CPS-Specific Metrics

**Detection Latency**: Time from attack start to detection
**Time-to-Impact**: Time from detection to physical consequence
**Safety Margin**: Time available for response

## Attack Taxonomy

### By Target

| Target | Examples | Detection Approach |
|--------|----------|-------------------|
| Sensors | False data injection | Model-based residual analysis |
| Actuators | Control signal manipulation | Command validation |
| Controllers | Malicious code | Behavior profiling |
| Communication | Man-in-the-middle | Network anomaly detection |
| Physical | Device tampering | Physical inspection + monitoring |

### By Knowledge

- **Zero-Knowledge**: Attacker knows nothing about system
- **Partial Knowledge**: Attacker knows some system parameters
- **Full Knowledge**: Attacker has complete system model

### By Stealth

- **Blatant**: Obvious anomalies
- **Stealthy**: Small deviations that evade detection
- **Zero-Alarm**: Attacks that never trigger alarms

## Implementation Guidelines

### 1. Threat Modeling
- Identify critical assets
- Analyze attack vectors
- Define attacker capabilities
- Determine detection requirements

### 2. Approach Selection

| System Characteristics | Recommended Approach |
|------------------------|---------------------|
| Well-modeled, linear | Model-based (Kalman filter) |
| Complex, nonlinear | Data-driven (deep learning) |
| Resource constrained | Statistical (CUSUM) |
| Safety-critical | Hybrid (multi-layer) |
| Large-scale distributed | Distributed detection |

### 3. Deployment Strategy

```
Phase 1: Baseline establishment
  - Collect normal operation data
  - Train/validate detection models
  - Set thresholds

Phase 2: Shadow mode
  - Run detection in parallel
  - Tune parameters
  - Validate false positive rate

Phase 3: Active protection
  - Enable automated responses
  - Continuous monitoring
  - Regular model updates
```

### 4. Response Mechanisms

**Detection → Response Pipeline**:
1. Alert generation
2. Alert correlation
3. Attack classification
4. Response selection
5. Automated/assisted response

**Response Actions**:
- Alert operators
- Isolate compromised components
- Switch to safe mode
- Activate backup systems
- Collect forensic data

## Research Gaps

1. **Adversarial Robustness**: Detection against adaptive attackers
2. **Explainability**: Understanding why anomalies are flagged
3. **Transfer Learning**: Applying detection across different systems
4. **Real-time Constraints**: Meeting latency requirements
5. **Human Factors**: Operator interaction with detection systems

## Tools & Datasets

### Datasets
- SWaT (Secure Water Treatment)
- WADI (Water Distribution)
- Power System Attack Dataset
- CAN Bus Intrusion Dataset

### Tools
- Zeek (network analysis)
- Snort (IDS)
- TensorFlow/PyTorch (ML)
- Matlab/Simulink (model-based)

## References

- Abshari, D., & Sridhar, M. (2025). Cyber-Physical Systems Security: A Comprehensive Review of Anomaly Detection Techniques.
- Cárdenas, A. A., et al. (2011). Attacks against process control systems: Risk assessment, detection, and response.
- Urbina, D. I., et al. (2016). Limiting the impact of stealthy attacks on industrial control systems.
- Feng, C., et al. (2017). A systematic framework to generate invariants for anomaly detection in industrial control systems.

## Related Skills

- `ai-systems-engineering-v-model` - Secure development lifecycle
- `contraction-theory-control-optimization` - Robust control for CPS
- `distributed-quantum-control-systems` - Advanced control theory


## Activation Keywords

- cps-security-anomaly-detection
- cps security anomaly
- cps security anomaly detection


## Tools Used

- `read` - 读取技能文档
- `write` - 创建输出
- `exec` - 执行相关命令


## Instructions for Agents

1. 理解技能的核心方法论
2. 根据用户问题提供针对性回答
3. 遵循最佳实践


## Examples

### Example 1: 基本查询

**User:** 请解释 Cps Security Anomaly Detection

**Agent:** Cps Security Anomaly Detection 是关于...
