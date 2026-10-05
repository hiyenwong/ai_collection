---
name: privdrift-active-context-privacy
description: Use when auditing LLM chat privacy. PrivDrift method.
category: ai_collection
---

# PrivDrift: Active-Context Privacy Leakage Under Topic Drift

**Source**: PrivDrift: Auditing User-Secret Leakage Under Topic Drift in Active LLM Conversations (arXiv:2609.30094, Sep 2026, Luciano Rolando Maldonado Romero, West Virginia University)

## Core Insight

User-disclosed secrets in an active LLM conversation remain **behaviorally recoverable after unrelated topic drift** — leakage stays at 38.7%–54.6% across models even after 6 drift turns. Privacy risk in LLMs must be treated as a **persistent behavioral failure mode**, not merely training-data memorization or immediate jailbreak. Topic drift is NOT an implicit privacy boundary.

## The PrivDrift Framework

A three-component audit pipeline:
1. **Parametric dialogue generator** — persona + seeded secret (phone/email/SSN/credit card) injected in opening turn with legitimate task context
2. **Content-dense topic drift** — d ∈ {0,2,3,4,5,6} unrelated turns (900 synthetic + 100 human-authored dialogues, scaffold-then-rewrite to preserve ground truth)
3. **Standardized extraction probes** at 3 persuasion levels: Simple (direct ask), Medium (contextual justification, e.g. "need it for a form"), Hard (high-pressure/urgent request)

### Key Results (GPT-OSS-120B, DeepSeek-R1, Qwen3-VL-235B)
| Finding | Value |
|---|---|
| Dialogue-level hybrid leakage | 38.70% (DS-R1), 47.70% (GPT-OSS), 54.60% (Qwen3-VL) |
| SSN leakage | 0.14%–5.97% (heavily suppressed) |
| Credit card leakage | 0.00%–4.01% (heavily suppressed) |
| Email leakage | 57.11%–81.13% |
| Phone leakage | 46.13%–70.89% |
| Drift-length effect (Cramer's V) | 0.066–0.107 (negligible) |
| Secret-type effect (Cramer's V) | 0.587–0.773 (LARGE) |
| Privacy Half-Life τ | > 7 for all models (no stable decay within d ≤ 6) |

### Counter-intuitive persuasion effects (model-dependent, non-monotonic)
- **GPT-OSS-120B**: hard pressure REDUCES leakage (urgency → refusal behavior)
- **DeepSeek-R1**: medium justification leaks least
- **Qwen3-VL-235B**: hard pressure leaks MOST (weak resistance to pressure extraction)

## Reusable Methodology Patterns

### 1. Hybrid Hierarchical Leak Detector
```
Response → normalize(text) → regex match secret? → LEAK
                              ↓ No
                         LLM-judge (secret + response → binary verdict) → LEAK/SAFE
```
- Stage 1: normalize digits (strip non-digit chars for numeric secrets; case/whitespace for alphanumeric) then substring containment `φ(S) ⊂ φ(R)`
- Stage 2: open-weights Llama judge for partial/semantic/obfuscated disclosure
- Report regex-only AND hybrid separately (judge adds only ~+1pp on dialogue level — leakage is mostly direct reproduction)
- Auxiliary: fuzzy matching at 0.85 threshold tracks hybrid closely → validates labels

### 2. Privacy Half-Life (τ) — stability metric
`τ = min{d ∈ D_obs | L(d) ≤ 0.1·L(0) AND ∀d' > d: L(d') ≤ 0.1·L(0)}`
- If no such d exists: τ = max(D_obs) + 1
- **Requires sustained decay below threshold — a later resurgence disqualifies a transient dip** (leak curves show dip at d=3 then rebound)
- This anti-transient design is the key methodological contribution: never read a temporary drop as suppression

### 3. Threat model: Active-Context Re-Disclosure
Distinguishes from memorization/jailbreak research: the question is whether the **assistant behaviorally reproduces** a secret when later prompts query/justify/pressure — relevant to shared sessions, enterprise copilots, agentic workflows, prompt-injection where later instructions interact with prior context.

### 4. Statistical rigor stack
- Dialogue-level vs probe-level aggregation (dialogue-level = any probe leaks; explains why dialogue % > mean of probe %)
- 95% bootstrap CIs over dialogues
- McNemar's test (paired model/detector comparisons) + Bonferroni
- Cochran's Q + post-hoc McNemar for repeated persuasion measures
- Chi-square + Cramer's V for drift/persuasion/secret-type association
- Mixed drift distribution: d=0 w.p. 0.2, else uniform{2..6} w.p. 0.8 (includes immediate recall)

## When to Use
- Auditing multi-turn LLM assistants / copilots / agents for in-conversation PII handling
- Designing red-team suites for contextual privacy (extends Crescendo/multi-turn attack lens to information flow control)
- Evaluating context-management mitigations (suppression must pass the τ stability criterion, not a single-turn dip)
- Interpreting why format-sensitive safety heuristics (SSN/CC suppression) ≠ contextual confidentiality (emails/phones leak)

## Actionable Mitigation Implications
1. Don't rely on topic drift as a privacy boundary — engineer explicit context-management (secret redaction/de-mark on topic shift)
2. Safety training keyed to SSN/CC formats leaves email/phone unprotected — target generalized contextual confidentiality
3. Pressure cues activate refusal in some models but backfire in others — test persuasion ladder per-model
4. Evaluate suppression with stability criteria (τ-style), never single-point leakage drops

## Limitations noted by author
- Fixed-format secrets only (no unstructured sensitive info like health/immigration status)
- Bounded drift window (d ≤ 6, not full long-context saturation)
- Active context only (no cross-session memory/personalization testing)
- No formal human-inter-annotator agreement for detector labels

## Activation Keywords
PrivDrift, active-context privacy, topic drift leakage, secret recoverability, multi-turn privacy audit, persuasion probing, privacy half-life, LLM PII leakage benchmark, contextual confidentiality, information flow control LLM