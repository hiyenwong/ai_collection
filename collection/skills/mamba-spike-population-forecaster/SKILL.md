---
name: mamba-spike-population-forecaster
description: >
  Mamba-based neural population spike forecasting for implicit behavioral decoding
  at Neuropixels scale. Trains a single Mamba forecaster on next-step spike counts
  that simultaneously delivers neural forecasts and behavioral readouts in one pass.
  Use when: neural population forecasting, spike-based BCI, behavioral decoding,
  Mamba for neuroscience, Neuropixels data analysis, implicit decoding, next-step
  prediction in neural data, Steinmetz visual-discrimination benchmark, closed-loop
  BCI with forecasting. Activation: mamba spike forecaster, neural population forecast,
  implicit behavioral decoding, next-step spike prediction, Mamba neuroscience,
  Neuropixels BCI, spike count forecasting.
---

# Mamba Spike Population Forecaster for Implicit Behavioral Decoding

A single Mamba forecaster, trained only on next-step spike counts at Neuropixels scale,
delivers both neural population forecasts and behavioral readouts in one forward pass.

## Key Finding

Training a Mamba model to predict next-step spike counts implicitly learns behavioral
state representations. A lightweight per-session linear head reading the model's
predicted rates decodes behavior **better** than the same linear classifier reading
raw spike counts, under matched temporal context.

## Experimental Results

**Dataset**: Steinmetz visual-discrimination benchmark (39 sessions, ~27K neurons, 1,994 held-out trials)

| Metric | Mamba Predicted Rates | Linear Decoder (raw spikes) | Chance |
|--------|----------------------|---------------------------|--------|
| Mouse Choice | 75.7% ± 0.2% trial vote | 69-71% | 50% |
| Stimulus Side | 66.1% ± 0.6% trial vote | 60-62% | 50% |
| Margin | +4-6 pp | baseline | - |

- Results consistent across three training seeds
- Session-start calibration: ~100-150 trials to reach asymptote (within 1-2 pp)
- Full pipeline fits within 50 ms bin budget on workstation-class GPUs
- Suitable for tethered chronic Neuropixels recordings

## Architecture Pattern

```
Raw Spike Counts → Mamba Forecaster → Predicted Rates → Linear Head → Behavioral Output
                                         ↓
                                   Neural Forecast
```

The Mamba forecaster learns rich internal representations of neural population
dynamics during next-step prediction. These predicted rates contain more decodable
behavioral information than the raw inputs, suggesting the model extracts latent
structure from population activity.

## BCI Application

1. **Training**: Train Mamba on next-step spike counts (unsupervised or self-supervised)
2. **Readout**: Attach lightweight per-session linear head to predicted rates
3. **Calibration**: ~100-150 trial calibration block per session
4. **Inference**: Single forward pass delivers both forecast and behavioral decoding
5. **Latency**: <50 ms on workstation GPUs — viable for closed-loop BCI

## Advantages over Direct Decoding

- **Implicit supervision**: No behavioral labels needed during forecaster training
- **Better representations**: Predicted rates > raw spikes for decoding
- **Dual purpose**: Single model for both forecasting and decoding
- **Efficient**: One forward pass, lightweight readout head
- **Transferable**: Forecaster pretrained; linear head adapted per session

## Related Patterns

- See `mamba-spike-forecaster-bci` for Mamba forecaster in closed-loop BCI context
- See `mamba-spike-behavioral-decoding` for implicit behavioral decoding methods
- See `neural-population-dynamics` for population dynamics analysis frameworks

## References

- Paper: arXiv:2605.12999 (submitted to NeurIPS 2026 Neuroscience & Cognitive Science Track)
- Authors: Minnick, Gonzalez-Ferrer, Hussain, Geng, Robbins, Mostajo-Radji, Haussler, Eshraghian, Teodorescu
