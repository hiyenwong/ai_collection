---
name: field-intelligence-jazz-improvisation
description: "Dyadic creativity pitch=identity rhythm=shared state"
category: neuroscience
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [neuroscience, creativity, predictive-processing, music-cognition, hyperscanning]
    related_skills: [mllm-brain-alignment-task-probing, harmonic-theory-behavior, emergent-language-consciousness]
trigger: interpersonal creativity, joint improvisation, jazz duos, turn-taking interaction, predictive processing creativity, information dynamics of music, surprise and uncertainty fluctuations, statistical learning model, IDyOM, hierarchical Bayesian statistical learning, field intelligence, collective creativity, inter-brain synchrony alternative, musical expectation, novelty regulation between minds, conversational coupling, complementary surprise, push-pull interaction, double dissociation identity vs shared state, pseudo-duet null model, Jensen-Shannon divergence of predictive distributions
---

# Field Intelligence in Dyadic Improvisation: Pitch Carries Identity, Rhythm Carries the Shared State

**Source**: "Music Between Two Minds: Individual Signatures, Shared States, and the Emergence of Creative Interaction" — Tatsuya Daikoku, Risa Kobayashi, Rina Tabuchi, Yoshia Abe, Yasuo Kuniyoshi (Univ. of Tokyo / Cambridge CNE / Seitoku Univ.), arXiv:2610.31131 (q-bio.NC, 22 Oct 2026).

## When to Use

Use when studying **how two agents (humans or models) jointly regulate novelty during real-time turn-taking interaction** — improvised music, conversation, dialogue, collaborative design; when testing whether interacting partners converge, diverge, or something else; when you need a measurable, corpus-level operationalization of "collective" or "emergent" states that cannot be attributed to either partner alone; when designing analyses of dyadic sequence data with a shared predictive model.

## Core Contribution

First note-level quantification of how predictive fluctuations (surprise, uncertainty) are organized **between** two improvising minds, over 986 professional jazz improvisations (6 duos, 12 professionals, 54 takes, 530 trading solos, 11,433 notes; Autumn Leaves solo-trading sections). Central finding — a **double dissociation**:
- **Pitch fluctuations = individual identity**: partners differed within 90% of takes; identity decodable from a single solo (AUC=0.87); separation never narrowed across turns or takes (between-performer JSD 2.14× within-performer, stable up to 22 turns).
- **Rhythm fluctuations = shared performance state**: partners statistically indistinguishable within a take (only 39% of comparisons significant); performer undecodable (AUC=0.52); variance decomposition: 74.3% of pitch-uncertainty variance = performer, 0.6% = take; rhythm: take R²=0.27–0.85 in 6/6 duos, performer ≈ 0.
- The shared rhythmic state is **take-specific** (real hand-offs 2× closer than pseudo-duets of the same two people assembled from different takes — even adjacent takes), **drifts collectively** within a performance (both partners move away from their own past at the same rate as from each other; lag–distance ρ=+0.17 in 6/6 duos), and is **renegotiated at every hand-off**: when one performer exceeds their own average surprise, the partner's next solo falls below theirs (push–pull complementarity: rhythm r=−0.230, pitch r=−0.151, both abolished by within-performer shuffle and circular-shift nulls).

=> Improvising pairs are neither one fused system nor two independent ones: **individuality and togetherness coexist, carried by different informational dimensions**, with active turn-level compensation on top.

## The "Field Intelligence" Framework (Daikoku 2026)

Creative interaction is sustained by predictive-fluctuation structure that belongs to the **interaction level** — not reducible to either partner. The puzzle alignment alone cannot solve: full convergence produces nothing new; independence produces no interaction. Prediction: individual differences are NOT erased, yet some predictive dynamics become jointly organized — detectable as occasion-specific structure + moment-to-moment dependence unreconstructable from the two performers independently. This paper is the first empirical test.

## Measurement Pipeline (reusable method)
1. **Corpus-trained reference model, frozen yardstick**: HBSL (hierarchical Bayesian statistical learning) trained on Weimar Jazz Database (456 transcribed solos, 78 musicians), then applied note-by-note in memory-keeping mode to the Improvising Duos corpus (Moran et al. 2015). Same model state evaluates both partners ⇒ between-partner comparisons uncontaminated.
2. **Per-note predictive quantities** (bits): surprise = information content I(e_{t+1}) = −log₂ P(e_{t+1}|e_t); uncertainty = entropy H of the predictive distribution. Computed separately for **pitch, rhythm, and joint streams** (all transposed to C major/A minor; note-to-note transitions only, chunking disabled).
3. **Audio → per-performer symbolic streams**: AI stem separation (LALAL.AI, after AuxIVA/ILRMA proved insufficient) → Klangio MusicXML transcription → manual cleanup → DTW audio alignment + Viterbi phrase-level pitch refinement (octave-error suppression).
4. **Duo as unit of inference** (n=6): effects computed within duo, tested across duos (paired t, df=5) + consistency ratio (x/6 duos) as distribution-free index. Note-level tests: Mann–Whitney U (skewed distributions).

## Analysis Battery (the transferable design)
- **Significance-rate contrast**: within-take between-performer vs between-take within-performer (pitch 90% vs 35%; rhythm 39% vs 60%).
- **Distribution distances**: 8-quantile-bin distributions per solo, Jensen–Shannon divergence (symmetric, bounded, empty-bin safe).
- **Identity decoding**: leave-one-take-out logistic regression on 10 summary features → AUC per duo.
- **PERMANOVA + mixed-model variance decomposition** on JSD matrices: performer vs take partial R² (restricted permutations, 999 iters).
- **Lag-stratified drift**: strict alternation ⇒ odd lags always cross-partner, even lags always own-past — read distance-to-other and distance-to-self as parallel series (no mixing).
- **Pseudo-duet null**: compare real partner-next-solo distance vs same-partner-instrument solo at same turn position in OTHER takes (the "same two people, not playing together" control; adjacent-take variant cancels slow session drift).
- **Hand-off complementarity**: detrend per take, express residuals relative to each performer's own mean, correlate consecutive-solo deviations; nulls = within-performer turn-position shuffle (A) and circular shift (B) — preserve everything about each individual except alignment with the partner.

## Operational Lessons
1. **Don't collapse dyads to one axis**: intermediate-distance compromises on a single dimension are NOT how creative coupling works — look for **division of roles across dimensions** (one fully shared, one fully individual) plus exchange-point compensation. An inverted-U on a single projected axis can be an artifact of averaging across such a partition.
2. **Complementarity ≠ imitation**: negative turn-coupling (spend/save on surprise) is the signature of joint regulation; positive coupling (convergence/alignment) is a different animal. Decide which one your theory predicts before testing.
3. **Occasion-specificity needs the pseudo-duet control**: showing two people are similar is NOT evidence of interaction-level structure — they may just be similar people. Compare against the same pair reassembled from different occasions.
4. **What is shared moves; what is not shared is preserved**: a group that travels together in a shared dimension explores without fragmenting while stable individual dimensions maintain diversity — a candidate general principle for collective creativity/cultural evolution, testable in dialogue.
5. **Shared-reference-model measurements cancel state confounds**: evaluate both partners at the same model state; pair with adjacent-occasion nulls to kill slow drift.

## Predicted Transfer to Dialogue/LLM Settings
Given a corpus-trained reference model: some informational dimensions of speech should identify the speaker and resist convergence; others should belong to the particular conversation, drift with it, and show compensatory surprise regulation at turn exchanges. Directly testable on chat/LLM-agent dyads with a frozen LM as the yardstick.

## Limitations (from source)
- Every duo = different instruments ⇒ melodic identity may partly be instrument affordance (rhythmic findings untouched — their defining feature is the ABSENCE of individual specificity).
- Observational: coupling exceeds stringent nulls, but causal pathway untested (needs simulation + perceptual manipulation experiments).
- Single tune, single idiom; pitch→identity / rhythm→state assignment may be idiom-specific.
- Reference-corpus choice shifts absolute surprise/uncertainty but within-corpus contrasts should be robust.

## Pitfalls
- Strict alternation + stable level differences between performers generates **spurious negative correlations** at hand-offs — the shuffle/circular-shift nulls are mandatory, not optional.
- Significance-rate comparisons at note level need equal statistical power across the contrasted families (same note counts).
- Do not average notes away when the claim is about distributions — use JSD/quantile representations, not means alone (though means suffice for the complementarity test after detrending).
- Model "memory-keeping" online updates change state slowly — always include the adjacent-take pseudo-duet variant.
