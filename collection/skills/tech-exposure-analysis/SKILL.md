---
name: tech-exposure-analysis
description: >
  Technology exposure analysis methodology for measuring and forecasting how emerging
  technologies affect existing systems, workflows, and markets. Combines theoretical
  capability assessment with real-world usage data to quantify automation risk,
  displacement potential, and adoption patterns. Use when analyzing AI/technology
  impact on jobs, processes, or industries; measuring task-level automation potential;
  or building early-warning systems for technological disruption.
---

# Technology Exposure Analysis

## Overview

A framework for measuring how emerging technologies affect existing systems by
combining three data sources: theoretical capability, real-world usage patterns,
and task-level decomposition. Provides actionable metrics for forecasting disruption
and identifying vulnerable components before effects are visible in aggregate data.

## Core Framework

### Exposure Metric

```
exposure = theoretical_capability × usage_weight × automation_factor
```

- **theoretical_capability (β)**: Whether the technology can perform the task
  significantly faster (score: 0 = no, 0.5 = with tools, 1 = alone)
- **usage_weight**: How much the technology is actually being used for this task
  (from real-world telemetry, not surveys)
- **automation_factor**: Weight automated uses more heavily than augmentative uses

### Three-Source Data Model

| Source | What It Provides | Example |
|--------|-----------------|---------|
| Task database | Enumeration of tasks per domain/role | O*NET occupational tasks |
| Usage telemetry | Real-world adoption patterns | API usage, session data |
| Capability studies | Theoretical feasibility assessments | Research papers, expert ratings |

## Analysis Workflow

### Step 1: Task Decomposition

Break the domain into granular tasks:

```python
tasks = [
    {"id": "T1", "name": "draft_email", "time_hours": 0.25},
    {"id": "T2", "name": "analyze_spreadsheet", "time_hours": 2.0},
    {"id": "T3", "name": "debug_code", "time_hours": 4.0},
    # ...
]
```

### Step 2: Capability Scoring

Score each task for theoretical automation potential:

```python
def score_capability(task, technology):
    """
    β score:
    1.0 = technology alone can 2x speed up this task
    0.5 = technology + tools can 2x speed up
    0.0 = technology cannot significantly speed up
    """
    if can_automate_fully(task, technology):
        return 1.0
    elif can_automate_partially(task, technology):
        return 0.5
    return 0.0
```

### Step 3: Usage Weighting

Incorporate real-world usage data:

```python
def compute_usage_weight(task_id, usage_data):
    """Weight based on actual observed usage, not theoretical potential."""
    automated_ratio = usage_data["automated_sessions"] / usage_data["total_sessions"]
    work_related = usage_data["work_related_ratio"]
    return automated_ratio * work_related
```

### Step 4: Aggregate Exposure

```python
def aggregate_exposure(tasks, capability_scores, usage_weights):
    """Compute weighted exposure across all tasks."""
    total_time = sum(t["time_hours"] for t in tasks)
    exposure = sum(
        capability_scores[t["id"]] * usage_weights[t["id"]] * t["time_hours"]
        for t in tasks
    ) / total_time
    return exposure  # 0.0 to 1.0
```

## Interpretation Guidelines

| Exposure Level | Meaning | Action |
|---------------|---------|--------|
| 0.0 - 0.2 | Low exposure | Monitor, no immediate action needed |
| 0.2 - 0.4 | Moderate exposure | Begin planning adaptation strategies |
| 0.4 - 0.6 | High exposure | Active mitigation recommended |
| 0.6 - 0.8 | Very high exposure | Urgent transformation needed |
| 0.8 - 1.0 | Critical exposure | Immediate action required |

## Key Insights from Application

### Gap Analysis
Compare theoretical capability vs. actual usage to identify the "AI capability gap":
- High theoretical + low usage = near-term disruption potential
- High theoretical + high usage = ongoing transformation
- Low theoretical + high usage = human-AI collaboration pattern

### Counterfactual Reasoning
Establish baselines before effects are visible:
- Measure exposure now, even when impacts are ambiguous
- Revisit periodically to detect emerging trends
- Compare exposed vs. less-exposed cohorts over time

### Demographic Patterns
Analyze who is most affected:
- Map exposure to worker characteristics (age, education, compensation)
- Identify concentration patterns (some roles disproportionately affected)
- Track hiring trends in exposed vs. non-exposed areas

## Pitfalls

1. **Aggregate data hides effects**: Overall unemployment may not change while
   specific cohorts experience significant impact. Always disaggregate.
2. **Theoretical ≠ actual**: High theoretical capability doesn't mean high actual
   impact. Usage data is essential for grounding predictions.
3. **Lag time**: Technology adoption follows S-curves. Early measurements may
   underestimate eventual impact.
4. **Task interdependence**: Automating one task may change the value of adjacent
   tasks in non-obvious ways.

## Verification

- Compare exposure predictions against subsequent employment/productivity data
- Validate capability scores with domain experts
- Cross-reference with independent studies (academic, industry reports)
- Track prediction accuracy over multiple time periods

## References

- Anthropic Economic Index methodology (2025-2026)
- Eloundou et al. (2023) - Task-level LLM exposure estimation
- Gans & Goldfarb (2025) - O-ring model of job automation
- Hampole et al. (2025) - Task exposure concentration effects
