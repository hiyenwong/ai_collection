# Quantum Medical Image Encoding & Compression

## arXiv:2505.06471 - Quantum medical image encoding and compression using Fourier-based methods

**Authors**: Taehee Ko, Inho Lee, Hyeong Won Yu
**Published**: 2025-05-09

### Problem
- Existing quantum image encoding uses ~2x gates compared to pixel count
- Even modest images are computationally demanding to simulate

### Solution
- Fourier-based encoding reduces gates by ≥4x vs pixel count
- Validated on 1024×1024 medical images from BABA robotic thyroidectomy surgery
- Two compression techniques further reduce gates and preprocessing time

### Key Results
- Negligible loss of image quality after compression
- Valuable option for large-scale medical imaging on quantum hardware

### When to Use
- Medical imaging with high resolution (≥1024×1024)
- CT, MRI, PET, surgical imaging requiring quantum encoding
- Any scenario where gate count is a limiting factor

## arXiv:2004.02036 - Quantum Medical Imaging Algorithms

**Authors**: Bobak Toussi Kiani, Agnes Villanyi, Seth Lloyd
**Published**: 2020-04-04

### Core Contribution
- Quantum algorithms for medical image reconstruction (CT, MRI, PET)
- Exponential speedup over classical counterparts when data is input as quantum state
- Outputs stored in quantum states; individual pixels not efficiently accessible classically
- Post-processing via quantum methods to extract information

### Applicability
- Image reconstruction from raw scanner data
- Requires quantum input data (not classical-to-quantum conversion bottleneck)
