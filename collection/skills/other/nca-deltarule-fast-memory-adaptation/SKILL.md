---
name: nca-deltarule-fast-memory-adaptation
description: Use for gradient-free online task adaptation via NCA cellwise fast memory.
category: ai_collection
---

# Online Task Adaptation via Self-Organisation: NCA + Cellwise Delta-Rule Fast Memory

Methodology from arXiv:2609.29281 (Proroković, Sep 2026, independent researcher, Montenegro).
Meta-learned self-organisation where **task adaptation requires zero gradients and zero parameter updates at adaptation time** — only cellwise delta-rule updates to a fast associative memory inside a Neural Cellular Automaton (NCA). Use when designing gradient-free adaptation, meta-learning fast weights, biological-plausibility arguments (no backprop at test), or in-context-learning alternatives with explicit memory.

## Core Separation (slow vs fast)

| | Slow parameters θ (backprop, meta-training only) | Fast memory M (delta rule, adaptation only) |
|---|---|---|
| What | backbone convs, perception filters κ, update MLP W_h/W_Δ, read/write projections W_read/W_write, output W_y | per-cell associative matrix M_ij ∈ R^{Cv×Ck} |
| When updated | meta-training via truncated-window backprop | online during adaptation, one pass over support set |
| Frozen at test? | YES — never touched after meta-training | NO — the ONLY thing that adapts |

Key contrast with MAML-family: MAML meta-learns initial weights adapted **by gradients** at test; this method learns an **adaptation mechanism** (the delta rule's read/write representations) so test-time adaptation is purely local. Key contrast with SRWM (Irie et al.): SRWM lets a weight matrix modify itself with learned write strength; here (1) each of the H×W spatial cells keeps its **own separate memory matrix**, (2) write strength is **error-norm-determined**, not learned (zero error → zero write, guaranteed), (3) batch-parallel memory writes (SRWM is sequential).

## Architecture

1. **Backbone**: 2× stride-2 3×3 convs (3→32→64 ch) reduce 32×32 → 8×8 grid. C_s = C_k = C_v = 32; F = 3 learnable 3×3 perception filters **per channel** (unlike original NCA which shares filters).
2. **Per-cell state + memory**: s_ij(t) ∈ R^Cs recurrent state; M_ij ∈ R^{Cv×Ck} fast memory, both zero-initialised.
3. **Read**: k_ij^read = norm(W_read·s_ij(t)) ∈ R^Ck; readout r_ij = M_ij·k_ij^read.
4. **Recurrent update** (T=16 steps, residual + stochastic firing mask ρ=0.5): Δs_ij = W_Δ·ReLU(W_h·[s_ij, p_ij, r_ij, x_ij] + b_h); s(t+1) = s(t) + ξ(t)⊙Δs(t). Input x_ij is clamped at every step.
5. **Output**: ŷ_ij = W_y·s_ij(T) + b_y; prediction = argmax of spatially averaged softmax.
6. **Cellwise error**: e_ij = softmax(ŷ_ij) − y (optionally label-smoothed target).
7. **Write key**: k^write = norm(W_write·s_ij(T)); **write value**: v_ij = W_v(2)·ReLU(W_v(1)·[s_ij(T), e_ij] + b_v(1)).
8. **Write strength**: η_ij = ‖e_ij‖₂/γ where γ = max possible error norm (analytic: γ≈1.345 for K=5 with label smoothing α=0.1). η ∈ [0,1], η=0 iff e=0.
9. **Delta-rule update** (batch of B′, scaled by meta-training batch size B=128):
   M_ij ← M_ij + (1/B)·Σ_b η·(v − M_ij·k^write)·(k^write)ᵀ
   Each term moves the value retrieved at the write key toward v, gated by error magnitude. B′ ≤ B enforced (larger batches split sequentially).

## Meta-Training Protocol (the load-bearing recipe)

- Tasks: CIFAR-100 superclass partition (FC100 split) — 12 train / 4 val / 4 test superclasses, each task = 5-way fine-grained classification within one superclass (e.g., 5 fish species). Disjoint superclasses ⇒ semantic shift between train and test tasks.
- **Non-episodic**: no support/query split during meta-training. Same labelled stream does double duty — provides meta-loss AND updates memory. First batch of each task is adaptation-only (excluded from loss); each batch is predicted on BEFORE adapting to it (predictions always on unseen-w.r.t.-memory data).
- **Truncated-window backprop**: gradients through windows of L=8 consecutive batches; memory carried forward at window boundary but stopgrad(M). Loss = per-cell cross-entropy applied after EVERY batch (encourages online improvement, not end-of-sequence only).
- Optimisation: AdamW lr=1e-3, wd=0.1, batch 128, label smoothing 0.1, grad-clip L2≤1. Kaiming-uniform init; **W_Δ, W_v(2) zero-initialised** (memory writes start silent).
- Model: 141,793 params (baseline without memory: 121,221).

## Results

| Metric | Value |
|---|---|
| Empty-memory accuracy (meta-test, chance=20%) | 20.0% |
| **After ONE pass over 2500 support images** | **48.2 ±0.3%** |
| Baseline trained from scratch w/ backprop (tens of passes) | 54.4 ±0.2% |
| Gap recovery | ~82% of chance→scratch gap, no gradients, 1 pass |

- Per-task (adapted vs scratch): aquatic mammals 45.2/52.8, insects 59.8/63.9, medium mammals 54.6/64.8, people 33.1/36.2.
- **Batch-size invariance**: support set in batches of 1/16/32/64/128 → 48.3/48.3/48.4/48.1/48.2%. Number of memory writes (2500→20) barely matters — per-example contribution fixed by 1/B scaling.
- **Repeated passes**: L=4/8 peak at pass 2, lose <3pp over 18 more passes. L=2 worse & declining. **L=22 (full backprop, no truncation) worst long-run stability** — falls to 29.4% by pass 20. Truncation is not just a memory-saving hack; it stabilises the learned adaptation rule.
- Generalises across semantic shift: 12 meta-train tasks → held-out mammal/invertebrate superclasses.

## Reusable Patterns

1. **Error-norm-gated writes**: η = ‖e‖/γ gives automatic "write only what you got wrong" — no learned gating needed; analytic normalisation keeps η∈[0,1]. Generalise to regression with bounded targets.
2. **One-stream meta-training**: same online stream provides adaptation signal AND meta-loss; predict-before-adapt ordering eliminates need for held-out support/query split during training. Cheaper than episodic meta-learning.
3. **Truncation-as-regulariser**: stopgrad through memory at window boundaries both bounds backprop memory and yields MORE stable repeated adaptation than full-length backprop.
4. **Per-cell memory parallelism**: spatially distributed memory allows batch-parallel writes with joint application — scale support-set size without changing semantics.
5. **Architecture-agnostic core**: read/write/delta-rule mechanism ports to Universal Transformers, looped Transformers, recurrent GNNs — any shared-parameter iterative refinement.

## Limitations (author-stated + inferred)

- Backprop still used at meta-training time (method is "gradient-free at adaptation", not gradient-free end-to-end).
- Memory starts empty (M=0); learned/generative memory init (cf. developmental priors) left to future work.
- Single domain (CIFAR-100 superclasses), 5-way; no regression/RL/sequence tasks tested.
- ~6pp behind from-scratch backprop baseline; "people" superclass hard for both (32×32 age/sex discrimination).

## vs Related Methods

- **Differentiable plasticity / Backpropamine** (Miconi): learned Hebbian plasticity on weights; here plasticity is prescribed (delta rule) and memory is a separate substrate.
- **Memory-Augmented NNs** (Santoro): external memory + gradient-trained controller; here read/write reps are meta-learned but updates are local & analytic.
- **Fast-weight programmers / linear transformers** (Schlag): fast weights = attention outer-products; here memory is spatially distributed and error-gated.
- **Meta Networks** (Munkhdalai): fast weights generated FROM gradients; here no gradients at test.
- **In-context learning**: conditions on demonstrations implicitly; here task info is explicit, incremental, inspectable memory content.

## Implementation Sketch (PyTorch)

```python
# adaptation step (no grad!)
with torch.no_grad():
    s_final = nca_infer(x, M, T=16)              # recurrent rollout, frozen θ
    e = softmax(cell_out(s_final)) - y_smooth     # [B,H,W,K]
    eta = e.norm(dim=-1, keepdim=True) / gamma    # [B,H,W,1]
    k_w = F.normalize(W_write @ s_final, dim=-1)  # [B,H,W,Ck]
    v = value_mlp(cat([s_final, e], -1))          # [B,H,W,Cv]
    # delta rule, batch-aggregated:
    M = M + (1/B) * sum_over_batch(eta * (v.unsqueeze(-1) - M @ k_w.unsqueeze(-2)) @ k_w.unsqueeze(-1).transpose(-1,-2))
```
