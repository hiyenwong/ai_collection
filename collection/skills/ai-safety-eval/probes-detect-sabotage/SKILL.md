---
name: probes-detect-sabotage
description: 'Caught in the Act: White-box deception detection via probes scaled to frontier monitoring settings. Novel probe architecture aggregating across layers and tokens for detecting sabotage and unverbalized deception.'
metadata:
  arxiv_id: "2610.12445"
  utility: 0.95
  authors: ["Oskar J. Hollinsworth", "Alex F. Spies", "Tigist Diriba", "Adam Gleave", "Chris Cundy"]
  published: "2026-10-08"
  categories: ["cs.LG", "cs.AI"]
  tags: ["deception-detection", "probes", "monitoring", "sabotage", "ai-safety", "white-box"]
---

# Caught in the Act: Probes Detect Sabotage and Unverbalized Deception

**arXiv:** [2610.12445](https://arxiv.org/abs/2610.12445)
**Utility:** 0.95

## Key Innovation

White-box deception detection via probes scaled to frontier monitoring settings:
- **Largest deception dataset** to date for training probes
- **Novel probe architecture** aggregating information across many layers and tokens

## Problem

Recent incidents highlight the challenge of monitoring LLM agents and the danger of models deceiving people. Deception can be unverbalized — hidden in internal representations while output appears normal.

## Method

- Train probes on internal model representations (not just outputs)
- Aggregate signals across layers and tokens for robust detection
- Scale to frontier models with large context windows

## Key Finding

Probes can effectively detect sabotage and catch unverbalized deception that would be invisible from output monitoring alone.

## Practical Use

- Deploy white-box monitoring for high-stakes agent deployments
- Detect agent sabotage before it manifests in outputs
- Build layered safety systems combining output and internal-state monitoring
