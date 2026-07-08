# Encoding Performance via Effective Rank

## Problem

Data encoding is critical in QML but predicting which encoding will work well is difficult. Traditional metrics fail.

## Solution: Effective Rank

For a quantum feature map Φ(x), compute the effective rank of the feature covariance matrix:

```
effective_rank = exp(H) / max_eigenvalue
H = -sum(p_i * log(p_i))  (Shannon entropy)
p_i = λ_i / sum(λ_j)      (normalized eigenvalues)
```

## Implementation

```python
import numpy as np
from scipy.linalg import eigvalsh

def compute_effective_rank(feature_matrix):
    cov = np.cov(feature_matrix.T)
    eigenvalues = eigvalsh(cov)
    eigenvalues = np.maximum(eigenvalues, 0)
    total = np.sum(eigenvalues)
    if total == 0:
        return 1.0
    probs = eigenvalues / total
    probs = probs[probs > 1e-10]
    entropy = -np.sum(probs * np.log(probs))
    return np.exp(entropy) / (np.max(eigenvalues) / total)

def accelerated_encoding_search(encoding_candidates, X_train, threshold=0.5):
    """Filter and rank encodings by effective rank before full training."""
    promising = []
    for enc in encoding_candidates:
        features = enc.transform(X_train)
        eff_rank = compute_effective_rank(features)
        max_rank = min(features.shape)
        normalized = eff_rank / max_rank
        if normalized > threshold:
            promising.append((enc, normalized))
    promising.sort(key=lambda x: x[1], reverse=True)
    return promising
```

## Key Finding (arXiv:2605.18540)

- Entanglement capability: **minimal correlation** with encoding performance
- Fourier decomposition: **minimal correlation** with encoding performance  
- Effective rank of feature maps: **meaningful correlation** — can serve as threshold criterion

Validated on two medical imaging datasets. Accelerates MCTS encoding search by 3-5x through early pruning.

## Parameters

- Effective rank threshold: 0.3–0.7 (dataset dependent)
- Minimum samples: 100+ for stable rank estimation
- Works as pruning criterion in MCTS or any search over encoding space