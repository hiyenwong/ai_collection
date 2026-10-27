---
name: stp-gui-spatially-aware-token-pruning
description: "Query-guided token pruning for Web-GUI agents: independent token-importance selection fragments local visual structures needed to recognize small GUI elements (buttons/icons/links); STP-GUI keeps fine-grained instruction-conditioned scoring but performs spatially coherent window-level selection, with a lightweight selector trained by policy learning over a frozen VLM. At 21% token retention preserves 77.7% performance, -31% latency, -57% FLOPs. Use for efficient VLM-based GUI agents."
category: ai_collection
trigger: GUI agent, token pruning, spatial coherence, window-level selection, screenshot efficiency, VLM agent, web agent, Android in the Wild, Online-Mind2Web, instruction-conditioned pruning, policy-learned selector
---

# STP-GUI: Spatially-Aware Token Pruning for Efficient Web-GUI Agents

Methodology from arXiv:2610.20390 (Wang, Zhou, Wang, Fu, Zhao et al.; 2026-10-14, cs.CV).

## The Diagnosis (why generic pruners fail on GUIs)

High-resolution screenshots + multi-turn histories → excessive visual tokens → heavy inference
overhead. Token pruning methods designed for **natural images** select tokens independently
by importance scores. But GUI understanding depends on **small elements** (buttons, icons,
hyperlinks) whose local visual structures get **fragmented** by independent selection — you
keep scattered pieces of a button but lose the button.

## The Fix: Score Fine, Select Spatial

STP-GUI separates scoring from selection:

1. **Fine-grained instruction-conditioned token scoring** — importance stays query-guided and
   per-token (preserves semantic grounding).
2. **Spatially coherent window-level selection** — pruning decisions are made over local
   windows so retained tokens keep contiguous local structure around small GUI elements.
3. **Lightweight selector trained via policy learning with the VLM backbone frozen** — the
   selector learns retention policies that maximize task success under token budgets, without
   touching the expensive backbone.

## Results (calibration anchors)

- Online-Mind2Web: at **21% token retention** preserves **77.7%** of full-token performance,
  **−31% inference latency, −57% FLOPs**.
- Android in the Wild: transfers to mobile GUI environments.

## Reusable Patterns

- **Decouple scoring granularity from selection granularity**: per-token (or per-patch)
  semantic scores + window/region-level keep decisions — applicable to any pruning task where
  the consumed structure is *local* (GUI elements, text lines, table cells, document layouts).
- **Frozen backbone + policy-trained lightweight selector**: when the expensive model cannot
  be retrained, train a cheap decision module against end-task reward instead of proxy losses.
- **Query-guided pruning for agents**: retention budgets should depend on the current
  instruction, not static saliency — different turns need different parts of the screenshot.

## When to Use

- Building efficient screenshot-based VLM agents (web, mobile, desktop GUI).
- Pruning visual tokens where output depends on small contiguous structures.
- Reducing multi-turn agent history cost (re-score old screenshots per current instruction).
