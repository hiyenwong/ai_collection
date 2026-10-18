---
name: textgrain-entropy-calibrated-watermarking
description: Use when watermarking LLM text. OpenAI textGrain method.
---

# textGrain: Entropy-Calibrated Watermarking for LM Text

Source: OpenAI technical report (Oct 5, 2026), accompanying the EU text-provenance announcement. Authors: Li, Wen, Chen, Long, Jain, Joly, Lam, Song, Su.

## When to use
- Embedding detectable statistical signals in LLM-generated text (regulatory provenance, academic integrity tooling, platform traceability)
- Evaluating watermark robustness under editing, translation, short-text, low-entropy-content regimes
- Designing detection access policies (why detectors should NOT be public)

## Core framework: watermarking as regularized optimal transport

1. **Coupling view**: A watermark is a joint distribution π(W, Ξ) over the sampled token W and keyed randomness Ξ (pseudorandom value from secret key + context window of up to L_ctx preceding tokens), with marginals fixed to the NTP distribution P and the key distribution μ. Unwatermarked sampling = independent coupling P ⊗ μ.
2. **Unbiasedness**: averaging the conditional token distribution Q(·|ξ) over Ξ ~ μ must recover P. Marginal constraints in the OT problem enforce this for free.
3. **Regularized OT selection**:
   π_λ ∈ argmin_{π∈Π(P,μ)} { E_π c(W,Ξ) + λ·D_KL(π ‖ P⊗μ) }
   with costs c(b,j) = −G_bj from standardized keyed Gumbel variables. Cost favors the chosen dependence; KL penalty limits it.
4. **Information-theoretic identity**: D_KL(π‖P⊗μ) = I(W;Ξ) = H(P) − E_Ξ H(Q(·|Ξ)). The KL penalty IS the average sampling entropy removed. An entropy budget β limits average entropy loss to β·H(P) — the strength knob has an exact meaning, and the detector does NOT need to know the budget used at generation.

## Block construction (dimensionality reduction)

- Keyed partition g: V → [B] assigns tokens to B blocks depending only on key + context window (detector can reconstruct without access to P).
- Block probabilities P_blk_b = Σ_{w: g(w)=b} P_w.
- OT couples P_blk to m equally-likely columns (row sums P_blk, column sums 1/m). Cost table from standardized Gumbels (Z − γ)/(π/√6). Solve with Sinkhorn under the entropy budget.
- Sampling: key+context selects a column uniformly → sample block from that column's normalized entries → sample token within block by ORIGINAL relative probabilities (within-block distribution untouched).
- Preserves unbiasedness; reduces optimization dimension from |V| to B×m.

## Why entropy calibration matters (vs Gumbel-max)
Gumbel-max (Aaronson 2023) always selects the same token at fixed context+key — repeated generation gives identical responses, killing sampling diversity. textGrain's entropy budget interpolates: β=0 → pure independence (no signal), β=1 → fully determined (no sampling randomness). Mutual information = the dial.

## Detection
Detector needs only generated text + secret key (reconstructs partition and Gumbel table from key+context). Tests statistical dependence between observed tokens/blocks and keyed values. No access to model internals, no need for the generation-time budget.

## Measured limits (publish honestly with any deployment)
- At 1% target false-positive rate: ~80% detection on 200-token passages, ~95% on 400-token (psychology-type content). Mathematics-type content: substantially lower (low word-choice freedom → little entropy to spend).
- Editing attacks: 10% synonym replacement drops detection 92%→66%; 25% replacement →17%.
- Quality cost ≈ zero: Astra benchmarks essentially unchanged with watermarking on (GPQA 94.44→93.94, BrowseComp 87.92→87.35, Terminal-Bench 4.0 53.90→56.06).
- Beat SynthID-Text in OpenAI's internal comparisons.

## Deployment policy template (from the EU rollout)
- Opt-in per API customer, OFF by default globally; auto-on only in the regulated region (EU) for eligible ChatGPT/Codex output.
- Detector access restricted to approved researchers/expert orgs (case-by-case). Rationale: public detectors teach adversaries the evasion threshold; false positives/negatives make public misuse likely. Detector reports only watermark presence — never user, prompt, ownership, or accuracy.
- Publish explicit "what a watermark does NOT tell you" list: not human-contribution share, not ownership/liability, not user identity, not accuracy, and absence of watermark ≠ human authorship.
- Layer with other provenance: C2PA Content Credentials + SynthID (image/audio) — text watermark is one layer, not the whole answer.

## Speculative sampling compatibility (Appendix B)
Draft and target share the same key and watermark construction. Draft proposes K tokens from watermarked Q^d; target computes Q^t in one forward pass; joint verification (r_i = min(r_{i-1}, Q^t_i(x_i)/Q^d_i(x_i)); h_i = z_i/(z_i + 1 − r_i)) determines longest retained prefix; residual correction RL_keep(w) ∝ [r_L·Q^t(w) − Q^d(w)]+ supplies target mass WITHOUT re-watermarking (already derived from watermarked distributions); bonus token from Q^t_{K+1}.

## References
- Technical report: cdn.openai.com/pdf/e9508624-d767-41b6-a26d-e34ca798ada6/textgrain-entropy-calibrated-watermarking-for-language-model-text.pdf
- Blog: openai.com/index/eu-text-provenance/
- Related: Kirchenbauer et al. 2023 (green-list); Aaronson 2023 (Gumbel-max); Dathathri et al. 2024 (SYNTHID-Text); Kuditipudi et al. 2024 (distortion-free).
