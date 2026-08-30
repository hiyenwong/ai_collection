# Closed-form Continuous-time Neural Models

**arXiv ID:** 2106.13898
**Authors:** Ramin Hasani, Mathias Lechner, Alexander Amini, Lucas Liebenwein, Aaron Ray, Max Tschaikowski, Gerald Teschl, Daniela Rus
**Published:** 2021-06-25T22:08:51Z
**Abstract:**
Continuous-time neural processes are performant sequential decision-makers that are built by differential equations (DE). However, their expressive power when they are deployed on computers is bottlenecked by numerical DE solvers. This limitation has significantly slowed down the scaling and understanding of numerous natural physical phenomena such as the dynamics of nervous systems. Ideally, we would circumvent this bottleneck by solving the given dynamical system in closed form. This is known to be intractable in general. Here, we show it is possible to closely approximate the interaction between neurons and synapses -- the building blocks of natural and artificial neural networks -- constructed by liquid time-constant networks (LTCs) efficiently in closed-form. To this end, we compute a tightly-bounded approximation of the solution of an integral appearing in LTCs' dynamics, that has had no known closed-form solution so far. This closed-form solution substantially impacts the design of continuous-time and continuous-depth neural models; for instance, since time appears explicitly in closed-form, the formulation relaxes the need for complex numerical solvers. Consequently, we obtain models that are between one and five orders of magnitude faster in training and inference compared to differential equation-based counterparts. More importantly, in contrast to ODE-based continuous networks, closed-form networks can scale remarkably well compared to other deep learning instances. Lastly, as these models are derived from liquid networks, they show remarkable performance in time series modeling, compared to advanced recurrent models.

## Skill Description

This skill is generated from the arXiv paper: Closed-form Continuous-time Neural Models (2106.13898).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2106.13898](http://arxiv.org/abs/2106.13898v2)
