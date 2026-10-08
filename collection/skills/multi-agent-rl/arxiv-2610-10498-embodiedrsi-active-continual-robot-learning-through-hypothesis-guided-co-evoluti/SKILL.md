---
name: arxiv-2610-10498-embodiedrsi-active-continual-robot-learning-through-hypothesis-guided-co-evoluti
description: 'EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution (arXiv: 2610.10498)'
metadata:
  {
    "arxiv_id": "2610.10498",
    "utility": 1.0,
    "title": "EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution",
    "authors": "Python Song, Zhixuan Liang, Kelsey Fu, Mengdi Wang, Junfeng Yang...",
    "url": "https://arxiv.org/abs/2610.10498v1",
    "categories": ["cs.AI"],
    "published": "2026-10-07"
  }
---

# EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution

**arXiv ID:** 2610.10498
**Authors:** Python Song, Zhixuan Liang, Kelsey Fu, Mengdi Wang, Junfeng Yang...
**URL:** https://arxiv.org/abs/2610.10498v1
**Utility Score:** 1.00
**Published:** 2026-10-07
**Categories:** cs.AI

## Summary

Robot foundation models provide strong visuomotor control, yet their performance can degrade when object positions or task instructions change. Further improvements often require post-training on substantial robot data, which can be costly to collect through methods such as teleoperation. Agentic harnesses can adapt around the model, but current self-evolving harnesses use robot trials inefficiently when deciding which code and skill changes to pursue. We introduce EmbodiedRSI, a self-evolving agentic harness that autonomously decides where to explore next and turns the resulting physical interaction into improved code and skills. EmbodiedRSI realizes this through a Fast-Slow Dual-System Architecture, in which competing code and skill hypotheses are maintained in a Hypothesis Graph. Value-of-Information Experiment Selection chooses physical experiments that can distinguish these hypotheses. Their outcomes guide Code-Skill Co-Evolution. The Slow System builds Hierarchical Memory, and Reward-Grounded Memory Learning selects effective memory according to their value for later Fast-System improvement. On RoboCasa365, EmbodiedRSI reaches 77.0% overall success and 71.3% on Composite-Unseen, compared with 40.1% for the best baseline. EmbodiedRSI also reaches 86.8% overall success on LIBERO-Pro. Beyond benchmark performance, EmbodiedRSI transfers zero-shot to real-world robot, achieving 71.3% overall success across multiple challenging tasks.

## Usage

This skill was automatically generated from the arXiv paper. It can be used to reference the paper's concepts, methodologies, or findings in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.10498v1
