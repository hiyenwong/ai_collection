---
name: full-extractors-hgp-qldpc
description: "Full extractor construction for logical processing in Hypergraph Product (HGP) QLDPC codes. Enables Pauli-based computation without compilation overhead. Extractors 50-80% of base code size, max qubit degree 10, fault-tolerant. arXiv:2606.03507."
metadata:
  arxiv_id: "2606.03507"
  category: "quant-ph"
  authors: ["John Blue", "Zhiyang He", "Hengyun Zhou", "Isaac L. Chuang"]
  published: "2026-06-02"
---

## Full Extractors for Logical Processing in Hypergraph Product Codes

**arXiv: 2606.03507** (June 2026)

### Problem

QLDPC codes are promising for low-overhead quantum memories, but large-scale fault-tolerant quantum computation requires logical processing methods. Prior work on QLDPC logical processing introduces compilation overhead compared to surface code Pauli-based computation (PBC) architectures.

### Solution

**Full Extractor Construction**:
- Surgery systems capable of measuring arbitrary logical Pauli operators on a code block
- Enables logical processing via PBC **without** compilation overhead
- Assembles many partial extractors with verifiable fault-tolerance into single full extractor

### Key Results

| Metric | Value |
|--------|-------|
| Extractor size | 50%-80% of base HGP code |
| Max qubit degree | 10 (fixed connectivity hardware compatible) |
| Distance-10 logical error rate | ~10^-6 at 0.1% physical error rate |
| Fault-tolerance | Verifiable via circuit-level noise simulation |

### Reusable Patterns

#### Pattern 1: Partial-to-Full Extractor Assembly
Build large-scale fault-tolerant logical processing by composing verified partial extractors:
1. Design partial extractors for subsets of logical operators
2. Verify each partial extractor's fault-tolerance independently
3. Assemble into full extractor with guaranteed combined fault-tolerance
4. Enables modular, composable QEC logical processing

#### Pattern 2: Fixed-Connectivity QLDPC Design
Design QLDPC codes for fixed-connectivity hardware constraints:
- Maximum qubit degree constraint (e.g., degree ≤ 10)
- Extractor-augmented codes maintain hardware compatibility
- Eliminates need for SWAP networks or dynamic routing
- Space efficiency of QLDPC + surface-code-PBC convenience

#### Pattern 3: QLDPC Pauli-Based Computation
Replace surface code PBC architectures with QLDPC extractors:
- Same PBC computational model (logical Pauli measurements)
- QLDPC space efficiency advantage preserved
- No compilation overhead vs surface code approach
- Circuit-level noise validated at practical error rates

### Implementation Considerations

- **Hardware mapping**: Extractor codes must respect physical connectivity constraints
- **Error rate threshold**: ~0.1% physical error rate needed for 10^-6 logical rates
- **Code distance scaling**: Extractor size scales sub-linearly with base code size
- **Partial extractor verification**: Each component must be independently verified

### Activation
quantum error correction, QLDPC, hypergraph product codes, full extractors, logical processing, Pauli-based computation, fault tolerance, fixed connectivity, surgery systems, code compilation

### Related Skills
- `distributed-quantum-error-correction` - Distributed QEC architecture patterns
- `quantum-fault-tolerance-verification` - QEC verification methodology
- `css-syndrome-decoding` - CSS QEC syndrome decoding
- `quantum-systems-engineering` - Quantum systems engineering patterns
