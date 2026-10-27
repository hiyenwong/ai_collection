---
name: agentic-genome-mining-discovery
category: ai_collection
description: Use when mining genomes for novel enzyme systems.
version: "1.0.0"
source: https://www.anthropic.com/research/claude-discovers-novel-enzyme-system
source_title: "Claude discovers a novel enzyme system with CRISPR-like repeats"
author: anthropic-cron-2026-10-27
license: MIT
---

# Agentic Genome Mining for Novel Biological Systems

Anthropic life-sciences lab methodology. Claude autonomously discovered ART (array-associated reverse transcriptases): a novel phage enzyme system with a CRISPR-like repeat array, from ~950 agents, 21 hours, 210M tokens — only high-level direction from scientists. Funnel: 200,000+ RTs gathered → 3,500 new candidate systems → 20 compelling candidates → human-readable reports → 1 lab-tested discovery. Prior RT was known; Claude was first to notice the system-defining features (repeat array + accessory protein).

## The discovery pipeline (survey → validate → anomaly → report → triage → lab)
1. **Survey a protein family** from sequence databases.
2. **Reproduce established results first** — Claude re-derives known findings from public data to check its own methods before trusting its novel claims.
3. **Hunt for what fits no described system**: family members or genomic neighbors that match no characterized system.
4. **Write a human-readable report per candidate**: proposed function + supporting evidence. Anomalies count — the discovery came from an agent noticing a tandem repeat array "by eye" in raw DNA next to an odd-looking RT, then counting repeats, measuring spacing, comparing layout to known systems, searching literature for prior reports.
5. **Self-critique triage**: Claude critically evaluates its own candidates in follow-up — most are eliminated here. A campaign may end with one candidate or none.
6. **Lab validation** (humans, BSL-1/2): express, characterize biochemically/structurally, with Claude interpreting the data. Discovery reports are filed for human review; the agent never tests its own hypotheses.

## Scale pattern
- Parallel agent harness coordinating many Claude sessions (Claude Science + Claude Code are sufficient tools); weeks-to-months of expert analysis compressed to ~a day.
- Wide funnel (10^5 sequences → 10^3 candidates → 10^1 reports) with machine-generated reports as the hand-off artifact to humans.

## Hypotheses as objects of study (the meta-method)
Because agents produce hundreds-to-thousands of candidate reports per campaign, the *set of hypotheses itself* becomes data: study what distinguishes worth-testing proposals from set-aside ones, then feed those lessons back into the campaign instructions — distilling the team's scientific taste into prompts.

## Transfer
- Same loop applies beyond genomics: literature-grounded survey → method validation on knowns → anomaly search in uncharacterized space → evidence-carrying reports → adversarial self-triage → human lab gate.
- Publish early even without function established (pre-print + technical report), with the honest caveat that function remains unknown.

**Activation**: genome mining, uncharacterized protein family, reverse transcriptase, CRISPR-like array, ART, hypothesis generation at scale, scientific taste distillation, agentic biology discovery, literature reproduction check, anomaly detection in sequences
