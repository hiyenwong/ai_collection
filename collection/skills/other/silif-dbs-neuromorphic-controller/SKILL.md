---
name: silif-dbs-neuromorphic-controller
description: "Neuromorphic Silicon Neuron Controller for Adaptive Deep Brain Stimulation in Parkinson's Disease - CMOS-implemented SiLIF-DBS controller achieving 5.85%/uW beta suppression efficiency with 75% power reduction vs open-loop"
tags: [neuromorphic, deep-brain-stimulation, parkinsons, CMOS, adaptive-dbs, LIF, biomarker]
activation_words: [SiLIF-DBS, neuromorphic DBS, adaptive deep brain stimulation, Parkinson's, beta suppression, CMOS neuron]
arxiv_id: "2607.05453"
---

# Neuromorphic Silicon Neuron Controller for Adaptive Deep Brain Stimulation

## Paper Info
- **Title**: Neuromorphic Silicon Neuron Controller for Adaptive Deep Brain Stimulation in Parkinson's Disease
- **arXiv**: 2607.05453
- **Authors**: Md Abu Bakr Siddique, Jakub Orłowski, Yan Zhang, Hongyu An
- **Date**: 2026-07-08
- **Categories**: cs.AR, cs.NE
- **DOI**: 10.1145/3822454.3822465

## Core Contribution

First **circuit-level realization** of a neuromorphic adaptive deep brain stimulation (aDBS) controller using CMOS technology. The SiLIF-DBS (Silicon Leaky Integrate-and-Fire DBS) controller achieves:
- **75% power reduction** vs open-loop stimulation
- **5.85%/μW suppression efficiency** for pathological beta activity
- Closed-loop operation driven by STN-LFP biomarkers

## System Architecture

### SiLIF-DBS Controller
- Implemented in CMOS (metal-oxide-semiconductor) technology
- Uses Leaky Integrate-and-Fire (LIF) neuron model in silicon
- Processes beta-band subthalamic nucleus local field potentials (STN-LFPs)
- Control biomarker: average rectified value (Beta ARV)

### Closed-Loop Validation Framework
- Embedded within Parkinsonian cortico-basal ganglia computational model
- Driven by beta-band STN-LFPs as physiological input
- Beta ARV extracted as real-time control signal
- Stimulation adjusted based on biomarker threshold crossings

## Key Results

| Metric | SiLIF-DBS | Open-Loop DBS |
|--------|-----------|---------------|
| Power consumption | 25% of baseline | 100% (baseline) |
| Beta suppression efficiency | 5.85%/μW | ~1.5%/μW |
| Pathological beta activity | Strongly suppressed | Moderately suppressed |

## Methodology

### Biomarker Extraction
1. Record STN-LFPs from implanted electrode
2. Bandpass filter for beta band (13-30 Hz)
3. Compute average rectified value (ARV) as amplitude envelope
4. Threshold crossing triggers stimulation adjustment

### Neuromorphic Implementation
- LIF neuron dynamics in analog CMOS circuits
- Subthreshold operation for ultra-low power
- Event-driven stimulation delivery (only when biomarker exceeds threshold)
- Hardware-software co-design for implantable form factor

## Clinical Significance

1. **Adaptive stimulation** — tracks motor symptom fluctuations in real-time
2. **Energy efficiency** — critical for implantable pulse generators (IPGs) with limited battery
3. **Reduced side effects** — stimulation only when needed, minimizing tissue damage
4. **Scalable** — CMOS fabrication enables mass production

## Limitations

- Validated only in computational model, not in vivo
- Single biomarker (Beta ARV) may not capture all symptom dimensions
- CMOS implementation details (process node, area) not fully specified
- Long-term stability of silicon neuron characteristics not addressed

## Related Skills
- [[neuromorphic-computing]]
- [[deep-brain-stimulation]]
- [[adaptive-control]]
- [[cmos-neural-circuits]]
- [[parkinsons-disease]]

## Implementation Notes

The key innovation is moving aDBS from software algorithms to actual silicon circuits. Previous aDBS systems run algorithms on general-purpose processors consuming too much power for chronic implantation. The SiLIF approach uses the physics of silicon neurons (subthreshold MOSFET operation) to perform biomarker detection and stimulation decision-making at the circuit level, achieving orders-of-magnitude power savings.
