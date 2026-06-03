---
name: tensor-network-medical-imaging
description: Quantum-inspired tensor network feature engineering for medical image classification. Use PARAFAC/CP tensor decompositions to extract discriminative features from medical imaging data (MRI, CT, X-ray) for multi-class neurological disorder prediction and clinical diagnosis. Applicable to any high-dimensional medical imaging classification task where tensor decompositions can capture latent structure.
---

# Tensor Network Medical Imaging

## Description
Apply quantum-inspired tensor network decompositions (PARAFAC/CP) to medical imaging data for multi-class classification. This approach converts high-dimensional images into compact tensor representations, decomposes them into latent factors, and feeds these features into ensemble classifiers for robust neurological disorder prediction.

## Activation Keywords
- tensor network medical
- PARAFAC medical imaging
- quantum-inspired classification
- neurological disorder prediction
- tensor decomposition MRI
- CP decomposition medical
- medical image tensor features
- tensor feature engineering
- PARAFAC CP decomposition
- 张量网络医学成像
- 医疗图像分类

## Tools Used
- python: Execute tensor decomposition and classification scripts
- sklearn: Classification models and cross-validation
- tensorly: Tensor operations and PARAFAC decomposition

## Installation

```bash
pip install tensorly scikit-learn numpy pandas
```

## Usage Patterns

### Pattern 1: MRI-based Neurological Disorder Classification
```python
from tensorly.decomposition import parafac
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Load medical imaging data (N_samples, height, width, channels)
images = load_medical_images()  # Shape: (N, H, W, C)

# Convert to tensor format for decomposition
tensor_data = images.reshape(-1, H, W, C)

# Apply PARAFAC decomposition
weights, factors = parafac(tensor_data, rank=64, n_iter_max=100)

# Use factors as features for classification
features = factors[0]  # Component weights
labels = get_diagnosis_labels()

# Train classifier with nested cross-validation
from sklearn.model_selection import cross_val_score
clf = RandomForestClassifier(n_estimators=100)
scores = cross_val_score(clf, features, labels, cv=5)
```

### Pattern 2: Multi-Modal Medical Image Fusion
```python
# Combine multiple imaging modalities using tensor fusion
mri_tensor = load_mri_data()
ct_tensor = load_ct_data()

# Stack modalities as additional tensor mode
fused_tensor = np.stack([mri_tensor, ct_tensor], axis=-1)

# Decompose fused tensor
weights, factors = parafac(fused_tensor, rank=128)

# Use decomposed features for enhanced classification
```

## Instructions for Agents

### Step 1: Data Preparation
- Load medical imaging data into numpy arrays
- Ensure consistent preprocessing (normalization, resizing)
- Handle missing modalities gracefully
- Balance dataset across diagnostic categories

### Step 2: Tensor Decomposition
- Choose appropriate PARAFAC rank (start with 32-128)
- Apply decomposition with sufficient iterations (100+)
- Validate decomposition quality with explained variance
- Extract component weights and factor matrices

### Step 3: Feature Engineering
- Use component weights as primary features
- Consider factor matrices for spatial/structural features
- Combine with traditional features if beneficial
- Handle high-rank vs low-rank configurations

### Step 4: Classification
- Use ensemble methods (Random Forest, Gradient Boosting)
- Implement nested stratified cross-validation
- Report both accuracy and per-class metrics
- Compare with baseline approaches

## Error Handling

### Tensor Decomposition Fails
```
If decomposition doesn't converge:
  1. Increase n_iter_max (try 200-500)
  2. Reduce rank
  3. Check for NaN/Inf in input data
  4. Try different initialization
```

### Memory Issues
```
For large datasets:
  1. Use mini-batch processing
  2. Reduce spatial resolution temporarily
  3. Apply PCA before tensor decomposition
  4. Use sparse tensor representations
```

## Best Practices

1. **Rank Selection**: Start with lower ranks (32-64) for robustness, increase if needed
2. **Cross-Validation**: Always use nested stratified CV for reliable estimates
3. **Baseline Comparison**: Compare against PCA, autoencoders, and CNNs
4. **Interpretability**: Factor matrices can reveal spatial patterns relevant to diagnosis
5. **Multi-Modal**: Tensor decomposition naturally handles multiple imaging modalities

## Examples

### Example: 8-Class Neurological Disorder Prediction
```python
# Based on arXiv:2605.17771
# Dataset: 55,160 MRI images across 8 diagnostic categories

import tensorly as tl
from tensorly.decomposition import parafac
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
import numpy as np

# Load data
images = np.load('mri_dataset.npy')  # (55160, 128, 128, 3)
labels = np.load('diagnosis_labels.npy')  # 8 classes

# PARAFAC decomposition
tensor_images = images.reshape(-1, 128, 128, 3)
weights, factors = parafac(tensor_images, rank=64, n_iter_max=100)

# Classification with 5-fold CV
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)

for train_idx, test_idx in skf.split(weights, labels):
    clf.fit(weights[train_idx], labels[train_idx])
    accuracy = clf.score(weights[test_idx], labels[test_idx])
    print(f"Fold accuracy: {accuracy:.4f}")
```

## Related Skills
- quantum-medical-diagnosis: Quantum computing for medical diagnosis
- medical-ai-diagnosis: AI-based medical diagnosis patterns
- brain-network-controllability: Brain network analysis

## Resources
- arXiv:2605.17771 - Original paper on PARAFAC for neurological disorder prediction
- TensorLy documentation: https://tensorly.org/
- scikit-learn ensemble methods: https://scikit-learn.org/
