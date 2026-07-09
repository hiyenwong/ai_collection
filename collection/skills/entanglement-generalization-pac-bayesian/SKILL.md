---
name: entanglement-generalization-pac-bayesian
description: |
  PAC-Bayesian analysis framework for generalization in quantum policies and value functions. 
  Reveals that generalization is governed by Fisher geometry effective dimension rather than raw parameter count.
  Entanglement inflates Fisher effective dimension, making it an independent axis of complexity.
  Use when: (1) analyzing quantum policy generalization, (2) designing parameterized quantum circuits for RL,
  (3) evaluating train-test gaps in quantum ML, (4) studying entanglement-complexity trade-offs,
  (5) certifying quantum circuit generalization. Trigger words: PAC-Bayesian quantum, Fisher geometry,
  entanglement generalization, quantum policy design, quantum value function generalization, train-test gap quantum.
---

# Entanglement-Generalization Trade-off (PAC-Bayesian View)

## Core Finding

Generalization in quantum RL policies is **not** predicted by raw parameter count.
Instead, it is governed by the **Fisher geometry effective dimension** induced by the circuit.

**Key mechanism:** Entanglement inflates Fisher effective dimension.
- Higher entanglement → larger Fisher effective dimension → larger train-test gaps
- Parameter count is a weak predictor
- Entangling connectivity is an independent axis of complexity

## PAC-Bayesian Bound

The PAC-Bayesian bound acts as a **ranking certificate**:
- Correctly orders circuits with identical parameter count (which parameter-counting bounds cannot do)
- Entangled circuits generalize worse than non-entangled circuits of equal parameter count
- Gaps shrink as sample size increases

## Empirical Validation

- Validated on: supervised classification, quantum contextual bandits, value-function generalization
- Strongest evidence: low-variance decision models (single-observable classifiers, value heads, one-step policies)
- Multi-step policy learning: entanglement effects statistically significant but high return variance partially obscures ordering
- Validated on IBM Heron quantum processor under real noise

## Design Implications

1. **Reframe quantum policy design** around entanglement-generalization trade-off, not expressivity alone
2. **Minimize unnecessary entanglement** in policy circuits when generalization is critical
3. **Use Fisher effective dimension** as a complexity metric instead of parameter count
4. **Partial-correlation analysis**: Fisher effective dimension screens off entangling pattern

## Circuit Design Guidelines

| Circuit Type | Fisher Eff. Dim. | Generalization | Recommendation |
|-------------|------------------|----------------|----------------|
| Low entanglement | Low | Good | Use when generalization matters |
| High entanglement | High | Poor | Use when expressivity is primary |
| Non-entangled | Minimal | Best | Baseline for comparison |

## Activation Keywords

- PAC-Bayesian quantum, Fisher geometry, entanglement generalization
- quantum policy design, quantum value function generalization
- train-test gap quantum, quantum circuit complexity
