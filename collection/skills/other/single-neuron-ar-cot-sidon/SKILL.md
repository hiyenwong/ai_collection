---
name: single-neuron-ar-cot-sidon
description: Use when analyzing CoT expressivity. One AR neuron suffices.
category: ai_collection
---

# Single Autoregressive Neuron Simulates Any Circuit via CoT (Sidon Set Encoding)

**Source**: Roey Magen, Nirmit Joshi, Gal Vardi (Weizmann / TTIC Chicago), arXiv:2610.17283 (12 Oct 2026), cs.LG — COLT-line theory paper.

## Central Result

A single **time-invariant autoregressive neuron** — one shared predictor f(x) = σ(⟨w, x⟩ + b), the SAME parameter vector w reused at every generation step — can simulate ANY size-s feedforward σ-circuit (threshold, ReLU, GELU, sigmoid, ...) on n inputs:

- **Dimension** d = O(ns + s²) — matches the worst-case circuit weight count (tight)
- **Generation length** T = O(s²) — tight under the natural "direct edge alignment" restriction (Theorem 4: T = Ω(L²) even for width-1 depth-L circuits)
- **Both bounds INDEPENDENT of circuit depth** — improves Joshi et al. (COLT 2025) whose bounds were O(size^depth), exponential in depth

Threshold activation ⟹ a single AR neuron simulates any polynomial-time Turing machine with poly dimension and generation length (Corollary 1).

## Proof Technique: Serialization via Sidon Sets

The core obstacle: parameter sharing. Assign each non-input circuit node v_i a designated generation step t_i at which the AR neuron emits C_i(x). An edge (v_i → v_j) with weight w(v_i, v_j) is encoded by setting the shared vector coordinate

```
 w[−(t_j − t_i)] = w(v_i, v_j)
```

because C_i(x), emitted at step t_i, appears as the (t_j − t_i)-th most recent context token when computing step t_j — its contribution to the preactivation is exactly w(v_i,v_j)·C_i(x), matching the circuit definition.

**Collision problem**: two distinct edges (i,j) ≠ (k,l) collide iff t_j − t_i = t_l − t_k — the same coordinate of w would have to hold two different weights. **Sidon sets** solve this: S ⊆ ℕ where a+b = c+d ⟹ {a,b} = {c,d}; equivalently ALL positive pairwise differences are distinct. The classical **Erdős–Turán construction** gives a size-s Sidon set with largest element O(s²), so choosing {t_i} from it makes every edge difference unique → T = O(s²) generation steps suffice, collision-free. Input-to-gate weights use distinct sums t_i + t′_q on the initial-position side.

This collision-free serialization — not the neuron — is the novel ingredient enabling depth independence.

## Learnability from CoT Supervision

A complete trajectory (x, f⋆^{CoT-T}(x)) is just T labeled prefix→next-token examples for the SAME shared neuron. So expressivity converts to tractable learning:

- **Threshold**: linear programming finds a w consistent with all observed prefix–next-token pairs in poly time; AR linear-threshold generalization bounds (sample complexity independent of generation length) give **Corollary 2**: a single neuron efficiently learns to predict the output of any poly-time Turing machine from poly(n) complete CoT traces.
- **ReLU**: activation-consistency LP + Bartlett-style pseudodimension bounds give the analogous guarantee for simulating feedforward ReLU networks (Corollary 3).
- **Hardness separation**: WITHOUT intermediate tokens (end-to-end supervision only), learning AR linear thresholds is computationally hard assuming ONLY the existence of one-way functions (Corollary 4) — strictly weaker than prior assumptions. The exponential-depth barrier of earlier reductions is removed by the new simulation.

## Experiment

Student = ONE shared AR ReLU neuron (sparse implementation of w, Adam) trained on 4,000 complete activation traces of a 4-hidden-layer CNN teacher on CIFAR-10 — **no access to teacher weights**:

| Model | Supervision | Test acc | Teacher agreement |
|---|---|---|---|
| CNN teacher | 45,000 images | 72.150% | — |
| Single AR neuron | 4,000 traces | 72.106±0.054% | 99.484±0.070% |

Training: ~5 minutes on one L40S GPU.

## Reusable Insights

1. **CoT supervision quality is architecture-relative**: intermediate steps should expose computations the student CAN represent. Well-structured traces substitute for architectural depth — an extreme formalization of why reasoning distillation works (complex teacher → simple student) and a design rule for teacher trace generation.
2. **Shared-module multiplexing via difference-unique positions**: whenever ONE reusable module must serve many roles across time/positions, assign role-positions from a Sidon set so all pairwise offsets are unique and roles never interfere. Applicable to any time-invariant parameter-shared controller.
3. **Complete-trajectory supervision turns sequence simulation into per-step supervised learning** (prefix→next-token), making LP/convex fitting applicable — trajectory exposure is the difference between tractable and cryptographically hard.
4. **Open questions the paper poses**: can non-edge-aligned simulations beat T = Θ(s²)? Can simple extensions reach T = Θ(s) or o(s)? — good entry points for follow-up theory work.

## When to Use

- Reasoning about the expressivity/learnability of autoregressive models with chain-of-thought
- Designing teacher→student distillation traces (what intermediate computation to expose)
- Any parameter-sharing collision/interference analysis across generation steps
- Understanding why CoT supervision (not just final answers) drives trainability

## Key References

- Malach (2023): CoT power empirics; per-step predictors (non-time-invariant)
- Joshi et al. (COLT 2025): time-invariant formalization, exponential-depth simulation (improved here)
- Erdős & Turán (1941): classical Sidon set construction, max element O(s²)
