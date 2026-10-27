---
name: agentic-binder-design-campaign
category: ai_collection
description: Use when running agentic de novo protein binder design.
version: "1.0.0"
source: https://www.anthropic.com/research/claude-scorpion-toxin-binder-design
source_title: "How Claude designed protein binders against scorpion neurotoxins"
author: anthropic-cron-2026-10-27
license: MIT
---

# Agentic De Novo Binder Design Campaign

Anthropic's scorpion-neurotoxin minibinder campaign: one initial prompt + four follow-ups, 64 hours, ~10k GPU hours → 318,484 designs from 12 design tools, 553,052 co-folded design–toxin pairs screened, 180 selected (+31 added) → CROs synthesized/tested 211 → 17 binders (11/60 single-toxin = 18%, consistent with typical campaigns). Strongest (Cn2-B1/B2) single-digit nM. All 211 designs + data released.

## Campaign structure (who decides what)
- **Prompt defines**: targets, allowed design/folding tools, novelty rules, scoring and filtering criteria.
- **Agent autonomously decides**: structures from PDB/AFDB, 5 hotspots per toxin, quality thresholds, how much to lean on each tool, multi-toxin strategies, final selection. This division — humans own the rules of the game, the agent owns judgment within them — is the reusable pattern.

## Target selection template
- Pick targets spanning a hard generalization axis: 5 neurotoxins (Cn2, Ts1, AaH I, AaH II, LqhIII) across 4 regions; shared fold but only 26–62% sequence identity; aim binders at the channel-binding site of each toxin.
- Escalating difficulty ladder: single-toxin → β-family → α-family → all-five universal cocktail binder.

## Validation protocol (dual-lab, strict criteria)
- Two independent CROs, complementary expression formats: cell-free vs mammalian Fc-fusion.
- SPR sensorgrams → K_D per replicate at both labs.
- **Binder criteria (all required)**: hit at BOTH labs, binding in every replicate, K_D ≤ 1 µM, and no off-target signal vs CLEC12A (stickiness control).
- Mechanistic follow-up: competition experiment against a known neutralizing antibody (LR) — binders competing for the same epitope suggest neutralization likelihood without animal tests.

## Honest negative results
- **All multitoxin binders failed** (0 met criteria against more than one toxin). Plausible causes left open: prompting, design-tool limits, or biological infeasibility of one-binder-many-toxins.
- Binding ≠ neutralization: no in vitro (patch-clamp) or in vivo tests; recombinant toxins only, not venom-purified. "Binding is no longer the bottleneck" — the drug-development pipeline beyond binding is.
- Compute honesty footnote: a simplified single-agent, single-GPU, 24h prompt reached comparable *in silico* scores.

## Reuse checklist
1. Write the campaign prompt as rules (targets, tools, novelty, scoring, filtering) — not procedures.
2. Let the agent choose structures/hotspots/thresholds; intervene only via follow-up prompts.
3. Budget: order 10^5 designs, co-fold ~2×10^5+ pairs, submit O(10^2) to synthesis.
4. Always include an unrelated-protein stickiness control and dual-expression-format testing.
5. Publish designs + binding data as a field resource, including the failures.
6. Applicability beyond neglected-disease antivenoms: any target with a structure — "designing a binder against almost any target no longer seems unrealistic."

**Activation**: de novo protein design, minibinder, binder design campaign, scorpion toxin, antivenom, hotspot selection, SPR, dual-lab validation, multitoxin binder, neglected tropical disease, drug discovery acceleration
