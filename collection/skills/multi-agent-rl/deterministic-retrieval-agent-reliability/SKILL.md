---
name: deterministic-retrieval-agent-reliability
description: Methodology from Anthropic's "Paving the way for agents in biology" (Jun 2026). Use when building LLM agents that must query structured scientific/enterprise databases reliably. Core pattern: wrap unreliable LLM API guessing behind a deterministic retrieval layer (exemplified by the gget virus tool for NCBI Virus) to lift accuracy from ~50% to ~100%. Also covers the "click tax" cost model and designing agent-friendly databases.
license: Complete terms in LICENSE.txt
---

# Deterministic Retrieval Layer for Agent Reliability

Methodology from Anthropic's "Paving the way for agents in biology" (Jun 8, 2026). Agents that call scientific/enterprise databases fail when they guess at opaque APIs. The fix: a thin deterministic retrieval layer that translates natural requests into exact queries.

## Core problem

- Frontier models + biology agents (Claude, Biomni, OpenAI's Edison) retrieved the correct virus from NCBI Virus only ~50% of the time when forced to use the API directly (and often <10% guessing IDs from memory).
- Root cause: APIs are designed for human point-and-click UIs, not for LLM tool use. The "click tax" — every interaction costs tokens/time — makes trial-and-error infeasible.

## The pattern: deterministic retrieval layer

- Anthropic built **gget virus**, a tool that sits between the model and NCBI Virus.
- It lets agents describe what they want in natural language; it deterministically resolves metadata (species, gene, accession) into the exact query the database needs.
- Result: **~100% retrieval accuracy** across Claude, Biomni (OSS), Edison (OpenAI), and GPT — from ~50% baseline. It's a general solution, not model-specific.

## "Click tax" framing

Every tool call / retry costs tokens and latency. Agents can't afford human-style exploration of bad UIs. Design tools so a single call resolves the intent deterministically; avoid multi-step guess-and-check against opaque endpoints.

## Design rules for agent-friendly databases/tools

1. Expose a natural-language → structured-query resolver (the deterministic layer).
2. Return stable, resolvable identifiers; don't require the agent to memorize IDs.
3. Make the common-path query a single deterministic call (no click tax loops).
4. Validate that accuracy reaches ~100% on a held-out set before shipping the agent.

## When to apply

Any agent that must pull from structured data sources (scientific DBs, CRM, inventory, internal APIs) where the model would otherwise hallucinate identifiers or fail at the API contract.

## Activation keywords

paving the way for agents in biology, deterministic retrieval layer, gget virus, NCBI Virus agent retrieval, click tax, agent-friendly database, LLM structured data retrieval, scientific agent reliability, tool design for agents, Anthropic biology agents 2026
