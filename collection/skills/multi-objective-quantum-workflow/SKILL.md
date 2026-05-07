---
name: multi-objective-quantum-workflow
description: >
  Multi-objective optimization methodology for quantum computing workflows,
  combining compilation strategy selection, noise suppression, and error-mitigation.
  Based on QBalance framework (arXiv: 2605.02966) and action-space engineering for
  RL-based circuit routing (arXiv: 238). Use when: designing quantum compilation
  pipelines, optimizing NISQ device execution, selecting error-mitigation strategies,
  or formulating multi-objective quantum workflow problems.
  Activation: quantum workflow, quantum compilation optimization, multi-objective quantum,
  QBalance, quantum error mitigation strategy, NISQ workflow, quantum circuit routing.
---

# Multi-Objective Quantum Workflow Optimization

## Core Concept

Near-term quantum workloads involve coupled decisions across compilation, noise suppression,
and error mitigation. Frame these as **finite multi-objective strategy-selection problems**
over circuits, backends, and transformation policies.

## Problem Formulation

Given a set of circuits C, backends B, and transformation policies T:

```
minimize  f(c, b, t) = w1·error(c,b,t) + w2·latency(c,b,t) + w3·cost(c,b,t)
subject to t ∈ T, b ∈ B, c ∈ C
```

Key insight: the strategy space is combinatorial. Use weighted objectives with
non-dominated selection rules and Bayesian surrogate ordering to navigate it.

## Strategy Selection Framework

### Step 1: Define Candidate Strategies

Each strategy is a tuple: `(layout_policy, routing_policy, basis_gates, noise_suppression, error_mitigation)`

Common strategies:
- **SABRE** routing + dynamical decoupling + ZNE
- **Greedy** layout + randomized compiling + M3 mitigation
- **Topology-aware** layout + adaptive DD + PEC

### Step 2: Score with Survival-Product Error Proxy

For each candidate, compute the survival-product proxy:

```
survival_product = ∏_g (1 - ε_g)
```

where ε_g is the estimated error rate for gate g under the candidate strategy.
This provides a lightweight ranking before expensive circuit execution.

### Step 3: Bayesian Candidate Ordering

Use a Bayesian linear surrogate to rank candidates before evaluation:

```
score(c) = E[w · φ(c)] + β · σ(c)
```

- φ(c): feature vector of candidate (circuit depth, gate count, topology match)
- σ(c): uncertainty estimate for exploration-exploitation tradeoff
- β: exploration coefficient (higher for initial rounds)

### Step 4: Non-Dominated Selection

Apply Pareto dominance filtering: candidate A dominates B if A is strictly better
on at least one objective and no worse on all others. Select from the Pareto front.

## Action-Space Engineering for RL-Based Routing

When using reinforcement learning for circuit routing (DQC architectures):

### Action-Space Design Principles

1. **State-dependent actions**: Actions should depend on current qubit placement
2. **Action masking**: Prune invalid actions (e.g., routing non-adjacent qubits)
3. **Modular decomposition**: Separate placement, routing, and execution decisions

### Effective Action Masking

```python
def get_valid_actions(state):
    """Return only valid routing actions given current qubit placement."""
    valid = []
    for q1, q2 in state.coupling_graph.edges():
        if state.needs_interaction(q1, q2):
            valid.append(('swap', q1, q2))
    return valid
```

Action masking reduces the effective action space by 10-100x, improving both
training convergence and inference performance.

## Distributionally Robust Control Integration

For quantum systems with uncertain noise distributions:

### Sinkhorn Ambiguity Sets

Use Sinkhorn discrepancy (regularized OT) to define uncertainty sets:

```
D_ε(ρ || ρ₀) ≤ δ
```

Advantages over Wasserstein:
- Does not constrain worst-case to discrete distributions
- Combines observed data with prior knowledge via reference distribution ρ₀
- Convex and tractable for LQ control problems

### Application to Quantum Control

When designing pulse sequences for quantum gates:
1. Characterize noise from calibration data → empirical distribution ρ_emp
2. Define ambiguity set around ρ_emp using Sinkhorn discrepancy
3. Optimize worst-case gate fidelity over the ambiguity set
4. Results in controllers robust to distributional shifts

## Practical Workflow

### Phase 1: Characterization
1. Profile target backend: gate fidelities, connectivity, coherence times
2. Characterize circuit: depth, width, entanglement structure
3. Estimate baseline error without mitigation

### Phase 2: Strategy Search
1. Generate candidate strategies from combinatorial space
2. Score with survival-product proxy
3. Apply Bayesian ordering for evaluation sequence
4. Execute top-K candidates, collect metrics

### Phase 3: Selection & Execution
1. Build Pareto front from results
2. Select strategy based on priority (fidelity vs. latency vs. cost)
3. Execute with selected strategy
4. Record results for Bayesian model update

## Key Limitations

- Bandit mechanisms order candidates but don't reduce evaluation count
- Greedy layout heuristics are only partially topology-aware
- ZNE implementations are typically parity-centered
- Circuit cutting hooks require full reconstruction pipeline
- RL routing requires state-dependent action masking for efficiency

## Related Patterns

- **quantum-systems-engineering**: Broader quantum system architecture patterns
- **quantum-error-correction-methods**: Error correction code design
- **distributed-quantum-control-systems**: Multi-module quantum control
