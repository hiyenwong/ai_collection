---
name: tta-eeg-foundation-models
description: >
  Test-time adaptation (TTA) methods for EEG foundation models under real-world
  distribution shifts. Covers entropy minimization, batch norm adaptation, TENT,
  MEMO, CoTTA, EATA, SAR, and related methods applied to EEG signals across
  cross-device, cross-subject, cross-session, and cross-clinical-site settings.
  Addresses privacy-preserving adaptation without source data access.
triggers:
  - EEG
  - electroencephalography
  - test-time adaptation
  - TTA
  - foundation model
  - distribution shift
  - clinical deployment
  - domain adaptation
  - entropy minimization
  - batch norm adaptation
  - cross-subject
  - cross-device
  - cross-session
  - cross-clinical-site
  - EEG foundation model
  - privacy-preserving adaptation
  - TENT
  - MEMO
  - CoTTA
  - EATA
  - SAR
  - real-world distribution shift
  - brain signal
  - neural signal processing
---

# Test-Time Adaptation for EEG Foundation Models

> Based on: "Test-Time Adaptation for EEG Foundation Models: A Systematic Study under Real-World Distribution Shifts" (arXiv 2604.16926)
> Authors: Gabriel Jason Lee, Jathurshan Pradeepkumar, Jimeng Sun
> Categories: cs.LG, cs.AI, eess.SP

---

## 1. Overview: Why TTA Matters for EEG Foundation Models

### The Problem

EEG foundation models (FMs) pre-trained on large-scale EEG datasets achieve strong generalization, but real-world deployment faces fundamental distribution shifts that degrade performance:

- **Device heterogeneity**: Different EEG systems (e.g., 14-channel Emotiv vs. 128-channel Biosemi) produce signals with varying channel configurations, impedances, and noise profiles.
- **Subject variability**: Inter-individual differences in brain anatomy, age, pathology, and baseline rhythms create substantial covariate shift.
- **Session drift**: The same subject's EEG changes across recording sessions due to fatigue, medication, electrode placement variability, and circadian effects.
- **Clinical site differences**: Different hospitals use different protocols, preprocessing pipelines, and clinical populations.

### Why Test-Time Adaptation?

Traditional domain adaptation requires access to labeled source data during training — often impossible in clinical settings due to:

1. **Privacy regulations** (HIPAA, GDPR): Patient EEG data cannot leave the originating institution.
2. **Limited labeled data**: New deployment sites rarely have labeled EEG data.
3. **Continual shift**: Distribution shifts evolve over time and are not stationary.

TTA solves this by adapting the model **at inference time** using only unlabeled target data, requiring **no access to source data** and **no labels from the target domain**.

### Key Insight from the Paper

Not all TTA methods work equally well for EEG. The non-stationary, high-dimensional, and artifact-prone nature of EEG signals means methods designed for natural images (e.g., TENT) can fail catastrophically. A systematic evaluation reveals which methods are robust under clinically realistic conditions.

---

## 2. Core Methodology

### 2.1 TTA Methods for EEG Foundation Models

#### Entropy Minimization Family

| Method | Mechanism | Update Target | Key Feature |
|--------|-----------|---------------|-------------|
| **TENT** (Wang et al., 2021) | Minimize prediction entropy via batch norm parameter updates | Batch norm affine parameters (γ, β) | Single-pass; updates BN statistics and affine params |
| **EATA** (Niu et al., 2022) | Entropy minimization + active sample selection + anti-forgetting | Batch norm parameters | Filters low-confidence samples; Fisher regularized to prevent catastrophic forgetting |
| **SAR** (Niu et al., 2023) | Sharpness-aware entropy minimization | Batch norm parameters | Removes high-entropy sample contribution; robust to noisy/ambiguous EEG epochs |
| **MEMO** (Zhang et al., 2022) | Marginal entropy minimization with single-sample augmentation | All model parameters | Augments each test sample, minimizes marginal entropy; robust to single-sample TTA |

#### Continual Adaptation Family

| Method | Mechanism | Update Target | Key Feature |
|--------|-----------|---------------|-------------|
| **CoTTA** (Wang et al., 2022) | Continual TTA with teacher-student stochastic augmentation | All model parameters | Periodically restores teacher weights; prevents error accumulation over long-term deployment |
| **ETA** (Niu et al., 2022) | Equilibrated TENT | Batch norm parameters | Reduces reliance on batch statistics; better for small batch EEG scenarios |

#### Batch Norm Adaptation

- **BN statistics update**: Replace source BN running statistics (μ, σ²) with target-domain batch statistics.
- **Simplest form of TTA** — no gradient computation required.
- Effective when the primary shift is in feature scale/mean (common in cross-device EEG).
- Can be combined with any other TTA method.

#### Additional Methods to Consider

- **PL (Pseudo-Labeling)**: Use high-confidence predictions as pseudo-labels for self-training at test time.
- **SHOT** (Li et al., 2020): Source-free domain adaptation via information maximization and pseudo-labeling.
- **TAST** (Test-time self-training): Iterative self-training at test time with entropy-based sample selection.

### 2.2 Distribution Shift Taxonomy in EEG

```
EEG Distribution Shifts
├── Cross-Device (Sensor Shift)
│   ├── Different channel counts (14 vs 32 vs 64 vs 128)
│   ├── Different electrode layouts (10-20 vs dense arrays)
│   ├── Different sampling rates (256 Hz vs 512 Hz vs 1024 Hz)
│   ├── Different ADC resolution and noise floors
│   └── Dry vs wet electrodes
├── Cross-Subject (Biological Shift)
│   ├── Age-dependent EEG changes (pediatric vs adult vs elderly)
│   ├── Pathology-dependent patterns (healthy vs epileptic vs post-stroke)
│   ├── Inter-individual anatomical variability
│   ├── Medication effects
│   └── Cognitive state baseline differences
├── Cross-Session (Temporal Shift)
│   ├── Electrode re-placement variability (±5mm displacement)
│   ├── Fatigue and alertness changes within/across sessions
│   ├── Circadian rhythm effects on spectral power
│   ├── Learning/plasticity effects (session 1 vs session 10)
│   └── Impedance drift during recording
└── Cross-Clinical-Site (Institutional Shift)
    ├── Different preprocessing pipelines (filter settings, artifact removal)
    ├── Different clinical protocols (eyes-open vs eyes-closed vs task)
    ├── Different patient populations and recruitment criteria
    ├── Different recording environments (shielded room vs ICU)
    └── Different ground/reference electrode placements
```

### 2.3 Method Selection Guide

| Scenario | Recommended Primary Method | Rationale |
|----------|---------------------------|-----------|
| Cross-device (same population) | BN adaptation + TENT | Feature-level scale shift dominates |
| Cross-subject (same device) | CoTTA or EATA | Continual biological variability; need anti-forgetting |
| Cross-session (same subject, same device) | SAR or EATA | Gradual drift; noisy single-sample adaptation |
| Cross-clinical-site (mixed shifts) | CoTTA + MEMO | Compound shift; need robust continual adaptation |
| Online/streaming EEG | EATA or SAR | Efficient per-sample adaptation with sample filtering |
| Low-latency clinical deployment | BN adaptation only | No gradient computation; fastest inference |

---

## 3. Implementation Guide

### 3.1 Prerequisites

```python
# Core dependencies
# - PyTorch >= 1.12 (for batch norm manipulation)
# - Pre-trained EEG foundation model (e.g., BioSig, LaBraM, EEGPT)
# - Target EEG data loader (unlabeled)
```

### 3.2 TENT for EEG Foundation Models

```python
import torch
import torch.nn as nn
from copy import deepcopy

class TENTAdapter:
    """TENT: Test-time Entropy minimization for EEG foundation models.

    Updates batch norm affine parameters (gamma, beta) to minimize
    prediction entropy on unlabeled target EEG data.

    Reference: Wang et al., "Tent: Fully Test-Time Adaptation by Entropy
    Minimization", ICLR 2021.
    """

    def __init__(self, model, lr=1e-3, eps=1e-5):
        self.model = deepcopy(model)
        self.model.eval()

        # Collect batch norm parameters for optimization
        self.bn_params = []
        for m in self.model.modules():
            if isinstance(m, (nn.BatchNorm1d, nn.BatchNorm2d, nn.LayerNorm)):
                if m.weight is not None and m.bias is not None:
                    self.bn_params.append(m.weight)
                    self.bn_params.append(m.bias)

        self.optimizer = torch.optim.Adam(self.bn_params, lr=lr)
        self.eps = eps

    @torch.enable_grad()
    def adapt_and_predict(self, x):
        """Adapt on a batch of unlabeled EEG and return predictions.

        Args:
            x: Input EEG tensor of shape (batch, channels, time) or
               (batch, channels, time, features)

        Returns:
            predictions: Model predictions after adaptation step
        """
        self.optimizer.zero_grad()

        # Forward pass
        logits = self.model(x)

        # Compute entropy loss
        probs = torch.softmax(logits, dim=-1)
        log_probs = torch.log(probs + self.eps)
        entropy = -(probs * log_probs).sum(dim=-1).mean()

        # Backward pass — only BN affine params have gradients
        entropy.backward()
        self.optimizer.step()

        # Return predictions (detached)
        return logits.detach()

    def reset(self):
        """Reset adapter state (e.g., between patients)."""
        # Re-initialize BN parameters if needed
        pass
```

### 3.3 EATA for EEG (with Sample Filtering)

```python
class EATAAdapter:
    """EATA: Efficient Test-Time Adaptation for EEG.

    Extends TENT with:
    1. Active sample filtering (only adapt on confident samples)
    2. Fisher information regularization (anti-forgetting)

    Reference: Niu et al., "Efficient Test-Time Model Adaptation without
    Forgetting", ICML 2022.
    """

    def __init__(self, model, lr=1e-3, fisher_alpha=2000.0,
                 entropy_threshold=0.5 * np.log(10)):
        self.model = deepcopy(model)
        self.model.eval()
        self.fisher_alpha = fisher_alpha
        self.entropy_threshold = entropy_threshold

        # BN parameters
        self.bn_params = []
        for m in self.model.modules():
            if isinstance(m, (nn.BatchNorm1d, nn.LayerNorm)):
                if m.weight is not None and m.bias is not None:
                    self.bn_params.append(m.weight)
                    self.bn_params.append(m.bias)

        self.optimizer = torch.optim.Adam(self.bn_params, lr=lr)

        # Store initial parameters for Fisher regularization
        self.initial_params = {id(p): p.data.clone() for p in self.bn_params}

        # Fisher information (estimated on first batch)
        self.fisher_info = {id(p): torch.zeros_like(p) for p in self.bn_params}
        self.fisher_estimated = False

    def _compute_fisher(self, x):
        """Estimate Fisher information matrix on target data."""
        self.model.zero_grad()
        logits = self.model(x)
        probs = torch.softmax(logits, dim=-1)

        # Sample from model distribution
        for _ in range(10):
            sampled = torch.multinomial(probs, 1).squeeze(-1)
            log_probs = torch.log_softmax(logits, dim=-1)
            selected_log_probs = log_probs.gather(1, sampled.unsqueeze(1)).squeeze()
            selected_log_probs.mean().backward(retain_graph=True)

            for p in self.bn_params:
                self.fisher_info[id(p)] += p.grad.data.clone() ** 2
                p.grad.zero_()

        for p in self.bn_params:
            self.fisher_info[id(p)] /= 10.0
        self.fisher_estimated = True

    @torch.enable_grad()
    def adapt_and_predict(self, x):
        """Adapt with sample filtering and anti-forgetting regularization."""
        self.optimizer.zero_grad()

        logits = self.model(x)
        probs = torch.softmax(logits, dim=-1)
        log_probs = torch.log(probs + 1e-5)

        # Per-sample entropy
        sample_entropy = -(probs * log_probs).sum(dim=-1)

        # Filter: only adapt on low-entropy (confident) samples
        mask = sample_entropy < self.entropy_threshold

        if mask.sum() == 0:
            return logits.detach()

        # Entropy loss on filtered samples
        entropy_loss = sample_entropy[mask].mean()

        # Fisher regularization: penalize deviation from initial params
        fisher_loss = 0.0
        if self.fisher_estimated:
            for p in self.bn_params:
                fisher_loss += (
                    self.fisher_info[id(p)] * (p - self.initial_params[id(p)]) ** 2
                ).sum()

        total_loss = entropy_loss + self.fisher_alpha * fisher_loss

        total_loss.backward()
        self.optimizer.step()

        return logits.detach()
```

### 3.4 CoTTA for Continual EEG Adaptation

```python
class CoTTAAdapter:
    """CoTTA: Continual Test-Time Adaptation for streaming EEG.

    Maintains a teacher-student pair with stochastic weight restoration
    to prevent error accumulation over long deployment periods.

    Reference: Wang et al., "Continual Test-Time Domain Adaptation",
    CVPR 2022.
    """

    def __init__(self, model, lr=1e-3, alpha=0.1, restore_prob=0.05):
        self.teacher = deepcopy(model)
        self.student = deepcopy(model)
        self.teacher.eval()
        self.student.eval()

        self.alpha = alpha  # EMA mixing coefficient
        self.restore_prob = restore_prob

        # Student trainable parameters (BN only or full)
        self.optimizable_params = []
        for m in self.student.modules():
            if isinstance(m, (nn.BatchNorm1d, nn.LayerNorm)):
                if m.weight is not None:
                    self.optimizable_params.append(m.weight)
                if m.bias is not None:
                    self.optimizable_params.append(m.bias)

        self.optimizer = torch.optim.Adam(self.optimizable_params, lr=lr)

    @torch.enable_grad()
    def adapt_and_predict(self, x):
        """Continual adaptation with stochastic restoration."""
        # Stochastic weight restoration
        if torch.rand(1).item() < self.restore_prob:
            for s_param, t_param in zip(
                self.student.parameters(), self.teacher.parameters()
            ):
                if s_param.requires_grad:
                    s_param.data = self.alpha * s_param.data + (
                        1 - self.alpha
                    ) * t_param.data

        # Augmented forward pass
        x_aug = x + torch.randn_like(x) * 0.01  # Small noise augmentation

        self.optimizer.zero_grad()
        logits = self.student(x_aug)

        # Teacher pseudo-labels
        with torch.no_grad():
            teacher_logits = self.teacher(x)
            pseudo_labels = teacher_logits.argmax(dim=-1)

        # Cross-entropy with teacher pseudo-labels
        loss = nn.functional.cross_entropy(logits, pseudo_labels)
        loss.backward()
        self.optimizer.step()

        # Update teacher via EMA
        with torch.no_grad():
            for s_param, t_param in zip(
                self.student.parameters(), self.teacher.parameters()
            ):
                t_param.data = self.alpha * t_param.data + (
                    1 - self.alpha
                ) * s_param.data

        return logits.detach()
```

### 3.5 Batch Norm Statistics Update (Lightweight Baseline)

```python
def adapt_bn_statistics(model, target_loader, num_batches=10):
    """Update batch norm running statistics with target EEG data.

    This is the simplest TTA method — no gradient computation needed.
    Effective when distribution shift is primarily in feature scale/mean.

    Args:
        model: Pre-trained EEG foundation model
        target_loader: DataLoader with unlabeled target EEG data
        num_batches: Number of batches to use for statistics estimation
    """
    # Reset BN statistics
    for m in model.modules():
        if isinstance(m, (nn.BatchNorm1d, nn.BatchNorm2d)):
            m.reset_running_stats()

    model.eval()
    with torch.no_grad():
        for i, batch in enumerate(target_loader):
            if i >= num_batches:
                break
            x = batch[0] if isinstance(batch, (list, tuple)) else batch
            _ = model(x)  # Forward pass updates BN running stats

    return model
```

### 3.6 Handling Channel Mismatch Across Devices

```python
def align_channels(source_channels, target_channels, eeg_data):
    """Align target EEG channels to source model's expected channel configuration.

    Handles the cross-device shift where channel sets differ.

    Args:
        source_channels: List of channel names the model was trained on
        target_channels: List of channel names in target data
        eeg_data: Target EEG tensor (batch, channels, time)

    Returns:
        Aligned EEG tensor matching source channel configuration
    """
    import numpy as np

    # Standard 10-20 channel name mappings
    channel_map = {
        'FP1': 'Fp1', 'FP2': 'Fp2', 'FZ': 'Fz', 'CZ': 'Cz', 'PZ': 'Pz',
        'OZ': 'Oz', 'F3': 'F3', 'F4': 'F4', 'C3': 'C3', 'C4': 'C4',
        'P3': 'P3', 'P4': 'P4', 'O1': 'O1', 'O2': 'O2', 'F7': 'F7',
        'F8': 'F8', 'T3': 'T3', 'T4': 'T4', 'T5': 'T5', 'T6': 'T6',
    }

    # Normalize channel names
    target_normalized = [channel_map.get(ch.upper(), ch.upper()) for ch in target_channels]
    source_normalized = [channel_map.get(ch.upper(), ch.upper()) for ch in source_channels]

    # Build alignment mapping
    aligned_data = torch.zeros(eeg_data.shape[0], len(source_channels), eeg_data.shape[2])

    for src_idx, src_ch in enumerate(source_normalized):
        if src_ch in target_normalized:
            tgt_idx = target_normalized.index(src_ch)
            aligned_data[:, src_idx, :] = eeg_data[:, tgt_idx, :]
        # Missing channels remain zero (or use interpolation for nearby electrodes)

    return aligned_data
```

---

## 4. Clinical Deployment Pipeline

### 4.1 End-to-End TTA Deployment Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   CLINICAL EEG DEPLOYMENT PIPELINE              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────┐  │
│  │  EEG Device   │───▶│  Preprocessing│───▶│  Channel Align  │  │
│  │  (Target)     │    │  Pipeline     │    │  & Resampling   │  │
│  └──────────────┘    └──────────────┘    └────────┬─────────┘  │
│                                                    │             │
│                                          ┌────────▼─────────┐  │
│                                          │  EEG Foundation  │  │
│                                          │  Model (Frozen)  │  │
│                                          └────────┬─────────┘  │
│                                                    │             │
│                              ┌─────────────────────┼─────────┐  │
│                              │                     │         │  │
│                    ┌─────────▼──────────┐  ┌──────▼───────┐  │  │
│                    │  TTA Engine        │  │  Shift        │  │  │
│                    │  (TENT/CoTTA/EATA) │  │  Detector     │  │  │
│                    └─────────┬──────────┘  └──────┬───────┘  │  │
│                              │                     │          │  │
│                    ┌─────────▼─────────────────────▼───────┐  │  │
│                    │        Adapted Predictions            │  │  │
│                    │  + Confidence Scores                  │  │  │
│                    └──────────────────┬────────────────────┘  │  │
│                                       │                       │  │
│                    ┌──────────────────▼────────────────────┐  │  │
│                    │     Clinical Decision Support         │  │  │
│                    │  (Alert / Escalate / Log)             │  │  │
│                    └───────────────────────────────────────┘  │  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Monitoring Layer                                         │  │
│  │  - Adaptation stability tracker                          │  │
│  │  - Performance degradation alerts                        │  │
│  │  - Automatic reset triggers                              │  │
│  │  - Audit log for regulatory compliance                   │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Deployment Checklist

1. **Pre-deployment**
   - [ ] Validate EEG FM on held-out clinical sites
   - [ ] Characterize expected distribution shifts (device, population)
   - [ ] Select TTA method matched to expected shift type (see §2.3)
   - [ ] Establish baseline performance without TTA
   - [ ] Define adaptation reset criteria (e.g., after N patients)

2. **At deployment site**
   - [ ] Verify target device channel configuration
   - [ ] Implement channel alignment pipeline
   - [ ] Collect warm-up batch for BN statistics (if applicable)
   - [ ] Initialize TTA adapter with source-pretrained weights
   - [ ] Enable shift detection monitoring

3. **During operation**
   - [ ] Monitor prediction entropy distribution (drift indicator)
   - [ ] Track adaptation step count per patient/session
   - [ ] Flag anomalous adaptations (entropy spikes)
   - [ ] Periodically evaluate on labeled calibration data (if available)
   - [ ] Log all adaptation events for audit trail

4. **Regulatory considerations**
   - [ ] Document TTA method as part of the device's adaptive algorithm
   - [ ] Define and validate the adaptation boundary conditions
   - [ ] Ensure TTA does not violate locked-device requirements (if applicable)
   - [ ] Maintain version control of both source model and TTA configuration

### 4.3 Streaming EEG Adaptation Protocol

```python
class StreamingEEGTTA:
    """Online TTA for streaming clinical EEG data.

    Processes EEG in fixed-length windows with continuous adaptation.
    """

    def __init__(self, model, tta_method='eata', window_length=2.0,
                 sampling_rate=256, stride=0.5):
        self.window_length = window_length
        self.sampling_rate = sampling_rate
        self.stride = stride
        self.window_samples = int(window_length * sampling_rate)
        self.stride_samples = int(stride * sampling_rate)

        # Initialize TTA adapter
        if tta_method == 'tent':
            self.adapter = TENTAdapter(model)
        elif tta_method == 'eata':
            self.adapter = EATAAdapter(model)
        elif tta_method == 'cotta':
            self.adapter = CoTTAAdapter(model)
        else:
            raise ValueError(f"Unknown TTA method: {tta_method}")

        self.buffer = torch.tensor([])
        self.prediction_history = []

    def process_chunk(self, new_eeg_chunk):
        """Process incoming EEG chunk with TTA.

        Args:
            new_eeg_chunk: Tensor of shape (channels, new_samples)

        Yields:
            (timestamp, prediction, confidence) tuples
        """
        self.buffer = torch.cat([self.buffer, new_eeg_chunk], dim=-1)

        while self.buffer.shape[-1] >= self.window_samples:
            # Extract window
            window = self.buffer[:, :self.window_samples]
            self.buffer = self.buffer[:, self.stride_samples:]

            # Add batch dimension
            window_batch = window.unsqueeze(0)  # (1, channels, time)

            # Adapt and predict
            logits = self.adapter.adapt_and_predict(window_batch)
            probs = torch.softmax(logits, dim=-1)
            confidence = probs.max(dim=-1).values.item()
            prediction = logits.argmax(dim=-1).item()

            self.prediction_history.append({
                'prediction': prediction,
                'confidence': confidence,
                'entropy': -(probs * torch.log(probs + 1e-5)).sum().item(),
            })

            yield prediction, confidence
```

---

## 5. Evaluation Framework Under Real-World Distribution Shifts

### 5.1 Evaluation Protocol

```
Evaluation Design for EEG TTA:

1. Source Training Phase
   └── Train EEG FM on source dataset (e.g., TUH EEG Corpus)

2. Target Evaluation Phases (each evaluated independently)
   ├── Cross-Device: Same task, different EEG device
   ├── Cross-Subject: Same device, unseen subjects
   ├── Cross-Session: Same subject, different recording sessions
   └── Cross-Site: Different hospital/clinical site

3. For each target phase:
   a. Baseline: Zero-shot (no adaptation)
   b. TTA method: Adapt during inference
   c. Oracle upper bound: Fine-tune on labeled target data (if available)
```

### 5.2 Metrics

| Metric | Purpose | Notes for EEG |
|--------|---------|---------------|
| **Classification accuracy** | Overall correctness | May be misleading with class imbalance (e.g., seizure detection) |
| **Balanced accuracy** | Accuracy adjusted for class balance | Preferred for clinical EEG tasks |
| **Macro F1 score** | Per-class harmonic mean | Robust to imbalance |
| **AUC-ROC** | Discrimination ability | Standard for binary clinical tasks (seizure vs non-seizure) |
| **Cohen's kappa** | Agreement beyond chance | Good for multi-class EEG classification |
| **Adaptation efficiency** | Performance gain per adaptation step | Important for real-time deployment |
| **Entropy** | Prediction confidence | Lower = more confident; track drift over time |
| **Stability score** | Prediction consistency across windows | Critical for clinical trust |
| **Adaptation time** | Wall-clock time per sample | Must meet real-time constraints |

### 5.3 Ablation Studies

Conduct systematic ablations to understand:

1. **Method comparison**: Rank TTA methods under each shift type
2. **Batch size sensitivity**: TTA performance vs. number of target samples per adaptation step (1, 4, 16, 64, 256)
3. **Adaptation frequency**: Every sample vs. every N samples vs. periodic reset
4. **Parameter scope**: BN-only vs. full model adaptation
5. **Learning rate sensitivity**: Impact of adaptation learning rate on stability
6. **EEG preprocessing effects**: Does the preprocessing pipeline interact with TTA effectiveness?
7. **Foundation model architecture**: Does TTA effectiveness depend on the FM architecture (Transformer vs. CNN vs. hybrid)?

### 5.4 Statistical Testing

- Use **paired permutation tests** or **Wilcoxon signed-rank tests** for comparing TTA methods (non-parametric, appropriate for small sample sizes typical in clinical EEG).
- Report **95% confidence intervals** via bootstrap (1000+ iterations).
- Correct for multiple comparisons using **Holm-Bonferroni** or **Benjamini-Hochberg** when testing multiple methods.

---

## 6. Pitfalls and Considerations for Clinical EEG

### 6.1 Common Failure Modes

| Pitfall | Description | Mitigation |
|---------|-------------|------------|
| **Catastrophic forgetting** | TTA degrades source knowledge over many steps | Use EATA (Fisher regularization) or CoTTA (weight restoration) |
| **Artifacts as signal** | TTA adapts to EEG artifacts (blinks, motion) rather than neural signal | Pre-filter artifacts; use robust TTA (SAR) with entropy filtering |
| **Batch size sensitivity** | Single-sample TTA is unstable; large batches delay adaptation | MEMO for single-sample; batch accumulation for TENT/EATA |
| **Channel mismatch** | Target device has different channel set than training | Channel alignment + interpolation (see §3.6) |
| **Sampling rate mismatch** | Different devices sample at different rates | Resample to model's expected rate before adaptation |
| **Reference mismatch** | Linked mastoid vs. average vs. Cz reference differences | Re-reference to model's expected reference montage |
| **Confirmation bias** | Pseudo-label errors compound during adaptation | Conservative entropy thresholds; periodic resets |
| **Non-stationarity within session** | EEG changes within a recording (drowsiness, habituation) | Continual methods (CoTTA) with frequent restoration |
| **Regulatory lock** | Medical devices may require fixed, validated models | Use TTA in shadow mode first; validate before clinical use |

### 6.2 EEG-Specific Considerations

1. **Signal non-stationarity**: EEG is inherently non-stationary even without distribution shift. TTA methods must distinguish true domain shift from normal physiological variability. Use statistical tests (e.g., KS test on feature distributions) to trigger adaptation only when genuine shift is detected.

2. **Artifact contamination**: Eye blinks, muscle activity, and line noise are ubiquitous in clinical EEG. These artifacts can dominate entropy-based TTA, causing the model to adapt to artifact patterns rather than neural activity. Always apply artifact rejection or correction (ICA, regression) before TTA.

3. **Small clinical batches**: In clinical settings, you may have very few EEG epochs from a new patient before a decision is needed. MEMO (single-sample augmentation-based TTA) is better suited than batch-dependent methods (TENT).

4. **Class imbalance**: Clinical EEG tasks are often highly imbalanced (e.g., seizures occupy <1% of recording). TTA methods that minimize entropy can be biased toward the majority class. Monitor per-class performance, not just overall metrics.

5. **Temporal correlations**: EEG windows are temporally correlated. Standard TTA assumes i.i.d. samples, which is violated in streaming EEG. Account for this in evaluation by using proper temporal cross-validation, not random splits.

6. **Privacy-aware logging**: TTA adaptation logs (gradient updates, BN statistics) could potentially leak information about target patients. Ensure compliance with HIPAA/GDAA when logging adaptation events.

### 6.3 When NOT to Use TTA

- **Regulatory locked-device requirements**: If the deployment context requires a fixed, validated model with no runtime modification, TTA is not appropriate.
- **Insufficient model confidence**: If the source model's predictions are near-random on target data (entropy near maximum), entropy-based TTA provides no useful gradient signal.
- **Extreme channel mismatch**: If the target device has no overlap with source channels, TTA cannot bridge the gap — retraining with channel alignment is needed.
- **Critical safety decisions**: TTA-adapted models have not been validated on the target distribution. For safety-critical decisions (e.g., intraoperative monitoring), use TTA only as a secondary opinion alongside the frozen model.

---

## 7. References

### Primary Paper

- Lee, G. J., Pradeepkumar, J., & Sun, J. (2025). *Test-Time Adaptation for EEG Foundation Models: A Systematic Study under Real-World Distribution Shifts*. arXiv:2604.16926.

### TTA Methods

- Wang, D., Shelhamer, E., Liu, S., Oliva, D., & Darrell, T. (2021). *Tent: Fully Test-Time Adaptation by Entropy Minimization*. ICLR 2021.
- Zhang, M., Levine, S., & Finn, C. (2022). *MEMO: Test Time Robustness via Adaptation and Augmentation*. NeurIPS 2022.
- Wang, Q., Fink, O., Van Gool, L., & Dai, D. (2022). *Continual Test-Time Domain Adaptation*. CVPR 2022.
- Niu, S., Wu, J., Zhang, Y., Chen, Y., Zheng, S., Zhao, J., & Tan, M. (2022). *Efficient Test-Time Model Adaptation without Forgetting*. ICML 2022.
- Niu, S., Wu, J., Zhang, Y., Wen, Z., Chen, Y., Zheng, S., & Tan, M. (2023). *Towards Stable Test-Time Adaptation in Dynamic Wild World*. ICLR 2023.
- Li, J., Chen, G., & Liu, H. (2020). *Model Adaptation: Unsupervised Domain Adaptation without Source Data*. CVPR 2020.

### EEG Foundation Models

- Jiang, Y., et al. (2024). *LaBraM: Large Brain Model for Learning Generic Representations with Massive EEG Data*. ICML 2024.
- Sun, C., et al. (2024). *EEGPT: Pretrained Transformer for Unified EEG Representation*. arXiv.
- Wang, Y., et al. (2023). *BioSig: A Large-Scale Biosignal Pre-trained Model*.

### EEG Domain Adaptation

- Zhang, X., et al. (2024). *Cross-Subject EEG Domain Adaptation: A Survey*. Neural Networks.
- Li, Y., et al. (2023). *Transfer Learning for EEG: Methods, Applications, and Challenges*. IEEE TBME.

### Clinical EEG Standards

- American Clinical Neurophysiology Society (ACNS). *Guidelines for EEG Recording*.
- International Federation of Clinical Neurophysiology (IFCN). *Standards for Digital EEG*.

---

## Appendix: Quick Reference Card

```
╔══════════════════════════════════════════════════════════════╗
║          TTA for EEG — Method Selection Quick Guide         ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Q1: What type of distribution shift?                       ║
║    ├─ Cross-device    → BN adaptation + TENT                ║
║    ├─ Cross-subject   → CoTTA or EATA                       ║
║    ├─ Cross-session   → SAR or EATA                         ║
║    └─ Cross-site      → CoTTA + MEMO                        ║
║                                                              ║
║  Q2: How many target samples per adaptation step?           ║
║    ├─ Single sample   → MEMO                                ║
║    ├─ Small batch     → EATA or SAR                         ║
║    └─ Large batch     → TENT                                ║
║                                                              ║
║  Q3: Is continual deployment needed?                        ║
║    ├─ Yes (streaming)  → CoTTA (with restoration)           ║
║    ├─ Yes (periodic)   → EATA (with Fisher reg.)            ║
║    └─ No (one-shot)    → TENT or BN adaptation              ║
║                                                              ║
║  Q4: Safety-critical application?                           ║
║    ├─ Yes  → Use TTA as advisory; validate frozen model     ║
║    └─ No   → Full TTA deployment with monitoring            ║
║                                                              ║
║  Q5: Real-time constraint?                                  ║
║    ├─ Strict latency   → BN adaptation only (no grad)       ║
║    ├─ Moderate          → TENT or EATA                      ║
║    └─ Offline/batch     → CoTTA or MEMO                     ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```
