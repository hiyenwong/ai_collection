---
name: intervention-aware-quantum-predictive-control
description: Intervention-aware variational quantum differentiable predictive control with safety attribution. Trains compact VQC policies under primal-dual intervention budget that penalizes reliance on safety filters. Based on arXiv:2606.09778.
version: 1.0
created: 2026-06-09
source: arXiv:2606.09778
category: quantum-control
tags:
  - quantum-control
  - model-predictive-control
  - safety-attribution
  - variational-quantum-circuits
  - control-barrier-functions
---

# Intervention-Aware Quantum Predictive Control with Safety Attribution

## Background

Hard safety filters are increasingly placed downstream of learned controllers to guarantee constraint satisfaction at runtime. Yet a filtered controller that never violates constraints may have learned nothing about safety — the filter silently repairs an incompetent policy, so post-filter success measures the filter, not the policy.

**Key question**: Who earns the safety — the policy or its protective layers?

arXiv:2606.09778 introduces **IA-VQC-DPC** (Intervention-Aware Variational Quantum Differentiable Predictive Control) that:
1. Trains a compact VQC policy under a **primal-dual intervention budget** penalizing reliance on CBF projection
2. Evaluates with a **safety attribution protocol** decomposing trajectory correction into CBF and deployment guard terms

## Core Methodology

### Intervention-Aware Training

The training objective combines control performance with an intervention penalty:

```
L_total = L_control + λ · L_intervention

L_intervention = Σ_t ||u_CBF(t) - u_VQC(t)||²
```

Where u_CBF is the safety-filtered action and u_VQC is the raw quantum policy output. The primal-dual budget dynamically adjusts λ to ensure the quantum policy learns safety constraints intrinsically.

### Safety Attribution Protocol

Post-training evaluation decomposes executed trajectory corrections:

1. **CBF correction term**: How much the Control Barrier Function had to intervene
2. **Deployment guard term**: Runtime safety guard corrections
3. **Guard-off evaluation**: Stress-test with safety layers disabled

### VQC Policy Architecture

- Compact variational quantum circuit (~400 parameters)
- Encoding: system state → quantum state via amplitude or angle encoding
- Ansatz: hardware-efficient layers with entangling gates
- Measurement: expectation values → control actions

## Key Results

- At equal ~400 parameter budget, quantum policy is **significantly safer and more comfortable** than matched classical policy (p < 10⁻⁴)
- Intervention-aware training **lowers raw pre-filter violation** and **total safety-layer reliance**
- Guard-off evaluation confirms improvement is **policy-level**, not filter-level
- **Negative result**: learned differentiable energy head is only safe when paired with distribution-aware runtime guard

## Implementation Steps

### Step 1: VQC Policy with Intervention Awareness

```python
import pennylane as qml
import numpy as np

def build_vqc_policy(n_qubits, n_layers, state_dim, action_dim):
    """Build compact VQC policy for predictive control."""
    
    dev = qml.device("default.qubit", wires=n_qubits)
    
    @qml.qnode(dev)
    def policy_circuit(state, params):
        # State encoding
        for i in range(min(n_qubits, state_dim)):
            qml.RY(state[i], wires=i)
        
        # Variational layers
        for layer in range(n_layers):
            for i in range(n_qubits):
                qml.Rot(*params[layer, i, :3], wires=i)
            for i in range(n_qubits - 1):
                qml.CNOT(wires=[i, i + 1])
        
        # Measurement → action
        actions = []
        for i in range(action_dim):
            actions.append(qml.expval(qml.PauliZ(i % n_qubits)))
        return actions
    
    return policy_circuit
```

### Step 2: Intervention-Aware Training Loop

```python
def intervention_aware_training(
    vqc_policy, 
    safety_filter, 
    env, 
    n_episodes,
    intervention_budget=0.1
):
    """Train VQC policy with intervention-aware loss."""
    
    lambda_intervention = 1.0  # primal variable
    dual_penalty = 0.0  # dual variable
    
    for episode in range(n_episodes):
        state = env.reset()
        total_intervention = 0
        
        for t in range(env.horizon):
            # VQC policy action
            u_vqc = vqc_policy(state)
            
            # Safety-filtered action
            u_safe, cbf_correction = safety_filter(u_vqc, state)
            total_intervention += np.linalg.norm(cbf_correction)**2
            
            # Execute safe action
            next_state, reward, done, _ = env.step(u_safe)
            
            # Intervention-aware loss
            loss = -reward + lambda_intervention * total_intervention / env.horizon
        
        # Primal-dual update
        dual_penalty += intervention_budget - total_intervention / env.horizon
        lambda_intervention = max(0, lambda_intervention + dual_penalty * 0.01)
    
    return vqc_policy
```

### Step 3: Safety Attribution Evaluation

```python
def safety_attribution_evaluation(policy, env, n_episodes, guard_off=False):
    """Evaluate policy with safety attribution decomposition."""
    
    results = {
        "cbf_corrections": [],
        "guard_corrections": [],
        "violations": [],
        "energy_consumption": []
    }
    
    for _ in range(n_episodes):
        state = env.reset()
        for t in range(env.horizon):
            u_raw = policy(state)
            
            if guard_off:
                u_executed = u_raw
                cbf_correction = 0
                guard_correction = 0
            else:
                u_safe, cbf_correction = cbf_filter(u_raw, state)
                u_executed, guard_correction = runtime_guard(u_safe, state)
            
            results["cbf_corrections"].append(np.linalg.norm(cbf_correction))
            results["guard_corrections"].append(np.linalg.norm(guard_correction))
            results["violations"].append(check_violations(u_executed, state))
        
    return results
```

## When to Use

- Quantum control policies where safety is critical (building control, robotics, process control)
- When you need to distinguish policy-level safety from filter-level safety
- Comparing quantum vs classical control policies at equal parameter budgets
- Any learned controller downstream of safety filters

## Activation Triggers

- "quantum predictive control", "VQC control", "quantum MPC"
- "safety attribution", "intervention-aware training", "CBF quantum"
- "control barrier function quantum", "safe quantum learning"
- "quantum policy safety", "primal-dual intervention"

## Pitfalls

1. **Intervention budget too tight**: Policy may not learn effective control if budget is too restrictive. Start loose, tighten gradually.
2. **Guard-off evaluation essential**: Without it, you cannot distinguish policy improvement from filter effectiveness.
3. **Distribution-aware runtime guard**: A learned energy head alone is NOT safe — must pair with distribution-aware guard.
4. **Parameter matching**: Fair comparison requires equal parameter budgets between quantum and classical policies.

## References

- arXiv:2606.09778 — "Who Earns the Safety? Intervention-Aware Quantum Predictive Control with Safety Attribution" (June 2026)
- BOPTEST building-control emulator for evaluation
- Control Barrier Functions (CBF) for safety filtering
