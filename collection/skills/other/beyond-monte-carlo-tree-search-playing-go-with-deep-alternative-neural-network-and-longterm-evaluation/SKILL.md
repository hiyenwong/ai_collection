# Beyond Monte Carlo Tree Search: Playing Go with Deep Alternative Neural Network and Long-Term Evaluation

**arXiv ID:** 1706.04052
**Authors:** Jinzhuo Wang, Wenmin Wang, Ronggang Wang, Wen Gao
**Published:** 2017-06-13T13:30:04Z
**Abstract:**
Monte Carlo tree search (MCTS) is extremely popular in computer Go which determines each action by enormous simulations in a broad and deep search tree. However, human experts select most actions by pattern analysis and careful evaluation rather than brute search of millions of future nteractions. In this paper, we propose a computer Go system that follows experts way of thinking and playing. Our system consists of two parts. The first part is a novel deep alternative neural network (DANN) used to generate candidates of next move. Compared with existing deep convolutional neural network (DCNN), DANN inserts recurrent layer after each convolutional layer and stacks them in an alternative manner. We show such setting can preserve more contexts of local features and its evolutions which are beneficial for move prediction. The second part is a long-term evaluation (LTE) module used to provide a reliable evaluation of candidates rather than a single probability from move predictor. This is consistent with human experts nature of playing since they can foresee tens of steps to give an accurate estimation of candidates. In our system, for each candidate, LTE calculates a cumulative reward after several future interactions when local variations are settled. Combining criteria from the two parts, our system determines the optimal choice of next move. For more comprehensive experiments, we introduce a new professional Go dataset (PGD), consisting of 253233 professional records. Experiments on GoGoD and PGD datasets show the DANN can substantially improve performance of move prediction over pure DCNN. When combining LTE, our system outperforms most relevant approaches and open engines based on MCTS.

## Skill Description

This skill is generated from the arXiv paper: Beyond Monte Carlo Tree Search: Playing Go with Deep Alternative Neural Network and Long-Term Evaluation (1706.04052).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:1706.04052](http://arxiv.org/abs/1706.04052v1)
