---
name: requirement-bound-verified-commissioning
description: Use when integrating LLMs into safety-critical commissioning or requirement acceptance. Separates candidate generation from release authority via deterministic entailment gates.
category: ai_collection
---

# Requirement-Bound Verified Commissioning (RBC)

## Paper Source
- **arXiv**: 2609.30219 (2026-09-24)
- **Title**: Requirement-Bound Verified Commissioning: A Frozen Four-Billion-Parameter Local Model as a Candidate Generator under an External Acceptance Layer with Verification and Release Authority
- **Author**: Mehmet İşcan (PythaLab, Yıldız Technical University)
- **Domain**: Mechatronic commissioning / cs.SE + eess.SY

## Core Thesis
Never let an LLM hold release authority in safety-critical acceptance decisions. Assign the LLM only a **candidate-generation** role; a **deterministic external entailment gate** (not the model, not a second model) holds release authority, deciding based on **derivability from requirement text under a sealed grammar** — never on model confidence.

## Architecture (Three-Layer Trust Split)

```
Requirement text
   │
   ▼
[1] Deterministic parser ──(unsupported)──► [2] Frozen 4B local LLM (candidate generator only)
   │                                            │ proposes candidate plan
   ▼                                            ▼
[3] External entailment gate ◄──────────── candidate plan
    (release authority, sealed grammar V1)
    │
    ├─ both facts derivable from text ──► RELEASE plan
    ├─ fact missing ──► single-question protocol: ask gold user ONCE,
    │                    append answer as canonical sentence T1, re-run gate
    └─ not derivable ──► ABSTAIN (legitimate outcome)
```

**Key rules**:
1. No confidence score derived from model output ever enters the release decision
2. Release evidence = requirement clauses (traceable), not model self-assessment
3. Abstention + question-asking is a first-class legitimate outcome
4. Generator can be swapped without changing the decision rule

## Why Self-Verification Fails (Evidence from Paper)
- Self-verification (model checks its own output) reduces performance on most GPT-4 reasoning/planning tasks (Stechly et al. 2025)
- The frozen 4B model **fabricated ready plans on 21 of 22 unanswerable tasks** (95.5% fabrication rate) — the model CANNOT abstain
- ALL 21 fabrications were rejected by the external gate (0/83 false releases in the sealed run)
- Ungated comparator (no acceptance layer): 9 of 18 delivered plans were FALSE (50%)
- Verifier cascades (second model checking first model) fail from correlated verification errors (Han 2026) — independence requires determinism, not just a second model

## Sealed Statistical Protocol (Preregistration Pattern)
The false-release endpoint was evaluated ONCE under a criterion fixed **before** benchmark construction:
- One-sided 95% Clopper–Pearson upper bound: U(0, 83) = 0.0354 (below sealed 5% threshold)
- Tasks written by **isolated agent contexts** without access to gate, grammar, or experimental plan (benchmark blinding)
- Zero count ≠ zero rate: always report the upper bound (Hanley & Lippman-Hand)
- **Post-seal honesty**: 1 false release in 146 plans observed OUTSIDE the benchmark (grammar V1 failed on anaphor "that same head" — polarity cue not extracted). The paper reports this kill-rule trigger transparently instead of hiding it.

## Textual Trust Boundary (Critical Finding)
When a fact is NOT independently constrained by requirement text, the gate can only trust the user answer:
- **Text-bound stratum** (13/96 tasks, both facts bound from text): 0 of 65 wrong-answer pairings released — gate rejects incorrect answers
- **Text-open stratum** (83/96 tasks): user answer is SOLE fact source — 169 of 431 wrong-answer pairings RELEASED (39.2%) — incorrect answers pass through
- Grammar V1 exclusion failures: "not/no/without" lexicon missed "outside the family" exclusions; appended answer clauses could override explicit coordinate exclusions

**Design rule**: rejection of wrong facts is only as strong as the independent textual constraints on them. Responsibility transfers to requirement wording + fact-source reliability.

## Reusable Implementation Patterns

### Pattern 1: Generator/Gate Separation (LLM acceptance layer)
```python
# Candidate generation: LLM proposes ONLY
candidate = frozen_llm.propose(requirement_text)  # plan: (coordinate, polarity, status)
# Release decision: deterministic gate, sealed grammar
facts_derivable = entailment_gate.check(requirement_text, candidate, grammar=V1)
if facts_derivable:
    release(candidate, evidence=gate.matched_clauses)  # traceable evidence
elif missing_fact(candidate):
    answer = ask_user_once(canonical_question)
    augmented = requirement_text + template_T1(answer)
    recheck = entailment_gate.check(augmented, candidate, grammar=V1)
    if recheck: release(...)
    else: abstain()
else:
    abstain()  # legitimate outcome, never fabricate
```

### Pattern 2: Preregistered Acceptance Criterion
```python
# Fix criterion BEFORE benchmark construction; apply once
SEALED_THRESHOLD = 0.05  # false-release upper bound tier
criterion = ClopperPearsonUpperBound(confidence=0.95, side="upper")
# Never sweep thresholds post-hoc; report both raw and guarded verdicts
verdict_raw = criterion(n_false_releases=0, n_releases=83)  # 0.0354 < 0.05 → supported
```

### Pattern 3: Benchmark Blinding
- Benchmark tasks + answer key written by isolated agent contexts without access to gate/grammar/plan
- Prevents task leakage into method design
- Distinguish: derivability (gate decision) vs correctness vs gold key (scoring endpoint, computed post-run, never fed back to release)

## When to Apply
- LLM-assisted control design, PLC programming, symbolic controller synthesis, requirement-to-model generation
- Any mechatronic/CPS commissioning where wrong sign/coordinate binding creates instability (reversed polarity converts negative feedback into positive feedback)
- "Agentic mechatronics": LLM agents propose at development stage boundaries; deterministic acceptance retained at each requirement boundary

## Limitations (from the paper, honestly reported)
- Gate sensitivity not measured; coverage bounded by single grammar V1
- Post-seal campaign found grammar V1 anaphor failure (1/146 false releases) — not repaired, disclosed
- 183 model calls for limited process contribution (model-free replay reproduced all 83 releases)
- Abstention cost: 13/96 answerable tasks not released; 1 correct delivery lost vs ungated shell
- Gold user simulated; real user behavior, partial/delayed/refused answers not evaluated
- No physical safety result: closed-loop testing must remain a separate commissioning activity

## Related Skills
- [[llm-as-a-verifier]] — probabilistic verification framework (contrast: RBC demands determinism)
- [[security-guardrails]] — secrets/credential guardrails
- [[contractual-skills-governspec]] — contract-based skill governance

## Key References
- Simplex architecture (Seto et al. 1998; Sha 2001; Bak et al. 2009) — untrusted component behind verified decision module
- Neural Simplex / shielding (Alshiekh et al. 2018; Phan et al. 2020)
- External sound critics for LLMs (Kambhampati et al. 2024)
- VDI/VDE 2206 mechatronic development V-model
