---
name: vnvspec-requirements-vv-specification
description: "VNVSpec methodology for machine-readable verification and validation (V&V) specifications that bridge high-level systems-engineering requirements with low-level test results. Use when: (1) designing or auditing requirements-to-tests traceability for AI-enabled, cyber-physical, or safety-critical systems; (2) building executable V&V specs in CI; (3) mapping standards clauses (EU AI Act, ISO 21448, UL 4600) to automated evidence; (4) evaluating agent-generated code against decomposed requirements. Activation: V&V, requirements traceability, model-based systems engineering, MBSE, AI safety assurance, verification validation, executable specifications, cyber-physical systems, EU AI Act, ISO 21448."
metadata:
  arxiv_id: "2607.17686"
  published: "2026-07-20"
  authors: ["Mansur Arief", "Ali Akarma", "Nur Ahmad Khatim", "Ahmad Alfan Alfian Irfan"]
  categories: ["cs.SE", "cs.AI"]
  source: "arXiv - Integrating High-Level Requirements to Low-Level Tests with Machine-Readable V&V Specifications"
license: Complete terms in LICENSE.txt
---

# VNVSpec: Machine-Readable V&V Specifications

## What problem it solves

Software engineering has low-level testing (pytest, JUnit, Jest) and systems engineering has rigorous V&V doctrine (INCOSE, ISO/IEC/IEEE 29148, NASA), but the two are usually disconnected. The mapping from high-level requirements to low-level tests is maintained by hand, if at all. VNVSpec turns the V&V specification itself into a typed, machine-readable, executable artifact that lives in the repository and in CI, producing traceable evidence for regulators, auditors, and developers.

## Core contributions

1. **Typed specification language** for requirements, interface contracts, hazards, operational design domains (ODDs), and evidence records. Models are immutable, serializable, and can be validated, composed, diffed, and traced.
2. **Bridge to existing test tooling** via a pytest plugin, JUnit XML ingestion, evidence collectors for scripts/formal verification, and model adapters for PyTorch / HuggingFace models.
3. **Quality checker** at authoring time that flags vague, unverifiable, or poorly structured requirements using ISO/IEC/IEEE 29148 / INCOSE rules.
4. **Traceability graph** (DAG) linking high-level requirements → module-level requirements (with metrics and acceptance criteria) → test cases → evidence records → verdicts.
5. **Audit-ready outputs**: compliance matrices, CI reports, and Goal Structuring Notation (GSN) assurance cases.

## When to use this skill

- Designing requirements-to-tests traceability for AI-enabled, cyber-physical, autonomous, or safety-critical systems.
- Building executable V&V specs that run in CI alongside normal tests.
- Mapping regulatory / standards clauses (EU AI Act, ISO/PAS 8800, ISO 21448, UL 4600) to concrete test evidence.
- Evaluating output of AI coding agents against decomposed requirements and acceptance criteria.
- Auditing whether high-level requirements are actually covered by tests at any given commit.

## Methodology

### 1. Author or import requirements

- Write high-level requirements directly in the VNVSpec language (YAML/TOML/Python objects), or import from catalogs derived from published standards.
- Run the quality checker to enforce rules: active voice, one verifiable condition per requirement, avoid vague terms, explicit metrics, acceptance criteria.

### 2. Decompose into module-level requirements

- For each high-level requirement, produce module-level requirements with:
  - a defined metric,
  - an acceptance criterion,
  - a parent link to the high-level requirement.

### 3. Link to tests and evidence

- Annotate tests with requirement IDs, or use the VNVSpec scanner to derive links from requirement-ID references in the codebase.
- Evidence routes:
  - **pytest**: pytest plugin captures pass/fail results per requirement.
  - **JUnit XML**: ingest results from JavaScript, Java, C++ test runners.
  - **Analysis scripts**: collect evidence from numerical analysis or formal verification runs (e.g., CROWN certified output bounds).
  - **Model adapters**: evaluate PyTorch / HuggingFace models directly against ODD / hazard requirements.

### 4. Roll up evidence and produce verdicts

- Evidence records flow back into the traceability DAG.
- Framework conservatively rolls up evidence into verdicts at each level.
- Outputs: compliance matrices (auditors), CI reports (developers), GSN assurance cases (safety engineers).

## Architecture overview

```
High-level requirements  (user or standards catalog)
         |
         v
  Quality gate (QC rules)
         |
         v
Module-level requirements  (metrics + acceptance criteria)
         |
         +----> Test cases  ----> pytest / Jest / JUnit / CROWN / model adapters
         |                         |
         |                         v
         |                  Evidence records
         |                         |
         v                         v
      Traceability DAG  <---- Evidence ingestion
         |
         v
  Verdicts + reports + GSN export
```

## Key design principles

- **Traceability as by-product**: Links are typed objects created where the work happens, not reconstructed later.
- **Developer-native**: Plain Python objects, YAML/TOML in repo, CI integration.
- **Solver-grounded / tool-grounded evidence**: A numerical result is reported only when it originates from a trusted tool and passes explicit verification.
- **Conservative verdict roll-up**: missing evidence does not silently become a pass.
- **Scalable**: reported linear scaling up to 10,000 requirements.

## Evidence routes and when to use them

| Route | Use case | Tool |
|-------|----------|------|
| pytest | Python unit tests and property-based tests | VNVSpec pytest plugin |
| JUnit XML | JavaScript, Java, C++ test runners | XML ingestion |
| Analysis scripts | Numerical analysis, simulation, formal verification | Evidence collector (e.g., CROWN certified output bounds) |
| Model adapters | Black-box ML model assessment | PyTorch / HuggingFace adapters |

## Quality checker rules (selection)

- One requirement states one verifiable condition.
- Use active voice; subject and responsible party are explicit.
- Avoid vague terms (e.g., "user-friendly", "fast", "robust"); define metrics.
- Each requirement has an associated acceptance criterion.
- Requirements are atomic, unambiguous, and traceable to a parent need.

## Implementation guidance

1. Start from the VNVSpec GitHub repo: `https://github.com/ai-vnv/vnvspec`.
2. Define a small catalog of requirements for one module or one ODD.
3. Add requirement IDs as comments or markers in existing tests.
4. Run the scanner and the quality checker in CI.
5. Iterate on decomposition until every high-level requirement has at least one linked test and evidence record.

## Limitations and future directions

- Requires upfront investment to write / decompose requirements.
- Does not automatically generate requirements from natural-language documents (though agentic modules are envisioned).
- Standards catalogs must be maintained manually or curated from authoritative sources.

## Related work

- ISO/IEC/IEEE 29148 (requirements engineering)
- INCOSE Guide to Writing Requirements and INCOSE Handbook
- NASA Systems Engineering Handbook
- EU AI Act, ISO/PAS 8800, ISO 21448, UL 4600 (AI safety standards)
- Doorstop, Sphinx-needs, Eclipse Capra (requirements-as-code/traceability)
- Cucumber / Gherkin (BDD acceptance criteria)

## References

- Arief et al., arXiv:2607.17686, 2026. "Integrating High-Level Requirements to Low-Level Tests with Machine-Readable V&V Specifications."
- GitHub repository: https://github.com/ai-vnv/vnvspec

## Activation Keywords

V&V, verification, validation, requirements traceability, machine-readable specification, MBSE, model-based systems engineering, cyber-physical systems, AI safety assurance, EU AI Act, ISO 21448, UL 4600, executable requirements, test evidence, assurance case, GSN, ISO 29148, INCOSE.
