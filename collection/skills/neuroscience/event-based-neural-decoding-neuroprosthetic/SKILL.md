# Event-Based Neural Decoding for Neuroprosthetic Motor Control

## Overview
This skill summarizes the methodology from arXiv:2607.11445v1 "Event-based Neural Decoding for Neuroprosthetic Motor Control". The paper proposes a high-performance neural decoding method that balances task performance and efficiency using an event-based gated recurrent unit (GRU) generating sparse communication with graded spikes, enabling on-device neural decoding for neuroprosthetics.

## Core Concepts
- **Event-based GRU**: A recurrent unit that processes spike events asynchronously, producing sparse graded spikes.
- **Sparse Communication**: Reduces bandwidth and energy by transmitting only significant events.
- **Graded Spikes**: Allow amplitude modulation to convey graded information beyond binary spikes.
- **Efficient Training & Sparse Inference**: Training uses surrogate gradients; inference leverages sparsity for low power.

## Workflow Steps
1. **Data Acquisition**: Record neural signals (e.g., ECoG, Utah array) in event-based format (spike times and amplitudes).
2. **Preprocessing**:
   - Align spikes to movement epochs.
   - Bin spikes into short time windows (e.g., 10 ms) preserving temporal resolution.
   - Normalize amplitude values.
3. **Model Architecture**:
   - Input layer receives event-based features (timestamp, amplitude, channel ID).
   - One or more Event-based GRU layers (custom implementation using surrogate gradient for spiking non-linearity).
   - Fully connected readout layer predicting kinematic variables (velocity, position) or discrete intentions.
4. **Training**:
   - Use mean squared error (for continuous) or cross-entropy (for discrete) loss.
   - Apply surrogate gradient (e.g., fast sigmoid) to enable backpropagation through spiking non-linearity.
   - Include sparsity regularization (L1 on spike rates) to encourage event-based efficiency.
   - Train on GPU/CPU with standard deep learning frameworks (PyTorch, TensorFlow).
5. **Inference Deployment**:
   - Deploy model on neuromorphic hardware or low-power MCU.
   - Leverage event-driven computation: only compute when spikes arrive.
   - Output decoded motor commands in real-time to drive prosthetic limb.
6. **Evaluation**:
   - Metrics: decoding accuracy (R² for continuous, accuracy for discrete), latency, energy consumption (estimated via spike count × energy per spike).
   - Compare against baseline dense RNN/LSTM and traditional spike sorting + linear decoder.

## Requirements
- Python ≥3.8
- PyTorch or TensorFlow
- Neuromorphic simulator (e.g., Brian2, Brian2GeNN) or actual hardware (Loihi, SpiNNaker) for deployment
- Neural recording dataset (e.g., BCIs, motor cortex recordings)

## References
- arXiv:2607.11445v1 - Event-based Neural Decoding for Neuroprosthetic Motor Control
- Supplementary material (if available) for detailed equations and pseudocode.

## Usage Hint
Integrate this decoding pipeline into a brain-computer interface (BCI) pipeline where neural events are streamed from an implantable sensor to an on-device decoder, enabling low-latency, low-power prosthetic control.