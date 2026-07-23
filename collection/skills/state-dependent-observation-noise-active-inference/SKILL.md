---
name: state-dependent-observation-noise-active-inference
description: State-Dependent Observation Noise methodology that reintroduces epistemic value in Linear-Gaussian Active Inference models. This skill provides the mathematical framework and implementation guidance for restoring curiosity-driven behavior in Gaussian agents by introducing state-dependent observation noise covariance R(x). Use when working with active inference, Bayesian filtering, dual control theory, or neural dynamics models where epistemic drive has been lost in standard linear-Gaussian formulations.
license: Complete terms in LICENSE.txt
---

# State-Dependent Observation Noise in Active Inference

## Overview

This methodology addresses a fundamental limitation in linear-Gaussian active inference: the loss of epistemic drive (curiosity) under standard formulations. Recent work established that linear-Gaussian state-space models lose their epistemic incentive "under any circumstances" because the Expected Free Energy's epistemic term becomes constant, reducing the agent to a fixed Kalman filter.

**Key insight**: State-dependent observation noise covariance R(x) that varies with the state x (representing sensor accuracy degrading with range) restores epistemic value by making the posterior covariance and Kalman gain dependent on actions.

## Mathematical Framework

### Problem Statement
In standard linear-Gaussian active inference:
- Dynamics: x_{t+1} = Ax_t + Bu_t + w_t, w_t ~ N(0, Q)
- Observations: y_t = Cx_t + v_t, v_t ~ N(0, R)  
- **Issue**: R is constant → epistemic term constant → no information-seeking behavior

### Solution: State-Dependent Observation Noise
- Modified observations: y_t = Cx_t + v_t, v_t ~ N(0, R(x_t))
- Where R(x) represents sensor accuracy that degrades with state (e.g., range-dependent measurement noise)
- Agent uses standard first-order Gaussian filter with R evaluated at predicted mean: R(μ̂_t)

### Key Results
1. **Dual Effect Restoration**: Actions now influence both state evolution AND future estimation quality
2. **Non-Constant Epistemic Value**: Under mild rank condition on C and non-degeneracy of R(x), epistemic value is no longer constant
3. **Scalar Case**: For scalar observations, reachable non-constancy alone suffices
4. **Bar-Shalom-Tse Dual Effect**: This represents the minimal constructive instance of dual control in maintained covariance

## Implementation Guidelines

### Detection of Incompatibility
The companion library `cpomdp v0.4.2` automatically detects model incompatibility:
- Raises `IncompatibleLinearizationError` from model specification alone
- Provides executable witness that would refute both theorem and witness if any fixed filter reproduced the agent

### Practical Applications
1. **Robotics**: Range-dependent sensor noise in LiDAR, cameras, or sonar
2. **Neuroscience**: Modeling attention mechanisms where sensory precision varies with stimulus properties  
3. **Finance**: Volatility-dependent observation noise in market models
4. **Control Systems**: Signal-to-noise ratio varying with system state

### Algorithm Steps
1. Define state-dependent observation covariance R(x)
2. Implement Gaussian filter using R(μ̂_t) where μ̂_t is predicted state mean
3. Compute Expected Free Energy with action-dependent posterior covariance
4. Optimize actions to balance extrinsic (utility) and intrinsic (information) objectives

## Verification

The methodology includes an executable witness:
- Any attempt to reproduce the agent with a fixed linear-Gaussian filter would simultaneously refute both the theorem and the witness
- This provides precise, observation-side characterization of curiosity in Gaussian agents

## References

- **Primary Paper**: Corva, D. (2026). "State-Dependent Observation Noise Reintroduces Epistemic Value in Linear-Gaussian Active Inference." arXiv:2607.20306 [q-bio.NC]
- **Companion Software**: cpomdp v0.4.2 (archived repository available)
- **Theoretical Foundation**: Bar-Shalom & Tse (1974) dual effect theory
- **Active Inference**: Friston et al. Expected Free Energy framework

## Activation Keywords

- state-dependent observation noise
- active inference epistemic value  
- linear-gaussian curiosity
- dual control bar-shalom-tse
- gaussian agent curiosity
- observation noise covariance
- expected free energy epistemic

## Related Skills

- active-inference-framework
- kalman-filter-extensions  
- dual-control-theory
- bayesian-filtering-neuroscience
- computational-neuroscience-models