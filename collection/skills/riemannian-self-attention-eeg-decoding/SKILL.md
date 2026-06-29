---
name: riemannian-self-attention-eeg-decoding
description: "Bures-Wasserstein metric-based Riemannian self-attention network for robust EEG decoding in BCI. Overcomes AIM quadratic dependency and ill-conditioning issues. Activation: riemannian self attention EEG, Bures-Wasserstein EEG decoding, GBWAtt, SPD learning BCI, Riemannian manifold EEG"
---

# Riemannian Self-Attention EEG Decoding (GBWAtt)

## Description

Riemannian self-attention network for robust EEG decoding in Brain-Computer Interface (BCI) applications. Uses Bures-Wasserstein Metric (BWM) instead of traditional Affine-Invariant Metric (AIM) to handle ill-conditioned SPD matrices with linear dependency, and extends to learnable generalized Bures-Wasserstein metric (GBWAtt) for nuanced geometric representation of SPD manifolds.

## Core Concepts

### Problem Space
- EEG decoding uses Symmetric Positive Definite (SPD) covariance matrices as features
- Traditional methods use Affine-Invariant Metric (AIM) with quadratic dependency on SPD matrices
- AIM cannot handle ill-conditioned SPD matrices — problematic for low-SNR EEG signals
- Basic network architectures don't explicitly capture local EEG signal relationships

### Bures-Wasserstein Metric (BWM)
- **Linear dependence** on SPD matrices (vs quadratic for AIM)
- Superior performance for ill-conditioned matrices
- Computationally more efficient for large-scale problems
- Naturally handles degenerate/near-singular covariance matrices

### Generalized Bures-Wasserstein Attention (GBWAtt)
- Power-deformed generalized BWM reveals nonlinear relationship between SPD matrices
- Matrix power deformation provides more nuanced SPD manifold geometry
- Learnable version adapts to task-specific manifold structure
- Self-attention mechanism captures local channel relationships in EEG

## Key Innovation

### BWM vs AIM Comparison
| Property | AIM | BWM |
|----------|-----|-----|
| Dependency | Quadratic O(n²) | Linear O(n) |
| Ill-conditioned | Fails | Handles well |
| Computation | Heavy | Efficient |
| Geometry | Full manifold | Wasserstein geometry |

### GBWAtt Architecture
1. **Covariance estimation**: Compute SPD covariance matrices from EEG epochs
2. **Power deformation**: Apply learnable matrix power deformation
3. **BWM self-attention**: Compute attention weights using Bures-Wasserstein distance
4. **Feature aggregation**: Aggregate features via Riemannian weighted mean
5. **Classification**: Project to Euclidean space for downstream classification

## Usage Patterns

### Pattern 1: Robust EEG Decoding with Low SNR
When EEG signals have low signal-to-noise ratio and traditional Riemannian methods fail:
```
Use GBWAtt for Riemannian self-attention → handles ill-conditioned SPD matrices
```

### Pattern 2: Efficient Large-Scale BCI
For real-time BCI with many channels where AIM is too slow:
```
Replace AIM-based Riemannian network with BWM-based → linear computational complexity
```

### Pattern 3: Learnable Manifold Geometry
When the optimal SPD manifold metric is task-specific:
```
Use GBWAtt learnable version → power deformation adapts to task geometry
```

## Instructions for Agents

### Step 1: Identify EEG Decoding Problem
- Check if SPD covariance matrices are used as features
- Identify SNR issues or ill-conditioned matrices
- Determine computational constraints (real-time vs offline)

### Step 2: Select Metric
- **AIM**: Only for well-conditioned, small-scale problems
- **BWM**: For ill-conditioned matrices or large-scale problems
- **GBWAtt**: When learnable manifold geometry is needed

### Step 3: Implement Architecture
```python
import torch
from pyriemann.tangentspace import TangentSpace
from pyriemann.classification import MDM

# BWM-based attention
def bures_wasserstein_distance(S1, S2):
    """Compute Bures-Wasserstein distance between SPD matrices."""
    sqrt_S1 = torch.matrix_power(S1, 0.5)
    inner = torch.linalg.matrix_power(sqrt_S1 @ S2 @ sqrt_S1, 0.5)
    return torch.trace(S1 + S2 - 2 * inner)

# GBWAtt: learnable power deformation
def gbw_attention(cov_matrices, power_param):
    """Generalized Bures-Wasserstein attention with learnable power."""
    deformed = torch.matrix_power(cov_matrices, power_param)
    return attention_weights
```

### Step 4: Validation
- Test on standard EEG benchmarks (BCI Competition IV, etc.)
- Compare against AIM-based baselines
- Check robustness to noise and ill-conditioning

## Error Handling

### Ill-Conditioned SPD Matrices
- **Symptom**: AIM-based methods diverge or produce NaN
- **Fix**: Switch to BWM — handles near-singular matrices naturally

### Computational Bottleneck
- **Symptom**: O(n²) AIM computation too slow for real-time
- **Fix**: BWM has linear dependency — use for large-scale BCI

### Power Deformation Instability
- **Symptom**: Learnable power parameter causes training instability
- **Fix**: Initialize power parameter near 1.0, use gradient clipping

## Related Skills
- `eeg-foundation-model-adapters` - EEG foundation model adaptation
- `riemannian-fmri-correlation-manifolds` - Riemannian methods for fMRI
- `bci-adversarial-robustness` - BCI robustness patterns

## Resources
- Paper: arXiv:2606.25456 (KDD 2026)
- Code: https://github.com/jissc/GBWAtt
- pyriemann library for Riemannian geometry operations
