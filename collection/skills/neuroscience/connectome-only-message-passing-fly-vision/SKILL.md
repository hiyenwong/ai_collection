---
name: connectome-only-message-passing-fly-vision
description: Connectome-only message-passing model on the fly connectome with anatomical eye front-end; wiring-constrained null ensembles. Use for structure-function, wiring economy, connectome GNN.
category: ai_collection
---

# Connectome-Only Message-Passing Vision on the Drosophila Connectome

Source: "Structure alone supports efficient visual computation in the Drosophila visual system" (Correig-Fraga, Guimerà, Sales-Pardo, arXiv:2610.10023, q-bio.NC, 7 Oct 2026)

## Core Framework

A **connectome-only** model: the anatomical graph (FlyWire FAFB v783, 139,255 neurons, 54.5M synapses) and eye geometry are **fixed**; the only learnable parameters are scalar synaptic gains (bounded by measured synapse counts) and neuronal thresholds. No added hidden units, no task-specific modules. This isolates what measured wiring alone can compute.

### 1. Anatomically faithful eye front-end

- Reconstruct ommatidial layout from retinal neuron 3D coordinates in the connectome: PCA-project R1–R8 terminals to 2D, use R7 positions as seeds for **Voronoi tessellation** → each cell = one ommatidium's angular catchment.
- Per input image: average pixel intensity inside each Voronoi cell → one signal per ommatidium → delivered to all 8 photoreceptors of that ommatidium.
- Spectral channels from measured sensitivities; RGB↔fly-range handled by a 200nm shift (R1–6 broad/white, R7 UV→blue, R8p green, R8y red).
- Output: activation vector over ~8,000 retinal neurons (each photoreceptor is a graph node).

### 2. Message-passing dynamics on the fixed graph

Generic form: x_i^(k) = γ^(k)( ⊕_{j∈N(i)} ϕ^(k)(x_j^(k−1), e_ji) ). With sum aggregation, no state retention (neurons reset each step), linear message:

```
x_i^(k) = γ( Σ_j x_j^(k−1) · e_ji · ω_ji − ξ_i )
```

- e_ji = anatomical synapse count; ω_ji = tanh(θ_ji) learnable gain ∈ [−1,1] → effective weight ≤ observed synapse count (Hebbian-like strength adaptation)
- γ = tanh; ξ_i = learnable threshold (optional)
- N = 3 propagation steps default (robustness 2–6); readout = mean Kenyon-cell (mushroom body) activity → single linear unit
- Plasticity regimes: (i) classifier-only, (ii) edges-only (default), (iii) thresholds-only, (iv) both. Sign-constrained variant: neurotransmitter-annotated ± synapse counts with sigmoid-bounded [0,1] gains.
- Training: cross-entropy, AdamW, lr 3e−4 one-cycle, ≤100 epochs, neuron/Kenyon/cell-type dropout; identical protocol for biological and all randomized graphs.

### 3. Wiring-constrained null ensembles (the causal test)

Wiring cost proxy: L_tot = Σ_{(j,i)} d_ji·s_ji (soma-soma Euclidean distance × synapse count); mean length d̄ = Σd·s/Σs.

| Ensemble | Rewiring rule | What it preserves |
|---|---|---|
| Unconstrained | random targets, fixed out-degree; synapse counts redistributed | node degrees only; L_tot, d̄ ≫ biological |
| Connection-pruned | unconstrained, then remove highest-cost connections until L_tot matches biological | total wiring budget; d̄ still > biological |
| Synapse-bin | group all pairs by soma distance into 100 bins; shuffle synapses within bins | global length distribution ⇒ L_tot and d̄ both preserved |
| Neuron-bin | per neuron, 20 outgoing-length bins; shuffle within bins | per-neuron length histogram + degree; only synaptic weights between connected pairs change (most constrained null) |

## Key Results

- **Multitask vision from structure alone**: color discrimination ≈ 100% trained (92% **untrained**, synapse counts only); shape recognition 64%; numerosity (choose color with more dots, area-controlled) above chance with **Weber-like ratio scaling**: 64% at r=1.5 → 85% at r=5.0, matching behavioral approximate-number-system signatures in real flies.
- **Propagation differences**: unconstrained graphs saturate the whole brain (≈100% neurons incl. Kenyon cells active by step 2); biological + constrained ensembles propagate gradually (~80% in 3 steps), info stays near the eye early. Long-range synapses accelerate spread.
- **Efficiency ordering** (all tasks): unconstrained ≈ connection-pruned > **biological** > synapse-bin > neuron-bin.
  - Under biological wiring constraints (matched L_tot AND length distribution), the **real connectome is the best in class** — an efficient evolutionary operating point, not merely feasible.
  - Unconstrained rewiring can beat biology but only by inflating wiring (energetic + developmental cost) — accuracy/wiring-cost trade-off.
- Takeaway: measured connectivity + eye geometry jointly set **efficient** (not maximal) operating points; precise connectivity is consequential only relative to the constraint set used for nulls.

## Implementation Skeleton

```python
# PyTorch Geometric (the paper's stack: torch + PyG)
# graph: edge_index (directed, presynaptic → postsynaptic), e = synapse counts, positions for d_ji
import torch, torch.nn as nn
from torch_geometric.nn import MessagePassing

class ConnectomeLayer(MessagePassing):
    def __init__(self, n_edges):
        super().__init__(aggr='sum', flow='source_to_target')
        self.theta = nn.Parameter(torch.zeros(n_edges))   # one gain per connection
        self.thr   = nn.Parameter(torch.zeros(1))          # optional per-neuron thresholds
    def forward(self, x, edge_index, e):
        w = torch.tanh(self.theta)                          # gains in (-1,1)
        return self.propagate(edge_index, x=x, e=e, w=w)
    def message(self, x_j, e_ji, w_ji):
        return x_j * e_ji * w_ji                            # activity × synapse count × gain
# x^(k) = tanh(ConnectomeLayer(x^(k-1)) − ξ); repeat N=3; readout: mean over Kenyon-cell mask → Linear(1)
# input: retinal activations from the Voronoi eye model; all non-retinal neurons start at 0
```

Null-model construction: rewire per the four ensembles, keeping (out-degree) fixed; prune by cost d_ji·s_ji until L_tot matches; bin by soma distance (100 global bins / 20 per-neuron bins).

## Reusable Lessons

- **Fix the graph, learn only gains bounded by synapse counts** — the cleanest way to ask "what does structure alone compute?" Connectome-constrained models that add hidden stages/modules cannot answer this.
- **Null ensembles must be constrained at matched wiring cost** — "biological beats random" claims are only meaningful when randomizations preserve the resource budget (L_tot and length distribution); less-constrained nulls SHOULD beat biology, and that's the cost signal, not a failure.
- **Read propagation dynamics before task metrics**: fraction of active neurons per step and mean distance-from-input reveal saturation vs gradual spread, which explains task accuracy differences.
- **Bounded-gain parameterization** (tanh(θ), |ω·e| ≤ synapse count) keeps learning biologically interpretable (Hebbian strength adaptation) and numerically stable.
- **Anatomical input front-end matters**: retinotopic Voronoi sampling + measured spectral sensitivities give the graph a biologically valid input basis; flat pixel→node injection would confound structure vs interface.
- Retinotopic-sector generalization protocol (train left half of visual field, test right half) as the position-invariance check.

## Key References

- FlyWire FAFB v783 proofread connectome + annotations v2.1.0 (Dorkenwald et al.); code: github.com/eudald-seeslab/train-your-fly, /connectome, /cogstim; data on Zenodo (CC BY 4.0)
- Wiring economy: Chklovskii et al.; Sterling & Laughlin — energetic/developmental cost framing for why unconstrained nulls win at a price
- Halberda et al. — approximate number system / Weber-ratio task design; numerical discrimination behaviorally demonstrated in Drosophila
- Contrasts with connectome-constrained models that add task modules (e.g., FlyVision-style pipelines): this framework tests structure ALONE
