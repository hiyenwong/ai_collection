---
name: systems-engineering-threat-modeling
description: >
  Automated threat modeling and security verification for cyber-physical systems (CPS) and AI-enabled systems.
  Use when: (1) Designing security architecture for CPS/IoT systems, (2) Performing automated threat modeling
  from system architecture models (SysML, DFDs), (3) Analyzing attack chains in LLM-enabled robotic or
  autonomous systems, (4) Mapping vulnerabilities to security controls (NIST 800-53, MITRE ATT&CK),
  (5) Verifying system safety properties (HyperLTL, reachability), (6) Building security-in-the-loop
  design pipelines for distributed control systems.
  Trigger keywords: threat modeling, CPS security, SysML security, automated security, LLM robot security,
  DFD analysis, NIST controls, MITRE ATT&CK, HyperLTL verification, system security inference.
---

# Systems Engineering Threat Modeling

Automated threat modeling patterns for cyber-physical systems and AI-enabled architectures,
synthesized from recent research (arXiv 2026-04/05).

## Core Methodologies

### 1. SMSI Pipeline (System Model Security Inference)

Three-stage hybrid neuro-symbolic pipeline for automated threat modeling:

**Stage 1: Component-to-Vulnerability Mapping**
- Parse system architecture model (SysML blocks/components)
- Map each software/hardware component to known CVEs via NVD database
- Output: component → vulnerability mapping with severity scores

**Stage 2: Vulnerability-to-Attack-Technique Mapping**
- Link CVEs to MITRE ATT&CK techniques via three approaches:
  - Supervised classifier (fine-tuned domain-specific BERT)
  - Retrieval-based dense encoders
  - Zero-shot LLM approach (large open-weight models)
- Output: vulnerability → ATT&CK technique mapping

**Stage 3: Attack-Technique-to-Control Mapping**
- Map ATT&CK techniques to NIST 800-53 security controls
- Use dense embedding similarity for control recommendation
- Output: prioritized security control list

### 2. DFD-Based Cross-Boundary Threat Analysis

For LLM-enabled systems (robots, agents, edge-cloud architectures):

**Step 1: Model the Architecture as Hierarchical DFD**
- Identify all system components and data flows
- Mark trust boundaries between components
- Identify six key boundary-crossing interaction points

**Step 2: Apply STRIDE-per-Interaction**
- Analyze each boundary crossing for: Spoofing, Tampering, Repudiation,
  Information Disclosure, Denial of Service, Elevation of Privilege
- Cross-reference three threat taxonomies:
  - Conventional Cyber Threats (network, protocol-level)
  - Adversarial Threats (ML model attacks, adversarial examples)
  - Conversational Threats (prompt injection, jailbreak, instruction manipulation)

**Step 3: Trace Cross-Boundary Attack Chains**
- Map attack paths from external entry to physical actuation
- Identify architectural weaknesses:
  - Missing semantic validation between input and actuator
  - Unmediated cross-modal translation vulnerabilities
  - Provider-side tool use boundary crossings

### 3. Formal Verification with HyperCertificates

For discrete-time dynamical systems safety verification:

- Use HyperLTL to specify hyperproperties (privacy, opacity, robustness)
- Construct HyperCertificates: (lookahead function, barrier/ranking function pair)
- Automate via SOS optimization or SMT solvers
- Verify system traces satisfy multi-trace properties

## Implementation Pattern

```python
# Pseudo-pattern for SMSI-style automated threat modeling

def automated_threat_modeling(sysml_model):
    # Stage 1: Parse architecture → components
    components = parse_sysml(sysml_model)
    
    # Stage 2: Component → CVE mapping via NVD
    vulnerabilities = {}
    for comp in components:
        cves = query_nvd(comp.type, comp.version)
        vulnerabilities[comp.id] = cves
    
    # Stage 3: CVE → ATT&CK mapping (choose one)
    attack_techniques = map_cves_to_attack(
        vulnerabilities,
        method="dense_encoder"  # or "supervised_classifier" or "zero_shot_llm"
    )
    
    # Stage 4: ATT&CK → NIST controls
    controls = recommend_controls(attack_techniques)
    
    return {
        "vulnerabilities": vulnerabilities,
        "attack_techniques": attack_techniques,
        "recommended_controls": controls
    }
```

## Key Architectural Weaknesses to Check

1. **No Independent Semantic Validation**: Verify all user inputs pass through
   a semantic validation layer before reaching actuators
2. **Cross-Modal Translation Gaps**: Check vision→language→action pipelines
   for adversarial translation attacks
3. **Unmediated Tool Use**: Ensure LLM tool calls pass through authorization gates
4. **Trust Boundary Crossings**: All data crossing trust boundaries need
   STRIDE analysis

## References

- SMSI Paper: [arxiv.org/abs/2604.23905](https://arxiv.org/abs/2604.23905)
- LLM Robot Threat Modeling: [arxiv.org/abs/2604.27267](https://arxiv.org/abs/2604.27267)
- Full analysis: [references/detailed-analysis.md](references/detailed-analysis.md)
