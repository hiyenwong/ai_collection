---
name: bsnn-causal-explainability
title: "Binary Spiking Neural Networks as Causal Models"
category: neuroscience
source:
  paper: "Binary Spiking Neural Networks as Causal Models"
  authors:
    - Aditya Kar
    - Emiliano Lorini
    - Timothée Masquelier
  arxiv: "2604.27007"
  date: "2026-04-29"
  fields:
    - cs.AI
description: >
  Causal analysis framework for Binary Spiking Neural Networks (BSNNs) that
  represents spiking activity as a binary causal model, enabling logic-based
  abductive explanations using SAT/SMT solvers. Guarantees explanations
  contain no irrelevant features, unlike SHAP.
keywords:
  - binary spiking neural network
  - BSNN
  - causal model
  - explainable AI
  - SAT solver
  - SMT solver
  - abductive explanation
  - spiking network
  - XAI for SNN
  - logical explanation
  - 二元脉冲神经网络
  - 因果模型
  - 可解释AI
  - 溯因解释
activation_keywords:
  - bsnn causal
  - binary spiking causal model
  - SAT SMT explanation SNN
  - abductive explanation spiking
  - causal spiking neural network
  - 脉冲网络因果解释
  - BSNN 可解释性
---

# BSNN Causal Explainability — Binary Spiking Neural Networks as Causal Models

## Overview

**Binary Spiking Neural Networks (BSNNs)** can be formally represented as **binary causal models**, enabling logic-based abductive explanations of network behavior. This approach uses **SAT** and **SMT solvers** to compute explanations that are **guaranteed to contain no irrelevant features** — a property that popular methods like SHAP cannot guarantee.

- **arXiv**: [2604.27007](https://arxiv.org/abs/2604.27007)
- **Authors**: Aditya Kar, Emiliano Lorini, Timothée Masquelier
- **Date**: 2026-04-29

---

## Key Contributions

1. **Formal BSNN Definition** — Rigorous mathematical formulation of Binary Spiking Neural Networks.
2. **Causal Model Representation** — Spiking activity is encoded as a binary structural causal model (SCM).
3. **SAT-Based Explanations** — Uses Boolean SAT solvers to compute abductive explanations from the causal model.
4. **SMT-Based Explanations** — Uses Satisfiability Modulo Theories solvers for richer constraint-based explanations.
5. **Irrelevance Guarantee** — Unlike SHAP, the logic-based approach guarantees found explanations do not contain completely irrelevant features.
6. **Empirical Validation** — Demonstrated on MNIST classification with pixel-level abductive explanations.

---

## Theoretical Framework

### Binary Spiking Neural Network (BSNN)

A BSNN is defined as a network where:
- Each neuron has a **binary state**: spiking (1) or non-spiking (0)
- Synaptic weights are **binary or discretized**
- Spike propagation follows deterministic update rules
- Temporal dynamics are captured through discrete timesteps

### Causal Model Representation

The BSNN spiking activity is represented as a **Structural Causal Model (SCM)**:

```
M = ⟨U, V, F⟩

where:
  U = exogenous variables (input stimuli)
  V = endogenous variables (neuron spike states)
  F = structural equations (neuron update rules)
```

Each neuron's spike state at time t is a function of:
- Its previous state
- Incoming spikes from presynaptic neurons
- Synaptic weights
- Threshold parameters

### Abductive Explanation

Given an observed output (classification), an **abductive explanation** is a minimal set of input features (pixel values) that, when fixed, guarantee the same output regardless of other features.

Formally: An explanation E ⊆ X is a subset of input features such that:
```
∀x' ∈ X: if x'_E = x_E then f(x') = f(x)
```

Where f is the BSNN classifier, x is the original input, and x' is any input agreeing with x on features in E.

---

## SAT/SMT-Based Explanation Computation

### SAT-Based Approach

1. **Encode BSNN as Boolean Formula**:
   - Each neuron spike → Boolean variable
   - Synaptic connections → logical implications
   - Threshold rules → CNF clauses

2. **Query for Minimal Explanation**:
   - Fix the output class to the observed prediction
   - Find minimal subset of input pixels that force this output
   - Use iterative SAT solving with cardinality constraints

3. **Algorithm**:
```
Input: BSNN M, input x, output class c
1. Encode M as Boolean formula φ
2. Assert φ ∧ (output = c) ∧ (input pixels = x)
3. For each pixel p in input:
   a. Temporarily unfix p
   b. Check if SAT formula is still satisfiable with output = c
   c. If yes, p is irrelevant → remove from explanation
   d. If no, p is necessary → keep in explanation
4. Return minimal set of necessary pixels
```

### SMT-Based Approach

The SMT approach extends SAT by supporting:
- **Arithmetic constraints** on membrane potentials
- **Temporal logic** for spike timing
- **Theory of arrays** for weight matrices

This allows richer explanations that can reference:
- Specific spike timing patterns
- Membrane potential thresholds
- Synaptic weight magnitudes

---

## Comparison with SHAP

| Property | SAT/SMT Approach | SHAP |
|----------|-----------------|------|
| Irrelevant feature guarantee | ✅ Yes | ❌ No |
| Minimal explanation | ✅ Yes | ❌ Approximate |
| Logical soundness | ✅ Proven | ❌ Heuristic |
| Computation time | Slower (solver-based) | Faster (approximation) |
| Temporal reasoning | ✅ Native (SMT) | ❌ Not supported |
| Feature interaction | ✅ Explicit | ❌ Additive approx |

---

## Implementation Examples

### SAT-Based Explanation with PySAT

```python
from pysat.solvers import Glucose3
from pysat.card import CardEnc
import numpy as np

class BSNNCausalExplainer:
    """SAT-based abductive explanation for BSNNs."""
    
    def __init__(self, bsnn_model):
        self.model = bsnn_model
        self.n_input = bsnn_model.input_size
        self.n_neurons = bsnn_model.total_neurons
    
    def encode_bsnn_as_cnf(self):
        """Encode BSNN structure as CNF formula."""
        cnf_clauses = []
        
        # Neuron variables: v(t, n) = neuron n spikes at time t
        # Synaptic variables: w(i, j) = connection from neuron i to j
        # Input variables: x(p) = pixel p is active
        
        for t in range(self.model.timesteps):
            for n in range(self.n_neurons):
                # LIF threshold condition as CNF
                # If weighted input sum >= threshold, then spike
                v_t_n = self._var_spike(t, n)
                
                # Get presynaptic connections
                presynaptic = self.model.get_presynaptic(n)
                
                if not presynaptic:
                    continue
                
                # Threshold clause: if enough presynaptic spikes → neuron fires
                for combo in self._threshold_combinations(presynaptic):
                    clause = [self._var_spike(t-1, p) for p in combo] + [-v_t_n]
                    cnf_clauses.append(clause)
        
        return cnf_clauses
    
    def compute_abductive_explanation(self, input_image, predicted_class):
        """
        Find minimal set of input pixels that explain the prediction.
        Uses iterative SAT solving.
        """
        # Step 1: Encode the BSNN
        cnf = self.encode_bsnn_as_cnf()
        
        # Step 2: Fix the input
        input_clauses = self._encode_input(input_image)
        cnf.extend(input_clauses)
        
        # Step 3: Fix the output
        output_clauses = self._encode_output(predicted_class)
        cnf.extend(output_clauses)
        
        # Step 4: Find minimal explanation
        necessary_pixels = set(range(self.n_input))
        
        with Glucose3(bootstrap_with=cnf) as solver:
            if not solver.solve():
                raise ValueError("Model inconsistent with input/output")
            
            # Iteratively test each pixel
            for pixel in range(self.n_input):
                if input_image[pixel] == 0:
                    continue  # Skip inactive pixels
                
                # Temporarily remove this pixel constraint
                test_cnf = [c for c in cnf if not self._clause_depends_on_pixel(c, pixel)]
                
                with Glucose3(bootstrap_with=test_cnf) as test_solver:
                    if not test_solver.solve():
                        # Pixel is necessary — keep it
                        pass
                    else:
                        # Pixel is irrelevant — remove from explanation
                        necessary_pixels.discard(pixel)
        
        return necessary_pixels
    
    def _var_spike(self, timestep, neuron_idx):
        """Return SAT variable index for neuron spike."""
        return timestep * self.n_neurons + neuron_idx + 1
    
    def _encode_input(self, image):
        """Encode input image as CNF clauses."""
        clauses = []
        for p, val in enumerate(image.flatten()):
            var = p + 1
            clauses.append([var] if val > 0.5 else [-var])
        return clauses
    
    def _encode_output(self, class_idx):
        """Encode output class as CNF clauses."""
        # Depends on output encoding scheme
        return [[self._var_spike(self.model.timesteps-1, class_idx)]]


# ── Usage Example ──────────────────────────────────────────────
# Assuming a trained BSNN on MNIST
# bsnn = load_trained_bsnn("mnist_bsnn.pkl")
# explainer = BSNNCausalExplainer(bsnn)
# 
# image = mnist_test[0]  # Single MNIST image
# prediction = bsnn.predict(image)
# 
# explanation = explainer.compute_abductive_explanation(image, prediction)
# print(f"Prediction: {prediction}")
# print(f"Explaining pixels: {len(explanation)} / {image.size}")
# 
# # Visualize explanation
# mask = np.zeros(image.shape, dtype=bool)
# mask.flat[list(explanation)] = True
# visualize(image, mask)
```

### SMT-Based Explanation with Z3

```python
from z3 import *

class BSNNSMTExplainer:
    """SMT-based explanation for BSNNs with temporal reasoning."""
    
    def __init__(self, bsnn_model):
        self.model = bsnn_model
        self.solver = Solver()
    
    def build_smt_model(self):
        """Build SMT model of BSNN with temporal dynamics."""
        # Variables for each neuron at each timestep
        self.v = {}
        self.membrane = {}
        
        for t in range(self.model.timesteps):
            for n in range(self.model.n_neurons):
                # Binary spike variable
                self.v[(t, n)] = Bool(f"spike_{t}_{n}")
                # Membrane potential (real-valued for SMT)
                self.membrane[(t, n)] = Real(f"mem_{t}_{n}")
        
        # Structural equations
        for t in range(1, self.model.timesteps):
            for n in range(self.model.n_neurons):
                # LIF dynamics: V(t) = decay * V(t-1) + sum(w * spikes)
                decay = RealVal(self.model.tau_mem)
                input_current = Sum([
                    RealVal(self.model.weights[p, n]) *
                    If(self.v[(t-1, p)], RealVal(1), RealVal(0))
                    for p in self.model.get_presynaptic(n)
                ])
                
                # Membrane update equation
                self.solver.add(
                    self.membrane[(t, n)] ==
                    decay * self.membrane[(t-1, n)] + input_current
                )
                
                # Spike threshold
                self.solver.add(
                    self.v[(t, n)] ==
                    (self.membrane[(t, n)] >= RealVal(self.model.threshold))
                )
    
    def find_temporal_explanation(self, input_image, output_class):
        """
        Find explanation that accounts for spike timing patterns.
        Returns: (necessary_pixels, spike_timing_pattern)
        """
        self.build_smt_model()
        
        # Fix input
        for p, val in enumerate(input_image.flatten()):
            self.solver.add(
                self.v[(0, p)] == (val > 0.5)
            )
        
        # Fix output
        self.solver.add(self.v[(self.model.timesteps-1, output_class)])
        
        # Check satisfiability
        if self.solver.check() == unsat:
            return None
        
        model = self.solver.model()
        
        # Extract spike timing for explanation
        spike_times = {}
        for t in range(self.model.timesteps):
            for n in range(self.model.n_neurons):
                if model.evaluate(self.v[(t, n)]):
                    if n not in spike_times:
                        spike_times[n] = []
                    spike_times[n].append(t)
        
        return spike_times
```

---

## When to Use This Skill

- **Explainable AI for spiking networks** when SHAP/LIME guarantees are insufficient
- **Causal analysis** of BSNN decision-making
- **Safety-critical applications** where explanation correctness is mandatory
- **Neuroscience-inspired AI interpretability** research
- **Formal verification** of spiking neural network behavior
- **Pixel-level or feature-level abductive explanations** for classification tasks

---

## Limitations

1. **Computational cost**: SAT/SMT solving is NP-hard; scales poorly with network size
2. **Binary restriction**: Current formulation requires binary neurons/weights
3. **Temporal depth**: Deep temporal unfolding increases formula size exponentially
4. **Approximate networks**: May not work directly with analog SNNs without discretization

---

## References

- Kar, A., Lorini, E., & Masquelier, T. (2026). "Binary Spiking Neural Networks as Cual Models." arXiv:2604.27007 [cs.AI].
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference.* Cambridge University Press.
- Shih, A., Choi, A., & Darwiche, A. (2018). "A Boolean Approach to Fairness." *IJCAI*.

---

## Related Skills

- [[snn-learning-survey]] — Comprehensive SNN learning rules
- [[spiking-computational-neuroscience-survey]] — SNN computational neuroscience
- [[explainable-gnn-eeg-neurological]] — Explainable GNN for neurological evaluation
- [[binary-spiking-causal-models]] — Causal analysis of BSNNs
