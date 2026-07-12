---
name: digital-quantum-reservoir-computing
description: "Digital quantum reservoir computing (QRC) framework for time series forecasting on near-term quantum devices. Uses parametrized four-qubit reservoirs with partial measurement and reset, encoding temporal data in rotation angles. Training restricted to classical Ridge-regression readout. Use when: quantum reservoir computing, time series forecasting, near-term quantum devices, ATM cash demand prediction, quantum ML for financial data."
metadata:
  arxiv_id: "2606.04686"
  published: "2026-06-03"
  authors: "Chiara Vercellino, Giacomo Vitali, Valeria Zaffaroni, Francesca Cibrario, Emanuele Dri, Paolo Viviani, Olivier Terzo, Davide Corbelletto"
  tags: [quantum-ml, reservoir-computing, time-series, forecasting, near-term-quantum]
---

# Digital Quantum Reservoir Computing for Time Series

## Core Concept

Digital QRC uses parametrized four-qubit reservoirs with fixed structure exploiting partial measurement and reset. Temporal data encoded in rotation angles; training restricted to classical Ridge-regression readout. Systematically analyzed circuit ansatz, reservoir memory, measurement-derived observables, and execution backend impact on forecasting performance.

## Architecture

### Quantum Reservoir

- **4-qubit parametrized reservoir** with fixed structure
- **Partial measurement and reset** between time steps
- **Rotation angle encoding** of temporal input data
- No trainable quantum parameters — only classical readout

### Classical Readout

- **Ridge regression** on quantum measurement outcomes
- Observable selection from measurement-derived operators
- Hyperparameter tuning only at classical level

## Key Findings

- QRC does NOT outperform classical Prophet benchmark in MAE/NMSE
- More competitive results in Dynamic Time Warping metric
- Partial ability to capture temporal structure despite metric limitations
- Validated on noiseless simulation, noise-aware emulation, and real IQM Spark quantum processor

## Workflow

### Step 1: Data Encoding

1. Convert time series to rotation angles via encoding function
2. Apply encoded rotations to 4-qubit reservoir circuit

### Step 2: Reservoir Evolution

1. Run parametrized reservoir circuit
2. Partial measurement of qubits
3. Reset measured qubits to |0⟩
4. Repeat for each time step

### Step 3: Classical Training

1. Extract measurement-derived observables
2. Train Ridge regression on reservoir outputs
3. Validate on held-out time series segments

### Step 4: Evaluation

1. MAE, NMSE for point prediction accuracy
2. Dynamic Time Warping for temporal structure capture
3. Compare against classical baselines

## Hardware Considerations

- Tested on IQM Spark quantum processor
- Noise-aware emulation for intermediate validation
- Near-term device limitations affect performance

## Activation Keywords

- quantum reservoir computing
- digital quantum reservoir
- quantum time series forecasting
- QRC financial prediction
- quantum ML time series
- near-term quantum machine learning
