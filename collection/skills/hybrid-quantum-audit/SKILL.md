---
name: hybrid-quantum-audit
description: "Methodology for auditing quantum advantage in hybrid quantum-classical optimization systems. Quantifies contribution of quantum processing units versus classical heuristics in hybrid pipelines. Based on D-Wave hybrid portfolio optimization audit research. Use when: evaluating hybrid quantum systems, measuring quantum vs classical contribution, analyzing D-Wave hybrid solvers, or designing quantum advantage metrics."
category: quantum-optimization
---

# Hybrid Quantum Advantage Audit

## Description

Audit quantum advantage in hybrid quantum-classical optimization systems. Quantify how much of the solution quality comes from the quantum processing unit (QPU) versus classical heuristics, and propose metrics for quantum contribution in hybrid pipelines.

## Activation Keywords

- hybrid quantum audit
- quantum advantage audit
- D-Wave hybrid
- quantum contribution measurement
- hybrid solver analysis
- quantum vs classical contribution

## Tools Used

- exec: Run hybrid quantum experiments, classical baselines
- read: Read optimization results, compare solver outputs
- write: Generate audit reports, contribution analysis

## Core Methodology

### Step 1: Isolate Quantum Contribution

Decompose the hybrid solver pipeline:
1. Run the full hybrid solver (QPU + classical)
2. Run classical-only variant (disable QPU calls)
3. Compare solution quality distribution across both
4. Attribute improvements to quantum or classical components

### Step 2: Define Quantum Contribution Metrics

Use these metrics to quantify quantum vs classical contribution:

- **Quantum Improvement Rate**: % of instances where QPU improves over classical-only
- **Solution Space Exploration Index**: Measure diversity of solutions explored by QPU
- **Classical Post-Processing Amplification**: How much classical refinement improves QPU solutions
- **Hybrid Synergy Score**: Whether quantum+classical > quantum alone + classical alone

### Step 3: Pipeline Analysis Framework

```
Input Problem
    │
    ├──→ Classical Pre-processing (screening, reduction)
    │         │
    │         ├──→ QPU Sampling (solution space exploration)
    │         │         │
    │         │         └──→ Raw QPU Solutions
    │         │
    │         └──→ Classical Post-processing (refinement, local search)
    │                   │
    │                   └──→ Final Solutions
    │
    └──→ Classical-Only Baseline (same pre/post, no QPU)
              │
              └──→ Baseline Solutions

Compare: Hybrid Solutions vs Classical-Only Solutions
```

### Step 4: Experimental Protocol

1. **Select representative problem instances** across difficulty levels
2. **Fix all random seeds** for reproducibility
3. **Run N iterations** of hybrid solver (N ≥ 30 for statistical significance)
4. **Run N iterations** of classical-only baseline
5. **Record**: best solution, mean solution, solution distribution, runtime
6. **Apply statistical tests**: t-test, Mann-Whitney U, effect size (Cohen's d)

### Step 5: Report Generation

Generate audit report with:
- Quantum advantage heatmap across problem sizes
- Contribution breakdown (% quantum, % classical, % synergy)
- Statistical significance of observed improvements
- Recommendations for when hybrid is justified vs classical-only

## Key Findings from Research

Current D-Wave hybrid approaches rely heavily on classical post-processing, with quantum contributions primarily in solution space exploration. The QPU helps escape local optima that classical heuristics get trapped in, but classical components handle the bulk of solution refinement.

## Error Handling

### No Quantum Advantage Detected
- Verify problem encoding is correct
- Check QPU connectivity and embedding quality
- Try different annealing schedules
- Consider that problem may be classically easy

### Statistical Noise
- Increase number of iterations (≥ 30)
- Use bootstrap confidence intervals
- Report effect sizes, not just p-values

## References

- "Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization" - Lozano et al.
- D-Wave Hybrid Solver Documentation
- Quantum advantage benchmarking frameworks
