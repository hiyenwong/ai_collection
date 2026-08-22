# Original IDyOM Model Reference

## Information Dynamics of Music (IDyOM)

The original IDyOM model was developed by Marcus Pearce and provides event-by-event estimates of uncertainty and surprise from symbolic musical sequences. Key characteristics:

### Architecture
- **Variable-order Markov models**: Learns patterns of varying lengths from musical sequences
- **Multiple viewpoints**: Handles different musical feature dimensions simultaneously (pitch, duration, onset, etc.)
- **Bayesian framework**: Combines multiple models using Bayesian model averaging
- **Lisp implementation**: Original implementation was in Lisp, making integration with modern Python workflows difficult

### Core Concepts
- **Information content**: Measures surprise of each musical event based on learned statistical regularities
- **Entropy**: Quantifies uncertainty in predictions
- **Statistical learning**: Learns from exposure to musical corpora without explicit supervision

### Limitations Addressed by GraphIDyOM
1. **Integration difficulty**: Original Lisp implementation hard to integrate with Python data science workflows
2. **Inaccessible memory**: Internal memory structures not easily accessible for inspection or modification  
3. **Limited extensibility**: Difficult to extend or modify the original implementation
4. **No network analysis**: Memory representations not suitable for graph-based analysis techniques

### Validation Benchmark
GraphIDyOM was validated against the original Lisp IDyOM across:
- Single viewpoint configurations
- Projected viewpoint configurations  
- Multiple viewpoint configurations

Performance metrics included coverage and computational performance compared to both original IDyOM and recent reimplementations.

## Key References

- Pearce, M. T. (2005). The construction and evaluation of statistical models of melodic structure in music perception and composition. PhD thesis, City University London.
- Conklin, D., & Witten, I. H. (1995). Multiple viewpoint systems for music prediction. Journal of New Music Research, 24(1), 51-73.
- Bono Rosselló, L. (2026). GraphIDyOM: A graph-native Python reimplementation of IDyOM for musical expectation modelling. arXiv:2607.25787 [cs.SD, q-bio.NC]

## Comparison Summary

| Feature | Original IDyOM | GraphIDyOM |
|---------|----------------|------------|
| Language | Lisp | Python |
| Memory Representation | Internal opaque structures | Explicit graph objects |
| Integration | Difficult with modern workflows | Seamless Python integration |
| Memory Access | Not accessible | Exportable and analyzable |
| Network Analysis | Not possible | Full NetworkX compatibility |
| Server Support | None | Local HTTP server API |
| Extensibility | Limited | Highly extensible |
| Reproducibility | Proprietary | Open-source |

This reference provides context for understanding what GraphIDyOM improves upon and why the graph-native approach is valuable for computational neuroscience research.