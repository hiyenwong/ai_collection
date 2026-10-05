---
name: arxiv-2610-02204v1-reconstruct-practice-go-real-guided-self-improveme
description: "arXiv paper: Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents"
tags: [arxiv, cs.RO, research]
created: 2026-10-04
utility: 0.85
---

# Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents

**arXiv ID:** 2610.02204v1
**Authors:** Yen-Jen Wang, Haozhe Jiang, Shuying Deng et al.
**Published:** 2026-10-01
**Category:** cs.RO
**Utility Score:** 0.85
**URL:** https://arxiv.org/abs/2610.02204v1

## Abstract

Building reliable robot capabilities across diverse tasks requires substantial human effort to develop and maintain skills, design rewards, and integrate perception with control. We present Reconstruct, Practice, Go Real (RPG), a framework for autonomous improvement of robot execution systems without updating model weights. RPG identifies manipulation capabilities in an offline dataset and constructs related practice tasks in simulation. During practice, RPG uses execution feedback, privileged simulator state, and available dataset videos to diagnose failures. It develops new reusable symbolic skills, refines existing skills, and revises the system prompt based on these diagnoses. Cross-task evaluation tests individual candidate changes and merged revisions before they are retained for reuse. At test time, a multimodal LLM uses the resulting system prompt and skill library to coordinate perception and robot control. On held-out initializations of 22 manipulation tasks, RPG improves task success from 28.6% after the first practice round to 95.0% after 15 rounds, outperforming all evaluated baselines, including ASPIRE (75.5%) and CaP-Agent0 powered by GPT-6 Astra Pro (60.0%). After a common calibration and hardware-adaptation procedure, the frozen system succeeds in all 30 physical trials, with ten trials on each of three tasks. Project Website: https://rpg-robot.github.io/

## Key Contributions

- Novel research in cs.RO
- Published on arXiv: 2026-10-01

## Related Work

See arXiv for citations and references.
