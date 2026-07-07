---
name: metabolic-multi-agent-optimizer
description: "Metabolic Multi-Agent Optimizer (MMAO) - bio-inspired optimization with endogenous resource allocation. Each agent carries internal energy with private-public metabolic loop. Fitness improvements converted to metabolic gains regulating sensing, search amplitude, branching, pruning, respawning. Parameter-light, self-calibrating. Use when: optimization without manual hyperparameter tuning, bio-inspired meta-heuristics, adaptive resource allocation in multi-agent systems."
---

## Core Methodology

### Metabolic Resource Loop

Each agent maintains:
- **Internal energy** (private metabolic state)
- **Continuous role state** (search behavior identity)
- **Motion or structural memory**
- **Local search history**

Population shares:
- **Communal resource pool** (public metabolic state)

### Closed-Loop Control

```
Fitness improvement → Normalized metabolic gain → Energy pool → Regulates:
  ├── Sensing intensity
  ├── Search amplitude
  ├── Role drift
  ├── Branching (replication)
  ├── Pruning (death)
  ├── Respawning (birth)
  └── Elite reinvestment
```

### Continuous Setting
- Energy-regulated symmetric zero-order probing
- Role-interpolated motion between agent types

### Discrete Setting
- Structural sensing
- Local route improvement
- Guided perturbation
- Energy-weighted edge reuse

### Key Properties

1. **Endogenous**: Adaptation derived from internal metabolic loop, not externally attached modules
2. **Parameter-light**: Self-calibrating through metabolic feedback
3. **Cross-domain**: Same control law works for continuous and discrete optimization
4. **Validated**: CEC2017 (10D/30D, 20 seeds) + TSPLIB (5 instances, 100 runs)

### Progress Scale
Fitness improvements converted via:
- Robust progress scale (handles noisy improvements)
- Recent success statistic (short-term performance memory)

## Implementation Pattern

```python
class MetabolicAgent:
    energy: float  # Internal metabolic state
    role: float    # Continuous search behavior
    memory: dict   # Local search history
    
    def probe(self):
        amplitude = f(self.energy)  # Energy-regulated
        return symmetric_zero_order_probe(amplitude)
    
    def update_energy(self, fitness_delta):
        gain = robust_progress_scale(fitness_delta)
        self.energy += gain - metabolic_cost
```

## When NOT to Use
- Not universally superior - main value is parameter-light self-calibration
- Use when manual hyperparameter tuning is costly, not when absolute performance is paramount

## Activation

metabolic optimizer, bio-inspired optimization, multi-agent optimization, endogenous adaptation, parameter-light optimizer, MMAO, self-calibrating search, cs.NE
