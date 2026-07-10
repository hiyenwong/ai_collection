---
name: dance-eeg-event-detection
description: DANCE (Detect And Classify Events) — deep learning pipeline for joint event detection and classification from continuous, unaligned EEG signals. Frames neural decoding as a set-prediction problem, eliminating the need for pre-aligned event windows. Achieves SOTA on seizure monitoring and matches onset-informed BCI models. Use when working with: EEG event detection, continuous neural decoding, seizure detection, asynchronous BCI, set prediction for time series, or real-time neural monitoring. Trigger words: DANCE, EEG event detection, continuous decoding, set prediction EEG, asynchronous neural decoding.
---

# DANCE: Detect And Classify Events in EEG

Based on arXiv:2605.10688

## Core Problem

Traditional EEG decoding classifies **fixed windows aligned to known event onsets** — fine for controlled experiments, but onset labels are unavailable in continuous real-world monitoring.

DANCE solves this by framing neural decoding as a **set-prediction problem**: jointly detect AND classify events directly from raw, unaligned signals.

## Architecture

```
Raw EEG (continuous) → Feature Encoder → Set Prediction Head → {Events: (time, class)}
```

### Key Design

- **Set prediction formulation**: Model outputs a set of (timestamp, class) pairs — no fixed windows needed
- **End-to-end asynchronous**: No alignment to stimulus markers required
- **Handles variable duration**: Events from milliseconds (ERPs) to minutes (seizures) in one model

## Set Prediction Loss

Uses bipartite matching (Hungarian algorithm) between predicted and ground-truth events:

```python
from scipy.optimize import linear_sum_assignment

def set_prediction_loss(pred_events, gt_events, num_classes):
    """
    pred_events: [(time, class_logit), ...] — N predictions
    gt_events: [(time, class_label), ...] — M ground truth
    """
    # Build cost matrix: time distance + classification cost
    cost_matrix = build_cost_matrix(pred_events, gt_events)
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    
    # Matched pairs: regression + classification loss
    matched_loss = compute_matched_loss(pred_events, gt_events, row_ind, col_ind)
    
    # Unmatched predictions: objectness penalty
    unmatched_loss = compute_unmatched_loss(pred_events, set(range(len(pred_events))) - set(row_ind))
    
    return matched_loss + unmatched_loss
```

## Performance

Evaluated on **10 datasets** spanning:
- Cognitive tasks (ERP detection)
- Clinical monitoring (seizure detection — new SOTA)
- BCI applications (matches onset-informed model accuracy)

## When to Use

- **Use DANCE when**: Continuous EEG monitoring without onset labels, real-time seizure detection, asynchronous BCI, mixed event-type pipelines
- **Don't use when**: You have perfectly aligned event windows and only need classification (simpler models suffice)
- **Keywords**: DANCE, EEG event detection, continuous decoding, set prediction, asynchronous BCI, seizure monitoring, unaligned neural signals

## Comparison to Traditional Approaches

| Aspect | Window-based Classification | DANCE (Set Prediction) |
|--------|---------------------------|----------------------|
| Onset labels needed | Yes | No |
| Event duration range | Fixed | Variable |
| Real-time capable | Requires alignment | Direct from raw signal |
| Seizure detection | Suboptimal | SOTA |
| BCI accuracy | Good (with alignment) | Matches aligned models |

## arXiv Reference

- Paper: "DANCE: Detect and Classify Events in EEG"
- ID: 2605.10688
- URL: https://arxiv.org/abs/2605.10688
