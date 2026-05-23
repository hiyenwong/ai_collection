---
name: liver-live-reconfiguration
description: "Live reconfiguration methodology for elastic distributed model training — replacing checkpoint/restart with live, bounded-memory handoffs between mixed-parallel training worlds. Based on LiveR paper (arXiv:2605.22014). Use when designing elastic training systems for LLMs, handling volatile GPU resources, or implementing live reconfiguration in distributed computing."
---

# LiveR: Live Reconfiguration for Elastic Model Training

Live reconfiguration runtime for elastic LLM training that replaces storage-backed restart with a **live, bounded-memory handoff between mixed-parallel training worlds**. Core insight: while the current world continues training, asynchronously prepare the target world and stream model state directly over high-bandwidth interconnects.

## Core Architecture

### Key Insight

Existing elastic training systems treat reconfiguration as **stop-and-restart**:
1. Externalize distributed state through checkpoints
2. Rebuild distributed runtime on a new topology
3. Restart training

This incurs substantial downtime from: checkpoint I/O, process restart, CUDA initialization, communicator setup.

**LiveR's approach**: Replace storage-backed restart with live handoff.

### Live Handoff Pipeline

```
Current World (still training)
│
├── Asynchronously prepare target world ───► Bootstraps new workers in isolation
│                                              (heavyweight init off critical path)
│
├── Stream model state over high-bandwidth ──► Reshape online across
│   interconnects                                TP, PP, DP dimensions
│
└── Lightweight commit ──► Switch training to new configuration
                           (no stop-and-restart on live path)
```

## Key Technical Components

### 1. Asynchronous Target World Preparation

While the current world continues training, LiveR:
- Prepares the target world in **isolated workers**
- Bootstraps newly added workers to keep heavyweight initialization off the critical path
- No pausing of the active training loop

### 2. Bounded-Memory State Streaming

Instead of checkpoint I/O (writing to disk), LiveR:
- Streams model state **directly over high-bandwidth interconnects** (NVLink, InfiniBand)
- Reshapes state **online** across tensor, pipeline, and data parallel dimensions
- Bounded memory footprint during handoff

### 3. Lightweight Commit

- Once target world is ready, a **lightweight commit** switches training
- No stop-and-restart on the live path
- Minimal downtime (seconds vs minutes)

### 4. Mixed-Parallel Training Support

Handles reconfiguration across:
- **Tensor Parallelism (TP)**
- **Pipeline Parallelism (PP)**
- **Data Parallelism (DP)**

## Implementation Details

- Built atop **Megatron-LM** and **PyTorch**
- Evaluated on a **multi-node GPU cluster**

## Performance Results

- **Reduces downtime from minutes to seconds**
- **14-23× speedup** over checkpoint/restart baselines
- **Minimal steady-state overhead**
- **Up to 99% training goodput** under volatile-resource conditions
- Makes volatile low-cost GPU capacity practical for LLM training

## Usage Patterns

### When to Apply This Pattern

- Elastic LLM training on spot/preemptible instances
- Shared cluster GPU reclaim scenarios
- Any distributed training needing dynamic resource elasticity
- Multi-tenant GPU clusters with variable allocations

### Key Design Decisions

1. **Avoid Checkpoint I/O**: Stream state over interconnects instead of writing/reading from storage
2. **Asynchronous Preparation**: Prepare target world while current world trains (hide latency)
3. **Isolated Bootstrapping**: New workers initialized independently (no main process blocking)
4. **Online State Reshaping**: Transform model state across parallelism dimensions without serialization

### System Requirements

- High-bandwidth interconnects between nodes (NVLink, InfiniBand)
- Megatron-LM compatible training infrastructure
- PyTorch distributed runtime

## Related Skills

- [[agent-first-bootstrap]] - Agent-First project initialization methodology
- [[speculative-decoding-optimization]] - LLM inference optimization patterns
- [[pbkv-agent-workflow]] - KV-cache optimization for LLM serving

## Activation Keywords

- elastic training, live reconfiguration, live handoff, mixed-parallel training
- LLM training, spot instances, preemptible GPU, volatile GPU
- distributed training, Megatron-LM, tensor parallelism, pipeline parallelism
- checkpoint restart, model training elasticity, elastic distributed computing