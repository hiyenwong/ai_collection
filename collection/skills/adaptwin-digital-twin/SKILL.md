---
name: adaptwin-digital-twin
description: "AdaPTwin: Adaptive Multi-Fidelity Predictive Digital Twin for proactive RRM in vehicular networks. Hierarchical cloud-edge architecture with dynamic fidelity selection."
category: "systems-engineering"
bump_similar: false
---

# AdaPTwin: Adaptive Multi-Fidelity Predictive Digital Twin

## Source
- **arXiv**: 2605.21897 (22 May 2026)
- **Authors**: Armin Makvandi, Md. Zoheb Hassan, Md. Jahangir Hossain
- **Venue**: Submitted to IEEE

## Core Problem
Digital twins for vehicular networks rely on ray-tracing for channel prediction, but high-fidelity ray-tracing is time-consuming, challenging accurate RRM under URLLC latency constraints.

## Key Innovation
Adaptive multi-fidelity — dynamically adjusting NDT fidelity based on network conditions via a hierarchical cloud-edge architecture:
- **Cloud tier** (~10 min intervals): computationally intensive fidelity policy selection
- **Edge tier** (every TTI): real-time proactive RRM loop

## Core Methodology

### 1. Hierarchical Cloud-Edge Decomposition
**Phase 1 — Cloud-based Fidelity Policy Optimization:**
- Benchmarks simulation parameters and selects optimal fidelity config
- MINLP formulation solved via enumeration + Multi-Start Iterative Coordinate Descent

**Phase 2 — Edge-based Proactive RRM:**
- Uses optimized NDT-fidelity from Phase 1
- Channel prediction: trajectory forecasting → look-ahead ray tracing → RRM execution

### 2. AI-Assisted Vehicle Trajectory Prediction
- Transformer-based model with continual learning for new mobility patterns
- Outperforms LSTM and Kalman Filter baselines (measured by FDE)

### 3. 3D Virtual Environment Modeling
- OpenStreetMap → Blender 3D models; detailed vehicle models for blockage prediction
- NVIDIA Sionna for ray-tracing and CIR computation

### 4. Adaptive Fidelity Control
- Low fidelity: simplified tracing, faster but less accurate
- High fidelity: detailed 3D ray-tracing, more accurate but slower
- Adaptive: selects fidelity per network state under latency budget

### 5. RRM Formulation
Joint optimization: service assignment + beam activation + fidelity selection
Objective: maximize proportionally fair sum-rate + minimize prediction error

## Key Results
- Predictive multi-fidelity beats reactive NDTs and 3GPP models
- Adaptive fidelity selection beats fixed single/multi-fidelity
- 3D vehicle modeling reduces blockage prediction error
- Near-optimal sum-rate with orders-of-magnitude lower latency vs exhaustive search

## Systems Engineering Patterns
1. **Cloud-Edge Decomposition**: separate planning (cloud, infrequent) from execution (edge, real-time)
2. **Adaptive Fidelity Selection**: monitor → evaluate → select → deploy → re-evaluate
3. **Predictive vs Reactive**: forecast future state to turn latency-constrained problems into look-ahead planning

## Activation
- **Keywords**: digital twin, adaptive fidelity, predictive control, cloud-edge, vehicular networks
- **Use when**: designing systems trading off accuracy vs latency, need proactive control in dynamic environments

## Pitfalls
- 3D model quality directly affects blockage prediction
- Trajectory prediction errors compound into channel errors
- NP-hard MINLP needs heuristic solvers for deployment
