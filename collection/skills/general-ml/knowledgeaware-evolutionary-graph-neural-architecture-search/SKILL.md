# Knowledge-aware Evolutionary Graph Neural Architecture Search

**arXiv ID:** 2411.17339
**Authors:** Chao Wang, Jiaxuan Zhao, Lingling Li, Licheng Jiao, Fang Liu, Xu Liu, Shuyuan Yang
**Published:** 2024-11-26T11:32:45Z
**Abstract:**
Graph neural architecture search (GNAS) can customize high-performance graph neural network architectures for specific graph tasks or datasets. However, existing GNAS methods begin searching for architectures from a zero-knowledge state, ignoring the prior knowledge that may improve the search efficiency. The available knowledge base (e.g. NAS-Bench-Graph) contains many rich architectures and their multiple performance metrics, such as the accuracy (#Acc) and number of parameters (#Params). This study proposes exploiting such prior knowledge to accelerate the multi-objective evolutionary search on a new graph dataset, named knowledge-aware evolutionary GNAS (KEGNAS). KEGNAS employs the knowledge base to train a knowledge model and a deep multi-output Gaussian process (DMOGP) in one go, which generates and evaluates transfer architectures in only a few GPU seconds. The knowledge model first establishes a dataset-to-architecture mapping, which can quickly generate candidate transfer architectures for a new dataset. Subsequently, the DMOGP with architecture and dataset encodings is designed to predict multiple performance metrics for candidate transfer architectures on the new dataset. According to the predicted metrics, non-dominated candidate transfer architectures are selected to warm-start the multi-objective evolutionary algorithm for optimizing the #Acc and #Params on a new dataset. Empirical studies on NAS-Bench-Graph and five real-world datasets show that KEGNAS swiftly generates top-performance architectures, achieving 4.27% higher accuracy than advanced evolutionary baselines and 11.54% higher accuracy than advanced differentiable baselines. In addition, ablation studies demonstrate that the use of prior knowledge significantly improves the search performance.

## Skill Description

This skill is generated from the arXiv paper: Knowledge-aware Evolutionary Graph Neural Architecture Search (2411.17339).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2411.17339](http://arxiv.org/abs/2411.17339v1)
