---
name: a-multi-agent-system-for-autonomous-fine-tuning-fr
description: "A Multi-Agent System for Autonomous, Fine-Tuning-Free Clinical Symptom Detection: Development and Validation Study - Clinical notes contain many of the signs and symptoms that bring patients to care, yet this information rarely reaches structured fields. Existing ext..."
version: 1.0.0
author: Cameron Cagan, Pedram Fard, Jiazi Tian et al.
arxiv_id: 2607.12886
created: 2026-07-14
category: multi-agent-rl
tags: [cs.AI]
activation_keywords: [multi, agent, system, autonomous, fine, tuning, free, clinical, symptom, detection]
---

# A Multi-Agent System for Autonomous, Fine-Tuning-Free Clinical Symptom Detection: Development and Validation Study

## Overview

Clinical notes contain many of the signs and symptoms that bring patients to care, yet this information rarely reaches structured fields. Existing extraction approaches either rely on context-insensitive rules that generate false positives or on supervised models that require substantial fine-tuning. We present Pythia, a multi-agent system that autonomously writes and optimizes extraction prompts for clinical concepts without manual prompt engineering or fine-tuning. Running on a locally hosted open-weights model, Pythia keeps clinical notes on local infrastructure and selects prompts using development-set sensitivity and specificity. We compared Pythia with a curated lexicon across 72 signs and symptoms from 400 clinical notes representing 387 patients. Development (n=300) and validation (n=100) sets were partitioned independently for each concept. Pythia achieved mean sensitivity of 0.76 and specificity of 0.95, compared with 0.82 and 0.76 for the lexicon, and matched or exceeded the lexicon on both metrics for 20 of 62 directly comparable concepts. For 14 concepts where the lexicon labeled every note positive, Pythia recovered mean specificity of 0.97 by requiring a present-tense, patient-attributed finding rather than any textual mention of a term. Specificity transferred from development to validation with minimal degradation across prevalences, whereas sensitivity transfer weakened below 5% prevalence, reaching a mean gap of 0.25 below 2% prevalence. A BERT classifier fine-tuned per concept on the same development set achieved mean sensitivity of 0.23 and collapsed to zero sensitivity for concepts below roughly 5% prevalence. These findings suggest that autonomous, fine-tuning-free prompt optimization can produce symptom extraction prompts that generalize effectively from development to validation while remaining deployable on local infrastructure.

## Key Insights

- TODO: Extract key insights from the paper

## Implementation Approach

- TODO: Describe how to implement the techniques from this paper

## Applications

- TODO: List potential applications

## Activation Keywords

multi, agent, system, autonomous, fine, tuning, free, clinical, symptom, detection

---
