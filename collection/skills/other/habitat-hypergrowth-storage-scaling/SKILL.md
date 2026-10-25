---
name: habitat-hypergrowth-storage-scaling
description: "Use when scaling storage platforms through hypergrowth."
---

# Habitat: Hypergrowth Storage Scaling

Engineering methodology from OpenAI's two-part "Rapidly scaling online storage to serve over 1 billion ChatGPT users" (Sep + Oct 2026): how Habitat grew from a Python client library (DevDay 2023) into a 70M+ QPS / 500PB+ / ~40-region online storage platform, and how its Cosmos DB tenant model was re-architected. Use as a playbook for services riding sustained ~10x/year growth.

## When to Use

- Scaling a data platform through multi-year hypergrowth (~10x/year)
- Deciding when to extract a library into a standalone service
- Deliberately carrying technical debt while betting on AI-assisted rewrites
- Choosing multi-tenant vs dedicated capacity for a NoSQL/cloud store
- Cutting global read latency on a read-heavy (90%+ reads) workload

## Part I — The Service (Habitat)

1. **Service-extraction timing criterion**: pull a library out of its host when cross-service protocol coordination becomes fragile (at OpenAI, an unrelated rollback of another service triggered an incident in the storage path) — independence buys unified deployment, observability, security, and access control.
2. **Deliberate technical debt**: kept Python long past its comfort zone (to 20M+ QPS), explicitly betting that Codex/GPT-class coding agents would make a future rewrite cheap. Make the debt a decision, not an accident.
3. **Survival tricks at 20M QPS on Python**:
   - asyncio **event-loop scheduling latency as a first-class latency metric** — queueing inside the loop is user-visible latency
   - feature-flag (Statsig) JSON parsing stalls — config parsing can dominate tail latency
   - **LIFO connection reuse caused metastable failures; switching to FIFO fixed it**
   - Envoy/HTTP2 connection fan-in to bound connection counts
4. **Whole-service Rust rewrite**: 2026 Q2, 2 engineers + Codex + GPT-5.5 rewrote the entire service from scratch in Rust — it now serves 95% of production traffic at **6x CPU and 15x memory efficiency**, with lower mean and tail latency.
5. **Restricted NoSQL API** (not arbitrary SQL) as a scalability tool — a deliberately limited interface preserves optimization freedom for the platform.

## Part II — The Tenant Model (Azure Cosmos DB)

The largest single Cosmos DB account (tens of PB, 20M+ QPS) went through a three-stage tenant journey:

1. **Shared containers** → logical-partition hot keys and noisy-neighbor interference
2. **Dedicated containers** → good isolation, but capacity planning lands on product teams who learn their true capacity needs **on launch day** (SEV firefights)
3. **Vendor-coengineered shared multi-tenancy** → joint work with Azure on hot-key throttling, request-class QoS, and improved serverless (10K RU/s per physical partition) — return to shared containers with **zero capacity-planning and zero noisy-neighbor incidents**

**Read-path tiering** (workload is 90%+ reads): data colocation, replication of latency-sensitive datasets, CDC-based integrated caching, and the Rust service cut global read p50 from ~120ms to ~10ms (12x). Next generation: RocksDB Cloud kernel + Raft-based replication toward self-built EB-scale storage.

## Pitfalls / Honest Limits

- Dedicated capacity feels safe but converts a platform problem into per-team capacity forecasting — usually held by teams with worse information.
- Shared multi-tenancy is only viable after the vendor side ships real protections (hot-key throttling, tiered QoS, serverless improvements); sequence accordingly.
- Carrying debt against an AI-rewrite bet is a portfolio decision — set explicit QPS/latency triggers for when the rewrite must start, in case the tooling underdelivers.
- Measure the event loop and the config parser, not just request handlers.

## Activation Keywords

- hypergrowth storage scaling
- service extraction timing
- deliberate technical debt
- AI-assisted Rust rewrite
- asyncio event loop latency metric
- LIFO FIFO connection reuse metastable failure
- multi-tenant NoSQL capacity planning
- noisy neighbor mitigation
- CDC read cache tiering
- Cosmos DB tenant model