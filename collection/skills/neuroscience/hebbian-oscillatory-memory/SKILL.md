---
name: skill.md---hebbian-imprinting-in-oscillatory-neura
description: Skill for AI agent capabilities
---

# SKILL.md - Hebbian Imprinting in Oscillatory Neural Networks

## Activation Keywords

- Hebbian learning, oscillatory neural networks, spike-timing plasticity
- memory imprinting, pattern retrieval, hippocampus model
- oscillatory dynamics, phase coding, cortical memory

## What It Does

Models generalized Hebbian learning and memory retrieval in oscillatory neural networks that mimic cortical areas like hippocampus and olfactory cortex. Shows how spike-timing-dependent plasticity can support memory encoding and recall.

## When To Use

**Use this skill when:**
- Modeling hippocampal memory systems
- Implementing oscillatory memory networks
- Studying spike-timing-dependent plasticity (STDP)
- Designing associative memory with phase coding
- Analyzing memory retrieval dynamics

**Do NOT use for:**
- Rate-based neural networks (no oscillations)
- Static memory models (no temporal dynamics)
- Non-Hebbian learning rules

## How To Use

### Step-by-Step Workflow

1. **Define Oscillatory Network**
   - Neurons as oscillators with phase θᵢ(t)
   - Global oscillation field (theta rhythm)
   - Phase relative to oscillation encodes information

2. **Hebbian Imprinting (Learning)**
   - Present pattern to store: ξᵢ ∈ {+1, -1}
   - Neurons spike at preferred phase based on pattern
   - Synaptic plasticity: Δwᵢⱼ = η · ⟨sᵢ · sⱼ⟩ₜ
   - Spike timing determines sign of weight change

3. **Retrieval Process**
   - Present partial cue pattern
   - Network dynamics converge to stored pattern
   - Phase coherence indicates successful retrieval

4. **Spike-Timing Dependence**
   - Pre before post → potentiation (LTP)
   - Post before pre → depression (LTD)
   - Timing window: ~10-20 ms

5. **Analysis**
   - Measure retrieval quality (overlap with stored pattern)
   - Compute storage capacity
   - Analyze phase dynamics

### Key Equations

**Oscillatory neuron dynamics:**
```
dθᵢ/dt = ω₀ + Σⱼ wᵢⱼ sin(θⱼ - θᵢ) + Iᵢ(t)
```

**Hebbian learning with spike timing:**
```
Δwᵢⱼ = A₊ exp(-|Δt|/τ₊)  if Δt > 0 (pre before post)
Δwᵢⱼ = -A₋ exp(-|Δt|/τ₋) if Δt < 0 (post before pre)
```

**Pattern overlap (retrieval quality):**
```
m = (1/N) Σᵢ ξᵢ · sign(sᵢ)
```

### Parameters

| Parameter | Typical Value | Biological Basis |
|-----------|---------------|------------------|
| Oscillation freq | 4-12 Hz | Theta rhythm |
| τ₊, τ₋ | 10-20 ms | STDP window |
| Learning rate η | 0.01-0.1 | Synaptic efficacy |
| Network size N | 100-10000 | Cortical column |

## Example Usage

### Memory Imprinting and Retrieval

**Problem:** Store and retrieve patterns in oscillatory network

**Setup:**
```python
import numpy as np

class OscillatoryMemoryNetwork:
    def __init__(self, N, omega=2*np.pi*8):  # 8 Hz theta
        self.N = N
        self.omega = omega
        self.phases = np.random.uniform(0, 2*np.pi, N)
        self.weights = np.zeros((N, N))
    
    def imprint_pattern(self, pattern, duration=0.5):
        """
        Imprint pattern using Hebbian learning
        pattern: {+1, -1} vector to store
        """
        dt = 0.001
        t = np.arange(0, duration, dt)
        
        # Neurons spike at phase determined by pattern
        preferred_phase = np.where(pattern > 0, 0, np.pi)
        
        for ti in t:
            # Update phases
            input_current = np.cos(self.omega * ti - preferred_phase)
            self.phases += dt * (self.omega + 0.1 * input_current)
            
            # Hebbian learning (simplified)
            for i in range(self.N):
                for j in range(self.N):
                    # Spike timing from phase difference
                    phase_diff = (self.phases[i] - self.phases[j]) % (2*np.pi)
                    if phase_diff < np.pi:  # j spikes before i
                        self.weights[j, i] += 0.001
    
    def retrieve(self, cue, duration=0.3):
        """
        Retrieve stored pattern from partial cue
        """
        # Initialize phases from cue
        self.phases = np.where(cue > 0, 0, np.pi)
        
        dt = 0.001
        for _ in range(int(duration/dt)):
            # Phase dynamics with learned weights
            phase_input = np.sin(self.phases - self.phases[:, None])
            dphase = self.omega + np.sum(self.weights * phase_input, axis=1)
            self.phases += dt * dphase
        
        # Decode retrieved pattern
        retrieved = np.where(self.phases < np.pi, 1, -1)
        return retrieved
```

### Storage Capacity Analysis

**Input:** Network with N neurons, patterns to store

**Analysis:**
```python
def measure_capacity(N, alpha_range=np.linspace(0.05, 0.3, 10)):
    """
    Measure storage capacity α = P/N
    """
    for alpha in alpha_range:
        P = int(alpha * N)
        network = OscillatoryMemoryNetwork(N)
        
        # Store P random patterns
        patterns = [np.random.choice([-1, 1], N) for _ in range(P)]
        for p in patterns:
            network.imprint_pattern(p)
        
        # Test retrieval
        overlaps = []
        for p in patterns:
            cue = p.copy()
            cue[:int(0.3*N)] = 0  # 30% cue
            retrieved = network.retrieve(cue)
            overlap = np.mean(p * retrieved)
            overlaps.append(overlap)
        
        print(f"α={alpha:.2f}: mean overlap={np.mean(overlaps):.3f}")
```

**Output:** Critical capacity α_c ≈ 0.1-0.2

## Key Insights

1. **Phase coding:** Information encoded in relative phase to oscillation
2. **Spike-timing plasticity:** Learning depends on precise spike timing
3. **Oscillation-gated learning:** Theta rhythm gates memory encoding
4. **Capacity limits:** Similar to Hopfield networks

## Description

SKILL.md - Hebbian Imprinting in Oscillatory Neural Networks

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Define Oscillatory Network

### Step 2: Hebbian Imprinting (Learning)

### Step 3: Retrieval Process

### Step 4: Spike-Timing Dependence

### Step 5: Analysis

## Examples

### Example 1: Basic Application

**User:** I need to apply SKILL.md - Hebbian Imprinting in Oscillatory Neural Networks to my analysis.

**Agent:** I'll help you apply hebbian-oscillatory-memory. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for hebbian-oscillatory-memory?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- **stdp-bernoulli-message-passing** - STDP learning rules
- **spike-timing-neuronal-assemblies** - Spike timing in assemblies
- **neuromodulated-synaptic-plasticity** - Neuromodulation effects

## Source

- arXiv:cond-mat/0111034v1 (now q-bio/0111034)
- Title: Hebbian imprinting and retrieval in oscillatory neural networks
- Utility: 0.87
- Authors: Silvia Scarpetta, Zhaoping Li, John Hertz
- Published: Neural Computation 14(10), 2002

## Notes

- Classic paper linking oscillations to memory
- Published in Neural Computation 2002
- Models hippocampus and olfactory cortex
- Key insight: oscillations enable phase-coded memory
- Precursor to modern oscillatory memory theories

---

_Created: 2026-04-01_