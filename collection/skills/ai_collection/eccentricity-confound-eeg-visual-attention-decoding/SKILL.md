---
name: eccentricity-confound-eeg-visual-attention-decoding
description: EEG-based visual attention decoding methodology addressing eccentricity confound in gaze-fixated neural tracking of motion. Use when decoding visual attention from EEG signals during natural video viewing, controlling for eye movement artifacts and stimulus properties.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [eeg, visual-attention, decoding, brain-computer-interface, eccentricity, eye-tracking]
    source_paper: "Eccentricity Confound in EEG-based Visual Attention Decoding from Gaze-Fixated Neural Tracking of Motion in Natural Videos (arXiv:2604.15223v1)"
    published: "2026-04-16"
---

# EEG Visual Attention Decoding with Eccentricity Control

## Overview
Methodology for decoding visual attention from EEG signals during naturalistic video viewing, with explicit control for eccentricity confounds from eye movement artifacts and stimulus properties.

## Problem
Current methods assume stronger coupling between object motion and neural activity indicates higher attention, but this is confounded by:
- Eye movement artifacts related to visual eccentricity
- Stimulus properties that vary with position in visual field

## Core Methodology
1. **Eccentricity-aware preprocessing**: Control for position-dependent artifacts
2. **Motion-neural coupling analysis**: Measure neural tracking of object motion
3. **Attention decoding**: Isolate genuine attention signals from confounds

## Applications
- Brain-computer interfaces for gaze-free attention decoding
- Cognitive neuroscience of visual attention
- Naturalistic stimulus EEG analysis
- Eye-movement artifact mitigation

## Activation
- EEG visual attention decoding
- eccentricity confound control
- gaze-fixated neural tracking
- natural video EEG analysis
- motion-neural coupling
- eye movement artifact removal

## References
- Eccentricity Confound in EEG-based Visual Attention Decoding from Gaze-Fixated Neural Tracking of Motion in Natural Videos
- Authors: Yuanyuan Yao, Celina Salamanca Gonzalez, Simon Geirnaert, Celine R. Gillebert, Tinne Tuytelaars, Alexander Bertrand
- arXiv: [2604.15223v1](http://arxiv.org/abs/2604.15223v1)
- PDF: https://arxiv.org/pdf/2604.15223v1
