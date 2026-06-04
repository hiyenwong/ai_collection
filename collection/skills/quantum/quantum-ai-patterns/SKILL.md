---
name: quantum-ai-patterns
description: >
  Reusable research patterns at the intersection of quantum computing and artificial intelligence.
  Use when analyzing quantum machine learning papers, designing hybrid quantum-classical systems,
  or extracting architectural patterns from quantum-AI research. Covers QNN design, distributed
  quantum computing, AI-assisted error correction, and continuous-time quantum models.
  Triggers: quantum machine learning, QNN, quantum neural network, hybrid quantum-classical,
  quantum AI patterns, distributed quantum computing, quantum error correction AI.
---

# Quantum-AI Research Patterns

Reusable patterns extracted from analyzing quantum computing + AI research papers.

## Pattern 1: Quantum-Classical Hybrid Architecture

Hybrid systems where quantum processors handle specific subroutines while classical systems manage orchestration.

**When to use**: Problems with separable quantum-suitable and classical-suitable subproblems.

**Architecture**:
```
Classical Controller → Quantum Subroutine → Classical Post-processing
     ↓                      ↓                      ↓
  Control flow          Linear algebra          I/O, display
  Optimization loop     Sampling/estimation     Decision logic
```

**Key principle**: Decompose problems into:
- **Quantum-suitable**: Linear algebra, optimization, sampling, Fourier transforms
- **Classical-suitable**: Control flow, I/O, preprocessing, decision logic

**Examples**: VQE (Variational Quantum Eigensolver), QAOA, quantum kernel methods

## Pattern 2: Distributed Quantum Resource Management

Managing limited qubit resources across multiple quantum processing nodes.

**When to use**: Computation exceeds single-device qubit capacity.

**Key techniques**:
- Circuit cutting: partition quantum circuits across devices
- Quantum teleportation: inter-node quantum state transfer
- Classical communication: coordinate distributed quantum operations
- Error-aware scheduling: account for varying noise profiles across nodes

**Key principle**: When resources are constrained, distribute computation with explicit communication protocols.

## Pattern 3: Error-Corrected Learning

Using machine learning to optimize quantum error correction and vice versa.

**When to use**: Quantum systems with noisy operations requiring adaptive error management.

**Bidirectional benefits**:
- **AI → QEC**: Neural decoders for syndrome measurement, adaptive threshold optimization
- **QEC → AI**: Quantum-enhanced feature spaces, noise-robust training

**Key principle**: Use ML to optimize system-level parameters traditionally hand-tuned (error correction thresholds, scheduling, gate calibration).

## Pattern 5: LLM-Guided Evolutionary Search for Quantum Code Discovery

Using LLMs as mutation engines in an evolutionary search loop to discover quantum error-correcting codes.

**When to use**: Searching large algebraic design spaces for quantum codes (LDPC, bivariate-bicycle, surface codes) where exhaustive search is infeasible.

**Workflow**:
1. **LLM program mutation**: LLM mutates Python programs that generate code ansätze (BB, perturbed BB, etc.)
2. **Campaign execution**: ~330 iterations per campaign, ~40K candidates screened
3. **Staged validation pipeline** (early rejection for efficiency):
   - GF(2) rank computation → distance estimation → distance certification → MILP → BLISS Tanner-graph dedup → decomposability analysis → local-Clifford equivalence checks
4. **Independent evaluation**: Candidates certified through independent mathematical verification, not just LLM output

**Key results** (arXiv:2606.02418): 465 distinct codes at n≤360, including new indecomposable [[288,16,12]] code

**Cost considerations**: ~$400 LLM inference per campaign, ~140h compute — budget accordingly

**Key principle**: LLMs are powerful at generating diverse ansatz programs but weak at verification. Pair LLM creativity with independent mathematical certification (GF(2) rank, MILP, BLISS isomorphism) for reliable discovery.

## Pattern 6: Branch-Aware Compile-Time Optimization for Dynamic Quantum Circuits

Extending classical compiler analysis techniques (constant propagation, dead code elimination) to dynamic quantum circuits with mid-circuit measurements and classical feedforward.

**When to use**: Compiling dynamic quantum circuits that contain mid-circuit measurements, conditional blocks, and classical control flow based on measurement outcomes.

**Key innovation**: Classical constant propagation (QCP) only handles unitary circuits. **Branch-aware** extension (BQCP, arXiv:2606.02018) tracks:
- Classical information from mid-circuit measurements
- Post-measurement quantum states per execution branch
- Path-sensitive reasoning inside conditional blocks

**Scalability strategy**: Bound quantum-state representation size AND number of tracked branches to keep analysis tractable.

**Results**: Consistently achieves larger reductions than QCP on dynamic circuits. Accepted at IEEE QSW 2026.

**Key principle**: Quantum circuits with classical control flow require compiler analyses that reason about BOTH classical measurement outcomes and quantum post-measurement states simultaneously across all execution branches.

## Pattern 4: Continuous-Time Quantum Models

Continuous-time formulations bridging differential equations and quantum computing.

**When to use**: Modeling dynamical systems, time-series analysis, recurrent architectures.

**Key models**:
- CTRQNets (Continuous-Time Recurrent Quantum Networks)
- LQNets (Liquid Quantum Networks)
- Quantum neural ODEs

**Key principle**: Continuous-time models provide more natural representations for dynamical systems than discrete-time approximations.

## Search Queries for Paper Discovery

Effective arXiv search patterns:
- `cat:quant-ph AND cat:cs.LG` — Quantum ML papers
- `all:"quantum neural network"` — QNN papers
- `all:"distributed quantum"` — Distributed QC papers
- `all:"variational quantum"` — VQA/VQE papers
- `all:"quantum error correction" AND all:"machine learning"` — AI-assisted QEC
- `all:"quantum control"` — Quantum control theory
- `all:"quantum" AND all:"optimal control"` — Quantum optimal control
- `all:"quantum reliability"` — Quantum reliability engineering

## Knowledge Graph Integration

When importing papers into kg.db:
1. Categorize by primary domain: `quant-ph`, `cs.LG`, `cs.AI`, `cs.CV`
2. Tag cross-domain papers with multiple categories (e.g., `quant-ph, cs.LG`)
3. Use PageRank to identify foundational papers in the intersection field
4. Community detection reveals research clusters (typically: QML, QEC, QNN, Distributed QC)

## Vector Similarity Search for Paper Discovery

When using kg.db with vector embeddings (stored as 256-float32 in `kg_vectors`):

```python
import struct, math

def text_embedding(text, dim=256):
    vec = [0.0] * dim
    for w in text.lower().split():
        vec[abs(hash(w)) % dim] += 1.0
    norm = math.sqrt(sum(v*v for v in vec))
    return [v/norm for v in vec] if norm > 0 else vec

def cosine_sim(a, b):
    dot = sum(x*y for x,y in zip(a,b))
    return dot / (math.sqrt(sum(x*x for x in a)) * math.sqrt(sum(y*y for y in b)) + 1e-10)
```

**Embedding storage format**: 256 float32 values packed with `struct.pack('256f', *vec)` (1024 bytes). Read with `struct.unpack('256f', blob)`.

**Workflow**: Generate embeddings for query text → compare against all stored vectors → rank by cosine similarity → retrieve paper metadata by entity_id.

## arXiv API Fallback Chain (Updated 2026-05)

arXiv API reliability has degraded significantly. Use this fallback chain:

1. **First**: Check kg.db for existing cached papers (fastest, no network)
2. **Second**: `web_search` with `site:arxiv.org` — broad discovery without hitting API
3. **Third**: Browser navigation to `/list/{category}/recent` pages
4. **Fourth**: `terminal` + `curl` with `https://` (NOT `http://` — triggers security scan approval)
5. **Avoid**: `httpx` in `execute_code` — returns empty/0-byte responses for arXiv API

**Critical**: arXiv API returns HTTP 429 on ALL queries during high-traffic periods. Never rely on it as the sole method. If API fails, proceed with cached knowledge graph data — 800+ papers typically available in kg.db.

## NISQ Measurement Efficiency Patterns

From arXiv:2605.03729 (Ensemble Engineering):

**Problem**: Uniform ensemble sampling on NISQ devices causes destructive cancellation — operator-sign structure and ensemble weights mismatch suppresses relevant signals.

**Solution pattern**:
1. Reformulate correlator in basis-resolved representation: `⟨O⟩ = Σ_i w_i · s_i · |⟨ψ_i|O|ψ_i⟩|`
2. Align ensemble weights `w_i` with operator sign structure `s_i`
3. Two circuit constructions:
   - Grover-type amplitude amplification (structure-aligned benchmark)
   - Oracle-free shallow circuits (practical NISQ deployment)
4. Manage amplification-vs-noise tradeoff per-device

**When to apply**: Any quantum measurement protocol on NISQ hardware where signal-to-noise is limited by sampling inefficiency rather than raw noise.
