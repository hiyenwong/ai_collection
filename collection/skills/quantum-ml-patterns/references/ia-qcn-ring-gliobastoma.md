# Importance-Aware QCNN with Ring-Topology for Glioblastoma (arXiv:2604.22877)

## Paper
"A Specialized Importance-Aware Quantum Convolutional Neural Network with Ring-Topology (IA-QCNN) for MGMT Promoter Methylation Prediction in Glioblastoma" — Akpinar & Oduncuoglu, 2026-04-24

## Clinical Context
- Glioblastoma (GBM): highly aggressive primary brain malignancy
- MGMT promoter methylation: pivotal prognostic biomarker for temozolomide response
- Personalized treatment requires accurate methylation prediction

## Architecture: IA-QCNN

### Importance-Aware Quantum Convolution (IA-QC)
- Weight quantum convolution operations by feature importance scores
- Prioritize clinically relevant features in quantum circuit design
- Use importance scores to guide qubit allocation and circuit depth

### Ring-Topology Quantum Architecture
- Qubits arranged in ring topology for efficient information flow
- Leverages nearest-neighbor connectivity patterns
- Reduces SWAP gate overhead vs linear arrangements
- Enables quantum convolution with periodic boundary conditions

### Hybrid Pipeline
1. Classical preprocessing: extract molecular/imaging features
2. Quantum convolution: IA-QCNN layers process features
3. Classical post-processing: final binary classification layer
4. End-to-end trainable with gradient-based optimization

## Input Data
- MRI imaging features (radiomics)
- Molecular markers from tumor sequencing
- Clinical patient data
- Multi-modal fusion before quantum processing

## Output
- Binary prediction: MGMT methylated vs unmethylated
- Prediction confidence scores
- Feature importance attribution

## Relationship to quantum-ml-patterns
This extends Pattern 8 (Quantum-Enhanced Medical Diagnostics) with a specific CNN-style quantum architecture for biomarker prediction. The ring-topology arrangement and importance-aware weighting are novel design choices that address common QML challenges (SWAP overhead, irrelevant feature noise).

## When to Use
- Molecular biomarker prediction from multi-modal data
- Binary classification tasks with feature importance structure
- Medical imaging + molecular data fusion scenarios
- Any QCNN where qubit connectivity optimization matters

## Pitfalls
- Feature importance estimation quality directly impacts circuit effectiveness
- Ring topology may not suit all data types — verify connectivity matches structure
- Limited qubit count restricts feature dimensionality — use careful feature selection
- Medical data privacy may limit cloud quantum computing access
