# Systems Engineering + Quantum RSS Discovery Feeds

Updated 2026-06-05: Expanded to 7 feeds, 55 high-relevance papers.

## Verified Feeds

```python
feeds = [
    'https://rss.arxiv.org/rss/quant-ph+cs.SY+eess.SY+cs.SE+cs.DC',  # ★ HIGH-YIELD (243 items, 230 filtered)
    'https://rss.arxiv.org/rss/quant-ph+cs.SE',    # Quantum + Software Engineering
    'https://rss.arxiv.org/rss/quant-ph+cs.SY',    # Quantum + Systems & Control
    'https://rss.arxiv.org/rss/quant-ph+eess.SY',  # Quantum + Systems & Control (EE)
    'https://rss.arxiv.org/rss/eess.SY+cs.SY',     # Systems & Control standalone
]
```

## Keyword Filtering

After fetching, filter title+description for: `quantum`, `control`, `system`, `optimization`, `reliability`, `safety`, `robust`, `distributed`, `architecture`, `engineering`, `network`, `fault`, `tolerance`, `error correction`, `verification`, `compiler`, `routing`, `scheduling`, `resource allocation`, `feedback`.

**Dual-keyword scoring strategy** (2026-06-04 verified): Score = count(syseng_keywords) + 2 × count(quantum_keywords). Papers scoring ≥7 are high-relevance. This dual-weighting prioritizes papers that strongly match both domains.

## Papers Discovered (2026-06-04)

- **2606.03507**: Full Extractors for Logical Processing in Hypergraph Product Codes (QLDPC, PBC, fault tolerance)
- **2606.02697**: ML-based Quantum Error Mitigation for Variational Algorithms (Clifford training, NISQ)
- **2606.03147**: Quantum Optimization Algorithms for Strongly Correlated Many-Body Systems (VQE, QAOA review)
- **2606.03293**: Deterministic Generation of Cat States with 100+ Photons Under Dissipation (UQC theory)
- **2606.03891**: Efficient Quantum Error Mitigation for Unitary k-Designs
- **2606.02104**: Penalty-free Quantum Optimization for Lattice Protein Folding

Note: Cross-domain intersections like `quant-ph+cs.SY` are sparse on any given day — keyword filtering may yield 0 matches from a feed with 177 entries. This is expected, not a failure. Fall back to browser search UI if all feeds return 0 quantum-related papers.

## Papers Discovered (2026-05-29, Archive)

- **2605.27425**: Quantum-Inspired Hamiltonian Optimization for QKD Network Routing
- **2605.27427**: Quantum Reservoir Networks Based on Decoherence-Free Subspaces
- **2605.27410**: Zero-shot Quantum Neural Architecture Search (MZeQAS)
- **2605.27408**: Neural Quantum Spectral Operator Learning for PDEs (NVQLS)
