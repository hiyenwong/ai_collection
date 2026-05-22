---
name: quantum-crypto-exposure-measurement
description: "Formal framework for measuring quantum cryptographic exposure under HNDL (Harvest Now Decrypt Later) threats. Factorizes compromise probability into temporal hazard, cryptographic vulnerability, and operational exposure terms."
tags: ["quantum", "cryptography", "security", "statistics", "probability"]
---

# Quantum Cryptographic Exposure Measurement under HNDL Threat

## Description
A formal mathematical framework for quantifying an organization's exposure to "Harvest Now, Decrypt Later" (HNDL) attacks, where adversaries collect encrypted data today for future quantum decryption. The framework factorizes the HNDL compromise probability into a temporal hazard, a multiplicative cryptographic-vulnerability and operational-exposure term, and a saturation denominator governed by defense-attack intensity ratio.

## Activation Keywords
- quantum crypto exposure
- HNDL threat measurement
- harvest now decrypt later
- quantum cryptographic risk
- post-quantum exposure
- 量子密码暴露测量
- cryptographic vulnerability scoring
- quantum threat prioritization

## Tools Used
- **terminal**: Run exposure calculation scripts
- **python/numpy**: Statistical modeling, hazard rate computation

## Core Methodology

### HNDL Compromise Probability Model

The compromise probability factorizes as:

```
P_compromise = h(t) × V_crypto × E_operational / (1 + D/A)

Where:
  h(t)    = Temporal hazard function (value decay over time)
  V_crypto = Cryptographic vulnerability term
  E_operational = Operational exposure term
  D       = Defense intensity
  A       = Attack intensity
```

### Three Structural Assumptions

1. **Adversarial Production**: Adversaries invest resources proportional to expected value
2. **Value Decay**: Data value decays over time (temporal hazard)
3. **Defense-Attack Ratio**: Saturation governed by D/A intensity ratio

### Implementation Pattern

```python
import numpy as np

def hndl_exposure(
    time_since_harvest: float,
    crypto_vulnerability: float,  # 0-1, based on algorithm
    operational_exposure: float,   # 0-1, based on data sensitivity
    defense_intensity: float,      # Defense capability score
    attack_intensity: float,       # Adversary capability score
    value_decay_rate: float = 0.1  # Per-year decay
) -> float:
    """
    Calculate HNDL compromise probability.
    
    Returns:
        Probability of compromise (0-1)
    """
    # Temporal hazard: exponential decay of data value
    temporal_hazard = value_decay_rate * np.exp(-value_decay_rate * time_since_harvest)
    
    # Saturation denominator
    saturation = 1 + (defense_intensity / max(attack_intensity, 1e-10))
    
    # Compromise probability
    p_compromise = (temporal_hazard * crypto_vulnerability * 
                    operational_exposure) / saturation
    
    return min(p_compromise, 1.0)

def prioritize_migration(assets: list[dict]) -> list[dict]:
    """
    Rank assets by HNDL exposure for migration prioritization.
    
    Args:
        assets: List of asset dicts with crypto/algebra parameters
    
    Returns:
        Sorted list by exposure score descending
    """
    for asset in assets:
        asset['exposure'] = hndl_exposure(**asset)
    
    return sorted(assets, key=lambda x: x['exposure'], reverse=True)
```

### Cryptographic Vulnerability Assessment

```python
def crypto_vulnerability_score(algorithm: str, key_length: int) -> float:
    """
    Score cryptographic vulnerability to quantum attacks.
    
    Scale: 0 (quantum-safe) to 1 (highly vulnerable)
    """
    vulnerability_map = {
        'RSA': min(1.0, 2048 / max(key_length, 1)),
        'ECC': min(1.0, 256 / max(key_length, 1)),
        'AES-128': 0.5,  # Grover's algorithm: sqrt speedup
        'AES-256': 0.25,
        'Kyber': 0.05,   # Post-quantum
        'Dilithium': 0.05,
    }
    return vulnerability_map.get(algorithm, 0.5)
```

## Use Cases

1. **Post-quantum migration planning**: Prioritize which systems to migrate first
2. **Risk assessment**: Quantify HNDL exposure across an organization
3. **Security budgeting**: Allocate defense resources based on exposure scores
4. **Compliance reporting**: Demonstrate quantum readiness to auditors

## Why Additive Scoring Fails

Traditional additive frameworks (score = w₁v₁ + w₂v₂ + ...) cannot reproduce the HNDL model because the interaction between cryptographic vulnerability and operational exposure is multiplicative by construction. A system with low crypto vulnerability but high operational exposure has a fundamentally different risk profile than one where both are moderate — additive scoring obscures this distinction.

## Error Handling

### Missing Parameters
```
If operational exposure is unknown:
  1. Use default value based on asset classification
  2. Flag for manual review
  3. Apply conservative (higher) estimate
```

### Uncertain Attack Intensity
```
If adversary capability is unknown:
  1. Use upper bound estimate (state-level adversary)
  2. Perform sensitivity analysis
  3. Report range of possible exposure values
```

## Best Practices

1. **Regular reassessment**: Update exposure scores as quantum computing advances
2. **Conservative estimates**: When in doubt, overestimate attack intensity
3. **Partial observability**: Framework is designed to work with incomplete information
4. **Marginal sensitivity**: Each dimension's impact depends on current position in vulnerability-exposure plane

## Limitations

- Requires estimation of adversary capabilities (inherently uncertain)
- Value decay rate is organization-specific
- Does not model zero-day quantum algorithm breakthroughs
- Assumes rational adversary behavior

## Resources

- arXiv: 2605.22569 - "A Formal Basis for Quantum Cryptographic Exposure Measurement under HNDL Threat"
- NIST Post-Quantum Cryptography Standardization
- NSA Commercial National Security Algorithm Suite

## Related Skills
- `quantum-system-engineering`: Quantum systems design patterns
- `post-quantum-cryptographic-protocol-analysis`: PQC protocol analysis
- `cross-layer-crypto-analysis`: Cross-layer cryptographic security analysis
