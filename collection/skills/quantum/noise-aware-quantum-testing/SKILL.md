---
name: noise-aware-quantum-testing
description: "Noise-aware mutation testing methodology for quantum programs under hardware noise. Extends mutation analysis beyond noiseless simulators to realistic noisy quantum hardware. Use when: testing quantum software robustness, evaluating quantum test quality under noise, designing noise-resilient quantum programs, or benchmarking quantum software testing techniques. Based on 'Robust Mutation Analysis of Quantum Programs Under Noise' (arXiv:2605.13279)."
category: quantum
---

# Noise-Aware Quantum Program Testing

## Description

Mutation testing methodology that evaluates quantum program robustness under **realistic hardware noise**. Unlike traditional mutation analysis which assumes noiseless execution, this approach models the interaction between code mutations and quantum noise, revealing whether tests remain effective when programs run on actual NISQ devices.

**Based on**: "Robust Mutation Analysis of Quantum Programs Under Noise" (Fortz, Mendiluze, Ali et al., arXiv:2605.13279v1, 2026-05-13)

## Activation Keywords

- noise-aware quantum testing
- quantum mutation testing under noise
- quantum noise testing
- robust quantum testing
- quantum program testing NISQ
- 量子噪声测试
- quantum hardware noise testing

## Problem Statement

Traditional mutation testing for quantum programs assumes **ideal, noiseless execution**. This creates a dangerous gap:
- A test suite may kill 95% of mutants on a simulator
- But on real hardware with noise, the **same mutants become undetectable**
- Noise masks mutation effects, reducing effective test quality
- Programs that pass tests in simulation may fail on real devices

## Noise Models for Mutation Testing

### 1. Depolarizing Noise
```python
# After each gate, apply depolarizing channel
# With probability p, replace state with maximally mixed state
def depolarizing_noise(state, p):
    return (1-p) * state + p * I / d
```

### 2. Amplitude Damping
```python
# Models energy loss (T1 relaxation)
# Kraus operators:
# K0 = [[1, 0], [0, sqrt(1-gamma)]]
# K1 = [[0, sqrt(gamma)], [0, 0]]
```

### 3. Phase Damping
```python
# Models dephasing (T2 relaxation)
# Kraus operators:
# K0 = [[1, 0], [0, sqrt(1-lambda)]]
# K1 = [[0, 0], [0, sqrt(lambda)]]
```

### 4. Readout Error
```python
# Measurement misclassification
# P(measure 0 | state is 0) = 1 - e0
# P(measure 1 | state is 1) = 1 - e1
```

## Noise-Aware Mutation Testing Workflow

### Step 1: Generate Mutants
Apply standard mutation operators to quantum program:
- Gate replacement (H → X, CNOT → CZ, etc.)
- Gate deletion
- Parameter perturbation
- Gate reordering

### Step 2: Inject Noise
For each mutant and the original program:
- Apply noise model to each gate operation
- Use realistic noise parameters from hardware calibration
- Run both noisy mutant and noisy original

### Step 3: Evaluate Under Noise
Compare output distributions:
```
mutation_effect_noisy = distance(noisy_mutant_output, noisy_original_output)
mutation_effect_clean = distance(clean_mutant_output, clean_original_output)
noise_masking_ratio = mutation_effect_noisy / mutation_effect_clean
```

### Step 4: Classify Results
| Classification | Criteria | Meaning |
|---|---|---|
| **Killed (clean)** | Test detects mutant, no noise | Mutant detectable in simulation |
| **Killed (noisy)** | Test detects mutant, with noise | Test robust to noise |
| **Survived (noise-masked)** | Test detects clean, NOT noisy | **Danger: noise hides defect** |
| **Equivalent** | No difference in either case | Functionally same program |

### Step 5: Compute Metrics
- **Noise-aware mutation score**: % of mutants killed under noise
- **Noise masking rate**: % of clean-killed mutants that survive under noise
- **Robustness gap**: (clean_score - noisy_score) / clean_score

## Implementation Pattern

```python
def noise_aware_mutation_test(original_circuit, mutants, noise_model, test_suite):
    """Run mutation analysis with and without noise."""
    
    results = []
    for mutant in mutants:
        # Clean execution
        clean_orig = run_circuit(original_circuit, noise=None)
        clean_mut = run_circuit(mutant, noise=None)
        clean_detected = test_suite.detects_difference(clean_orig, clean_mut)
        
        # Noisy execution
        noisy_orig = run_circuit(original_circuit, noise=noise_model)
        noisy_mut = run_circuit(mutant, noise=noise_model)
        noisy_detected = test_suite.detects_difference(noisy_orig, noisy_mut)
        
        if clean_detected and noisy_detected:
            classification = "killed_noisy"
        elif clean_detected and not noisy_detected:
            classification = "noise_masked"  # DANGER
        elif not clean_detected:
            classification = "equivalent"
        else:
            classification = "killed_clean_only"
        
        results.append({
            "mutant": mutant,
            "clean_detected": clean_detected,
            "noisy_detected": noisy_detected,
            "classification": classification
        })
    
    return results
```

## Key Findings from Research

1. **Noise significantly reduces mutation scores** - up to 40% of detectable mutants become undetectable under realistic noise
2. **Different noise types have different masking effects** - depolarizing noise masks more than readout error
3. **Circuit depth matters** - deeper circuits suffer more noise masking
4. **Test design matters** - tests using statistical distance are more noise-resilient than exact matching

## Best Practices

1. **Always test under noise models** before deploying to real hardware
2. **Use hardware-specific noise parameters** from calibration data
3. **Design noise-resilient tests** using statistical rather than exact comparisons
4. **Track noise masking rate** as a quality metric alongside mutation score
5. **Increase shot counts** to reduce statistical noise variance
6. **Apply error mitigation** (zero-noise extrapolation, readout mitigation) before testing

## Anti-Patterns

| Anti-Pattern | Risk | Fix |
|---|---|---|
| Exact output matching | Fails under any noise | Use statistical distance (KL, TV, JS) |
| Single-shot evaluation | High variance masks mutations | Use 1000+ shots per evaluation |
| Ignoring crosstalk | Underestimates noise effects | Include crosstalk in noise model |
| No error mitigation | Unnecessarily low scores | Apply readout mitigation + ZNE |

## Related Skills

- qml-mutation-testing (QML-specific, noiseless)
- quantum-program-linting (static analysis)
- quanforge-qnn-testing (QNN testing)
- quantum-system-engineering (broader QE practices)

## References

- Fortz, Mendiluze, Ali et al. "Robust Mutation Analysis of Quantum Programs Under Noise" (arXiv:2605.13279v1, 2026)
- KG entity IDs: check kg.db for related papers on quantum software testing
