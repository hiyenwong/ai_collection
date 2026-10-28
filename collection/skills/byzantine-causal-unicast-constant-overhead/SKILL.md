---
name: byzantine-causal-unicast-constant-overhead
description: O(1)-overhead Byzantine causal unicast ordering protocol.
created: 2026-10-08
version: 1.0
author: hermes-cron (from Patel & Kshemkalyani, arXiv:2610.07368)
license: CC-BY-NC-SA-4.0 (paper); skill text original
source: arXiv:2610.07368
tags: [distributed-systems, byzantine-fault-tolerance, causal-ordering, protocol-design]
metadata:
  hermes:
    tags: [distributed-systems, byzantine-fault-tolerance, causal-ordering, protocol-design]
    related_skills: [cron-research-workflow]
---

# Byzantine-Tolerant Causal Unicast with Constant Message Space Overhead

**Source:** Patel & Kshemkalyani (UIC), arXiv:2610.07368, Oct 2026, cs.DC.

**Trigger:** designing Byzantine-resilient message ordering, causal broadcast/unicast, fault-tolerant distributed protocols without cryptography.

## When to Use

Use this skill when you need to design or reason about: message-ordering guarantees under adversarial nodes; causal delivery in asynchronous systems; low-overhead fault-tolerant protocol design; or when an impossibility result blocks a strong-safety + liveness combination and you need a quantified relaxation strategy.

## Problem Landscape

Causal message ordering (respecting Lamport happens-before) in **asynchronous systems under Byzantine failures** hits a proven impossibility wall: Misra & Kshemkalyani showed deterministic, cryptography-free protocols cannot guarantee both strong safety and liveness. Existing escape routes each pay heavily:

- Cachin et al. (secure causal atomic broadcast): threshold-encrypts full payloads through consensus → O(n³) expected word complexity.
- Auvolat et al.: BRB primitive → O(n) message overhead, O(n²) messages, unbounded memory.
- Minicast (Rumreich & Sivilotti): O(n) control broadcasts, unbounded local space (memory-exhaustion vulnerable).
- Sender-Inhibition / Channel Sync: require **synchrony** (bounded latency, timeouts).

## Core Methodology

### 1. SPS Invariant (Sender Permission to Send) — from Almeida 2026
Causality is enforced **at the sender, not the receiver**. A process i is blocked from network-sending m to j while there are undelivered messages that were sent to any process other than i by any peer k≠j that previously transmitted to i. Theorem chain: **SPS + FIFO ⇒ Causal delivery**. Receivers ACK every delivery; senders issue PERMITs once their own earlier sends are ACK-cleared. Key trick: **dependency vectors (DV) and last-message-sent (LMS) snapshots live ONLY in local state — never transmitted**. Network messages carry only fixed scalars (mid, per-flag, payload) → O(1) size vs system size n.

### 2. Isolated-Buffer Optimistic Model (the Byzantine contribution)
Replace Almeida's unified buffers with **per-peer isolated queues**:
- `U_i[1..n]` — unacked outbound messages per destination, capacity M_max (default 1024)
- `Q_i[1..n]` — missing-permit buffers per destination, capacity Q_max
- Local tracking vectors: `LD_i` (last delivered per src), `LMS_i` (last sent per dst), `LPR_i` (last permit received per src), plus a per-message DV/LMS snapshot stored locally.

Isolation confines each Byzantine peer's damage to its own queue pair — cross-channel DoS is structurally impossible.

### 3. Event-Driven Cascading Space Evictions (liveness mechanism)
When a queue saturates, the **head entry is force-evicted**: an unsent message is immediately network-sent (bypassing the SPS block); a sent-but-unpermitted message moves to Q (which itself evicts by force-sending a PERMIT). This is "optimistic": under attack or extreme latency the protocol degrades by *sending anyway* rather than deadlocking.

Neutralizes the canonical attacks:
- **ACK withholding** → only U_i[b] fills; eviction purges it, honest peers unaffected.
- **PERMIT withholding (state-pinning)** → blocked head is force-evicted when U_i[dst] saturates.
- **Future-message flooding** → receive() checks `m.mid ≤ LD_i[src]` and drops instantly, never buffering out-of-order data.
- **Replay** → monotone local clocks + LD filter drop duplicates/fakes.

### 4. Safety Abstraction: Congestion-Relaxed Causal Delivery (CRCD)
Formal middle ground between strong and weak safety: weak causal safety holds **for all honest-to-honest communication unless** (a) a correct sender's U-queue evicted, or (b) Q-queue evicted, or (c) a due PERMIT hadn't arrived before network-send. If no evictions occur at correct processes, CRCD reduces to standard Weak Safety. Violations are thus *quantifiably bounded* by local buffer capacities, not probabilistic.

## Complexity Contract
| Metric | Cost | Rationale |
|---|---|---|
| Network message size | **O(1)** | DV/LMS never leave the process |
| Local space | O(n²) | n queues × n-sized per-message snapshots |
| Time | worst O(n²) pass, **amortized O(n)** | event-driven, capacity-bounded |
| Crypto | none | deterministic |

The O(n²) local space is the deliberate trade: memory is cheap and private; network bandwidth is shared and expensive.

## Implementation Pattern (portable pseudocode)

```
on causalSend(dst, payload):
    if U[dst].full: evict_head(U[dst])           # force network-send; cascade to Q
    m := {mid: clock++, per: anyOtherQueueNonEmpty, payload}
    m.DV := LD_snapshot; m.LMS := LMS_snapshot   # LOCAL ONLY
    U[dst].enqueue(m); SendMessages(); SendPermits()

on receive MSG(m) from src:
    if m.mid <= LD[src]: drop (replay/fake)
    if not m.per: LPR[src] := m.mid
    LD[src] := m.mid; ACK(src, m.mid); deliver(m)

on receive ACK(mid) from src: dequeue U[src] up to mid; overflow → enqueue PERMIT candidates to Q[src]; SendPermits()

on receive PERMIT(mid) from src:
    if LD[src] >= mid > LPR[src]: LPR[src] := mid; SendMessages()

SendMessages(): for each dst, drain U[dst] head while ∀x≠dst: m.DV[x] <= LPR[x]
SendPermits(): for each dst, drain Q[dst] head while ∀x: m.LMS[x] < U[x][0].mid or U[x] empty
```

## Engineering Lessons
1. **Impossible trinity is navigable**: when a proof says X+Y is impossible, define a *quantified relaxation* (CRCD) instead of abandoning one property wholesale — the relaxation must degrade to the strict property under normal conditions.
2. **Move metadata off the wire**: any O(n) per-message metadata can often be reconstructed from sender-local state + a small control-plane (ACK/PERMIT) — trading local memory for network bytes.
3. **Isolation beats unification under adversary**: unified queues let one bad peer stall everything; per-peer isolation bounds blast radius structurally, no heuristics.
4. **Bounded optimism as liveness**: capacity-triggered force-eviction converts "waiting forever" into "occasionally violating ordering" — a deterministic, auditable degradation path.
5. **Caveat**: eviction-driven liveness assumes continuous traffic (or timeout-mode for reactive apps); credit-based flow control with window < min(M_max, Q_max) can re-deadlock.

## References
- Patel, Kshemkalyani. *Byzantine-Tolerant Causal Unicast with Constant Message Space Overhead*. arXiv:2610.07368 (2026)
- Almeida (2026) — SPS invariant, space-optimal crash-tolerant causal delivery
- Misra & Kshemkalyani (2024) — impossibility of deterministic crypto-free Byzantine causal ordering
