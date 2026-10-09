---
name: ontrack-agent-monitoring
description: 'OnTrack: Real-Time Monitoring and Intervention in LLM Agent Trajectories via Streaming Structure-Aware Optimal Transport. Low-latency trajectory monitoring for agent safety.'
metadata:
  arxiv_id: "2610.12375"
  utility: 0.90
  authors: ["Babak Barazandeh", "Connor Swanson", "Chinmay Kulkarni", "Nikhil Mungel"]
  published: "2026-10-08"
  categories: ["cs.AI", "cs.CL", "cs.CY", "cs.LG"]
  tags: ["agent-monitoring", "trajectory", "optimal-transport", "real-time", "intervention", "safety"]
---

# OnTrack: Real-Time Monitoring and Intervention in LLM Agent Trajectories

**arXiv:** [2610.12375](https://arxiv.org/abs/2610.12375)
**Utility:** 0.90

## Key Innovation

Real-time monitoring and intervention in LLM agent trajectories via **Streaming Structure-Aware Optimal Transport**.

## Problem

LLM agents work autonomously with minimal safeguarding, leading to cost and safety issues from irreversible actions. Existing solutions:
- Safeguard agent monitoring every step → adds cost and latency
- Post-hoc log evaluation → too late for intervention

## Method

- Structure-aware optimal transport for comparing agent trajectories to safe reference trajectories
- Streaming computation enabling real-time comparison
- Intervention triggers when trajectory diverges beyond threshold

## Practical Use

- Deploy real-time monitoring for autonomous agents
- Intervene before agents take irreversible harmful actions
- Reduce monitoring overhead compared to full safeguard-agent approaches
