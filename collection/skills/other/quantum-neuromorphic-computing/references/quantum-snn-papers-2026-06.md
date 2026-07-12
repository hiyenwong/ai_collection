# Quantum-SNN Fusion: Session References (2026-06-15)

## Key Papers from June 2026

### 1. QDS-SNN (arXiv: 2606.07657)
- **Full Title**: Energy-efficient Quantum Deeply-Supervised Spiking Neural Network Algorithm for Traffic Sign Recognition
- **Authors**: Zhiguo Qu, Keqi Li, Le Sun, Wenjie Liu, Yimin Yu, Saif Al-Kuwari, Ahmed Farouk
- **Key Results**: 
  - GTSRB: 99.72% accuracy, 6 time steps, 55.77% energy reduction
  - TSRD: 97.90% accuracy, 52.68% energy reduction
- **Components**: TSA-LIF neuron, QACM (Quantum-Assisted Classifier Module), PennyLane simulation

### 2. Scalable On-Hardware QNN Training (arXiv: 2606.03517)
- **Full Title**: Scalable On-Hardware Training of Quantum Neural Networks and Application to Clinical Data Imputation
- **Authors**: Natansh Mathur, Panagiotis Kl. Barkoutsos, Masako Yamada, Martin Roetteler, Iordanis Kerenidis
- **Key Results**: 16-qubit IonQ hardware training, 32-qubit inference
- **Components**: Butterfly circuit, layer-wise training, parallelized parameter-shift

### 3. QUIVER (arXiv: 2606.09734)
- **Full Title**: Adaptive directional gradients for parameterised quantum circuits
- **Authors**: Brian Coyle, Snehal Raj, Virag Umathe, El Amine Cherrat, Elham Kashefi
- **Key Results**: 60 qubits, 1770 parameters, ECG5000 + MNIST datasets
- **Components**: Forward gradient estimator, QUIVER optimizer, no ancilla overhead

### 4. JGRA (arXiv: 2606.09964)
- **Full Title**: JGRA: Jacobian Geometry Robustness Assessment in NISQ Noise-Aware Quantum Neural Networks
- **Authors**: Gianluca Scanu, Luca Barletta, Stefano Rini
- **Venue**: Accepted at IEEE qCCL 2026
- **Components**: Entropy-matched noise calibration, noise-conditioned Jacobian extraction
