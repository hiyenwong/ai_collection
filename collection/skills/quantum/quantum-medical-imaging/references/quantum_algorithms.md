# Quantum Algorithms for Medical Imaging

## Quantum Fourier Transform (QFT)

**Purpose:** Polynomial speedup for Fourier-based operations

**Medical Application:** 
- MRI reconstruction uses Fourier transforms
- Classical: O(N log N) with FFT
- Quantum: O(log N) with QFT

**Limitations:**
- Requires fault-tolerant quantum computers
- NISQ devices insufficient for medical-grade reconstruction

## Variational Quantum Eigensolver (VQE)

**Purpose:** Find ground state of quantum systems

**Medical Application:**
- Optimize reconstruction parameters
- Energy minimization for image denoising
- Can run on NISQ devices

## Quantum Approximate Optimization Algorithm (QAOA)

**Purpose:** Combinatorial optimization

**Medical Application:**
- Image segmentation optimization
- Feature selection in radiomics
- Treatment planning optimization

## Quantum Annealing

**Purpose:** Energy landscape optimization

**Medical Application:**
- CT reconstruction optimization
- MRI pulse sequence optimization
- Dose optimization in radiotherapy

## NV-Center Magnetometry

**Purpose:** Precision magnetic field sensing

**Medical Application:**
- Enhanced MRI sensitivity
- Cellular-level imaging
- Neural activity detection
- Lower radiation dose imaging

**Advantages:**
- Works at room temperature
- High spatial resolution (~nm)
- Can operate in biological environments