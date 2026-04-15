---
name: data-poisoning-informativity-observability
description: "Data poisoning attacks against informativity-based analysis for observability in data-driven control systems. Invariance-based attack synthesis using invertible linear transformations. Activation: data poisoning, cyber attack control, observability attack, informativity analysis attack."
---

# Data Poisoning Attacks on Informativity for Observability

## Overview

This methodology studies cyber attacks against informativity-based analysis in data-driven control systems, focusing on strong observability. The adversary post-processes finite time-series data using invertible linear transformations that are undetectable by standard analysis methods.

## Core Methodology

### 1. Attack Model

**Adversary Capabilities**:
- Post-processes finite time-series data matrices
- Applies invertible linear transformations
- Acts on data after collection, before analysis

**Attack Goal**: Compromise observability analysis without detection

### 2. Informativity-Based Analysis

**Background**: Data-driven control methods use finite data to determine system properties (controllability, observability) without explicit model identification.

**Vulnerability**: Linear transformations of data preserve certain statistical properties while altering system identification.

### 3. Attack Characterization

**Undetectable Transformations**:
```
Given data matrix D, adversary applies: D' = T · D

Where T is invertible and preserves:
- Data covariance structure
- Statistical moments
- Rank properties (under certain conditions)
```

**Observable System Compromise**:
- Original data: System is observable
- Transformed data: Observability appears compromised
- Detection: Standard tests cannot distinguish D from D'

### 4. Worst-Case Attack Synthesis

**Optimization Problem**:
```
Minimize: rank(O_obs)  [Observability matrix rank]
Subject to:
  - T is invertible
  - T preserves data informativity
  - Attack is stealthy (LMI constraints)
```

**Solution Method**: Convex relaxation of rank minimization

```python
# Attack synthesis algorithm
def synthesize_attack(data_matrix, system_dim):
    """
    Synthesize worst-case data poisoning attack
    
    Args:
        data_matrix: Original time-series data
        system_dim: System dimension
    
    Returns:
        transformation: Invertible attack matrix T
        compromised_data: T · data_matrix
    """
    # Formulate as rank minimization with LMI constraints
    # Solve via convex relaxation (nuclear norm minimization)
    # Return transformation matrix
    pass
```

## Mathematical Framework

### Strong Observability

A system is strongly observable if the initial state can be uniquely determined from input-output data over finite time.

**Observability Matrix**:
```
O = [C; CA; CA²; ...; CA^(n-1)]

Rank condition: rank(O) = n (system dimension)
```

### Invariance Properties

**Theorem**: Invertible linear transformations of data matrices preserve:
1. Row space dimension
2. Certain correlation structures
3. Informativity for some (but not all) system properties

**Attack Space**: All T ∈ GL(n) such that transformed data appears valid

## Defense Strategies

### 1. Data Authentication

- Cryptographic signatures on sensor data
- Hardware-level attestation
- Secure data collection protocols

### 2. Redundancy-Based Detection

```python
def detect_anomaly_with_redundancy(data_sources):
    """
    Detect data poisoning using redundant sensors
    """
    # Compare informativity analysis across multiple sources
    # Flag inconsistencies as potential attacks
    pass
```

### 3. Robust Informativity Analysis

- Statistical outlier detection
- Bounded error analysis
- Interval-based observability tests

## Applications

### Power Systems Example

**Scenario**: State estimation from smart meter data

**Attack**: Compromise observability to hide grid instabilities

**Impact**: Cascading failures due to undetected system state

```python
# Power system observability analysis
def power_system_observability(grid_data):
    """
    Analyze observability of power grid state
    
    Vulnerable to: Data poisoning on meter readings
    Defense: Multi-source data validation
    """
    pass
```

## Activation Keywords

- data poisoning control systems
- cyber attack observability
- informativity analysis attack
- data-driven control security
- stealthy control attack
- rank minimization attack

## Reference

- **Paper**: Data Poisoning Attacks on Informativity for Observability: Invariance-Based Synthesis
- **Authors**: Iori Takaki, Ahmet Cetinkaya, Hideaki Ishii
- **arXiv**: [2604.11657](https://arxiv.org/abs/2604.11657) (2026-04-13)
- **Category**: eess.SY (Systems and Control)

## Tools Used

- Python 3.x with NumPy, SciPy
- CVXPY (for convex optimization)
- Control systems toolbox (optional)

## Instructions for Agents

### Defensive Analysis Workflow

1. **Load Data**: Import time-series data from sensors
2. **Check Informativity**: Verify data contains enough information for observability analysis
3. **Test Transformations**: Apply various linear transformations to test robustness
4. **Validate Results**: Cross-check with redundant data sources
5. **Document Findings**: Record any anomalies or vulnerabilities

### Security Assessment Steps

```python
# 1. Load sensor data
data = load_sensor_data('power_grid.csv')

# 2. Check observability informativity
observable = check_observability(data)

# 3. Test against attack transformations
for T in generate_test_transformations():
    compromised_data = T @ data
    compromised_observable = check_observability(compromised_data)
    if observable != compromised_observable:
        alert(f"Vulnerability detected with transformation {T}")

# 4. Implement defense
if vulnerable:
    deploy_redundancy_measures()
```

## Error Handling

### Analysis Failures

1. **Rank Deficiency**: Data matrix is rank-deficient
   - **Cause**: Insufficient sensor diversity
   - **Solution**: Add more sensors or collect longer time series

2. **Non-Invertible Transformation**: T is singular
   - **Cause**: Poorly conditioned data
   - **Solution**: Regularization or data preprocessing

3. **Numerical Instability**: LMI solver fails
   - **Cause**: Badly scaled problem
   - **Solution**: Normalize data matrices

### Defense Failures

1. **Redundancy Mismatch**: Multiple sensors disagree
   - **Action**: Use voting mechanism or median filter
   
2. **False Positives**: Legitimate data flagged as attack
   - **Action**: Adjust detection thresholds

## Related Skills

- cps-security-anomaly-detection
- automated-cps-testing-act
- control-systems

## Examples

**User**: "Analyze power grid data for potential data poisoning vulnerabilities in observability analysis"

**Agent**: I'll perform a security assessment of your power grid data against data poisoning attacks on observability.

```python
# 1. Load sensor data
grid_data = load_sensor_data('power_grid.csv')

# 2. Check observability informativity
observable = check_observability(grid_data)
print(f"System observable: {observable}")

# 3. Test against attack transformations
vulnerabilities = []
for T in generate_test_transformations():
    compromised_data = T @ grid_data
    compromised_observable = check_observability(compromised_data)
    if observable != compromised_observable:
        vulnerabilities.append(T)
        alert(f"Vulnerability detected with transformation {T}")

# 4. Assess vulnerability level
if len(vulnerabilities) > 0:
    print(f"Found {len(vulnerabilities)} potential attack vectors")
    deploy_redundancy_measures()
else:
    print("No vulnerabilities detected with tested transformations")
```

This defensive analysis helps identify and mitigate data poisoning risks before attackers exploit them.

## Implementation Notes

1. **Ethical Considerations**: This methodology is for defensive analysis
2. **Detection Difficulty**: Attacks are mathematically stealthy
3. **Mitigation Priority**: Focus on prevention and redundancy
4. **Domain Application**: Critical infrastructure protection
