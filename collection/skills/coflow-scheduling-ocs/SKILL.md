---
name: coflow-scheduling-ocs
description: Coflow Scheduling in Multi-Core Optical Circuit Switching Networks with Performance Guarantee. Optimize parallel data flow coordination in distributed systems using optical circuit switching. Use for data center network optimization, coflow scheduling, and distributed job completion time reduction.
---

# Coflow Scheduling in Multi-Core OCS Networks

This skill implements approximation algorithms for coflow scheduling in multi-core Optical Circuit Switching (OCS) data center networks with provable performance guarantees.

## Overview

Coflow provides an application-layer abstraction for capturing communication patterns, enabling efficient coordination of parallel data flows to reduce job completion times in distributed systems. Modern data centers employ multiple independent OCS cores operating concurrently to meet massive bandwidth demands.

**Key Features:**
- Multi-core OCS network scheduling
- Cross-core flow assignment optimization
- Provable worst-case performance guarantees
- Trace-driven validation with real workloads

## When to Use This Skill

- Data center network optimization
- Distributed job scheduling with communication patterns
- Optical circuit switching network management
- Coflow-aware resource allocation

## Problem Challenges

### Cross-Core Coupling
- Traffic assignment across heterogeneous cores
- Inter-core coordination complexity

### Per-Core OCS Constraints
- **Port Exclusivity**: Each port can support at most one circuit at a time
- **Reconfiguration Delay**: Circuit setup time overhead
- **Not-All-Stop Model**: One circuit's reconfiguration doesn't interrupt others

## Algorithm Framework

### Joint Optimization

```
Cross-Core Flow Assignment
         ↓
Per-Core Circuit Scheduling
         ↓
Minimize Weighted Coflow Completion Time (CCT)
```

### Approximation Algorithm

1. **Flow Assignment**: Distribute flows across available cores
2. **Circuit Scheduling**: Schedule circuits within each core
3. **Performance Guarantee**: Provable worst-case bound

### Key Results

- Approximation ratio for multi-core OCS
- Extends to multi-core EPS (Electrical Packet Switching)
- Reduces weighted CCT and tail CCT

## Implementation Guide

### Input

- Coflow set with flow sizes and endpoints
- Number of OCS cores
- Port configuration per core
- Reconfiguration delay

### Algorithm Steps

1. **Parse** coflow requests and network topology
2. **Assign** flows to appropriate cores
3. **Schedule** circuits considering reconfiguration delays
4. **Output** completion times and resource allocation

### Performance Metrics

| Metric | Description |
|--------|-------------|
| Weighted CCT | Total weighted coflow completion time |
| Tail CCT | 95th/99th percentile completion time |
| Approximation Ratio | Worst-case performance bound |

## Validation Results

Trace-driven simulations using **Facebook workloads** demonstrate:
- Effective reduction in weighted CCT
- Improved tail CCT performance
- Practical applicability to production workloads

## References

**Paper**: Scheduling Coflows in Multi-Core OCS Networks with Performance Guarantee
- **Authors**: Xin Wang, Hong Shen, Hui Tian, Dong Wang
- **arXiv**: 2604.08242
- **Date**: 2026-04-09
- **Categories**: cs.DC

## Related Skills

- `bandwidth-reduction-packetized-mpc`: Bandwidth reduction for packetized MPC
- `distributed-system-resiliency`: Resilience patterns for distributed systems


## Instructions for Agents

使用此技能时遵循以下流程：

1. **理解问题**：分析输入需求和约束条件
2. **选择方法**：根据场景选择合适的技术方案
3. **执行操作**：按照方法论实施具体步骤
4. **验证结果**：检查结果是否符合预期

## Examples

### Example 1: Basic Usage

**User:** 请帮我应用此技能

**Agent:** 我将按照标准流程执行...

### Example 2: Advanced Usage

**User:** 有更复杂的场景需要处理

**Agent:** 针对复杂场景，我将采用以下策略...

## Tools Used

- `exec`
- `read`
- `write`


## Activation Keywords

- coflow-scheduling-ocs
- coflow scheduling ocs
- coflow scheduling ocs
