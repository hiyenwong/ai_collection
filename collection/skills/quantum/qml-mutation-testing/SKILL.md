---
name: qml-mutation-testing
description: "Systematic mutation testing methodology for quantum machine learning models. Use when testing, validating, or assessing robustness of quantum ML models, variational quantum circuits, and QNNs."
category: quantum-ml
---

# QML Mutation Testing

## Description

Systematic mutation testing methodology for quantum machine learning (QML) models. Provides structured approaches for testing correctness and robustness of quantum circuits through controlled mutations.

## When to Use

- Testing quantum machine learning model correctness
- Validating robustness of variational quantum circuits
- Assessing QNN resilience to parameter perturbations
- Building test suites for quantum algorithms

## Mutation Operators for QML

### Gate-Level Mutations
- **Gate replacement**: Replace a gate with a different gate type (e.g., RX to RY)
- **Parameter perturbation**: Modify rotation angles by small amounts
- **Gate deletion**: Remove gates from the circuit
- **Gate insertion**: Add extra gates at random positions
- **Gate order swap**: Change the ordering of consecutive gates

### Circuit-Level Mutations
- **Entanglement modification**: Change CNOT/CZ gate targets or controls
- **Qubit permutation**: Swap qubit assignments in the circuit
- **Depth variation**: Increase or decrease circuit depth
- **Measurement mutation**: Change measurement basis (X, Y, Z)

### Parameter-Level Mutations
- **Initial parameter perturbation**: Modify starting parameters
- **Learning rate mutation**: Change optimization step sizes
- **Regularization mutation**: Add or remove regularization terms

## Testing Workflow

1. Define mutant set: Select mutation operators relevant to the QML model
2. Generate mutants: Apply each mutation to create variant circuits
3. Evaluate mutants: Run each mutant through the same training/evaluation pipeline
4. Compute kill rate: Determine what fraction of mutants are detected (degraded performance)
5. Analyze survivors: Study which mutations the model is insensitive to

## Metrics

- **Mutation score**: Fraction of mutants killed (higher = better test suite)
- **Sensitivity profile**: Which mutation types most affect model performance
- **Robustness index**: Correlation between mutation severity and performance degradation
- **Equivalent mutants**: Mutants that behave identically to original

## Pitfalls

- Quantum noise on real hardware can mask mutation effects - use simulators for clean testing
- Some mutations may produce functionally equivalent circuits
- Mutation size matters: too small and no effect, too large and trivially detected
- Account for quantum measurement stochasticity when comparing mutant outputs

## Related QML Validation Patterns

Mutation testing is one part of a broader QML quality assurance workflow. Complementary patterns:

- **Robustness analysis**: Evaluate QNNs under noise and adversarial perturbations (see `ml-quantum-error-correction` skill, `references/qml-model-validation.md`)
- **Certified training**: Quantum Interval Bound Propagation (IBP) for adversarial robustness guarantees
- **Hardware readiness**: Circuit compilation, error mitigation, deployment checklist for real quantum backends

## References

- Andrews, Mishra. "Efficient Mutation Testing of Quantum Machine Learning Models" (arXiv:2605.00107, 2026)
