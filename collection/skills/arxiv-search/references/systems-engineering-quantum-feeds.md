# Systems Engineering + Quantum RSS Discovery Feeds

Confirmed 2026-05-29 via cron job. These feeds discover papers at the intersection of quantum computing and systems engineering.

## Verified Feeds

```python
feeds = [
    'https://rss.arxiv.org/rss/quant-ph+cs.SE',    # Quantum + Software Engineering
    'https://rss.arxiv.org/rss/quant-ph+cs.SY',    # Quantum + Systems & Control
    'https://rss.arxiv.org/rss/quant-ph+eess.SY',  # Quantum + Systems & Control (EE)
    'https://rss.arxiv.org/rss/eess.SY+cs.SY',     # Systems & Control standalone
]
```

## Keyword Filtering

After fetching, filter title+description for: `quantum`, `control`, `system`, `optimization`, `reliability`.

Note: Cross-domain intersections like `quant-ph+cs.SY` are sparse on any given day — keyword filtering may yield 0 matches from a feed with 177 entries. This is expected, not a failure. Fall back to browser search UI if all feeds return 0 quantum-related papers.

## Papers Discovered (2026-05-29)

- **2605.27425**: Quantum-Inspired Hamiltonian Optimization for QKD Network Routing
- **2605.27427**: Quantum Reservoir Networks Based on Decoherence-Free Subspaces
- **2605.27410**: Zero-shot Quantum Neural Architecture Search (MZeQAS)
- **2605.27408**: Neural Quantum Spectral Operator Learning for PDEs (NVQLS)
