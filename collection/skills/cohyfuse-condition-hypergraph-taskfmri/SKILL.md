---
name: cohyfuse-condition-hypergraph-taskfmri
description: Use for task-fMRI prediction with condition-specific hypergraphs. Condition-wise K_q incidence.
category: ai_collection
---

# CoHyFuse: Condition-wise Hypergraph Fusion with Global Connectome in Task-fMRI

**Paper**: "CoHyFuse: Condition-wise Hypergraph Fusion with Global Connectome in Task-fMRI" (arXiv: 2610.05913, Kim, Chung & Jang, Hanyang University / HUFS, Oct 2026)

## What It Solves

Task-fMRI connectome prediction (fluid cognition, age, ADHD subtype) when conventional methods **marginalize away task-state structure**: aggregating all TRs into one static pairwise FC graph obscures condition-specific multi-ROI organization. Two specific failures of prior art:
1. Pairwise graphs restrict message passing to dyadic ROI–ROI edges — no ROI-set aggregation.
2. Condition-agnostic models collapse encoding/distraction/recall phases into one representation, blurring state-resolved signatures.

**Key design principle**: the task condition does not merely add a feature or branch label — it **determines the incidence structure itself**, so the same ROI can join different multi-ROI hyperedges in different task phases.

## Method Pipeline

### Step 1: Condition-wise FC estimation
- ROI time series X ∈ ℝ^(T×V), TR-wise condition labels c_t ∈ {1..Q} from the paradigm timing file (not subject metadata).
- Per condition q: pool time points T_q = {t | c_t = q} across repeated blocks (treat as condition-indexed observations, NOT a continuous series across block boundaries).
- Compute Pearson correlation FC matrix A^(q) over pooled samples; zero diagonal; Fisher z-transform off-diagonal.
- Reliability check (from paper): within-subject split-half edge consistency r≈0.61 > between-condition similarity r≈0.42 → condition FCs are reliable yet distinct.

### Step 2: Condition-specific ROI-centered hypergraph construction (the core novelty)
- Each ROI i is a node, initialized with its **FC profile** r_i^(q) = A^(q)_{i,:} (row of the condition FC matrix).
- Trainable FC-profile encoder: z_i^(q) = φ_θ(r_i^(q)).
- Similarity: negative squared Euclidean distance s_ij^(q) = −‖z_i^(q) − z_j^(q)‖².
- **E = V hyperedges per condition**, one anchored at each ROI (column i of the incidence matrix is anchored at ROI i).
- Weighted incidence matrix (Eq. 3):
  - H^(q)_{j,i} = 1 if j = i (anchor self-membership)
  - H^(q)_{j,i} = K_q · softmax_{j'∈N_{K_q}(i)}(s_{ij'}/τ_q)_j for j in top-K_q neighborhood
  - 0 otherwise
  - τ_q is a **learnable condition-wise temperature**.
- The K_q multiplication keeps total neighbor mass scaling with K_q (prevents per-neighbor weight shrinkage at large K).
- **Per-condition neighborhood size K_q** (not shared K): best FACENAME config was K(ENC,DIST,REC) = (50, 45, 5) — encoding/distraction need wide ROI-set neighborhoods, recall needs tight ones.
- H^(q) recomputed from current embeddings each forward pass; top-K_q index selection is a non-differentiable support (no gradient through indices, gradients flow through the softmax weights).

### Step 3: Condition-wise HGNN encoding
- Hypergraph convolution with symmetric degree normalization (Feng et al. HGNN), shared parameters Θ across conditions:
  X^(q) = σ(D_v^{-1/2} H D_e^{-1} H^T D_v^{-1/2} Z^(q) Θ)
- Attention pooling over ROIs → condition embedding h^(q) ∈ ℝ^D (D=64; MLP produces per-ROI attention logit).

### Step 4: Multi-condition fusion + whole-session branch
- Stack condition embeddings E_c ∈ ℝ^(Q×D) → multi-head self-attention (4 heads) + FFN with residuals → mean pool → h_cond.
- **Complementary whole-session FC branch**: A^(all) from all TRs, vectorized upper triangle, MLP → h_all. Captures stable session-level structure.
- Predict ŷ = g([h_cond; h_all]) with MLP; MSE loss (regression) or cross-entropy (classification).

## Results

| Benchmark | CoHyFuse | Best baseline |
|---|---|---|
| AABC FACENAME FCC prediction (N=1,074) | **7.83±0.10 MAE, R²=0.439** | TA-GAT 8.17 MAE (Δ=0.34, p=0.004) |
| AABC VISMOTOR age prediction | **7.52±0.37 MAE, R²=0.592** | ALTER 7.91 MAE (Δ=0.39, p=0.018) |
| CMI-HBN ADHD 3-class (N=223, ages 6–10) | **72.0% mAUC, 74.2% ACC** | STNAGNN 68.0 mAUC (+4.0 pts) |

- **Ablations** (FACENAME): removing all condition branches is worst (MAE +0.48); removing whole-FC branch +0.37; removing DIST condition is the largest single-condition loss (+0.34).
- **Operator control**: matched GCN/GAT propagation with same inputs underperforms HGNN (8.13/8.07 vs 7.83) → incidence-based ROI-set aggregation itself adds value, not just condition-wise inputs.
- **Distance metric**: Euclidean > correlation > cosine.
- **Confound control**: age/sex/FD-only model R²=0.25 vs 0.439; fold-wise residualized association remains significant (partial r=0.34, p<0.001, 10k permutations).
- **Interpretability**: occlusion ranks hyperedges; DIST hyperedges concentrate in Salience/Ventral Attention Network (SAN) with SAN–FPN and within-SAN motifs; DIST subnetwork strength–FCC association strongest (r=0.36, FDR q≤0.018, survives age/motion adjustment).

## Implementation Notes

- ~0.71M parameters; single RTX A6000; AdamW, batch 64, weight decay 1e-4, grad clip 1.0, dropout 0.2, early stopping, ≤80 epochs; lr ∈ {3e-4, 5e-4, 1e-3}; K_q searched over {5,10,…,50} step 5.
- Schaefer 100-parcel atlas; subject-wise 5-fold CV with 64/16/20 split; all selection on inner validation only.
- Interpretation is hyperedge/subnetwork-level (not individual FC edges); occlusion results = model reliance, not causal biomarker evidence.
- Limitations: needs paradigms with long enough condition windows for stable condition-wise FC; K_q search cost scales with Q.

## Reusable Patterns

1. **Condition-determined incidence**: any time you have segment labels (task conditions, sleep stages, movie scenes), let the segment index determine hypergraph structure per segment, then attention-fuse segment embeddings — instead of one static graph.
2. **FC-profile-neighborhood hyperedges**: define hyperedges as embedding-space top-K neighborhoods of FC-profile rows; anchor self-membership = 1; softmax-weigh the rest with learnable temperature; multiply by K to preserve mass.
3. **Heterogeneous per-condition K_q**: state-specific neighborhood scales beat any shared K; search K_q independently per condition.
4. **Dual dynamic/stable fusion**: pair a state-resolved branch with a whole-session static branch — ablations show both carry complementary signal.
5. **Occlusion-based hyperedge attribution**: rank hyperedges by prediction-error increase when removed; aggregate memberships to Yeo-7 network pairs for neurocognitive reading.

**Activation**: task-fMRI, hypergraph neural network, condition-wise FC, incidence matrix, brain-behavior prediction, ADHD classification, K_q neighborhood, SAN-FPN, brain network
