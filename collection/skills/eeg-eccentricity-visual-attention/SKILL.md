---
name: eeg-eccentricity-visual-attention
description: "EEG-based visual attention decoding methodology addressing the eccentricity confound in gaze-fixated neural tracking. Use when decoding visual attention from EEG during naturalistic video viewing, designing BCI attention decoding systems, or interpreting neural tracking results. Critical finding: neural tracking strength is confounded by visual eccentricity. Trigger keywords: EEG visual attention, eccentricity confound, neural tracking, gaze fixation, BCI attention decoding, naturalistic video, motion tracking, match-mismatch decoding."
---

# EEG Visual Attention Decoding with Eccentricity Control

## Key Finding (arXiv 2604.15223v1, April 2026)

Visual eccentricity (distance from fixation point) significantly confounds neural tracking of object motion in EEG. Current attention decoding methods that assume coupling strength reflects attention alone are flawed — eccentricity must be controlled.

## Three Key Conclusions

1. **Neural tracking of object motion in natural videos works under gaze fixation** — validates the paradigm
2. **Neural tracking strength under gaze fixation is predictive of attention** — confirms BCI utility
3. **Significant eccentricity confound exists** — poorer neural tracking at larger eccentricities

## Problem

Previous free-viewing studies couldn't distinguish whether neural tracking reflected genuine attention or oculomotor artifacts (eye movements toward attended objects). This study controls eye movements via gaze fixation and shows the effect is genuine neural processing.

## Experimental Design

- **Three tasks** manipulating object eccentricity and attention conditions
- **Gaze fixation maintained** throughout (no eye movement artifacts)
- **EEG recording** during naturalistic video viewing
- **Correlation analysis** and **match-mismatch decoding**

## Methodology

### Neural Tracking Analysis
1. Present naturalistic video with objects at different eccentricities
2. Record EEG while participant maintains gaze fixation
3. Compute temporal response function (TRF) for object motion
4. Correlation between predicted and actual EEG = neural tracking strength

### Match-Mismatch Decoding
1. Build encoding model from EEG → attended stimulus
2. Test: can model correctly identify which of two stimuli was attended?
3. Accuracy above chance = attention decoding

### Eccentricity Analysis
- Compare neural tracking strength across eccentricity levels
- Control for attention condition
- Isolate eccentricity effect from attention effect

## Implications for BCI

1. **Decoding models must account for eccentricity** — otherwise attention estimates are biased
2. **Free-viewing results are genuine neural processing** — not just eye movement artifacts
3. **Fixation-controlled paradigms** provide cleaner attention signals
4. **Eccentricity correction** needed for real-world BCI applications

## Activation Keywords

- EEG visual attention
- eccentricity confound
- neural tracking
- gaze fixation
- BCI attention decoding
- naturalistic video EEG
- motion tracking EEG
- match-mismatch decoding
- temporal response function
- attention decoding


## Tools Used

- `read` - 读取技能文档
- `write` - 创建输出
- `exec` - 执行相关命令


## Instructions for Agents

1. 理解技能的核心方法论
2. 根据用户问题提供针对性回答
3. 遵循最佳实践


## Examples

### Example 1: 基本查询

**User:** 请解释 Eeg Eccentricity Visual Attention

**Agent:** Eeg Eccentricity Visual Attention 是关于...
