# Synergizing Quality-Diversity with Descriptor-Conditioned Reinforcement Learning

**arXiv ID:** 2401.08632
**Authors:** Maxence Faldor, Félix Chalumeau, Manon Flageat, Antoine Cully
**Published:** 2023-12-10T19:53:15Z
**Abstract:**
A hallmark of intelligence is the ability to exhibit a wide range of effective behaviors. Inspired by this principle, Quality-Diversity algorithms, such as MAP-Elites, are evolutionary methods designed to generate a set of diverse and high-fitness solutions. However, as a genetic algorithm, MAP-Elites relies on random mutations, which can become inefficient in high-dimensional search spaces, thus limiting its scalability to more complex domains, such as learning to control agents directly from high-dimensional inputs. To address this limitation, advanced methods like PGA-MAP-Elites and DCG-MAP-Elites have been developed, which combine actor-critic techniques from Reinforcement Learning with MAP-Elites, significantly enhancing the performance and efficiency of Quality-Diversity algorithms in complex, high-dimensional tasks. While these methods have successfully leveraged the trained critic to guide more effective mutations, the potential of the trained actor remains underutilized in improving both the quality and diversity of the evolved population. In this work, we introduce DCRL-MAP-Elites, an extension of DCG-MAP-Elites that utilizes the descriptor-conditioned actor as a generative model to produce diverse solutions, which are then injected into the offspring batch at each generation. Additionally, we present an empirical analysis of the fitness and descriptor reproducibility of the solutions discovered by each algorithm. Finally, we present a second empirical analysis shedding light on the synergies between the different variations operators and explaining the performance improvement from PGA-MAP-Elites to DCRL-MAP-Elites.

## Skill Description

This skill is generated from the arXiv paper: Synergizing Quality-Diversity with Descriptor-Conditioned Reinforcement Learning (2401.08632).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2401.08632](http://arxiv.org/abs/2401.08632v2)
