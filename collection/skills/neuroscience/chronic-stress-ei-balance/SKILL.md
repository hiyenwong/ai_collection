---
name: chronic-stress-ei-balance
description: "Computational modeling methodology for chronic stress effects on prefrontal working memory networks via excitatory-inhibitory (E/I) balance perturbation. Use when modeling stress-induced cognitive dysfunction, E/I ratio alterations, or prefrontal cortex network dynamics under chronic perturbation."
---

## Chronic Stress E/I Balance Modeling

### Description

Computational framework for modeling how chronic stress shifts the excitatory-inhibitory (E/I) balance in prefrontal pyramidal neurons toward inhibitory dominance, degrading working memory function. Based on recurrent network models of working memory with stress-induced E/I perturbation analysis.

### Activation Keywords
- chronic stress modeling
- E/I balance
- 兴奋抑制平衡
- prefrontal working memory
- 慢性应激
- stress neural network
- inhibitory dominance
- 前额叶工作记忆
- E/I ratio perturbation
- stress-induced cognitive dysfunction

### Core Framework

#### 1. Working Memory Network Model
Standard recurrent E/I network with:
- **Excitatory population**: Pyramidal neurons (80% of neurons)
- **Inhibitory population**: Interneurons (20% of neurons)
- **Recurrent connectivity**: Structured (stimulus-specific) for E→E, random for others
- **Bistable dynamics**: Low-activity (spontaneous) and high-activity (persistent/memory) states

#### 2. Chronic Stress Perturbation
Chronic stress modeled as a gradual shift in E/I balance:
- **Increased inhibitory synaptic strength**: g_I→E ↑
- **Decreased excitatory synaptic strength**: g_E→E ↓
- **Altered NMDA/AMPA ratio**: Reduced NMDA contribution to recurrent excitation
- **Time scale**: Chronic = hours to days (slow parameter drift)

#### 3. Key Metrics
- **Persistent activity maintenance**: Can the network sustain elevated firing during delay?
- **Working memory capacity**: Number of simultaneously maintained items
- **Attractor stability**: Depth of the high-activity attractor basin
- **Signal-to-noise ratio**: Ratio of signal (memory) to background activity
- **Transition probability**: Likelihood of spontaneous memory loss

### Implementation Patterns

#### Pattern 1: E/I Network with Stress Perturbation

```python
import numpy as np

class EIWorkingMemoryNetwork:
    def __init__(self, N_E=800, N_I=200, stress_level=0.0):
        self.N_E, self.N_I = N_E, N_I
        self.stress = stress_level  # 0 = healthy, 1 = severe chronic stress
        
        # Baseline connection strengths
        self.J_EE = 1.0   # E→E (NMDA-dominated, slow)
        self.J_EI = 0.8   # E→I
        self.J_IE = 0.6   # I→E
        self.J_II = 0.4   # I→I
        
        # Stress-induced modifications
        self.apply_stress_perturbation()
        
    def apply_stress_perturbation(self):
        """Apply chronic stress effects on E/I balance."""
        s = self.stress
        # Inhibitory dominance: I→E strengthens
        self.J_IE_eff = self.J_IE * (1 + 0.5 * s)
        # Excitatory weakening: E→E reduces (NMDA hypofunction)
        self.J_EE_eff = self.J_EE * (1 - 0.3 * s)
        # External input to E decreases
        self.input_E_scale = 1.0 - 0.2 * s
        
    def is_working_memory_intact(self):
        """Check if persistent activity can be sustained."""
        # Mean-field analysis: check if high-activity fixed point exists
        net_excitation = self.J_EE_eff * 0.8  # 80% E cells
        net_inhibition = self.J_IE_eff * 0.2  # 20% I cells
        return net_excitation > net_inhibition + 0.3  # Threshold for bistability
```

#### Pattern 2: Stress Dose-Response Curve

```python
def stress_dose_response(stress_levels, n_trials=50):
    """Map chronic stress level to working memory performance."""
    results = []
    for stress in stress_levels:
        network = EIWorkingMemoryNetwork(stress_level=stress)
        intact_count = sum(
            network.is_working_memory_intact() 
            for _ in range(n_trials)
        )
        results.append({
            'stress': stress,
            'wm_intact_rate': intact_count / n_trials,
            'ei_ratio': network.J_EE_eff / network.J_IE_eff,
        })
    return results

# Critical stress threshold: typically ~0.4-0.6 where WM collapses
```

### Step-by-Step Usage

1. **Define baseline network**: Set E/I population sizes, connection strengths, time constants
2. **Implement stress perturbation**: Map stress level to parameter modifications
3. **Simulate dynamics**: Run network with stimulus → delay → response protocol
4. **Measure WM performance**: Track persistent activity during delay period
5. **Compute dose-response**: Vary stress level to find critical threshold
6. **Validate against data**: Compare to experimental findings on stress-induced WM deficits
7. **Test interventions**: Model pharmacological or behavioral interventions

### Pitfalls

1. **Time scale separation**: Chronic stress operates on hours/days, but network dynamics are ms-scale. Use slow parameter drift or separate timescales.
2. **NMDA vs AMPA**: Stress primarily affects NMDA-mediated recurrent excitation, not fast AMPA transmission. Model NMDA separately.
3. **Region specificity**: PFC is most stress-sensitive; hippocampus and amygdale have different stress responses. Don't generalize PFC findings to other regions.
4. **Individual variability**: Not all individuals show the same E/I shift — include population heterogeneity.
5. **Reversibility**: Acute stress effects are reversible; chronic stress causes structural changes. Model reversibility appropriately.

### Related Concepts
- Persistent activity and attractor dynamics
- NMDA receptor hypofunction
- Glucocorticoid signaling in PFC
- Dendritic spine remodeling under stress
- Cognitive reserve and stress resilience
