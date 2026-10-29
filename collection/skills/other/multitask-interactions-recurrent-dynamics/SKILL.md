---
name: multitask-interactions-recurrent-dynamics
description: Use when multitask RNN transfer or interference matters.
category: ai_collection
trigger: 100-task cognitive battery, hierarchical AL-RNN, task-similarity space, negative transfer prediction, leave-one-out task adaptation, linear region bitcode routing
---

# Multitask Interactions in Recurrent Dynamics across 100 Cognitive Tasks

**Source**: arXiv:2610.33926 — García-Hernández, Hamid, Brenner (ESI Frankfurt / Goethe University, psynamic-lab). Code: github.com/psynamic-lab/multitask_interactions

## Framework: hierarchical AL-RNN as a controlled multitask testbed

Three decoupled axes make task interactions measurable:

1. **AL-RNN dynamics** (almost-linear RNN, Brenner et al. 2024): z_t = A·z_{t−1} + W·Φ*(z_{t−1}) + C·s_t + h, with DIAGONAL A ∈ R^{M×M}, off-diagonal W, and nonlinearity (ReLU) applied ONLY to the last P ≤ M units: Φ*(z) = [z1..z_{M−P}, φ(z_{M−P+1})..φ(z_M)]. P=0 → linear state-space model; P=M → standard piecewise-linear RNN. Binary activation pattern b_t ∈ {0,1}^P ("bitcode") indexes one of 2^P linear regions; within a region dynamics are the linear system z_t = (A + W·D(b_t))·z_{t−1} + C·s_t + h.
2. **Hierarchical task conditioning** (hypernetwork, Brenner et al. 2025): task k gets embedding p^(k) ∈ R^{Nfeat} (Nfeat ≪ dim θ); a LINEAR hypernetwork G maps p^(k) → ALL task-specific recurrent params θ^(k) = {A^(k), W^(k), C^(k), B^(k), h^(k)}. Group parameters receive gradients from every task → structure useful more than once is preferentially represented at group level; per-task freedom confined to Nfeat coordinates. Provides task identity and a forgetting-proof adaptation interface by construction.
3. **Task battery**: K=100 supervised cognitive tasks (working memory, decision-making, perception, attention, timing, reasoning, motor; 66 base identities + 34 compositional variants with delay/sequence-generation/interval-integration modifiers) assembled from Yang et al. 2019, Mod-Cog (Khona et al. 2023), Driscoll et al. 2024 + systems-neuroscience literature. Common masked MSE objective; task solved = ≥80% test accuracy in ≥3 of 5 seeds.

## Core quantitative findings (200 samples/task, matched parameter budgets)

- Hierarchical AL-RNN: 96.5% test acc (94 solved; M=64, P=32, Nfeat=16, 82K params). Individual models: 91.3% (87). Flat joint model: 80.9% (65). Hierarchical LSTM 96.3%, GRU 95.6%, vanilla RNN 93.8% — hierarchy helps every architecture.
- **Joint solvability ≠ sum of individual solvability**: 52/100 tasks are individually linear-solvable, yet the flat LINEAR joint model solves only 14. As jointly-trained individually-linear task sets grow, required nonlinear capacity P grows. Nonlinear capacity is the price of SHARING.
- Capacity demand is surprisingly low: Nfeat=4 → ~95% at sufficient P; P=2 nonlinear units → 89% at sufficient Nfeat (extends Khona 2023: most "cognitive" tasks admit simple recurrent solutions). Exceptions (e.g. HeadDirection integration) genuinely need nonlinear attractor structure.
- Linear solvability predicts learning speed: individually-linear tasks converge ~4–5× faster; per-task convergence times correlate between individual and hierarchical training (Spearman ρ ≈ 0.86). Flat joint model shows task-specific optimization outliers.

## Three task-separation mechanisms — measure all three

1. **Task features** (low-dim hierarchical interface — hierarchical models only)
2. **Linear-region routing**: I(Q;R) = H(R) − H(R|Q), mutual information between task identity Q and active bitcode R. Flat model: ~5.0 bits at P=16 (near the 6.64-bit task-entropy ceiling) — relies on separating tasks into distinct linear regions. Hierarchical: 1.6 bits — offloads separation to task features.
3. **State geometry**: overlap of task-specific first-5-PC subspaces — hierarchical 0.26 vs flat 0.14 (hierarchical shares more geometry); global PC1-5 explained variance 0.43 vs 0.32 (hierarchical more compact).

Flat models must separate via region usage + geometry; hierarchical models share more and separate via features → higher joint performance.

## Task-similarity spaces → transfer prediction

- Pairwise similarities from the three mechanisms (feature cosine, bitcode-distribution overlap, PC-overlap) are reproducible across seeds (r≈0.76–0.78), partially inter-agree (r=0.47–0.70), and feature similarity generalizes moderately across architectures (AL-RNN↔LSTM r=0.53, ↔GRU r=0.57).
- Interpretable structure: (a) shared dynamical objects — HeadDirection, NoiseCleaner+int, PerceptualDM+int cluster in ALL three spaces and reuse a piecewise-linear ring-attractor approximation; (b) compositional variants cluster in feature space (mean cosine distance 0.21±0.02 to variants vs 0.62±0.03 to others, p<.001); (c) pro/anti variants of the same task occupy OPPOSING linear subregions — jointly solving similar tasks with opposing response rules requires nonlinearity.
- **Pairwise transfer** (init target task from other task's trained solution, first 100 epochs): ~70% of source→target pairs improve over random init, but some tasks are systematically NEGATIVE transfer sources. More isolated tasks (mean distance to others) = worse transfer sources: ρ = −0.26 (geometry), −0.23 (region usage).
- **Leave-one-out adaptation**: freeze ALL shared params after training on 99 tasks; adapt ONLY the 16-dim feature vector for the held-out task. Best-source init: 92.1%±0.1 (oracle) ≈ full joint 96.5% > individual full models 91.3%; mean-init: only 84.5%±1.9, failing across all tested learning rates → non-smooth adaptation landscape; initialization from a good source matters. 16 adapted parameters replace ~800 params of an equivalent individual model; pretrained tasks are preserved by construction.
- Source quality ↔ task isolation: ρ = −0.74 (geometry), −0.86 (features), −0.53 (region usage), all p<.001.

## Reuse recipe for multitask recurrent models

1. Prefer HIERARCHICAL (hypernetwork over low-dim task embeddings) over flat joint training AND over per-task models at matched parameter budgets.
2. Use SPARSE nonlinearity (P ≪ M): performance peaks at P=16/234 units in flat models and declines with more — dense nonlinearity is not better.
3. Build the three similarity spaces (features, bitcodes, PCs) as a representation-based task taxonomy; use them to find shared dynamical motifs instead of verbal task categories.
4. Continual-learning protocol: freeze backbone, optimize only the task-feature vector; initialize from the NEAREST source task in feature space (mean init is unreliable).
5. Before using a task as a pretraining source, check its isolation in the learned task spaces — isolated tasks transfer poorly.

## Pitfalls

- Task-similarity spaces depend on architecture and optimization; same task may admit multiple dynamical solutions.
- Conclusions are battery-specific; the field lacks standardized transfer/interference benchmarks (the paper's 100-task suite + pairwise protocol is itself a contribution toward this).
- Mean-feature initialization fails due to non-smooth loss landscape — treat best-source results as an oracle upper bound.
- "Individually linear" classification depends on at least one of 5 seeds solving with a linear individual model.
