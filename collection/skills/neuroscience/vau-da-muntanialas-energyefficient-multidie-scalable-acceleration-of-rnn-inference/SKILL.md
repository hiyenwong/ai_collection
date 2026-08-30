# Vau da muntanialas: Energy-efficient multi-die scalable acceleration of RNN inference

**arXiv ID:** 2202.07462
**Authors:** Gianna Paulin, Francesco Conti, Lukas Cavigelli, Luca Benini
**Published:** 2022-02-14T09:21:16Z
**Abstract:**
Recurrent neural networks such as Long Short-Term Memories (LSTMs) learn temporal dependencies by keeping an internal state, making them ideal for time-series problems such as speech recognition. However, the output-to-input feedback creates distinctive memory bandwidth and scalability challenges in designing accelerators for RNNs. We present Muntaniala, an RNN accelerator architecture for LSTM inference with a silicon-measured energy-efficiency of 3.25$TOP/s/W$ and performance of 30.53$GOP/s$ in UMC 65 $nm$ technology. The scalable design of Muntaniala allows running large RNN models by combining multiple tiles in a systolic array. We keep all parameters stationary on every die in the array, drastically reducing the I/O communication to only loading new features and sharing partial results with other dies. For quantifying the overall system power, including I/O power, we built Vau da Muntanialas, to the best of our knowledge, the first demonstration of a systolic multi-chip-on-PCB array of RNN accelerator. Our multi-die prototype performs LSTM inference with 192 hidden states in 330$μs$ with a total system power of 9.0$mW$ at 10$MHz$ consuming 2.95$μJ$. Targeting the 8/16-bit quantization implemented in Muntaniala, we show a phoneme error rate (PER) drop of approximately 3% with respect to floating-point (FP) on a 3L-384NH-123NI LSTM network on the TIMIT dataset.

## Skill Description

This skill is generated from the arXiv paper: Vau da muntanialas: Energy-efficient multi-die scalable acceleration of RNN inference (2202.07462).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2202.07462](http://arxiv.org/abs/2202.07462v1)
