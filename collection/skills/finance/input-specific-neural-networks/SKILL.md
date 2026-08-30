# Input Specific Neural Networks

**arXiv ID:** 2503.00268
**Authors:** Asghar A. Jadoon, D. Thomas Seidl, Reese E. Jones, Jan N. Fuhg
**Published:** 2025-03-01T00:57:16Z
**Abstract:**
The black-box nature of neural networks limits the ability to encode or impose specific structural relationships between inputs and outputs. While various studies have introduced architectures that ensure the network's output adheres to a particular form in relation to certain inputs, the majority of these approaches impose constraints on only a single set of inputs. This paper introduces a novel neural network architecture, termed the Input Specific Neural Network (ISNN), which extends this concept by allowing scalar-valued outputs to be subject to multiple constraints. Specifically, the ISNN can enforce convexity in some inputs, non-decreasing monotonicity combined with convexity with respect to others, and simple non-decreasing monotonicity or arbitrary relationships with additional inputs. The paper presents two distinct ISNN architectures, along with equations for the first and second derivatives of the output with respect to the inputs. These networks are broadly applicable.
  In this work, we restrict their usage to solving problems in computational mechanics. In particular, we show how they can be effectively applied to fitting data-driven constitutive models. We then embed our trained data-driven constitutive laws into a finite element solver where significant time savings can be achieved by using explicit manual differentiation using the derived equations as opposed to automatic differentiation. We also show how ISNNs can be used to learn structural relationships between inputs and outputs via a binary gating mechanism. Particularly, ISNNs are employed to model an anisotropic free energy potential to get the homogenized macroscopic response in a decoupled multiscale setting, where the network learns whether or not the potential should be modeled as polyconvex, and retains only the relevant layers while using the minimum number of inputs.

## Skill Description

This skill is generated from the arXiv paper: Input Specific Neural Networks (2503.00268).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2503.00268](http://arxiv.org/abs/2503.00268v1)
