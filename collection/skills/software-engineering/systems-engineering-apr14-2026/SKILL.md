---
name: systems-engineering-apr14-2026
description: "Systems engineering research synthesis from April 14, 2026 arXiv papers. 8 papers covering: multikernel serverless OS, datacenter digital twins, proactive K8s autoscaling with DQN, CPS hardware testing, multi-robot rigidity control, Koopman irregular sampling, physics-informed SSM, and LLM-based formal verification."
category: systems-engineering
tags: ["systems-engineering", "distributed-systems", "control-theory", "digital-twin", "kubernetes", "multi-robot", "koopman", "physics-informed", "formal-methods"]
---

# Systems Engineering Research - April 14, 2026

Synthesis of latest arXiv papers (2604.xxxxx series) in distributed systems, control theory, and AI-assisted infrastructure.

## Quick Reference

| Paper | Category | Key Innovation | arXiv |
|-------|----------|----------------|-------|
| Nanvix | cs.DC | Multikernel OS for serverless density | 2604.11669 |
| OpenDT | cs.DC | Self-calibrating datacenter digital twin | 2604.11445 |
| NimbusGuard | cs.DC | DQN+LSTM+LLM proactive K8s autoscaling | 2604.11017 |
| ACT | cs.SE | Hardware-integrated CPS testing | 2604.11708 |
| Angle Rigidity | eess.SY | First bearing-angle equivalence proof | 2604.11754 |
| Koopman | eess.SY | Irregular sampling breaks aliasing | 2604.11715 |
| PISSM | eess.SY | Hard physics constraints via gating | 2604.11807 |
| FM-Agent | cs.SE | LLM Hoare reasoning for large systems | 2604.11556 |

## 1. Multikernel OS for Serverless

**Problem:** High deployment density vs isolation tradeoff  
**Solution:** Split-kernel: microkernel per invocation + macrokernel per tenant

**Metrics:**
- 20-100× fewer host servers
- Order-of-magnitude lower cold starts

**Pattern:** `ephemeral_state(VM_micro) ↔ persistent_state(VM_macro)`

## 2. Datacenter Digital Twin

**Cycle:** Physical ICT → Telemetry → Simulation → SLO Feedback → HITL → Adjustment

**Result:** MAPE 4.39% (vs 7.86% baseline)

## 3. Proactive Kubernetes Autoscaling

**Threefold Architecture:**
```
LSTM(forecast) → DQN(policy) → LLM(validation)
                        ↑
                   MCP Server
```

**Advantage:** Eliminates reactive lag, prevents under/over-provisioning

## 4. Automated CPS Testing

**Integration:** GitHub Actions → Self-hosted Runner → Physical Robot → Results

**Hardware:** Pololu 3pi+ 2040, sensors, actuators, displays

## 5. Multi-Robot Rigidity Control

**Theorem:** Infinitesimally bearing rigid ⟺ infinitesimally angle rigid  
(in SE(d), directed graphs, body-frame measurements)

**Control:** `u = u_mission + λ·∇(rigidity_eigenvalue)`

## 6. Koopman Irregular Sampling

**Finding:** Irregular sampling breaks aliasing through phase cancellation

**Loss:** `Σ ||φ(x_{t_{k+1}}) - K·φ(x_{t_k})·e^(λΔt_k)||²`

## 7. Physics-Informed SSM

**Architecture:**
1. Hankel embedding (noise filtering)
2. Linear SSM (continuous dynamics)
3. Physics gating (SZA × KT hard constraints)

**Result:** <40k parameters, edge deployable

## 8. LLM Formal Verification

**Approach:** Top-down spec generation from caller intent

**Results:**
- 143k LoC systems verified
- 522 new bugs found
- 2 days per system

## Cross-Patterns

| Pattern | Source | Core Idea |
|---------|--------|-----------|
| State Disaggregation | Nanvix | Separate ephemeral/persistent |
| Prediction-Action | NimbusGuard | Proactive > Reactive |
| Hard Constraints | PISSM | Structural > Loss-based |
| Rigidity Maintenance | Multi-Robot | Geometric stability |
| Irregular Sampling | Koopman | Break aliasing |
| NL-to-Formal | FM-Agent | LLM bridges intent/verification |

## Activation Keywords

multikernel, serverless density, digital twin, proactive autoscaling, DQN, CPS testing, angle rigidity, bearing rigidity, Koopman irregular sampling, physics-informed SSM, Hoare verification, LLM formal methods

## References

1. Segarra et al. Nanvix. arXiv:2604.11669
2. Nicolae et al. OpenDT. arXiv:2604.11445  
3. Wanigasooriya & Ekanayake. NimbusGuard. arXiv:2604.11017
4. Krishnan et al. ACT. arXiv:2604.11708
5. Presenza et al. Angle Rigidity. arXiv:2604.11754
6. Cho & Sowers. Koopman. arXiv:2604.11715
7. Abdullah. PISSM. arXiv:2604.11807
8. Ding et al. FM-Agent. arXiv:2604.11556

---
Created: April 14, 2026 | Papers: 8 | Categories: cs.DC, cs.SE, eess.SY