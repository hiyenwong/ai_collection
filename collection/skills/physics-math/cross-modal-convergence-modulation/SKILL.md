---
name: cross-modal-convergence-modulation
category: ai_collection
description: "Modulating Cross-Modal Convergence with Single-Stimulus, Intra-Modal Dispersion - neural network methodology for modulating representational convergence across architectures and modalities. Reveals how single-stimulus dispersion within modalities predicts cross-modal alignment. Based on arXiv:2604.21836."
source_paper: "arXiv:2604.21836v1"
paper_title: "Modulating Cross-Modal Convergence with Single-Stimulus, Intra-Modal Dispersion"
authors: "Eghbal A. Hosseini, Brian Cheung, Evelina Fedorenko, et al."
date: "2026-04-23"
keywords: ["cross-modal convergence", "representation alignment", "intra-modal dispersion", "brain alignment", "neural networks", "multimodal"]
trigger: ["cross-modal convergence", "representation alignment", "intra-modal dispersion", "brain alignment", "multimodal representation", "model-brain alignment"]
---

# Cross-Modal Convergence Modulation

## Source Paper
- **Title**: Modulating Cross-Modal Convergence with Single-Stimulus, Intra-Modal Dispersion
- **arXiv**: 2604.21836v1
- **Date**: April 23, 2026
- **Categories**: q-bio.NC, cs.AI
- **PDF**: https://arxiv.org/pdf/2604.21836v1.pdf

## Overview

Neural networks exhibit remarkable representational convergence across diverse architectures, training objectives, and even data modalities. This convergence is predictive of alignment with brain representations. This paper demonstrates that **intra-modal dispersion** — the variability of representations within a single modality across different models — can be used to **modulate and predict cross-modal convergence**.

## Core Concepts

### Representational Convergence
- Neural networks trained on different tasks/modalities converge to similar representations
- Convergence predicts brain alignment: models that align with each other tend to align with brain data
- Suggests learning underlying structure in similar ways

### Cross-Modal Alignment
- Alignment between vision and language models
- Alignment between artificial and biological neural networks
- Measured via representational similarity analysis (RSA)

### Intra-Modal Dispersion
- **Definition**: Variability of a stimulus's representation across models within the same modality
- **High dispersion**: Different models represent the same stimulus very differently
- **Low dispersion**: Models agree on stimulus representation
- **Key insight**: Dispersion is predictive of cross-modal alignment

### Single-Stimulus Modulation
- Focus on individual stimuli rather than aggregate measures
- Stimuli with high intra-modal dispersion show different cross-modal convergence patterns
- Enables targeted analysis of representation structure

## Methodology

### Intra-Modal Dispersion Calculation
```python
import numpy as np
from scipy.spatial.distance import cosine
from scipy.stats import spearmanr

class IntraModalDispersionAnalyzer:
    """Analyze intra-modal dispersion and its relation to cross-modal convergence."""
    
    def __init__(self, modality='vision'):
        self.modality = modality
        self.model_representations = {}  # {model_name: {stimulus_id: representation}}
        
    def add_model_representations(self, model_name, stimuli_ids, representations):
        """Add representations from a model.
        
        Args:
            model_name: Name of the model
            stimuli_ids: List of stimulus identifiers
            representations: Array of shape (n_stimuli, n_features)
        """
        self.model_representations[model_name] = {
            sid: rep for sid, rep in zip(stimuli_ids, representations)
        }
    
    def compute_intra_modal_dispersion(self, stimulus_id, distance_metric='cosine'):
        """Compute dispersion for a single stimulus across models.
        
        Args:
            stimulus_id: Identifier for the stimulus
            distance_metric: Distance metric ('cosine', 'euclidean', 'correlation')
            
        Returns:
            dispersion: Float, measure of representation variability
            pairwise_dists: Array of pairwise distances between model representations
        """
        # Collect representations from all models
        reps = []
        models = list(self.model_representations.keys())
        
        for model_name in models:
            if stimulus_id in self.model_representations[model_name]:
                reps.append(self.model_representations[model_name][stimulus_id])
        
        if len(reps) < 2:
            return None, None
        
        reps = np.array(reps)
        n_models = len(reps)
        
        # Compute pairwise distances
        pairwise_dists = []
        for i in range(n_models):
            for j in range(i+1, n_models):
                if distance_metric == 'cosine':
                    dist = cosine(reps[i], reps[j])
                elif distance_metric == 'euclidean':
                    dist = np.linalg.norm(reps[i] - reps[j])
                elif distance_metric == 'correlation':
                    dist = 1 - np.corrcoef(reps[i], reps[j])[0, 1]
                pairwise_dists.append(dist)
        
        # Dispersion = mean pairwise distance
        dispersion = np.mean(pairwise_dists)
        
        return dispersion, np.array(pairwise_dists)
    
    def compute_all_dispersions(self, stimuli_ids, distance_metric='cosine'):
        """Compute dispersion for all stimuli.
        
        Returns:
            dispersions: Dict mapping stimulus_id to dispersion value
        """
        dispersions = {}
        for sid in stimuli_ids:
            disp, _ = self.compute_intra_modal_dispersion(sid, distance_metric)
            if disp is not None:
                dispersions[sid] = disp
        
        return dispersions
    
    def categorize_by_dispersion(self, stimuli_ids, n_bins=3):
        """Categorize stimuli into dispersion bins.
        
        Args:
            stimuli_ids: List of stimulus IDs
            n_bins: Number of dispersion categories
            
        Returns:
            categories: Dict mapping stimulus_id to category (0=low, n_bins-1=high)
        """
        dispersions = self.compute_all_dispersions(stimuli_ids)
        
        if not dispersions:
            return {}
        
        values = np.array(list(dispersions.values()))
        percentiles = np.linspace(0, 100, n_bins + 1)
        
        thresholds = np.percentile(values, percentiles[1:-1])
        
        categories = {}
        for sid, disp in dispersions.items():
            cat = np.searchsorted(thresholds, disp)
            categories[sid] = cat
        
        return categories


class CrossModalConvergenceModulator:
    """Modulate cross-modal convergence using intra-modal dispersion."""
    
    def __init__(self):
        self.modality_a_reps = {}
        self.modality_b_reps = {}
        
    def add_modality_representations(self, modality, models_data):
        """Add representations for a modality.
        
        Args:
            modality: 'A' or 'B'
            models_data: Dict {model_name: {stimulus_id: representation}}
        """
        if modality == 'A':
            self.modality_a_reps = models_data
        elif modality == 'B':
            self.modality_b_reps = models_data
    
    def compute_cross_modal_alignment(self, stimulus_id, model_a, model_b):
        """Compute cross-modal alignment for a stimulus.
        
        Args:
            stimulus_id: Stimulus identifier
            model_a: Model name in modality A
            model_b: Model name in modality B
            
        Returns:
            alignment: Similarity between cross-modal representations
        """
        if stimulus_id not in self.modality_a_reps.get(model_a, {}):
            return None
        if stimulus_id not in self.modality_b_reps.get(model_b, {}):
            return None
        
        rep_a = self.modality_a_reps[model_a][stimulus_id]
        rep_b = self.modality_b_reps[model_b][stimulus_id]
        
        # Cosine similarity
        alignment = np.dot(rep_a, rep_b) / (np.linalg.norm(rep_a) * np.linalg.norm(rep_b))
        
        return alignment
    
    def analyze_dispersion_alignment_correlation(self, stimuli_ids):
        """Analyze correlation between dispersion and cross-modal alignment.
        
        Returns:
            results: Dict with correlation statistics
        """
        # Compute dispersion for modality A
        analyzer = IntraModalDispersionAnalyzer(modality='A')
        for model_name, reps in self.modality_a_reps.items():
            analyzer.add_model_representations(model_name, list(reps.keys()), 
                                               list(reps.values()))
        
        dispersions = analyzer.compute_all_dispersions(stimuli_ids)
        
        # Compute cross-modal alignments
        model_names_a = list(self.modality_a_reps.keys())
        model_names_b = list(self.modality_b_reps.keys())
        
        alignments = []
        disp_vals = []
        
        for sid in stimuli_ids:
            if sid not in dispersions:
                continue
            
            # Average alignment across model pairs
            align_vals = []
            for model_a in model_names_a:
                for model_b in model_names_b:
                    align = self.compute_cross_modal_alignment(sid, model_a, model_b)
                    if align is not None:
                        align_vals.append(align)
            
            if align_vals:
                alignments.append(np.mean(align_vals))
                disp_vals.append(dispersions[sid])
        
        # Compute correlation
        if len(alignments) > 2:
            corr, pvalue = spearmanr(disp_vals, alignments)
        else:
            corr, pvalue = 0, 1
        
        return {
            'correlation': corr,
            'pvalue': pvalue,
            'n_stimuli': len(alignments),
            'dispersions': disp_vals,
            'alignments': alignments
        }
    
    def modulated_rsa(self, stimuli_ids, target_brain_data, n_dispersion_bins=3):
        """Perform RSA modulated by intra-modal dispersion.
        
        Args:
            stimuli_ids: List of stimulus IDs
            target_brain_data: Brain RDM (n_stimuli x n_stimuli)
            n_dispersion_bins: Number of dispersion categories
            
        Returns:
            results: RSA results stratified by dispersion
        """
        from scipy.spatial.distance import pdist, squareform
        
        # Compute dispersion categories
        analyzer = IntraModalDispersionAnalyzer()
        for model_name, reps in self.modality_a_reps.items():
            analyzer.add_model_representations(model_name, list(reps.keys()), 
                                               list(reps.values()))
        
        categories = analyzer.categorize_by_dispersion(stimuli_ids, n_dispersion_bins)
        
        results = {}
        
        for bin_idx in range(n_dispersion_bins):
            # Select stimuli in this bin
            bin_stimuli = [sid for sid, cat in categories.items() if cat == bin_idx]
            
            if len(bin_stimuli) < 3:
                continue
            
            # Compute model RDM for these stimuli
            model_rdm = self._compute_model_rdm(bin_stimuli)
            
            # Extract brain RDM for these stimuli
            idxs = [stimuli_ids.index(sid) for sid in bin_stimuli]
            brain_rdm_subset = target_brain_data[np.ix_(idxs, idxs)]
            
            # Compute RSA
            rdm_vec_model = squareform(model_rdm, checks=False)
            rdm_vec_brain = squareform(brain_rdm_subset, checks=False)
            
            corr, pval = spearmanr(rdm_vec_model, rdm_vec_brain)
            
            results[f'bin_{bin_idx}'] = {
                'n_stimuli': len(bin_stimuli),
                'spearman_r': corr,
                'pvalue': pval
            }
        
        return results
    
    def _compute_model_rdm(self, stimuli_ids):
        """Compute model representational dissimilarity matrix."""
        # Average representations across models
        avg_reps = {}
        for sid in stimuli_ids:
            reps = []
            for model_name, model_reps in self.modality_a_reps.items():
                if sid in model_reps:
                    reps.append(model_reps[sid])
            if reps:
                avg_reps[sid] = np.mean(reps, axis=0)
        
        # Compute RDM
        n = len(stimuli_ids)
        rdm = np.zeros((n, n))
        
        for i, sid_i in enumerate(stimuli_ids):
            for j, sid_j in enumerate(stimuli_ids):
                if sid_i in avg_reps and sid_j in avg_reps:
                    rdm[i, j] = 1 - np.corrcoef(avg_reps[sid_i], avg_reps[sid_j])[0, 1]
        
        return rdm
```

## Key Findings

### 1. Dispersion Predicts Convergence
- Stimuli with **high intra-modal dispersion** show **weaker cross-modal convergence**
- Stimuli with **low intra-modal dispersion** show **stronger cross-modal convergence**
- Effect is consistent across multiple model pairs and modalities

### 2. Modulation Effect
- Conditioning on intra-modal dispersion **modulates cross-modal alignment scores**
- Enables identification of stimuli with robust vs. fragile cross-modal representations
- Provides insight into representation structure

### 3. Brain Alignment Prediction
- Cross-modal convergence is **predictive of brain alignment**
- Models that converge across modalities better align with neural recordings
- Dispersion-informed convergence improves brain alignment prediction

## Applications

### 1. Model Selection for Brain Studies
```python
# Select models with highest dispersion-modulated brain alignment
def select_best_model(models, brain_data, stimuli):
    modulator = CrossModalConvergenceModulator()
    
    # Load model representations
    for model_name in models:
        reps = load_model_representations(model_name, stimuli)
        modulator.add_modality_representations('A', {model_name: reps})
    
    # Compute alignment stratified by dispersion
    results = modulator.modulated_rsa(stimuli, brain_data)
    
    # Return model with best low-dispersion alignment
    best_model = select_best(results)
    return best_model
```

### 2. Stimulus Selection
- Identify stimuli with robust cross-modal representations
- Exclude high-dispersion stimuli for reliable brain alignment
- Create curated stimulus sets for neuroscience experiments

### 3. Multimodal Learning
- Use dispersion as training signal
- Regularize models to reduce intra-modal dispersion
- Improve cross-modal transfer learning

## Related Skills
- [[cross-region-alignment-brain-models]]
- [[brain-alignment-crap-analysis]]
- [[functional-connectome-fingerprint]]
- [[computational-lesions-multilingual-language-models]]

## References
- Hosseini et al. (2026). Modulating Cross-Modal Convergence with Single-Stimulus, Intra-Modal Dispersion. arXiv:2604.21836v1.
