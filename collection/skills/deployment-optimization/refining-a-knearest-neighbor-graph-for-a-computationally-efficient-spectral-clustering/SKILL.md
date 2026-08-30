# Refining a $k$-nearest neighbor graph for a computationally efficient spectral clustering

**arXiv ID:** 2302.11296
**Authors:** Mashaan Alshammari, John Stavrakakis, Masahiro Takatsuka
**Published:** 2023-02-22T11:31:32Z
**Abstract:**
Spectral clustering became a popular choice for data clustering for its ability of uncovering clusters of different shapes. However, it is not always preferable over other clustering methods due to its computational demands. One of the effective ways to bypass these computational demands is to perform spectral clustering on a subset of points (data representatives) then generalize the clustering outcome, this is known as approximate spectral clustering (ASC). ASC uses sampling or quantization to select data representatives. This makes it vulnerable to 1) performance inconsistency (since these methods have a random step either in initialization or training), 2) local statistics loss (because the pairwise similarities are extracted from data representatives instead of data points). We proposed a refined version of $k$-nearest neighbor graph, in which we keep data points and aggressively reduce number of edges for computational efficiency. Local statistics were exploited to keep the edges that do not violate the intra-cluster distances and nullify all other edges in the $k$-nearest neighbor graph. We also introduced an optional step to automatically select the number of clusters $C$. The proposed method was tested on synthetic and real datasets. Compared to ASC methods, the proposed method delivered a consistent performance despite significant reduction of edges.

## Skill Description

This skill is generated from the arXiv paper: Refining a $k$-nearest neighbor graph for a computationally efficient spectral clustering (2302.11296).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2302.11296](http://arxiv.org/abs/2302.11296v1)
