---
name: dynamic-sampling-non-stationary-spontaneous-activity
title: Dynamic sampling of non-stationary spontaneous activity in dissociated neuronal networks
arxiv_id: 2607.24269
date: 2026-07-27
authors:
  - Kazushi Takehana
  - Dai Akita  
  - Hirokazu Takahashi
domain: neuroscience
description: Adaptive electrode-selection method using discounted Poisson-Gamma model with Thompson sampling for tracking non-stationary spontaneous activity during long-term HD-MEA recordings under fixed channel budget constraints.
tags:
  - hd-mea
  - adaptive electrode selection
  - thompson sampling
  - non-stationary neural activity
  - bayesian optimization
---

# Dynamic Sampling of Non-Stationary Spontaneous Activity in Dissociated Neuronal Networks

## Overview
This methodology develops and evaluates an adaptive electrode-selection method for tracking non-stationary spontaneous activity during long-term high-density microelectrode array (HD-MEA) recordings under a fixed channel budget constraint.

## Core Methodology

### Problem Formulation
- **Objective**: Track evolving neural activity patterns over extended recording periods with limited readout channels
- **Challenge**: Neural activity is non-stationary, with electrode activity levels changing substantially over time (47.8% turnover at 34 hours)
- **Constraint**: Fixed channel budget (e.g., 100 electrodes from 529 candidates)

### Technical Approach
- **Sequential subset-selection**: Formulate electrode allocation as a sequential decision problem
- **Discounted Poisson-Gamma model**: Bayesian framework for modeling spike count dynamics with temporal discounting
- **Thompson sampling**: Uncertainty-aware exploration strategy for adaptive electrode selection
- **Real-time updates**: Continuously update electrode-specific activity estimates from observed spike counts

### Implementation Details
- **Offline evaluation**: Tested on nine 34-hour HD-MEA recordings with 100/529 electrode selection
- **Online validation**: Demonstrated in real-time recording with 1,024 routed electrodes
- **Performance metric**: Fraction of spikes captured compared to oracle selector

## Key Results

### Performance Gains
- **17.2 percentage point improvement** over static electrode selection at final time point
- **Optimal spike capture**: Bayesian method captured the largest fraction of available spikes among tested strategies
- **Dynamic adaptation**: Successfully tracked substantial changes in active electrode sets over time

### Practical Applications
- **Synchronized burst detection**: Captured first synchronized burst in online recording
- **Trajectory analysis**: Supported center-of-activity trajectory analysis
- **Long-term monitoring**: Enables efficient recording over extended periods despite non-stationarity

## Significance and Applications

### Scientific Impact
- **Adaptive sensing**: Provides foundation for uncertainty-aware exploration in neural recording
- **Resource efficiency**: Maximizes information capture under fixed hardware constraints
- **Temporal dynamics**: Addresses critical challenge of non-stationary neural activity in long-term experiments

### Use Cases
- **Chronic neural interfaces**: Adaptive electrode selection for brain-computer interfaces
- **Network plasticity studies**: Tracking evolving connectivity patterns over days/weeks
- **Drug screening**: Monitoring long-term effects of compounds on network activity
- **Developmental neuroscience**: Observing maturation of neural circuits in culture

## Activation Triggers
Use when:
- Working with HD-MEA recordings under channel budget constraints
- Need to track non-stationary neural activity over extended periods
- Implementing adaptive sensing strategies for neural interfaces
- Designing experiments requiring long-term monitoring of dissociated networks
- Optimizing electrode selection for maximum information capture

## Keywords
adaptive electrode selection, HD-MEA, Thompson sampling, non-stationary neural activity, Bayesian optimization, dynamic sampling, spontaneous activity, dissociated neuronal networks, channel budget constraints, temporal discounting