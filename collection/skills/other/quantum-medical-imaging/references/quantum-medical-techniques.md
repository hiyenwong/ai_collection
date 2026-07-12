# Quantum Medical Imaging Techniques

## CV-QNN for Edge Medical AI (arXiv: 2606.28252)
- Simplified Φ∘D∘U₁ architecture reduces params 40-45% vs standard CV-QNN
- PCA to 16D raises gradient variance by ~58 orders of magnitude (barren plateau fix)
- 18-parameter model beats 55-parameter classical baseline
- Room temperature photonic QC — no cryogenics needed for edge deployment

## Fourier-Based Quantum Image Encoding (arXiv: 2505.06471)
- Gate count ≤ N/4 vs standard 2N (4x reduction)
- Two compression techniques with negligible quality loss
- Demonstrated on 1024×1024 medical images (BABA robotic surgery)

## Post-Quantum Healthcare Security (arXiv: 2606.09412, 2606.14515)
- ML-KEM-768 + ML-DSA-65 for PQC pharmacovigilance pipelines
- Kubernetes-based PQC orchestration for IoMT federated learning
- Raspberry Pi testbed validated feasible overhead

## Hybrid Quantum-Classical PINNs (arXiv: 2606.01110)
- Quantum-classical FBPINN: 8x fewer iterations, 33% fewer params
- Applicable to medical ultrasound tomography

## QSCI for Drug Discovery (arXiv: 2606.30551)
- LCNot-UCCSD ansatz: O(N⁴) vs O(N⁶) parameter init
- QSCI-RBM: RBM replaces SQD configuration recovery
- Applied to Amantadine and SARS-CoV-2 protease inhibitor
