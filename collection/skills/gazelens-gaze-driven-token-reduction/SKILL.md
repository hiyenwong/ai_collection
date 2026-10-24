---
name: gazelens-gaze-driven-token-reduction
description: "Use when egocentric-video VLMs on smart glasses must fit a compute budget. GazeLens: cheap frame selection (HOG transitions, sharpness) plus gaze-focused and complementary Gaussian-pooling tokens blended by a question-conditioned gate - 2 tokens per frame."
category: ai_collection
metadata:
  arxiv_id: "2610.28502"
---

# GazeLens: Gaze-Driven Adaptive Token Reduction for Egocentric Video QA

Source: arXiv:2610.28502 (Pham, Nguyen, Nguyen, Le, Oct 2026). Small vision-language models on smart glasses must preserve useful evidence within a tight compute budget. Redundant frames consume the visual budget while aggressive spatial compression discards relevant details. Gaze identifies the wearer's focus, but the question may need **surrounding scene** evidence.

## Pipeline

1. **Frame selection before visual encoding** (cheap signals only): HOG transitions + image sharpness pick informative frames — no encoder forward pass wasted on redundant frames.
2. **Per selected frame, two summaries via Gaussian pooling**:
   - a **gaze-focused** summary (pooling centered on gaze),
   - a **complementary** summary (the periphery/context around gaze).
3. **Question-conditioned lightweight gate** blends the two into a **primary token** — relevance of focus vs context depends on the question.
4. A **global scene token** is kept; total cost is **two tokens per frame** (primary + global).

## Results (StreamGaze)

- Higher macro and micro accuracy than evaluated full-grid and token-reduction baselines.
- **Lower input-forward FLOPs** than shared-backbone token-reduction baselines.

## Reuse pattern

- Gaze (or any free attention signal: mouse, saliency, touch) should **split, not select**: keep a focused token *and* a complementary token, and let a downstream gate decide per query — binary keep/drop loses question-dependent context.
- Do frame selection with classical cheap features (HOG, sharpness, optical-flow proxies) before invoking any neural encoder.
- Budget rule: one gated primary token + one global scene token per frame is a strong operating point for streaming video VLMs.
- Applies to wearable/streaming perception, robotics cameras with pointing signals, UI video agents with cursor traces.

Related: query-guided token pruning (Web-GUI agents), video token compression, streaming egocentric perception, saliency-guided sparse attention.
