---
name: retrieved-not-read-evidence-use-failure
description: Use when auditing stale answers despite retrieved evidence.
category: ai_collection
arxiv_id: "2610.21731"
source_paper: "Retrieved but Not Read: Understanding Why Search-Augmented LLMs Fail to Use Available Evidence (Walters, Chen, Toni, Imperial College London, 2026)"
---

# Retrieved but Not Read — Evidence-Use Failure Audit for Search-Augmented LLMs

Use when auditing why a RAG/search-augmented LLM produces stale or unfaithful answers **even though correct evidence was retrieved**. From arXiv 2610.21731.

## Core Finding

Models frequently answer from search snippets without opening source pages ("snippet-only" episodes). Most stale answers and unfaithful citations concentrate in exactly those episodes. Even when retrieved evidence **does** influence internal predictions (visible in upper layers), the stale parametric value is **promoted but not suppressed**, and re-overtakes in final layers. Evidence use fails at two stages: (1) reading depth — the model never opens the page; (2) evidence competition — the retrieved value gains advantage but fails to displace the stale one.

## Benchmark Design Pattern (reusable)

**Post-cutoff temporal facts with dual values.** Build facts whose value changed after the model's training cutoff (paper: 225 facts, 6 domains — FDA labels 62, finance/SEC 65, sports 47, people 43, chemical 8; cutoff 2026-02-16). Each fact carries BOTH an outdated and a current value, so endorsement of the stale claim is graded against its true twin deterministically.

Key design rules:
- Facts extracted from primary sources (SEC filings, FDA labels, Wikipedia/Wikidata) via a deterministic, regenerable pipeline; the one model-assisted step manually reviewed for every fact.
- Include control facts that did NOT change across the cutoff → gives each model's unfaithful-citation **floor**.
- Estimate closed-book leakage: run the strongest model with no search (paper: 23.3% on open questions) to separate "knows" from "retrieves".

**Frozen retrieval protocol.** All models receive the identical 10-result search menu (built once from Brave). Ground-truth page keeps its rank if organically in top-10; otherwise inserted at a seeded position → always reachable. Same search/open-page/find tools for every model, temperature 0, pinned providers. This converts deployed-web-search behavior into a controlled experiment while preserving agentic navigation.

## Measures (the audit metric set)

1. **Reading depth** from tool traces: `snippet-only` (opens no page) / `opened-not-cited` / `integrated` (cites a page it opened).
2. **Accuracy**: share correct among {correct, stale, another-value}; abstentions excluded.
3. **Unfaithful citation** (distinct from correctness): the cited page **contradicts the value the reply asserts**. Scored per graded answer; on-claim rates count only citations attached to the claim under test.

## Grading Rigor Pattern

- Every prompt states the date and ends with a required **answer line** allowing `CAN NOT VERIFY` → deterministic grading across 30,000+ replies. (Pre-registered check: the answer-line contract lowered a deployed model's false endorsement by 17.5 points — deployed failure rates are therefore LOWER BOUNDS.)
- **LLM marker asymmetry**: an LLM grader may only assign PASSING faithfulness outcomes, each backed by a verbatim span of the archived page; every adverse label requires human confirmation. This prevents marker-driven false accusations.
- **Carry-over test**: compute odds ratios for per-fact failures between deployed search and frozen retrieval across models. Shared failures (paper: OR 1.84–6.46 on 7/9 failure types, negative control OR 1.05) show the phenomenon is model-general, not one deployment's artifact.

## Key Quantitative Results

- Deployed proprietary model: 53.6% of search episodes answered from snippets alone (93.5% accuracy).
- Frozen retrieval: snippet-share ranges 9.9%–76.0% across 7 open-weight configurations — reading depth is a model property, not a retrieval property.
- Pooled: snippet-only episodes stale **6.4%** vs integrated **1.3%**; unfaithful citations **6.4%** vs **2.3%**. Sports worst: snippet-only stale 20.2% vs 2.1% integrated.
- **Association**: 81.8% (27/33) of on-claim citations are unfaithful when the answer is stale, vs 0.9% (6/694) when current. Stale answers and unfaithful citations are the same failure viewed from two sides.
- Search itself helps everywhere: +27–42 points claim-check accuracy.

## Mechanistic Probe Pattern

For facts with short answers (sports club transfers), build paired prompts: fact sheet asserting the outdated club, ± the player's current Wikipedia page. Read out both candidate answers at the answer slot across layers via **logit lens** and **Jacobian lens** (project intermediate states onto token-level logits; score = max logit over first tokens of each name).

- Success: retrieved club gains advantage in upper layers and keeps it.
- Failure: retrieved club ranks ABOVE the stale club early in upper layers (evidence IS internally used — ∆new > 0, p ≤ 0.04) but stale overtakes in final layers. Failure = **insufficient suppression**, not absent promotion.

## Interventions That Work (ranked)

1. **Provide the source page directly in the prompt** (skip the search menu): gemma-4-31b stale endorsements 14/50 → 0/50; gpt-oss-20b 11/47 → 1/50. Strongest known fix.
2. **Restate the full question after each opened page** (the agentic loop buries the question before everything retrieved): recovers 26.1% (41/157) of failed fact-sheet checks. Cheap, deployment-compatible.
3. Snippet-only behavior itself is the failure locus: any mechanism forcing page-open before citation attacks both stale answers and unfaithful citations at once.

## When Applying This Skill

- Diagnosing "model answered outdated despite correct retrieval" reports.
- Designing RAG agent evaluation: include reading-depth tracking, dual-value temporal facts, citation-faithfulness grading (cite-vs-asserted-value), and control-fact floors.
- Post-hoc fixes: evidence re-injection and question-restating, before retraining.
- Caveat: domain-dependent — answer-in-first-line facts (sports) fail most; long-label reasoning facts (FDA) fail differently. Single-proprietary-model deployed results are lower bounds.

## Related

- `llm-rater-multiplicity-audit` — same marker-asymmetry rigor family.
- `availability-contract-earnings-nlp` — label-clock validity audits.
- `recursive-evidence-replay-reasoning` — complementary evidence-handling harness.
