---
name: quantum-empirical-comparison-audit
category: quantum
description: CLAIMSTAB-QC framework for auditing empirical comparisons in quantum software papers. Records baselines, metrics, and evidence; locks comparison design before outcomes; classifies reported directions as Sustained, Unresolved, or Reversed within locked audit scope. Evaluates 455 claims from 119 papers revealing a materialization gap.
tags: [quantum, auditing, benchmarking, reproducibility, empirical-methods, software-engineering]
arxiv_id: "2607.00516v1"
created: "2026-07-07"
---

# CLAIMSTAB-QC: Auditing Empirical Comparisons in Quantum Software

## Overview
CLAIMSTAB-QC is a source-bounded framework for auditing empirical comparisons in quantum software research. It addresses a critical reproducibility gap: 455 comparative claims from 119 papers were evaluated, finding that only 8 out of 53 lockable designs exposed enough matched evidence to audit without proxy reconstruction.

## The Materialization Gap

### Key Statistics
- **455** comparative claims from **119** quantum-software papers
- **175** claims representable for audit planning
- **79** become scalar-directional planning records
- **53** yield lockable audit or diagnostic designs
- **Only 8** expose enough matched evidence for direct audit
- Of those 8: **2 Sustained, 4 Unresolved, 2 Reversed**

### The Problem
Empirical quantum-software comparisons are not properties of a tool alone — they change with:
- Benchmark scope
- Circuit construction methods
- Compilation strategies
- Sampling methods
- Backend or noise assumptions
- Optimizer choices
- Resource budgets

## Audit Framework

### Step 1: Record Comparison Design
For each reported comparison, record:
- **Baselines**: What is being compared against
- **Metric**: How performance is measured
- **Relation**: What type of comparison (greater, less, equal)
- **Admissible evidence**: What counts as valid support

### Step 2: Lock the Design
- Lock the comparison design **before** outcomes are computed
- Prevents outcome-dependent design changes (p-hacking analog)
- Defines the audit scope explicitly

### Step 3: Classify Outcomes
For strict scalar-directional comparisons:
- **Sustained**: Evidence supports the originally reported direction within locked scope
- **Unresolved**: Evidence is insufficient to confirm or refute within locked scope
- **Reversed**: Evidence contradicts the originally reported direction within locked scope

### Step 4: Diagnostic Analysis
When full audit isn't possible:
- Perform controlled diagnostics over benchmark-relevant comparisons
- Show that simpler checks can preserve apparent directions
- Reveal when support weakens under locked audit designs

## Implementation Pattern

```python
# Pseudo-code for audit workflow
def audit_comparison(paper, claim):
    # 1. Extract comparison components
    baselines = extract_baselines(claim)
    metric = extract_metric(claim)
    relation = extract_relation(claim)
    evidence = extract_admissible_evidence(paper)
    
    # 2. Lock the design
    audit_design = lock_design(baselines, metric, relation, evidence)
    
    # 3. Check evidence sufficiency
    if has_matched_evidence(evidence, audit_design):
        outcome = classify_outcome(evidence, audit_design)
        return {"status": "audited", "outcome": outcome}
    else:
        return {"status": "proxy_reconstruction_needed", 
                "diagnostic": run_diagnostics(audit_design)}
```

## When to Use
- Reviewing quantum software papers for empirical claims
- Designing reproducible quantum benchmarking studies
- Auditing your own empirical comparisons before publication
- Evaluating claims about compiler/optimizer/backend performance
- Establishing evidence standards for quantum software research

## Activation Keywords
CLAIMSTAB-QC, empirical audit, quantum software comparison, reproducibility, locked audit, materialization gap, benchmark auditing, evidence boundary, Sustained Unresolved Reversed
