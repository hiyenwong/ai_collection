---
name: reasoning-pattern-energy-geometry
description: Use when analyzing human reasoning variability or response stability.
category: ai_collection
---

# Response Variability and Stability in Human Reasoning: Metric-Geometry p-Energy Framework

Source: Bombach, Lakshmanan, Ragni (TU Chemnitz, 2026) "Response Variability and Stability in Human Reasoning" (arXiv:2610.03008). Formalizes individual reasoning patterns as **maps between metric spaces** and measures their internal variability with **p-energy** (generalization of graph/Dirichlet energy to metric-space-valued functions, after Jost 1994).

## Core Framework

Identify a reasoner's response pattern with a function:

    f : (X, d_X) → (Y, d_Y)

- **X** = task space (64 categorical syllogisms: quantifier pair × figure)
- **Y** = response space (9 canonical responses: {A,E,I,O}×{ac,ca} ∪ {NVC})
- Distances between patterns: ℓᵖ-metric d_ℓᵖ(f,g) = (Σ_x d_Y(f(x),g(x))ᵖ)^{1/p}

**Theory-driven 6-bit task encoding** (into Hamming cube H₆, one-to-one):
- Each quantifier q → (u_q, p_q): universality bit (A,E=1; I,O=0) + positivity bit (A,I=1; E,O=0) — directly embeds **atmosphere theory** (Woodworth & Sells 1935)
- Figure r → (t_r, s_r): transitivity bit (figures 1,2 = 1; 3,4 = 0 — a figure-2 syllogism reduces to figure-1 by premise swap) — embeds **TransSet** (Brand 2019); s_r = 1 if term a in first premise
- d_X = pullback of Hamming distance on H₆

**Response encoding** (into H₄):
- NVC → (0,0,0,0) (origin)
- (q, ac) → (u_q, p_q, 1, 0); (q, ca) → (u_q, p_q, 0, 1)
- O-responses lie closest to NVC — embeds PHM **O-heuristic** (reasoners avoid uninformative O-conclusions; Chater & Oaksford 1999)

## Variability Measure: p-Energy

View task space X as a graph (edges = distance-1 pairs in Hamming cube). Local p-energy at task x:

    Eᵖ(f; x) = (1/deg(x)) Σ_{y∼x} d_Y(f(x), f(y))ᵖ

Total energy Eᵖ(f) = Σ_x Eᵖ(f; x); normalized Ẽᵖ = (Eᵖ)^{1/p}.

- **Interpretation**: energy ≈ degree to which f is NOT locally constant = response variability / psychological consistency
- p=2 normalized energy = **Dirichlet energy** (used in Laplacian eigenmaps); special case of p-energy of maps between metric measure spaces (Jost 1994)
- Low energy = systematic/consistent response pattern; high energy = erratic responses relative to psychologically-similar tasks

## Analysis Pipeline (validated on N=100, 64 syllogisms × 2 sessions, 1 week apart; Dames 2022 dataset)

1. **Distance between patterns**: ℓ² metric on test–retest pairs vs cross-participant pairs
2. **k-means clustering** of participant-level feature vectors v̄ᵢ = mean over trials of (response one-hot 4-bit, local Ẽ² at that task), standardized. Elbow + silhouette → k=3 clusters:
   - Cluster 1: 67.2% correctness, LOW energy (0.307) — coherent correct strategy
   - Cluster 2: 37.9%, HIGHEST energy (0.471) — erratic
   - Cluster 3: 30.3%, high energy (0.389), different response-direction preference (ac vs ca loads on PC2)
   - PCA: PC1 (61.6% var) ↔ energy; PC2 (24.7%) ↔ response direction
3. **GLMM (logit link)** predicting retest correctness: C_retest ~ C*V*E² − C:V:E² + C̄ + (C+V|participant) + (C+E²|task)
   - E² has significant effect (β=0.225**, SE=0.076); model comparison vs no-energy model: ΔAIC=39, G²(6)=50.82, p=3.2e−9
   - **Key interaction β_{C:E²} = −0.438***: energy flips sign by initial correctness
   - Effective odds ratios OR(E²): correct→0.72 (high energy hurts retention), incorrect→1.41 (high energy predicts improvement); strongest for incorrect answers on invalid syllogisms
   - Interpretation: correct-but-high-energy = unsystematic luck, less likely retained; incorrect-but-high-energy = unstable state, more likely to improve on retest. "Stably incorrect" reasoners stay incorrect.
4. **Stability test (Q2)**: LMM d_ij ~ 1_{i=j} + (1|i) + (1|j) → within-reasoner test–retest distance smaller than between-reasoner by β = −2.44 (95% CI [−2.69,−2.19]) distance units; first-order stochastic dominance of same-participant ECDF. Reasoning patterns are **individual fingerprints** — stable within reasoners across time. (R²_conditional=0.709, R²_marginal=0.011: effect robust but small vs inter-individual spread)

## Methodological Lessons

- **Encoding matters**: theory-driven 6-bit encoding beats one-hot (ΔAIC = −25 for one-hot; energy main effect becomes non-significant). A coarse encoding can still detect NVC-preference effects (constant patterns lower energy encoding-independently).
- Framework is **domain- and theory-independent** at the math level: any (task metric, response metric) pair induces distance + energy on patterns.
- Natural extensions: probabilistic response distributions (Tessler 2022), belief-bias/content-effect encodings, other reasoning domains (conditional, propositional).

## Reuse Recipe

1. Encode tasks into binary features along **psychologically meaningful axes** (from competing heuristic theories), keep dimension minimal (6 bits for 64 tasks beats 64-dim one-hot)
2. Encode responses similarly; map "null/residual" categories to the origin near their psychological neighbors
3. Compute local 2-energy per (participant, task) — a per-item variability score
4. Aggregate per participant (mean over trials) → cluster → interpret clusters by correctness × energy
5. Feed Ẽ² into mixed-effects models as participant-centered predictor with correctness interactions
6. Test stability with the 1_{i=j} LMM on pattern distances

## Activation Triggers

reasoning pattern analysis, response variability, cognitive consistency metric, syllogism, GLMM cognitive modeling, test-retest stability, metric geometry psychology, Dirichlet energy behavior, individual differences clustering
