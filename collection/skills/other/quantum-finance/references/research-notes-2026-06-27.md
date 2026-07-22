# 2026-06-27 Quantum Finance Research Notes

## FPQC-SAC: Parameterized Quantum Circuit + SAC for Financial RL (arXiv: 2606.10448)

### Architecture
```
Market State → Feature Engineering → PQC Layer → Entangled Features
    → Actor Network (SAC) → Action (Buy/Hold/Sell)
    → Critic Network (SAC) → Q-Value
    → Entropy Bonus → Policy Update
```

### Key Innovation
PQC layer is placed BEFORE actor/critic networks:
- Acts as a feature filter/constraint
- Uses quantum entanglement to capture cross-asset interactions
- Angle encoding maps normalized features to qubit rotation angles
- 2-4 hardware-efficient layers with entangling gates (CNOT/CZ chains)
- Measurement expectations become input to classical actor/critic

### Results
- 66.89% return gain over classical SAC
- Low-SNR financial environments benefit most
- Quantum entanglement captures non-linear correlations between assets

### Hyperparameters
- Learning Rate: 3e-4 (Adam)
- Batch Size: 256
- Gamma: 0.99
- PQC Layers: 2-4
- Replay Buffer: 1e6

## Entangled Neural Traders Market Stabilization (arXiv: 2602.06367)

### Core Concept
- Prototype quantum stock market where entanglement between traders' valuations mitigates speculative busts
- RL agents with quantum-correlated qubit valuations
- Entanglement serves as endogenous market stabilization mechanism

### Mathematical Framework
```
Trader i valuation: |ψᵢ⟩ = α|buy⟩ + β|sell⟩ + γ|hold⟩
Entanglement: |Ψ⟩ = Σ cᵢⱼ |ψᵢ⟩ ⊗ |ψⱼ⟩
Market price: P = f(Σ action_i)
```

## CVaR Portfolio Quantum Benchmarking (arXiv: 2606.07727)

### Key Finding
HE-VQNN vs WS-QAOA hardware benchmarking reveals expressibility-coherence trade-off on NISQ devices.
- WS-QAOA: exact mapping but catastrophic decoherence from SWAP gate overhead
- HE-VQNN: preserves hardware coherence but lacks expressibility for dense tail-risk correlations
- Maps up to 16 assets on IBM heavy-hex

## Quantum RL Trading Agent for Sector Rotation (arXiv: 2506.20930)

### Architecture
- PPO backbone algorithm
- Quantum-enhanced models: QNN, QRWKV, QASA
- Automated feature engineering from capital share data

## Related Skills Created
- `fpqc-sac-quantum-financial-rl` - Full FPQC-SAC methodology
- `entangled-neural-trader-market-stabilization` - Entangled trader stabilization