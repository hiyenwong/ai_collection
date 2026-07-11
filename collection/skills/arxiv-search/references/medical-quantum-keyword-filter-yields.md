# Medical + Quantum Keyword Filter Yield Analysis

## 2026-06-03 Comparison

| Filter Type | Terms | Feed | Total Items | Matched | Yield Rate |
|-------------|-------|------|-------------|---------|------------|
| Broad medical | quantum + medical/healthcare/clinical/diagnosis/treatment/patient | quant-ph+q-bio.QM+q-bio.TO+cs.AI+cs.LG | 812 | 30 | ~3.7% |
| Specific medical | quantum + (medical, healthcare, clinical, diagnosis, treatment, patient, disease, therapy, drug, cancer, biomarker, imaging, hospital, protein folding, retinal, eeg, ecg, fmri, mri, pharmac, neurological, neurodegenerative, alzheimer, stroke, brain, neural, neuron, cell) | quant-ph+q-bio.QM+q-bio.TO+cs.AI+cs.LG | 812 | 13 | ~1.6% |
| Narrow feed | quantum + medical terms | quant-ph+q-bio.QM+q-bio.TO | ~207 | 10 | ~4.8% |

## Key Insight

The **specific keyword filter** (27+ medical terms) yields ~1.6% on the broad feed — significantly lower than the broad filter's ~3.7%. This is expected: more specific terms = fewer matches. 

**Practical guidance for cron jobs**:
- Use **broad filter** (6 terms: medical, healthcare, clinical, diagnosis, treatment, patient) for maximum discovery coverage — catches papers like 2606.03517 (QNN clinical data imputation) and 2606.02104 (protein folding)
- Use **specific filter** when you want high-signal papers but accept lower recall — found 2508.16784 (QRNN amplitude encoding) which the broad filter also caught
- The narrow feed (`quant-ph+q-bio.QM+q-bio.TO`) has the highest precision (~4.8%) but lowest absolute yield (~10 papers from 207 total)

## Top Papers by Filter

### Specific Filter Only (not in broad)
- 2508.16784: Improving QRNNs with Amplitude Encoding (score=4) — QRNN for time series, validated on real-world datasets

### Both Filters
- 2606.03517: Scalable On-Hardware Training of QNNs for Clinical Data Imputation (score=7)
- 2606.02104: Penalty-free quantum optimization for lattice protein folding (score=5)
