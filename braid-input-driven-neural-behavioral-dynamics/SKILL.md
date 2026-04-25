---
name: braid-input-driven-neural-behavioral-dynamics
version: 1.0
date: 2026-04-22
paper: "2509.18627"
title: "BRAID: Input-Driven Nonlinear Dynamical Modeling of Neural-Behavioral Data"
description: "BRAID deep learning framework that models nonlinear neural dynamics underlying behavior while explicitly incorporating external inputs. Disentangles intrinsic recurrent dynamics from input effects using forecasting objectives."
category: neural-dynamics
tags: [neural-dynamics, behavioral-modeling, recurrent-neural-network, input-driven, motor-cortex, disentanglement]
---

# BRAID: Input-Driven Nonlinear Dynamical Modeling of Neural-Behavioral Data

## Summary
Deep learning framework for modeling nonlinear neural dynamics underlying behavior while explicitly incorporating measured external inputs (sensory stimuli, upstream regions, neurostimulation). Disentangles intrinsic recurrent dynamics from input effects.

## Core Methodology

### Problem
- Neural populations are often modeled as autonomous dynamical systems
- External inputs (sensory stimuli, neurostimulation) shape population activity but are ignored
- Need to disentangle intrinsic dynamics from input-driven effects

### BRAID Framework
1. **Input-Driven RNN**: Incorporates measured external inputs into recurrent neural network model
2. **Forecasting Objective**: Includes prediction task to learn dynamics that generalize
3. **Multi-Stage Optimization**: Prioritizes learning of intrinsic dynamics related to behavior of interest
4. **Disentanglement**: Separates intrinsic recurrent dynamics from external input effects

### Key Components
- Input-driven recurrent neural network architecture
- Neural-behavioral multi-modal learning
- Behavioral relevance constraint on learned dynamics
- Forecasting-based intrinsic dynamics extraction

### Validation
- **Nonlinear simulations**: Accurately recovers shared intrinsic dynamics between neural and behavioral modalities
- **Motor cortex data**: More accurately fits neural-behavioral data by incorporating sensory stimuli
- **Forecasting**: Improves prediction of neural-behavioral data vs baseline methods

## Applications
- Motor cortical activity modeling during tasks
- Neural dynamics with sensory input decomposition
- Neurostimulation effect analysis
- Brain-behavior relationship modeling

## Activation Triggers
neural dynamics, behavioral modeling, input-driven, RNN, motor cortex, disentanglement, neural population, recurrent dynamics
