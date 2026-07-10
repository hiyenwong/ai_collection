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

- See: `references/witness-expansion-resource-detection.md` for Witness Expansion framework (arXiv:2606.27105)
- See: `references/quantum-software-engineering.md` for Qolumbina testing benchmark, CLAIMSTAB-QC auditing framework, CV vs DV paradigm comparison, and QPipe agentic quantum code generation

## Pattern 10: Quantum Software Engineering Patterns

Three critical gaps in quantum software research identified in 2026-07 papers:

### 10a. Benchmark Infrastructure (Qolumbina, arXiv:2607.02029)
Existing quantum software testing relies on scattered circuit-level benchmarks. Qolumbina curates 40 scalable programs with standardized interfaces, enabling fair comparison across testing approaches. Key insight: backend-dependent effects can skew QST results — always test across multiple backends.

### 10b. Empirical Comparison Auditing (CLAIMSTAB-QC, arXiv:2607.00516)
455 claims from 119 quantum software papers audited — only 8 had enough evidence for direct audit. Framework: record baselines/metrics/evidence → lock design before outcomes → classify as Sustained/Unresolved/Reversed. The "materialization gap" means most quantum software comparisons cannot be validated without proxy reconstruction.

### 10c. Controlled Paradigm Comparison (CV vs DV, arXiv:2607.00961)
To isolate quantum circuit effects: shared classical backbone + interchangeable quantum heads. Finding: CV-QNN achieves 79.7% vs DV-QNN 61.6% on wafer-map classification — 18-point gap rooted in CV's structured phase-space encoding, not Hilbert space dimensionality. DV limitation is representational capacity ceiling, not optimization failure.

## Pattern 11: Agentic Quantum Application Generation (QPipe, arXiv:2607.00939)

LLM-based multi-agent pipeline converting NL requirements into executable quantum applications. Six specialized agents: requirement parsing → formulation → code generation → review → execution → verification. Achieves 100% compilation and 96.7% execution rates. Generated solutions outperform genetic algorithm baseline. Ablation shows advantage requires ALL four components: code-gen skills, task knowledge, review feedback, and multi-agent decomposition.

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

## Pattern 8: Quantum-Enhanced Monte Carlo Tree Search (AtomTreeSearch)

Embed a quantum subroutine (MWIS on neutral-atom platform) within classical MCTS at each expansion step:
- **Quantum role**: Select diverse, high-quality candidate actions collectively via maximal weighted independent set
- **Classical role**: MCTS tree policy, simulation, backpropagation
- **Validated**: TSP up to 60 cities (random Euclidean) / 100 cities (TSPLIB), matching or exceeding OR-Tools
- **Advantage**: More diverse and higher-quality branches than classical greedy alternatives
- **NISQ-compatible**: Quantum subroutine is shallow and focused; graceful classical fallback available

**Key principle**: Carefully scoped quantum subroutines embedded in classical search frameworks represent a promising path toward near-term quantum utility.

## Pattern 9: Neural Surrogates for Quantum Bottlenecks

Replacing expensive classical subroutines in quantum workflows with trained neural network surrogates that approximate the same mapping at dramatically reduced computational cost.

**When to use**: Quantum workflows where a classical subroutine scales linearly (or worse) with problem size and dominates total computation — gradient estimation, operator selection, confidence estimation, syndrome decoding.

**Architecture pattern**:
```
Quantum Workflow Classical Bottleneck → Train NN on (input, ground_truth) pairs → 
Deploy NN as filter/shortlist/surrogate → Verify against ground truth on subset
```

**Key principle**: Neural networks can learn the structure of expensive classical computations from training data. Use the neural output as a surrogate that reduces resource consumption, then verify critical outputs against exact methods.

**Verified instances (2026-06-10)**:

1. **Gradient Estimation** (arXiv:2606.09734 — QUIVER): Forward gradient estimators using automatic differentiation framework replace parameter-shift rule. Tunes number of random directional derivatives to interpolate between SPSA (single-direction, cheap) and parameter-shift (full-gradient, expensive). Trains 60-qubit QNNs with 1770 parameters.

2. **Operator Selection** (arXiv:2606.08794 — GNN-VQE): GNN policy predicts next entangling operator for ADAPT-VQE from interaction graph and state observables. GNN as shortlist generator — rescoring few GNN-proposed candidates recovers near-oracle behavior while searching tiny fraction of pool. Validated on molecular benchmarks LiH, BeH2.

3. **Confidence Estimation** (arXiv:2606.08758): GNN decoder logit replaces MWPM logical gap for QEC confidence estimation. Neural decoder trained only on syndromes and logical labels learns both gap-like discrimination and quantitative confidence scale. Post-selection based on GNN logit yields lower logical error rate than MWPM gap.

**Design checklist**:
- [ ] Identify the bottleneck's input/output mapping
- [ ] Generate training data using exact/ground-truth method on representative instances
- [ ] Train surrogate on (input, output) pairs
- [ ] Deploy as filter: use surrogate to shortlist candidates, then verify with exact method
- [ ] Verify: compare surrogate output distribution against ground truth distribution
- [ ] Measure: resource reduction factor vs. accuracy degradation trade-off

**Pitfalls**:
- **Distribution shift**: Neural surrogate trained on one noise model or problem class may fail on others. Retrain or validate transferability (GNN-VQE tested on molecular benchmarks beyond spin models).
- **Verification budget**: Always reserve a fraction of evaluation budget for ground-truth verification — the surrogate can only be trusted to the extent it has been verified.
- **Training data cost**: Generating ground-truth training data may itself be expensive. Consider active learning or transfer learning from related problems.

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
