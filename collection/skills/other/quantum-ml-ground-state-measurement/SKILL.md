---
name: quantum-ml-ground-state-measurement
description: "基于SIC-POVM测量空间的量子基态变分学习方法。使用自回归神经网络（GRU）编码SIC-POVM测量结果的概率分布，通过梯度下降最小化能量并强制物理性约束（正性层级条件）。适用于量子多体基态求解、变分量子态制备。"
---

# Learning quantum ground states in the space of measurement outcomes

- **arXiv**: 2605.28931
- **Date**: 2026-05-29
- **Topic**: Quantum Machine Learning + Statistics

## Abstract

基于SIC-POVM测量空间的量子基态变分学习方法。使用自回归神经网络（GRU）编码对称信息完备正算子值测量（SIC-POVM）结果的概率分布，通过梯度下降最小化能量并强制物理性约束。在横场Ising模型和海森堡模型上验证（系统大小达L=128）。

## Core Methodology

SIC-POVM测量空间表示：将量子态表示为SIC-POVM测量结果的概率分布

自回归神经网络编码：基于GRU的网络参数化概率分布

物理性约束强制：层级正性条件确保测量分布对应物理量子态

基准验证：一维横场Ising模型和海森堡模型，系统大小达L=128

## Activation

quantum ground state, SIC-POVM, variational learning, autoregressive neural network, GRU, measurement space

## References

- Paper: https://arxiv.org/abs/2605.28931
