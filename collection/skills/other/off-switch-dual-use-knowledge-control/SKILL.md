---
name: off-switch-dual-use-knowledge-control
description: "Off switch for dual-use knowledge using GRAM methodology."
metadata:
  title: "An off switch for dual-use knowledge in AI models"
  date: "Jul 8, 2026"
  authors: "Anthropic Research Team"
  category: "Alignment"
  url: "https://www.anthropic.com/research/off-switch-dual-use"
license: Complete terms in LICENSE.txt
---

# Off Switch for Dual-Use Knowledge Control

## Overview

This skill implements the Gradient-Routed Auxiliary Modules (GRAM) methodology from Anthropic's research on controlling dual-use knowledge in AI models. The approach provides an "off switch" that can selectively disable harmful capabilities while preserving beneficial ones.

## Core Methodology

The GRAM methodology works by:

1. **Auxiliary Modules**: Adding specialized auxiliary modules to the model architecture that handle specific dual-use capabilities
2. **Gradient Routing**: During training, gradients are selectively routed through or around these auxiliary modules based on whether the capability should be active or disabled
3. **Selective Disable**: At inference time, the auxiliary modules can be disabled to turn off the dual-use capability without affecting other model functions

## Implementation Steps

### Step 1: Identify Dual-Use Capabilities
- Analyze model capabilities to identify those with potential dual-use applications
- Categorize capabilities by risk level and potential harm

### Step 2: Design Auxiliary Modules
- Create specialized modules for each identified dual-use capability
- Ensure modules are modular and can be independently controlled
- Design interfaces that allow seamless integration with the main model

### Step 3: Implement Gradient Routing
- Modify training procedure to include gradient routing logic
- Implement mechanisms to selectively enable/disable gradient flow to auxiliary modules
- Ensure routing decisions are consistent with safety objectives

### Step 4: Training with GRAM
- Train the model with auxiliary modules and gradient routing enabled
- Validate that disabling modules effectively removes dual-use capabilities
- Verify that beneficial capabilities remain intact when modules are disabled

### Step 5: Deployment and Monitoring
- Deploy model with auxiliary modules that can be toggled on/off
- Implement monitoring to detect attempts to bypass the off switch
- Establish procedures for updating auxiliary modules as new risks emerge

## Key Benefits

- **Selective Control**: Can disable specific harmful capabilities without affecting overall model performance
- **Training Efficiency**: Leverages existing training infrastructure with minimal modifications
- **Scalability**: Can be applied to multiple dual-use capabilities simultaneously
- **Transparency**: Provides clear mechanism for understanding and controlling model capabilities

## Activation Keywords

- off switch dual use
- GRAM methodology
- gradient-routed auxiliary modules
- dual-use knowledge control
- harmful capability disable
- selective model control
- Anthropic off switch