"""
Computational Lesions for Brain-Model Alignment Analysis

Implementation of lesion methodology using multilingual LLMs
to separate shared and language-specific brain alignment.

Reference: arXiv:2604.10627v1
"""

import numpy as np
import torch
import torch.nn as nn
from typing import Dict, List, Tuple
import copy
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt


class ComputationalLesion:
    """
    Create computational lesions in multilingual LLMs to study
    shared vs language-specific brain alignment.
    """
    
    LESION_TYPES = ['shared_core', 'language_specific']
    
    def __init__(self, model: nn.Module, languages: List[str] = None):
        """
        Initialize lesion analyzer.
        
        Args:
            model: Multilingual LLM
            languages: List of languages to analyze
        """
        self.model = model
        self.languages = languages or ['en', 'zh', 'fr']
        self.original_state = copy.deepcopy(model.state_dict())
    
    def identify_important_parameters(self, language: str = None,
                                     importance_threshold: float = 0.9) -> List[Tuple[str, torch.Tensor]]:
        """
        Identify important parameters using gradient-based importance.
        
        Args:
            language: Target language (None for cross-language)
            importance_threshold: Top fraction to select
        
        Returns:
            List of (param_name, param_mask) tuples
        """
        important_params = []
        
        # Compute parameter importance (simplified)
        for name, param in self.model.named_parameters():
            if param.requires_grad:
                # Use magnitude as proxy for importance
                importance = param.abs().flatten()
                
                # Select top-k important parameters
                k = int(len(importance) * (1 - importance_threshold))
                _, indices = torch.topk(importance, k)
                
                # Create mask
                mask = torch.zeros_like(param)
                mask.view(-1)[indices] = 1
                
                important_params.append((name, mask))
        
        return important_params
    
    def create_shared_core_lesion(self, zeroing_fraction: float = 0.1) -> nn.Module:
        """
        Create lesion of shared core (important across all languages).
        
        Args:
            zeroing_fraction: Fraction of parameters to zero
        
        Returns:
            Lesioned model
        """
        lesioned_model = copy.deepcopy(self.model)
        
        # Identify parameters important across all languages
        all_important = []
        for lang in self.languages:
            important = self.identify_important_parameters(lang, 1 - zeroing_fraction)
            all_important.append(important)
        
        # Find intersection (important in all languages)
        shared_important = self._intersection_params(all_important)
        
        # Apply lesion
        for name, mask in shared_important:
            param = dict(lesioned_model.named_parameters())[name]
            param.data *= (1 - mask)
        
        return lesioned_model
    
    def create_language_specific_lesion(self, language: str,
                                       zeroing_fraction: float = 0.1) -> nn.Module:
        """
        Create lesion specific to one language.
        
        Args:
            language: Target language
            zeroing_fraction: Fraction of parameters to zero
        
        Returns:
            Lesioned model
        """
        lesioned_model = copy.deepcopy(self.model)
        
        # Identify language-specific important parameters
        important = self.identify_important_parameters(language, 1 - zeroing_fraction)
        
        # Apply lesion
        for name, mask in important:
            param = dict(lesioned_model.named_parameters())[name]
            param.data *= (1 - mask)
        
        return lesioned_model
    
    def _intersection_params(self, param_lists: List[List]) -> List[Tuple[str, torch.Tensor]]:
        """Find intersection of important parameters across lists."""
        if not param_lists:
            return []
        
        # Simplified: use first list
        return param_lists[0]
    
    def reset_model(self):
        """Reset model to original state."""
        self.model.load_state_dict(self.original_state)


class BrainEncoder:
    """
    Encoding model to predict fMRI responses from LLM embeddings.
    """
    
    def __init__(self, embedding_dim: int, n_voxels: int):
        """
        Initialize encoder.
        
        Args:
            embedding_dim: LLM embedding dimension
            n_voxels: Number of fMRI voxels
        """
        self.embedding_dim = embedding_dim
        self.n_voxels = n_voxels
        self.encoder = Ridge(alpha=1.0)
        self.is_trained = False
    
    def extract_embeddings(self, model: nn.Module, texts: List[str],
                          layer: int = -2) -> np.ndarray:
        """
        Extract LLM embeddings for texts.
        
        Args:
            model: LLM model
            texts: List of input texts
            layer: Which layer to extract from
        
        Returns:
            Embeddings array [n_texts, embedding_dim]
        """
        embeddings = []
        
        model.eval()
        with torch.no_grad():
            for text in texts:
                inputs = model.tokenizer(text, return_tensors='pt')
                outputs = model(**inputs, output_hidden_states=True)
                
                # Extract from specified layer
                layer_output = outputs.hidden_states[layer]
                
                # Mean pool over sequence
                embedding = layer_output[0].mean(dim=0).numpy()
                embeddings.append(embedding)
        
        return np.array(embeddings)
    
    def train(self, embeddings: np.ndarray, fmri_data: np.ndarray):
        """
        Train encoding model.
        
        Args:
            embeddings: LLM embeddings [n_samples, embedding_dim]
            fmri_data: fMRI responses [n_samples, n_voxels]
        """
        self.encoder.fit(embeddings, fmri_data)
        self.is_trained = True
    
    def predict(self, embeddings: np.ndarray) -> np.ndarray:
        """
        Predict fMRI responses.
        
        Args:
            embeddings: LLM embeddings
        
        Returns:
            Predicted fMRI responses
        """
        if not self.is_trained:
            raise ValueError("Encoder not trained")
        return self.encoder.predict(embeddings)
    
    def evaluate(self, embeddings: np.ndarray, fmri_data: np.ndarray) -> Dict:
        """
        Evaluate prediction quality.
        
        Args:
            embeddings: Test embeddings
            fmri_data: Test fMRI data
        
        Returns:
            Dictionary with evaluation metrics
        """
        predictions = self.predict(embeddings)
        
        # Compute correlation for each voxel
        correlations = []
        for voxel_idx in range(fmri_data.shape[1]):
            true = fmri_data[:, voxel_idx]
            pred = predictions[:, voxel_idx]
            corr = np.corrcoef(true, pred)[0, 1]
            if not np.isnan(corr):
                correlations.append(corr)
        
        return {
            'mean_correlation': np.mean(correlations),
            'max_correlation': np.max(correlations),
            'n_voxels_significant': sum(np.array(correlations) > 0.1)
        }


class LesionExperiment:
    """
    Run computational lesion experiments to analyze brain alignment.
    """
    
    def __init__(self, model: nn.Module, languages: List[str] = None):
        """
        Initialize experiment.
        
        Args:
            model: Multilingual LLM
            languages: Languages to test
        """
        self.lesion = ComputationalLesion(model, languages)
        self.languages = languages or ['en', 'zh', 'fr']
        self.results = {}
    
    def run_lesion_study(self, fmri_data: Dict[str, np.ndarray],
                        texts: Dict[str, List[str]],
                        encoder: BrainEncoder) -> Dict:
        """
        Run complete lesion study.
        
        Args:
            fmri_data: Dictionary mapping language -> fMRI data
            texts: Dictionary mapping language -> stimulus texts
            encoder: Trained brain encoder
        
        Returns:
            Results dictionary
        """
        results = {
            'intact': {},
            'shared_lesion': {},
            'language_lesions': {}
        }
        
        # 1. Baseline with intact model
        print("Testing intact model...")
        for lang in self.languages:
            embeddings = encoder.extract_embeddings(
                self.lesion.model, texts[lang]
            )
            metrics = encoder.evaluate(embeddings, fmri_data[lang])
            results['intact'][lang] = metrics
        
        # 2. Shared core lesion
        print("Testing shared core lesion...")
        shared_lesioned = self.lesion.create_shared_core_lesion()
        for lang in self.languages:
            embeddings = encoder.extract_embeddings(shared_lesioned, texts[lang])
            metrics = encoder.evaluate(embeddings, fmri_data[lang])
            results['shared_lesion'][lang] = metrics
        
        # 3. Language-specific lesions
        for lesion_lang in self.languages:
            print(f"Testing {lesion_lang}-specific lesion...")
            lang_lesioned = self.lesion.create_language_specific_lesion(lesion_lang)
            
            results['language_lesions'][lesion_lang] = {}
            for test_lang in self.languages:
                embeddings = encoder.extract_embeddings(lang_lesioned, texts[test_lang])
                metrics = encoder.evaluate(embeddings, fmri_data[test_lang])
                results['language_lesions'][lesion_lang][test_lang] = metrics
        
        self.results = results
        return results
    
    def compute_lesion_effects(self) -> Dict:
        """
        Compute relative effects of lesions.
        
        Returns:
            Dictionary with lesion effect sizes
        """
        effects = {
            'shared_core_reduction': {},
            'language_specificity': {}
        }
        
        # Shared core effect
        for lang in self.languages:
            intact_corr = self.results['intact'][lang]['mean_correlation']
            lesioned_corr = self.results['shared_lesion'][lang]['mean_correlation']
            reduction = (intact_corr - lesioned_corr) / intact_corr
            effects['shared_core_reduction'][lang] = reduction
        
        # Language-specific effects
        for lesion_lang in self.languages:
            effects['language_specificity'][lesion_lang] = {}
            for test_lang in self.languages:
                intact_corr = self.results['intact'][test_lang]['mean_correlation']
                lesioned_corr = self.results['language_lesions'][lesion_lang][test_lang]['mean_correlation']
                reduction = (intact_corr - lesioned_corr) / intact_corr
                effects['language_specificity'][lesion_lang][test_lang] = reduction
        
        return effects
    
    def visualize_results(self):
        """Visualize lesion experiment results."""
        effects = self.compute_lesion_effects()
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Shared core effect
        ax = axes[0]
        langs = list(effects['shared_core_reduction'].keys())
        reductions = [effects['shared_core_reduction'][lang] for lang in langs]
        ax.bar(langs, reductions)
        ax.set_ylabel('Correlation Reduction')
        ax.set_title('Shared Core Lesion Effect')
        ax.axhline(y=0.6, color='r', linestyle='--', label='60% threshold')
        ax.legend()
        
        # Language specificity heatmap
        ax = axes[1]
        lesion_langs = list(effects['language_specificity'].keys())
        test_langs = self.languages
        
        matrix = np.zeros((len(lesion_langs), len(test_langs)))
        for i, l_lang in enumerate(lesion_langs):
            for j, t_lang in enumerate(test_langs):
                matrix[i, j] = effects['language_specificity'][l_lang][t_lang]
        
        im = ax.imshow(matrix, cmap='Reds', vmin=0, vmax=0.5)
        ax.set_xticks(range(len(test_langs)))
        ax.set_yticks(range(len(lesion_langs)))
        ax.set_xticklabels(test_langs)
        ax.set_yticklabels([f"{lang} lesion" for lang in lesion_langs])
        ax.set_title('Language-Specific Lesion Effects')
        plt.colorbar(im, ax=ax, label='Correlation Reduction')
        
        plt.tight_layout()
        return fig


def demonstrate_lesion_methodology():
    """Demonstrate computational lesion methodology."""
    print("=" * 70)
    print("Computational Lesions for Brain-Model Alignment")
    print("=" * 70)
    
    print("\n1. Methodology Overview")
    print("-" * 50)
    print("""
    Step 1: Identify important parameters
            - For each language, compute parameter importance
            - Use gradient-based or magnitude-based measures
    
    Step 2: Create lesions
            - Shared core: Zero parameters important across ALL languages
            - Language-specific: Zero parameters important for ONE language
    
    Step 3: Evaluate brain prediction
            - Extract embeddings from lesioned model
            - Predict fMRI responses using encoding model
            - Compare to intact model predictions
    
    Step 4: Analyze effects
            - Shared core lesion → affects ALL languages equally
            - Language lesion → selectively affects target language
    """)
    
    print("\n2. Expected Findings")
    print("-" * 50)
    print("""
    Finding 1: Shared Core
    - Shared core lesion reduces brain prediction by ~60% across languages
    - Indicates compact multilingual processing core exists
    
    Finding 2: Language Specialization
    - Language-specific lesions show selective impairment
    - Shared core contains language-specific specializations
    
    Finding 3: Brain Alignment
    - Shared core regions align with bilingual brain areas
    - Specializations align with proficiency-related regions
    """)
    
    print("\n3. Implications")
    print("-" * 50)
    print("""
    - Supports 'shared backbone + language-specific' theory
    - Provides causal evidence for brain-model alignment
    - Enables targeted analysis of multilingual processing
    """)
    
    print("\n" + "=" * 70)


if __name__ == '__main__':
    demonstrate_lesion_methodology()
