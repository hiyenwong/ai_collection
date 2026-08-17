### Lapis: Laplacian Spiking Attention via First-Spike Timing and Membrane Leakage
- [[lapis-spiking-attention]] - Lapis: multiplication-free spiking attention using first-spike timing and membrane leakage dynamics. (arXiv: 2608.11865)
  - Uses L1 distance between first-spike latency vectors under time-to-first-spike coding
  - Laplacian kernel matches leaky integrate-and-fire membrane dynamics naturally
  - Eliminates all multiplications; uses only subtraction, absolute value, accumulation
  - Achieves 96.56% CIFAR-10 accuracy (within 0.53 points of dot-product baseline)
  - 14.5× lower arithmetic energy compared to dense dot-product attention
  - **Activation**: lapis, spiking attention, first-spike timing, membrane leakage, energy-efficient SNN, Laplacian kernel attention, multiplication-free attention