---
name: two-trace-stdp-model
description: 'Two-trace model for spike-timing-dependent plasticity (STDP). Model NMDA receptor activation and Ca2+ concentration traces. Reproduce pairwise STDP rules and triplet nonlinearities. Bridge phenomenological rules and detailed models.'
---

# Two-Trace STDP Model

## Description

An effective model for timing-dependent synaptic plasticity (STDP) using two interacting traces: NMDA receptor activation and Ca2+ concentration in dendritic spine. Bridges simplistic phenomenological rules and highly detailed models, reproducing both pairwise STDP and triplet nonlinearities in hippocampal culture and cortical slices.

**Source:** arXiv:1410.0557v1 (Neural Computation 2015)
**Utility:** 0.90

## Activation Keywords

- two-trace STDP
- spike-timing-dependent plasticity
- NMDA receptor trace
- calcium concentration plasticity
- triplet STDP
- STDP model
- synaptic plasticity timing

## Core Concepts

### 1. Two Traces

**Trace 1: NMDA Receptor Activation**
```
x(t) = fraction of activated NMDA receptors
Decays with time constant τ_x
```

**Trace 2: Ca2+ Concentration**
```
y(t) = Ca2+ concentration in dendritic spine
Decays with time constant τ_y
```

### 2. STDP Rule

**Pairwise STDP:**
```
Δw = A+ * x_pre * y_post - A- * x_post * y_pre

where:
- A+: LTP amplitude
- A-: LTD amplitude
- x_pre: presynaptic trace
- y_post: postsynaptic trace
```

### 3. Triplet Nonlinearities

**Key Feature:**
- Reproduces triplet experiments in hippocampal culture
- Reproduces triplet experiments in cortical slices
- Only 3 free parameters

## Quick Implementation

```python
import numpy as np

class TwoTraceSTDP:
    """Two-trace STDP model."""
    
    def __init__(self, tau_x=20.0, tau_y=40.0, A_plus=0.1, A_minus=0.1):
        self.tau_x = tau_x  # NMDA decay
        self.tau_y = tau_y  # Ca2+ decay
        self.A_plus = A_plus  # LTP
        self.A_minus = A_minus  # LTD
        
        self.x = 0.0  # NMDA trace
        self.y = 0.0  # Ca2+ trace
        
    def update_traces(self, dt, pre_spike=False, post_spike=False):
        """Update traces with exponential decay."""
        self.x *= np.exp(-dt / self.tau_x)
        self.y *= np.exp(-dt / self.tau_y)
        
        if pre_spike:
            self.x += 1.0
        if post_spike:
            self.y += 1.0
            
    def compute_weight_change(self, pre_spike=False, post_spike=False):
        """Compute STDP weight change."""
        dw = 0.0
        if pre_spike and post_spike:
            # Causal (LTP)
            dw += self.A_plus * self.x * self.y
        elif pre_spike:
            # Post-before-pre (LTD)
            dw -= self.A_minus * self.y
        elif post_spike:
            # Pre-before-post (LTP)
            dw += self.A_plus * self.x
            
        return dw
```

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Understand the Request

### Step 2: Search for Information

### Step 3: Apply the Framework

### Step 4: Provide Results

### Step 5: Verify Accuracy

## Examples

### Example 1: Basic Application

**User:** I need to apply Two-Trace STDP Model to my analysis.

**Agent:** I'll help you apply two-trace-stdp-model. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for two-trace-stdp-model?

**Agent:** Let me search for the latest research and best practices...

## References

- Echeveste, R. et al. (2015). "Two-trace model for spike-timing-dependent synaptic plasticity" Neural Computation 27(3), 672-698

---

**Created:** 2026-03-30 03:06