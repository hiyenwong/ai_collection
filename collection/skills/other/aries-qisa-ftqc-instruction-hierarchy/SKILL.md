---
name: aries-qisa-ftqc-instruction-hierarchy
description: ARIES QISA methodology for FTQC control stacks. Use when designing or analyzing quantum instruction set architectures, classical-quantum control boundaries, cryogenic thermal budgets, or FTQC instruction execution.
category: systems-engineering
arxiv_id: "2610.17058"
source: https://arxiv.org/abs/2610.17058
authors: "Dmitry Filippov, Justin Hogaboam, Mathias Soeken, Raghu Gatta, Prakash Murali, Matthias Troyer"
published: "2026-10-12"
---

# ARIES QISA: Architecting Instruction Execution for Scalable FTQC

## Overview

FTQC at practical scale requires orchestrating millions of operations continuously across a
tightly coupled classical-quantum control stack. The central systems-engineering decision is
**where to place the hardware-software boundary** — the Quantum Instruction Set Architecture
(QISA). ARIES (Microsoft + Cambridge) provides a five-level abstraction hierarchy for QISAs
and an end-to-end evaluation toolflow (cycle-accurate classical driver + hardware engine
simulator) that measures the three coupled bottleneck resources:

1. **Issue bandwidth** (driver → engine): `BW_issue = k_L × s_L × f_L / η` — instructions per cycle × bit-width × issue frequency ÷ line-encoding efficiency (η ≈ 0.8 for 8b/10b)
2. **Return bandwidth** (engine → driver): `BW_return = m_L × r_L × f_L / η` — measurement results per cycle × result width × frequency
3. **Transceiver power**: `P_TRX = BW_total × E_bit`, viable only if `BW_total ≤ BW_cap` AND `P_TRX ≤ P_budget` (cryogenic cooling limit, ~1.5 W at 4K)

Scope: cryogenic fixed-connectivity platforms (superconducting transmons, topological
Majorana qubits) where the driver-engine interface physically crosses the dilution
refrigerator thermal boundary.

## The ARIES Five-Level QISA Hierarchy

| Level | Name | Operations | Key property |
|-------|------|-----------|--------------|
| 5 | Canonical Operations | AllocateQ/FreeQ, R(θ) rotations, CanonicalClifford, RemoteControlledClifford | Architecture-agnostic, all-to-all, variable control footprint |
| 4 | **Local Logical Operations** ⭐ recommended | Init/Meas, InitBell/MeasureBell, LocalClifford, LocalCNOT, LocalSWAP, LocalMove, CheckMagic, ConsumeMagic | QEC-agnostic, local 1-2 qubit ops only, deterministic latency, fixed bit-width |
| 3 | QEC-Native Logical | InitX/InitZ, MeasX/MeasZ, MeasXX/MeasZZ, MeasPauli, CheckMagic | Exposes QEC primitives (lattice surgery); implicit idling |
| 2 | QEC Micro-operations | InitData, MeasData, ExtractSyndrome, MergeBoundary, SplitBoundary, DistillCycle | Stabilizer patch building blocks, patch-ID addressing |
| 1 | Physical Operations | vMeasZ/vMeasX, vRx(θ), vCZ/vCNOT (SC); vJointParity (Majorana) | Per-physical-qubit + SIMD variants; current NISQ-era QISAs (eQASM, cQASM, OpenQASM) |

Each level decomposes into the level below via known gate identities. The driver performs
**JIT instruction translation** (full pre-compilation gives prohibitive binary sizes — 260 GB
for one factoring schedule), logical Pauli frame tracking, and defers correction gates by
commuting them through issued Clifford operations until synchronization points.

## Quantified Level Tradeoffs (8 applications × 2 platforms)

- **Level 1 (even with SIMD)**: 55 Tbps–20 Pbps issue bandwidth; violates dilution-fridge
  cooling by **>4000×**. Physical QISAs are strictly unusable at FTQC scale.
- **Level 1→2**: 6× issue BW, 12× return BW, 8× power improvement (syndrome pattern = 1 instr).
  Still infeasible — driver still feeds idling qubits and decodes all syndromes (XQSim-style
  Level 2 assumptions are unrealizable).
- **Level 2→3**: 214× issue, 490× return, 263× power — **implicit idling** (engine handles
  background syndrome extraction) is the single biggest win, since idling qubits vastly
  outnumber active ones. From Level 3 up, transceiver power fits cooling budgets.
- **Level 3→4** (recommended step): further 1.5× issue, **2.6× return (up to 5.2×)**, 1.6×
  power. Level 3 is measurement-heavy (driver maintains futures + issues correction gates);
  Level 4 absorbs those. Plus 1.3–1.4× kernel speedups (factoring, quantum chemistry).
- **Level 4→5**: abstracting further **worsens** issue bandwidth ~2× and underestimates
  routing congestion/runtimes. Level 5 engine needs 260k LUTs at 4096 logical qubits (router
  alone 217k LUTs > Kintex-7), with ~10× per-instruction latency variance.

Engine cost model (FPGA LUTs, validated by SystemVerilog synthesis):
`LUTs = L_decode + L_schedule + L_patch + L_meas`, `BRAM = N_instr × L_maxexp × W_µop`.
At 4096 logical qubits: Level 4 ≈ 40k LUTs (~0.5M gate-equiv ≈ 10–20 mW in 22nm cryo-CMOS =
1% of 4K budget) vs Level 5 ≈ 260k LUTs (~2.5M gate-equiv).

## Why Level 4 Wins (Architectural Design Rules)

1. **Deterministic latency + fixed instruction widths** → predictable engine timing, RISC-like
   encoding, no variable-bitwidth decode.
2. **QEC-agnosticism** → one engine serves surface codes AND Hastings-Haah (fewer rounds:
   3 vs 20 measurements per cycle) AND future codes; field hasn't converged on a code, so
   isolating that choice from the engine interface avoids re-verification per code change.
3. **Return-path awareness** → prior work optimized issue bandwidth only (Level 3); the
   return path (measurement results → decoder) is equally QISA-sensitive.
4. **Routing complexity stays in software** → remote operations synthesized by the driver from
   bounded local primitives; engine never does dynamic ancilla allocation/routing.
5. **Move from analytical resource estimation to cycle-level simulation** — standard practice
   in classical computer architecture, now required for quantum stacks.

## Related Skills

- `distributed-quantum-control-architecture` — HISQ ISA + BISP synchronization (multi-controller)
- `hi-hcqc-tightly-coupled-hybrid-quantum-control` — RFSoC/PCIe control hardware
- `riscv-quantum-control-processor` — vector-extension control processor design
- `real-time-qec-system-stack` — six-layer QEC decoding stack
- `qec-enabled-network-control` / `scope-syndrome-control-plane` — syndrome-driven control planes

## Key References

- ARIES paper (this skill): arXiv:2610.17058
- XQSim (Level 2 mixed abstraction): arXiv:2407.10407
- Issue-bandwidth abstraction (Level 3, defect-based surface codes): prior control-stack work
- Resource estimation with Level 5 ops: arXiv quantum resource estimation literature

**Activation**: QISA, quantum instruction set architecture, FTQC control stack, cryogenic
control bandwidth, dilution refrigerator thermal budget, instruction issue bandwidth, logical
ISA, fault-tolerant instruction execution, control engine FPGA sizing
