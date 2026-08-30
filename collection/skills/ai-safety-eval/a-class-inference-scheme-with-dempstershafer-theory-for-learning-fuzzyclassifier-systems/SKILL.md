# A Class Inference Scheme With Dempster-Shafer Theory for Learning Fuzzy-Classifier Systems

**arXiv ID:** 2506.03588
**Authors:** Hiroki Shiraishi, Hisao Ishibuchi, Masaya Nakata
**Published:** 2025-06-04T05:38:49Z
**Abstract:**
The decision-making process significantly influences the predictions of machine learning models. This is especially important in rule-based systems such as Learning Fuzzy-Classifier Systems (LFCSs) where the selection and application of rules directly determine prediction accuracy and reliability. LFCSs combine evolutionary algorithms with supervised learning to optimize fuzzy classification rules, offering enhanced interpretability and robustness. Despite these advantages, research on improving decision-making mechanisms (i.e., class inference schemes) in LFCSs remains limited. Most LFCSs use voting-based or single-winner-based inference schemes. These schemes rely on classification performance on training data and may not perform well on unseen data, risking overfitting. To address these limitations, this article introduces a novel class inference scheme for LFCSs based on the Dempster-Shafer Theory of Evidence (DS theory). The proposed scheme handles uncertainty well. By using the DS theory, the scheme calculates belief masses (i.e., measures of belief) for each specific class and the ``I don't know'' state from each fuzzy rule and infers a class from these belief masses. Unlike the conventional schemes, the proposed scheme also considers the ``I don't know'' state that reflects uncertainty, thereby improving the transparency and reliability of LFCSs. Applied to a variant of LFCS (i.e., Fuzzy-UCS), the proposed scheme demonstrates statistically significant improvements in terms of test macro F1 scores across 30 real-world datasets compared to conventional voting-based and single-winner-based fuzzy inference schemes. It forms smoother decision boundaries, provides reliable confidence measures, and enhances the robustness and generalizability of LFCSs in real-world applications. Our implementation is available at https://github.com/YNU-NakataLab/jUCS.

## Skill Description

This skill is generated from the arXiv paper: A Class Inference Scheme With Dempster-Shafer Theory for Learning Fuzzy-Classifier Systems (2506.03588).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2506.03588](http://arxiv.org/abs/2506.03588v1)
