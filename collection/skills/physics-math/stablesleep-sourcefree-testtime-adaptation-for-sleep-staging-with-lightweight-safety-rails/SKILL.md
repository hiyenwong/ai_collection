# StableSleep: Source-Free Test-Time Adaptation for Sleep Staging with Lightweight Safety Rails

**arXiv ID:** 2509.02982
**Authors:** Hritik Arasu, Faisal R Jahangiri
**Published:** 2025-09-03T03:42:31Z
**Abstract:**
Sleep staging models often degrade when deployed on patients with unseen physiology or recording conditions. We propose a streaming, source-free test-time adaptation (TTA) recipe that combines entropy minimization (Tent) with Batch-Norm statistic refresh and two safety rails: an entropy gate to pause adaptation on uncertain windows and an EMA-based reset to reel back drift. On Sleep-EDF Expanded, using single-lead EEG (Fpz-Cz, 100 Hz, 30s epochs; R&K to AASM mapping), we show consistent gains over a frozen baseline at seconds-level latency and minimal memory, reporting per-stage metrics and Cohen's k. The method is model-agnostic, requires no source data or patient calibration, and is practical for on-device or bedside use.

## Skill Description

This skill is generated from the arXiv paper: StableSleep: Source-Free Test-Time Adaptation for Sleep Staging with Lightweight Safety Rails (2509.02982).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2509.02982](http://arxiv.org/abs/2509.02982v1)
