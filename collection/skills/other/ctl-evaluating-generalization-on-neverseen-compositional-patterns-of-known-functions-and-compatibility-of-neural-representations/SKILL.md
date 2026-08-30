# CTL++: Evaluating Generalization on Never-Seen Compositional Patterns of Known Functions, and Compatibility of Neural Representations

**arXiv ID:** 2210.06350
**Authors:** Róbert Csordás, Kazuki Irie, Jürgen Schmidhuber
**Published:** 2022-10-12T16:01:57Z
**Abstract:**
Well-designed diagnostic tasks have played a key role in studying the failure of neural nets (NNs) to generalize systematically. Famous examples include SCAN and Compositional Table Lookup (CTL). Here we introduce CTL++, a new diagnostic dataset based on compositions of unary symbolic functions. While the original CTL is used to test length generalization or productivity, CTL++ is designed to test systematicity of NNs, that is, their capability to generalize to unseen compositions of known functions. CTL++ splits functions into groups and tests performance on group elements composed in a way not seen during training. We show that recent CTL-solving Transformer variants fail on CTL++. The simplicity of the task design allows for fine-grained control of task difficulty, as well as many insightful analyses. For example, we measure how much overlap between groups is needed by tested NNs for learning to compose. We also visualize how learned symbol representations in outputs of functions from different groups are compatible in case of success but not in case of failure. These results provide insights into failure cases reported on more complex compositions in the natural language domain. Our code is public.

## Skill Description

This skill is generated from the arXiv paper: CTL++: Evaluating Generalization on Never-Seen Compositional Patterns of Known Functions, and Compatibility of Neural Representations (2210.06350).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2210.06350](http://arxiv.org/abs/2210.06350v1)
