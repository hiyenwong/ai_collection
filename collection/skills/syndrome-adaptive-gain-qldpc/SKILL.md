---
name: syndrome-adaptive-gain-qldpc
description: >
  Syndrome Adaptive Gain Min-Sum (SAGMS) decoding methodology for quantum LDPC codes.
  Dynamically adjusts the MS scaling factor based on syndrome patterns during iterative
  decoding, eliminating the need for per-code/per-noise-level gain optimization.
  Use when: designing quantum LDPC decoders, optimizing belief propagation alternatives,
  implementing low-complexity QEC decoding, comparing MS vs BP vs neural decoders,
  or working with generalized bicycle QLDPC codes.
  Keywords: quantum LDPC decoding, min-sum scaling, syndrome adaptive gain, SAGMS,
  QEC decoder optimization, belief propagation alternative, iterative decoding,
  量子LDPC解码, 自适应增益, 最小和译码.
---

# Syndrome Adaptive Gain Min-Sum (SAGMS) for QLDPC Decoding

## Core Methodology

Min-Sum (MS) decoding approximates belief propagation (BP) by retaining only the
minimum incoming message magnitude at each check node (CN). This causes systematic
message magnitude overestimation. The standard fix is Scaled MS (SMS) with a fixed
scaling factor α, but α depends on code structure and noise level — requiring
expensive offline optimization.

**SAGMS** replaces the fixed α with a dynamic gain αₜ computed at each iteration t
from the current syndrome pattern:

### Algorithm

```
Initialize: messages m_{e}^{(0)} = channel LLRs
For iteration t = 1, 2, ..., T:
  1. Compute syndrome s^{(t)} from current estimates
  2. Calculate adaptive gain: αₜ = f(s^{(t)}, fraction of unsatisfied checks)
  3. CN update: m_{cn→v} = αₜ × sign_product × min(|m_{v→cn}|)
  4. VN update: m_{v→cn} = channel_LLR + Σ m_{cn'→v} (excluding cn)
  5. Check convergence: if s^{(t)} == 0, return estimates
```

### Key Properties

1. **No offline optimization**: αₜ adapts online based on decoding state
2. **Degree-robust**: SMS scaling factor decreases with CN degree — any fixed α
   optimized for one degree degrades as CN degree varies. SAGMS avoids this.
3. **MS-level complexity**: O(E) per iteration, same as MS/BP
4. **Performance**: Matches or exceeds offline-optimized SMS; approaches BP FER

### Adaptive Gain Function

The gain adapts to the fraction of unsatisfied syndrome bits:

```python
def adaptive_gain(syndrome, n_checks):
    """Compute adaptive scaling factor from syndrome pattern."""
    unsatisfied = sum(syndrome) / n_checks  # fraction of unsatisfied checks
    
    # Gain increases when more checks are unsatisfied
    # Empirical form: linear or piecewise function
    if unsatisfied > 0.5:
        return 0.8   # Higher gain for aggressive correction
    elif unsatisfied > 0.2:
        return 0.6   # Moderate gain
    else:
        return 0.4   # Lower gain for fine-tuning
```

### Performance Characteristics

| Decoder | Complexity | Offline Opt. Needed | FER Performance |
|---------|-----------|---------------------|-----------------|
| BP | O(E log d_v) | No | Best |
| MS | O(E) | No | Poor (overestimation) |
| SMS | O(E) | Yes (per code/SNR) | Good (if α tuned) |
| **SAGMS** | **O(E)** | **No** | **≈ BP, > SMS** |
| Neural | O(E) | Yes (training) | Varies |

## Implementation Patterns

### Basic SAGMS Decoder

```python
import numpy as np

def sagms_decode(H, llr, max_iter=100, eps=1e-10):
    """
    Syndrome Adaptive Gain Min-Sum decoder.
    
    Args:
        H: Parity check matrix (m x n) over GF(2)
        llr: Channel log-likelihood ratios (n,)
        max_iter: Maximum iterations
        eps: Numerical stability constant
    
    Returns:
        estimates: Decoded codeword
        converged: Whether decoding succeeded
        iterations: Number of iterations used
    """
    m, n = H.shape
    
    # Initialize messages (VN to CN)
    edges = np.argwhere(H == 1)
    
    # Message initialization: VN→CN = channel LLR
    m_v2c = np.full(len(edges), 0.0)
    for idx, (i, j) in enumerate(edges):
        m_v2c[idx] = llr[j]
    
    for t in range(max_iter):
        # Compute syndrome from current estimates
        estimates = (llr < 0).astype(int)
        syndrome = (H @ estimates) % 2
        
        if syndrome.sum() == 0:
            return estimates, True, t
        
        # Calculate adaptive gain
        unsat_fraction = syndrome.sum() / m
        alpha = adaptive_gain(unsat_fraction)
        
        # CN-to-VN messages
        m_c2v = np.zeros_like(m_v2c)
        for idx, (i, j) in enumerate(edges):
            other_msgs = [m_v2c[k] for k, (ci, _) in enumerate(edges) 
                         if ci == i and k != idx]
            if other_msgs:
                abs_min = min(abs(x) for x in other_msgs)
                sign_prod = np.prod([np.sign(x) for x in other_msgs])
                m_c2v[idx] = alpha * sign_prod * abs_min
        
        # VN-to-CN messages
        m_v2c_new = np.zeros_like(m_v2c)
        for idx, (i, j) in enumerate(edges):
            other_msgs = [m_c2v[k] for k, (_, cj) in enumerate(edges)
                         if cj == j and k != idx]
            m_v2c_new[idx] = llr[j] + sum(other_msgs)
        
        m_v2c = m_v2c_new
    
    estimates = (llr < 0).astype(int)
    return estimates, False, max_iter


def adaptive_gain(unsat_fraction):
    """Piecewise adaptive gain based on syndrome unsatisfied fraction."""
    if unsat_fraction > 0.5:
        return 0.8
    elif unsat_fraction > 0.2:
        return 0.6
    else:
        return 0.4
```

## When to Use

1. **QLDPC code decoding**: Primary use case for generalized bicycle and similar codes
2. **Replacing SMS**: When fixed scaling factor optimization is impractical
3. **Resource-constrained QEC**: Need BP-level performance with MS complexity
4. **Multi-code deployment**: Single decoder works across different code parameters
5. **FPGA implementation**: MS complexity enables real-time decoding

## Comparison with Neural Decoders

Recent work (arXiv:2605.12046) shows neural decoders face accuracy-latency tradeoffs:
- INT4 quantization required for μs latency on FPGA
- Performance driven by data scale, not architectural complexity
- SAGMS offers an alternative: no training data needed, deterministic performance

## Integration with Other Decoders

```python
# Hybrid approach: try SAGMS first, fall back to BP if needed
def hybrid_decode(H, llr):
    result, converged, iters = sagms_decode(H, llr, max_iter=50)
    if not converged:
        result, converged, _ = bp_decode(H, llr, max_iter=100)
    return result
```

## References

- Paper: "Syndrome Adaptive Gain Control for Min-Sum Decoding of Quantum LDPC Codes"
  arXiv: 2605.10433
  Authors: Hernan Cordova, Alexios Balatsoukas-Stimming, Yunus Can Gültekin, Gabriele Liga, Alex Alvarado
- Related: CSS syndrome decoding, belief propagation, scaled min-sum decoding
