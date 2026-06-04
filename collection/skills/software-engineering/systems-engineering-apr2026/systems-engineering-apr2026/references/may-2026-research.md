# May 2026 Systems Engineering Research — Session Detail

Discovered 2026-05-26 via arXiv cs.SY (45 new submissions), model-based SE search (103 results), and control theory search.

## Paper 1: Convex Hybrid Modeling — An Operator-Based Approach

- **arXiv**: 2605.23151 | **Submitted**: 2026-05-22
- **Author**: Wentao Tang (eess.SY, stat.ML)
- **Url**: https://arxiv.org/abs/2605.23151
- **Skill**: `convex-hybrid-modeling`

### Three Settings

| Setting | Formulation | Use Case |
|---------|------------|----------|
| (1) Reference model regularization | min loss + lambda * ||model - ref||^2 | Refine first-principles model with data |
| (2) Interpretable subspace restriction | model in span{phi_1,...,phi_k} | Known functional form, unknown coefficients |
| (3) Kernel-based mixture manifold | Lifted canonical features via operator theory | Nonlinear dynamics, local interpretable models |

### Key Implementation Pattern

Setting 3: kernel-based mixture of interpretable models
model(x) = sum_i w_i * k(x, x_i) * g_local(x; theta_i)
where k = kernel, g_local = local interpretable model, w = learned weights

RKHS formulation ensures convexity. Kernel trick makes infinite-dimensional lifted features tractable. Nystrom approximation scales to large datasets.

### Related Techniques
- Koopman operator theory (DMD/KMD for linear representations)
- Gaussian processes (related via kernel formulation)
- SINDy (sparse identification for interpretable dynamics)
- PINNs (neural approach with physics constraints)

---

## Paper 2: SHIA — SysML-Hardware Interface Architecture

- **arXiv**: 2605.11248 | **Submitted**: 2026-05-11
- **Authors**: Charles Lewis, Amal Elsokary, Siyuan Ji (cs.SE, eess.SY)
- **Url**: https://arxiv.org/abs/2605.11248
- **Skill**: shia-sysml-hardware-interface (already exists)

### Architecture
SysML Server (IBM Rhapsody C++) --Socket-- Hardware Server (Raspberry Pi)

### Verification Stages
1. Model Only Mode (MOM) -- SysML server standalone
2. Hardware server in isolation
3. Bidirectional integration + Karnaugh map comparison

### Key Result
Zero discrepancy between SysML-generated and hardware-generated outputs.

---

## Paper 3: Sheaves for Consistency in MBSE

- **arXiv**: 2605.08609 | **Submitted**: 2026-05-09
- **Author**: Josh Gibson (cs.LO, math.CT)
- **Url**: https://arxiv.org/abs/2605.08609
- **Skill**: sheaf-consistency-mbse (already exists)

### Key Theorem
Design presheaf F on architectural site X is a sheaf iff F satisfies pairwise intersection compatibility.

### Consequences
- Pairwise interface checks certify global consistency
- Compatible local designs yield unique global design
- Limit-preserving functors inherit consistency
- Machine-verified in Lean 4 / Mathlib

---

## Other Notable Papers (cs.SY, May 25 New Submissions)

| arXiv ID | Title | Area |
|----------|-------|------|
| 2605.23042 | Open-Source METANET Calibration for Freeway Traffic | Traffic systems engineering |
| 2605.23864 | Distributed Optimization via Individual Motivation | Multi-agent distributed optimization |
| 2605.23813 | Minimum Effort Control Using Variational Methods | Optimal control |
| 2605.23030 | Impedance-based Stability Margin for Offshore Wind | Power systems control |
| 2605.16144 | MAxLM: Multi-Agent Language Model Scheduling | AI-assisted wireless systems engineering |
| 2605.23129 | Deception and Counter Deception in Adversarial Graph Traversal | Game-theoretic control |
