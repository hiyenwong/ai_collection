---
name: variance-brain-foundation-models-forgot
description: "Brain foundation models (BFMs) lose third-order statistics (co-skewness) during pretraining - variance allocation problem where billion-parameter models predict cognition worse than linear FC. Solution: preserve co-skewness subspace. Activation: brain foundation model, variance allocation, co-skewness, third-order statistics, BFM pretraining, functional connectivity, cognitive prediction."
---

## Context

**Paper**: arXiv:2606.04010 (May 2026)
**Authors**: Giovanni Marraffini, Gabriel Mahuas, Trinidad Borrell, Victoria Shevchenko, Demian Wassermann
**Key Finding**: BFMs predict cognition worse than ~80K parameter linear FC due to variance allocation problem.

Brain foundation models (BrainLM, etc.) pretrained on fMRI fail to predict cognitive performance despite having 650M parameters. Linear functional connectivity (FC) with ~80K parameters outperforms them.

## Core Methodology

### 1. Variance Allocation Problem

**Diagnosis**: BFM pretraining captures dominant variance components but loses higher-order structure:
- **Preserved**: Second-order covariance (partially)
- **Destroyed**: Third-order co-skewness tensor (largely)
- **Result**: Models capture fMRI variance but not cognitive predictors

**Per-Cumulant Analysis**:
```python
# Decompose reconstructed signal
signal_reconstructed = bfm.decode(latent)
signal_original = fmri_data

# Cumulant comparison
covariance_2nd = compute_covariance(signal_original)  # ~50% preserved
co_skewness_3rd = compute_co_skewness(signal_original)  # ~10% preserved (mostly destroyed)
```

### 2. Co-Skewness Preservation Pipeline

**Solution**: Project fMRI into subspace that preserves co-skewness:

```python
# Step 1: Compute co-skewness tensor
def compute_co_skewness(X):
    # Third-order cumulant: E[X_i X_j X_k]
    N, T = X.shape
    co_skew = np.zeros((N, N, N))
    for i in range(N):
        for j in range(N):
            for k in range(N):
                co_skew[i,j,k] = np.mean(X[i] * X[j] * X[k])
    return co_skew

# Step 2: Find subspace preserving co-skewness
def find_skewness_subspace(co_skew, target_dim=100):
    # Eigendecomposition of flattened co-skewness
    flat_skew = co_skew.reshape(N**2, N)
    eigenvals, eigenvecs = np.linalg.eigh(flat_skew @ flat_skew.T)
    # Select subspace with largest co-skewness variance
    subspace = eigenvecs[:, -target_dim:]
    return subspace

# Step 3: Project and compute FC
X_projected = subspace @ X_original
FC_preserved = compute_covariance(X_projected)
```

### 3. Finetuning Recovery

**Recover Raw-FC Ceiling on BrainLM**:
```python
# Finetune with loss targeting co-skewness subspace
def skewness_preserving_loss(model, X):
    latent = model.encode(X)
    reconstructed = model.decode(latent)
    
    # Preserve co-skewness
    skew_orig = compute_co_skewness(X)
    skew_recon = compute_co_skewness(reconstructed)
    
    loss = ||skew_orig - skew_recon||^2
    return loss
```

## Implementation Steps

### Step 1: Evaluate BFM vs FC Baseline
```python
# Load BFM (BrainLM 650M)
bfm = load_brainlm('650M')
fc_baseline = compute_fc(fmri_data)  # ~80K params

# Cognitive prediction task
cognition_scores = load_cognition_data()

# Compare
bfm_pred = bfm.predict_cognition(fmri_data)
fc_pred = linear_regression(fc_baseline, cognition_scores)

# Result: fc_pred > bfm_pred (linear FC wins!)
```

### Step 2: Per-Cumulant Analysis
```python
# Reconstruct signal
latent = bfm.encode(fmri_data)
reconstructed = bfm.decode(latent)

# Compute cumulants
cov_orig = np.cov(fmri_data)
cov_recon = np.cov(reconstructed)
cov_preservation = np.corrcoef(cov_orig.flatten(), cov_recon.flatten())[0,1]

skew_orig = compute_co_skewness(fmri_data)
skew_recon = compute_co_skewness(reconstructed)
skew_preservation = np.corrcoef(skew_orig.flatten(), skew_recon.flatten())[0,1]

print(f"2nd-order preservation: {cov_preservation:.2f}")  # ~0.5
print(f"3rd-order preservation: {skew_preservation:.2f}")  # ~0.1 (destroyed!)
```

### Step 3: Implement Co-Skewness Pipeline
```python
# Full pipeline (no pretraining, no GPU needed)
def skewness_preserving_fc_pipeline(fmri_data, cognition_scores):
    # 1. Compute co-skewness
    skew = compute_co_skewness(fmri_data)
    
    # 2. Find preservation subspace
    subspace = find_skewness_subspace(skew, target_dim=50)
    
    # 3. Project data
    projected = subspace @ fmri_data
    
    # 4. Compute FC in subspace
    fc_preserved = np.cov(projected)
    
    # 5. Predict cognition
    pred = linear_regression(fc_preserved, cognition_scores)
    return pred

# Outperforms BFM and raw FC!
```

### Step 4: Finetune BFM
```python
# Targeted finetuning (preserve co-skewness)
optimizer = torch.optim.Adam(bfm.parameters())

for epoch in range(100):
    latent = bfm.encode(fmri_batch)
    reconstructed = bfm.decode(latent)
    
    # Skewness-preserving loss
    loss = skewness_preserving_loss(bfm, fmri_batch)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# After finetuning: bfm matches raw-FC ceiling!
```

## Pitfalls

- **Co-Skewness Computation Cost**: O(N^3 T) for N regions, T timepoints. Use approximations for large N.
- **Subspace Dimension Selection**: target_dim must balance preservation vs overfitting. Test 20-200 range.
- **Numerical Instability**: Third-order cumulants can overflow. Use normalization and log-space.
- **Finetuning Overfitting**: Skewness-preserving loss may overfit to training data. Use cross-validation.

## Verification

1. **Preservation Metrics**: 2nd-order ~0.5, 3rd-order ~0.1 (before); 3rd-order > 0.3 after fix
2. **Prediction Accuracy**: Co-skewness pipeline > raw FC > BFM
3. **Scale Paradox**: BrainLM 650M < BrainLM 111M (larger = worse due to variance allocation)
4. **Finetuning Recovery**: After skewness loss, BFM matches raw-FC ceiling

## Applications

- **Fix BFMs**: Add co-skewness preservation to pretraining objectives
- **Cognitive prediction**: Use co-skewness pipeline as simple, effective baseline
- **Model diagnosis**: Per-cumulant analysis reveals what models lose
- **Pretraining theory**: Higher-order statistics matter for cognition, not just variance

## Key Results

- **Gap widens with scale**: 650M predicts worse than 111M (variance allocation worsens)
- **Linear pipeline wins**: No pretraining, no GPU, outperforms billion-parameter models
- **Root cause identified**: Pretraining objective, not architecture or size
- **Solution validated**: Finetuning with skewness loss recovers ceiling performance

## Activation Keywords

`brain foundation model`, `variance allocation`, `co-skewness`, `third-order statistics`, `BFM pretraining`, `functional connectivity`, `cognitive prediction`, `BrainLM`, `cumulant analysis`, `variance preservation`, `neural variance`, `fMRI foundation model`

## Related Skills

- `brain-foundation-model-batch-effects`: BFM batch effects analysis
- `brain-dit-fmri-foundation-model`: Brain-DiT foundation model
- `neural-encoding-evaluation-ground-truth`: Ground-truth encoding evaluation
