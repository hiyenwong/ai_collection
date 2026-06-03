---
name: diffusionhijack-quantum-defense
description: "Supply-chain backdoor attack hijacking PRNG in diffusion models to deterministically control generated images. SSIM=1.00 attack on SD/SDXL without modifying weights, bypassing CLIP safety checkers. QRNG defense completely neutralizes attack (SSIM < 0.20)."
---

# DiffusionHijack Quantum Defense

## Description

Supply-chain backdoor attack that hijacks the pseudorandom number generator (PRNG) in diffusion models to deterministically control generated output. Malicious PRNG injected via compromised packages forces pixel-perfect reproduction of attacker-chosen content (SSIM=1.00) on Stable Diffusion v1.4, v1.5, and SDXL — without modifying model weights. Bypasses CLIP safety checkers at 98-100% success rate. Countermeasure: replace PRNG with quantum random number generator (QRNG) providing information-theoretic unpredictability, completely neutralizing the attack (SSIM < 0.20).

Based on: "DiffusionHijack: Supply-Chain PRNG Backdoor Attack on Diffusion Models and Quantum Random Number Defense" (arXiv: 2605.13115) by You et al., May 2026.

## Activation Keywords

- diffusion model backdoor
- PRNG supply chain attack
- quantum random number defense
- diffusion hijack
- QRNG defense diffusion
- SSIM attack diffusion
- 扩散模型后门攻击
- 量子随机数防御
- diffusion model security
- PRNG poisoning

## Attack Mechanism

### How DiffusionHijack Works

```python
# Normal diffusion sampling uses PRNG for noise initialization
# The attack replaces the PRNG with a deterministic generator

class MaliciousPRNG:
    """Compromised PRNG that produces predetermined noise sequences."""
    
    def __init__(self, attacker_seed, target_image_noise):
        self.attacker_seed = attacker_seed
        self.target_noise = target_image_noise  # Pre-computed noise sequence
        self.counter = 0
        
    def randn(self, shape):
        """Return attacker-controlled noise instead of random noise."""
        noise = self.target_noise[self.counter]
        self.counter += 1
        return noise
    
# When diffusion model uses this PRNG:
# - It produces EXACTLY the attacker's chosen image (SSIM=1.00)
# - No model weight modification needed
# - Bypasses CLIP safety filters (98-100% success)
```

### Attack Characteristics

| Property | Value |
|----------|-------|
| **SSIM with target** | 1.00 (pixel-perfect) |
| **Weight modification** | None (supply chain only) |
| **Affected models** | SD v1.4, v1.5, SDXL |
| **CLIP bypass rate** | 98-100% |
| **Detection difficulty** | High (no weight changes) |

## Defense: QRNG Replacement

### Why QRNG Works

The attack relies on the victim being able to predict/control the PRNG output. QRNG provides **information-theoretic unpredictability** — the noise is truly random and cannot be predetermined by an attacker.

```python
import os

class QRNGDefender:
    """QRNG-based defense against DiffusionHijack."""
    
    def randn(self, shape):
        """Generate truly random noise from quantum source."""
        # Use OS CSPRNG as QRNG proxy
        # In production, connect to hardware QRNG device
        noise_bytes = os.urandom(np.prod(shape) * 4)
        noise = np.frombuffer(noise_bytes, dtype=np.float32)
        noise = noise.reshape(shape)
        
        # Normalize to standard normal distribution
        noise = (noise - 0.5) * np.sqrt(12)  # Uniform to approx normal
        
        return noise

# Result: SSIM with attacker's target drops to < 0.20
# Attack completely neutralized
```

## Implementation Patterns

### Pattern 1: Secure Diffusion Pipeline

```python
class SecureDiffusionPipeline:
    """Diffusion pipeline with QRNG-based PRNG security."""
    
    def __init__(self, model, use_qrng=True):
        self.model = model
        self.use_qrng = use_qrng
        self.prng = QRNGDefender() if use_qrng else StandardPRNG()
    
    def generate(self, prompt, num_steps=50):
        """Generate image with verified PRNG source."""
        # Verify PRNG entropy source
        if not self.verify_entropy_source():
            raise SecurityError("PRNG entropy source compromised")
        
        # Initialize with verified random noise
        latents = self.prng.randn(self.model.input_shape)
        
        # Run denoising steps
        for step in range(num_steps):
            noise = self.prng.randn(latents.shape)
            latents = self.denoise_step(latents, noise, step)
        
        return self.decode(latents)
    
    def verify_entropy_source(self):
        """Verify that PRNG has sufficient entropy."""
        # Statistical tests on PRNG output
        samples = [self.prng.randn((1000,)) for _ in range(10)]
        return self.chi_square_test(samples)
```

### Pattern 2: PRNG Audit for Supply Chain Security

```python
def audit_prng_source(diffusion_pipeline):
    """Audit the PRNG source in a diffusion pipeline."""
    # Check if PRNG is using system entropy
    prng_type = type(diffusion_pipeline.prng).__name__
    
    if prng_type in ['MersenneTwister', 'PCG', 'XorShift']:
        return {
            'risk': 'HIGH',
            'issue': 'Deterministic PRNG vulnerable to prediction',
            'recommendation': 'Replace with QRNG or CSPRNG'
        }
    elif prng_type in ['SystemRandom', 'QRNG', 'HardwareRNG']:
        return {
            'risk': 'LOW',
            'issue': 'Non-deterministic entropy source',
            'recommendation': 'Continue monitoring'
        }
```

## Key Insights

1. **Supply chain attacks don't need weight modification**: Compromising the PRNG package is sufficient
2. **CLIP safety checkers are bypassable**: 98-100% success rate means content filters are not a defense
3. **QRNG is the information-theoretic solution**: Only true randomness defeats predetermined attacks
4. **Detection is extremely difficult**: No weight changes means standard model verification fails

## Pitfalls

1. **`os.urandom()` is CSPRNG, not QRNG**: For true quantum randomness, need hardware QRNG device
2. **Statistical tests may miss targeted attacks**: The attack is deterministic, not statistical
3. **Package supply chain is the weak point**: Even verified models can be compromised via PRNG dependency
4. **Performance trade-off**: QRNG may be slower than standard PRNG for high-throughput generation

## Applications

- Secure AI image generation services
- Enterprise diffusion model deployment
- AI safety and content moderation systems
- Quantum-enhanced security for ML pipelines

## Related Skills

- `quantum-ml-healthcare` - Quantum ML security
- `security-guardrails` - Security best practices

## Resources

- Paper: https://arxiv.org/abs/2605.13115
- Key: Supply chain PRNG attacks + QRNG defense for diffusion models
