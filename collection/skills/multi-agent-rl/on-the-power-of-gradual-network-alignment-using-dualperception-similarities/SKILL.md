# On the Power of Gradual Network Alignment Using Dual-Perception Similarities

**arXiv ID:** 2201.10945
**Authors:** Jin-Duk Park, Cong Tran, Won-Yong Shin, Xin Cao
**Published:** 2022-01-26T14:01:32Z
**Abstract:**
Network alignment (NA) is the task of finding the correspondence of nodes between two networks based on the network structure and node attributes. Our study is motivated by the fact that, since most of existing NA methods have attempted to discover all node pairs at once, they do not harness information enriched through interim discovery of node correspondences to more accurately find the next correspondences during the node matching. To tackle this challenge, we propose Grad-Align, a new NA method that gradually discovers node pairs by making full use of node pairs exhibiting strong consistency, which are easy to be discovered in the early stage of gradual matching. Specifically, Grad-Align first generates node embeddings of the two networks based on graph neural networks along with our layer-wise reconstruction loss, a loss built upon capturing the first-order and higher-order neighborhood structures. Then, nodes are gradually aligned by computing dual-perception similarity measures including the multi-layer embedding similarity as well as the Tversky similarity, an asymmetric set similarity using the Tversky index applicable to networks with different scales. Additionally, we incorporate an edge augmentation module into Grad-Align to reinforce the structural consistency. Through comprehensive experiments using real-world and synthetic datasets, we empirically demonstrate that Grad-Align consistently outperforms state-of-the-art NA methods.

## Skill Description

This skill is generated from the arXiv paper: On the Power of Gradual Network Alignment Using Dual-Perception Similarities (2201.10945).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2201.10945](http://arxiv.org/abs/2201.10945v3)
