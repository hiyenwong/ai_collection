---
name: effective-rank-encoding-predictor
description: "Effective rank methodology for predicting quantum data encoding performance. Uses feature map effective rank as a threshold criterion to accelerate the search for high-performing QML encodings. Activation: effective rank encoding, feature map rank QML, encoding performance prediction, quantum encoding predictor, QML encoding ranking."
---

# Effective Rank Encoding Predictor Methodology

Use effective rank of quantum feature maps as a performance predictor for quantum machine learning (QML) data encodings.

## Core Concept

Traditional metrics like entanglement capability and Fourier decomposition provide minimal insight into encoding performance. The effective rank of quantum feature maps exhibits meaningful correlation with QML model performance and can serve as a threshold criterion to accelerate encoding discovery.

## Mathematical Foundation

### Effective Rank Definition

For a quantum feature map \(\Phi(x)\), the effective rank is computed from the eigenvalues \(\{\lambda_i\}\) of the feature covariance matrix:

```
effective_rank = exp(H) / max_eigenvalue
where H = -sum(p_i * log(p_i)) is the Shannon entropy
and p_i = λ_i / sum(λ_j) are normalized eigenvalues
```

### Why Effective Rank Works

1. **Dimensionality Capture**: Measures effective dimensionality of encoded feature space
2. **Information Preservation**: High effective rank = more information retained
3. **Expressivity Indicator**: Correlates with model capacity to discriminate classes

## Implementation

### Step 1: Compute Feature Map
```python
import numpy as np
from scipy.linalg import eigvalsh

def compute_effective_rank(feature_matrix):
    """Compute effective rank of quantum feature matrix.
    
    Args:
        feature_matrix: (n_samples, n_features) from quantum encoding circuit
    
    Returns:
        effective_rank: float between 1 and min(n_samples, n_features)
    """
    # Compute covariance matrix
    cov = np.cov(feature_matrix.T)
    
    # Get eigenvalues
    eigenvalues = eigvalsh(cov)
    eigenvalues = np.maximum(eigenvalues, 0)  # Ensure non-negative
    
    # Normalize to probability distribution
    total = np.sum(eigenvalues)
    if total == 0:
        return 1.0
    probs = eigenvalues / total
    
    # Compute Shannon entropy
    probs = probs[probs > 1e-10]  # Filter near-zero
    entropy = -np.sum(probs * np.log(probs))
    
    # Effective rank
    return np.exp(entropy) / (np.max(eigenvalues) / total)
```

### Step 2: Encoding Performance Prediction
```python
def predict_encoding_performance(encoding_circuit, X_train, y_train, threshold=0.5):
    """Predict if an encoding will perform well based on effective rank.
    
    Args:
        encoding_circuit: Quantum circuit that encodes data
        X_train, y_train: Training data
        threshold: Effective rank threshold for filtering
    
    Returns:
        predicted_performance: bool, whether encoding is promising
        effective_rank: float, computed effective rank
    """
    # Generate feature matrix from encoding circuit
    feature_matrix = encoding_circuit.transform(X_train)
    
    # Compute effective rank
    eff_rank = compute_effective_rank(feature_matrix)
    
    # Normalize by maximum possible rank
    max_rank = min(feature_matrix.shape)
    normalized_rank = eff_rank / max_rank
    
    return normalized_rank > threshold, normalized_rank
```

### Step 3: Accelerated Search
```python
def accelerated_encoding_search(encoding_candidates, X_train, y_train, threshold=0.5):
    """Use effective rank to accelerate encoding search.
    
    Args:
        encoding_candidates: List of encoding circuits to evaluate
        X_train, y_train: Training data
        threshold: Effective rank threshold
    
    Returns:
        promising_encodings: List of (encoding, effective_rank) tuples
    """
    promising = []
    for enc in encoding_candidates:
        is_promising, rank = predict_encoding_performance(
            enc, X_train, y_train, threshold
        )
        if is_promising:
            promising.append((enc, rank))
    
    # Sort by effective rank (higher is better)
    promising.sort(key=lambda x: x[1], reverse=True)
    return promising
```

## Workflow

1. **Generate encoding candidates**: Create pool of encoding circuits
2. **Compute effective rank**: For each candidate, compute feature map effective rank
3. **Filter by threshold**: Discard encodings below effective rank threshold
4. **Evaluate survivors**: Train QML models only on promising encodings
5. **Select best**: Choose encoding with best actual performance

## Parameters

- **Effective Rank Threshold**: 0.3-0.7 (dataset dependent)
- **Normalization**: Always normalize by max possible rank
- **Sample Size**: Use at least 100 samples for stable rank estimation

## Advantages

- **Computationally Cheap**: Effective rank computation is O(n^2) vs full QML training
- **Early Filtering**: Eliminates poor encodings before expensive training
- **Correlated with Performance**: Validated on medical imaging datasets
- **Model-Agnostic**: Works with any QML model architecture

## Use Cases

- QML encoding circuit selection
- MCTS-guided encoding discovery (pruning search space)
- Feature map comparison for different encoding strategies
- Hybrid quantum-classical neural network design
- Medical image classification with QML

## References

- Tokuhiro et al. (2026). "Discovering Data Encoding Strategies for Quantum-Classical Neural Networks Using Monte Carlo Tree Search" (arXiv:2605.18540)

## Related Skills

- mcts-quantum-encoding-discovery
- quantum-ml-data-loading
- quantum-neural-network-designer
