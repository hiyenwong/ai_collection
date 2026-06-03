---
name: agentic-systems-monitoring-maturity
description: "Monitoring and triage methodology for agentic systems before they're reliable. Decomposes evaluation into three dimensions (quality, suitability, efficiency) at three scopes (within-run, cross-run, structural), using variance as characterization signal. Routes findings through FMEA-based severity classification. Activation: monitoring agentic systems, agent monitoring, agent triage, agentic systems reliability, agent maturity staging."
---

## Practical Defaults

- **Paper**: arXiv:2606.02494 - "Monitoring Agentic Systems Before They're Reliable"
- **Authors**: Marisa Ferrara Boston, Glen Hanson, Effi Georgala, JD Hudgens, Heather Frase
- **Submitted**: 2026-06-01
- **Categories**: cs.SE, cs.AI
- **Conference**: Workshop on Agentic Software Engineering (AgenticSE), ACM CAIS 2026

## Core Methodology

### Problem Statement
Agentic systems entering production operate as **partially integrated assemblies** where **structural defects, not task-level errors, dominate the failure landscape**. At this maturity level:
- Task-level error detection may be infeasible
- Structural failure modes mask the signal that task-level monitors are designed to detect
- Traditional outcome-only evaluation is insufficient

### Three-Dimensional Evaluation Framework

Decompose agentic system evaluation into **three dimensions** at **three monitoring scopes**:

| Dimension | Description |
|-----------|-------------|
| **Quality** | Output correctness, completeness, coherence |
| **Suitability** | Alignment with task requirements, constraints |
| **Efficiency** | Resource usage, latency, cost |

| Scope | Coverage | Typical Findings |
|-------|----------|------------------|
| **Within-run** | Single execution trace | Deterministic stage defects (CV = 0.02) |
| **Cross-run** | Multiple executions, same config | Stochastic integration consequences (CV = 1.25) |
| **Structural** | Architecture-level patterns | Integration gaps with perfect consistency (CV = 0.00) |

### Variance-Based Characterization

Use **Coefficient of Variation (CV)** as the characterization signal:

- **CV ≈ 0.00**: Perfect consistency → Structural defect (deterministic)
- **CV ≈ 0.02**: Low variance → Stage-level defect
- **CV ≈ 1.25**: High variance → Integration-level stochastic failure
- **24% at L2**: Intermediate variance → Partial integration gaps

### FMEA-Based Severity Classification

Adapt Failure Mode and Effects Analysis (FMEA) for findings routing:

| Severity Level | Action | Automation |
|----------------|--------|------------|
| **Critical** | Immediate human investigation | 0% automated |
| **High** | Priority tracking + review | 10% automated |
| **Medium** | Automated tracking + periodic review | 97% automated |
| **Low** | Log-only | 100% automated |

Key finding: **Deterministic triage routes 97% of findings to automated tracking**, leaving only 2% reflecting variable behavior for human investigation.

### Maturity-Staging Model

Proposed **three-stage maturity model** for monitoring transition:

```
Stage 1: Structural Characterization
  → Focus on architecture-level defects
  → Monitor integration gaps
  → CV-based scope identification

Stage 2: Error Detection
  → Transition to task-level monitoring
  → As structural defects resolve
  → Enable outcome validation

Stage 3: Reliability Tracking
  → Full task-level coverage
  → Continuous reliability metrics
  → Production monitoring
```

## Key Results

From 220 runs across 120 document bundles with controlled error injection:

1. **Monitor scope determines failure type**:
   - Within-run → deterministic stage defects (CV = 0.02)
   - Cross-run → stochastic integration (CV = 1.25, 24% at L2)
   - Structural → integration gaps (CV = 0.00)

2. **Structural defects mask task-level signal**:
   - Injected task-level errors **indistinguishable from clean baselines**
   - Structural failure modes dominate early production

3. **Early monitoring value**:
   - **Deploy monitoring early**: "The first thing it finds is the most important thing to fix"

## Implementation Pattern

### Monitoring Pipeline

```python
# Three-scope monitoring architecture
class AgenticMonitor:
    def __init__(self, dimensions=['quality', 'suitability', 'efficiency']):
        self.scopes = {
            'within_run': WithinRunMonitor(),
            'cross_run': CrossRunMonitor(),
            'structural': StructuralMonitor()
        }
        
    def evaluate(self, run_trace):
        findings = []
        for scope_name, monitor in self.scopes.items():
            for dimension in self.dimensions:
                result = monitor.evaluate(run_trace, dimension)
                cv = compute_cv(result.values)
                severity = classify_severity(cv, scope_name)
                findings.append(Finding(scope_name, dimension, cv, severity))
        
        return self.triage(findings)
    
    def triage(self, findings):
        # Route based on severity
        for finding in findings:
            if finding.cv < 0.05:  # Structural defect
                finding.route = 'automated_tracking'
            elif finding.cv > 1.0:  # Stochastic failure
                finding.route = 'human_investigation'
            else:
                finding.route = 'periodic_review'
        return findings
```

### Scope-Specific Monitors

**Within-run monitor**: Detect deterministic stage defects
- Stage-level validation
- Output coherence checks
- Constraint verification

**Cross-run monitor**: Detect stochastic integration issues
- Run-to-run comparison
- Variance tracking
- Ensemble behavior analysis

**Structural monitor**: Detect integration gaps
- Architecture-level patterns
- Interface consistency
- Contract violations

## Practical Applications

### Document-Driven Workflows
The methodology transfers architecturally to:
- Multi-stage agentic pipelines
- Document processing workflows
- Regulated industry applications (finance, healthcare, legal)

### Calibration Points
Domain-specific calibrations needed for:
- Severity thresholds
- CV interpretation ranges
- Automation routing percentages

### Integration with Existing Tools
- FMEA frameworks (adapt severity classification)
- CI/CD pipelines (stage-level monitoring)
- APM tools (within-run metrics)
- Logging systems (cross-run analysis)

## When to Use

- **Agentic systems in early production** (partial integration stage)
- **Document-driven workflows** with multi-stage processing
- **Regulated industries** requiring audit trails
- **Systems where structural defects > task-level errors**

## Related Skills

- [[agent-integration-testing]] - Integration testing for autonomous agents
- [[system-resilience-design-patterns]] - System resilience patterns
- [[spec-driven-agent-architecture]] - Specification-driven agent architecture
- [[agentic-reliability-framework]] - Agentic reliability patterns

## Pitfalls

- **Don't wait for task-level monitoring** → Structural defects mask task-level signal
- **Don't ignore variance** → CV = 0.00 is structural, not random
- **Don't over-automate human review** → Only 2% needs human attention
- **Don't skip cross-run analysis** → Integration issues are stochastic
- **Domain-specific calibration required** → Thresholds don't transfer directly

## References

- arXiv:2606.02494 - Original paper
- Workshop on Agentic Software Engineering (AgenticSE) 2026
- FMEA (Failure Mode and Effects Analysis) methodology