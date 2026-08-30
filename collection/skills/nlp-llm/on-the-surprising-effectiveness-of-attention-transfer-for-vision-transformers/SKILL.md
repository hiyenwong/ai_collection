# On the Surprising Effectiveness of Attention Transfer for Vision Transformers

**arXiv ID:** 2411.09702
**Authors:** Alexander C. Li, Yuandong Tian, Beidi Chen, Deepak Pathak, Xinlei Chen
**Published:** 2024-11-14T18:59:40Z
**Abstract:**
Conventional wisdom suggests that pre-training Vision Transformers (ViT) improves downstream performance by learning useful representations. Is this actually true? We investigate this question and find that the features and representations learned during pre-training are not essential. Surprisingly, using only the attention patterns from pre-training (i.e., guiding how information flows between tokens) is sufficient for models to learn high quality features from scratch and achieve comparable downstream performance. We show this by introducing a simple method called attention transfer, where only the attention patterns from a pre-trained teacher ViT are transferred to a student, either by copying or distilling the attention maps. Since attention transfer lets the student learn its own features, ensembling it with a fine-tuned teacher also further improves accuracy on ImageNet. We systematically study various aspects of our findings on the sufficiency of attention maps, including distribution shift settings where they underperform fine-tuning. We hope our exploration provides a better understanding of what pre-training accomplishes and leads to a useful alternative to the standard practice of fine-tuning

## Skill Description

This skill is generated from the arXiv paper: On the Surprising Effectiveness of Attention Transfer for Vision Transformers (2411.09702).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2411.09702](http://arxiv.org/abs/2411.09702v1)
