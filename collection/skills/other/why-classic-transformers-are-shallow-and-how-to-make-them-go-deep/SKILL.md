# Why "classic" Transformers are shallow and how to make them go deep

**arXiv ID:** 2312.06182
**Authors:** Yueyao Yu, Yin Zhang
**Published:** 2023-12-11T07:49:16Z
**Abstract:**
Since its introduction in 2017, Transformer has emerged as the leading neural network architecture, catalyzing revolutionary advancements in many AI disciplines. The key innovation in Transformer is a Self-Attention (SA) mechanism designed to capture contextual information. However, extending the original Transformer design to models of greater depth has proven exceedingly challenging, if not impossible. Even though various modifications have been proposed in order to stack more layers of SA mechanism into deeper models, a full understanding of this depth problem remains lacking. In this paper, we conduct a comprehensive investigation, both theoretically and empirically, to substantiate the claim that the depth problem is caused by \emph{token similarity escalation}; that is, tokens grow increasingly alike after repeated applications of the SA mechanism. Our analysis reveals that, driven by the invariant leading eigenspace and large spectral gaps of attention matrices, token similarity provably escalates at a linear rate. Based on the gained insight, we propose a new strategy of surgically removing excessive similarity in contrast to the existing approach of diminishing the SA mechanism explicitly or implicitly (such as in pre-norm transformers). Preliminary experimental results confirm the effectiveness of the proposed strategy in small-scale post-norm Transformer models.

## Skill Description

This skill is generated from the arXiv paper: Why "classic" Transformers are shallow and how to make them go deep (2312.06182).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2312.06182](http://arxiv.org/abs/2312.06182v2)
