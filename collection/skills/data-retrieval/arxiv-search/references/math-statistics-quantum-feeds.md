# Math/Statistics/Number Theory + Quantum RSS Feed Combinations

Verified feed URLs for discovering papers at the intersection of quantum mechanics and mathematics/statistics/number theory (confirmed 2026-05-29).

## Primary Math+Quantum Feeds

### Comprehensive Math+Stats+Quantum
```bash
# Math + Statistics + Quantum combined
curl -x http://127.0.0.1:7890 -s --max-time 30 "https://rss.arxiv.org/rss/quant-ph+stat.ME+stat.ML+math.NT+math.PR+math.ST" -o /tmp/arxiv_math_quantum.xml
# Yields: ~390 papers (verified 2026-05-29)
# Keyword filter yields: ~119 quantum+math/stats papers
```

### Narrower Subsets
```bash
# Pure quantum + number theory
curl -o /tmp/arxiv_qnt.xml "https://rss.arxiv.org/rss/quant-ph+math.NT"

# Quantum + statistics
curl -o /tmp/arxiv_qstat.xml "https://rss.arxiv.org/rss/quant-ph+stat.ME+stat.ML"

# Quantum + probability
curl -o /tmp/arxiv_qprob.xml "https://rss.arxiv.org/rss/quant-ph+math.PR"

# Quantum + statistics (standalone)
curl -o /tmp/arxiv_stat.xml "https://rss.arxiv.org/rss/stat.ML+stat.ME"
```

## Category Definitions

| Category | Description | Typical Content |
|----------|-------------|-----------------|
| `quant-ph` | Quantum Physics | Quantum computing, quantum information, quantum algorithms |
| `math.NT` | Number Theory | Prime numbers, modular forms, L-functions, Diophantine equations |
| `stat.ME` | Statistics (Methodology) | Statistical methods, inference, estimation theory |
| `stat.ML` | Machine Learning (Statistics) | Statistical learning theory, Bayesian methods |
| `math.PR` | Probability | Stochastic processes, probability theory, random matrices |
| `math.ST` | Statistics (Theory) | Theoretical statistics, asymptotics |
| `math.CO` | Combinatorics | Graph theory, combinatorial structures |

## High-Yield Keywords for Filtering

After downloading RSS feed, filter by keywords to identify most relevant:

```python
import re

QUANTUM_MATH_KEYWORDS = [
    'quantum', 'qubit', 'hamiltonian', 'entanglement',
    'number theory', 'prime', 'factorization', 'shor',
    'statistical', 'probability', 'distribution', 'stochastic',
    'random matrix', 'bayesian', 'gaussian', 'entropy',
    'linear algebra', 'hilbert space', 'eigenvalue', 'eigenvector',
    'topological', 'homology', 'algebraic topology',
    'tensor network', 'coding theory', 'information theory',
    'option pricing', 'derivative', 'finance', 'black-scholes',
    'reservoir computing', 'ground state', 'markovian',
    'persistent homology', 'betti number',
]

def is_quantum_math(title, abstract):
    text = (title + ' ' + abstract).lower()
    has_quantum = 'quantum' in text or 'qubit' in text or 'hamiltonian' in text
    has_math = any(kw in text for kw in QUANTUM_MATH_KEYWORDS if kw != 'quantum' and kw != 'qubit' and kw != 'hamiltonian')
    return has_quantum and has_math
```

## Two-Step Mandatory Pattern

Security guardrail blocks `curl | python3`. Always:

1. **Download**: `curl -o /tmp/arxiv_math_quantum.xml "https://rss.arxiv.org/rss/quant-ph+stat.ME+stat.ML+math.NT+math.PR+math.ST"`
2. **Parse**: `python3 parse_papers.py /tmp/arxiv_math_quantum.xml`

## Notable Discoveries (2026-05-29)

| arXiv ID | Title | Key Innovation |
|----------|-------|----------------|
| 2605.28986 | Comparing Classical Simulation and Sample-Based Learning of Quantum Systems | Empirical framework: simulability ≠ learnability for quantum systems |
| 2605.28964 | Prime Number Identification with Quantum Processors | First experimental prime detection via entanglement dynamics on IBM hardware |
| 2605.28931 | Learning quantum ground states in the space of measurement outcomes | SIC-POVM variational learning with autoregressive GRU, L=128 benchmark → skill: quantum-ml-ground-state-measurement |
| 2605.28927 | Quantum encodings preserving persistent homology | Topology-preserving quantum data encoding for TDA+QML → skill: quantum-persistent-homology-encoding |
| 2605.28859 | Analytic Properties of the Jost Functions via the Poincaré-Picard Theorem | ODE-theoretic analysis of Jost function analyticity for quantum scattering → skill: jost-function-analytic-ode |
| 2605.29508 | Quantum Markovian Dynamics from Double Covariance Stochastic Framework | Subquantum stochastic derivation of Lindblad dynamics |
| 2605.29071 | Hidden bottleneck in linear reservoir computing | Proves quantum linear reservoirs suffer same capacity limits as classical |
| 2605.28950 | Exponentially Fast Heat Equation for Option Pricing | Black-Scholes→quantum linear system mapping for derivative pricing |

## Best Practices

- **Download broad, filter narrow**: The combined feed yields 390 papers; Python keyword filtering reduces to ~119 relevant ones
- **Use proxy for curl**: `curl -x http://127.0.0.1:7890` is more reliable than direct access for RSS feeds
- **Cross-domain intersections are sparse**: Narrow combinations like `quant-ph+math.NT` alone may yield only 0-5 papers on a given day — always combine multiple categories
- **Math+Quantum papers appear in multiple categories**: Check all categories, not just the first one listed

## Related Reference Files

- [neuroscience-rss-feeds.md](neuroscience-rss-feeds.md) — Neuroscience-specific feeds
- [quantum-finance-feeds.md](quantum-finance-feeds.md) — Quantum + finance feeds
- [systems-engineering-quantum-feeds.md](systems-engineering-quantum-feeds.md) — Systems engineering feeds
