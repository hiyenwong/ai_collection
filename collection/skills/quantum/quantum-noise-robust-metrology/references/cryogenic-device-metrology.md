# Cryogenic Device Noise Metrology

Device-agnostic methodology for characterizing noise in nonlinear cryogenic quantum devices. Based on arXiv:2605.28808 (2026-05).

## Core Approach

Characterize noise properties independent of device physics using standardized metrics:
- **Added noise temperature (T_add)**: noise added beyond quantum limit
- **Noise figure (NF)**: input/output SNR ratio
- **Third-order intercept point (IP3)**: linearity for nonlinear devices
- **Gain compression (P1dB)**: 1 dB gain drop point
- **Quantum efficiency**: actual performance vs fundamental quantum limit

## Measurement Protocol

1. Define device-agnostic noise metrics
2. Use standardized measurement protocols for any nonlinear cryogenic device
3. Compare against quantum limits (SQL, Heisenberg)
4. Extract noise spectral density, added noise temperature, compression points

## Signal Processing Chain

Quantum-limited amplifier → Cryogenic HEMT (4K) → Room-temp amp → Digitization → DSP noise subtraction

Optimization: Friis formula for cascaded noise, impedance matching, cryogenic isolators.

## Nonlinear Effects to Characterize

- Gain compression and saturation
- Intermodulation distortion (IMD)
- Parametric mixing and frequency conversion
- Pump-induced dephasing and heating
- Cross-Kerr and self-Kerr nonlinearities

## Typical Targets

| Metric | Target | Quantum Limit |
|---|---|---|
| T_add | < 1 K | ~0 (freq-dependent) |
| NF | < 0.5 dB | 0 dB |
| IP3 | > -80 dBm | N/A |
| Bandwidth | > 100 MHz | N/A |

## Key Paper

"Device-Agnostic Microwave Noise Metrology for Nonlinear Cryogenic Quantum Devices" (arxiv:2605.28808, 2026-05)