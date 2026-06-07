# Friday Math+Statistics+Quantum Cron — 2026-06-05

## Papers Discovered

| arXiv | Title | Category | Score | Notes |
|-------|-------|----------|-------|-------|
| 2606.06456 | Quantum element-wise transforms | quant-ph | 9 | QSVT/LCU improvement, exponential space reduction for element-wise polynomial functions |
| 2606.06392 | Robustness of Entanglement Manipulation for almost i.i.d. sources | quant-ph | 8 | MSR almost i.i.d. sources, Schur-Weyl universal protocol, entanglement concentration/dilution |
| 2606.06482 | Two-Sample Hypothesis Testing for Subspace Equality in Network Data | stat.ME; math.ST | 4 | Frobenius norm test statistic, Gaussian convergence, stochastic blockmodels |

## Skills Created

1. **quantum-element-wise-transforms** — QSVT/LCU improvement, exponential space reduction
2. **entanglement-manipulation-robustness** — MSR almost i.i.d. entanglement robustness, Schur-Weyl protocol
3. **subspace-equality-hypothesis-testing** — Network subspace equality testing, Frobenius norm statistic

## Discovery Sources

- `browser_navigate` to `https://arxiv.org/list/quant-ph/recent` → 65 entries (Fri Jun 5)
- Browser console JS extraction: `document.querySelectorAll('dt')` + `document.querySelectorAll('dd')` pattern for paper ID/title extraction
- Individual paper abstracts via `browser_navigate` to `https://arxiv.org/abs/{id}`

## Hash-Based Vector Embedding Fallback

When `kg_tool embed` is unavailable, use this deterministic hash-based embedding:

```python
import json, sqlite3, hashlib

def hash_embedding(text, dim=384):
    """Deterministic hash-based embedding for kg_vectors fallback (cross-session consistent)."""
    words = text.lower().split()
    embedding = [0.0] * dim
    for w in words:
        h = int(hashlib.sha256(w.encode()).hexdigest(), 16) % dim
        embedding[h] += 1.0
    norm = sum(x*x for x in embedding) ** 0.5
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding

# Usage:
vec = json.dumps(hash_embedding(title + " " + abstract)).encode()
conn = sqlite3.connect('kg.db')
cur = conn.cursor()
cur.execute("INSERT INTO kg_vectors (entity_id, vector_data) VALUES (?, ?)", (entity_id, vec))
conn.commit()
```

**Note**: Python's `hash()` is session-deterministic but varies across Python invocations due to `PYTHONHASHSEED`. Use `hashlib.sha256` for cross-session consistency.

## KG Import Details

- 3 papers imported to kg.db entities 2265-2267
- 3 vector embeddings generated (kg_vectors table, `vector_data` BLOB column, 384-dim)
- kg_entities schema verified: id is INTEGER PRIMARY KEY (auto-increment)

## Sync

- Branch: `math-cron-2026-06-05`
- Commit: `43110ac5` — feat: add 3 math+quantum skills
- 4 files: 3 SKILL.md + INDEX.md
- Skills synced to both `~/.hermes/skills/` and `~/ai_github/ai_collection/collection/skills/`

## Keyword Scoring (Verified)

- **Math keywords** (43 terms): number theory, statistics, probability, matrix, lattice, optimization, estimation, distribution, algorithm, theorem, conjecture, bound, random matrix, bayesian, gaussian, entropy, linear algebra, eigenvalue, eigenvector, topological, homology, tensor, coding theory, information theory, persistent homology, betti number, stochastic, markovian, calculus, algebra, geometry, analysis, convergence, polynomial, spectral, approximation, kernel, inference, variance, covariance, regression, classification, prime, factorization, shor, modular form, diophantine
- **Quantum keywords** (28 terms): quantum, qubit, entanglement, superposition, hamiltonian, gate, fidelity, decoherence, phonon, fermionic, boson, bosonic, fermion, spin, operator, eigenstate, wavefunction, density matrix, trace, measurement
- **Top scores today**: 2606.06456 (9), 2606.06392 (8), 2606.06482 (4)
