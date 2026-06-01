---
name: fnirs-3d-monte-carlo-simulator
description: "High-fidelity 3D fNIRS simulator methodology using mesh-based Monte Carlo simulations for generating physiologically realistic synthetic functional near-infrared spectroscopy data. Combines anatomically accurate sensitivity profiles with parameterized hemodynamic response models, systemic physiology, and noise artifacts for in silico experimentation, denoising algorithm validation, and data augmentation. Use when: fNIRS data simulation, synthetic neuroimaging data generation, hemodynamic response modeling, Monte Carlo light transport in tissue, motion artifact simulation, brain imaging pipeline validation."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.30552"
  published: "2026-05-28"
  authors: "Condell Eastmond, Niels Bracher, Xavier Intes, Stefan T. Radev"
  tags: [fNIRS, Monte-Carlo, simulator, hemodynamic-response, synthetic-data, brain-imaging]
---

# fNIRS 3D Monte Carlo Simulator

## Core Concept

Generate physiologically realistic synthetic fNIRS data using mesh-based Monte Carlo (MMC) simulations of light transport in tissue, combined with parameterized models of hemodynamic responses, systemic physiology, and non-systematic artifacts. Addresses the critical bottleneck of limited annotated fNIRS datasets that hinders AI-based analysis pipeline development.

## Key Components

### 1. Mesh-Based Monte Carlo Light Transport
- Uses anatomically accurate 3D head mesh models
- Simulates photon propagation through tissue layers (scalp, skull, CSF, gray/white matter)
- Computes spatial sensitivity profiles (photon measurement density functions)
- Captures wavelength-dependent absorption and scattering

### 2. Hemodynamic Response Model
- Parameterized models of HbO/HbR concentration changes
- Task-evoked hemodynamic responses with canonical HRF shapes
- Spatial variability across cortical regions
- Temporal dynamics: onset delay, peak time, undershoot

### 3. Systemic Physiology
- Cardiac pulsation (~1 Hz)
- Respiration (~0.2-0.3 Hz)
- Mayer waves (~0.1 Hz)
- Low-frequency drift

### 4. Non-Systematic Artifacts
- Motion artifacts (sudden spikes, baseline shifts)
- Instrument noise (photon counting statistics)
- Physiological noise coupling

## Workflow

### Step 1: Define Anatomy
- Load or generate 3D head mesh (MRI-derived or template)
- Assign optical properties per tissue type (μa, μs', g, n)
- Place source-detector geometry on scalp surface

### Step 2: Run MMC Simulation
```python
# Pseudocode for mesh-based Monte Carlo
def run_mmc(mesh, sources, detectors, wavelengths):
    sensitivity = {}
    for src in sources:
        for det in detectors:
            for wl in wavelengths:
                # Launch N photons, track paths
                photon_paths = simulate_photons(mesh, src, det, wl, N=1e7)
                # Accumulate sensitivity in each voxel
                sensitivity[(src,det,wl)] = accumulate_paths(photon_paths)
    return sensitivity
```

### Step 3: Generate Synthetic Signals
```python
def generate_fnirs_signal(sensitivity, hrf_params, physiology_params, artifacts):
    # Task-evoked hemodynamic response
    hrf = canonical_hrf(**hrf_params)
    delta_hbo = convolve(hrf, task_design) * sensitivity * extinction_coeff_HbO
    delta_hbr = convolve(hrf, task_design) * sensitivity * extinction_coeff_HbR
    
    # Add systemic physiology
    signal += cardiac_noise(freq=1.0, amplitude=0.01)
    signal += respiration_noise(freq=0.25, amplitude=0.005)
    signal += mayer_waves(freq=0.1, amplitude=0.008)
    signal += low_frequency_drift(cutoff=0.01)
    
    # Add motion artifacts (probabilistic)
    if motion_probability > threshold:
        signal += motion_spike(amplitude, duration)
    
    # Add instrument noise
    signal += gaussian_noise(snr=snr_db)
    
    return delta_hbo, delta_hbr
```

### Step 4: Validate
- Compare power spectral density with real fNIRS data
- Validate HRF shape against experimental finger-tapping data
- Check motion artifact statistics against empirical distributions

## Parameters for Realistic Simulation

| Parameter | Typical Range | Notes |
|-----------|--------------|-------|
| Source-Detector Distance | 20-40 mm | Determines penetration depth |
| HRF Peak Time | 4-8 s | Task-dependent variability |
| HRF Amplitude (ΔHbO) | 1-10 μM | Region and task dependent |
| Cardiac Frequency | 0.8-1.2 Hz | Subject-dependent |
| SNR | 10-30 dB | Depends on coupling quality |
| Motion Artifact Rate | 0.01-0.1 Hz | Higher in mobile/child studies |

## Applications

1. **Denoising Algorithm Validation**: Ground-truth known signals to test removal of motion artifacts, systemic physiology
2. **Data Augmentation**: Generate unlimited labeled datasets for training ML models
3. **Optimal Channel Design**: Test source-detector layouts before experiments
4. **Statistical Power Analysis**: Estimate sample sizes for planned studies
5. **In Silico Experimentation**: Test analysis pipelines without human subjects

## Pitfalls

- **Mesh Quality Matters**: Poor mesh resolution leads to inaccurate sensitivity profiles
- **Optical Property Uncertainty**: Tissue optical properties vary across subjects and wavelengths
- **HRF Variability**: Canonical HRF may not capture all response shapes (especially in patient populations)
- **Computational Cost**: MMC with 10^7 photons per channel pair can take hours
- **Validation Gap**: Always validate against real experimental data before trusting simulations

## Activation Keywords
- fNIRS simulator, fnirs simulation, synthetic fnirs data
- Monte Carlo light transport tissue, mesh-based Monte Carlo
- hemodynamic response simulation, HbO HbR simulation
- near-infrared spectroscopy simulation, brain imaging simulator
- fNIRS denoising validation, fNIRS data augmentation
- fnirs 3d simulator, 近红外光谱模拟
