# Research Patterns Extracted - 2026-05-29

## Session Theme: Number Theory + Statistics + Mathematics (Friday) + Quantum Mechanics (Daily)

## Key Papers Analyzed

### 1. Non-Invertible Symmetry Enriched Topological Orders (arXiv: 2605.28794)
- **Domain**: Mathematical Physics, Category Theory, Quantum Computing
- **Core Insight**: Traditional SETOs with group symmetries can be generalized to fusion category symmetries
- **Implementation**: Two equivalent approaches - UFC full inclusions and anyon condensation
- **Mathematical Tools**: Fusion rules, F-symbols, R-symbols, Drinfeld centers, modular S-matrix
- **Created Skill**: `non-invertible-topological-order-analysis`

### 2. Quantum Statistical Estimation Theory
- **Domain**: Quantum Mechanics, Statistics, Metrology
- **Core Insight**: Quantum Fisher Information provides fundamental limits on parameter estimation
- **Key Results**: QFI for pure/mixed states, Cramér-Rao bounds, multi-parameter estimation trade-offs
- **Applications**: Quantum sensing, metrology, parameter estimation in quantum systems
- **Created Skill**: `quantum-statistical-estimation-framework`

### 3. Dynamic Entanglement Packet Scheduling (arXiv: 2605.28795)
- **Domain**: Quantum Networks, Computer Science
- **Core Insight**: TDMA-based entanglement packet architecture for scalable multi-user quantum networks
- **Related Existing Skill**: `quantum-network-control`

### 4. Device-Agnostic Microwave Noise Metrology (arXiv: 2605.28808)
- **Domain**: Quantum Engineering, Metrology
- **Core Insight**: Near-quantum-limited signal processing characterization for solid-state quantum technologies
- **Related Existing Skill**: `quantum-metrology-sensing-review`

## Extracted Skill Patterns

### Pattern 1: Topological Phase Classification
- **Trigger**: Analyzing topological phases with non-standard symmetries
- **Approach**: 
  1. Identify symmetry structure (group vs fusion category)
  2. Choose implementation method (UFC inclusion vs anyon condensation)
  3. Compute topological invariants (anyon spectrum, S-matrix, spins)
  4. Validate consistency (pentagon/hexagon equations)
- **Verification**: Check fusion rule associativity, F/R symbol consistency

### Pattern 2: Quantum Parameter Estimation
- **Trigger**: Estimating parameters of quantum states/processes
- **Approach**:
  1. Compute Quantum Fisher Information (QFI)
  2. Apply Quantum Cramér-Rao Bound
  3. For multi-parameter: check QFIM positive definiteness
  4. Consider Bayesian framework for small samples
- **Pitfalls**: Multi-parameter bounds may not be simultaneously achievable

## Knowledge Graph Operations

### Successful Patterns
- arXiv API via `urllib.request` with User-Agent header works reliably
- `kg_entities` schema: INTEGER PRIMARY KEY auto-increment (NOT TEXT)
- `kg_vectors.vector_data`: binary float32 BLOBs (256-dim most common)
- Hash-based embeddings work for keyword matching but NOT semantic similarity
- Connected components community detection more reliable than Louvain with hash vectors

### Pitfalls Encountered
1. **Vector format confusion**: Mixed binary BLOB and JSON-text formats in `kg_vectors`
2. **Pagerank column mismatch**: `pagerank` table may not have `id` column for joining
3. **Dimension inconsistency**: Vector dimensions vary (256, 1024, 1536, 2066) - never assume fixed size
4. **web_search failure**: Firecrawl backend completely down, use arXiv API directly

## ai_collection Sync Pattern

1. Copy skill directory to `ai_collection/collection/skills/{name}/`
2. Update INDEX.md with new entry format:
   ```
   ## YYYY-MM-DD - {Theme} (Cron Job)
   
   ### {Paper Title}
   - [[{skill-name}]] - Description (arXiv: {id})
     - Core要点 1
     - Core要点 2
     - **Activation**: keywords
   ```
3. Git add + commit + push
