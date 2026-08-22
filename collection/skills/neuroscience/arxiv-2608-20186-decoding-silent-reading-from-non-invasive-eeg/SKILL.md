---
name: arxiv-2608-20186-decoding-silent-reading-from-non-invasive-eeg
description: 'Decoding silent reading from non-invasive EEG (arXiv: 2608.20186)'
category: neuroscience
version: "1.0"
date: 2026-08-22
---

# Decoding silent reading from non-invasive EEG

**Authors:** Ingo Marquardt, Anthilia Alchanat, Priyanka Jain
**arXiv:** 2608.20186
**Utility:** 1.00
**Published:** 2026-08-20T15:41:05Z
**Link:** http://arxiv.org/abs/2608.20186

## Abstract

Non-invasive decoding of inner speech faces a fundamental data problem: a corpus pairing brain activity with a person's spontaneous inner monologue cannot be collected, and the available proxy paradigms (cued repetitive and retrospectively reported generative inner speech) are slow to acquire, poorly time-locked, and subject compliance is unverifiable. We therefore treat silent reading as a scalable proxy task and ask how much lexical and semantic information a contrastive decoder can extract from it. We report an open-vocabulary analysis of approximately 240,000 word presentations recorded from a single densely-sampled participant across 393 runs (ca. 49 h) of 19-channel dry-electrode EEG. Words from continuous narrative text were presented in rapid serial visual presentation, with typography randomised on every trial to partially decorrelate word identity from low-level visual form. A convolutional EEG encoder, optionally followed by a causal transformer, was trained with a CLIP-style contrastive objective to align short EEG windows with hidden-state embeddings of the presented word taken from a large language model. Decoding, evaluated as word-grouped top-10 retrieval against permutation baselines, was reliably above chance, extended to mid-frequency and rare words, and scaled log-linearly with training-data volume with no sign of saturation. Removing occipital and posterior-temporal electrodes reduced the word-level gain by roughly one third but left context tracking unchanged. Control analyses separate word-level decoding from narrative context tracking and from a non-neural positional prior introduced by the transformer's positional embedding. These results establish that open-vocabulary word-level information is recoverable from EEG during silent reading, and that decoding is data-limited rather than saturated.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Decoding silent reading from non-invasive EEG". 
The paper presents novel ideas in neuroscience that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.20186
