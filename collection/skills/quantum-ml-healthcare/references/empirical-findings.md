# Empirical Findings: Quantum ML in Healthcare

## Key Paper Results

### arXiv:2601.00656 — VQE Protein Simulation
- **Chemical accuracy:** < 1.6 mHartree on 4-orbital serine protease fragment
- **Correlation energy recovery:** 95.3%
- **SARS-CoV-2 protease inhibition:** MAE = 0.25 kcal/mol
- **Cytochrome P450 metabolism:** 85% site prediction accuracy
- **Convergence:** 3 phases — exponential decay (α=0.95), power law (γ=1.21), asymptotic
- **Implementation:** Pure Python VQE, Jordan-Wigner transformation
- **Hardware requirement:** Near-term quantum hardware viable

### arXiv:2505.20804 — QSVM vs QNN on Clinical Datasets
- **Datasets:** Prostate Cancer, Heart Failure, Diabetes (all highly imbalanced)
- **Result:** QSVM > QNN across all datasets
- **Why:** QNNs overfit on small medical datasets; QSVM leverages quantum kernel in higher-dimensional space
- **Key insight:** Quantum models particularly effective when classical models fail on imbalanced data (>10:1 ratio)
- **Published:** IJCNN 2025

### arXiv:2501.06225 — Distributed Hybrid QCNN
- **Circuit splitting:** 8-qubit QCNN → 5-qubit hardware execution
- **Method:** Partition by entanglement depth, execute sub-circuits independently, recombine classically
- **Result:** Superior performance with fewer parameters vs classical baselines on 3 datasets (binary + multiclass)

### arXiv:2604.24597 — Quantum Kernel Advantage on Medical Foundation Models
- **First evidence** of quantum kernel advantage on real medical foundation model embeddings (MIMIC-CXR)
- **QSVM wins 18/18 configurations** vs untuned classical SVM (F1 gain +0.293 at q=11)
- **Critical finding:** Classical kernel collapses to majority-class on 90-100% of seeds; QSVM maintains recall
- **Implication:** Quantum advantage most pronounced on imbalanced clinical data

### Industry Milestone (May 2026)
- **IBM + Cleveland Clinic + RIKEN:** 12,635-atom protein simulation on quantum hardware — largest known biologically meaningful molecule simulated with quantum computers

## Withdrawn Papers to Avoid
- **arXiv:2509.14277** (HQCNN) — Withdrawn due to methodological error in Quantum Attention-Fourier Layer and alignment errors in results/figures

## Benchmark Summary
| Dataset | Best Quantum Model | Classical Baseline | Quantum Advantage |
|---------|-------------------|-------------------|-------------------|
| MIMIC-CXR (imbalanced) | QSVM | SVM | F1 +0.293 (quantum maintains recall when classical collapses) |
| Prostate Cancer | QSVM | Classical ML | QSVM > QNN (QNN overfits) |
| Heart Failure | QSVM | Classical ML | QSVM > QNN |
| Diabetes | QSVM | Classical ML | QSVM > QNN |
| PathMNIST (binary) | HQCNN* | Classical CNN | 99.91% accuracy (*withdrawn) |
| SARS-CoV-2 protease | VQE | Classical DFT | MAE 0.25 kcal/mol at chemical accuracy |
