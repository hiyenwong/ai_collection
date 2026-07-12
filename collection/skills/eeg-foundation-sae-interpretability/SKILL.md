---
name: eeg-foundation-sae-interpretability
description: "Mechanistic interpretability of EEG foundation models using Sparse Autoencoders (SAEs). Extracts interpretable feature dictionaries from EEG transformer embeddings via TopK SAEs, benchmarks monosemanticity across architectures (SleepFM, REVE, LaBraM), and introduces concept steering with target vs. off-target probe metrics. Use when: interpreting EEG models, sparse autoencoders for neural data, EEG foundation model analysis, mechanistic interpretability of time-series models, concept steering in brain models, EEG feature disentanglement. Activation: EEG SAE, EEG interpretability, sparse autoencoder EEG, EEG foundation model, concept steering EEG, EEG monosemanticity, EEG feature dictionary."
---

# Mechanistic Interpretability of EEG Foundation Models via Sparse Autoencoders

Apply TopK Sparse Autoencoders to extract interpretable features from EEG foundation model embeddings. (arXiv: 2605.13930)

## Core Methodology

### TopK SAE on EEG Transformers

Train TopK Sparse Autoencoders on embeddings from EEG foundation models to extract feature dictionaries:

```python
# TopK SAE forward pass
encoded = topk(Encoder(x), k)  # Keep only top-k active features
decoded = Decoder(encoded)
loss = MSE(x, decoded) + λ * sparsity_penalty
```

### Cross-Architecture Benchmarking

Apply SAEs across three architecturally distinct EEG transformers:

| Architecture | Focus | SAE Transferability |
|---|---|---|
| SleepFM | Sleep staging | Robust feature extraction |
| REVE | General EEG | Cross-dataset features |
| LaBraM | Brain activity | Clinical feature grounding |

### Clinical Taxonomy Grounding

Ground extracted features against clinical categories:
- **Abnormality** — pathological EEG patterns
- **Age** — developmental/aging signatures
- **Sex** — sex-specific neural patterns
- **Medication** — drug-induced EEG changes

### Dictionary Health Audit

Intrinsic procedure to evaluate SAE quality:
- **Monosemanticity** — single feature → single concept
- **Entanglement** — feature-concept mapping complexity
- **Coverage** — fraction of variance explained
- **Sparsity** — average active features per input

### Concept Steering & Probe Metrics

**Target vs. Off-Target Probe Area:**
- Quantify steering selectivity
- Three operational regimes identified:
  1. **Selective steering** — activates target concept without off-target effects
  2. **Mixed activation** — partial selectivity
  3. **Entangled steering** — activates multiple concepts simultaneously

Single hyperparameter procedure transfers robustly across all architectures.

## Implementation Workflow

### Step 1: Extract Embeddings

```python
# Load EEG foundation model
model = load_eeg_model("SleepFM")  # or REVE, LaBraM
embeddings = model.encode(eeg_data)  # [batch, seq, dim]
```

### Step 2: Train TopK SAE

```python
sae = TopKSAE(
    input_dim=embeddings.shape[-1],
    dict_size=16384,  # Feature dictionary size
    k=32,             # Top-k sparsity
)
sae.train(embeddings, lr=1e-4, batch_size=256)
```

### Step 3: Audit Dictionary Health

```python
audit = DictionaryAudit(sae, eeg_data)
monosemanticity = audit.compute_monosemanticity()
entanglement = audit.compute_entanglement()
coverage = audit.compute_coverage()
```

### Step 4: Concept Steering

```python
# Identify feature directions for clinical concepts
directions = identify_directions(sae, labeled_data, concepts=["abnormality", "age"])

# Steer model activation
steered = steer(embeddings, directions["abnormality"], strength=2.0)
probe_score = probe(steered, target="abnormality", off_target=["age", "sex"])
```

## Key Findings

1. **SAEs transfer across architectures** — a single hyperparameter setting works for SleepFM, REVE, and LaBraM
2. **Clinical features are recoverable** — abnormality, age, sex, and medication signatures emerge as sparse features
3. **Steering selectivity varies** — three distinct regimes from selective to fully entangled
4. **Intrinsic audit predicts transfer** — dictionary health metrics predict downstream steering quality

## Activation Conditions

Use this skill when:
- Interpreting EEG foundation model internals
- Applying SAEs to neural time-series data
- Benchmarking EEG model architectures
- Performing concept steering on brain models
- Analyzing feature entanglement in neural representations
- Evaluating clinical trustworthiness of EEG models

## Related Skills

- `eeg-foundation-lrp-interpretability` - LRP-based EEG interpretability
- `eeg-foundation-model-adapters` - EEG foundation model domain adaptation
- `mechanistic-interpretability` - General mechanistic interpretability methods
