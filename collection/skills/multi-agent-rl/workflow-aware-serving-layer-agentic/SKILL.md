---
name: workflow-aware-serving-layer-agentic
description: "A workflow-aware serving layer for agentic applications. Addresses the gap between model-serving engines and workflow orchestration for agentic AI workloads that form DAGs of LLM and tool calls with per-node model choices and quality operators. Activation: agentic serving, workflow-aware, LLM serving, DAG orchestration, quality operators, verifiers, agentic workload, serving infrastructure."
metadata:
  arxiv_id: "2607.02942"
  published: "2026-07-03"
  authors: "Jiayi Qian, Zishen Wan, Hanchen Yang, Chun Tao, Souvik Kundu, Tushar Krishna"
  tags: [agentic-serving, workflow-aware, llm-serving, dag-orchestration, quality-operators, verifiers, serving-infrastructure]
---

# A Workflow-Aware Serving Layer for Agentic Applications

## Overview

Agentic AI applications form an emerging serving workload in which a request creates a workflow: a directed acyclic graph (DAG) of LLM and tool calls that exposes per-node model choices and optional quality operators such as verifiers. This workload falls between two existing layers: model-serving engines (which optimize individual LLM calls) and workflow orchestration frameworks (which manage control flow but not serving-level optimization). This paper proposes a workflow-aware serving layer to bridge this gap.

## Key Problem

### The Serving Gap for Agentic Workloads
- Agentic requests create DAGs of LLM and tool calls, not single inference requests
- Model-serving engines optimize individual calls but don't understand workflow structure
- Workflow orchestrators manage control flow but don't optimize serving-level metrics
- No existing layer jointly optimizes model selection, resource allocation, and quality verification across the DAG

## Key Innovations

### Workflow-Aware Serving
- Understands the DAG structure of agentic requests
- Optimizes across the entire workflow, not just individual nodes
- Enables per-node model selection based on workflow-level objectives

### Quality Operators
- Optional verifiers and quality checks at workflow nodes
- Trade-off between quality and latency/cost at each DAG node
- Workflow-aware placement of quality operators for optimal end-to-end performance

### Per-Node Model Choices
- Different LLMs can be selected for different nodes in the workflow
- Model selection considers node-specific requirements (reasoning depth, output format, etc.)
- Enables cost optimization by using smaller models where sufficient

## Methodology

1. **Workflow DAG Representation**: Model agentic requests as DAGs with LLM and tool call nodes
2. **Serving Optimization**: Joint optimization of model selection, batching, and resource allocation across DAG
3. **Quality Operator Integration**: Optional verifier nodes with workflow-aware placement
4. **Performance Metrics**: End-to-end latency, throughput, cost, and quality trade-offs

## Implications

- New serving infrastructure layer purpose-built for agentic AI workloads
- Bridges the gap between model serving and workflow orchestration
- Per-node model selection enables significant cost optimization
- Quality operators as first-class citizens in the serving stack
- Essential infrastructure for production agentic AI deployments

## Pitfalls

- Workflow DAGs may be dynamic and hard to predict at request time
- Per-node model selection adds scheduling complexity
- Quality operator placement is an optimization problem that may not scale
- Interaction with existing serving engines (vLLM, TensorRT-LLM) needs integration work
- Benchmarking agentic serving workloads is an open problem

## Activation Keywords

agentic serving, workflow-aware, LLM serving, DAG orchestration, quality operators, verifiers, agentic workload, serving infrastructure, per-node model selection, workflow optimization

## Paper Reference

arXiv:2607.02942 - "A Workflow-Aware Serving Layer for Agentic Applications" (Jul 2026)
