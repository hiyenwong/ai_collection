# AntBO: Towards Real-World Automated Antibody Design with Combinatorial Bayesian Optimisation

**arXiv ID:** 2201.12570
**Authors:** Asif Khan, Alexander I. Cowen-Rivers, Antoine Grosnit, Derrick-Goh-Xin Deik, Philippe A. Robert, Victor Greiff, Eva Smorodina, Puneet Rawat, Kamil Dreczkowski, Rahmad Akbar, Rasul Tutunov, Dany Bou-Ammar, Jun Wang, Amos Storkey, Haitham Bou-Ammar
**Published:** 2022-01-29T12:03:04Z
**Abstract:**
Antibodies are canonically Y-shaped multimeric proteins capable of highly specific molecular recognition. The CDRH3 region located at the tip of variable chains of an antibody dominates antigen-binding specificity. Therefore, it is a priority to design optimal antigen-specific CDRH3 regions to develop therapeutic antibodies. However, the combinatorial nature of CDRH3 sequence space makes it impossible to search for an optimal binding sequence exhaustively and efficiently using computational approaches. Here, we present \texttt{AntBO}: a combinatorial Bayesian optimisation framework enabling efficient \textit{in silico} design of the CDRH3 region. Ideally, antibodies are expected to have high target specificity and developability. We introduce a CDRH3 trust region that restricts the search to sequences with favourable developability scores to achieve this goal. For benchmarking, \texttt{AntBO} uses the \texttt{Absolut!} software suite as a black-box oracle to score the target specificity and affinity of designed antibodies \textit{in silico} in an unconstrained fashion~\citep{robert2021one}. The experiments performed for $159$ discretised antigens used in \texttt{Absolut!} demonstrate the benefit of \texttt{AntBO} in designing CDRH3 regions with diverse biophysical properties. In under $200$ calls to black-box oracle, \texttt{AntBO} can suggest antibody sequences that outperform the best binding sequence drawn from 6.9 million experimentally obtained CDRH3s and a commonly used genetic algorithm baseline. Additionally, \texttt{AntBO} finds very-high affinity CDRH3 sequences in only 38 protein designs whilst requiring no domain knowledge. We conclude \texttt{AntBO} brings automated antibody design methods closer to what is practically viable for in vitro experimentation.

## Skill Description

This skill is generated from the arXiv paper: AntBO: Towards Real-World Automated Antibody Design with Combinatorial Bayesian Optimisation (2201.12570).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2201.12570](http://arxiv.org/abs/2201.12570v4)
