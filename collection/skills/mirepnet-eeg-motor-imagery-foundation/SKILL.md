---
name: mirepnet-eeg-motor-imagery-foundation
version: 1.0
date: 2026-04-22
paper: "2507.20254"
title: "MIRepNet: A Pipeline and Foundation Model for EEG-Based Motor Imagery Classification"
description: "First EEG foundation model tailored specifically for motor imagery (MI) paradigm. Includes neurophysiologically-informed channel template and hybrid pretraining combining self-supervised masked reconstruction with supervised MI classification."
category: eeg-bci
tags: [eeg, foundation-model, motor-imagery, bci, pretraining, channel-template, self-supervised]
---

# MIRepNet: EEG Foundation Model for Motor Imagery Classification

## Summary
First EEG foundation model specifically designed for the motor imagery (MI) BCI paradigm. Features a neurophysiologically-informed channel template adaptable to arbitrary electrode configurations, and hybrid pretraining strategy combining self-supervised and supervised learning.

## Core Methodology

### Problem
- General EEG foundation models overlook paradigm-specific neurophysiological distinctions
- In practice, BCI paradigm is determined before data acquisition
- MI-specific features are not captured by general-purpose EEG models

### MIRepNet Architecture
1. **Preprocessing Pipeline**: High-quality EEG preprocessing with neurophysiologically-informed channel template
2. **Channel Template**: Adaptable to EEG headsets with arbitrary electrode configurations
3. **Hybrid Pretraining**: 
   - Self-supervised masked token reconstruction
   - Supervised MI classification
4. **Rapid Adaptation**: Requires fewer than 30 trials per class for novel downstream MI tasks

### Key Features
- Paradigm-specific foundation model (motor imagery focused)
- Neurophysiologically-informed channel selection
- Hybrid SSL + supervised pretraining strategy
- Cross-dataset generalization

### Results
- State-of-the-art performance across five public MI datasets
- Significantly outperforms both specialized and generalized EEG models
- Rapid adaptation with minimal downstream data

## Applications
- Stroke rehabilitation BCIs
- Assistive robotics control
- Motor imagery decoding
- EEG foundation model for MI paradigm

## Activation Triggers
motor imagery, EEG, foundation model, BCI, MI classification, channel template, pretraining, self-supervised

## Activation Keywords

- "mirepnet-eeg-motor-imagery-foundation"
- "mirepnet eeg motor imagery foundation"
- "use mirepnet eeg motor imagery foundation"
- "mirepnet eeg motor imagery foundation help"
- "mirepnet eeg motor imagery foundation analysis"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify the user's specific question or task related to Mirepnet Eeg Motor Imagery Foundation
2. Gather relevant context from files or user input
3. Apply Mirepnet Eeg Motor Imagery Foundation methodology to address the request
4. Provide clear results with actionable insights

## Examples

### Basic usage
```
User: "Help me with mirepnet eeg motor imagery foundation"
→ Understand requirements → Apply methodology → Provide results
```

### Advanced usage
```
User: "I need detailed Mirepnet Eeg Motor Imagery Foundation assistance"
→ Clarify scope → Execute analysis → Present findings
```
