# Stochastic Quantum Spiking Neural Networks (SQSNN) — arXiv:2506.21324

## Core Innovation
Multi-qubit quantum circuits for spiking neurons with internal quantum memory, eliminating the two key limitations of existing quantum SNNs:
1. Classical memory on single qubits requiring repeated measurements → replaced by quantum memory
2. Dependence on classical backpropagation → replaced by local learning rules

## Architecture
- SQS neuron: multi-qubit quantum circuit with internal quantum memory
- SQSNN: networks of SQS neurons
- Single-shot probabilistic spike generation during inference (no repeated measurements)

## Training
- Hardware-friendly local learning rule
- Synapses update based on local pre/post spike correlations
- No global gradient computation or backpropagation needed
- Outperforms Q-SNN predecessors and classical models at fixed parameter count

## Complementary to QHDC
QHDC (2511.12664) provides quantum-native brain-inspired representation learning; SQSNN provides quantum-native brain-inspired temporal/spiking computation. Together they form a complete quantum neuromorphic stack.
