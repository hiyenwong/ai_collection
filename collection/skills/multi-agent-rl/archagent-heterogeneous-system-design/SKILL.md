---
name: archagent-heterogeneous-system-design
description: Agentic DSE for chip, scale-up, scale-out system design.
category: ai_collection
---

# ArchAgent: Agentic Heterogeneous System Design

Use when designing AI/HPC system configurations (chip, scale-up, scale-out domains), running LLM-agent design-space exploration (DSE), or building agentic pipelines where the LLM must never fabricate performance numbers.

Paper: "ArchAgent: Agentic AI for Heterogeneous System Design Across Chip, Scale-Up, and Scale-Out Domains" (arXiv:2610.23724, Argonne National Laboratory + UIUC, Oct 2026).

## Core idea

LLM agents carry architectural priors into system DSE, but a **deterministic analytical evaluator is the only source of performance numbers** — agents propose and critique; the tool scores and attributes bottlenecks. This "agents propose, evaluator disposes" split makes the search auditable and hallucination-free.

## Method

1. **Design representation** — candidate = JSON of partitions. Each partition: chip archetype (SIMT GPU / SRAM-dataflow / RISC-V / wafer-scale), scale-up fabric (NVLink, UALink, ICI, NeuronLink), scale-out fabric (InfiniBand, Slingshot, RoCEv2, Ultra Ethernet), power fraction, and workload role (general / prefill / decode / solver / ai). Roles let the evaluator model disaggregated execution (prefill on GPU partition, decode on SRAM-resident dataflow partition) without explicit placement management.
2. **Schema gate before evaluation** — feasibility validator (fabric bandwidth vs chip port capacity, power budget, FP64 capability for HPC); structured errors returned to agents instead of wasting eval cycles.
3. **Agent hierarchy** — planner proposes/revises whole designs and must call `evaluate_design`; specialist sub-agents (chip: roofline + memory hierarchy; scale-up: alpha-beta intra-domain communication + domain sizing; scale-out: collectives + topology) return concise parameter-level guidance attached to results.
4. **Deterministic evaluator** — roofline chip model (dtype-specific peak FLOPs, MFU, bandwidth-efficiency factors) for conventional accelerators; pipelined layer-sharding model for SRAM-resident dataflow (per-stage compute + point-to-point activations instead of TP all-reduce); alpha-beta communication model (ring + hierarchical all-reduce, TP/PP/DP with pipeline bubble, ZeRO-style memory-feasibility check; disaggregated prefill/decode for serving). Output: mixed-workload score + per-workload speedup + **bottleneck attribution** (compute throughput / memory bandwidth / fabric latency / bisection bandwidth).
5. **Calibration hierarchy** — 32 automated checks at 3 levels: spec invariants vs vendor datasheets, asymptotic identities of collective models, end-to-end predictions vs published MLPerf/vendor measurements (e.g. 910 tok/s/GPU for Llama-70B BF16 on 1024xH100 vs 750-1100 reported).

## Evaluation methodology (reusable)

- **Iso-power first** (1 MW facility level, including fabric ports), iso-cost secondary — otherwise comparisons are meaningless.
- Objective: weighted geometric mean of per-workload speedups vs homogeneous reference; **score 0 if any workload cannot run**.
- **Same-generation control**: restrict candidates to one hardware generation, else the optimizer trivially wins by picking newest silicon (preliminary searches degenerated to all-B200) and heterogeneity is never tested.
- Matched evaluation budgets for search-method comparison (ArchAgent passed hill-climbing's final 1.65 score at evaluation 18 of 100).

## Results

- 1.93x weighted geomean speedup over homogeneous H100+NVLink4+IB-NDR baseline (training 1.72x, serving 1.67x, HPCG 4.76x, coupled AI+HPC 2.61x, FFT 1.37x as binding constraint).
- Emergent pattern: **large GPU-like partition + small (2-10% power) role-specialized dataflow and FP64 partitions** — procurement by workload role, not one homogeneous fleet.
- Persistent gaps = roadmap: >=200 GB/s endpoint injection with in-network collectives; HBM4-class >=10 TB/s with FP64 capability.
- Planner capability matters: gpt-oss-120b reached 1.93, gemma-4-31B-it reached 0.87 (below baseline) with 7 schema-invalid + 4 infeasible designs in 50 evals.

## Reusable patterns

- **Tool-validated scoring invariant**: never let the LLM output performance estimates in DSE/agentic-optimization loops; route all numbers through a deterministic tool and feed back bottleneck attribution. Turns hallucination risk into an auditability property.
- **Partition + workload-role JSON schema** for facility-level designs; schema validation as a cheap first gate before expensive evaluation.
- **Planner + specialist sub-agents** mirroring the natural decomposition axes of the problem (chip / scale-up / scale-out).
- **Analytical-first, simulator-later**: keep expensive high-fidelity simulators OUT of the primary search loop; validate only top-ranked configurations afterwards (ASTRA-sim for collectives, Timeloop-class for mapping).

## Pitfalls

- Evaluator fidelity bounds all conclusions (no switch congestion, fixed compute/communication overlap factors, no KV-cache-transfer modeling) — but the agent loop is evaluator-agnostic, so swap in higher-fidelity models without redesign.
- LLM stochasticity: report across seeds; the planner model is part of the system under test (framework doubles as a benchmark for open-weight models on hardware-design search).
- Unrestricted generational mixing makes "heterogeneity wins" claims vacuous — always run the same-generation control.

**Activation**: heterogeneous system, system design DSE, scale-up scale-out, agentic design exploration, AI/HPC procurement, roofline model, alpha-beta collective model, workload roles, LLM system co-design
