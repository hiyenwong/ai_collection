# Systems Engineering + Quantum RSS Discovery (2026-06-04)

## Feed Configuration
- **Feed**: `https://rss.arxiv.org/rss/quant-ph+cs.SE+cs.SY+cs.DC+cs.CR`
- **Total entries**: 320
- **SE-related**: 294 (92%) | **Quantum-related**: 115 (36%) | **Intersection**: 106 (33%)

## Targeted Scoring Methodology

### Category Keywords
```python
target_keywords = {
    'quantum control': ['quantum control', 'quantum feedback', 'quantum optimal control'],
    'quantum error correction': ['quantum error correction', 'qec', 'quantum ldpc', 'syndrome', 'fault tolerant'],
    'quantum network': ['quantum network', 'quantum communication', 'entanglement distribution', 'quantum routing'],
    'quantum systems': ['quantum system', 'quantum architecture', 'distributed quantum'],
    'quantum reliability': ['quantum reliability', 'quantum fault', 'quantum verification'],
    'quantum scheduling': ['quantum scheduling', 'quantum resource', 'qubit routing', 'quantum compilation'],
    'quantum security': ['quantum security', 'quantum cryptography', 'qkd', 'quantum key'],
}
```

### Scoring Formula
- `score = matched_categories * 3 + se_indicators`
- SE indicators: distributed, control, network, scheduling, optimization, architecture, protocol, verification, reliability, fault-tolerant, multi-agent, consensus, resource

### Top Results (2026-06-04)
| Score | arXiv | Title | Categories |
|-------|-------|-------|------------|
| 9 | 2606.03611 | Q-FE: Quantum-Native 6G Far-Edge Architecture | quantum security |
| 7 | 2606.03293 | Deterministic generation of cat states (100+ photons) | quantum control |
| 7 | 2511.12482 | Autonomous QEC via deep reinforcement learning | QEC + systems |
| 6 | 2508.16784 | Amplitude Encoding for Quantum RNNs | quantum scheduling |

## New Skill Created
- **lie-algebra-quantum-control-interpolation** (arXiv: 2606.02014) - Lie group theory + neural networks for zero-optimization quantum control pulse generation

## Pitfall: INDEX.md Line Number Artifacts
When using `read_file` with offset/limit pagination on INDEX.md, the line number prefix (e.g., `1|1|`, `    11|`) gets embedded in the file content. When patching, these artifacts must be stripped:
```python
import re
cleaned = re.sub(r'\n\s+\d+\|', '\n', content)  # Remove "    11|" style artifacts
cleaned = re.sub(r'^\s+\d+\|', '', cleaned, flags=re.MULTILINE)  # Remove leading artifacts
```
Always verify INDEX.md is clean after patching. The `patch` tool's diff may introduce these artifacts when the old_string contains line-number-prefixed content.
