---
name: chloride-concentration-seizure-transitions
description: "Conductance-based neuronal network model for studying how chloride concentration dynamics modulate seizure transitions in excitatory and inhibitory networks."
arxiv_source: "2604.15747"
version: v1.0.0
last_updated: 2026-04-20
---

# Chloride Concentration Modulation in Seizure Transitions

Conductance-based neuronal network model for studying how intracellular chloride concentration regulates excitation-inhibition balance and drives seizure evolution and stage transitions.

## Core Innovation

- **Activity-dependent chloride dynamics**: Chloride concentration changes during neural activity
- **EI balance modulation**: Intracellular chloride levels regulate excitation/inhibition balance
- **Seizure stage transitions**: Model captures transitions between different seizure stages
- **Conductance-based modeling**: Biophysically realistic neuronal dynamics

## Technical Approach

### Neuron Model

Conductance-based neuron model with dynamic chloride:
```
C·dV/dt = -g_Na·m³·h·(V-E_Na) - g_K·n⁴·(V-E_K) - g_L·(V-E_L) - g_syn·(V-E_syn)
```

### Chloride Dynamics

Intracellular chloride concentration evolves as:
```
d[Cl-]/dt = J_in - J_out + J_activity
```

Where:
- `J_in`: Chloride influx through GABA_A receptors
- `J_out`: Active chloride extrusion (KCC2 transporter)
- `J_activity`: Activity-dependent chloride accumulation

### Network Architecture

- **Excitatory neurons**: Principal cells with glutamatergic synapses
- **Inhibitory neurons**: Interneurons with GABAergic synapses
- **Chloride dynamics**: Activity-dependent in both populations

## Applications

- Epilepsy mechanism understanding
- Anti-epileptic drug development
- Seizure prediction algorithms
- Network-level pathology analysis

## Activation Keywords

- chloride concentration seizure
- seizure transitions
- conductance-based neuron
- excitation inhibition balance
- epilepsy model
