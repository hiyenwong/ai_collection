---
name: ppvm-quantum-digital-twin
description: Joint QPU, noise, control VM for quantum digital twins.
category: ai_collection
version: "1.0.0"
source: arXiv:2610.18225
source_title: "PPVM - A Circuit Simulation Framework for Digital Twins of Quantum Processors"
authors: "Xiu-Zhe Luo, David Plankensteiner, Kai-Hsin Wu, et al. (QuEra Computing)"
published: 2026-10-13
categories: quant-ph
trigger_words:
  - quantum digital twin
  - pauli propagation
  - generalized tableau simulation
  - atom loss
  - qec simulation
  - virtual machine quantum
  - measurement feed-forward
  - neutral atom noise
---

# PPVM: Quantum Processor Digital Twins

## Overview

PPVM (Programmable Pauli Virtual Machine) is an open-source framework emulating a quantum processor TOGETHER with its classical controller as a digital twin. The core insight: verifying early-FTQC hardware requires **joint emulation** of (1) the quantum processor, (2) hardware noise, and (3) classical control/decoding logic — none of the existing simulators combine all three.

## Core Architecture (reusable pattern)

### 1. Shared bytecode virtual machine
- Upstream compiler (e.g. Bloqade) emits bytecode containing **quantum, classical, AND debug instructions** in one program
- Virtual CPU: integer/float arithmetic + control flow (loops, branches), LIFO stack as working memory
- Virtual QPU: gates + noise channels, dispatched from the same stack — gate args popped, measurement results pushed back
- **Stack bridges classical control and quantum instructions** — feed-forward is just CPU branching on a stack value
- Atom loss reported as a distinct measurement outcome `m=2`, letting the CPU branch on loss events
- Breakpoints pause execution for full machine-state inspection (debugger + CLI)

### 2. Dual-backend unification under one abstraction
- **Generalized tableau** (Schrödinger picture): stabilizer tableau O(n²) + sparse coefficient vector over destabilizer basis; non-Clifford rotation at most doubles nonzero coefficients; supports sampled mid-circuit measurement, feed-forward, loss via classical flags
- **Pauli propagation** (Heisenberg picture): evolve observable O backwards through adjoint circuit; cost controlled by truncation (coefficient threshold, Hamming-weight cap); NO mid-circuit measurement/feed-forward (open problem)
- Backend selected per-program via `device` directive in bytecode header

### 3. Atom-loss channel theory (neutral atoms)
- Extended basis {I, X, Y, Z, L} with L = |L⟩⟨L| projector; 2×2 Paulis embedded as 3×3 with zero row/column (I=diag(1,1,0), Z=diag(1,-1,0), L=diag(0,0,1))
- **Gate representations differ from basis elements**: Z-gate = diag(1,-1,1) ≠ Z basis element (gate acts trivially on lost qubit — unit entry in loss subspace)
- Independent loss Kraus: K1=√p0|L⟩⟨0|, K2=√p1|L⟩⟨1|; state-dependent p0≠p1 supported (asymmetric loss)
- **Correlated loss during 2-qubit gates**: both-lost pLL, each-individually pLQ, partner-already-lost pLN (dynamics differ!) — survival prob 1−pLL−2pLQ
- Adjoint (Heisenberg) action: E†[P]=(1−p)P for computational Paulis; E†[L]=L+pI — no branching without reset ops
- Reset channel: K1=|0⟩⟨L|; adjoint E†[P]=P+L for P∈{I,Z} (counterintuitive L-generation is a Heisenberg-picture artifact: reset applied BEFORE backward loss channels)
- Truncation control: configurable cutoff on number of loss projectors per word; words with k loss projectors carry factor p^k

### 4. Conserved-quantity protection under truncation
- **Protected set**: user-specified Pauli words exempt from truncation
- Preserves overlap with conserved quantities (e.g. total magnetization M=ΣZi) exactly, if protection covers the quantity's expansion and truncation applied only after conserving gate blocks
- Verified: Heisenberg spin-correlation m(t) stays exactly at 1 with protection vs drifts below without
- Loss weighting: m(t)=(1−p)^k(t) for k(t) CZ gates — lossy lines reproduce analytical scaling exactly

### 5. Classical-mixture sampling
- Mixed state as Σ pk|ϕk⟩⟨ϕk|, each pure state a generalized tableau
- Noise channels branch the mixture; weights are probabilities (nonneg, sum 1)
- Cutoff C retains branches with pk>C, renormalize; caps terms at 1/C
- K bit-flip channels → retain-≤r-flips count = Σ_{j≤r} C(K,j) — avoids full 2^K blowup

## Key Results
- Loss-aware magic state distillation (5-to-1 Bravyi-Kitaev, triangular 4.8.8 color codes) scaled to **1435 qubits** (d=23), ~0.1s/shot single-thread Apple M4; noise adds small overhead vs noiseless
- Bloqade QEC Studio integration: gadget control-flow graph (prep/syndrome/gates/readout) + deq decoder in the loop — classical control branches on decoded logical outcomes, quantum state persists across gadgets
- Heisenberg dynamics with loss: correlated-loss channel attached to CZ gates only ([pLL,pLQ,pLN]=[p/3,p/3,p/3])

## Harness-Engineering Workflow (SE lesson)
Development combined human guidance + AI-agent optimization: (1) human writes reference implementation, (2) AI agent develops benchmarks/tests, (3) autotune evaluates candidates against benchmarks + reference + physics tests, (4) iterate. Recorded session: mixture-construction time ×5.04 via 7 accepted/rejected experiments — biggest win: **delay tableau cloning until after branch merging/truncation** (2025 branches retained); a rejected experiment (scalar hash without buffer) was caught by measurement and reverted. AI agents (Claude/Cursor/Codex) assisted implementation from Jan 2026; scientific content by humans.

## Activation

Use when: building quantum-processor simulators/digital twins, modeling atom loss/erasure noise, needing measurement-conditioned control flow in stabilizer simulation, verifying QEC+decoder co-design, neutral-atom architecture validation, or designing VM abstractions that mix classical and quantum instruction streams.

## Pitfalls
- Pauli propagation cannot represent mid-circuit measurement feed-forward (open problem); use tableau backend for adaptive programs
- Asymmetric loss (p0≠p1) in Pauli propagation branches identity → blowup; use symmetric approx when possible
- Gate matrix ≠ basis element in the extended 3×3 representation (loss-subspace entries)
- Reset in Heisenberg picture generates L terms — they vanish against computational initial states only if no loss channel precedes
- Compiled sampling modes (Stim/Tsim/Clifft) exploit circuit structure — unfair to compare against per-shot VM execution
