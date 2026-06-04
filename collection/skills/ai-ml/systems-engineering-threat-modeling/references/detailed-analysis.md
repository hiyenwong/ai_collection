# Detailed Analysis: Systems Engineering Threat Modeling Papers

## Paper 1: SMSI - System Model Security Inference
**arXiv: 2604.23905** | Published: 2026-04-26 | Authors: Ro''ah Radaideh, Ali Khreis

### Core Contribution
First automated pipeline that starts from SysML architecture models and produces
prioritized NIST 800-53 security controls for cyber-physical systems.

### Technical Method
1. **Deterministic Parser**: Maps SysML system components to NVD vulnerabilities
2. **CVE→ATT&CK Mapping**: Three approaches compared:
   - Fine-tuned SecureBERT+ (supervised): best precision for known patterns
   - Dense retrieval encoders: best generalization to novel vulnerabilities
   - Zero-shot LLM (Gemma-4 26B): flexible but less consistent
3. **ATT&CK→NIST Control Recommender**: Dense embedding similarity matching

### Validation
- Healthcare IoT gateway with 9 software components
- Dense embeddings achieved highest control retrieval scores
- End-to-end pipeline reduces manual threat modeling from weeks to hours

### Implementation Pattern
- Input: SysML model → Parse blocks → Query NVD → Map to ATT&CK → Recommend NIST controls
- Key insight: Dense embeddings > supervised classification for generalization

---

## Paper 2: From Prompt to Physical Actuation
**arXiv: 2604.27267** | Published: 2026-04-29 | Authors: Neha Nagaraja, Hayretdin Bahsi, Carlo R. da Cunha

### Core Contribution
First DFD-based threat analysis integrating conventional cyber threats, adversarial
ML threats, and conversational threats across the full perception-planning-actuation
pipeline of LLM-enabled robotic systems.

### Technical Method
1. **Hierarchical DFD Modeling**: Edge-cloud robot architecture with 6 trust boundaries
2. **STRIDE-per-Interaction**: Applied at each boundary crossing
3. **Three-Category Taxonomy**:
   - Conventional: network attacks, protocol exploitation
   - Adversarial: visual adversarial examples, model poisoning
   - Conversational: prompt injection, jailbreak, instruction manipulation

### Key Findings
Three cross-boundary attack chains identified:
1. **Semantic Validation Gap**: No independent validation between user input and actuator dispatch
2. **Cross-Modal Translation**: Vision perception → LLM instruction can be adversarially manipulated
3. **Unmediated Tool Use**: Provider-side tool calls bypass internal security boundaries

### Significance
- Unifies previously separate threat research areas
- Provides actionable architectural hardening guidelines
- Demonstrates physical-world consequences of LLM vulnerabilities

---

## Paper 3 (Supplementary): HyperCertificates
**arXiv: 2605.00752** | Published: 2026-05-01 | Authors: Vishnu Murali, Amin Falah, Ashutosh Trivedi, Majid Zamani

### Core Contribution
Functional inductive framework for verifying discrete-time dynamical systems against
HyperLTL specifications (hyperproperties relating multiple system traces).

### Technical Method
- HyperCertificates: (lookahead function modeled by closure certificates, barrier/ranking functions)
- Automation via SOS optimization and SMT solvers
- Applicable to: opacity, privacy, robustness verification
