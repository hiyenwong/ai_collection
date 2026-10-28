---
description: Use when enabling external research on private usage data.
name: privacy-preserving-external-research-pilot
version: 1.0
author: cs-cron-2026-10-27
license: MIT
metadata:
  hermes:
    tags: [privacy-preserving-analysis, independent-research, usage-data-access, aggregate-statistics, question-wording-calibration, proxy-dataset-shift, transparency-without-enablement, third-party-privacy-audit, research-governance, anthropic-insights]
    source: https://www.anthropic.com/research/enabling-independent-research
    published: 2026-08-26
    related_skills: [privdrift-active-context-privacy, ai-expectations-gap-survey-methodology, open-weights-abliteration-risk, ai-native-employment-transformation]
---

# Privacy-Preserving External Research on AI Usage Data

Methodology from Anthropic's "Enabling independent research on how people use Claude" (Societal Impacts team, Aug 26 2026) — the first program where external researchers (Stanford SALT Lab, Oxford Human Information Processing Lab, METR) designed and ran independent studies on an AI company's own usage data: ~250,000 Claude.ai / Claude Code conversations (April–May 2026) analyzed via Anthropic Insights (ex-Clio), with aggregate results released publicly.

## One-Line Summary

External researchers get **aggregate-only** access (LLM-classified categories + percentages, never raw conversations), under an **independence-preserving contract** (lab review limited to privacy / safeguard-enablement / confidentiality / accuracy), with **question calibration on public proxy data + documented distribution shift**, a **transparency-without-enablement disclosure rule** for misuse categories, and a **third-party privacy audit + explicit threat model** for everything released.

## When to Use / Activation

- Designing any program that gives external parties research access to sensitive user data (AI usage logs, platform telemetry, health/behavioral data).
- Deciding what aggregate statistics can be published vs. what enables harm.
- Calibrating LLM-as-classifier questions when nobody can read the underlying records.
- Structuring research agreements so external findings stay publishable even when inconvenient to the data holder.

## The Six Program Design Rules

1. **Aggregate-only access.** Researchers pose questions (e.g., "What type of guidance is this person asking for?"); an internal classifier answers per-conversation; researchers see only final categories and the percentage of conversations in each — the same legal/privacy review as internal analyses, never raw records.
2. **Independence-preserving contract.** Data-holder review rights restricted to exactly four domains: user privacy, information that could help people violate usage policies, confidential business information, and research accuracy. Everything else — findings, framing, publication — is out of the data holder's hands; publication is contractually free even if inconvenient.
3. **Question calibration with proxy data + shift caveat.** LLM-classifier outputs are highly sensitive to question wording, and mis-wordings are nearly uncatchable when no one can read the underlying conversations. Internal teams iterate for weeks; external partners can't (each iteration would need a fresh privacy review). Fix: test questions on a public proxy corpus (WildChat) where answers can be checked against raw conversations — **but proxies skew** (WildChat skews casual/creative vs. real platform traffic), so questions that validated on the proxy can misclassify on real data. Mitigation: ship interpretation guidance with every release; invest in pre-validation tooling before scaling.
4. **Transparency without enablement.** Publish what misuse users *attempted*; never publish *how* they circumvented safeguards. In the pilot <5% of categories/conversations were affected; in every case the researchers were told which clusters were altered or removed and why. Surfaced violations are simultaneously routed to the internal safeguards team — disclosure and defense are one pipeline.
5. **Third-party privacy audit + explicit threat model.** An independent auditor (Imperial College London) verified the privacy protections actually held for everything shared, and all released data is held to a published privacy threat model. Do not rely on the data holder's self-attestation.
6. **Overlap as a feature.** When external proposals duplicate internal research (METR's productivity study vs. internal economics work), treat it as independent replication from a different vantage point, and connect the two teams — not as competition to be discouraged.

## Operational Lessons (honest costs)

- The program was **slow and resource-intensive** relative to the lab's normal research tempo — privacy review, per-study legal gates, and interpretation guidance all add latency. This is the main scaling bottleneck, not researcher demand.
- Question-wording errors are the dominant scientific risk of the aggregate-only design; budget for them explicitly.
- Expect some partner studies to still be underway at publication; release early results anyway with "writeup pending" links.

## Pilot Findings (context for reuse)

- **>50% of conversations delegated consequential tasks** to the model (esp. legal/financial guidance) — contradicting the prior assumption that people keep high-stakes work for themselves.
- ~3/4 of conversations: human sets direction, model assists, human adapts output rather than using it verbatim.
- Collaboration friction is common and often *productive* — it forces intent clarification and keeps users engaged.
- Affect–behavior coupling: model warmth ↔ user positivity; refusal ↔ pushback; eccentricity ↔ intellectual engagement; plain helpfulness ↔ satisfaction. Experience patterns resemble everyday web browsing.
- METR: newer model generations deliver larger real speedups; and model self-estimates of counterfactual task time correlate with actual developer completion times (validating the estimation method).

## Pitfalls

- Publishing raw aggregate percentages without question-wording documentation invites misreading — always ship the questionnaire text and per-category guidance.
- A public-proxy validation is necessary but NOT sufficient; treat proxy-to-production shift as an explicit threat, not a surprise.
- "Aggregate" is not automatically private: small-cell categories can re-identify; the audit and threat model must cover cell-size thresholds.
- Review rights creep: any contract clause beyond the four allowed domains converts "independent research" into PR review — resist adding veto categories.

## Connection Map
- Privacy auditing of LLM chat → privdrift-active-context-privacy.
- Survey/measurement methodology on AI populations → ai-expectations-gap-survey-methodology.
- Disclosure rules for dangerous capability info → open-weights-abliteration-risk, oss-scanner-model-only-disclosure.
- Aggregate labor-market measurement on AI-era work → ai-native-employment-transformation.
