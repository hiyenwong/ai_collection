---
name: eeg-foundation-sae-interpretability
description: "Mechanistic interpretability of EEG foundation models using Sparse Autoencoders (SAEs). Extract sparse feature dictionaries from EEG transformer embeddings, benchmark monosemanticity, perform concept steering, and map interventions to physiological frequency signatures."
---

# EEG Foundation Model Interpretability via Sparse Autoencoders

Mechanistic interpretability methodology for EEG foundation models using TopK Sparse Autoencoders (SAEs). Extracts sparse feature dictionaries from transformer embeddings, grounds them in clinical taxonomy, quantifies steering selectivity, and maps latent interventions back to physiological frequency signatures.

Based on: *Mechanistic Interpretability of EEG Foundation Models via Sparse Autoencoders* (arXiv: 2605.13930v2)
Authors: Lehn-Schiøler et al., 2026

## Activation

- EEG foundation model interpretability
- Sparse autoencoder EEG
- EEG transformer interpretability
- concept steering EEG
- mechanistic interpretability brain models
- EEG SAE
- 脑电基础模型可解释性
- 稀疏自编码器 EEG

## Core Methodology

### Step 1: SAE Training on EEG Transformer Embeddings

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class TopK_SAE(nn.Module):
    """TopK Sparse Autoencoder for EEG transformer embeddings."""
    
    def __init__(self, d_model: int, expansion_factor: int = 8, k: int = 32):
        super().__init__()
        self.d_model = d_model
        self.d_dict = d_model * expansion_factor  # Dictionary size
        self.k = k  # Number of active features
        
        # Encoder: project to dictionary, then top-k
        self.W_enc = nn.Parameter(torch.nn.init.kaiming_uniform_(
            torch.empty(d_model, self.d_dict)))
        self.b_enc = nn.Parameter(torch.zeros(self.d_dict))
        
        # Decoder: reconstruct from dictionary
        self.W_dec = nn.Parameter(torch.nn.init.kaiming_uniform_(
            torch.empty(self.d_dict, d_model)))
        self.b_dec = nn.Parameter(torch.zeros(d_model))
        
        # Normalize decoder weights
        with torch.no_grad():
            self.W_dec.div_(self.W_dec.norm(dim=1, keepdim=True))
    
    def forward(self, x: torch.Tensor) -> tuple:
        # Encode
        pre_acts = x @ self.W_enc + self.b_enc
        
        # Top-k activation
        topk_values, topk_indices = torch.topk(pre_acts, self.k, dim=-1)
        acts = torch.zeros_like(pre_acts)
        acts.scatter_(-1, topk_indices, F.relu(topk_values))
        
        # Decode
        reconstructed = acts @ self.W_dec + self.b_dec
        return reconstructed, acts, pre_acts
```

**Training objective:**
```python
def sae_loss(x, reconstructed, acts, W_dec, l1_coeff=0.0):
    """Reconstruction loss + L1 sparsity."""
    recon_loss = F.mse_loss(reconstructed, x)
    l1_loss = l1_coeff * acts.abs().sum(dim=-1).mean()
    return recon_loss + l1_loss
```

### Step 2: Hyperparameter Selection via Dictionary Health Audit

Use intrinsic metrics to select the optimal `k` and expansion factor:

```python
def dictionary_health_audit(sae, validation_data):
    """Audit SAE dictionary quality."""
    metrics = {}
    
    # Sparsity: fraction of near-zero activations
    activations = []
    with torch.no_grad():
        for x in validation_data:
            _, acts, _ = sae(x)
            activations.append(acts)
    acts = torch.cat(activations)
    
    metrics['firing_rate'] = (acts > 0).float().mean()
    
    # Dead features: features never activated
    max_acts = acts.max(dim=0).values
    metrics['dead_features'] = (max_acts < 1e-6).float().mean()
    
    # Reconstruction quality
    recons = []
    with torch.no_grad():
        for x in validation_data:
            recon, _, _ = sae(x)
            recons.append(recon)
    recons = torch.cat(recons)
    originals = torch.cat(validation_data)
    
    metrics['explained_variance'] = 1 - (
        (originals - recons).var() / originals.var())
    
    return metrics
```

### Step 3: Clinical Grounding via Concept Probes

Ground sparse features against clinical taxonomy (abnormality, age, sex, medication):

```python
def probe_concept_concepts(sae, labeled_data, concept_labels):
    """Train linear probes to map SAE features to clinical concepts."""
    _, all_acts, _ = sae(labeled_data)
    
    # For each concept, train logistic regression on activations
    concept_scores = {}
    for concept_name, labels in concept_labels.items():
        # Simple linear probe
        weights = torch.linalg.lstsq(all_acts, labels.float()).solution
        predictions = all_acts @ weights
        accuracy = ((predictions > 0.5) == labels).float().mean()
        concept_scores[concept_name] = {
            'accuracy': accuracy.item(),
            'weights': weights,
            'top_features': weights.abs().topk(10).indices,
        }
    
    return concept_scores

def monosemanticity_score(concept_scores):
    """Measure how monosemantic each feature is."""
    # A feature is monosemantic if it strongly predicts only one concept
    all_weights = []
    for name, score in concept_scores.items():
        all_weights.append(score['weights'].abs())
    
    weight_matrix = torch.stack(all_weights)
    # Feature-level: max concept / sum of all concepts
    max_concept = weight_matrix.max(dim=0).values
    total = weight_matrix.sum(dim=0)
    mono_scores = max_concept / (total + 1e-8)
    return mono_scores.mean()

def entanglement_score(concept_scores):
    """Measure how entangled concepts are in the feature space."""
    # High entanglement = features predict multiple concepts
    all_weights = []
    for name, score in concept_scores.items():
        all_weights.append(score['weights'].abs())
    
    weight_matrix = torch.stack(all_weights)
    # Cross-concept correlation
    correlations = torch.corrcoef(weight_matrix)
    # Off-diagonal mean
    n = correlations.size(0)
    off_diag = correlations.sum() - correlations.diag().sum()
    return off_diag / (n * (n - 1))
```

### Step 4: Concept Steering and Selectivity Quantification

Implement "target vs. off-target" probe area metric:

```python
def concept_steering(sae, input_data, concept_probe, 
                     steering_direction, magnitudes):
    """Apply concept steering at different magnitudes."""
    results = {}
    
    for mag in magnitudes:
        # Get SAE activations
        recon, acts, pre_acts = sae(input_data)
        
        # Steering: add direction to activations
        steered_acts = acts.clone()
        steered_acts += mag * steering_direction
        
        # Decode steered representation
        steered_recon = steered_acts @ sae.W_dec + sae.b_dec
        
        # Evaluate
        target_change = concept_probe['target'](steered_recon) - concept_probe['target'](recon)
        off_target_change = concept_probe['off_target'](steered_recon) - concept_probe['off_target'](recon)
        
        results[mag] = {
            'target_change': target_change,
            'off_target_change': off_target_change,
            'selectivity': target_change / (abs(off_target_change) + 1e-8),
        }
    
    return results

def classify_steering_regime(steering_results):
    """Classify into three operational regimes."""
    max_selectivity = max(r['selectivity'] for r in steering_results.values())
    max_target = max(abs(r['target_change']) for r in steering_results.values())
    
    if max_selectivity > 5.0 and max_target > 0.1:
        return "selectively steerable"
    elif max_target > 0.1:
        return "encoded but entangled"
    else:
        return "non-encoded"
```

### Step 5: Spectral Decoder - Mapping Interventions to Frequency

```python
def spectral_decoder(intervention_data, raw_eeg, sampling_rate=256):
    """Map SAE interventions back to amplitude spectrum."""
    from scipy.signal import welch
    
    # Compute power spectral density
    freqs, psd_intervention = welch(intervention_data, fs=sampling_rate, nperseg=1024)
    freqs, psd_original = welch(raw_eeg, fs=sampling_rate, nperseg=1024)
    
    # Frequency band differences
    bands = {
        'delta': (0.5, 4),
        'theta': (4, 8),
        'alpha': (8, 13),
        'beta': (13, 30),
        'gamma': (30, 45),
    }
    
    spectral_changes = {}
    for band, (lo, hi) in bands.items():
        mask = (freqs >= lo) & (freqs <= hi)
        orig_power = psd_original[mask].mean()
        intv_power = psd_intervention[mask].mean()
        spectral_changes[band] = {
            'original': orig_power,
            'intervention': intv_power,
            'change': (intv_power - orig_power) / (orig_power + 1e-8),
        }
    
    return spectral_changes
```

## Key Findings from the Paper

### Three Steering Regimes

1. **Selectively steerable**: Features can be modified without affecting unrelated concepts
2. **Encoded but entangled**: Concept is present but inseparable from others (e.g., age-pathology confounding)
3. **Non-encoded**: Concept not represented in the feature space

### Critical Representational Failures

- **"Wrecking-ball" interventions**: Steering that collapses global model performance
- **Clinical entanglements**: Age-pathology confounding where suppressing one concept corrupts the other
- **Entanglement as a diagnostic**: If two clinical concepts are entangled, the model may learn spurious correlations

### Architectural Transferability

A single hyperparameter procedure transfers robustly across three distinct architectures:
- **SleepFM**: Sleep-focused EEG transformer
- **REVE**: Representation for EEG with Versatile Embeddings
- **LaBraM**: Large Brain Model

## Application Patterns

### Pattern 1: Detecting Spurious Correlations

```python
# Check if model uses age as proxy for pathology
age_probe = train_concept_probe(sae_acts, age_labels)
pathology_probe = train_concept_probe(sae_acts, pathology_labels)

# If same features predict both, model may conflate them
shared_features = set(age_top_features) & set(pathology_top_features)
if len(shared_features) > threshold:
    print(f"WARNING: {len(shared_features)} features encode both age and pathology")
    print("Model may have learned spurious age-pathology correlation")
```

### Pattern 2: Safe Intervention Design

```python
# Before applying intervention, check regime
regime = classify_steering_regime(steering_results)
if regime == "selectively steerable":
    print("Safe to apply intervention")
elif regime == "encoded but entangled":
    print("CAUTION: Intervention will affect other concepts")
else:
    print("Concept not represented; intervention will have no effect")
```

### Pattern 3: Physiological Interpretation

```python
# Map SAE intervention to frequency changes
spectral_changes = spectral_decoder(steered_eeg, original_eeg)

# Example output interpretation
if spectral_changes['delta']['change'] < -0.3:
    print("Intervention suppresses pathological slow waves")
if spectral_changes['alpha']['change'] > 0.2:
    print("Intervention restores alpha band activity")
```

## Pitfalls

1. **Dead features**: If too many dictionary features are never activated, the expansion factor is too large or `k` is too small
2. **Wrecking-ball effect**: Large steering magnitudes can collapse model performance entirely — always sweep magnitudes
3. **Architecture-specific features**: Feature dictionaries are not directly transferable between architectures; retrain SAE per model
4. **Probe reliability**: Linear probes may fail for non-linearly separable concepts — verify with cross-validation
5. **Clinical confounding**: Age, sex, and medication can be deeply entangled with pathology in training data

## Dependencies

```bash
pip install torch scipy scikit-learn numpy
```

## Related Skills

- **eeg-foundation-lrp-interpretability**: LRP-based interpretability for EEG models
- **eeg-foundation-model-adapters**: Domain adaptation for EEG foundation models
- **eeg-foundation-sae-interpretability**: This skill (SAE-based approach)
- **mechanistic-interpretability**: General mechanistic interpretability methods

## References

- Lehn-Schiøler, W., et al. "Mechanistic Interpretability of EEG Foundation Models via Sparse Autoencoders." arXiv:2605.13930v2, 2026.
- Bricken et al. "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning." 2023.
- Templeton et al. "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet." 2024.
