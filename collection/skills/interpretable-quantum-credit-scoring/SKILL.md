---
name: interpretable-quantum-credit-scoring
description: "Interpretable Quantum Neural Network framework for multiclass credit risk classification with Inter-Class Attribution Alignment (ICAA) metric for quantifying attribution divergence across credit risk categories."
tags: ["quantum", "finance", "credit-scoring", "interpretability", "qml"]
related_skills: ["qml-benchmark-financial-prediction", "quantum-neural-network-designer", "quantum-ml-patterns"]
---

# Interpretable Quantum Credit Scoring

## Description

Framework for building interpretable Quantum Neural Networks for credit risk classification. Combines variational QNN with post-hoc explanation techniques tailored for structured financial data. Introduces the Inter-Class Attribution Alignment (ICAA) metric to quantify how the model distinguishes between credit risk categories. Based on arXiv:2510.15044 (IQNN-CS).

## Activation Keywords

- interpretable quantum credit scoring
- IQNN-CS
- quantum neural network credit risk
- ICAA metric
- 量子可解释信用评分
- quantum explainable finance
- interpretable QML finance

## Tools Used

- terminal: Run quantum circuit simulations
- web_search: Search for related interpretable QML papers
- execute_code: Run IQNN experiments

## Usage Patterns

### Pattern 1: Credit Risk Classification with Interpretability
Build a QNN that not only predicts credit risk classes but provides feature attributions explaining why each class was assigned.

### Pattern 2: Inter-Class Attribution Analysis
Use ICAA metric to understand which features drive the model's decisions differently across risk categories (e.g., low vs. medium vs. high risk).

### Pattern 3: Regulatory-Compliant QML
Deploy QML models in regulated financial environments where model decisions must be explainable to regulators and customers.

## Instructions for Agents

### Step 1: Data Preparation
1. Load structured credit dataset (features: income, debt ratio, payment history, etc.)
2. Encode categorical features using one-hot or ordinal encoding
3. Standardize numerical features (mean=0, std=1)
4. Split data: train/validation/test with stratified sampling

### Step 2: Quantum Feature Encoding
1. Use angle encoding for numerical features (maps feature values to rotation angles)
2. Use basis encoding for binary/categorical features
3. Ensure number of features ≤ number of available qubits
4. Consider feature selection if too many features for current quantum hardware

### Step 3: Variational QNN Architecture
1. Design ansatz with alternating rotation and entanglement layers
2. Use Ry/Rz rotations for single-qubit gates
3. Use CNOT or CZ for entanglement between qubits
4. Measure expectation values as output logits
5. Apply softmax for multiclass classification

### Step 4: Post-Hoc Interpretability
1. Compute feature attributions using gradient-based or perturbation-based methods
2. For each prediction, generate attribution scores for all input features
3. Aggregate attributions across test set for global feature importance

### Step 5: ICAA Computation
1. For each pair of predicted classes (i, j), compute attribution divergence
2. ICAA = mean(|attribution_i - attribution_j|) across all features
3. High ICAA indicates model uses different reasoning for different classes
4. Report ICAA matrix as interpretability diagnostic

### Step 6: Evaluation
1. Predictive performance: accuracy, F1, precision, recall per class
2. Interpretability: ICAA score, feature attribution consistency
3. Training stability: loss convergence, gradient norms
4. Compare with classical baselines (XGBoost, Random Forest, MLP)

## Error Handling

### Too Many Features for Qubits
```
If feature count > available qubits:
  1. Apply feature selection (mutual information, LASSO)
  2. Use dimensionality reduction (PCA) before encoding
  3. Use amplitude encoding (log2(N) qubits for N features)
```

### QNN Training Instability
```
If training loss oscillates or diverges:
  1. Reduce learning rate
  2. Use gradient clipping
  3. Reduce circuit depth
  4. Try parameter initialization from classical pre-training
```

### Low Interpretability Scores
```
If ICAA is near zero across all class pairs:
  1. Model may not be learning class-discriminative features
  2. Check if dataset has sufficient class separation
  3. Try different ansatz architecture
  4. Increase circuit expressivity (more layers)
```

## Key Findings from Paper

- IQNN-CS achieves competitive predictive performance on credit datasets
- Stable training dynamics compared to standard QNN
- ICAA metric reveals how model distinguishes between risk categories
- Post-hoc explanations are tailored for structured financial data
- Path toward transparent and accountable QML for financial decision-making

## Best Practices

1. **Always include interpretability** when deploying QML for credit decisions
2. **Use ICAA as a diagnostic tool** to verify model is reasoning differently per class
3. **Combine multiple explanation methods** (gradient-based + perturbation-based)
4. **Validate attributions** with domain expert knowledge
5. **Report both performance and interpretability metrics** together

## Limitations

- Current implementation on simulators, not real quantum hardware
- Feature count limited by available qubits
- Post-hoc explanations approximate, not exact
- ICAA measures divergence but doesn't guarantee correctness of reasoning

## Resources

- Paper: https://arxiv.org/abs/2510.15044 (arXiv:2510.15044)
- Authors: Abdul Samad Khan, Nouhaila Innan, Aeysha Khalique, Muhammad Shafique
- Published: 2025-10-16 (Accepted for oral presentation at QUEST-IS'25)
- DOI: 10.1007/978-3-032-13855-2_8

## Related Skills

- qml-benchmark-financial-prediction: Benchmark QML vs classical for financial prediction
- quantum-neural-network-designer: Design and optimize QNN architectures
- quantum-ml-patterns: Reusable QML research patterns
- quantum-finance: Quantum computing applications in finance

## Notes

- This skill focuses on **interpretability** — a critical requirement for regulated financial applications
- ICAA is a novel metric specific to this paper; not a standard ML metric
- Credit scoring is high-stakes — model decisions directly impact individuals' access to credit
- Regulatory frameworks (e.g., ECOA, GDPR) require explainable decisions
