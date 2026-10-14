---
name: arxiv-2610-16921-time-window-optimization-for-motor-imagery-classification-vi
description: 'Time Window Optimization for Motor Imagery Classification via Temporal Structure (arXiv: 2610.16921)'
metadata:
  {
    "arxiv_id": "2610.16921",
    "utility": 1.0,
    "title": "Time Window Optimization for Motor Imagery Classification via Temporal Structure Embedded Reinforcement Learning",
    "authors": "",
    "url": "https://arxiv.org/abs/2610.16921"
  }
---

# Time Window Optimization for Motor Imagery Classification via Temporal Structure Embedded Reinforcement Learning

**arXiv ID:** 2610.16921
**URL:** https://arxiv.org/abs/2610.16921
**Utility Score:** 1.00

## Abstract

Online motor imagery-based brain-computer interfaces (MI-BCIs) typically decode continuous EEG using fixed-length sliding windows that may be misaligned with neural events. Existing window optimization methods often evaluate windows independently, overlooking temporal dependencies and potentially producing fragmented or physiologically implausible selections. We propose Temporal Structure Embedded Reinforcement Learning (TSE-RL), a framework that incorporates prior knowledge of MI event structure into a constrained Markov decision process for adaptive window optimization. First, TSE-RL assigns each window an explicit semantic role through Discard, Onset, Sustain, or Offset actions, extending binary retain/discard decisions to event-level alignment. Second, a finite-state machine masks invalid actions to enforce the temporal order of MI phases and promote physiologically plausible window sequences. Third, a Transformer-based history encoder captures dependencies across windows, improving training stability and computational efficiency compared with recurrent architectures. TSE-RL is plug-and-play and can be integrated with diverse MI classifiers. Experiments on multiple benchmark datasets demonstrate consistent improvements in decoding performance in both cross-session and cross-subject settings. Visualization analyses further suggest that the learned window selection policy aligns with neurophysiological principles.

## Key Topics

reinforcement learning, brain, neural, eeg, bci, rag

## Usage

This skill references the paper's concepts, methodologies, and findings for use in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.16921
