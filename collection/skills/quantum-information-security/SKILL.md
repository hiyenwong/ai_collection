---
name: quantum-information-security
description: >
  Security patterns for quantum computing systems: covert quantum computation,
  side-channel analysis, crosstalk detection, failure-guided fuzzing for HQC
  programs, self-testing protocols, and quantum resource verification.
  Use when designing secure quantum cloud platforms, testing quantum programs,
  or implementing device-independent certification.
  Trigger: quantum security, covert quantum computing, crosstalk, quantum side channel,
  quantum fuzzing, HQC testing, self-testing quantum, quantum resource distillation.
---

# Quantum Information Security Patterns

Reusable security patterns from recent quantum computing research papers.

## Pattern 1: Covert Quantum Computing

Protect quantum computations from adversaries sharing the same quantum processing unit (QPU) in multi-tenant cloud platforms.

### Core Concept
Covert quantum computing ensures an adversary with access to all other QCUs cannot detect computation on the subset they cannot access. Analogous to covert communication but with a richer framework since the adversary controls systems used for detection.

### Isoperimetric Analysis
- For n-qubit planar graph circuit layouts with nearest-neighbor crosstalk assumption:
  - Only **O(√n) border qubits** provide detection information to the adversary
  - Derive discrete isoperimetric inequalities to bound information leakage
  - The scaling law holds on real hardware (IBM Heron 2, IQM Emerald)

### Real-World Findings
- Long-range coupling effects **beyond border qubits** create side channels
- Long-range crosstalk is induced by **leakage from drive and control lines**
- This weakens covertness assumptions and exposes co-tenants to unintended crosstalk

### Implementation Checklist
- [ ] Characterize actual crosstalk topology on target QPU
- [ ] Model adversary capabilities (quantum memory + adaptive operations)
- [ ] Use quantum-strategy framework for covertness analysis
- [ ] Design spatial isolation strategies beyond nearest-neighbor assumptions

## Pattern 2: Failure-Guided Fuzzing for HQC Programs

Testing methodology for hybrid quantum-classical algorithms (VQE, QAOA).

### Core Strategy
Two-phase fuzzing approach:
1. **Phase 1**: Search for non-convergent seeds (failure-inducing configurations)
2. **Phase 2**: Locally fuzz circuit parameters around discovered failure seeds

### Five Budgeted Strategies
| Strategy | Description | Effectiveness |
|----------|-------------|---------------|
| Random hybrid testing | Random optimizer + circuit params | Baseline |
| Classical enumeration | Enumerate classical params, no fuzzing | Moderate |
| Random-seed local fuzzing | Fuzz around random seeds | Better |
| Enumeration-seed local fuzzing | Fuzz around enumerated non-convergent seeds | Good |
| Concolic-seed local fuzzing | Fuzz around symbolically discovered seeds | Best for VQE |

### Key Findings
- **Failure-guided local fuzzing** is the main driver of improvement over random testing
- **Concolic seed discovery** provides additional benefits on VQE
- Concolic approach is **less stable on QAOA** - value is workload-dependent

### Implementation Checklist
- [ ] Model hybrid input as (optimizer hyperparams, circuit params) pair
- [ ] Define convergence criteria and failure detection thresholds
- [ ] Implement two-phase search: seed discovery → local fuzzing
- [ ] Compare against random baseline within same execution budget
- [ ] Choose strategy based on workload type (VQE vs QAOA)

## Pattern 3: Scalable Self-Testing of Quantum States

Device-independent certification of quantum states from measurement statistics alone.

### Problem
Characterizing large quantum systems with minimal assumptions. Traditional self-testing requires exponentially many samples in system size.

### Solution
- Protocol robustly self-tests almost all **n-qubit states with polynomial sample complexity**
- Key: Efficient device-independent evaluation of multipartite Pauli measurements
- Requires only **linear number of ancillary Bell pairs** + standard projective/Bell measurements
- Well within reach of current quantum technology

### Applications
- Large-scale quantum network certification
- Device-independent quantum information processing
- Learning and certification protocols in multi-party quantum settings

## Pattern 4: Universal Quantum Resource Distillation

Distillation of quantum resources (e.g., entanglement) without knowledge of the input state.

### Key Result
- Distillation can be performed **universally**: optimal rates achieved with no knowledge of input state
- Relies on **generalized quantum Stein's lemma** extended to composite hypothesis testing
- Null hypothesis composed of i.i.d. copies of an **unknown state** (not fixed)
- Optimal rates governed by **regularized relative entropy** of the resource

### Practical Implications
- Robust against state preparation errors
- No need for precise state characterization before distillation
- Applicable to purification of entanglement under non-entangling maps

## Pattern 5: Quantum Side-Channel Detection

Systematic approach to detecting and characterizing side channels in quantum processors.

### Detection Methodology
1. **Ramsey experiments**: Measure idle qubits to detect unintended couplings
2. **Spatial analysis**: Map crosstalk beyond nearest-neighbor pairs
3. **Control line leakage**: Characterize drive/control line induced coupling
4. **Adversarial modeling**: Quantify what information an adversary can extract

### Mitigation Strategies
- Spatial isolation of sensitive computations
- Crosstalk characterization and compensation
- Temporal scheduling to minimize simultaneous activation of coupled qubits
- Drive line filtering and calibration

## Verification Steps

When implementing quantum security patterns:
1. Verify crosstalk characterization on actual hardware (not just simulation)
2. Test covertness against adaptive adversaries with quantum memory
3. Compare fuzzing strategies within equal execution budgets
4. Validate self-testing protocol polynomial scaling empirically
5. Check resource distillation rates against theoretical bounds

## Resources

- arXiv:2605.14325 - "Toward Covert Quantum Computing" (Anderson et al., 2026)
- arXiv:2605.14219 - "Failure-Guided Fuzzing for Hybrid Quantum-Classical Programs" (Zhang, 2026)
- arXiv:2605.15106 - "Scalable self-testing of generic multipartite quantum states" (Liu et al., 2026)
- arXiv:2605.15174 - "Universal quantum resource distillation via composite generalised quantum Stein's lemma" (Lami et al., 2026)

## KG Entity References

- Entity 1187: Toward Covert Quantum Computing (kg.db)
- Entity 1188: Failure-Guided Fuzzing for Hybrid Quantum-Classical Programs (kg.db)
- Entity 1181: Blind Quantum Computation on a Modular Superconducting Processor (kg.db)
- Entity 1182: QLAM: A Quantum Long-Attention Memory Approach to Long-Sequence Token Modeling (kg.db)