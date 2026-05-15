# QAOA Noise Analysis with Landscape Span Compression

## LSC Metric Definition

Landscape Span Compression measures how hardware noise flattens the energy
landscape of QAOA, approaching 1 as the landscape collapses toward a barren plateau.

## Key Results (ibm_fez, Heron r2, 156 qubits)

- p=1 QAOA, up to 57,344 shots per grid point
- 3 constrained binary optimization instances (QUBO encoded)
- Noise compresses landscape span by 24-30%
- Global minimum position preserved despite noise
- IBM calibration model: Pearson r=0.959, explains ~42% of AR degradation
- Leading unexplained contributors: crosstalk, coherent errors
- Noise cost: ~0.03 approximation-ratio units consistently
- ZNE results: +7%/+9%/-4% improvement per instance, 3-5x uncertainty inflation

## Parameter Transfer Strategy

1. Optimize parameters classically (noiseless simulation)
2. Transfer to hardware (global minimum position preserved)
3. Fine-tune if needed (small adjustments due to noise shift)
