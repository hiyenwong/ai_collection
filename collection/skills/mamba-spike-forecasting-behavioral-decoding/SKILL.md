---
name: mamba-spike-forecasting-behavioral-decoding
description: "Mamba forecaster methodology for implicit behavioral decoding from next-step spike forecasts at population scale. Applies Mamba state-space models to Neuropixels-scale neural data for simultaneous spike forecasting and behavior decoding."
---

# Mamba Spike Forecasting for Behavioral Decoding

## Core Idea

A single Mamba forecaster, trained only on next-step spike counts at Neuropixels scale, can simultaneously deliver spike forecasting and behavioral readout in one forward pass. The predicted rates from the Mamba model serve as implicit features that decode behavior better than raw spike counts.

## Paper Reference

**Title:** Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale
**Authors:** John R. Minnick, Jesus Gonzalez-Ferrer, Kamran Hussain, Jinghui Geng, Ash Robbins, Mohammed A. Mostajo-Radji, David Haussler, Jason Eshraghian, Mircea Teodorescu
**arXiv:** 2605.12999v1 (q-bio.NC, cs.LG)
**Published:** 2026-05-13
**Submitted to:** NeurIPS 2026 Neuroscience & Cognitive Science Track

## Key Findings

1. **Unified Architecture:** Single Mamba model handles both forecasting and decoding
2. **Performance:** Decodes mouse choice at 75.7% (2.3x chance), stimulus side at 66.1% (2x chance)
3. **Baseline Comparison:** Outperforms linear decoder by 4-6 percentage points
4. **Calibration Efficiency:** 100-150 trials bring readout within 1-2pp of asymptote
5. **Latency:** Full pipeline fits within 50ms bin budget on workstation GPUs

## Benchmark Details

- **Dataset:** Steinmetz visual-discrimination benchmark
- **Scale:** 39 sessions, ~27,000 neurons, 1,994 held-out trials
- **Evaluation:** 3 training seeds for statistical significance

## Architecture

1. **Input:** Next-step spike counts at Neuropixels scale
2. **Model:** Mamba state-space sequence model
3. **Readout:** Lightweight per-session linear head on predicted rates
4. **Output:** Behavioral state predictions (choice, stimulus side)

## Implementation Notes

### Mamba Configuration
- Sequence length matched to temporal context window
- State dimension tuned for neural population size
- Training objective: next-step spike count prediction

### Linear Readout Head
- Per-session adaptation (not cross-session)
- Reads from model's internal predicted rates
- Lightweight: minimal parameters, fast inference

### Calibration
- Session-start calibration block: 100-150 trials
- Rapid convergence to asymptotic performance
- No extensive retraining needed

## Applications

1. **Closed-loop BCIs:** Real-time behavioral state readout
2. **Neural decoding:** Implicit feature extraction from spike forecasts
3. **Population-scale analysis:** Handling Neuropixels-scale data efficiently
4. **Multi-task neural models:** Unified forecasting + decoding

## Activation

- Mamba neural decoding
- spike forecasting behavioral
- Neuropixels decoding
- implicit behavioral readout
- mamba state-space neuroscience
- next-step spike prediction

## Related Work

- State-space models for neural data
- Brain-computer interface decoding
- Neuropixels population analysis
- Steinmetz visual-discrimination benchmark

## Technical Details

### Latency Budget
- Target: 50ms per bin (typical for tethered chronic Neuropixels)
- Achieved: Full pipeline (forecast + decode) within budget
- Hardware: Workstation-class GPUs

### Training Protocol
- Objective: Next-step spike count prediction
- Seeds: 3 training seeds for robustness
- Validation: Held-out trials across sessions

## Potential Extensions

1. Cross-session generalization
2. Multi-modal neural data integration
3. Real-time closed-loop implementation
4. Transfer to human neural data
5. Larger-scale population recordings

## Limitations

- Per-session linear head requires calibration
- Limited to visual-discrimination tasks so far
- GPU requirements for real-time deployment
- Need validation on non-visual tasks
