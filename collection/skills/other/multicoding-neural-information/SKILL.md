---
name: skill.md---multicoding-neural-information-transfer
description: Skill for AI agent capabilities
---

# SKILL.md - Multicoding Neural Information Transfer

## Activation Keywords

- multicoding, neural coding, frequency-dependent plasticity
- spike timing, firing rate, STDP, synaptic plasticity in vivo
- neural information transfer, dual coding

## What It Does

Analyzes neural information transfer using multicoding framework — combining firing rate and spike timing codes. Addresses frequency-dependent synaptic plasticity in vivo, where precise spike timing is inhibited by brain's inhibitory nature.

## When To Use

**Use this skill when:**
- Modeling neural information transfer in vivo
- Analyzing frequency-dependent synaptic plasticity
- Implementing multicoding (rate + timing) in neural networks
- Studying STDP limitations in biological systems
- Designing bio-inspired learning rules

**Do NOT use for:**
- Simple rate-only coding models
- STDP in controlled experimental conditions (not in vivo)
- Non-synaptic plasticity mechanisms

## How To Use

### Step-by-Step Workflow

1. **Understand Dual Coding Framework**
   - **Rate coding:** Information in firing frequency
   - **Temporal coding:** Information in spike timing
   - **Multicoding:** Combined rate + timing signals

2. **Identify In Vivo Constraints**
   - Brain's inhibitory nature prevents precise spike timing
   - STDP (spike-timing-dependent plasticity) limited in vivo
   - Frequency-dependent plasticity more robust

3. **Implement Frequency-Dependent Plasticity**
   - Plasticity rule: Δw = f(frequency, timing_window)
   - High frequency → strong potentiation
   - Low frequency → weak/depression
   - Timing window broader than STDP

4. **Design Multicoding Transmission**
   - Sender: encode info in both rate and timing
   - Receiver: decode from combined signals
   - Reliability: redundant encoding

5. **Validate Against Biological Data**
   - Compare with in vivo recordings
   - Check frequency-dependent response curves
   - Verify information transfer capacity

### Key Parameters

| Parameter | Range | Biological Basis |
|-----------|-------|------------------|
| Frequency threshold | 10-50 Hz | In vivo firing rates |
| Timing window | ±50-100 ms | Broader than STDP |
| Plasticity gain | 0.01-0.1 | Synaptic weight changes |

### Information Capacity Analysis

**Rate coding capacity:**
```
I_rate = log2(firing_rate_levels)
```

**Timing coding capacity:**
```
I_timing = log2(timing_precision_bins)
```

**Multicoding capacity (redundant):**
```
I_multi = I_rate + I_timing - I_overlap
```

## Example Usage

### Neural Network with Multicoding

**Problem:** Implement bio-inspired learning rule for in vivo conditions

**Traditional STDP (fails in vivo):**
```python
def stdp(pre_spike, post_spike, dt):
    if dt > 0:  # post after pre
        w += A_plus * exp(-dt / tau_plus)
    else:  # pre after post
        w -= A_minus * exp(dt / tau_minus)
```

**Frequency-dependent multicoding (robust):**
```python
def freq_dependent_plasticity(pre_rate, post_rate, timing_correlation):
    # Frequency component
    freq_factor = (pre_rate * post_rate) / (baseline_rate ** 2)
    
    # Timing correlation (broader window)
    timing_factor = exp(-abs(timing_correlation) / tau_broad)
    
    # Combined plasticity
    delta_w = freq_factor * timing_factor * plasticity_gain
    return delta_w
```

**Result:** More stable learning under in vivo inhibitory conditions

### Information Transfer Analysis

**Input:** Neural firing patterns from in vivo recording

**Analysis:**
1. Extract firing rates (Hz)
2. Compute spike timing correlations
3. Estimate information capacity per channel

**Output:**
```
Rate coding: 3.2 bits/channel
Timing coding: 2.1 bits/channel
Multicoding: 4.8 bits/channel (redundant)
```

## Description

SKILL.md - Multicoding Neural Information Transfer

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Understand Dual Coding Framework

### Step 2: Identify In Vivo Constraints

### Step 3: Implement Frequency-Dependent Plasticity

### Step 4: Design Multicoding Transmission

### Step 5: Validate Against Biological Data

## Examples

### Example 1: Basic Application

**User:** I need to apply SKILL.md - Multicoding Neural Information Transfer to my analysis.

**Agent:** I'll help you apply multicoding-neural-information. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for multicoding-neural-information?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- **stdp-bernoulli-message-passing** - STDP-based learning
- **neuromodulated-synaptic-plasticity** - Neuromodulator effects
- **spiking-mode-neural-networks** - SNN architecture

## Source

- arXiv:2001.04103v1
- Title: Multicoding in neural information transfer suggested by mathematical analysis of the frequency-dependent synaptic plasticity in vivo
- Utility: 0.88
- Authors: Katsuhiko Hata, Osamu Araki, Osamu Yokoi, et al.
- Published: Scientific Reports (Nature) 2020

## Notes

- Key insight: STDP precise timing fails in vivo due to inhibition
- Solution: Frequency-dependent plasticity with broader timing window
- Multicoding = rate + timing, provides redundancy
- Applications: bio-inspired neural networks, robust learning rules
- Published in Nature Scientific Reports 2020

---

_Created: 2026-04-01_