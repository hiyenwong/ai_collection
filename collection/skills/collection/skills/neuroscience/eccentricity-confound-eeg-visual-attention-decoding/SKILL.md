---
name: eccentricity-confound-eeg-visual-attention-decoding
description: EEG-based visual attention decoding methodology addressing eccentricity confounds in gaze-fixated neural tracking of motion in natural videos. BCI research for decoding visual attention from EEG signals.
tags: ["eeg", "brain-signal", "attention", "decoding", "bci", "visual-tracking", "eye-movement", "motion-tracking", "gaze-fixation"]
related_skills: []
arxiv: 2604.15223
authors: ["Yuanyuan Yao", "Celina Salamanca Gonzalez", "Simon Geirnaert", "Celine R. Gillebert", "Tinne Tuytelaars", "Alexander Bertrand"]
published: 2026-04-16
categories: [eess.SP]
---

# Eccentricity Confound in EEG-based Visual Attention Decoding

## Overview

This paper addresses a critical methodological issue in brain-computer interface (BCI) research: **whether neural tracking of visual motion in EEG genuinely reflects attention or is confounded by eye movement artifacts and stimulus eccentricity**.

**arXiv**: 2604.15223 | **Published**: April 2026

## Core Findings

1. **Neural tracking of object motion in natural videos works under gaze fixation** — confirming genuine neural processing, not just oculomotor artifacts
2. **Neural tracking strength under gaze fixation is predictive of attention** — validates the core assumption of attention decoding
3. **Significant eccentricity confound exists** — poorer neural tracking of motion at larger eccentricities (distance from fixation point)

## Methodology

### Experimental Design
- **Three tasks** manipulating object eccentricity and attention conditions
- Participants maintain **gaze fixation** (controls for eye movement artifacts)
- EEG recording during naturalistic video viewing

### Analysis Pipeline
1. **Correlation analysis** between object motion features and EEG responses
2. **Match-mismatch decoding** to quantify neural tracking quality
3. **Eccentricity-controlled analysis** — isolating genuine neural tracking from artifacts

### Key Variables
- **Independent**: Object eccentricity, attention condition
- **Dependent**: Neural tracking strength (correlation coefficient, decoding accuracy)
- **Control**: Gaze fixation (eliminates saccadic artifacts)

## Implications for BCI Systems

### What This Validates
- Previous free-viewing studies captured genuine neural processing
- Neural tracking strength IS a valid attention proxy

### What This Challenges
- Current decoding approaches that assume coupling strength reflects attention **alone**
- Must account for eccentricity effects in attention decoding algorithms

### Practical Recommendations
- **Calibrate for eccentricity** in attention decoding systems
- **Control for gaze position** in experimental design
- **Use fixation-based protocols** for clean neural tracking measurements

## Trigger Words
eeg, visual attention, neural tracking, bci, gaze fixation, motion decoding, eccentricity, eye movement artifacts
