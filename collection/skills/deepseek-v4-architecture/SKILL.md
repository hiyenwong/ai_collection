---
name: deepseek-v4-architecture
version: 1.0.0
description: DeepSeek-V4 series architecture and training methodology — hybrid CSA/HCA attention, mHC residual connections, Muon optimizer, On-Policy Distillation, and infrastructure innovations for million-token context.
trigger_words:
  - deepseek-v4
  - deepseek v4
  - hybrid attention
  - compressed sparse attention
  - heavily compressed attention
  - CSA HCA
  - manifold-constrained hyper-connection
  - mHC
  - muon optimizer
  - on-policy distillation
  - OPD
  - million-token context
  - mega-kernel MoE
  - TileLang
  - FP4 quantization training
  - DSec sandbox
---

# DeepSeek-V4 Architecture & Training Methodology

**Source**: "DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence" (arXiv 2026)
**Models**: V4-Flash (13B/284B MoE), V4-Pro (49B/1.6T MoE)

## 1. Hybrid Attention Architecture

### CSA (Compressed Sparse Attention) — for short/medium context
- **Lightning Indexer**: Lightweight attention scores compressed KV entries; selects top-k blocks (FP4 precision)
- Equations 13-19: Query projection → score KV entries → softmax → top-k selection
- **Shared KV MQA**: Single shared key-value head across all query heads (eq 18-19)
- **Grouped Output Projection**: Split nh heads into g groups; per-group down-projection reduces output dimension
- KV cache: BF16 for RoPE dims + FP8 for rest

### HCA (Heavily Compressed Attention) — for long context
- More aggressive compression: m' (≫m) tokens → 1 KV entry
- Sliding window KV (nwin recent uncompressed tokens) preserves local dependencies
- Same shared KV MQA + grouped output as CSA

### Supporting Techniques
- **Partial RoPE**: Applied to last 64 dims only; inverse RoPE on attention output carries relative position
- **Attention Sink**: Learnable sink logits allow total attention < 1 (eq 27)
- **RMSNorm** on queries and KV entries before core attention (prevents logit explosion)
- **KV cache**: ~2% of GQA8 baseline at 1M context

## 2. Manifold-Constrained Hyper-Connections (mHC)

### Problem
Standard Hyper-Connections (HC) suffer numerical instability when stacking many layers.

### Solution
- Constrain residual mapping Bₗ to **doubly stochastic matrix manifold** (Birkhoff polytope)
- M = {M ∈ Rⁿˣⁿ | M1=1, 1ᵀM=1ᵀ, M≥0}
- Guarantees ∥Bₗ∥₂ ≤ 1 (non-expansive) → training stability
- Closed under multiplication → stable deep stacking
- Sinkhorn-Knopp algorithm (20 iterations) for projection
- Input/output mappings: Sigmoid constraint for non-negativity

### Dynamic Parameterization
- Static (input-independent) + Dynamic (input-dependent) components
- Learnable gating factors initialized to small values
- nₕc × d projection matrices (nₕc ≪ d, e.g. nₕc=2)

## 3. Muon Optimizer

### Usage
- **Muon** for: attention, MoE, mHC linear layers
- **AdamW** for: embedding, prediction head, RMSNorm, mHC static biases/gating

### Algorithm (Algorithm 1)
1. Compute gradient Gₜ
2. Accumulate momentum: Mₜ = μMₜ₋₁ + Gₜ
3. Hybrid Newton-Schulz: orthogonalize (μMₜ + Gₜ) — Nesterov trick
4. Rescale update RMS: Oₜ = Oₜ' · √max(n,m) · γ
5. Weight decay + update: Wₜ = Wₜ₋₁(1-ηλ) - ηOₜ

### Hybrid Newton-Schulz (10 iterations, 2 stages)
- Stage 1 (8 steps): (a,b,c) = (3.4445, -4.7750, 2.0315) — rapid convergence
- Stage 2 (2 steps): (a,b,c) = (2, -1.5, 0.5) — stabilize singular values at 1

### Key: QK-Clip NOT needed
mHC + attention RMSNorm already prevent logit explosion.

## 4. Infrastructure

### Expert Parallelism (EP) Communication Overlap
- Wave-based fine-grained scheduling: experts split into waves
- Dispatch(wave N+1) ‖ Compute(wave N) ‖ Combine(wave N-1)
- 1.50-1.96× speedup; open-sourced as MegaMoE (DeepGEMM)
- Hardware insight: C/B ≤ 2d = 6144 FLOPs/Byte suffices (bandwidth ceiling)

### TileLang DSL
- Host Codegen: moves Python host logic to generated code (<1μs overhead)
- Z3 SMT solver for formal integer analysis (QF_NIA)
- fast-math OFF by default; IEEE-754 bitwise reproducibility support

### FP4 Quantization (MXFP4)
- Inference: native FP4 weights
- Training: lossless FP4→FP8 dequantization, reuse FP8 mixed-precision framework
- Applied to rollouts and inference-only forward passes

## 5. Post-Training

### On-Policy Distillation (OPD)
- Replaces mixed RL; multi-teacher distillation
- **Full-vocabulary** logit distillation (not token-level KL) — more stable
- L_OPD = Σ wᵢ · D_KL(π_θ ‖ π_Eᵢ) (reverse KL)
- 10+ domain experts → single student
- Teacher hidden states cached; prediction heads loaded on demand per mini-batch

### Three Reasoning Modes
| Mode | Context | Use Case |
|------|---------|----------|
| Non-think | 8K | Fast intuitive responses |
| Think High | 128K | Conscious logical analysis |
| Think Max | 384K | Maximum reasoning effort |

### Quick Instruction
- Special tokens appended to input for auxiliary tasks (search trigger, title gen, domain classify)
- Reuses pre-computed KV cache → reduces TTFT

### DSec Sandbox Platform
- 4 substrates: Function Call / Container / microVM / fullVM
- EROFS + 3FS for fast image loading
- Token-granular WAL for preemptible/fault-tolerant rollout
- Hundreds of thousands concurrent instances

### Interleaved Thinking
- Tool scenarios: full reasoning history preserved across user turns
- Non-tool scenarios: reasoning discarded on new user turn (concise context)

## 6. Key Performance (V4-Pro-Max)

| Benchmark | Score |
|-----------|-------|
| MMLU-Pro | 87.5 |
| GPQA Diamond | 90.1 |
| Codeforces Rating | 3052 |
| HMMT 2026 Feb | 95.2 |
| MRCR 1M (MMR) | 83.5 |
| SWE Verified | 80.6% |
| Putnam-2025 (formal) | 120/120 |

## 7. Lessons for Architecture Design

1. **Hybrid attention** is the key to million-token efficiency — compress aggressively for long range, keep local window
2. **Manifold constraints** (Birkhoff polytope) are a principled way to ensure deep network stability
3. **Muon + hybrid Newton-Schulz** converges faster than Adam for most modules
4. **Full-vocabulary OPD** > token-level KL for stable multi-teacher distillation
5. **Wave-based EP scheduling** hides all communication under computation when C/B threshold met
6. **FP4 for inference + FP4→FP8 for training** is a clean mixed-precision strategy
7. Conservative architecture choices (many validated tricks) may be necessary for stability at scale, even if complex

## Activation Keywords

- "deepseek-v4-architecture"
- "deepseek v4 architecture"
- "use deepseek v4 architecture"
- "deepseek v4 architecture help"
- "deepseek v4 architecture analysis"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify the user's specific question or task related to Deepseek V4 Architecture
2. Gather relevant context from files or user input
3. Apply Deepseek V4 Architecture methodology to address the request
4. Provide clear results with actionable insights

## Examples

### Basic usage
```
User: "Help me with deepseek v4 architecture"
→ Understand requirements → Apply methodology → Provide results
```

### Advanced usage
```
User: "I need detailed Deepseek V4 Architecture assistance"
→ Clarify scope → Execute analysis → Present findings
```
