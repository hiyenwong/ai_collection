---
name: representation-specialization-latent-susceptibility
category: ai_collection
description: How shared representations specialize under intervention.
---

# Representation Specialization and Latent Susceptibility

**Source**: arXiv 2610.15830 — Takahashi, T. (Doshisha University), "How Shared Representations Become Specialized: Formation, Maintenance, and Latent Susceptibility", Oct 2026.

## Core Framework

When several predictions read from one shared representation, some targets remain more precisely recoverable than others ("representational specialization"). The paper dissociates THREE experimentally separable objects that behavioral/endpoint observation alone confuses:

1. **Formation** — which conditions created the bias
2. **Present support** — which conditions currently sustain it
3. **Latent susceptibility** — how readily an endpoint-matched learner responds to new learning

Key insight: a condition that created a bias need not be the condition keeping it in place, and learners matched on selected endpoint measurements can respond very differently to the same subsequent intervention.

## Experimental System (replicable minimal design)

- Two 3-dim Gaussian targets A, B with correlation ρ=0.35 (B = ρA + √(1−ρ²)ε), mixed by seed-specific random orthogonal transform.
- Encoder: hidden width 32 → **2-dim bottleneck** (tanh) → shared code → two separate LINEAR readout heads reconstruct A and B against noise-free signals.
- **Acquisition precision** = noise σ on target-specific input (high 0.05 / low 1.20; formed-state experiments use 0.15), inputs variance-normalized so precision ≠ scale. **Update allocation** = loss weights L_t = w_A ℓ_A + w_B ℓ_B, w_A + w_B = 1.
- **Allocation index**: s = (D_B − D_A)/(D_A + D_B), measured by freezing encoder, fitting FRESH linear readouts on unused probe data, evaluating on separate held-out data with common high-precision inputs. D = variance-normalized MSE.
- Evidence discipline: 40 confirmatory seeds (pilot seeds set levels), 95% seed-level bootstrap intervals, **pre-specified equivalence margins** (±0.02 etc.), mirrored target labels averaged within seed. Pre-registration-style: time-stamped frozen analysis plans + archived raw CSVs.

## Result 1: Acquisition precision selects specialization under EQUAL loss weights

- 9-condition factorial (3 acquisition × 3 update weights) after 100 balanced init updates, 500 formation updates:
  - A-precise acquisition with equal weights: s = +0.3385; B-precise: s = −0.3338. Paired contrast 0.672 [0.666, 0.679] (> pre-specified 0.30 criterion), **40/40 seeds** favor the precisely-acquired target.
- Acquisition and updating are COMPETING controls: aligned strengthens, conflict weakens; strong opposing update weight can overcome acquisition advantage. No universal "acquisition sets speed, updating sets direction" rule.
- **Redirection of already-formed states**: acquisition flips an update-formed specialization in 40/40 seeds within 1,000 updates (terminal contrast 0.716 ≈ neutral-start 0.709); first zero crossings ~17 updates but trajectories non-monotonic.

## Result 2: Formation history ≠ current support

- Symmetrizing both controls AFTER formation: |s| decays 0.41 → 0.04 over 400 updates (joint removal; decaying at window end).
- Linear-bottleneck cross: releasing a 1-dim/one-target constraint reduces |s| 0.971 → 0.130 (above never-constrained 0.059) — residual formation effects without original magnitude.
- **State-following feedback sustains long-lived regimes**: rule that updates the BETTER-represented target amplifies incidental differences — terminal |s| 0.868 vs 0.421 under fixed-propensity control. Feedback result is amplification/support, not sign-selection.
- Metastable regimes (operational term for finite-time residence/recovery/switching/coexistence): 2-dim bottleneck shows two coexisting regimes over 8,000 updates (16,000-update stability check); weak opposing pulses recover, strong pulses switch regimes. NOT proven permanent bistability.

## Result 3: Latent susceptibility (the headline finding)

**Setup**: Two formation routes — acquisition-formed (precise observation of favored target, equal loss weights) vs update-formed (balanced observation, 0.80 loss weight on favored target) — calibrated to match FIVE endpoint measures: aligned s (diff −0.0064, within ±0.02), target error, non-target error, total error, low-precision s. 200-update neutral continuation also equivalent.

**Same 10-update opposing pulse, different responses**:
- Combined pulse (precise acquisition of weaker target + weight 0.85): acquisition-formed loses MORE specialization than update-formed — difference 0.1951 [0.188, 0.202]. Crossing-zero rate: **67.5% vs 0%**.
- All three pulse types (acquisition-only 0.167, update-only 0.151, combined 0.195) show the same route asymmetry with INHERITED Adam state.

**Optimizer-state interventions identify Adam's second moment v as causal**:
- **Reset Adam** (keep weights): difference collapses 0.195 → 0.0103 — within ±0.02 equivalence margin.
- **Exchange first moment m** between route endpoints: no substantial change (inside equivalence margin).
- **Exchange second moment v**: REVERSES which route is more susceptible (+0.197 → −0.127).
- Decomposition (40 new seeds, prospective): equalize mean inverse-scaling āv (keep each route's v pattern): 0.191 → 0.088. Replace v by scalar: → 0.125. BOTH: → 0.040. Swap other route's v pattern + equalize āv: reverses to −0.011. → Mean adaptive scale explains PART; the **coordinate-wise pattern of v also causally modifies response**.
- Mediator candidate: first-10-updates cumulative **parameter-path length** ratio 1.872 (vs gradient-norm ratio 0.987); path-length difference correlates 0.806 with response difference; leave-one-seed-out path-length regression cuts squared error 62% vs mean-only. Path length = strong mediator candidate, NOT identified mediation.

**Timing shifts with optimizer condition**:
- Inherited Adam: large difference at updates 10–20 (0.181–0.213).
- Fresh Adam: 0.0096 at update 10 but 0.0274 at 50; calibrated SGD: 0.0123 → 0.0433 at 50, 0.031 at 100.
- ALL conditions converge by update 500: endpoint difference −0.00045 [−0.0015, 0.0006]. Inherited−fresh contrast even flips sign at 50–100 updates (−0.007).
- → Optimizer state shifts WHEN route differences appear, not whether history ever matters.

**Within-route control (rules out "route label" as the mechanism)**: constant 0.80 loss weight vs variable (1.00/0.60 alternating, same mean, same acquisition/batches/count). Endpoints equivalent, but constant schedule retains SMALLER total second moment (0.82× variable) and moves FURTHER under pulse (+0.032); v swap reverses (−0.014); reset → 0.005. → Realized weight-sequence variability, jointly with order, changes latent susceptibility even with identical mean loss weights.

**Negative control on predictive coordinates**: slow task-framing variable κ predicted regime switching only when perturbation strengths POOLED (AUC 0.712); within fixed levels it failed (ΔAUC 0.0049, slightly worse log loss). → A candidate slow variable must predict BEYOND the intervention that produced it; correlating with history ≠ sufficient dynamical state.

## Result 4: Three-target extension

Three symmetric 3-dim targets (pairwise ρ=0.35, mixed into 9 inputs), bottleneck 2 or 3, update weights 1/3 each, centered log-error scores q_i (Σq_i=0). Designated-target precise acquisition wins in **40/40 seeds at both capacities** (gain 0.37 at 2-dim; 0.90–0.92 at 3-dim). Effects NON-collinear: second singular value 0.55 (2-dim) / 1.37 (3-dim), intervals exclude zero; near-unit σ2/σ1 ratios verify label symmetry. Precise acquisition INCREASES total reconstruction error vs balanced — **redistribution of readable information, not uniform improvement**.

## Reusable Intervention Map

| Question | Intervention | Result |
|---|---|---|
| What is learned? | Vary acquisition (fix loss weights) / vary loss weights (fix acquisition) | Both select specialization; competing controls |
| What sustains it? | Remove constraints; symmetrize controls; retain/break state tracking | Formed bias decays; state-following feedback maintains regimes |
| What remains hidden? | Match endpoints, common pulse; reset Adam; exchange m/v | Matched specialization ≠ matched response; v causally modifies and reverses short-pulse susceptibility |
| When does it appear? | Extend common intervention under inherited/fresh Adam, SGD | Optimizer shifts the timing; long common training converges endpoints |
| Does formation generalize? | Add symmetric third target | Acquisition-selected formation spans two observable contrasts |

## Practical Recipes

1. **Distinguish formation from support**: clone a checkpoint; symmetrize all biasing conditions; measure decay of |s| over a fixed window. Residual = formation trace; ongoing bias = current support.
2. **Detect latent susceptibility**: match learners on ≥5 endpoint measures within pre-specified margins, then apply one common brief pulse; reset/exchange optimizer components with weights fixed. Large response differences that collapse under reset = optimizer-state-carried; differences that persist or emerge later (updates 50–100) = model-side history.
3. **Measure functional accessibility, not geometry**: fresh-probe linear readouts on held-out common inputs; CKA alone (0.927 here) does NOT imply matched dynamics.
4. **For multi-target (>2) allocation**: use centered log-error scores (q_i, Σq_i=0) and check whether intervention effects are collinear (SVD); non-collinear effects mean a single comparison axis is insufficient.
5. **Equivalence testing discipline**: pre-specify margins BEFORE the pulse; report seed-level bootstrap intervals; use pilot/confirmatory seed separation; average mirrored labels within seed.

## Caveats
- Minimal Gaussian/tanh systems, 500–600 formation updates, longest redirection 1,000; no asymptotic attractor claims. 8,000-update coexistence is operational metastability only.
- Strongest optimizer evidence is the 10-update pulse in the two-target network; endpoint equivalence ≠ complete network identity (CKA 0.927, parameters differ).
- v exchange interpretable only because both recipients share the common ancestor's parameter coordinates.
- The constant-vs-variable control confounds weight variability with order (not separately manipulated).
- Three-target: transitions and optimizer exchange untested.

## Activation
representational specialization, shared representation, gradient starvation, modality competition, acquisition precision, update allocation, loss weighting, latent susceptibility, endpoint matching, equivalence testing, Adam second moment, optimizer state, state-following feedback, metastable regimes, critical periods, training memory, multi-task interference, continual learning plasticity, allocation index, linear readout probes
