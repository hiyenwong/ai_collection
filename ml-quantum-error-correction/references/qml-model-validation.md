# QML Model Quality Assurance

Distinct from QEC (error correction at the hardware level). This covers **validation and robustness of trained quantum ML models** themselves.

## Pattern 1: Mutation Testing for QML (2605.00107)

Inject controlled faults into quantum circuits to verify test suite adequacy.

**Mutation operations for quantum circuits:**
- Gate replacement (H → X, RZ(θ) → RZ(θ+δ))
- Gate insertion (add spurious CNOT)
- Gate removal (delete single-qubit gate)
- Parameter perturbation (θ → θ + ε)
- Qubit swap (remap qubit assignment)

**Workflow:**
1. Define mutation operators for target QNN architecture
2. Generate mutated circuits from the original model
3. Run test suite against each mutant
4. Mutation score = (killed mutants) / (total non-equivalent mutants)
5. If score < threshold, augment test suite

**Key insight:** Equivalent mutants (semantically identical to original) must be filtered — use circuit equivalence checking or simulation-based comparison.

## Pattern 2: QNN Accuracy & Robustness Analysis (2604.26110)

Systematic evaluation of VQC-based QNNs under noise and adversarial conditions.

**Evaluation dimensions:**
- Clean accuracy on benchmark datasets
- Robustness to depolarizing noise at varying rates
- Robustness to adversarial parameter perturbations
- Barren plateau susceptibility during training
- Expressibility vs trainability trade-off

**Key finding:** QNNs with deeper circuit depth show higher expressibility but degrade faster under noise. Optimal depth depends on hardware error rates.

## Pattern 3: Quantum Interval Bound Propagation (2605.00747)

Certified training ensuring correct predictions under bounded adversarial perturbations.

**How it works:**
1. Track lower/upper bounds of quantum gate parameters through the circuit
2. Propagate bounds layer-by-layer using quantum-specific bounding rules
3. During training, optimize for worst-case prediction within bounds
4. Result: model certified to predict correct label for all perturbations within bound ε

**Quantum-specific challenge:** Unitary evolution preserves norm but bounds on measurement probabilities require specialized interval arithmetic on the Bloch sphere.

**Comparison with classical IBP:**
| Aspect | Classical IBP | Quantum IBP |
|--------|--------------|-------------|
| Bounds | Linear/ReLU intervals | Bloch sphere intervals |
| Propagation | Matrix multiplication | Unitary + measurement bounds |
| Certification | L∞ norm on inputs | Parameter perturbation radius |

## Pattern 4: QNN Hardware Readiness (2604.24886)

Practical checklist for deploying QNNs on real quantum hardware.

**Key challenges:**
- Circuit depth vs coherence time constraints
- Qubit connectivity topology mismatch
- Gate set limitations (native gates vs compiled gates)
- Shot noise and measurement sampling overhead
- Classical optimization loop latency

**Mitigation strategies:**
- Circuit compilation for target backend topology
- Gate decomposition to native gate set
- Error mitigation: zero-noise extrapolation, probabilistic error cancellation
- Batched evaluation to reduce classical-quantum communication overhead

## When to Use This vs QEC

| Concern | Use QEC Skill | Use QML QA |
|---------|--------------|------------|
| Hardware-level error correction | ✅ | |
| Logical qubit encoding | ✅ | |
| Syndrome decoding | ✅ | |
| Model accuracy testing | | ✅ |
| Adversarial robustness | | ✅ |
| Certified predictions | | ✅ |
| Mutation testing | | ✅ |
| Hardware deployment readiness | | ✅ |
