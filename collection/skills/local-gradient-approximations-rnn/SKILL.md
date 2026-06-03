---
name: local-gradient-approximations-rnn
description: Dynamics and Representation Structure of Local Approximations to Gradient-Based Learning in Linear Recurrent Neural Networks. Analytical framework comparing RFLO, tBPTT, and BPTT learning dynamics using dynamical systems theory. Key finding: RFLO solutions restricted to low-rank perturbations, with qualitatively distinct convergence behavior.
authors:
  - Ezekiel Williams
  - Alexandre Payeur
  - Guillaume Lajoie
arxiv_id: 2606.00243
date: 2026-06-03
status: camera-ready
conference: ICML 2026
keywords:
  - recurrent neural networks
  - local learning
  - gradient descent
  - RFLO
  - truncated BPTT
  - learning dynamics
  - neuromorphic computing
  - biological learning
  - low-rank representations
subjects:
  - cs.NE (Neural and Evolutionary Computing)
  - q-bio.NC (Neurons and Cognition)
  - stat.ML (Machine Learning)
---

# Local Gradient Approximations in Linear RNNs

## Abstract Summary

This paper applies dynamical systems theory to understand how locality constraints shape learning in biological and neuromorphic RNNs. The authors compare three learning algorithms: **RFLO** (Random Feedback Local Online), **tBPTT** (Truncated Backpropagation Through Time), and **BPTT** (Full Backpropagation Through Time), finding qualitatively distinct behavior for each.

## Key Contributions

### 1. Theoretical Framework

**Data-Aligned Linear RNNs**: The paper leverages a special class of linear RNNs whose dynamics can be separated into orthogonal modes, enabling analytical tractability:
- Separation into fast and slow modes
- Orthogonal decomposition of dynamics
- Stationary solution analysis

### 2. Learning Algorithm Comparison

| Algorithm | Locality Constraint | Key Finding |
|-----------|---------------------|-------------|
| BPTT | None (full backprop) | Gold standard, full gradient |
| tBPTT | Temporal truncation (n steps) | Intermediate behavior |
| RFLO | Spatial + temporal locality | Low-rank perturbations only |

**RFLO Distinctive Properties**:
- Solutions restricted to **low-rank perturbations** of initial parameters
- Convergence to different stationary solutions than BPTT
- Different stability properties and convergence rates

### 3. Representation Structure

**Low-Rank Constraint Discovery**:
- RFLO learning produces solutions that are low-rank perturbations of initial weights
- This constraint holds **beyond the data-aligned setting**
- Implies fundamental limitation on representational capacity under local learning

## Mathematical Framework

### Linear RNN Dynamics

The model: $x_{t+1} = A x_t + B u_t$, $y_t = C x_t$

Key insight: For data-aligned RNNs, dynamics decompose into orthogonal modes:
$$A = \sum_i \lambda_i P_i$$

where $P_i$ are projection operators onto orthogonal subspaces.

### Learning Dynamics Analysis

**Stationary Solutions**: For each algorithm, the paper derives:
1. Fixed point equations for converged weights
2. Stability conditions around stationary points
3. Convergence rate bounds

**RFLO Learning Rule**:
$$\Delta W = \eta \cdot (e_t \cdot x_t^T) \cdot B_{feedback}$$

where $B_{feedback}$ is a random feedback matrix (not the true gradient path).

### Low-Rank Perturbation Proof

**Key Result**: Under RFLO, the learned weight matrix satisfies:
$$W_{final} = W_{init} + \sum_{k=1}^{K} \alpha_k v_k u_k^T$$

where $K$ is much smaller than full dimension, creating an effective low-rank constraint.

## Implementation Guide

### RFLO Training Implementation

```python
import torch
import torch.nn as nn

class RFLOLinearRNN(nn.Module):
    """Random Feedback Local Online learning for linear RNNs."""
    
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.A = nn.Parameter(torch.randn(hidden_dim, hidden_dim) * 0.01)
        self.B = nn.Parameter(torch.randn(hidden_dim, input_dim) * 0.01)
        self.C = nn.Parameter(torch.randn(output_dim, hidden_dim) * 0.01)
        
        # Random feedback weights (fixed, not learned)
        self.B_feedback = torch.randn(hidden_dim, output_dim) * 0.01
        self.B_feedback.requires_grad = False
        
    def forward(self, u_seq):
        """Forward pass through linear RNN."""
        T, batch, input_dim = u_seq.shape
        h = torch.zeros(batch, self.A.shape[0])
        outputs = []
        hidden_states = []
        
        for t in range(T):
            h = self.A @ h.T + self.B @ u_seq[t].T
            h = h.T  # (batch, hidden)
            y = self.C @ h.T
            outputs.append(y.T)
            hidden_states.append(h)
            
        return torch.stack(outputs), torch.stack(hidden_states)
    
    def rflo_update(self, hidden_states, outputs, targets, lr=0.01):
        """Local RFLO weight update - no backprop needed."""
        T, batch, hidden_dim = hidden_states.shape
        
        # Local error at each timestep
        for t in range(T):
            e_t = targets[t] - outputs[t]  # (batch, output_dim)
            h_t = hidden_states[t]  # (batch, hidden_dim)
            
            # RFLO update: use random feedback instead of true gradient
            # ΔA = η * (B_feedback @ e_t) * h_t^T
            delta_A = lr * (self.B_feedback @ e_t.T) @ h_t.unsqueeze(-1)
            delta_B = lr * (self.B_feedback @ e_t.T) @ u_seq[t].unsqueeze(-1)
            
            self.A.data += delta_A.mean(0)
            self.B.data += delta_B.mean(0)
            
        # C uses true gradient (output layer)
        for t in range(T):
            e_t = targets[t] - outputs[t]
            h_t = hidden_states[t]
            self.C.data += lr * e_t.T @ h_t
```

### Truncated BPTT Implementation

```python
class TruncatedBPTTRNN(nn.Module):
    """Truncated Backpropagation Through Time with n-step truncation."""
    
    def __init__(self, input_dim, hidden_dim, output_dim, truncate_steps=5):
        super().__init__()
        self.truncate_steps = truncate_steps
        self.rnn = nn.RNN(input_dim, hidden_dim, nonlinearity='linear')
        self.output = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, u_seq):
        """Forward with truncated gradient propagation."""
        # Detach hidden state every truncate_steps
        h = None
        outputs = []
        
        for t in range(u_seq.shape[0]):
            if t % self.truncate_steps == 0 and h is not None:
                h = h.detach()  # Truncate gradient flow
            
            out, h = self.rnn(u_seq[t].unsqueeze(0), h)
            outputs.append(self.output(out))
            
        return torch.stack(outputs)
```

## Experimental Validation

### Datasets
- Linear regression tasks with varying temporal dependencies
- Sequence prediction with controlled eigenvalue spectra
- Orthogonal mode separation tests

### Metrics
- **Convergence rate**: Time to reach stationary solution
- **Solution rank**: Effective dimensionality of learned weights
- **Stability**: Jacobian eigenvalues at fixed points
- **Task performance**: Final loss achieved

## Key Findings

### 1. Convergence Behavior

**BPTT**: Smooth convergence to global optimum (for linear case)
**tBPTT**: Intermediate convergence, depends on truncation depth
**RFLO**: Converges to different stationary point, slower but stable

### 2. Stability Properties

The stability matrix eigenvalues differ qualitatively:
- BPTT: Eigenvalues determined by true gradient structure
- RFLO: Eigenvalues reflect feedback matrix structure
- This creates different basins of attraction

### 3. Low-Rank Constraint Implications

**Practical Impact**:
- RFLO cannot learn full-rank solutions
- Representational capacity limited by locality
- May be beneficial for regularization
- Aligns with biological observations of low-rank neural representations

## Applications

### Neuromorphic Computing
- Hardware-friendly local learning rules
- Reduced memory requirements (no full backprop storage)
- Energy-efficient training

### Biological Learning Models
- Explains constraints on cortical learning
- Supports theories of local synaptic plasticity
- Connects to experimental observations

### Machine Learning
- Novel regularization through locality
- Alternative optimization landscapes
- Potential for continual learning applications

## Related Work

1. **Lillicrap et al. (2016)**: Random feedback alignment
2. **Marschall et al. (2020)**: RFLO learning theory
3. **Bengio et al. (1994)**: Truncated BPTT analysis
4. **Kros et al. (2022)**: QIF neuron gradient continuity

## Limitations

1. Analysis limited to linear RNNs (nonlinear case more complex)
2. Assumes data-aligned structure (special condition)
3. RFLO performance gap vs BPTT on complex tasks
4. Low-rank constraint may limit task performance

## Future Directions

1. Extend analysis to nonlinear RNNs
2. Combine RFLO with adaptive feedback learning
3. Study low-rank solutions in biological networks
4. Develop hybrid algorithms (local + occasional global updates)

## References

```bibtex
@article{williams2026local,
  title={Dynamics and Representation Structure of Local Approximations to Gradient-Based Learning in Linear Recurrent Neural Networks},
  author={Williams, Ezekiel and Payeur, Alexandre and Lajoie, Guillaume},
  journal={arXiv preprint arXiv:2606.00243},
  year={2026},
  note={Accepted to ICML 2026}
}
```

## Activation Keywords

`RNN training`, `local learning`, `RFLO`, `truncated BPTT`, `neuromorphic`, `biological learning`, `low-rank`, `gradient descent`, `learning dynamics`, `dynamical systems theory`

---

**Research Source**: arXiv:2606.00243 - Williams, Payeur, Lajoie (ICML 2026)