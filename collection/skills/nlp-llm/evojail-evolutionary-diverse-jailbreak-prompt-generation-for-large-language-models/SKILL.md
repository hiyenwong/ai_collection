# EvoJail: Evolutionary Diverse Jailbreak Prompt Generation for Large Language Models

**arXiv ID:** 2605.02921
**Authors:** Rui Tang, Kaiyu Xu, Pengsen Cheng, Hao Ren, Haizhou Wang, Shuyu Jiang
**Published:** 2026-04-22T02:59:49Z
**Abstract:**
As LLMs continue to shape real-world applications, automated jailbreak generation becomes essential to reveal safety weaknesses and guide model improvement. Existing automatic jailbreak generation methods have not yet fully considered two important aspects: adaptability to evolving safety-finetuned models, which affects their effectiveness on newer model versions, and diversity in generated prompts, which can cause narrow or repetitive attack patterns. To address these issues, we propose EvoJail, an instruction-fusion-driven evolutionary jailbreak generation framework that formalizes jailbreak prompt generation as a multi-objective black-box optimization problem and leverages the principles of evolutionary algorithms to search for jailbreak prompts that can adapt across different model versions and exhibit diverse attack patterns. Specifically, EvoJail integrates jailbreak prompt generation into an iterative evolutionary loop, where at each iteration candidate prompts are evaluated directly against the target model and then selected and varied based on the target model's responses, enabling the generation process to continuously adapt to model updates. To enhance diversity, EvoJail introduces field-aware instruction fusion to construct diverse starting points and incorporates diversity-aware objectives into the evolutionary fitness function, guiding the search toward prompts with richer semantic variation, while further designing multi-level LLM-based mutation operators that modify prompt structures at different granularities to promote structural diversity throughout the evolutionary process. Results demonstrate that EvoJail has stronger adaptability and can achieve over $93\%$ attack success rate and more than $5.6\%$ improvement in diversity metrics over state-of-the-art methods.

## Skill Description

This skill is generated from the arXiv paper: EvoJail: Evolutionary Diverse Jailbreak Prompt Generation for Large Language Models (2605.02921).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2605.02921](http://arxiv.org/abs/2605.02921v1)
