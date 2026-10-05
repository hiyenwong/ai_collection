---
name: brain-to-language-decoding-survey
description: Brain-to-language decoding tasks, signals, and evaluation.
trigger: brain-to-language decoding, speech neuroprosthesis, inner speech decoding, articulatory decoding, EEG MEG language decoding, five-level BCI trajectory, semantic reconstruction, communication cost evaluation
license: MIT
metadata:
  arxiv_id: "2609.27650"
  published: "2026-09-23"
  authors: "Yiqian Yang, Yiqun Duan, Chenyu Liu, Yiqi Wang, Xinliang Zhou, Chin-Teng Lin, Yu Zhang (Uploading Inc / UTS / Stanford HAI)"
  tags: [brain-computer-interface, speech-decoding, survey, inner-speech, neuroprosthesis, evaluation-methodology]
---

# Brain-to-Language Decoding: Tasks, Signals, Methods, Evaluation (Survey Synthesis)

Methodology from arXiv:2609.27650 — "Brain-to-Language Decoding: Tasks, Signals, Methods, Evaluation, Practical Use and Beyond" (Yang, Duan et al., Sep 2026). Comprehensive survey with no lower year limit through Sep 2026.

## The Organizing Framework: Task × Signal × Target

The survey's central move is to make **task conditions** (what the participant actually did) the primary axis — not vocabulary size, model architecture, or output form. The same word heard, read, imagined, or attempted engages different neural populations and provides different supervision.

### Three Task Groups, Nine Subtypes

| Group | Subtype | Meaning |
|---|---|---|
| **Articulated** | Overt | Executed articulation with audible speech |
| | Mouthed | Executed articulation without audible speech |
| | Limited | Impaired speech attempts WITH actual residual articulation |
| **Inner** | Articulatory | Internal simulation of speaking movements/sensations, no attempted execution |
| | Auditory | Internal simulation of speech sounds |
| | Mixed | Explicit combination of articulatory + auditory imagery |
| **Perceived** | Auditory | Perception of externally presented speech sounds (Listening) |
| | Visual | Perception of written language (Reading) or visible articulation (Lipreading) |
| | Audiovisual | Joint auditory + visual language perception |

**Critical definitional discipline**: "Clinical attempted speech" specifies a motor intention. Residual movement determines confirmed Articulated membership; a **movement-free motor attempt stays "attempted speech"** — it is NOT silently reassigned to Inner imagery. This prevents the chronic confation of attempted-speech clinical results with imagery-based results.

### Signal → Representation → Output Chain

- **Invasive (ECoG, sEEG, Utah array, stereo-EEG)**: high-resolution speech-production cortex → phonetic/articulatory trajectories → text, streaming speech, facial animation (Metzger 2023, Willett 2023, Littlejohn 2025 home use).
- **Non-invasive (EEG, MEG)**: coarser but safe → shared corpora (Hollenstein ZuCo, LibriBrain) + pretrained speech/language representations (Whisper, LLMs) bridge the gap (Défossez 2023 neural code; d'Ascoli 2025).
- **Haemodynamic (fMRI)**: long timescales → semantic reconstruction (Tang 2023 semantic decoder).

## Three Complementary Decoding Routes

1. **Phonetic/lexical targets** — support word-sequence construction (articulatory + production activity).
2. **Acoustic/articulatory trajectories** — support voice output and facial animation.
3. **Contextual/semantic representations** — support recovery of meaning across wording changes.

Each route preserves different aspects of a message; pretraining and multimodal supervision increasingly connect them.

## Evaluation Methodology (the survey's second pillar)

- **Within-protocol comparison only**: published performance and communication costs are meaningful only inside their reported protocol; cross-study numbers are not comparable without shared benchmarks.
- **Shared benchmark lineages**: Brain-to-Text '24 (attempted speech), LibriBrain/MEG-XL (listening MEG, 50-word retrieval with 13% vs full-data training budgets), NeuGPT/NeuSpeech/MAD/BrainECHO (MEG-to-text, BLEU-1 5→13 as pipelines mature).
- **Negative evidence counts**: leakage-audited cross-subject EEG vowel benchmarks show when claimed decoding doesn't generalize.
- **Communication costs alongside accuracy**: calibration time, feedback loops, user control (initiate/reject/revise) are first-class metrics, not afterthoughts. Streaming, adaptation, sustained home use are the practical-use frontier.

## The Five-Level Trajectory (prospective, not maturity grades)

| Level | Name | Defining capability | Transition test |
|---|---|---|---|
| L1 | Command | Issue a discrete instruction; select/cancel a chosen action | Intentional selection evidence (withholding), not just task-correlated activity |
| L2 | Language | Express formulated words — compose NEW sentences beyond fixed commands | Large-vocabulary neuroprostheses (Willett 2023, Metzger 2023) are foundations |
| L3 | Meaning | Convey intention independent of wording — preserve intended RELATIONS across formulations | Paraphrase accuracy alone insufficient; must distinguish meaning from covertly formulated words (nonverbal elicitation, transfer to new formulations) |
| L4 | Scenario | Share an unfolding situation: actors, goals, order, changing conditions | Relational + temporal structure; new combinations beyond rehearsed narratives |
| L5 | Bidirectional | Receive new content via neural return channel; refine it (concept in → refinement out) | Transfer to untrained content; new judgements beyond memorized stimulation-response codes |

**L3 is the frontier; L4-L5 are prospective.** Utility is separate from level — a reliable L1 can serve a person better than an unreliable L4.

## Key Synthesis Points

1. **Recoverable information = f(behaviour, sampled populations, measurement timescale)** — jointly. This explains why modality roles are complementary rather than competing.
2. **Match the decoding target to available information**: forcing text output from signals that only support command-level distinctions produces misleading claims.
3. **User authority is a design requirement**: activation, message release, data retention, error recognition and repair — especially as inner-speech decoding raises mental-privacy questions. Fluent output ≠ unrestricted access to thought.

## Applying This Skill

Use when: (a) designing/evaluating a BCI decoding study — pick the task descriptor first and report it; (b) choosing a decoding target matched to your recording modality; (c) benchmarking against the right lineage; (d) positioning a new system on the L1-L5 trajectory; (e) reviewing inner-speech decoding claims for definitional soundness (imagery vs attempted speech).

## Related Skills
- [[brain-to-language-source-attribution]] — source attribution for MEG-to-audio decoding
- [[eeg-silent-reading-decoding]] — decoding silent reading from non-invasive EEG
- [[zero-shot-imagined-speech-meg]] — zero-shot imagined speech from MEG
- [[unibci-invasive-foundation-model]] — unified pretrained invasive BCI model
- [[iphoneme-brain-to-text-als-conformerxl]] — brain-to-text for ALS

## Sources
- arXiv:2609.27650 — Yang, Duan, Liu, Wang, Zhou, Lin, Zhang (2026)
- Anchor citations: Moses/Metzger/Willett (clinical neuroprostheses), Tang 2023 (semantic reconstruction), Défossez 2023 (listening EEG), LibriBrain/Brain-to-Text '24 (benchmarks), Littlejohn 2025 / Card 2026 (streaming + home use)
