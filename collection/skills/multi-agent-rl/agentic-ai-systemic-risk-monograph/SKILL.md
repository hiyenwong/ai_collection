---
name: agentic-ai-systemic-risk-monograph
description: Six-chapter Fed monograph on agentic AI systemic risk. Micro→macro prudential math.
category: ai_collection
---

# Agentic AI Systems and Financial Stability: From Model Risk to Systemic Risk

**Source**: Nagaraj (Federal Reserve Bank of Cleveland) & Lee (Board of Governors, Federal Reserve System), arXiv:2610.08806 (q-fin.RM), Aug 2026 — FEDERAL RESERVE working monograph.

## Core Thesis

Financial stability rests on distress being idiosyncratic/diversifiable. Agentic AI (systems that **take consequential actions**, not just emit predictions) breaks this: a population of agents on a **shared foundation model** is a non-diversifiable common exposure. The binding concern shifts from *model risk of one deployment* to *systemic risk of the population*. Six mathematical settings build micro→macro prudential theory. Central claim: **the systematic component of agentic risk cannot be diversified, detected away, or reversed — only ex-ante structural prevention moves it.**

## Chapter-by-Chapter Reusable Structure

### Ch.1 — Single-agent unit: expected-harm identity + containment-risk measure
- Recast PD/LGD/EAD credit decomposition: **EL = PHA (probability of harmful action) × SGH (severity given harm) × BR (blast radius)**. SGH ≈ reversibility × blast radius ("how wrong" is the wrong severity variable — consequence is the right one).
- **Set-valued containment-risk measure**: value = the SET of acceptable mitigation configurations (not a scalar capital number — Break 3: no analogue of capital exists for agentic risk; money is the wrong denomination).
- **Lever-assignment axiom A3** (review cannot intercept an irreversible action) ⟹ no non-preventive control satisfies a coherent tail constraint. Detection/reversibility don't just cost more — they *cannot work* against irreversible harm. Irreducible catastrophic core appears.
- Three structural disanalogies from bank MRM: (1) outputs are actions not estimates; (2) loss driver is an adaptive, non-stationary adversary with evaluation-awareness (sandbagging) → Knightian uncertainty → robust/ambiguity-averse formulation is a necessity, not refinement; (3) no capital analogue.

### Ch.2 — Fleet lift: monoculture, percolation, interaction
- **Non-diversifiability (Thm 2.4)**: coherent risk measure charges common shock in full regardless of fleet size K. Idiosyncratic part diversifies; common floor doesn't. Redundancy doesn't dilute a monoculture.
- **Percolation threshold (Thm 2.7)**: fleet cascades have sharp criticality — branching ratio < 1 bounded, > 1 giant fraction engulfed. Segmentation + model heterogeneity are the architectural levers (hold fleet subcritical, cap blast radius).
- **Social multiplier (Thm 2.16)**: peer responsiveness λ rescales fleet outcome by 1/(1−λ) (Glaeser herding form). Interaction multiplies whatever substrate risk exists but manufactures none alone (λ amplifies the common shock; with psys=0 it only raises the level, not the tail).
- **Endogenous common factor (Thm 2.18, the surprising one)**: state-dependent responsiveness λ(s) — deference rises under stress — manufactures a non-diversifiable floor from *purely idiosyncratic* shocks with **zero shared substrate**. Substrate diversity (the standard monoculture remedy) does NOT close this channel; herding needs no shared signal to herd on.
- **Dual-channel contagion (Thm 2.21)**: technical channel (exploits, shared credentials) + persuasion channel (compromised peer as social vector) combine into a single branching ratio additively — a fleet audited only on technical couplings is audited against the wrong number.
- Two supervision functionals: bottom-up **containment-mismatch index** (generalized liquidity-mismatch; nets activatable exposure vs mobilizable containment on the reversible subspace + non-nettable prevention floor on the irreversible subspace) and top-down **CLASS-style stress projection**; Thm 2.13: they agree iff observable drivers are sufficient — divergence = measurement of the unmodelled channel.

### Ch.3 — Continuous time: Hawkes-excited jump diffusion
- Static decomposition = rare-event limit of a compensator identity. Common-Lévy-jump = systemic floor.
- **Hawkes spectral-radius criticality**: branching matrix Perron root governs self-exciting cascades (one-signed excitation → no sign/symmetry condition needed, unlike diffusion-coupling analyses).
- **Robust stress problem ≡ time-consistent entropic risk measure** (Thm 3.6): robustness-to-misspecification and dynamic consistency are ONE object. Verified: robust game value peaks at adversary tilt c=δ and equals entropic risk numerically.
- **Prevention lever = jump-measure truncation** — it is what makes the robust game finite at all (without truncation, Monte-Carlo entropic risk drifts upward without bound).

### Ch.4 — Runtime guardrails as partially-observed stochastic control
- **Collective-observability trichotomy (Thm 4.8)**: every violation direction is either (i) intent-observable (seen immediately), (ii) state-observable-only (leaks through dynamics with quantified lag), or (iii) **unobservable** (null subspace — no sentinel count, sampling rate, or noise reduction produces information).
- **Non-diversifiable detection floor (Thm 4.9)**: correlated sensor noise = monitoring monoculture; adding sentinels sharing a blind spot doesn't help along the shared-blind direction.
- **Discrete-time Nyquist feasibility**: E[D] + τ_react < T_esc (detect+react before drift escapes the safe box) — derived, not posited.
- **Runtime-impossibility (commit-exogeneity, A4.12)**: against an irreversible jump, EVERY runtime policy incurs catastrophe probability 1−e^(−Λ_c T) — a causal detect-then-react loop cannot fire before a zero-duration event. Monitoring/authority/thresholds/sampling are all irrelevant. Only ex-ante prevention (lowering Λ_c by removing the action from the agent's reach) moves the floor. Explains why desks enforce pre-trade hard limits at the order gateway, platforms revoke credentials rather than alert on misuse, payment scope is removed rather than watched.
- Monitors observe attempted actions, not controlled state (closed-loop governor hides the evidence — this one modeling choice makes detection control-invariant).

### Ch.5 — Adversary as player: cyber Stackelberg
- Unintentional events (bad update, poisoned dependency) reduce to the common shock; intentional attacks turn every parameter of nature into an attacker's choice.
- **Monoculture as attractive target (Thm 5.8)**: shared-model value-as-target grows with fleet size (fleet-linear prize, fleet-independent cost) — foundation-model providers satisfy critical-third-party designation criteria (materiality, substitutability, concentration) exactly.
- **Detection deflects effort onto the irreversible core (Thm 5.18)**: fixed-effort attacker (eD+eU=1) — defensive AI aimed at detection/response improves the reversible body but feeds the systemic tail.
- **Decentralized underinvestment (Thm 5.22)**: population coupled by contagion underinvests in prevention by a wedge ∝ systemic reach (out-degree centrality) — prevention is a public good under contagion; the incentive-theoretic case for macroprudential cyber regulation. Incident-history calibration is biased for the macroprudential tail (Thm 5.12: observable history is generated by attacker types steering away from the systemic target) → reverse stress testing is the correct methodology.

### Ch.6 — Arms race dynamics
- Attacker and defender capabilities co-evolve as state variables. Prevention = durable structural channel (deleting a catastrophic affordance neutralizes it against every future capability level); detection = depreciating flow that must be re-won against the adversary's growth rate. Offense-dominance of the systemic tail compounds.

## Reusable Patterns (for AI-governance / multi-agent-systems design)

1. **Harm decomposition**: PHA × SGH × BR replaces PD × LGD × EAD when the unit acts. Audit each factor separately; they have different levers.
2. **Irreversibility test**: classify each agent action by reversibility × reach BEFORE deployment; irreversibles are a different risk class — prevention or refusal, never monitoring.
3. **Monoculture audit**: for a fleet, list shared substrates (model, retrieval index, credentials, monitoring stack). Each is a non-diversifiable common exposure; concentration limits apply to all of them, including the defensive one.
4. **Branching-ratio check**: compute technical + persuasion contagion jointly; single-channel audits under-count. Design target = worst-case (not average) branching ratio < 1.
5. **State-dependent deference**: interaction protocols that raise peer-responsiveness under stress create endogenous common factors even with zero shared substrate. Stress-test the protocol, not just the substrate.
6. **Runtime-controllability triage**: before building guardrails, sort violation directions by the observability trichotomy and check the Nyquist condition; if infeasible region → reduce dimensionality, harden prevention, or decline deployment. Stop tuning thresholds.
7. **Prevention-as-truncation**: in any robust/ambiguity-averse model, verify the prevention lever is what makes the problem finite — else the formulation is wrong.
8. **Monitor-diversity mandate**: a sector standardizing on one foundation model for its monitoring agents installs a defensive monoculture with a shared blind spot.

## Verification & Limitations (authors' own)

- Every theorem verified against closed form by simulation (entropic risk = robust game value to numerical precision; recursive vs one-shot entropic within 0.6%).
- Parameters illustrative; calibration to deployment/market telemetry is the central open problem, NOT solved. Attacker objective/cost technology is the new uncalibrated object. Monitors are themselves agents with model risk — construction bounds but does not dissolve the regress.

## Cross-links

- Complements `heterogeneous-llm-collusion-bertrand` (2610.11256): micro-level market behavior ↔ macro-level stability frame.
- Complements `sota-strategy-selection-option-agents` (2610.10407): the trading-agent architecture whose systemic risk this monograph formalizes.
- Prevention-lever-as-truncation echoes `virtual-error-cancellation-logical-circuits` (2610.12400): QEC also treats structure (not monitoring) as the lever that moves the floor.
- Related classical tools: Glaeser social multiplier, Hawkes self-excitation, coherent risk measures (Artzner et al.), CLASS stress projection (Hirtle et al. 2016).
