---
name: liver-live-reconfiguration
description: "LiveR: Live reconfiguration runtime for elastic LLM training. Fine-grained elasticity via live handoff between mixed-parallel training worlds without stop-and-restart."
category: "systems-engineering"
bump_similar: false
---

# LiveR: Live Reconfiguration for Elastic Model Training

## Source
- **arXiv**: 2605.22014 (22 May 2026)
- **Authors**: Haoyuan Liu, Kairui Zhou, Shuyao Qi, Qinwei Yang, Shengkai Lin, Shizhen Zhao, Wei Zhang
- **Venue**: MLSys 2026 (to appear)

## Core Problem
Elastic LLM training on volatile GPU capacity (spot instances, reclaimable resources) needs frequent reconfiguration. Existing systems use stop-and-restart: checkpoint → teardown → rebuild → resume, incurring minutes of downtime per event.

## Key Innovation
LiveR replaces storage-backed restart with a **live, bounded-memory handoff between mixed-parallel training worlds**. While the current world trains, LiveR asynchronously prepares the target world and streams model state over high-bandwidth interconnects, reshaping state online across TP/PP/DP dimensions.

## Core Methodology

### 1. Parallel Worlds (Background Construction)
- **Active World**: continues training uninterrupted
- **Shadow World**: asynchronously initialized with new process groups
- Worlds coexist during reconfiguration — no teardown until switch

### 2. Mock Process Groups (Hide Initialization Latency)
- New ranks join isolated groups; boot CUDA, NCCL, JIT in background
- Only final commit is on critical path (<0.5s)

### 3. Streaming Resharding (Bounded Memory)
- **Abstract Resource View**: state defined by logical tensors + sharding spec
- **Intersection-based transfer**: computes minimal data movement between source/target layouts
- Layers transferred via pipeline streaming; staging buffer capped at one layer (~512MB–1GB)
- No full model copy needed

### 4. Atomic Switch & Consistent Cut
- Finish current iteration (natural consistent cut under 1F1B pipeline)
- Streaming transfers → atomic metadata swap (<0.5s)

### 5. Design Invariants
1. No global restart on live path
2. Bounded memory during transition (no second model copy)
3. Arbitrary TP/PP/DP reshaping
4. Bit-exact numerical parity

## Key Results
- **14×–23× speedup** over Megatron-LM Checkpoint
- **~7s downtime** per event (vs 150s+)
- **<0.3% steady-state overhead**
- **~99% training efficiency** under volatility (vs 61.3%)
- Verified bit-exact; supports 1,024 GPUs / 70B params

## Systems Engineering Patterns
1. **Live Handoff (Blue/Green for Training)**: two parallel worlds during transition
2. **Background Initialization Batching**: move cold-start off critical path
3. **Streaming State Transfer**: decouple logical from physical layout; use geometric intersection for minimal data movement
4. **Consistent Cut**: natural iteration boundaries as state transfer points

## Implementation
- ~10K lines Python; runtime extension to Megatron-LM + PyTorch Distributed
- Companion Manager daemon for shadow world lifecycle
- Staging buffer: 512MB–1GB per rank; NCCL backend

## Activation
- **Keywords**: elastic training, live reconfiguration, distributed systems, LLM training, spot instances
- **Use when**: building distributed training infra, elastic compute systems needing topology changes without downtime

## Pitfalls
- Assumes warning-based/planned elasticity (preemption notices)
- Requires GPU reachability during transfer (2-4s)
- Not for unannounced failures; needs checkpoint fallback
- ~2GB memory overhead per rank during transition
