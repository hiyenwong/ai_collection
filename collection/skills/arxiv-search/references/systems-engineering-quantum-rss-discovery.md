# Systems Engineering + Quantum RSS Discovery (2026-05-28)

## Verified Working Pattern

RSS feed download + Python file parse is the only reliably working method for arXiv discovery in cron jobs. API returns 429, browser times out.

```bash
# Step 1: Download
curl -s --max-time 30 "https://rss.arxiv.org/rss/quant-ph" -H "User-Agent: Mozilla/5.0" -o /tmp/arxiv_quantum.xml

# Step 2: Parse (Python on file, NOT pipe)
python3 /tmp/extract_papers.py
```

## Systems Engineering Keywords for Filtering

```python
keywords = ['control', 'system', 'engineering', 'optimization', 'reliability', 'robust', 'network', 'distributed']
```

## Feed Combinations

| Feed | Yield for Systems+Quantum | Notes |
|------|---------------------------|-------|
| `quant-ph` (standalone) | 5-8 relevant per 50 papers (70/140 with score>=2) | **Best yield** — keyword filter essential |
| `quant-ph+cs.LG` | ~1 relevant per 50 | ML-heavy, less systems |
| `quant-ph+cs.SE` | 0-1 per 50 | Very sparse |
| `cs.SE+cs.SY` (standalone) | 0 quantum papers (confirmed 2026-05-28) | **No quantum content** — cs.SE+cs.SY has zero quantum overlap on a typical day; narrow cross-domain intersections are sparse. Do NOT treat 0 RSS matches as a discovery failure — the intersection is simply sparse. |

## Keyword Scoring (Confirmed 2026-05-28)

```python
keywords = ['control', 'system', 'engineering', 'optimization', 'reliability', 'robust',
            'network', 'distributed', 'architecture', 'safety', 'feedback',
            'protocol', 'routing', 'compiler', 'scheduling', 'resource',
            'management', 'monitoring', 'fault', 'error']
# Score >= 2 captures most relevant papers; score >= 4 is high-signal

## Key Papers Found (2026-05-28)

- **2605.27425**: QKD network routing via Hamiltonian optimization + tensor networks (in KG)
- **2605.27670**: Quantum annealing for greenhouse control QUBO (benchmarking) (in KG)
- **2605.27410**: Zero-shot quantum neural architecture search (MZeQAS)
- **2605.27416**: Quantum federated learning security (CULT backdoor model)
- **2605.28162**: VarEFTQC - learning logical operations for arbitrary QEC codes
- **2605.27417**: QML for 6G edge network adaptive communication → skill: `quantum-6g-network-systems`
- **2605.28795**: Dynamic entanglement packet scheduling (IEEE QuNAP 2026) → skill: `quantum-networks-systems-engineering`
- **2605.28511**: Chirped-pulse engineering for robust cavity QED control → skill: `quantum-robust-control-engineering`
- **2605.28040**: Filter-assisted quantum subspace diagonalization via sparsity engineering
- **2605.27420**: Hybrid classical-quantum NNs for AlGaN/GaN MIS-HEMT device optimization

## Additional Papers Found in quant-ph RSS (score>=3, not above)

- **2605.28690**: Latent-conditioned parameterized quantum circuits as universal approximators
- **2605.27442**: Coherent catalyst for ergotropy stabilization in open quantum batteries
- **2605.27775**: Entanglement-enhanced probing of atomic parity violation
- **2603.17892**: Zeno/Anti-Zeno effects in dark-state dynamics under thermal dephasing
- **2605.00205**: Quantum in Biology, Quantum for Biology, Biology for Quantum (evidence mapping)
- **2506.15375**: Learning to maximize QNN expressivity via effective rank

## Git Push

`git push` succeeded on retry (commit fbd17fef). Network issues are transient, not permanent.
