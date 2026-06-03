---
name: hdc-stdp-emergent
description: >
  Comprehensive methodology for emergent STDP in inverted Galois-field
  Hyperdimensional Computing (HDC). Derives the closed-form expression for
  STDP magnitude, documents the VaCoAl algorithm, SRAM-CAM hardware mapping,
  catastrophic forgetting mitigation, and path-dependent semantic selection.
  Bridges theoretical neuroscience with practical deterministic AI hardware.
tags:
  - hyperdimensional-computing
  - emergent-stdp
  - galois-field
  - vacoal
  - sram-cam
  - catastrophic-forgetting
  - neuromorphic
  - path-dependent-selection
trigger_keywords:
  - hyperdimensional computing
  - STDP emergent
  - VaCoAl
  - Galois field HDC
  - SRAM-CAM neuromorphic
  - catastrophic forgetting
  - path-dependent selection
  - closed-form STDP
  - inverted Galois-field
  - Vague Coincident Algorithm
  - hypervector binding
  - sparse distributed memory
related_skills:
  - hyperdimensional-stdp-computing
  - vacoul-hdc-sram-cam-ai
  - spiking-neural-network-analysis
  - snn-learning-survey
  - brain-inspired-memory-ai-agents
paper:
  title: >-
    "Beyond LLMs, Sparse Distributed Memory, and Neuromorphics: A
    Hyper-Dimensional SRAM-CAM 'VaCoAl' for Ultra-High Speed, Ultra-Low Power, and Low Cost"
  authors: [Chuma, Otsuka, Sato]
  arxiv: "2604.11665"
  year: 2026
---

# Emergent STDP in Hyperdimensional Computing (VaCoAl)

## 1. Overview — Inverted Galois-Field HDC Architecture

### 1.1 The Paradigm Shift

Conventional HDC uses Galois-field (GF) algebra to **converge** toward a
unique correct answer — error-correction drives noise out and collapses
the representation to a single symbol.

The **inverted Galois-field HDC** architecture does the opposite:

- GF algebra is used as an **engine for relative similarity ranking**, not
  convergence to a unique answer.
- Multiple candidate paths remain active simultaneously; their
  **path-quality is ranked** by collision-tolerance and coherence decay.
- The system **selects semantically** based on path-dependent evidence
  rather than deterministic unbinding alone.

### 1.2 Architecture Components

```
┌─────────────────────────────────────────────────────────┐
│                    Inverted GF-HDC                       │
├──────────────┬──────────────┬───────────────────────────┤
│   Encoder    │    Memory    │      Decoder / Selector   │
│              │              │                            │
│ Symbol → HV  │ SRAM-CAM     │ Path-quality ranking      │
│ Bind/Bundle  │ store (HV,D) │ STDP-equivalent selection │
│ Permute      │ lookup (HV)  │ CR score (reliability)    │
│ Unbind       │ parallel     │ Multi-path comparison     │
└──────────────┴──────────────┴───────────────────────────┘
```

### 1.3 Key Architectural Properties

| Property | Conventional HDC | Inverted GF-HDC (VaCoAl) |
|---|---|---|
| GF purpose | Error correction → unique answer | Relative similarity ranking |
| Path handling | Single-path, deterministic | Multi-path, quality-ranked |
| Selection | Threshold-based match | Path-dependent semantic selection |
| Plasticity | Explicit weight updates | Emergent from algebraic structure |
| Hardware | SRAM or DRAM | SRAM-CAM with parallel match |
| Forgetting | Weight overwrite | Orthogonal hypervectors (no interference) |

### 1.4 Core HDC Operations (Galois-Field GF(q))

```python
class InvertedGaloisFieldHDC:
    """
    Inverted Galois-field HDC for relative similarity ranking.
    
    Instead of converging to a single answer, this architecture
    maintains multiple candidate paths and ranks them by
    collision-tolerance and coherence decay.
    """
    
    def __init__(self, dim: int = 10_000, q: int = 2):
        self.dim = dim
        self.q = q  # GF(q) field order
        
    # --- Binding: GF(q) addition (⊗) ---
    def bind(self, hv1: np.ndarray, hv2: np.ndarray) -> np.ndarray:
        """Element-wise GF(q) addition: hv ⊗ hv' = (hv + hv') mod q"""
        return np.mod(hv1 + hv2, self.q)
    
    # --- Unbinding: GF(q) subtraction (⊘) ---
    def unbind(self, composite: np.ndarray, key: np.ndarray) -> np.ndarray:
        """Inverse binding: (composite ⊘ key) = (composite - key) mod q"""
        return np.mod(composite - key, self.q)
    
    # --- Bundling: GF(q) accumulation + threshold (⊕) ---
    def bundle(self, vectors: list[np.ndarray]) -> np.ndarray:
        """Superposition: majority-rule over GF(q) elements."""
        summed = np.sum(vectors, axis=0)
        return np.mod(np.round(summed), self.q)
    
    # --- Permutation: position encoding (ρ) ---
    def permute(self, hv: np.ndarray, shift: int = 1) -> np.ndarray:
        """Cyclic shift for encoding sequence order."""
        return np.roll(hv, shift)
    
    # --- Similarity: Hamming match fraction ---
    def similarity(self, hv1: np.ndarray, hv2: np.ndarray) -> float:
        """Fraction of matching elements (normalized Hamming similarity)."""
        return np.mean(hv1 == hv2)
    
    # --- Noise injection: simulate GF diffusion ---
    def diffuse(self, hv: np.ndarray, noise_rate: float) -> np.ndarray:
        """
        Apply GF(q) diffusion noise.
        Each element flips to a random GF(q) value with probability noise_rate.
        """
        mask = np.random.random(self.dim) < noise_rate
        noisy = hv.copy()
        noisy[mask] = np.random.randint(0, self.q, size=np.sum(mask))
        return noisy
```

---

## 2. Derivation of Emergent STDP from HDC Operations

### 2.1 The Key Insight

In the inverted GF-HDC architecture, **collision-tolerance** — the ability
of the system to tolerate element-wise conflicts during bundling — creates
a **path-dependent pruning** mechanism:

1. **Multiple reasoning paths** compete simultaneously.
2. **Longer paths** accumulate more collision noise (more bundling
   operations → more element-wise conflicts in GF(q)).
3. **Shorter paths** maintain higher coherence (fewer operations → less
   accumulated noise).
4. The system **selects shorter, more coherent paths** — behaviorally
   equivalent to STDP's temporal preference.

### 2.2 Formal Derivation

Let a reasoning path be a sequence of $L$ binding operations:

$$H_L = h_1 \otimes h_2 \otimes \cdots \otimes h_L$$

where each $h_i \in \text{GF}(q)^D$ is a hypervector of dimension $D$.

**Collision model**: When two hypervectors are bundled, each element
position experiences a collision with probability:

$$P_{\text{collision}} = 1 - \frac{1}{q}$$

For GF(2) (binary), $P_{\text{collision}} = 0.5$.

After $L$ bundling operations, the probability that an element remains
unperturbed is:

$$P_{\text{clean}}(L) = \left(\frac{1}{q}\right)^L$$

The **expected coherence** (fraction of unperturbed elements) after $L$
operations:

$$C(L) = \frac{1}{q^L} + \left(1 - \frac{1}{q^L}\right) \cdot \frac{1}{q}$$

For GF(2):

$$C(L) = \frac{1}{2^L} + \frac{1}{2} \left(1 - \frac{1}{2^L}\right) = \frac{1}{2} + \frac{1}{2^{L+1}}$$

### 2.3 Emergent STDP Mapping

Map path length $L$ to temporal interval $\Delta t$:

$$L \leftrightarrow \frac{|\Delta t|}{\tau_0}$$

where $\tau_0$ is a characteristic timescale (number of operations per
time unit).

The **coherence-based selection weight** becomes:

$$W(\Delta t) = C\left(\frac{|\Delta t|}{\tau_0}\right) - \frac{1}{q}$$

The subtraction of $1/q$ removes the baseline random-match level,
isolating the **signal above chance**.

For GF(2):

$$W(\Delta t) = \frac{1}{2^{L+1}} = \frac{1}{2} \cdot \exp\left(-\frac{|\Delta t|}{\tau_0} \ln 2\right)$$

This is **exponential decay** — identical to the STDP window function:

$$\Delta w = A \cdot \exp\left(-\frac{|\Delta t|}{\tau}\right)$$

where:
- $A = 1/2$ (maximum potentiation for GF(2))
- $\tau = \tau_0 / \ln 2$ (effective time constant)

### 2.4 Causal vs. Anti-Causal

The inverted GF-HDC architecture distinguishes causal from anti-causal
through **permutation direction**:

- **Causal** (pre → post): forward permutation $\rho(h)$
- **Anti-causal** (post → pre): inverse permutation $\rho^{-1}(h)$

The coherence differs:

$$W_{\text{causal}}(\Delta t > 0) = A_+ \exp(-|\Delta t|/\tau_+)$$
$$W_{\text{anti-causal}}(\Delta t < 0) = -A_- \exp(-|\Delta t|/\tau_-)$$

where the asymmetry $A_+ \neq A_-$ arises from **directional diffusion**
in the GF bundling process.

```python
def derive_stdp_from_hdc(
    delta_t: float,
    tau_0: float = 1.0,
    q: int = 2,
    asymmetric: bool = True
) -> float:
    """
    Compute the emergent STDP weight change from HDC coherence decay.
    
    Args:
        delta_t: Time difference (post-spike time - pre-spike time).
        tau_0: Characteristic timescale (operations per time unit).
        q: Galois field order.
        asymmetric: Whether to use causal/anti-causal asymmetry.
    
    Returns:
        delta_w: STDP-like weight change.
    """
    L = abs(delta_t) / tau_0  # Path length equivalent
    
    # Coherence above random baseline
    coherence = (1/q**L) + (1 - 1/q**L) * (1/q)
    baseline = 1/q
    signal = coherence - baseline  # = 1/q^(L+1)
    
    if asymmetric:
        if delta_t > 0:
            # Causal: full signal
            amplitude = 1.0
        else:
            # Anti-causal: attenuated (directional diffusion)
            amplitude = -0.5
    else:
        amplitude = 1.0 if delta_t > 0 else -1.0
    
    return amplitude * signal
```

---

## 3. Closed-Form Expression for STDP Magnitude

### 3.1 The Expression

The closed-form prediction for the STDP-equivalent magnitude in the
inverted GF-HDC architecture:

$$\boxed{\Delta W(L) = \frac{1}{q^{L+1}}}$$

where $L$ is the effective path length (number of bundling/bind operations).

In temporal form:

$$\boxed{\Delta W(\Delta t) = \frac{1}{q} \cdot \exp\left(-\frac{|\Delta t|}{\tau_0} \ln q\right)}$$

### 3.2 Parameter Mapping

| Biological STDP | HDC Equivalent | Expression |
|---|---|---|
| Maximum weight change $A$ | $1/q$ | $0.5$ for GF(2) |
| Time constant $\tau$ | $\tau_0 / \ln q$ | $\tau_0 / \ln 2 \approx 1.44\tau_0$ |
| Exponential decay | Coherence decay | $q^{-L}$ |
| Asymmetry ratio | Diffusion directionality | $A_-/A_+ \approx 0.5$ |

### 3.3 Validation Against Measurements

The closed-form expression matches **measured values** from the VaCoAl
system:

```python
def validate_closed_form(
    measured_values: list[float],
    path_lengths: list[int],
    q: int = 2,
    tolerance: float = 0.05
) -> dict:
    """
    Validate the closed-form STDP prediction against measured data.
    
    Args:
        measured_values: Experimentally measured STDP magnitudes.
        path_lengths: Corresponding path lengths for each measurement.
        q: Galois field order.
        tolerance: Acceptable relative error.
    
    Returns:
        Dictionary with validation results.
    """
    predicted = [1.0 / (q ** (L + 1)) for L in path_lengths]
    
    errors = []
    for m, p in zip(measured_values, predicted):
        rel_error = abs(m - p) / (p + 1e-10)
        errors.append(rel_error)
    
    return {
        "predicted": predicted,
        "measured": measured_values,
        "relative_errors": errors,
        "max_error": max(errors),
        "mean_error": sum(errors) / len(errors),
        "within_tolerance": all(e < tolerance for e in errors),
    }
```

### 3.4 Numerical Examples

```python
# STDP magnitude table for GF(2)
print(f"{'Path L':<8} {'ΔW (closed-form)':<20}")
print(f"{'─' * 8} {'─' * 20}")
for L in range(1, 8):
    dw = 1.0 / (2 ** (L + 1))
    print(f"{L:<8} {dw:<20.6f}")

# Output:
# Path L   ΔW (closed-form)    
# ──────── ────────────────────
# 1        0.250000            
# 2        0.125000            
# 3        0.062500            
# 4        0.031250            
# 5        0.015625            
# 6        0.007812            
# 7        0.003906    
```

---

## 4. VaCoAl Algorithm — Path-Dependent Selection

### 4.1 Algorithm Overview

**VaCoAl** (Vague Coincident Algorithm) performs **path-dependent semantic
selection** by ranking competing reasoning paths using coherence metrics
derived from the inverted GF-HDC architecture.

### 4.2 Full Algorithm

```python
class VaCoAlAlgorithm:
    """
    VaCoAl: Vague Coincident Algorithm for path-dependent semantic selection.
    
    Steps:
    1. Encode all candidate items as hypervectors
    2. Build reasoning paths via binding sequences
    3. Score each path by coherence decay (CR Score)
    4. Select top-ranked path(s) based on quality
    5. Return result with reliability metric
    """
    
    def __init__(self, dim: int = 10_000, q: int = 2):
        self.hdc = InvertedGaloisFieldHDC(dim, q)
        self.dim = dim
        self.q = q
        self.memory: dict[str, np.ndarray] = {}
        self.path_registry: list[dict] = []
    
    # --- Step 1: Encode ---
    def encode(self, symbol: str) -> np.ndarray:
        """Encode symbol as random hypervector (or retrieve cached)."""
        if symbol not in self.memory:
            self.memory[symbol] = np.random.randint(0, self.q, size=self.dim)
        return self.memory[symbol].copy()
    
    # --- Step 2: Build paths ---
    def build_path(
        self, start: str, relations: list[tuple[str, str]]
    ) -> dict:
        """
        Build a reasoning path via sequential binding.
        
        Args:
            start: Starting symbol.
            relations: List of (relation_name, target_symbol) tuples.
        
        Returns:
            Path dictionary with composite hypervector and metadata.
        """
        current = self.encode(start)
        composites = [current.copy()]
        
        for rel_name, target in relations:
            rel_hv = self.encode(f"REL:{rel_name}")
            target_hv = self.encode(target)
            
            # Bind: current ⊗ relation → query vector
            query = self.hdc.bind(current, rel_hv)
            
            # Bundle with target for storage
            composite = self.hdc.bundle([query, target_hv])
            
            composites.append(composite.copy())
            current = target_hv.copy()
        
        return {
            "start": start,
            "relations": relations,
            "composites": composites,
            "length": len(relations),
        }
    
    # --- Step 3: Score paths (CR Score) ---
    def score_path(self, path: dict) -> float:
        """
        Compute CR (Coherence Reliability) Score for a path.
        
        CR Score = average pairwise coherence between consecutive composites.
        Penalizes longer paths (more collisions = lower coherence).
        """
        composites = path["composites"]
        L = path["length"]
        
        if L == 0:
            return 1.0
        
        similarities = []
        for i in range(len(composites) - 1):
            sim = self.hdc.similarity(composites[i], composites[i + 1])
            similarities.append(sim)
        
        avg_coherence = np.mean(similarities)
        
        # Length penalty (exponential decay, matches closed-form)
        length_penalty = 1.0 / (self.q ** (L + 1))
        
        # Combine: CR Score is coherence scaled by expected signal
        cr_score = avg_coherence * length_penalty
        
        return cr_score
    
    # --- Step 4: Rank and select ---
    def rank_paths(self, paths: list[dict]) -> list[dict]:
        """Score and rank all candidate paths."""
        scored = []
        for path in paths:
            cr = self.score_path(path)
            # Also compute closed-form prediction
            closed_form = 1.0 / (self.q ** (path["length"] + 1))
            scored.append({
                **path,
                "cr_score": cr,
                "closed_form_prediction": closed_form,
            })
        
        scored.sort(key=lambda x: x["cr_score"], reverse=True)
        return scored
    
    # --- Step 5: Select ---
    def select(
        self, start: str, candidate_paths: list[list[tuple[str, str]]],
        top_k: int = 1
    ) -> list[dict]:
        """
        Build, score, and select the best reasoning paths.
        
        Args:
            start: Starting symbol.
            candidate_paths: List of relation sequences to evaluate.
            top_k: Number of top paths to return.
        """
        built = [self.build_path(start, rels) for rels in candidate_paths]
        ranked = self.rank_paths(built)
        return ranked[:top_k]
    
    # --- Full multi-hop reasoning ---
    def reason(
        self, query: tuple[str, str], knowledge: list[tuple[str, str, str]]
    ) -> dict:
        """
        Full VaCoAl reasoning with multi-path exploration.
        
        Args:
            query: (subject, relation) to resolve.
            knowledge: List of (subject, relation, object) triples.
        
        Returns:
            Result with answer, CR score, and all explored paths.
        """
        subject, relation = query
        
        # Encode knowledge
        for s, r, o in knowledge:
            self.encode(s)
            self.encode(f"REL:{r}")
            self.encode(o)
        
        # Find all paths from subject through relation
        direct_hits = [(s, o) for s, r, o in knowledge if s == subject and r == relation]
        
        if direct_hits:
            # Direct match — highest coherence
            best_o = direct_hits[0][1]
            return {
                "answer": best_o,
                "cr_score": 1.0 / (self.q ** 2),  # L=1 path
                "path_type": "direct",
                "all_answers": [o for _, o in direct_hits],
            }
        
        # Multi-hop: find intermediate paths
        intermediates = [
            (s, o) for s, r, o in knowledge if s == subject
        ]
        
        candidate_paths = []
        for _, inter in intermediates:
            second_hops = [
                (rel, o) for s, r, o in knowledge
                if s == inter and r != relation
            ]
            for r2, o2 in second_hops:
                candidate_paths.append([(relation, inter), (r2, o2)])
        
        if not candidate_paths:
            return {"answer": None, "cr_score": 0.0, "path_type": "no_path"}
        
        ranked = self.select(subject, candidate_paths, top_k=1)
        best = ranked[0]
        
        last_rel, last_target = best["relations"][-1]
        return {
            "answer": last_target,
            "cr_score": best["cr_score"],
            "path_type": "multi_hop",
            "path": best["relations"],
            "length": best["length"],
        }
```

### 4.3 Path-Dependent Selection Properties

1. **Preferential attachment to short paths**: The $q^{-(L+1)}$ decay
   means shorter paths are exponentially favored.
2. **No explicit training**: Selection emerges from algebraic properties,
   not learned weights.
3. **Deterministic**: Same inputs always produce same rankings.
4. **Transparent**: CR Score provides interpretable confidence.
5. **Parallelizable**: All paths can be scored simultaneously.

---

## 5. SRAM-CAM Hardware Implementation

### 5.1 Hardware Architecture

VaCoAl maps naturally to **SRAM-CAM** (Static RAM + Content-Addressable
Memory) because:

| HDC Operation | SRAM-CAM Hardware Mapping |
|---|---|
| **Store** | Write hypervector to SRAM row |
| **Lookup** | CAM parallel match: all rows compared simultaneously |
| **Bind (GF add)** | XOR gate array (bitwise parallel) |
| **Unbind (GF sub)** | Same XOR (self-inverse in GF(2)) |
| **Bundle (majority)** | Column-wise population count + threshold |
| **Similarity** | XNOR + popcount (single cycle in CAM) |
| **Permute** | Fixed wiring permutation (no logic needed) |

### 5.2 SRAM-CAM Data Path

```
┌──────────────────────────────────────────────────────┐
│                   SRAM-CAM Array                      │
│                                                       │
│  [HV Row 0]  ──┐                                      │
│  [HV Row 1]  ──┤                                      │
│  [HV Row 2]  ──┤──→ Parallel match lines ──→ Match    │
│  [HV Row 3]  ──┤                                    flags
│  [HV Row N]  ──┘                                      │
│                                                       │
│  Query HV ──→ CAM match lines (all N rows in 1 cycle) │
│                                                       │
│  XOR array ──→ Bind/Unbind (element-wise GF add)     │
│  Popcount ──→ Similarity score                       │
│  Majority ──→ Bundle output                          │
└──────────────────────────────────────────────────────┘
```

### 5.3 Hardware Implementation Guide

```python
class SRAM_CAM_VaCoAl:
    """
    Simulated SRAM-CAM implementation of VaCoAl.
    Maps HDC operations to hardware-equivalent circuits.
    """
    
    def __init__(self, dim: int = 10_000, num_rows: int = 1024):
        self.dim = dim
        self.num_rows = num_rows
        # SRAM array: each row stores one hypervector
        self.sram = np.zeros((num_rows, dim), dtype=np.uint8)
        self.valid = np.zeros(num_rows, dtype=bool)
        self.next_row = 0
    
    # --- SRAM WRITE: Single cycle ---
    def write(self, index: int, hv: np.ndarray):
        """Write hypervector to SRAM row. Single-cycle write."""
        if index < self.num_rows:
            self.sram[index] = hv.astype(np.uint8)
            self.valid[index] = True
    
    # --- CAM MATCH: Parallel (1 cycle) ---
    def cam_match(self, query: np.ndarray) -> list[tuple[int, float]]:
        """
        Content-addressable match: compare query against ALL rows.
        
        Hardware: Match lines activate in parallel for all rows.
        Returns (row_index, similarity) for all valid rows.
        """
        results = []
        for i in range(self.num_rows):
            if not self.valid[i]:
                continue
            # XNOR + popcount in hardware (single cycle)
            matches = np.sum(self.sram[i] == query)
            similarity = matches / self.dim
            results.append((i, similarity))
        return sorted(results, key=lambda x: x[1], reverse=True)
    
    # --- BIND: XOR gate array (1 cycle) ---
    def bind_hw(self, row_a: int, row_b: int) -> np.ndarray:
        """
        Hardware bind: XOR gate array between two SRAM rows.
        
        All dim bits processed in parallel. 1 cycle latency.
        """
        a = self.sram[row_a].astype(np.uint8)
        b = self.sram[row_b].astype(np.uint8)
        return np.bitwise_xor(a, b)
    
    # --- BUNDLE: Column popcount + threshold ---
    def bundle_hw(self, row_indices: list[int]) -> np.ndarray:
        """
        Hardware bundle: column-wise population count + majority threshold.
        
        All columns processed in parallel. 1 cycle for popcount + 1 for threshold.
        """
        subset = self.sram[row_indices].astype(np.uint8)
        counts = np.sum(subset, axis=0)
        return (counts >= len(row_indices) / 2).astype(np.uint8)
    
    # --- Performance estimates (typical 28nm CMOS) ---
    def hardware_specs(self) -> dict:
        return {
            "lookup_latency_cycles": 1,          # CAM parallel match
            "bind_latency_cycles": 1,            # XOR gate array
            "bundle_latency_cycles": 2,          # Popcount + threshold
            "permute_latency_cycles": 0,         # Fixed wiring (no delay)
            "power_lookup_nJ": 0.01,             # Ultra-low: match lines
            "power_bind_pJ": 0.001,              # XOR gates
            "power_idle_nW": 100,                # SRAM standby
            "throughput_paths_per_us": 1000,     # Parallel path evaluation
            "area_mm2": 1.5,                     # 1024 rows × 10K dims
            "process_node_nm": 28,
        }
```

### 5.4 Hardware Design Considerations

1. **Bit-serial vs. bit-parallel**: For $D > 4096$, consider bit-serial
   processing to reduce routing congestion.
2. **Match-line capacitance**: Long CAM match lines slow down with more
   rows. Partition into sub-arrays (e.g., 256 rows each).
3. **Power gating**: Only activate rows that are valid. Unused rows
   contribute to leakage.
4. **Error tolerance**: The inherent noise tolerance of HDC means
   occasional bit-flip errors in SRAM do not significantly affect results.
5. **Scalability**: Adding more rows increases capacity linearly but
   match time sub-linearly (due to partitioning).

---

## 6. Catastrophic Forgetting Mitigation

### 6.1 Why HDC Avoids Catastrophic Forgetting

Traditional neural networks suffer from catastrophic forgetting because:

- **Shared weights**: New patterns modify the same weights used by old
  patterns.
- **Gradient interference**: Updates for new data corrupt old knowledge.

Inverted GF-HDC **does not have this problem**:

- **Orthogonal storage**: Each symbol is stored as a random high-dimensional
  hypervector. With $D = 10{,}000$, the expected cosine similarity between
  any two random vectors is $\approx 0$.
- **No weight sharing**: Adding a new item simply writes a new row — it
  does not modify existing rows.
- **Additive memory**: Bundling is additive; removing an item requires
  unbinding, not weight overwriting.

### 6.2 Forgetting Mechanisms (When Desired)

While catastrophic forgetting is avoided, the system supports
**controlled forgetting**:

```python
class ForgettingMechanism:
    """
    Controlled forgetting mechanisms for HDC memory.
    
    These are optional — the base system has no forgetting.
    """
    
    def __init__(self, hdc: InvertedGaloisFieldHDC):
        self.hdc = hdc
        self.usage_counts: dict[str, int] = {}
        self.timestamps: dict[str, float] = {}
    
    def track_access(self, symbol: str):
        """Track symbol access for LRU-based forgetting."""
        self.usage_counts[symbol] = self.usage_counts.get(symbol, 0) + 1
    
    def lru_forget(
        self, memory: dict[str, np.ndarray],
        keep_top_k: int
    ) -> dict[str, np.ndarray]:
        """
        Least Recently Used forgetting.
        Keep top_k most frequently accessed symbols.
        """
        sorted_items = sorted(
            memory.items(),
            key=lambda x: self.usage_counts.get(x[0], 0),
            reverse=True
        )
        return dict(sorted_items[:keep_top_k])
    
    def time_decay_forget(
        self, memory: dict[str, np.ndarray],
        current_time: float, decay_threshold: float
    ) -> dict[str, np.ndarray]:
        """
        Time-based decay forgetting.
        Remove symbols not accessed since decay_threshold.
        """
        return {
            symbol: hv for symbol, hv in memory.items()
            if self.timestamps.get(symbol, 0) > decay_threshold
        }
    
    def capacity_forget(
        self, memory: dict[str, np.ndarray],
        max_items: int, strategy: str = "lru"
    ) -> dict[str, np.ndarray]:
        """
        Capacity-based forgetting when memory is full.
        """
        if len(memory) <= max_items:
            return memory
        
        if strategy == "lru":
            return self.lru_forget(memory, max_items)
        elif strategy == "random":
            import random
            to_remove = random.sample(
                list(memory.keys()), len(memory) - max_items
            )
            return {k: v for k, v in memory.items() if k not in to_remove}
        else:
            raise ValueError(f"Unknown strategy: {strategy}")
```

### 6.3 Interference Analysis

Even without explicit forgetting, there is **theoretical interference**
from bundling multiple items:

**Expected interference after storing $N$ items in $D$ dimensions (GF(2))**:

$$P_{\text{error}}(N, D) \approx \frac{1}{2} \cdot \text{erfc}\left(\frac{\sqrt{D}}{2\sqrt{N}}\right)$$

For $D = 10{,}000$, $N = 1{,}000$:

$$P_{\text{error}} \approx \frac{1}{2} \cdot \text{erfc}\left(\frac{100}{2\sqrt{1000}}\right) \approx \frac{1}{2} \cdot \text{erfc}(1.58) \approx 0.013$$

**Practical guidance**:
- $D = 10{,}000$: Can store ~1,000 items with <2% error
- $D = 100{,}000$: Can store ~10,000 items with <2% error
- Error probability decreases **exponentially** with $D$

### 6.4 Comparison with Neural Network Forgetting

| Aspect | Traditional NN | Inverted GF-HDC |
|---|---|---|
| **New pattern storage** | Modifies shared weights | Writes new row (no modification) |
| **Old pattern degradation** | Gradient interference | Only from bundling collisions |
| **Degradation rate** | Rapid (catastrophic) | Gradual (controlled by $D/N$ ratio) |
| **Mitigation needed** | Replay, regularization, elastic weights | None by default; optional capacity mgmt |
| **Perfect recall** | Impossible after many updates | Achievable if $D \gg N$ |

---

## 7. Comparison with Traditional STDP

### 7.1 Side-by-Side Comparison

| Feature | Biological STDP | Emergent STDP (Inverted GF-HDC) |
|---|---|---|
| **Mechanism** | Calcium-dependent synaptic modification | Collision-tolerance in GF bundling |
| **Time window** | ~20-100 ms | Path length (abstract time) |
| **Potentiation** | Pre→Post: $A_+ e^{-\Delta t/\tau_+}$ | Coherence: $1/q^{L+1}$ |
| **Depression** | Post→Pre: $-A_- e^{\Delta t/\tau_-}$ | Anti-causal diffusion attenuation |
| **Implementation** | Biological synapses | XOR gates + popcount in SRAM-CAM |
| **Energy per update** | ~10⁶ ATP molecules | ~1 pJ (CMOS) |
| **Speed** | Milliseconds | Nanoseconds (hardware) |
| **Determinism** | Stochastic (probabilistic release) | Deterministic (algebraic) |
| **Predictability** | Empirical fit | Closed-form exact prediction |
| **Scalability** | Limited by biology | Linear with $D$ and rows |
| **Hardware** | N/A (biological) | Standard CMOS SRAM-CAM |
| **Training required** | No (inherent to synapse) | No (emergent from architecture) |
| **Forgetting** | Natural synaptic decay | Orthogonal storage (no interference) |

### 7.2 Why Emergent STDP Matters

1. **No explicit learning rule needed**: The STDP-like behavior emerges
   from the algebraic structure — there is no separate "learning" phase.
2. **Hardware efficiency**: Implementing STDP in neuromorphic hardware
   requires complex spike-timing circuits. In GF-HDC, it's just XOR +
   popcount.
3. **Predictable**: The closed-form expression allows **a priori**
   prediction of learning behavior — no empirical fitting.
4. **Scalable**: Works at any dimension $D$ and any number of paths.
5. **Bridges paradigms**: Shows that biological learning rules can emerge
   from purely algebraic/computational structures.

### 7.3 Equivalence Proof Sketch

The equivalence between traditional STDP and emergent STDP rests on three
observations:

1. **Exponential decay**: Both use exponential decay with temporal/spatial
   distance.
   - STDP: $\Delta w \propto e^{-|\Delta t|/\tau}$
   - HDC: $\Delta W \propto q^{-L} = e^{-L \ln q}$

2. **Causal asymmetry**: Both show stronger potentiation for causal
   (pre→post) than anti-causal ordering.
   - STDP: $A_+ > A_-$
   - HDC: Directional diffusion creates $A_-/A_+ \approx 0.5$

3. **Path competition**: Both select the "best" path among competing
   alternatives.
   - STDP: Strongest synapses survive, weak ones depress
   - HDC: Highest-coherence paths win, noisy ones are pruned

---

## 8. Implementation Guide — Step by Step

### Step 1: Set Up the HDC Basis

```python
import numpy as np

DIM = 10_000
Q = 2  # GF(2) — binary hypervectors

class HDCBasis:
    def __init__(self, dim, q, seed=42):
        self.dim = dim
        self.q = q
        self.rng = np.random.RandomState(seed)
        self.vectors = {}
    
    def get(self, symbol):
        if symbol not in self.vectors:
            self.vectors[symbol] = self.rng.randint(0, self.q, self.dim)
        return self.vectors[symbol].copy()
    
    def similarity(self, a, b):
        return np.mean(a == b)
```

### Step 2: Implement Core Operations

```python
def bind(a, b, q=2):
    """GF(q) binding (element-wise addition)."""
    return np.mod(a + b, q)

def unbind(composite, key, q=2):
    """GF(q) unbinding (element-wise subtraction)."""
    return np.mod(composite - key, q)

def bundle(vectors, q=2):
    """GF(q) bundling (majority vote)."""
    return np.mod(np.round(np.sum(vectors, axis=0)), q)

def permute(hv, shift=1):
    """Cyclic permutation for position encoding."""
    return np.roll(hv, shift)
```

### Step 3: Compute Emergent STDP

```python
def emergent_stdp(delta_t, tau_0=1.0, q=2):
    """
    Compute emergent STDP magnitude from closed-form expression.
    
    Args:
        delta_t: Time difference (positive = causal).
        tau_0: Operations per time unit.
        q: GF order.
    
    Returns:
        Weight change (positive = potentiation, negative = depression).
    """
    L = abs(delta_t) / tau_0
    magnitude = 1.0 / (q ** (L + 1))
    
    # Asymmetric: causal positive, anti-causal negative
    sign = 1.0 if delta_t > 0 else -0.5
    return sign * magnitude
```

### Step 4: Build and Rank Paths (VaCoAl)

```python
def build_and_rank_paths(start, path_candidates, basis, q=2):
    """
    Build reasoning paths and rank by CR score.
    
    Args:
        start: Starting symbol.
        path_candidates: List of relation sequences.
        basis: HDCBasis instance.
        q: GF order.
    """
    scored_paths = []
    
    for rels in path_candidates:
        # Build path
        current = basis.get(start)
        composites = [current.copy()]
        
        for rel_name, target in rels:
            rel_hv = basis.get(f"REL:{rel_name}")
            query = bind(current, rel_hv, q)
            target_hv = basis.get(target)
            composite = bundle([query, target_hv], q)
            composites.append(composite.copy())
            current = target_hv.copy()
        
        # Score
        L = len(rels)
        similarities = [
            basis.similarity(composites[i], composites[i+1])
            for i in range(len(composites) - 1)
        ]
        avg_coherence = np.mean(similarities)
        cr_score = avg_coherence / (q ** (L + 1))
        closed_form = 1.0 / (q ** (L + 1))
        
        scored_paths.append({
            "path": rels,
            "cr_score": cr_score,
            "closed_form": closed_form,
            "length": L,
        })
    
    scored_paths.sort(key=lambda x: x["cr_score"], reverse=True)
    return scored_paths
```

### Step 5: Verify Closed-Form Prediction

```python
def verify_prediction(measured_dws, path_lengths, q=2):
    """Verify closed-form STDP prediction matches measurements."""
    predicted = [1.0 / (q ** (L + 1)) for L in path_lengths]
    
    print(f"{'Length':<8} {'Measured':<12} {'Predicted':<12} {'Error':<10}")
    print("─" * 42)
    for L, m, p in zip(path_lengths, measured_dws, predicted):
        err = abs(m - p) / p
        print(f"{L:<8} {m:<12.6f} {p:<12.6f} {err*100:<10.2f}%")
    
    mean_err = np.mean([abs(m-p)/p for m, p in zip(measured_dws, predicted)])
    print(f"\nMean relative error: {mean_err*100:.2f}%")
    return mean_err < 0.05  # 5% tolerance
```

---

## 9. Quick Reference Card

| Concept | Formula / Value |
|---|---|
| **STDP closed-form** | $\Delta W(L) = q^{-(L+1)}$ |
| **Temporal form** | $\Delta W(\Delta t) = q^{-1} \cdot \exp(-|\Delta t|\ln q/\tau_0)$ |
| **GF(2) max weight** | $A = 0.5$ |
| **Effective time constant** | $\tau = \tau_0 / \ln 2 \approx 1.44\tau_0$ |
| **Interference prob** | $P_{\text{error}} \approx \frac{1}{2}\text{erfc}(\sqrt{D}/2\sqrt{N})$ |
| **Similarity** | Hamming match fraction: $\frac{1}{D}\sum_i [h_{1,i} = h_{2,i}]$ |
| **CR Score** | $\text{avg\_coherence} \times q^{-(L+1)}$ |
| **Hardware latency** | Lookup: 1 cycle, Bind: 1 cycle, Bundle: 2 cycles |
| **Energy per op** | ~1 pJ (CMOS 28nm) |

---

## 10. Pitfalls and Troubleshooting

### Pitfall 1: Dimensionality Too Low
- **Symptom**: High interference, poor recall, CR scores unreliable.
- **Fix**: Increase $D$ to at least 4,096. For >1,000 items, use $D \geq
  10{,}000$.

### Pitfall 2: GF Order Mismatch
- **Symptom**: Binding/unbinding produces incorrect results.
- **Fix**: Ensure all operations use the same $q$. GF(2) uses XOR, GF(q>2)
  uses modular arithmetic.

### Pitfall 3: Permutation Direction
- **Symptom**: Sequence decoding produces wrong order.
- **Fix**: Encode with $\rho^i$, decode with $\rho^{-i}$. Permutation is
  its own inverse only for specific shift values.

### Pitfall 4: Bundle Saturation
- **Symptom**: Bundled vector converges to all-same value (no information).
- **Fix**: Limit bundle size or use weighted bundling. With $N$ items in
  GF(2), need $D \gg N$ to avoid saturation.

### Pitfall 5: Misinterpreting Emergent STDP
- **Symptom**: Expecting biological fidelity from algebraic equivalence.
- **Fix**: The equivalence is at the **functional level** (same mathematical
  form), not the mechanistic level (different physical process). Use it
  for efficient computation, not neuroscience simulation.

---

## 11. Related Work and Further Reading

- **Kanerva (2009)**: Hyperdimensional Computing — foundational HDC paper
- **Plate (2003)**: Holographic Reduced Representation — binding theory
- **Gallant & Okaywe (2013)**: Representing object relations in HDC
- **Rachkovskij & Kussul (2001)**: HDC for analogical reasoning
- **Chuma, Otsuka, Sato (2026)**: VaCoAl paper — arXiv:2604.11665
- **Bi & Poo (1998)**: Original STDP discovery in biological synapses
- **Song, Abbott & Nelson (2000)**: STDP theory and modeling

---

## 12. When to Use This Skill

Use this skill when:
- Implementing **hyperdimensional computing** with path-dependent selection
- Designing **SRAM-CAM hardware** for neuromorphic inference
- Addressing **catastrophic forgetting** in continual learning systems
- Needing **deterministic reasoning** with interpretable confidence scores
- Exploring **emergent learning rules** from algebraic structures
- Building **edge AI** systems with ultra-low power requirements
- Researching **STDP equivalents** in non-biological systems
