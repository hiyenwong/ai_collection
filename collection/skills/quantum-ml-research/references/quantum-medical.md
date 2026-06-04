# Quantum ML for Medical Diagnosis

## Key Papers (from 2026-05-06 research session)

### Hybrid Quantum-Classical Feature Fusion (arXiv:2604.22903)
- **Authors**: Yasmin Rodrigues Sobrinho et al.
- **Problem**: Optimization asymmetry between quantum and classical branches
- **Solution**: Three fusion strategies
  - SHF: Static Hybrid Fusion (offline, frozen features)
  - DHF: Dynamic Hybrid Fusion (end-to-end joint training)
  - TSHF: Temperature-Scaled Hybrid Fusion (learnable scalar for gradient balance)
- **Results**: TSHF + ResNet + trainable QC → 87.82% acc, 91.77% F1, 89.08% AUC-ROC on BreastMNIST

### Tensor-Network Quantum Federated Learning (arXiv:2604.01616)
- **Authors**: Hiroshi Yamauchi, Rodney Van Meter et al.
- **Problem**: MPC communication overhead + small-qubit limitation for medical images
- **Solution**: Client-side tensor-network compression (MPS/TTN/MERA) → MPC aggregation → QEP refinement
- **Key finding**: TTN+QEP combination most balanced; qubit count must match latent dimension
- **Dual role**: TN compression enables small-qubit processing AND reduces MPC overhead

### Hybrid QNN for Breast Cancer Thermography (arXiv:2604.16953)
- **Authors**: Riza Alaudin Syah et al.
- **Architecture**: 4-qubit variational circuit + multi-head attention + classical CNN
- **Result**: Superior convergence and feature representation vs. classical baselines

### QML for Coronary Heart Disease (arXiv:2409.10932)
- **Authors**: Mehroush Banday et al.
- **Deployment**: Raspberry Pi 5 GPU platform
- **Result**: Hybrid QML outperforms classical ML in accuracy, sensitivity, F1, specificity

### Formal Methods for Quantum Medicine (arXiv:2502.18639)
- **Authors**: Markus Bertl et al. (AISoLA 2024)
- **Key idea**: Formal specification + model checking + theorem proving for quantum medical algorithms
- **Four contributions**: (1) behavior specification, (2) model checking, (3) theorem proving, (4) optimization

## Datasets

| Dataset | Task | Best Approach | Metric |
|---------|------|---------------|--------|
| BreastMNIST | Cancer classification | ResNet + TSHF + QC | 87.82% acc |
| PneumoniaMNIST | Pneumonia detection | TTN + QEP | Balanced |
| CHD datasets | Heart disease | Ensemble QML | Higher F1 |
| MedMNIST v2 | Multi-task | HQCNN | Competitive |

## Benchmarks

- **QEP stability**: Requires qubit count ≈ latent dimension
- **Noise sensitivity**: QEP degrades under noise vs. noiseless simulation
- **Current quantum advantage**: Demonstrated via classical simulation only
- **Parameter efficiency**: QC reduces trainable parameters by 10-100x
