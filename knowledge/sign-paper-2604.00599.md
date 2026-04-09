# SIGN: Sparse Identification Graph Neural Network

## Paper Metadata

- **Title**: Predicting Dynamics of Ultra-Large Complex Systems by Inferring Governing Equations
- **arXiv ID**: 2604.00599
- **Authors**: Qi Shao, Duxin Chen, Jiawen Chen, Yujie Zeng, Athena Ma, Wenwu Yu, V. Latora, Wei Lin
- **Year**: 2026
- **Citations**: 0 (new)

---

## Core Contribution

**Sparse Identification Graph Neural Network (SIGN)** - A framework that combines:
1. **Graph Neural Networks** for network encoding
2. **Sparse Regression** for equation discovery
3. **Edge-level symbolic discovery** for scalability

### Key Innovation

Decouples sparse identification from network size by defining symbolic discovery at edge level.

---

## Results

| Metric | Performance |
|--------|-------------|
| Max network size | 100,000+ nodes |
| Equation recovery | 95-99% |
| Long-term prediction | 500+ steps |
| Noise tolerance (SNR=10) | 92% accuracy |

---

## Applications

1. **Climate**: Sea surface temperature (71,987 positions, 2-year prediction)
2. **Neural dynamics**: Wilson-Cowan model (50,000 neurons)
3. **Epidemic**: SIR spreading (100,000 nodes)

---

## Skill Created

- **Name**: `sign-complex-systems`
- **Path**: `~/.openclaw/skills/sign-complex-systems/`
- **Package**: `sign-complex-systems.skill`

---

## Related Topics

- Complex systems dynamics
- Equation discovery
- Graph neural networks
- Interpretable AI
- Symbolic regression

---

*Added: 2026-04-09*