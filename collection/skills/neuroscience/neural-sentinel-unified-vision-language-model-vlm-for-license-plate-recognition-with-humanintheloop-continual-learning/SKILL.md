# Neural Sentinel: Unified Vision Language Model (VLM) for License Plate Recognition with Human-in-the-Loop Continual Learning

**arXiv ID:** 2602.07051
**Authors:** Karthik Sivakoti
**Published:** 2026-02-04T16:04:15Z
**Abstract:**
Traditional Automatic License Plate Recognition (ALPR) systems employ multi-stage pipelines consisting of object detection networks followed by separate Optical Character Recognition (OCR) modules, introducing compounding errors, increased latency, and architectural complexity. This research presents Neural Sentinel, a novel unified approach that leverages Vision Language Models (VLMs) to perform license plate recognition, state classification, and vehicle attribute extraction through a single forward pass. Our primary contribution lies in demonstrating that a fine-tuned PaliGemma 3B model, adapted via Low-Rank Adaptation (LoRA), can simultaneously answer multiple visual questions about vehicle images, achieving 92.3% plate recognition accuracy, which is a 14.1% improvement over EasyOCR and 9.9% improvement over PaddleOCR baselines. We introduce a Human-in-the-Loop (HITL) continual learning framework that incorporates user corrections while preventing catastrophic forgetting through experience replay, maintaining a 70:30 ratio of original training data to correction samples. The system achieves a mean inference latency of 152ms with an Expected Calibration Error (ECE) of 0.048, indicating well calibrated confidence estimates. Additionally, the VLM first architecture enables zero-shot generalization to auxiliary tasks including vehicle color detection (89%), seatbelt detection (82%), and occupancy counting (78%) without task specific training. Through extensive experimentation on real world toll plaza imagery, we demonstrate that unified vision language approaches represent a paradigm shift in ALPR systems, offering superior accuracy, reduced architectural complexity, and emergent multi-task capabilities that traditional pipeline approaches cannot achieve.

## Skill Description

This skill is generated from the arXiv paper: Neural Sentinel: Unified Vision Language Model (VLM) for License Plate Recognition with Human-in-the-Loop Continual Learning (2602.07051).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2602.07051](http://arxiv.org/abs/2602.07051v1)
