---
name: rise-and-fall-of-g-in-agi
description: "PCA analysis of 39 AI models across 14 benchmarks revealing that PC1 (general intelligence factor) variance declines with reasoning-specialized models, suggesting intelligence factorization changes in advanced AI. Activation triggers: AGI, general intelligence, g-factor, PCA benchmarks, model evaluation, reasoning models, intelligence measurement, factor analysis."
---

# The Rise and Fall of G in AGI

> Principal Component Analysis of 39 AI models across 14 benchmarks shows the general intelligence factor (PC1) explains progressively less variance in reasoning-specialized models, indicating that advanced AI may restructure the intelligence factor space rather than simply scaling a single g-factor.

## Metadata
- **Source**: arXiv:2604.09911
- **Authors**: Jose Hernandez-Orallo
- **Published**: 2026-04-06
- **Categories**: cs.AI, q-bio.NC

## Core Methodology

### Key Innovation
Applies psychometric factor analysis (PCA) to AI model benchmark performance, mirroring the g-factor analysis used in human intelligence testing. Reveals that as AI models become more reasoning-specialized, the structure of their "intelligence" changes fundamentally — the single dominant factor fragments.

### Technical Framework

1. **Dataset**: 39 frontier AI models evaluated on 14 diverse benchmarks
2. **Analysis Pipeline**:
   - Normalize benchmark scores per model
   - PCA decomposition of the 14×39 performance matrix
   - Track PC1 variance explained across model generations
   - Compare with human psychometric g-factor patterns

3. **Key Finding — The "Rise and Fall"**:
   - **Rise phase**: Early generalist models (GPT-3.5 era) → PC1 explains ~70-80% variance, resembles human g-factor
   - **Plateau**: Mid-generation models → PC1 around 50-60%
   - **Fall phase**: Reasoning-specialized models (o1, o3, DeepSeek-R1) → PC1 drops significantly, intelligence factorizes into multiple components

4. **Implications**:
   - AI "intelligence" is not unitary — it decomposes differently than human intelligence
   - Reasoning capability may be orthogonal to other cognitive abilities in AI
   - Benchmark design must account for multi-dimensional intelligence structure

## Implementation Guide

### Prerequisites
- Python 3.x with NumPy, SciPy, scikit-learn, matplotlib
- Benchmark score matrix (models × tasks)

### Step-by-Step
1. Collect benchmark scores across models and tasks
2. Normalize scores (z-score per benchmark)
3. Apply PCA to the correlation matrix
4. Analyze eigenvalue spectrum and PC loadings
5. Track PC1 variance across model release timeline
6. Compare with human psychometric data

### Code Example
```python
import numpy as np
from sklearn.decomposition import PCA
from scipy import stats

class IntelligenceFactorAnalysis:
    """Analyze intelligence factor structure in AI model benchmarks."""
    
    def __init__(self, benchmark_matrix, model_names, benchmark_names):
        """
        benchmark_matrix: (n_models, n_benchmarks) array of scores
        """
        self.scores = benchmark_matrix
        self.models = model_names
        self.benchmarks = benchmark_names
    
    def normalize(self):
        """Z-score normalize each benchmark column."""
        self.scores_norm = stats.zscore(self.scores, axis=0, nan_policy='omit')
        return self.scores_norm
    
    def run_pca(self, n_components=None):
        """Run PCA on normalized benchmark scores."""
        if n_components is None:
            n_components = min(self.scores.shape)
        self.pca = PCA(n_components=n_components)
        self.pc_scores = self.pca.fit_transform(self.scores_norm)
        return {
            "explained_variance": self.pca.explained_variance_ratio_,
            "cumulative_variance": np.cumsum(self.pca.explained_variance_ratio_),
            "loadings": self.pca.components_.T,  # (n_benchmarks, n_pcs)
            "pc_scores": self.pc_scores
        }
    
    def g_factor_analysis(self):
        """Extract g-factor (PC1) properties."""
        results = self.run_pca()
        g_variance = results["explained_variance"][0]
        g_loadings = results["loadings"][:, 0]
        
        return {
            "g_variance_explained": float(g_variance),
            "g_loadings": dict(zip(self.benchmarks, g_loadings.tolist())),
            "is_dominant": g_variance > 0.5,
            "n_significant_factors": int(np.sum(
                results["explained_variance"] > 1.0 / len(self.benchmarks)
            ))
        }
    
    def track_factorization(self, model_release_dates):
        """Track how g-factor changes across model generations."""
        results = []
        for i in range(len(self.models)):
            subset = self.scores_norm[:i+1, :]
            pca = PCA(n_components=min(subset.shape))
            pca.fit(subset)
            results.append({
                "model": self.models[i],
                "date": model_release_dates[i],
                "g_variance": float(pca.explained_variance_ratio_[0]),
                "n_models": i + 1
            })
        return results
```

## Applications
- **AI evaluation methodology**: Multi-dimensional intelligence assessment beyond single benchmarks
- **AGI measurement**: Tracking structural changes in AI capability space
- **Benchmark design**: Understanding which tasks probe distinct cognitive dimensions
- **Cognitive science comparison**: AI vs. human intelligence factor structures
- **Model selection**: Choosing models based on multi-dimensional profiles rather than aggregate scores

## Key Findings
1. PC1 variance declines from ~80% to ~40% across model generations
2. Reasoning-specialized models (o1/o3/DeepSeek-R1) show most fragmentation
3. Mathematical reasoning and code generation form separate factors
4. Language understanding remains a strong cross-cutting factor
5. The "fall of g" suggests AGI may not have unitary intelligence

## Pitfalls
- PCA assumes linear relationships between benchmark performances
- Benchmark selection bias strongly influences factor structure
- Small model counts (N=39) limit statistical power
- Different prompting strategies can change benchmark scores substantially
- The analogy to human g-factor is imperfect — AI and human cognition differ fundamentally

## Related Skills
- llm-neuroscience-intersection-2026
- computational-neuroscience-in-llm-era
- cheesebench-rodent-neuroscience
