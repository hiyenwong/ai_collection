---
name: clinical-reasoning-llm-hepatocellular-carcinoma-risk-stratification
description: "HCC-STAR: clinically aligned LLM for hepatocellular carcinoma staging, treatment, and prognosis. Reads EMR narratives, outputs risk stratification, guideline-consistent treatments with rationales, and survival estimates. Outperforms GPT-5 and Gemini-2.5 Pro. Activation: clinical-reasoning LLM, hepatocellular carcinoma, risk stratification, treatment guidance, EMR."
metadata:
  arxiv_id: "2607.08602"
  published: "2026-07-09"
  authors: "Peng Cui, Jitao Wang, Siyan Xue, Yao Huang, Haoming Xia"
  tags: [clinical-reasoning-llm, hepatocellular-carcinoma, risk-stratification, treatment-guidance, electronic-medical-records]
---

# Towards Precision Therapy in Hepatocellular Carcinoma: A Clinical-Reasoning LLM for Risk Stratification and Treatment Guidance

## Overview

HCC-STAR (Hepatocellular Carcinoma Staging, Treatment And pRognosis) is a clinically aligned large language model that reads routine EMR narratives and jointly outputs risk score-based staging, ranked guideline-consistent treatments with evidence-based rationales, and individualized survival estimates for hepatocellular carcinoma.

## Key Innovations

### EMR Narrative Processing
- Reads routine electronic medical record narratives directly
- Extracts clinical context missed by coarse staging systems
- Addresses within-stage heterogeneity in HCC

### Knowledge-Aligned Reasoning Framework
- Optimized with step-verifiable composite reward
- Moves beyond text-level memorization of clinical guidelines
- Generates evidence-based rationales for treatment recommendations

### Multi-Center Validation
- Trained on ~30,000 HCC cases from SEER, expanded into EMR-style narratives
- Validated on 6,668 patients from 12 hospitals in China
- Outperforms GPT-5 and Gemini-2.5 Pro in treatment recommendation
- Blinded hepatobiliary specialists rate reasoning as trustworthy

### Survival Impact
- Median survival of 51 months under HCC-STAR recommendations
- vs. 29 months (BCLC) and 32 months (CNLC) under standard guidelines
- Helps physicians make more accurate decisions faster

## Methodology

1. **Data Curation**: 30,000 HCC cases from SEER expanded into EMR narratives via clinician-validated augmentation
2. **Training**: Knowledge-aligned reasoning with step-verifiable composite reward
3. **Multi-Center Validation**: 6,668 patients across 12 hospitals
4. **Clinician-Centric Evaluation**: Blinded specialist ratings on reasoning and evidence quality

## Implications

- LLM-based clinical decision support can meaningfully improve patient outcomes
- EMR narrative understanding captures context missed by staging systems
- Step-verifiable rewards enable aligned clinical reasoning
- Outperforming frontier general LLMs shows value of domain-specific training

## Pitfalls

- EMR narrative augmentation may not capture all clinical nuances
- Multi-center validation is China-specific — generalization to other populations needs testing
- LLM recommendations should supplement, not replace, clinician judgment
- Survival analysis is hypothetical — prospective validation needed

## Activation Keywords

clinical-reasoning LLM, hepatocellular carcinoma, HCC-STAR, risk stratification, treatment guidance, EMR processing, precision therapy, survival estimation, clinical decision support

## Paper Reference

arXiv:2607.08602 - "Towards Precision Therapy in Hepatocellular Carcinoma: A Clinical-Reasoning LLM" (Jul 2026)
