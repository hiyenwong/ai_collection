# Even Faster SNN Simulation with Lazy+Event-driven Plasticity and Shared Atomics

**arXiv ID:** 2107.04092
**Authors:** Dennis Bautembach, Iason Oikonomidis, Antonis Argyros
**Published:** 2021-07-08T20:13:54Z
**Abstract:**
We present two novel optimizations that accelerate clock-based spiking neural network (SNN) simulators. The first one targets spike timing dependent plasticity (STDP). It combines lazy- with event-driven plasticity and efficiently facilitates the computation of pre- and post-synaptic spikes using bitfields and integer intrinsics. It offers higher bandwidth than event-driven plasticity alone and achieves a 1.5x-2x speedup over our closest competitor. The second optimization targets spike delivery. We partition our graph representation in a way that bounds the number of neurons that need be updated at any given time which allows us to perform said update in shared memory instead of global memory. This is 2x-2.5x faster than our closest competitor. Both optimizations represent the final evolutionary stages of years of iteration on STDP and spike delivery inside "Spice" (/spaIk/), our state of the art SNN simulator. The proposed optimizations are not exclusive to our graph representation or pipeline but are applicable to a multitude of simulator designs. We evaluate our performance on three well-established models and compare ourselves against three other state of the art simulators.

## Skill Description

This skill is generated from the arXiv paper: Even Faster SNN Simulation with Lazy+Event-driven Plasticity and Shared Atomics (2107.04092).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2107.04092](http://arxiv.org/abs/2107.04092v2)
