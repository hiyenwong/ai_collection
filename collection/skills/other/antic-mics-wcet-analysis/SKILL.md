---
name: antic-mics-wcet-analysis
description: "Mixed-Criticality (MC) system WCET (Worst-Case Execution Time) analysis and optimization using AnTi-MiCS and MulTi-MiCS frameworks. Enables optimal low WCET determination for real-time embedded systems, balancing processor utilization against Quality-of-Service. Use when: (1) designing mixed-criticality real-time systems, (2) optimizing WCET bounds for embedded tasks, (3) analyzing execution time distributions for mode switch optimization, (4) reducing utilization waste in MC scheduling. Activation: mixed criticality, WCET analysis, real-time systems, embedded scheduling, mode switch optimization, AnTi-MiCS, MulTi-MiCS."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    source_paper: "AnTi-MiCS: Analytical Framework for Bounding Time in Embedded Mixed-Criticality Systems (arXiv:2604.27862)"
    citations: 0
    tags: [real-time-systems, embedded-systems, mixed-criticality, wcet, scheduling]
---

# AnTi-MiCS: Mixed-Criticality WCET Optimization

## Overview

AnTi-MiCS and MulTi-MiCS provide analytical frameworks for determining optimal low WCET bounds in Mixed-Criticality systems. They solve the fundamental trade-off: low WCET → better utilization but more mode switches; high WCET → fewer switches but wasted resources.

Source: Ranjbar & Kumar, arXiv:2604.27862 (Apr 2026)

## Core Concepts

### The WCET Trade-off

In MC systems, tasks have multiple WCET values:
- **High WCET**: Conservative bound for HI-criticality mode (guaranteed safe)
- **Low WCET**: Optimistic bound for LO-criticality mode (better utilization)

**Trade-off**: Lower low-WCET → schedule more tasks but trigger more mode switches → degrade QoS

### AnTi-MiCS (Single Low WCET)

Analytical method to determine optimal single low WCET:
1. Collect task execution traces
2. Analyze execution time distribution
3. Compute optimal low WCET balancing utilization vs. mode switch probability

### MulTi-MiCS (Multiple Low WCETs)

Extension for bimodal/multimodal execution distributions:
1. Identify clusters in execution time distribution
2. Compute multiple low WCET values per cluster
3. Exploit temporal correlation between consecutive inputs

## Implementation Pattern

```python
import numpy as np
from collections import Counter

class AntiMiCSAnalyzer:
    """AnTi-MiCS: Single low WCET determination."""
    
    def __init__(self, high_wcet, execution_traces, utilization_weight=0.5):
        """
        Args:
            high_wcet: High-criticality WCET bound
            execution_traces: Array of observed execution times
            utilization_weight: Trade-off parameter (0=QoS focus, 1=utilization focus)
        """
        self.high_wcet = high_wcet
        self.traces = execution_traces
        self.weight = utilization_weight
        
    def compute_optimal_low_wcet(self):
        """
        Compute optimal low WCET by analyzing execution distribution.
        
        Returns:
            low_wcet: Optimal low WCET value
            expected_utilization: Predicted processor utilization
            mode_switch_prob: Probability of mode switch
        """
        # Sort traces and analyze cumulative distribution
        sorted_traces = np.sort(self.traces)
        n = len(sorted_traces)
        
        best_score = -np.inf
        best_wcet = sorted_traces[0]
        
        for candidate in sorted_traces:
            # Tasks completing within candidate WCET
            within_bound = np.sum(sorted_traces <= candidate)
            utilization = within_bound / n * candidate / self.high_wcet
            mode_switch_prob = 1 - within_bound / n
            
            # Score: balance utilization and QoS (inverse of mode switches)
            score = (self.weight * (1 - utilization) + 
                    (1 - self.weight) * (1 - mode_switch_prob))
            
            if score > best_score:
                best_score = score
                best_wcet = candidate
        
        return best_wcet, utilization, mode_switch_prob


class MultiMiCSAnalyzer(AntiMiCSAnalyzer):
    """MulTi-MiCS: Multiple low WCET determination."""
    
    def __init__(self, high_wcet, execution_traces, n_clusters=2):
        super().__init__(high_wcet, execution_traces)
        self.n_clusters = n_clusters
        
    def compute_multi_wcet(self):
        """
        Compute multiple low WCET values for multimodal distributions.
        Exploits temporal correlation between consecutive inputs.
        
        Returns:
            wcet_values: List of (wcet, probability) pairs
        """
        # Use k-means or Gaussian mixture to cluster execution times
        from sklearn.mixture import GaussianMixture
        
        traces_2d = self.traces.reshape(-1, 1)
        gmm = GaussianMixture(n_components=self.n_clusters)
        gmm.fit(traces_2d)
        
        wcet_values = []
        for i in range(self.n_clusters):
            # WCET for each cluster: mean + 3*std (covers 99.7%)
            mean = gmm.means_[i][0]
            std = np.sqrt(gmm.covariances_[i][0][0])
            wcet = min(mean + 3 * std, self.high_wcet)
            wcet_values.append((wcet, gmm.weights_[i]))
        
        return sorted(wcet_values, key=lambda x: x[0])
```

## Workflow

1. **Collect execution traces** - Run tasks on target platform, record execution times
2. **Analyze distribution** - Check if unimodal (use AnTi-MiCS) or multimodal (use MulTi-MiCS)
3. **Compute optimal WCET(s)** - Apply framework to determine bounds
4. **Configure scheduler** - Use computed WCETs in MC scheduling algorithm (e.g., EDF-VD)
5. **Monitor and adapt** - Track actual execution times, update bounds if distribution drifts

## Expected Results (from paper)

| Framework | QoS Improvement | Utilization Waste Reduction |
|-----------|----------------|----------------------------|
| AnTi-MiCS | 30.27% average | 35.89% |
| MulTi-MiCS | 36.68% (6.41% over AnTi) | 44.12% (8.23% over AnTi) |

## When to Use

- **Mixed-criticality embedded systems** (automotive, aerospace, industrial)
- **Real-time scheduling optimization** where WCET tuning matters
- **Multimodal workloads** with distinct execution patterns
- **Resource-constrained platforms** needing utilization maximization

## Related Standards

- ISO 26262 (automotive functional safety)
- DO-178C (avionics software)
- IEC 61508 (industrial functional safety)

## References

- Ranjbar, B., Kumar, A. (2026). "AnTi-MiCS: Analytical Framework for Bounding Time in Embedded Mixed-Criticality Systems." arXiv:2604.27862.
- Related skills: [[real-time-scheduling]], [[embedded-systems-design]]
