---
name: dance-eeg-event-detection-classification
description: "DANCE (Detect and Classify Events in EEG) — deep learning pipeline that frames neural decoding as a set-prediction problem for joint event detection and classification from raw, unaligned EEG signals. Activation triggers: DANCE, EEG event detection, set prediction, asynchronous neural decoding, event-based EEG, raw EEG decoding, event classification, Meta AI EEG."
---

# DANCE: Detect and Classify Events in EEG

> End-to-end set-prediction framework for jointly detecting and classifying neural events directly from raw, unaligned EEG signals — eliminating the need for onset-informed segmentation that dominates current benchmarks.

## Metadata
- **Source**: arXiv:2605.10688
- **Authors**: Jarod Lévy, Hubert Banville, Jérémy Rapin, Jean-Remi King, Thomas Moreau, Stéphane d'Ascoli
- **Published**: 2026-05-11
- **Affiliations**: Meta AI, Inria (Université Paris-Saclay)

## Core Methodology

### Problem Statement
Current EEG decoding is dominated by classifying **pre-segmented windows** aligned to known event onsets — a paradigm that works in controlled experiments but fails in real-world continuous monitoring where onset markers are unavailable. DANCE bridges this gap by treating neural decoding as a **set-prediction problem**: jointly detecting *when* events occur and *what* they are, directly from continuous raw signals.

### Key Innovation: Set-Prediction for EEG
Instead of dense sample-by-sample classification or sliding-window approaches, DANCE predicts a **set of events** (each with start time, end time, and class label) in one forward pass. This is inspired by DETR-style object detection in computer vision, adapted for 1D temporal neural signals.

### Architecture

```
Raw EEG (continuous window)
    │
    ▼
┌─────────────────┐
│  CNN Backbone    │  ← Extracts local spatio-temporal features from multi-channel EEG
│  (1D conv)       │
└────────┬────────┘
         ▼
┌─────────────────┐
│  Perceiver       │  ← Global context aggregation across time and channels
│  (cross-attention)│
└────────┬────────┘
         ▼
┌─────────────────┐
│  Decoder         │  ← Predicts N event hypotheses: (start, end, class)
│  (transformer)   │
└─────────────────┘
```

### Loss Formulation
The model uses a **set-prediction loss** combining:
1. **Classification loss**: Cross-entropy for event class prediction
2. **Temporal localization loss**: Bounding box regression for start/end times (smooth L1 or GIoU adapted for time)
3. **Hungarian matching**: Optimal bipartite matching between predicted and ground-truth event sets to handle variable event counts

### Evaluation Paradigm
Two complementary metrics:
- **Event-based**: Precision/recall/F1 on detected events (requires temporal tolerance window)
- **Sample-based**: Per-sample classification accuracy (dense prediction baseline)

Evaluated on **10 heterogeneous datasets** spanning 6 modalities:
- Typing, Seizure monitoring, Speech listening, Motor imagery, P300, Artifact detection
- Total: 2.35 million events across datasets

### Results Summary
- Outperforms existing methods across cognitive, clinical, and BCI tasks
- Sets new state-of-the-art for **seizure monitoring**
- Matches accuracy of onset-informed models for **BCI tasks** (despite not using onset markers)
- Single architecture handles diverse event types (milliseconds to minutes)

## Implementation Guide

### Prerequisites
- PyTorch
- EEG data in standard formats (EDF, BIDS)
- Event annotations with (start, end, label) tuples

### Step-by-Step

1. **Data Preparation**
   - Collect continuous EEG recordings with event annotations
   - Segment into fixed-length windows (no onset alignment needed)
   - Normalize per-channel (z-score or band-pass filter)

2. **Model Construction**
   ```python
   import torch
   import torch.nn as nn

   class DanceModel(nn.Module):
       def __init__(self, n_channels, n_classes, n_queries=20, d_model=256):
           super().__init__()
           # CNN backbone for local features
           self.backbone = nn.Sequential(
               nn.Conv1d(n_channels, 64, kernel_size=3, padding=1),
               nn.ReLU(),
               nn.Conv1d(64, 128, kernel_size=3, padding=1),
               nn.ReLU(),
               nn.Conv1d(128, d_model, kernel_size=3, padding=1),
           )
           # Perceiver for global context
           self.perceiver = nn.TransformerEncoder(
               nn.TransformerEncoderLayer(d_model, nhead=8),
               num_layers=4
           )
           # Decoder heads
           self.class_head = nn.Linear(d_model, n_classes)
           self.time_head = nn.Linear(d_model, 2)  # start, end
           self.query_embed = nn.Parameter(torch.randn(n_queries, d_model))

       def forward(self, x):
           # x: (batch, channels, time)
           features = self.backbone(x)  # (batch, d_model, time)
           features = features.permute(2, 0, 1)  # (time, batch, d_model)
           context = self.perceiver(features)  # (time, batch, d_model)
           # Cross-attend queries to context
           queries = self.query_embed.unsqueeze(1).expand(-1, x.size(0), -1)
           # ... decode events
           classes = self.class_head(queries.permute(1, 0, 2))
           times = torch.sigmoid(self.time_head(queries.permute(1, 0, 2)))
           return classes, times
   ```

3. **Hungarian Matching for Training**
   ```python
   from scipy.optimize import linear_sum_assignment

   def hungarian_match(pred_times, pred_classes, gt_times, gt_classes, cost_weights):
       # Build cost matrix: classification cost + temporal localization cost
       cost_matrix = (
           cost_weights['cls'] * classification_cost(pred_classes, gt_classes) +
           cost_weights['time'] * temporal_cost(pred_times, gt_times)
       )
       row_ind, col_ind = linear_sum_assignment(cost_matrix)
       return row_ind, col_ind
   ```

4. **Training Loop**
   ```python
   for batch in dataloader:
       pred_classes, pred_times = model(eeg_signal)
       # Hungarian matching
       matched_pred, matched_gt = hungarian_match(...)
       # Compute losses on matched pairs
       loss = class_loss(pred_classes[matched_pred], gt_classes[matched_gt]) + \
              time_loss(pred_times[matched_pred], gt_times[matched_gt])
       loss.backward()
   ```

5. **Inference**
   - Apply confidence threshold to filter low-probability event predictions
   - Apply non-maximum suppression (NMS) to remove overlapping event predictions
   - Output: list of (start_time, end_time, class, confidence) tuples

## Applications
- **Clinical EEG monitoring**: Real-time seizure detection without pre-segmentation
- **BCI systems**: Asynchronous motor imagery and P300 detection
- **Cognitive neuroscience**: Event detection in naturalistic/continuous paradigms
- **Sleep staging**: Automatic detection of sleep events (spindles, K-complexes)
- **Artifact rejection**: Detecting eye blinks, muscle artifacts in continuous EEG

## Pitfalls
- **Event density**: Set prediction works best when events are sparse relative to window length; very high event density may require smaller windows or more queries
- **Temporal resolution**: CNN stride determines minimum temporal granularity of event boundaries
- **Class imbalance**: Rare event classes may need focal loss or class-weighted Hungarian matching
- **Cross-dataset generalization**: Model trained separately per dataset; transfer learning across heterogeneous EEG setups remains an open challenge
- **Computational cost**: Transformer-based Perceiver adds compute vs. pure CNN approaches

## Related Skills
- eeg-foundation-model-adapters
- bandroutenet-eeg-artifact-removal
- explainable-gnn-eeg-neurological
- eeg-ieeg-bridge-bci
- li-dsn-eeg-decoding
