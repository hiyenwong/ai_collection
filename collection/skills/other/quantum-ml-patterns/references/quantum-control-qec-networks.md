# Quantum Control & QEC Network Patterns (2026-06-09)

## IA-VQC-DPC: Intervention-Aware Quantum Predictive Control (arXiv: 2606.09778)

### Problem
Hard safety filters downstream of learned controllers guarantee constraint satisfaction but mask policy incompetence — the filter silently repairs bad policies, so post-filter success measures the filter, not the policy.

### Solution: IA-VQC-DPC
**Intervention-Aware Variational Quantum Differentiable Predictive Control**

1. **Primal-dual intervention budget**: Penalizes VQC policy's reliance on CBF (Control Barrier Function) projection during training
2. **Safety attribution protocol**: Decomposes executed trajectory correction into:
   - CBF correction term (how much safety filter intervened)
   - Deployment runtime guard term
   - Guard-off evaluation (stress-test with guards disabled)

### Key Results
- At equal ~400 parameter budget: quantum policy significantly safer and more comfortable than matched classical (p < 10⁻⁴)
- Intervention-aware training lowers raw pre-filter violation and total safety-layer reliance
- **Negative result**: learned differentiable energy head is ONLY safe when paired with distribution-aware runtime guard

### Activation
quantum predictive control, VQC control, safety attribution, intervention-aware training, CBF quantum, control barrier function quantum, safe quantum learning

---

## SCOPE: Syndrome-Driven QEC Network Control Plane (arXiv: 2606.08873)

### Problem
Current quantum network control planes route based on physical link fidelity or topology, not logical error rate. Active tomography for noise characterization is operationally prohibitive.

### Solution: SCOPE
**Syndrome-Driven Control Plane for QEC-Enabled Quantum Networks**

1. **Passive syndrome collection**: Uses QEC cycle data already generated — no active tomography
2. **Noise structure inference**: Syndrome statistics reveal noise bias patterns
3. **Logical error prediction**: Predicts end-to-end logical error rate for candidate routes
4. **Syndrome-aware routing**: Minimizes logical error rate, not physical fidelity

### Key Innovation
Routes based on what actually matters (logical error rate) using data that's already available (syndrome statistics from QEC cycles).

### Activation
quantum network routing, QEC control plane, syndrome-driven routing, logical error rate routing, SCOPE, fault-tolerant quantum network

---

## GNN for Adaptive VQE Operator Selection (arXiv: 2606.08794)

### Problem
ADAPT-VQE iteratively selects operators from a pool using gradient-based criteria. Full-pool gradient evaluation scales linearly with pool size — major bottleneck for large operator sets.

### Solution: GNN-VQE
Reformulates operator selection as a **graph-based decision problem**:
1. GNN policy predicts next entangling operator from interaction graph + state observables
2. Trained on exact simulations of disordered long-range spin chains
3. **Highly effective as shortlist generator**: exact rescoring over few GNN-proposed candidates recovers near-oracle behavior while searching small fraction of pool

### Transferability
Policy trained on spin models transfers to molecular benchmarks (LiH, BeH₂) as shortlist generator.

### Activation
adaptive VQE, operator selection, graph neural network VQE, ADAPT-VQE acceleration, quantum chemistry GNN

---

## Neural Decoder Confidence as Logical Gap Proxy (arXiv: 2606.08758)

### Problem
QEC decoders need soft information (confidence) for post-selection and reliability estimation. MWPM uses complementary/logical gap as confidence measure, but computing it is costly.

### Finding
A GNN decoder trained only on syndromes and logical labels **learns both gap-like discrimination AND a quantitative confidence scale**:
- GNN logit post-selection yields lower logical error rate than MWPM gap post-selection
- Signed GNN confidence distribution resembles signed MWPM gap at low/intermediate values
- GNN assigns higher confidence to many correctly decoded shots that MWPM underestimates

### Implication
Neural decoders can provide confidence-based post-selection when MWPM gap estimates are unavailable, costly, or poorly matched to noise model.

### Activation
neural decoder confidence, logical gap, GNN QEC decoder, post-selection quantum error correction, surface code decoder, soft information QEC
