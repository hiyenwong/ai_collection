---
name: charts-epistemic-actions-agentic
description: "Charts as Epistemic Actions for Experience-Driven Agentic Data Analysis. Tests whether charts can serve as internal epistemic actions inside data agents."
paper_id: 2610.30072
utility_score: 0.80
categories: [cs.AI]
date: 2026-10-21
tags: [data-agents, visual-reasoning, epistemic-actions, react, agentic-analysis]
---

# Charts as Epistemic Actions for Experience-Driven Agentic Data Analysis

## Key Contribution
Tests whether charts can serve as internal epistemic actions inside data agents built on ReAct-style loops. Human analysts move between numbers, tables, and charts to expose trends/anomalies that text summaries drop. This work asks if data agents can do the same.

## Core Method
- **Problem**: Data agents (ReAct-style) execute analytical workflows over structured data, but intermediate reasoning runs almost entirely through text. Human analysts use charts as cognitive tools.
- **Hypothesis**: Charts can serve as internal epistemic actions — not just outputs, but intermediate reasoning steps that expose patterns invisible to text.
- **Implementation**: 
  - Agent can generate charts as intermediate actions (not just final outputs)
  - Charts are fed back to the agent as visual evidence for next reasoning step
  - Agent learns when charting is more informative than text-based analysis
- **Experience-driven**: Agent accumulates experience about when charts help vs. when text suffices

## Why It Matters
- Bridges the gap between human analytical practice and AI agent design
- Shows that visual representations can improve agent reasoning, not just human interpretation
- Practical for data analysis agents, business intelligence, scientific discovery
- Suggests multi-modal reasoning (text + vision) is valuable even for structured data tasks

## Application Scenarios
- Data analysis agents working with tabular/structured data
- Business intelligence automation
- Scientific data exploration and hypothesis generation
- Any agentic workflow where intermediate visualizations could reveal patterns

## Implementation Notes
- Requires vision-capable LLM (to interpret generated charts)
- Chart generation can use matplotlib/plotly — agent decides what to visualize
- Epistemic action: chart is generated, interpreted by agent, then used for next reasoning step
- Overhead: chart generation + vision inference adds latency, but can reduce reasoning errors
- Key design choice: when should the agent decide to generate a chart vs. continue with text?
