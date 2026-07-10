# Classical Collapse in Medical QSVM (arXiv:2604.24597)

## The Classical Collapse Phenomenon

When using frozen embeddings from medical foundation models (MedSigLIP-448, RAD-DINO, ViT-patch32) for binary medical classification, **classical linear SVMs consistently collapse to majority-class prediction** across 90-100% of random seeds.

### Evidence (MIMIC-CXR chest radiographs)

- **Tier 1** (untuned, C=1 both sides): Classical linear SVM collapses in 90-100% of seeds at every qubit count. QSVM maintains non-trivial recall in all 18 configurations.
- **At q=11** (MedSigLIP-448 plateau center): QSVM F1=0.343 vs Classical F1=0.050 (gain +0.293, p<0.001)
- **Tier 2** (untuned QSVM vs. C-tuned RBF SVM): QSVM wins all 7 configurations (mean +0.068, max +0.112)
- Classical collapse is **C-invariant** — hyperparameter tuning does NOT fix it

### Eigenspectrum Analysis

- Quantum kernel effective rank = 69.80 at q=11
- Classical linear kernel rank is far lower
- A full qubit sweep reveals **architecture-dependent concentration onset** across foundation models

### Implications for QML Research

1. **Don't use linear SVM as baseline** for medical foundation model embeddings — it collapses
2. **RBF SVM with tuning** is the appropriate classical baseline
3. **Quantum advantage is most visible** when classical methods suffer from kernel collapse
4. **Eigenspectrum analysis** is a valuable diagnostic tool

### Code for Eigenspectrum Comparison

```python
import numpy as np
from sklearn.metrics.pairwise import linear_kernel, rbf_kernel

def effective_rank(K):
    s = np.linalg.svd(K, compute_uv=False)
    s = s / s.sum()
    s = s[s > 1e-10]
    entropy = -np.sum(s * np.log(s))
    return np.exp(entropy)
```
