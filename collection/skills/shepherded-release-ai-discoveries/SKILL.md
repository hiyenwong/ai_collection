---
description: Use when releasing AI-generated scientific discoveries.
name: shepherded-release-ai-discoveries
version: 1.0
author: openai-research-cron-2026-10-27
license: MIT
metadata:
  hermes:
    tags: [shepherded-release, ai-discovery-governance, raw-research-data, lean-formalization, external-collaboration, release-strategy, verified-ai-math, openai]
    source: https://openai.com/index/building-scientific-understanding-with-academic-communities/
    published: 2026-10-27
---

# Shepherded Release of AI-Generated Scientific Discoveries

Methodology from OpenAI's "Working with academic communities to build scientific understanding" (Oct 27, 2026), demonstrated across three landmark results: local smoothing conjecture proved in all dimensions (implies Kakeya + Stein restriction), the Exponential Time Hypothesis refuted, and a rigorous existence proof for 4D interacting QFTs incl. QCD and a Standard Model completion (Yang–Mills existence as subproblem).

## Core Premise

Treat AI output as **raw research data**, not finished science. The bottleneck is no longer producing proofs/results — it is converting raw output into **scientific understanding** owned by the research community. Do that through external expert **shepherds** who organize working groups, not through unilateral publication.

## When to Use

- Your AI system produced a scientific result (proof, theorem, discovery) that a field must verify, absorb, and build on
- Designing disclosure policy for AI-generated claims with far-reaching consequences (e.g., refuting a widely-used conjecture)
- Structuring external academic collaboration without co-option of credit
- Any org needing a governance process for "drop a bombshell result, then what"

## Pipeline (5 stages)

1. **Produce + formalize** — natural-language writeup from the model AND an independent formalization (Lean). Ship them as twin artifacts. Verify before any engagement.
2. **Recruit a shepherd** — one recognized expert per result; ask them to recommend the release strategy rather than imposing one.
3. **Pick one of three strategies** (see below) per result, not per org.
4. **Constitute the working group** under the four principles.
5. **Fund absorption** — workshops/conferences via an independent foundation (OpenAI: $5M to Simons Foundation) so third parties can examine, explain, and extend.

## Three Release Strategies (spectrum of control transfer)

- **S1 Raw release** — publish the AI output openly; researchers self-organize to explain it. Best when the community already has organizing norms (the math result).
- **S2 Hybrid** — external collaboration group explains the result, AND raw output is public immediately for anyone to examine. Best when independent verification needs all artifacts (the ETH refutation: all raw data public + funded conference).
- **S3 Full deference** — external group decides whether/when/how to release AI artifacts, possibly writing up in their own voice first. Best when the result is long, complex, and community norms demand human mediation (the QFT existence proof).

Per-result variation is the point: same org, same day, three different strategies — delegated to each community's shepherds.

## Four Governance Principles

1. **Transparency** — the collaboration's existence is public; no NDAs; participants may discuss, share intermediates, publish.
2. **No Academic Credit** — the org claims no authorship credit for model-produced discoveries; stewarding a group ≠ having made the discovery.
3. **Recognition** — the group owns and is credited for the understanding, writeups, and materials it produces; it polices citation of prior work the result draws on.
4. **Independence** — participation voluntary and unpaid; conclusions are the members' own; neither side speaks for the other.

## Known Tradeoffs (state them explicitly)

- Choosing initial shepherds shapes who participates first and creates **information asymmetry** — acknowledge it and solicit feedback on broadening.
- S3 delays availability of raw artifacts (physics: produced Sep 9/Oct 16, held for group's own writeup).
- No-credit removes incentive contamination but complicates attribution of the *understanding* vs the *discovery* — the Recognition principle handles the former, not the latter.

## Evidence / Precedent

- Oct 2026 release: math result = S1 (paper + Lean on github.com/openai/math); ETH refutation = S2 (shepherds: Impagliazzo, Paturi, R. Williams; raw data public, conference funded); QCD/Yang–Mills = S3 (shepherds: Gross, Douglas, Jaffe, Klebanov, Nekrasov; artifacts withheld by their decision).
- Contrasts with the Oct 6, 2026 pure-S1 release ("Ten advances in mathematics"); the shepherded layer is the Oct 27 evolution after academic feedback.
