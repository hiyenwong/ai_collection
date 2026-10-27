---
name: quantum-cadence-postquantum-consensus
description: Use when designing post-quantum BFT consensus protocols.
category: ai_collection
---

# Quantum Cadence — Post-Quantum Consensus Without Quorum Certificates

Source: arXiv 2610.32803 — "Quantum Cadence: Post-Quantum Consensus with Multiple Concurrent Proposers" (Jalalzai, Klenze, Komatovic; submitted 2026-10-23, 35pp). Systems-engineering methodology for migrating certificate-based BFT consensus to post-quantum signatures.

## Problem
High-performance BFT consensus (HotStuff family; Cadence/Chorus) relies on quorum certificates: 2f+1 validator signatures aggregated by BLS into ONE short aggregate signature, broadcast by every validator for every proposer. A large-scale quantum computer breaks pairing-based BLS. Known post-quantum signatures (Dilithium, SPHINCS+) are several times larger, and no post-quantum aggregation scheme achieves comparable aggregate size/time — so an unaggregated certificate is a list of 2f+1 large signatures per proposer per slot, making certificate broadcast bandwidth-infeasible.

## Core idea (reusable pattern)
**Eliminate certificates entirely: count quorums LOCALLY.** No validator ever proves a quorum to another; each validator decides from quorums among the messages it has received itself. Safety and liveness then rest only on authenticated channels + collision-resistant hashing — signatures become purely an accountability add-on (at most 2 signed votes per validator per slot, each ONE signature over the whole per-proposer entry vector, so signature count is independent of the number of proposers).

## Architecture
Outer loop (Cadence) unchanged in structure: the Conductor schedules slots (extreme pipelining, no slot waits for an earlier slot's block). Slot consensus = **Quantum Chorus** (replaces Chorus), per slot with deadline D, n = 3f+1 validators:

1. **Dissemination (at D−Δ):** proposer erasure-codes its proposal into n symbols (any f+1 suffice to decode), commits via Merkle root ρ, signs the header ⟨j, ρ⟩; each validator receives its symbol + Merkle proof.
2. **Deadline vote (at D or early if all chunks held):** each validator broadcasts ONE Vote: per proposer an entry — positive ⟨j, ρ⟩ with its chunk attached, or negative ⟨j, ⊥⟩ — and ONE signature over the entire entry vector (Chorus signed per proposer, growing linearly with proposers).
3. **PathVote (at D+Δ):** each validator locally classifies per proposer from votes it received: 2f+1 entries naming the same value → ⟨fast, v⟩; f+1 positive entries with a valid decode→re-encode check → ⟨fallback, ρ⟩; else ⟨fallback, ⊥⟩. One signature over the whole path vote.
4. **Fast path (any time):** if 2f+1 received PathVotes carry ⟨fast, v_j⟩ with the same v_j for every proposer, plus f+1 corroborating positive Votes with chunks (decode+re-encode must reproduce the root) → FINALIZE meta-block (v_j) and relay ⟨Finalized, x⟩.
5. **Speculative finality:** a validator whose own entries are all fast speculatively finalizes ONE round earlier (at Step 3); speculation is reverted only if some validator equivocated.
6. **Fallback path:** at D+2Δ, per proposer take the first "clean set" — 2f+1 accepted entries from distinct validators with all fast entries agreeing — and adopt: ⟨fast, ⊥⟩ wins (unambiguous); ⟨fast, ρ⟩ wins only if decode→re-encode reproduces ρ; f+1 ⟨fallback, ρ⟩ for the same ρ wins; else ⊥. Feed the adopted meta-block to **Coda**.

### Coda — signature-free fallback Byzantine agreement
Builds on Forget-IT (leader-based BA with constant persistent memory). Coda decides a meta-block with per-proposer strong unanimity + obligation (decides the common input value for a proposer unless correct inputs differ; never decides a value no correct validator input).
- **Leaderless first view:** two voting rounds, implicit proposal (everyone votes its own input at once). When all correct validators adopted the same meta-block (the common late-proposer case: chunks reached only f+1..2f validators in time), decides in 2 message delays (D+4Δ) instead of 5 with a leader. The leaderless view is an optimization; without it Coda stays correct but slower.
- **Leader views** rotate round-robin; leader proposes its guard; validators vote-1 (justified by f+1 echoes of the previous view per entry), vote-2 on 2f+1 vote-1 (locking the meta-block); decide on 2f+1 vote-2 of current or previous view with the same lock.
- **View change:** echo safe values per proposer (consistent with every decision so far); next-view guard assembled from echoes; vote-2 messages carry sender's lock and guard (acceptance rule: f+1 vote-1 for the same meta-block first).
- **Persistent memory:** O(c·k) words for k proposers and c = max distinct values correct validators input per proposer (c ≤ 2 here: root or ⊥, absent equivocation) — constant in n, independent of the number of views; at most linear in n under equivocation. Long asynchronous periods cost NO persistent memory.
- **No cryptography at all:** guarantees hold against a computationally unbounded adversary (information-theoretic), using only authenticated channels and local clocks (drift-free after GST; no synchronized clocks needed).

### Halting gadget
Upon ⟨Finalized, x⟩ from f+1 distinct validators for the same x: finalize (relay it). Upon 2f+1: HALT — stop processing further slot messages but keep persistent state and never abandon ongoing broadcasts (retransmissions continue so lagging validators can still finalize). Time guards stay enabled after deadlines; a validator that halted handles no further messages of the slot.

### Accountability (the only use of signatures)
Votes are signed, so misbehavior leaves evidence: two different signed roots from one proposer prove equivocation (used as fallback certificates for ⊥); signed votes let correct validators prove to anyone which validator deviated. Lemma: under f faults, if some correct validator does not finalize by D+4Δ then at least f+1−(faults already identified) faulty validators are provably accountable.

## Guarantees preserved vs certificate-based Chorus
Agreement; termination; speculative finality; proposal inclusion (timely slot ⇒ block contains every correct proposer's proposal ⇒ short-term censorship resistance); optimal fast-path latency: 3 communication rounds including dissemination (speculation at 2), even with some proposers offline.

## Transferable design rules
1. When a cryptographic aggregate becomes the migration bottleneck (PQC, large signatures, slow aggregation), replace GLOBAL proofs with LOCAL quorum observation — anything a validator needs to decide, it can count itself from received messages.
2. Amortize signatures across vectors: sign the whole per-proposer entry vector once, not one signature per proposer; keep per-slot signature count O(1) per validator.
3. Erasure coding (f+1 of n) + Merkle commitment + decode/re-encode verification gives data availability and encoding validity without any certificate.
4. Reserve signatures for accountability evidence, never for safety/liveness — minimizes PQC bandwidth while preserving fault attribution.
5. Insert a leaderless first view in fallback BA to decide in 2 delays when correct validators agree (late-delivered proposals), before paying 5 delays for the first leader.
6. Make halting non-destructive: persisted state + never-abandoned broadcasts, so finalized values propagate to stragglers after halting.
7. Keep message validity checks purely local (signature on root + Merkle path + at-most-one Vote/PathVote per validator) so acceptance rules stay checkable without global state.

## Evaluation pattern
Simulation vs BLS-aggregated Chorus, n = 200 validators, 1 Gbps links, up to 20 proposers: latency comparable to Chorus (≈200 ms from proposer broadcast to finalize; speculative finality ≈50 ms earlier) while carrying post-quantum signatures; scales BETTER with the number of proposers because Chorus's signature count grows linearly with proposers but Quantum Chorus's stays constant.

## Pitfalls
- Simply deleting certificates from an existing protocol fails — several parts (MVBA external validity, fallback certification, Conductor proofs) structurally depend on them; each dependency must be redesigned (Coda replaces certified-input MVBA; Conductor certificate forwarding is replaced by Finalized-relay halting).
- Local quorum counting requires message persistence and retransmission discipline ("halting does not abandon broadcasts").
- Fast-path finalization must corroborate with chunks + decode/re-encode, else a Merkle root alone cannot guarantee data availability.
- Speculative finality is revertible by design — downstream applications must tolerate one-round reverts on equivocation.

## Activation
post-quantum consensus, certificate-free BFT, quorum certificate, blockchain validator bandwidth, Chorus, Cadence, HotStuff migration, BLS aggregation replacement, signature-free Byzantine agreement, Forget-IT, multiple concurrent proposers, accountability, extreme pipelining, censorship resistance.