---
name: vanillasort-spike-sorting
description: Use when spike sorting with noisy auto-generated labels.
version: "1.0.0"
source: https://arxiv.org/abs/2609.22322
source_title: "Spike Sorting with VanillaSort"
authors: "Zishuo Feng, Feng Cao"
published: 2026-09-15
categories: q-bio.NC
trigger_words:
  - spike sorting
  - spike detection
  - noisy labels
  - positive-bag loss
  - visibility-aware masking
  - template-guided clustering
  - waveform consistency
  - electrophysiology
  - Hybrid Janelia
---

# Spike Sorting with VanillaSort

## Overview

**arXiv 2609.22322** (Feng & Cao — 2026-09-15). A spike-sorting pipeline that **learns from imperfect, algorithmically generated labels** on real recordings — solving the core weakness of supervised detectors trained on noisy ground truth. Two stages: **VanillaDet** (multichannel detection) + **VanillaCluster** (spatially augmented, template-guided clustering).

## Core Methodology

### 1. VanillaDet — Learning Detection from Noisy Labels
Four components that convert noisy auto-generated labels into reliable supervision:
- **Visibility-aware masking**: only train on channels/time-regions where the label generator is trustworthy — mask loss where labels are unreliable.
- **Truncated Gaussian targets**: regression targets are Gaussian peaks **truncated** to avoid overconfident supervision at ambiguous event boundaries.
- **Temporally tolerant positive-bag loss**: multiple time bins within ±tolerance form a positive bag — any bin firing counts as correct (multiple-instance learning against timing jitter in labels).
- **Conditional event-SNR gating**: post-hoc filter that drops detected events below an SNR threshold, conditioned on local noise estimate.

### 2. VanillaCluster — Template-Guided Clustering
- **HuiduRep embeddings + relative-amplitude features** → Gaussian mixture clustering.
- **Cross-fitted waveform templates**: templates built only from selected **core events** (high-confidence), then assignments refined by template matching — waveforms must be consistent with their assigned unit.
- Cross-fitting avoids self-confirmation: template for cluster A never built from the events it will reassign.

### 3. Results
- Hybrid Janelia benchmark: detection accuracy **+2 pp (static) / +3 pp (drift)** over SimSort.
- Full pipeline beats HuiduRep baselines on sorting metrics.
- Robustness to electrode **drift** is a first-class evaluation axis.

## Reusable Patterns

1. **Noisy-label training quadruple**: visibility masking + truncated targets + positive-bag tolerance + SNR gating — general recipe for ANY detector trained on algorithmically generated labels (not just spikes).
2. **Cross-fitted templates**: build cluster prototypes from held-out core events only — prevents template self-confirmation loops in any iterative clustering.
3. **Waveform/template consistency as a constraint**: assignment must be consistent with a physical signature (waveform shape) — applicable to any event-clustering with a physical generative model.
4. **Drift as evaluation axis**: evaluate pipelines separately on static vs drift subsets — aggregate metrics hide drift failures.

## Activation
- Training spike/neural-event detectors on real recordings with auto-generated labels
- Clustering waveform events with template consistency refinement
- Any detection task where ground truth is algorithmically generated (noisy, incomplete)
- Benchmarking electrophysiology pipelines under electrode drift

## Pitfalls
- **Do not train on all label positions** — without visibility masking, noisy-boundary labels corrupt the detector.
- Positive-bag tolerance trades temporal precision for recall; if downstream analysis needs sub-ms timing, tighten the bag width.
- GMM clustering assumes roughly unimodal unit clusters — heavily overlapping units need the template-refinement pass, not just embeddings.
- Results are on Hybrid Janelia (dense multichannel probes); performance on tetrode/low-channel-count data unverified.

## Source
- arXiv: [2609.22322](https://arxiv.org/abs/2609.22322)
- Imported to kg.db entities 9702, linked to 8 neuroscience papers via kg_relations
