---
name: execution-gap-intent-validation-cps
description: Execution-gap model + AIS contract + version-conditional commands: run the last check where context is owned
category: ai_collection
trigger: execution gap, TOCTOU race in industrial CPS, action intent schema, AIS, XAIR runtime, version-conditional command, read-set version, predicate-truth version, global version false revocations, stale release, stale effect, A-B-A undone change, history violation, serialization domain, context store replica, controller scan check, PLC interlock, operator pause race, late-binding authorization, freshness window, intent deadline, LLM agent command validation, edge runtime OpenPLC, ROS 2 action governance, OPC UA context, stop fencing, atomic commit authorization, actuation log, placement rule for runtime checks
---

# Execution-Time Validation of Context-Carrying Action Intents in Industrial CPS

**Source**: "Execution-Time Validation of Context-Carrying Action Intents in Industrial Cyber-Physical Systems" — Luca D'Agati, Giuseppe Tricomi, Fabio Orazio Mirto, Giovanni Merlino (University of Messina + CINI), arXiv:2610.27971 (cs.PL, cs.CR, cs.DC, eess.SY, 20 Oct 2026).

## Core Contribution

Names and formalizes the **execution gap** — a command proposed by a learned policy, operator, or scheduler is admissible at decision time but **no longer admissible when released** into middleware (inference + confirmation + transport in between; the plant changed, e.g., an operator pause). Shows the problem is **architectural, not a speed problem**: what the last check can guarantee depends on **where it runs** (which serialization domain owns the state) and **which version scope it compares**, much less on how fast it is. Delivers AIS (producer contract) + XAIR (edge runtime) + a placement design guide, validated in controlled ablations with declared ground truth on 6 testbeds (single host, distributed, reserved cores, wide-area VPN, LAN, ARM/RISC-V embedded boards) + OpenPLC.

## The Formal Model (the reusable abstraction)

- **Intent** `I = (td, w, d, P, S, α, r, p)`: decision time `td`, **freshness window** `w` (max age at validation), **deadline** `d` (max age at release; default `d = w`), preconditions `P`, hard constraints `S`, action descriptor `α`, target `r`, priority `p`.
- **Instants**: `td < tv ≤ tℓ < tm ≤ ta` — decision, validation, **last check** (`tg` = optimistic gate recheck, or `tc` = atomic commit), middleware release, effect. Unprotected intervals: `∆g = tℓ − tv`, `∆r = tm − tℓ`.
- **Any check on a replica leaves an unprotected interval** `]tℓ, tm]`. Only a check **in the serialization domain that owns the context** — the controller's scan that produces the effect — closes it, and only for the state that controller owns. Cross-owner read-sets split `R = R1 ∪ … ∪ Rk`; guarantee holds per owner subset; no single domain closes everything short of a distributed transaction.
- **Version scopes** (what advances the version the check compares):
  - **global**: every accepted update → blocks everything including A–B–A, but revokes valid intents under unrelated updates (measured FPR 12% @20 Hz, 64% @100 Hz, ~99% on slow embedded gate @100 Hz).
  - **read-set `νR`**: only value changes on paths `R(I)` that the predicates read → conservative, blocks A–B–A; correct for supervisory/discrete state, but **destroyed by continuous signals** (hydraulic trace: 37% false revocations at 10 ms publishing even though the threshold predicate never flipped).
  - **predicate-truth `πI`**: only truth flips of registered predicates → zero false revocations on continuous traces, still blocks A–B–A, cost = re-evaluating registered predicates on every touching update (registry lag: document layout sustains 100 Hz only at 10 predicates, 53 upd/s at 1k, 4.9 at 10k; hash layout 100 Hz at 1k, 10.8 upd/s at 10k).
- **FPR model**: `Pr[revoke | valid] ≈ λ·∆g` (Poisson: `1 − e^(−λ∆g)`; periodic: `min(1, λ∆g)`) — **cost of a version scope = admitted update rate × gate latency**. Slower gate (embedded, wide-area) ⇒ scope choice matters more.
- **Three failure classes**: stale release (`Y=1 ∧ ¬A(I,tm)`), stale effect (replica `C` lags controller `X`, effect evaluated on `X(ta)`), **history violation** (A–B–A: predicates held again at release but were false in between — e.g., pause-then-resume; not stale, but violates uninterrupted-validity policies).

## AIS + XAIR Design (the mechanism)

- **AIS = contract carried by the payload**: validity travels with the action; transport-agnostic (HTTP/ROS 2/MQTT/OPC UA); JSON-Schema-validated; **unknown fields rejected**; only enforceable degradation policies accepted. Predicate grammar = **conjunctions of `Path Op Literal` comparisons** → read-set derivable directly from syntax → store maintains νR/πI per update. Everything **fails closed** (empty/incompatible/timeout/missing path ⇒ refuse).
- **Three properties kept apart** (XAIR gives only the first in full): (1) **intent validity** — declared assumptions still hold at last check; (2) **policy compliance** — operator-mandated predicates appended per action type server-side (producers cannot remove them; omitted producer precondition still releases unless mandated — measured); (3) **physical safety** — NOT provided; safety-rated layer stays authoritative.
- **Action classes** (operator policy; class follows action type, never producer-declared): **stop** class = never rechecked, no lock, not in actuation log, **fences in-flight intents of its target** (writes stop-time into context; every other intent on that target carries "stop-time ≤ its decision time" → falsified at recheck/commit). Measured: fence turns 238–245/330 stale into 0/330 while releasing all valid controls. Emergency stops stay on the safety PLC path, never through XAIR.
- **Two release modes**: **optimistic** (gateway recheck at `tg`; leaves `]tg,tm]` ≈ 1–4 ms unprotected) vs **atomic commit** (`tc`: store-side script serialized with all updates — exact ordering, authorization log, +0.01–0.19 ms only, but **does not shorten the interval**; post-commit invalidations detectable from versions; release guard/margin needed to hold deadline at `tm`). Actuation log + idempotent actuator ⇒ at-most-once application, crash-safe.
- **Version-conditional command** (the closing move): gateway passes the expected version + absolute deadline; controller executes **only if its own version is unchanged, in the same scan that produces the effect**. Valid under A1–A5: controller is sole writer; version advances on every relevant variable change; replica carries (state, version) atomically; versions never reused (incl. across restarts); check+effect in one scan. ≈ If-Match/CAS/fencing tokens, **but the expected version is declared in the contract by a producer that never talks to the controller**.

## Key Empirical Results (declared ground truth, 6 testbeds + OpenPLC)

- **Floors fail 100%**: direct release and freshness-only validation released every obsolete intent; never-refreshed cache released every obsolete intent; read-through/XAIR 0.
- **Placement law (E4)**: unconditional commands via replica checks — stale effects up to **100% of trials** when the pause lands a few ms after submission (6–16 ms distributed; 20–40 ms LAN; ≥160 ms wide-area; ~1 in 6 on OpenPLC). Controller-local interlock or version-conditional command: **0/1100 stale** (95% UB 0.35%). The unprotected interval is measurable and architecture-dependent, not eliminated by speed.
- **A–B–A (E3/E4)**: predicate-only gates released **250/250** undone changes; versioned gates (read-set or truth) blocked **all**, in XAIR **and in a policy engine (OPA) once given the same versions** — the protection is the version, not the engine. At the controller: interlock still executed ~28–30% after pause-resume; version-conditional refused all.
- **Scope cost (E5/E5-trace)**: global version revokes valid intents (12%@20Hz/64%@100Hz); read-set clean on discrete state but 37% FPR under continuous signals; predicate-truth 0% FPR everywhere, at registry-maintenance cost. **E6 production job-shop log**: drift within a minute is rare, but decisions that *wait* (LLM, operator confirmation, queue) see machine-state change in a few % to ~half of cases within an hour — the gap matters for long-wait, high-consequence actions.
- **Edge cost (E7)**: XAIR on one pinned core of Raspberry Pi 4 / RISC-V VisionFive 2: **148–168 intents/s**, ~6 ms E2E, <100 MB RSS; server 909–956/s; 50 producers fine; crash tests: no stale release, no lost/duplicated command.
- **Headline lesson**: the **fastest** guard (stale cache) failed every drift trial; the **slowest** (XAIR) failed none. A latency figure alone says nothing about semantic safety without the **consistency class + observation boundary + drift protocol** under which it was measured.

## Design Guide (Table 11 condensed) — last check × version scope → what it blocks

| Last check runs | Version | change before check | change after check | undone (A–B–A) | revokes valid intents by |
|---|---|---|---|---|---|
| Local cache | none | no | no | no | – |
| Store gate | none | blocked | no | no | – |
| Store gate | global | blocked | no | blocked | every update |
| Store gate | read-set | blocked | no | blocked | read-set value changes |
| Store gate | predicate-truth | blocked | no | blocked | truth flips only |
| Atomic commit | read-set/truth | blocked (exactly ordered) | not blocked, **detected+audited** | blocked | as its version |
| Controller scan | none (interlock) | blocked | blocked (owned ctx only) | no | – |
| Controller scan | own version | blocked | blocked (owned ctx only) | **blocked** | changes of the state it covers |

**Placement rule**: run the last check **where the state it reads is owned, in its serialization domain** (controller's scan when the controller owns it; otherwise as close to `tm` as transport allows, anchored to an atomic commit when post-commit invalidations must be audited); compare a **version scoped to what the intent depends on** (read-set for discrete supervisory state, predicate-truth when continuous signals touch the read-set).

## Reusable Patterns Beyond Industrial Cells

- Any pipeline where a **decision waits** (LLM planner, human confirmation, scheduler queue) before acting on mutable state: attach freshness window + deadline + declared read-set to the decision; revalidate at release; version-condition the final write. Sibling problems: LLM-agent TOCTOU defenses, browser-use page-state validation, verdict-staleness in self-adaptive systems, agent tool gateways (OpenPort state witnesses) — all are **checks on a replica** unless the owner of the state does the compare.
- Serialization-domain thinking generalizes: middleware monitors, policy engines, and gateways all observe **replicas**; a guarantee only exists where the check is serialized with the writes it guards against.
- Fail-closed contracts beat scattered guards: validity metadata inside every request; unknown/unenforceable fields rejected; mandatory predicates added server-side; stops exempted by class; audit separates authorized/committed/released/effect-confirmed states (never conflate authorization with execution).
- Evaluation protocol worth copying: **declare ground truth before running** (O = invalidated set, V = valid set), report both **stale-release rate** and **false-positive revocation rate**, vary consistency class while holding payloads/drift fixed, and measure **where the interval is** (submission-offset sweeps) rather than only aggregate rates.

## Assumptions That Bound the Claims

Producers faulty-not-malicious; controlled network; every state transition must flow through the versioned context interface (a bypassed write is invisible to every gate); clock offset within declared ε (checker accepts `â ≤ d − ε`); single store primary; prototype is software-controller evidence, **not a safety certification** — physical safety stays with the safety-rated layer.
