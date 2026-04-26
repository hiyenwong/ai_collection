---
name: active-bayesian-sensor-attack-recovery
description: "Active Bayesian inference framework for robust control under sensor false data injection attacks. Models perception pipelines as bipartite graphs with Bayesian networks for attack detection, inference, and recovery. 激活词: active Bayesian inference, sensor attacks, false data injection, robust control"
category: systems-engineering
date_created: 2026-04-14
source_paper: arXiv:2604.11410
---

# Active Bayesian Inference for Sensor Attack Recovery

## Overview

Framework for bridging the gap between sensor attack detection and recovery in cyber-physical systems.

## Problem Statement

**Challenge**: Modern CPS with complex perception pipelines face sensor false data injection attacks. Detection alone is insufficient without recovery.

## System Model

### Perception Pipeline as Bipartite Graph

**Graph Structure**:
```
G = (S, X, E)
- S: Sensors
- X: State components
- E: Influence edges
```

## Bayesian Network Framework

### Inference

**Belief Propagation**:
```
P(S_i = 0 | A) = b_{S_i}(0)
```

### Active Inference

**Information Gain**:
```
IG(q) = H(S | A) - E[H(S | A, A_q)]
```

### Recovery

**State Reconstruction**:
- Maximum likelihood estimation from healthy sensors
- Kalman filter with sensor selection
- Controller adaptation

## Algorithm

```python
class ActiveBayesianController:
    def step(self, measurements, alerts):
        # 1. Detect and infer compromised sensors
        compromised, beliefs = self.detect_and_infer(measurements, alerts)
        
        # 2. Active query if uncertain
        if self.uncertainty_high(beliefs):
            queries = self.active_query(beliefs)
            
        # 3. Recover and control
        control, state = self.recover_and_control(measurements, compromised)
        
        return control
```

## Applications

- Autonomous vehicle security
- Industrial control systems
- Sensor fusion security
- CPS protection

## Activation Keywords

active Bayesian inference, sensor attacks, false data injection, robust control, cyber-physical security, graceful degradation
