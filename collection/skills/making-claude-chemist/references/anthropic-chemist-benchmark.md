# Anthropic: Making Claude a Chemist (2026-06-05)

Source: https://www.anthropic.com/research/making-claude-a-chemist

## Benchmark Results

### Hydrogen NMR (¹H)
| Model | Avg Error | Notes |
|-------|-----------|-------|
| Opus 4.7 | ±0.079 ppm | Highest share of peaks in tolerance |
| ChemDraw | ~0.16 ppm | ~2x wider error |
| MestReNova | ~0.09 ppm | Close second |

### Carbon NMR (¹³C)
- Opus 4.7 and MestReNova performed comparably

### Structure Elucidation (1D Inverse)
- 8 simple structures: 100% recovery (spectra + formula)
- 7 hard targets: 100% recovery (with starting-material hint)

### Methodology
- LLM queried 3 times per compound, averaged
- Deterministic tools run once each
- ppm tolerance windows for validation

## Bottlenecks
1. Representation translation (SMILES ↔ structures ↔ spectra)
2. Spectral analysis (NMR, IR, MS)
3. Retrosynthesis planning (still being scoped)
4. Instrument readout reconciliation
5. Database querying in correct notation
