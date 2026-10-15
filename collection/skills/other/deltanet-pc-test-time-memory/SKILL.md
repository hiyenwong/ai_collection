---
name: deltanet-pc-test-time-memory
description: Use when building fixed-size test-time memory without BPTT.
category: ai_collection
trigger: predictive coding memory, test-time memorization, linear attention, DeltaNet, recursive least squares fast weights, local learning rules, BPTT-free sequence model
---

# DeltaNet-PC: Test-Time Memory Without BPTT

Source: Morrill & Zemel (Columbia), "DeltaNet-PC: Test-Time Memory Without Backpropagation Through Time" (arXiv:2610.15185, cs.LG, Oct 2026).

## Core Insight

Treat the per-step memory update ΔS_t of a fast-weight memory as a **latent variable** to be inferred (fully settled), not a small gradient step on a slow weight. Taking the negative log-probability of a standard predictive-coding (PC) Gaussian generative model then **derives linear-attention machinery natively** — the resulting write rule is recursive least squares (RLS), and every design choice in the linear attention literature falls out of the energy function.

This gives test-time verbatim sequence memorization that is:
- **Local in space** (Hebbian: only pre/post activity) and **local in time** (no BPTT, no unrolled graph)
- **Fixed-size memory**: two D×D matrices regardless of sequence length L
- **Trained**: encoder/decoder/key-map learn from local signals only

## Derivation Chain (reusable pattern)

1. **Generative model**: p(S) = N(0, I/ε); p(v_t | k_t, S) = N(S k_t, I); keys from previous observation via learned map + RoPE.
2. **Energy = negative log prob**: E(S) = ε/2 ‖S‖²_F + Σ_t 1/2 ‖v_t − S k_t‖²  → ridge regression over all pairs (batch form, unusable online).
3. **Partial energy + Taylor expansion** of E_{t−1} about S_{t−1} with the past summarized in (S_{t−1}, C_{t−1}), C = Σ_{i<t} k_i k_i^⊤:
   E_t(S_{t−1}+Δ) = 1/2‖r_t − Δk_t‖² (new pair) + 1/2 Tr(Δ C_{t−1} Δ^⊤) (stored pairs) + ε/2‖Δ‖²_F (ridge), where r_t = v_t − S_{t−1}k_t.
   → the "interference with stored pairs" term is what outer-product/DeltaNet write rules approximate.
4. **Set ∂E/∂Δ = 0** (full settle, not one gradient step):
   ΔS_t = r_t k_t^⊤ (k_t k_t^⊤ + A_{t−1})^−1,  A = C + εI.
5. **Online RLS form** (no matrix inverse per step):
   - S_t = S_{t−1} + g_t r_t (P_{t−1} k_t)^⊤
   - P_t = P_{t−1} − g_t (P_{t−1}k_t)(P_{t−1}k_t)^⊤,  P_0 = I/ε
   - s_t = k_t^⊤ P_{t−1} k_t,  g_t = 1/(1+s_t)

## Mapping to the Linear-Attention Family

| Linear attention component | PC energy derivation |
|---|---|
| Outer-product write S += v k^⊤ (Katharopoulos) | fit new pair only, ignore interference |
| DeltaNet delta rule (LMS/NLMS) + learned gate β_t | one gradient step on the new-pair term; gate = step size |
| Erase term (S_{t−1} k_t subtracted) | residual r_t = v_t − S_{t−1}k_t |
| Mesa-layer RLS (von Oswald) | exact minimizer of the full energy incl. interference term |
| Write strength schedule | RLS gain g_t computed from the running inverse P — no learning needed |

DeltaNet-PC = the only entry combining: trained keys/values + sequential data + local-in-space-and-time updates + test-time (one-pass, no weight gradients) writes + D² training AND inference memory.

## Architecture

- enc(x): linear, no bias → latent v_t; dec(v): linear + LayerNorm g(·), bias.
- Key map: k_t = R(W_k enc(x_{t−1}), t), R = RoPE with **learned per-band frequencies** — training automatically speeds frequencies when order matters (sequential tasks) and slows them when it does not (key-value binding). Queries = keys (q_t = k_t).
- Multi-episode: context vector c enters the rotary code R(·, t, c); episodes with overlapping segments (e.g., metro lines sharing stops) disambiguate via context.
- Settling (inference): latents k_t, v_t settled with memory S held fixed; gradients accumulated into a running mean; parameters updated once per sequence.
- Value-orthogonality regularizer + activity clipping needed for stability (ablations confirm).

## Empirical Anchors

- **Write-rule comparison** (trained, L=D=256 sequential recall, chance 0.10): outer product 0.66±0.03; delta rule NLMS 0.26±0.01 (worse than untrained-trained gap — interference pathology); RLS **1.00±0.00**. Untrained systems all ≈0.13.
- **Capacity**: perfect recall while L ≤ D (orthogonal-directions count); graceful degradation above; L=D=1024 scales at 100%.
- **Multi-episode**: 100% recall at full memory load (K=8 episodes × ℓ=32, D=256) incl. tree-structured collisions (8→4→2→1 branching); unseen context vectors.
- **Contextual inference by settling**: run memory backwards to hypothesize context, forwards to test — tracks the ideal observer bound (resolves "bank(river) vs bank(money)" from evidence). Settling depth replaces the multi-layer depth feedforward systems need for such inference.
- **MQAR** (512-token, V=8192): 100% test accuracy from **32 training streams** vs DeltaNet's 1,024; training memory **constant 0.25 GB** at any L vs DeltaNet 0.7/55 GB/OOM at L=512/65k/131k. Params 0.20M vs 0.53M; state 131k vs 65k floats (S+P two matrices).
- **Omniglot→MNIST key-value** (unseen character classes): 99.99% at full load L=256, D=256.

## Limitations & Hardware Implications

- Settling is iterative on digital hardware (main PC cost); on analog/neuromorphic substrates, Kirchhoff/Ohm physics settles in parallel instantaneously — positions this rule for in-memory computing.
- RLS update ≡ fully settled ΔS_t, so writes themselves need no iteration; amortized inference (Tschantz et al. 2023) is the forward path for query settling.
- Verbatim recall only (what to store = future work); claims no accuracy advantage over BPTT Transformers — the win is locality + bounded memory + 32× sample efficiency in this regime.

## Reuse Recipes
- **Drop-in fast-weight block**: replace outer-product/delta-rule writes with the two-matrix RLS update (S, P) for any key-value streaming memory; expect large gains when sequences exceed key orthogonality budget or when re-writes collide (NLMS pathology).
- **PC-derived write rules**: any plasticity rule can be read as "how much of the energy do you minimize per step" — full settle ⇒ least-squares/RLS; one step ⇒ LMS; new-pair-only ⇒ outer product. Use this to design or sanity-check new write rules.
- **Bounded-memory online learning**: ridge + running-inverse summary (C or P) is the general trick for making any "disturb stored memories as little as possible" objective online with fixed footprint.
- **Context inference without extra depth**: backward hypothesis + forward test through the same memory beats adding layers for disambiguation tasks.

## Key References
- Schlag et al. 2021 (DeltaNet); Yang et al. 2024b (NLMS normalization); Katharopoulos et al. 2020 (linear attention); von Oswald et al. 2024 (Mesa-RLS); Tang et al. 2023a (tPC — slow-weight memorization, no test-time writes); Yoo & Wood 2022 (BayesPCN — non-sequential); Plackett 1950 (RLS); Whittington & Bogacz 2017 (PC).