---
name: stimulus-evoked-network-dynamics-organoids
description: Graph-computational framework for analyzing stimulus-evoked propagation dynamics in human cortical organoids using HD-MEA recordings. Includes stimulus-conditioned functional graphs, graph-constrained dynamical models, biological message-passing principles, and longitudinal depression analysis.
trigger: When analyzing stimulus-evoked network dynamics in cortical organoids or similar neural tissue preparations using high-density microelectrode arrays (HD-MEA).
---

# Stimulus-Evoked Network Dynamics in Human Cortical Organoids

## Overview
This methodology provides a comprehensive graph-computational framework for quantifying stimulus-evoked propagation dynamics in human cortical organoids. The approach combines experimental HD-MEA recordings with computational graph theory to distinguish structured information processing from spontaneous synchronization.

## Key Components

### 1. Stimulus-Conditioned Functional Graphs
- Construct functional connectivity graphs conditioned on stimulus timing
- Account for true acquisition sampling rate and precise stimulus timing recovery
- Analyze peak-latency vs. distance relationships to measure propagation

### 2. Graph-Constrained Dynamical Model
- Implement graph-neural-network as system identification tool
- Model network dynamics constrained by observed graph structure
- Validate model predictions against empirical data

### 3. Biological Message-Passing Principle
- Establish bounds on integration depth based on observable propagation depth
- Define metrics: effective depth (Deff), reachability index, maximum depth (dmax)
- Apply constraints to prevent overinterpretation of limited data

### 4. Longitudinal Depression Analysis
- Track repeated-stimulation effects across multiple days
- Compare stimulation-naive vs. repeatedly-stimulated organoids
- Measure response-population size and spatial contraction
- Control for developmental maturation using matched controls

## Implementation Steps

1. **Data Acquisition Setup**
   - Use high-density microelectrode array (HD-MEA) recordings
   - Ensure precise stimulus timing synchronization
   - Record longitudinal data across multiple days

2. **Preprocessing**
   - Recover true acquisition sampling rate
   - Align stimulus timing with neural responses
   - Filter and preprocess spike data

3. **Graph Construction**
   - Build daily functional connectivity graphs
   - Apply statistical thresholds for edge significance
   - Account for trial count limitations in reliability

4. **Propagation Analysis**
   - Calculate peak-latency vs. distance slopes
   - Determine if outward propagation is measurable (slope ≠ 0)
   - Apply integration depth metrics only when propagation is confirmed

5. **Longitudinal Comparison**
   - Implement developmentally-matched control design
   - Compare first-ever stimulation vs. repeated stimulation responses
   - Quantify response depression and spatial contraction

## Key Findings & Insights

- **Negative Result**: Evoked responses in organoids show fast, near-synchronous network bursts with no measurable outward propagation (peak-latency vs. distance slope = 0)
- **Methodological Consequence**: Traditional propagation/integration-depth metrics may not apply to organoid data due to limited trial counts and synchronous responses
- **Positive Finding**: Repeated daily stimulation progressively depresses and spatially contracts evoked responses (93% array engagement in naive vs. 10% in repeatedly-stimulated organoids)

## Applications

- **Organoid Research**: Validated framework for studying neural circuit formation in human cortical organoids
- **Neuroscience**: Methodology for distinguishing structured processing from spontaneous synchronization
- **Brain-Computer Interfaces**: Insights into network-level response properties in developing neural tissue
- **Computational Neuroscience**: Graph-theoretical approaches to neural dynamics analysis

## Pitfalls & Considerations

- **Trial Count Limitations**: Per-day connectivity graphs may not be reliably estimable with limited trial counts
- **Developmental Confounds**: Longitudinal designs must separate stimulation effects from natural maturation
- **Synchronization vs. Propagation**: Fast synchronous bursts should not be misinterpreted as propagating activity
- **Control Design**: Essential to include stimulation-naive controls matched for developmental stage

## Validation Metrics

- Peak-latency vs. distance slope significance
- Response-population size percentage
- Spatial contraction measurements  
- Control-validated depression effects

## References
- Nadimi, E. S., Gogineni, V. C., Braun, J.-M., Larsen, M. R., Blanes-Vidal, V., & Barnkob, H. B. (2026). Stimulus-Evoked Network Dynamics in Human Cortical Organoids: From a Graph-Computational Framework to Repeated-Stimulation Depression. arXiv:2607.28068 [q-bio.NC].