---
name: medical-ai-diagnosis
description: >
  Patterns for building AI-based medical diagnosis systems with clinical explainability.
  Covers foundation models for medical imaging, clinical reasoning trace generation,
  multi-modal patient data integration, and explainable AI for healthcare.
  Use when building medical AI diagnosis tools, clinical decision support systems,
  explainable medical ML models, or medical foundation models.
  Trigger: medical AI, clinical diagnosis AI, explainable healthcare, medical foundation model,
  DeepMedix, clinical reasoning, medical AI benchmarking, subgroup fairness, cancer detection evaluation,
  医疗AI诊断, 可解释医疗AI, 医学AI基准测试.
---

# Medical AI Diagnosis Patterns

Patterns for building AI-based medical diagnosis systems with clinical explainability.

## When to Use

- Building AI systems for medical diagnosis (X-ray, MRI, CT, pathology)
- Designing clinical decision support systems
- Implementing explainable AI for healthcare applications
- Developing medical foundation models

## Core Pattern: Explainable Medical Diagnosis

### Architecture

```
Input (Medical Data) → Feature Extraction → Clinical Reasoning → Diagnosis + Explanation
```

### Key Components

1. **Multi-modal Input Processing**
   - Text: EHR, clinical notes, lab results
   - Images: X-ray, CT, MRI, pathology slides
   - Structured: Vital signs, demographics

2. **Clinical Reasoning Engine**
   - Step-by-step diagnostic reasoning
   - Differential diagnosis generation
   - Evidence-based guideline reference

3. **Explainability Layer**
   - Visual attention maps for imaging
   - Clinical reasoning traces (why this diagnosis?)
   - Confidence scores with uncertainty quantification
   - Alternative diagnoses with reasoning

## Implementation Pattern (from DeepMedix-R1)

```python
# Explainable Medical Diagnosis Pipeline

class MedicalDiagnosisModel:
    def diagnose(self, patient_data):
        # 1. Multi-modal encoding
        features = self.encode(patient_data)
        
        # 2. Clinical reasoning
        reasoning_steps = self.reason(features)
        
        # 3. Diagnosis prediction
        diagnosis = self.predict(features)
        
        # 4. Generate explanation
        explanation = self.explain(reasoning_steps, diagnosis)
        
        return {
            "diagnosis": diagnosis,
            "confidence": self.confidence(diagnosis),
            "reasoning": reasoning_steps,
            "explanation": explanation,
            "alternatives": self.differential_diagnosis(features)
        }
```

## Key Design Principles

1. **Clinical Trust Through Explainability**
   - Black-box models fail clinical adoption
   - Every diagnosis must have traceable reasoning
   - Show evidence, not just predictions

2. **Multi-modal Integration**
   - Combine imaging + text + structured data
   - Cross-modal attention mechanisms
   - Handle missing modalities gracefully

3. **Uncertainty Quantification**
   - Medical decisions require confidence estimates
   - Bayesian methods or ensemble approaches
   - Flag low-confidence predictions for human review

4. **Guideline Alignment**
   - Reference clinical practice guidelines
   - Generate ICD codes with reasoning
   - Align with medical ontology (SNOMED, LOINC)

## Today's Research Findings

- **DeepMedix-R1** (arxiv:2509.03906): Foundation model for CXR with clinical reasoning
- **Skin Lesion AI** (arxiv:2601.00964): Automated classification via deep learning
- **MRI Spine CAD** (arxiv:2503.20316): Spinal pathology detection system
- **Oncology AI** (arxiv:2501.15489): Cancer detection and personalized therapy

## Validation Requirements

- Internal validation: Cross-validation on training data
- External validation: Different hospital/demographic
- Clinical validation: Comparison with expert radiologists
- Prospective validation: Real-world deployment study

## Benchmarking & Fairness Evaluation Pattern

### Multi-Dimensional Benchmark Framework (BenchX, arXiv: 2606.24883)

When evaluating medical AI models, assess across four dimensions simultaneously:
1. **Tumor/lesion size**: micro (<5mm), small, medium, large
2. **Anatomical location**: per-organ and per-region
3. **Patient subgroups**: age, gender, ethnicity, comorbidity
4. **Imaging protocol**: scanner manufacturer, slice thickness, contrast phase

**Key finding**: Models optimized for average accuracy often underperform >15% in rare/underrepresented subgroups.
**Mitigation**: LLM-assisted subgroup extraction from clinical text + DICOM headers for stratified evaluation.

### Fairness Metrics
- Per-subgroup sensitivity/specificity
- Performance gap: max(subgroup) - min(subgroup)
- Fairness index: worst-performing subgroup / overall average

## References

- See references/research-notes.md for detailed paper analysis
- Related: quantum-ml-healthcare skill for quantum approaches
