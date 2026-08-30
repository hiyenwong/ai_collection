# Socrates Loss: Unifying Confidence Calibration and Classification by Leveraging the Unknown

**arXiv ID:** 2604.12245
**Authors:** Sandra Gómez-Gálvez, Tobias Olenyi, Gillian Dobbie, Katerina Taškova
**Published:** 2026-04-14T03:43:15Z
**Abstract:**
Deep neural networks, despite their high accuracy, often exhibit poor confidence calibration, limiting their reliability in high-stakes applications. Current ad-hoc confidence calibration methods attempt to fix this during training but face a fundamental trade-off: two-phase training methods achieve strong classification performance at the cost of training instability and poorer confidence calibration, while single-loss methods are stable but underperform in classification. This paper addresses and mitigates this stability-performance trade-off. We propose Socrates Loss, a novel, unified loss function that explicitly leverages uncertainty by incorporating an auxiliary unknown class, whose predictions directly influence the loss function and a dynamic uncertainty penalty. This unified objective allows the model to be optimized for both classification and confidence calibration simultaneously, without the instability of complex, scheduled losses. We provide theoretical guarantees that our method regularizes the model to prevent miscalibration and overfitting. Across four benchmark datasets and multiple architectures, our comprehensive experiments demonstrate that Socrates Loss consistently improves training stability while achieving more favorable accuracy-calibration trade-off, often converging faster than existing methods.

## Skill Description

This skill is generated from the arXiv paper: Socrates Loss: Unifying Confidence Calibration and Classification by Leveraging the Unknown (2604.12245).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2604.12245](http://arxiv.org/abs/2604.12245v1)
