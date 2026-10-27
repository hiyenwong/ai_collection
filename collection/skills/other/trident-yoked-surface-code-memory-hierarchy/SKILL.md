---
name: trident-yoked-surface-code-memory-hierarchy
category: ai_collection
description: Use when designing FTQC memory tiers with YSC hierarchy.
version: "1.0.0"
source: arXiv:2610.32152
source_title: "Trident: Efficient Load Verification for Yoked Surface Codes using a Three-Level Memory Hierarchy"
authors: "Gunagya Singh Mamak, Suhas Vittal, Kabir Dubey, Kaitlin N. Smith, Moinuddin K. Qureshi (ASPLOS 2027)"
author: cs-cron-2026-10-27
license: MIT
published: 2026-10-23
categories: quant-ph, computer architecture
metadata:
  hermes:
    tags: [quantum-computing, ftqc, surface-codes, memory-hierarchy, computer-architecture]
    related_skills: [lattice-surgery-surface-code, puremagic-lattice-surgery-scheduler, barbell-qldpc-superconducting-hardware]
arxiv_id: "2610.32152"
trigger_words:
  - FTQC memory hierarchy
  - yoked surface codes
  - YSC load verification
  - quantum memory tier
  - compiler-managed cache
  - Belady OPT replacement
  - quantum prefetching
  - surface code architecture
  - teraquop machine
---

# Trident: Three-Level Memory Hierarchy for Yoked Surface Codes

## When to Use

- Designing or simulating the memory subsystem of a surface-code FTQC (teraquop regime, YSC or qLDPC-backed memory).
- Profiling quantum programs where load/store verification stalls dominate IPC (baseline: 64% of cycles).
- Porting classical cache/prefetch techniques to exclusive (no-cloning) hierarchies.
- Any system where a correctness check on fetched state (not data movement) is the serial bottleneck.

## Overview

Trident (ASPLOS 2027, Georgia Tech / IBM) applies classical memory-hierarchy design to fault-tolerant quantum computers built on surface codes. In Yoked Surface Code (YSC) memories, a load is not fault-tolerant: after an 8-cycle retrieval, the FTQC must measure ALL yokes of the 2D YSC block to verify the load — 178 cycles during which compute stalls. Baseline FTQCs spend 64% of cycles stalled on load verification. Trident adds a small 1D-YSC intermediate tier (L1) whose 2 yokes interleave with retrieval (0-cycle exposed verification), then manages that tier with compiler-side cache replacement (Trident-D) or prefetching (Trident-P). Results: 2.8x / 4.2x speedup at only +4.9% physical-qubit cost, capturing 73.7% of the ideal 5.7x (zero-verification) speedup while the all-1D ideal would cost +52.8% qubits.

## Core Insight: Verification, Not Retrieval, Is the Quantum Memory Bottleneck

In classical ECC-DRAM, verification of loaded data is negligible and retrieval dominates. YSC memory inverts this:

- **Retrieval** = logical state teleportation: measure joint ZZ between source (YSC qubit) and a |+>-prepared surface-code target, then measure source in X basis. 8 cycles regardless of variant.
- **Verification** = re-establishing the syndrome history the load broke. During retrieval the YSC routing channel is occupied by lattice surgery, so yokes go unmeasured and the loaded qubit's syndrome history is incomplete — no lattice-surgery operation can be resolved on it until all yokes are measured.
- 2D YSC [[256,194,4]] (d_in=11, w=16): verification = 25*d_in*w + 4*d_in = 4444 syndrome rounds = 4444/d_eff ~= 178 compute cycles (d_eff=25). 1D YSC [[n, n-2, 2]] (d_in=15): only 2 yokes, measured in the gaps of the retrieval schedule → total load = 8 cycles, exposed verification = 0.

**Verification latency scaling** (fits all 5 block sizes in the paper):

```
V.L.(cycles) = (25 * d_in * sqrt(BlockSize) + 4 * d_in) / d_eff
Block 64 -> 90 cycles; 144 -> 134; 256 -> 178; 400 -> 222; 576 -> 266
```

Larger outer codes buy density but pay sqrt-proportional verification latency — the fundamental density/latency tension Trident resolves in hardware structure rather than code choice.

## The Three-Level Hierarchy

```
L0  compute      4 surface codes, d=25, 2028 phys qubits/logical (incl. routing)
L1  1D YSC       1 block, 8 entries, d_in=15, 1100 phys qubits/logical, 0-cycle verify
L2  2D YSCs      [[256,194,4]], 194 logical/block, 454 phys qubits/logical, 178-cycle verify
```

Density ordering is inverted relative to latency: L2 is 4.5x denser than plain surface codes but slow to verify; L1 is only 1.8x denser but free to verify. Replacing all L2 with L1 would cost 2.5x memory qubits — so keep L2 as the bulk store and use a SINGLE 8-entry L1 as a latency-kill tier (8.8k physical qubits total, +4.9% memory footprint).

### Exclusive-hierarchy load semantics (no-cloning constraint)

A quantum memory hierarchy is EXCLUSIVE: a qubit lives at exactly one level, so every load must be paired with a store (conservation of slots):

- **L1 load**: target B moves to L0; the L0 victim A swaps into B's vacated L1 slot.
- **L2 load**: target C moves to L0; L0 victim A goes to L1, the L1 evictee B drops into C's vacated L2 slot. (Compiler may alternatively route A directly to L2.)

Consequence: in an exclusive hierarchy every hit removes the accessed qubit from its location, so **LRU degenerates to FIFO** — classical recency information is destroyed by the no-cloning theorem.

## Trident-D: Compiler-Managed Cache (demand-driven)

Quantum programs have deterministic, compile-time-known access streams. That makes **Belady OPT replacement implementable** — impossible for hardware-managed classical caches:

1. Pass 1: read the program, record the DAG-layer timestamp of every load (no modification).
2. Pass 2: re-read and rewrite. On an L2 load, evict the L1 qubit whose NEXT load is farthest in the future (OPT); on L1 hit, the load + its paired store follow semantic 1 unchanged.

Results: LRU(FIFO) 2.3x / hit 66.7%; OPT 2.8x / hit 78.7%. OPT is the ceiling for demand-driven caching — workloads with poor temporal locality (chromium_q_sel: 33% memory ops) thrash it, motivating prefetch.

## Trident-P: Prefetch-Driven Hierarchy

Make performance independent of temporal locality: for every L2 load, insert a prefetch that moves the target into L1 BEFORE the load:

- **Victim choice = FIFO (smallest t_store)**. The prefetch instruction is inserted DIRECTLY AFTER the instruction that stored the victim — the earliest legal point. Evicting the oldest resident maximizes (t_load - t_prefetch), the window in which L2 verifies the prefetch off the critical path.
- If t_load - t_prefetch >= 178 cycles, the subsequent L1 load has ZERO verification overhead; otherwise exposed latency = 178 - (t_load - t_prefetch).
- **Inflight prefetches are never evicted** (evicting one would undo the prefetch); L1 holds up to 8 inflight prefetches — saturation (<0.01% of loads) leaves the qubit to load from L2.

Results: 4.2x gmean; mean verification latency 178 -> 14.3 cycles (Trident-D: 41.3); stalls 64% -> 20%; prefetch coverage 32.5% of loads; latency fully hidden for 91.0% of loads, partially for 9.0%. Trident-P at L1 capacity 8 beats Trident-D at capacity 16 (4.2x vs 3.8x) — prefetching buys back capacity.

## Fidelity Model (why performance IS fidelity)

Yoke-cycle logical error probability grows POLYNOMIALLY in r (syndrome rounds elapsed per yoke cycle) — serving memory accesses delays yoke measurement:

```
e_1D = r^2 * n   * 10^(-d_in)  / 2000
e_2D = r^4 * n^2 * 200^(-d_in) / 20000
```

(The 200^(-d_in) base for 2D reflects distance-4 outer-code protection of 2D error chains; the /2000, /20000 are the paper's normalizations. Note pdftotext renders these ambiguously — the exponent is -d_in, NOT -d_in/2000, which would give probabilities near 1.) Bounding rules in simulation: 2D YSC serves at most 100 consecutive access cycles and starts yoke measurement after 14 idle cycles; 1D YSC checks on every access or after 50 idle cycles. Application fidelity tracks speedup because fewer cycles = less error exposure: baseline 92.9% -> Trident-D 97.4% -> Trident-P 98.1% (ideal 100%).

## Reusable Pattern (beyond quantum)

**Tiered-verification latency hiding** — whenever a storage tier's CORRECTNESS CHECK (not its data movement) dominates access latency:

1. Account retrieval and verification latency separately (profile where the asymmetry is).
2. Interpose a small tier where the check interleaves with access (near-zero exposed check); keep the bulky tier for density.
3. Exploit deterministic/compile-time-known access streams: optimal (Belady) replacement becomes practical; otherwise note LRU collapses to FIFO in exclusive (move-not-copy) hierarchies.
4. If temporal locality is absent, switch to prefetch: schedule the expensive check EARLY by binding prefetch insertion to the earliest slot-freeding instruction, and evict the oldest resident to maximize the overlap window. Protect in-flight items from eviction.
5. Price the tier in the scarce resource (here physical qubits, +4.9%) against the latency-hiding gain (73.7% of ideal) — the cost/benefit frontier is usually dominated by a very small tier.

This applies to: verified loading in verified filesystems/databases (fsck-on-read), attested TEE memory paging, post-quantum signed-state deserialization, and any pipeline where validation of fetched state is the serial bottleneck.

## Quantitative Anchors (for benchmark porting)

- Baseline: 64% of cycles stalled on verification; ideal zero-verify 5.7x gmean.
- 10 workloads: qubitization (PREPARE Rz-heavy/compute-bound; SELECT memory-bound), Trotterization, Shor RSA-24, Grover 3-SAT; HamLib Hamiltonians; 100M instructions simulated, IPC metric; teraquop regime (10^-15 logical error/round).
- L1 capacity sweep 4/8/16/24: D 2.1/2.8/3.8/4.3x, P 3.1/4.2/4.9/5.5x (near-linear).
- Compute capacity sweep 4/8/12/16: D 2.8/2.4/2.5/2.3x, P 4.2/3.4/3.4/3.1x (normalized per-capacity baseline).
- Block-size sweep: Trident advantage shrinks with larger blocks (D 3.7x@64 -> 2.4x@576; P 4.6x -> 3.8x) but stays large — sqrt-scaling of verification latency is the binding constraint.

## Pitfalls

- **Loads and stores are both unverified** during YSC routing-channel use; store verification is simply off the critical path (compute rarely depends on stores). Do not model stores as free — they just hide.
- **Never evict inflight prefetches** — performance loss is immediate and the prefetch must re-issue from L2.
- LRU==FIFO in exclusive hierarchies; classical cache intuition about recency does not transfer.
- Verification latency scales with sqrt(outer-code size) — bigger YSC blocks make BOTH baseline and Trident worse; the +4.9% overhead figure assumes the [[256,194,4]] default.
- Magic-state factories are EXCLUDED from the +4.9% footprint accounting (compute + memory subsystems only).
- The simulator serializes all memory ops (one at a time) — parallel access scheduling is unmodeled upside.

## References

- arXiv:2610.32152 — Trident (ASPLOS '27). YSCs from Google's yoked-surface-code proposal (concatenate surface code with high-rate outer codes; yokes = outer-code parity checks).
- Related local skills: lattice-surgery-surface-code, puremagic-lattice-surgery-scheduler (surgery scheduling), barbell-qldpc-superconducting-hardware (qLDPC alternative to YSC density).
- Companion import this batch: arXiv:2610.31694 (verified Pauli-product measurement compilation — the compiler side of the same FTQC stack).
