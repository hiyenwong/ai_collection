---
name: agent-scale-source-control
category: ai_collection
description: Use when scaling VCS infra for agent-driven monorepos.
version: "1.0.0"
source: https://www.anthropic.com/research/redesigning-source-control
source_title: "Redesigning source control at Anthropic"
author: anthropic-cron-2026-10-27
license: MIT
---

# Agent-Scale Source Control (Scion design principles)

Anthropic's Scion VCS, built when merges grew 2,500 → 30,000/day and git infrastructure (several hundred mirrors, ~600 PB/day naive traffic, 25M checkouts/day) collapsed. Full monorepo migration from git in 5 months; 7-person team; 200× smaller infra footprint; CI checkouts seconds instead of minutes (25% CI CPU win). Prior art: Piper, Sapling/Mononoke (Bonsai model).

## Core insight
Git was designed for decentralized, offline humans, but is deployed centralized — and at agent scale every client (agent, CI job) is online by definition. The properties that make git excellent offline actively block scaling. Redesign assuming the network is always there.

## Six design principles
1. **Clients are always online** — fetch data when needed instead of replicating the repo.
2. **Client–server asymmetry** — server does history, blame, commits, merges, rebases; client is a bounded object cache + working-copy layout + FS watcher. Thin client, little local data.
3. **Source control as a service** — every client query is also an API; jobs often need no checkout at all. This is what makes automated bisect/revert pipelines cheap.
4. **Everything horizontally scalable** — data distributed; no fully materialized copy anywhere (not even server-side); no packfiles → no repository maintenance; content-addressed objects → any server can cache without coordination.
5. **Commits cheap, incremental, lock-free** — commit cost scales with the change size, not repo size. Discourage refs: global state every server must agree on is the looming bottleneck (a ref move = one compare-and-swap on a single Spanner row).
6. **Working copy optional and sparse by design** — diff vs merge-base via API; virtualized checkouts materialize files only on read; many write workloads skip checkout entirely.

## Data model
- **Changeset = write-ahead log entry**: changed files relative to first parent + content-addressed blob pointers. Server-created, instantly visible everywhere; no pack negotiation, no locking, no ref dance.
- **Derived data (blame, path history, commit-graph skip lists, copy detection, path search) via one generic recursive mechanism**: value at a changeset = f(values at its parents). Per type, choose eager vs deferred; internals invisible to clients so indices can be reoptimized without protocol changes. Servers are big caches that compute derived data on demand and write back to Spanner.

## Negotiation + cache topology
- Client negotiates *only on trees/blobs it wants* (never advertises what it has): recursive missing-object requests; resumable; no multi-GB packfile responses; any cache can serve immutable objects → tiered caches: `scion-daemon` (per-node, snapshot-seeded, shared by colocated jobs) → `scion-cache` (regional, streams from memory in the on-disk format) → `scion-server` (authoritative, Spanner/cloud storage). Identical RPCs at every tier; strict tiering enforced to isolate failure domains. >99% hit rate; no long-lived state.

## Operating lessons (transfer beyond VCS)
- **Engineers say "no"**: agents violate system constraints to satisfy a pattern (brute-force reading the commit log instead of asking the review tool; over-engineered defensive validation prompted by adversarial review). Humans own design tradeoffs and intent; review the *intent* of changes, not every line.
- **"Superfan" agents**: one Claude per component, obsessively monitoring its telemetry in a Slack channel, catches subtle/novel issues traditional alerts miss.
- **Merge queues don't survive agent scale**: no global repo lock is feasible when thousands of changes land while tests run → move verification to post-merge/pre-deploy; concurrent conflicts are fixed by agents faster than humans can spot them.
- **Security in the monorepo**: directory-level permissions; review tooling expressing semantic approval constraints (comment-only vs sensitive logical changes) so scarce human review focuses on consequential diffs.
- **Scope honesty**: this only makes sense for enormous monorepos with agent swarms; the transferable contribution for everyone else is git-side — server-side RPCs, want-based negotiation, composable sparse/shallow.

**Activation**: source control design, monorepo scaling, agent-scale infrastructure, Scion, changeset, derived data, tiered cache, virtualized checkout, merge queue, content-addressed storage, dev infra for AI agents
