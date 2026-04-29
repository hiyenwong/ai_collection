---
name: information-theoretic-neural-code-experiment-design
version: 1.0
date: 2026-04-22
paper: "2603.01387"
title: "An Information-Theoretic Framework For Optimizing Experimental Design To Distinguish Probabilistic Neural Codes"
description: "Information-theoretic framework for optimizing task stimulus distributions to distinguish between likelihood coding (PPC) and posterior coding (neural sampling) hypotheses in sensory neural populations using the information gap metric."
category: neural-coding
tags: [information-theory, neural-coding, bayesian-brain, experimental-design, probabilistic-population-code, neural-sampling, KL-divergence]
---

# Information-Theoretic Framework for Optimizing Experimental Design to Distinguish Probabilistic Neural Codes

## Summary
Framework for optimizing experimental task design to distinguish between two competing probabilistic neural coding hypotheses: likelihood encoding (PPC) vs posterior encoding (neural sampling). Uses information-theoretic "information gap" metric to maximize discriminative power.

## Core Methodology

### Problem
- Bayesian brain hypothesis: brain performs Bayesian computations under uncertainty
- Two competing hypotheses for neural encoding:
  - **Likelihood encoding** (Probabilistic Population Codes / PPC): early sensory populations encode the likelihood function
  - **Posterior encoding** (Neural Sampling Codes): populations encode the posterior distribution
- Key distinction: whether stimulus priors modulate neural responses
- Experimentally differentiating these hypotheses is challenging

### Information Gap Framework
1. **Metric**: Information gap = expected performance difference when likelihood vs posterior decoders are applied
2. **Computation**: Kullback-Leibler divergence between true posterior and task-marginalized surrogate posterior
3. **Optimization**: Maximize information gap to find stimulus distributions that optimally differentiate hypotheses

### Algorithm
1. Define competing probabilistic coding hypotheses (PPC vs neural sampling)
2. Compute information gap under candidate stimulus distributions
3. Optimize stimulus distribution to maximize information gap
4. Validate via decoder performance simulations

### Key Results
- Information gap accurately predicts decoder performance differences across diverse task settings
- Maximizing information gap yields stimulus distributions that optimally differentiate coding hypotheses
- Enables principled, theory-driven experimental designs

## Applications
- Designing neurophysiology experiments to test neural coding hypotheses
- Probabilistic population coding analysis
- Neural sampling model validation
- Sensory uncertainty representation studies

## Activation Triggers
neural coding, probabilistic population code, neural sampling, Bayesian brain, information theory, KL divergence, experimental design, likelihood vs posterior, uncertainty coding
