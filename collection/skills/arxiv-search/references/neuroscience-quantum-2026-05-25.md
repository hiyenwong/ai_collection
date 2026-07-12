# Neuroscience + Quantum Research Notes (2026-05-25)

## Search Strategy

Combined query: `all:neuroscience AND all:quantum` returned 80 total results from arXiv API.

```bash
curl -s --max-time 30 -x http://127.0.0.1:7890 \
  "https://export.arxiv.org/api/query?search_query=all:neuroscience+AND+all:quantum&sortBy=submittedDate&max_results=10" \
  -H "User-Agent: Mozilla/5.0" -o /tmp/arxiv.xml
```

RSS alternative: `https://rss.arxiv.org/rss/quant-ph+q-bio.NC` or `https://rss.arxiv.org/rss/quant-ph+cs.NE`

## Key Papers Discovered

### 2511.06401 — Metabolic quantum limit to MEG information capacity
- **Core insight**: Combines energy resolution limit of magnetic sensing with brain's metabolic power to derive technology-independent bound
- **Key number**: 2.2 Mbit/s max information rate for human brain
- **Parameters**: Geometry + neural metabolism + Planck's constant only
- **Categories**: physics.bio-ph, physics.comp-ph, quant-ph

### 2511.11609 — Stochastic Quantum Neural Network Model for AI
- **Core insight**: Qubits evolve via stochastic differential equations inspired by biological neurons
- **Challenge addressed**: Von Neumann bottleneck in traditional ANNs
- **Categories**: q-bio.NC, math.QA, quant-ph

### 2509.16253 — Quantum-like representation: mental entanglement
- **Core insight**: QLM for entanglement generation by classical networks using operator algebras
- **Framework**: Prequantum classical statistical field theory (PCSFT)
- **Categories**: q-bio.NC, quant-ph

### 2511.07313 — fMRI De-Individualization via Bures Geometry
- **Core insight**: Mahalanobis whitening interpreted through Bures distance (connected to quantum mechanics)
- **Application**: Improves Alzheimer's diagnosis accuracy in preclinical stage
- **Categories**: q-bio.NC, cs.LG, q-bio.QM

### 2510.06361 — Diffusion-Guided Renormalization of Neural Systems
- **Core insight**: Quantum statistical mechanics-inspired coarse-graining for neural systems
- **Method**: Tensor networks + diffusion-based renormalization at entropy transitions
- **Categories**: q-bio.NC, cond-mat.stat-mech, cs.LG

### 2508.16895 — Quantum State Fidelity for Functional Neural Network Construction
- **Core insight**: Maps neural activity patterns to density matrices and uses quantum state fidelity F(ρ₁, ρ₂) as functional connectivity metric
- **Key finding**: Reveals distinct functional network structures not captured by classical correlation/MI
- **Workflow**: Encode → Fidelity computation → Network construction → Classical baseline comparison
- **Categories**: quant-ph, cs.ET, cs.NE, math.MG, q-bio.NC
- **Skill**: `quantum-state-fidelity-neural-networks`

## Duplicate Skills Found

- `stochastic-quantum-neural-networks` — malformed SKILL.md frontmatter (`name: skill.md---stochastic-quantum-neural-networks`)
- `stochastic-quantum-neural-network-ai` — valid, covers same paper (arXiv:2511.11609)
- **Resolution**: Keep `stochastic-quantum-neural-network-ai`, delete malformed one
