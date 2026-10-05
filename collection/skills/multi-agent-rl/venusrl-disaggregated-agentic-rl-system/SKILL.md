---
name: venusrl-disaggregated-agentic-rl-system
description: "Use when training LLM agents with RL at scale. Priority scheduling + page-sharing sandboxes."
category: ai_collection
---

# VenusRL: Fully Disaggregated Agentic RL System

Source: arXiv:2610.03286 (Mingjun Zhang et al. — 2 Oct 2026; implemented in 24k lines Python/Rust/Golang atop SGLang + E2B + Firecracker)

## Core Methodology

System design for agentic RL (multi-turn tool-using LLM agents). Two system-level bottlenecks that per-GPU optimizations cannot fix:

1. **Group-completion straggler problem**: trainer waits for ENOUGH COMPLETE GROUPS (all rollouts of one prompt), not for GPU utilization. Action-level scheduling maximizes rollout GPU throughput but *scatters progress across groups* — many nearly-done groups, none done → training step still blocked. Selecting the optimal critical-group set at runtime is NP-hard (App. B) → use a lightweight heuristic.
2. **Sandbox memory stranding + state duplication**: tool sandboxes statically provisioned by declared memory ceilings (actual resident set far smaller) → most physical memory stranded. Worse: rollouts in the same sample group launch from identical templates → large fraction of pages byte-identical until divergent tool calls write new state — but native fork/mmap treats them as independent instances.

### Mechanism 1: Priority-aware action scheduler

- **Critical groups** = unfinished groups whose completion most likely unblocks the next trainer batch. Identify via **length-prediction heuristic**: a small fine-tuned predictor estimates each sample's remaining generation length at turn boundaries (kept off the critical path, updated asynchronously).
- Priority enforced at THREE layers:
  a. **Batch admission / GPU-slot execution** — high-priority samples scheduled first;
  b. **KV Cache residency** — preserve KV entries of high-priority trajectories best-effort (avoids recompute on resume after tool execution — multi-turn suspension is the KV killer);
  c. **Cross-worker request orchestration** — mitigate imbalanced distribution of high-priority samples across rollout workers.
- Scheduling granularity stays at action level (turn), decoupling generation workers from environment workers — keeps the anti-bubble benefit while re-focusing progress toward group completion.

### Mechanism 2: Environment resource manager

- **Dynamic admission threshold T (Alg. 1)**: node admits a new sandbox only when projected memory (current usage + estimated future growth of live sandboxes) stays under safe bound — estimates future growth from observed trajectories. **Sandbox migration**: if a node still exceeds the safe threshold, migrate sandboxes (Mooncake-based) rather than kill.
- **Template-keyed group page pool** (the elegant part): per-GROUP page pool indexed by **guest-memory offset**, keyed by the environment TEMPLATE (not content hash → never scan memory; sharing by construction). Three decoupled concerns that fork/mmap conflates:
  1. *virtual-address ownership* — each sandbox keeps its own VMA + page table;
  2. *physical-page residency* — read-only PTEs from different sandboxes in a group alias the SAME physical frame; pages populated lazily, one loader per offset at a time; pool entries immutable after population;
  3. *write permission* — masked until an actual write → **lazy CoW**. A write allocates a private frame for that sandbox only; divergence is local, isolation preserved at PTE granularity; a compromised sandbox can corrupt only its own private frames.
  Two requirements: **eager binding** (sharing installed at sandbox creation, before any page fault — no redundant frame ever allocated for snapshot pages) and **strict isolation** (write-invisible to peers, shared backing store untouchable).

### Results

- End-to-end training speedup: **1.07–3.26× vs Slime, 1.06–4.24× vs RollFlash, up to 2.67× vs ThunderAgent** (up to 4.24× headline). Holds under strict on-policy (async_factor=1).
- Batch-size scaling: bs=16 modest (1.06–1.17×), bs=32/64 → 1.26–1.71×+ (Qwen3-4B).
- Page sharing alone: up to **2.09×** speedup from cache-hit/density effects; admission+sharing combine multiplicatively.
- Sandbox lifecycle overhead negligible vs native E2B (Table 2).

## Reusable Patterns

- **Optimize for the blocking resource, not utilization**: identify what the consumer actually waits on (complete GROUPS, not idle GPUs) and route all scheduling priorities toward unblocking it. Length-prediction heuristics are a cheap, effective proxy when the true scheduling problem is NP-hard.
- **Template-keyed resource pooling**: when many worker instances instantiate from the same template, key shared immutable state by (template, offset) instead of content hashing — sharing becomes by-construction, zero scanning cost, lazy CoW preserves isolation. Generalizes to any sandbox/VM/worker-pool system (browser tabs, WASM runtimes, test-grid containers).
- **Decouple admission from provisioning**: static ceiling-based provisioning (memory ceilings, CPU limits, quota) systematically strands resources; replace with runtime admission control driven by *projected growth* estimates + migration as the safety valve.
- **Three-layer priority propagation**: a priority tag is only real if it survives every queue it passes through (batch admission, cache residency policy, cross-worker routing). Enforce at all layers or the high-priority path silently degrades to average.

## Pitfalls

- Length prediction is a heuristic — periodically validate against realized completion or the scheduler drifts toward wrong groups; keep the predictor small and off the critical path.
- Page pool keyed by template means DIVERGENT tool calls still write private frames — sharing gains vanish for templates that mutate early; group rollouts that diverge at step 1 get little benefit.
- KV-residency preservation is best-effort — under extreme concurrency, even high-priority trajectories get evicted; the recompute fallback must remain correct (it is, just slow).
- Dynamic admission needs an OOM escape hatch (migration), or a single mis-estimated burst kills the node.

## Activation

agentic RL training system, priority-aware scheduling, critical group, length-prediction heuristic, KV cache residency, sandbox memory stranding, page sharing pool, lazy copy-on-write, template-keyed pool, dynamic memory admission, disaggregated rollout training
