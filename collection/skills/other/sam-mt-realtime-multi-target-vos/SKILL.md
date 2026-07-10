---
name: sam-mt-realtime-multi-target-vos
category: computer-vision
tags: [vision, video-segmentation, sam2, real-time, multi-target, efficiency]
source: arXiv:2607.08688v1
authors: Ruiqi Shen, Chang Liu, Henghui Ding
date: 2026-07-09
---

# SAM-MT: Real-Time Interactive Multi-Target Video Segmentation

Decouples VOS latency from target count for real-time multi-target video segmentation.

## Problem

Multi-target VOS typically replicates single-target processing per object, causing FPS to drop and latency to grow unbounded with target count.

## Solution

Transform SAM2 into a real-time multi-target interactive framework using:
1. **Explicit queries** to represent different individual targets
2. **Shared representation** for global context (processed once)
3. **Decoupled masked attention** to keep individual identities distinct from cross-target interference
4. **Sparse memory** for stable temporal evolution
5. Specialized strategies for occlusion handling and overlap prevention

## Key Results

- >36 FPS for 10 targets (on par with single-target baselines)
- Successfully decouples latency from number of targets
- Maintains SAM2's robust video segmentation performance

## Implementation Pattern

1. Single backbone pass for global context (shared)
2. Per-target query embeddings for identity
3. Decoupled attention: each target attends to global context independently
4. Sparse memory bank: only store keyframes, not all frames
5. Overlap prevention: post-processing to handle overlapping masks
6. Occlusion handling: track target visibility per frame

## Pitfalls

- Identity switching: explicit queries must be maintained across frames
- Memory management: sparse memory requires careful keyframe selection
- Overlap resolution: when targets intersect, need deterministic resolution

## Verification

- Measure FPS vs target count (should be flat, not linear)
- Check segmentation quality (mAP/IoU) matches single-target baseline
- Verify identity consistency across occlusions
