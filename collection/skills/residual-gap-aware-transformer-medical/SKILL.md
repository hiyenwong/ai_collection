---
name: residual-gap-aware-transformer-medical
description: "Residual Gap-Aware Transformer methodology for medium-horizon medical prognosis prediction. Anchors predictions at clinical visits, uses only historical data observed at or before anchor, and predicts future clinical score changes (e.g., 24-month CDR-SB change for Alzheimer's). Addresses baseline severity confounding and irregular biomarker observation patterns. Use when: residual gap prediction, anchor-based medical forecasting, Alzheimer's progression prediction, CDR-SB change forecasting, longitudinal clinical prediction, irregular biomarker time series, ADNI analysis, medium-horizon prognosis."
---

# Residual Gap-Aware Transformer for Medical Prognosis

## Core Problem

Medium-horizon medical prognosis (e.g., 24-month Alzheimer's progression) is difficult because:
1. **Baseline severity confounding** — Future clinical scores remain tied to baseline, making change prediction harder than absolute prediction
2. **Irregular biomarker histories** — Clinical and biomarker data are observed at irregular intervals with missing values
3. **Anchor-dependent predictions** — Predictions must use only data available at the anchor visit

## Residual Gap-Aware Framework

Instead of predicting absolute scores, predict **residual changes**:
```
ΔCDR-SB = CDR-SB(t+24) - CDR-SB(t_anchor)
```

The model learns the gap between expected progression (based on baseline) and actual progression.

## Architecture

```
Irregular History → Time-Aware Encoding → Residual Gap Encoder → Transformer → Δ Prediction
```

### Key Design Choices

1. **Anchor-based sampling** — Each sample anchored at MCI visit, uses only data ≤ anchor time
2. **Residual target** — Predict change from anchor, not absolute future score
3. **Gap-aware attention** — Transformer attends to the gap between baseline trajectory and observed progression
4. **Irregular time encoding** — Handle variable observation intervals in biomarker histories

## Implementation Pattern

```python
class ResidualGapTransformer:
    def __init__(self, d_model, n_heads, n_layers):
        self.encoder = TimeAwareEncoder(d_model)
        self.gap_attention = GapAwareAttention(d_model, n_heads)
        self.transformer = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(d_model, n_heads), n_layers
        )
        self.prediction_head = nn.Linear(d_model, 1)
    
    def forward(self, history, anchor_time, anchor_score):
        """
        history: list of (time, features) tuples up to anchor_time
        anchor_time: time of anchor visit
        anchor_score: clinical score at anchor
        """
        # Encode irregular history
        encoded = self.encoder(history, anchor_time)
        
        # Compute residual gap representation
        gap_rep = self.gap_attention(encoded, anchor_score)
        
        # Transform and predict
        output = self.transformer(gap_rep)
        delta_prediction = self.prediction_head(output[:, -1])
        
        return delta_prediction
```

## Application Scenarios

**Scenario 1: Alzheimer's progression** — Predict 24-month CDR-SB change from ADNI clinical/biomarker histories anchored at MCI visits.

**Scenario 2: Any progressive disease** — Parkinson's UPDRS changes, cancer progression scores, any disease with longitudinal clinical scores.

**Scenario 3: Irregular clinical data** — Works with real-world EHR data where visits and tests are at irregular intervals.

## Pitfalls

- **Anchor selection bias** — Must ensure anchor visits are representative; MCI anchors differ from dementia anchors
- **Time window definition** — 18-30 month window for "24-month" follow-up must be consistent
- **Harmonization** — Multi-site data (like ADNI) requires harmonization to remove site effects
- **Small effect sizes** — Medium-horizon changes are subtle; model must be sensitive to small signals

## Activation

残差间隙预测, residual gap transformer, anchor-based medical forecasting, Alzheimer's CDR-SB prediction, longitudinal clinical prognosis, irregular biomarker prediction, ADNI forecasting
