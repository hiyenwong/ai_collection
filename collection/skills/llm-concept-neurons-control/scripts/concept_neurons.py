"""
Psychological Concept Neurons Analysis in LLMs

Implementation of concept neuron identification and control
using Big Five personality framework.

Reference: arXiv:2604.11802v1
"""

import numpy as np
import torch
import torch.nn as nn
from typing import Dict, List, Tuple
from sklearn.linear_model import LogisticRegression
from collections import defaultdict


class BigFiveDimensions:
    """Big Five personality dimensions with descriptors."""
    
    DIMENSIONS = {
        'openness': {
            'high': ['curious', 'creative', 'intellectual', 'imaginative', 'artistic'],
            'low': ['conventional', 'practical', 'down-to-earth', 'uncreative']
        },
        'conscientiousness': {
            'high': ['organized', 'responsible', 'disciplined', 'careful', 'diligent'],
            'low': ['spontaneous', 'careless', 'easy-going', 'disorganized']
        },
        'extraversion': {
            'high': ['outgoing', 'energetic', 'talkative', 'assertive', 'sociable'],
            'low': ['reserved', 'quiet', 'introverted', 'shy', 'solitary']
        },
        'agreeableness': {
            'high': ['cooperative', 'trusting', 'empathetic', 'kind', 'helpful'],
            'low': ['competitive', 'skeptical', 'challenging', 'critical']
        },
        'neuroticism': {
            'high': ['anxious', 'insecure', 'emotional', 'nervous', 'sensitive'],
            'low': ['confident', 'calm', 'stable', 'secure', 'relaxed']
        }
    }
    
    @classmethod
    def get_prompt(cls, trait: str, level: str) -> str:
        """Generate persona prompt for trait level."""
        descriptors = cls.DIMENSIONS[trait][level]
        return f"You are a person who is {', '.join(descriptors)}. Describe yourself:"
    
    @classmethod
    def get_all_prompts(cls) -> List[Tuple[str, str, str]]:
        """Get all prompts with labels."""
        prompts = []
        for trait, levels in cls.DIMENSIONS.items():
            for level in ['high', 'low']:
                prompt = cls.get_prompt(trait, level)
                prompts.append((trait, level, prompt))
        return prompts


class ConceptProber:
    """Probe for psychological concepts in LLM hidden states."""
    
    def __init__(self, model: nn.Module, n_layers: int):
        """
        Initialize prober.
        
        Args:
            model: LLM model
            n_layers: Number of layers
        """
        self.model = model
        self.n_layers = n_layers
        self.probes = {}
        self.accuracies = {}
    
    def extract_hidden_states(self, texts: List[str], 
                              layer: int) -> torch.Tensor:
        """
        Extract hidden states at specific layer.
        
        Args:
            texts: List of input texts
            layer: Layer index
        
        Returns:
            Hidden states tensor [n_texts, hidden_dim]
        """
        hidden_states = []
        
        self.model.eval()
        with torch.no_grad():
            for text in texts:
                # Tokenize
                inputs = self.model.tokenizer(text, return_tensors='pt')
                
                # Forward pass
                outputs = self.model(**inputs, output_hidden_states=True)
                
                # Extract layer hidden state (last token)
                h = outputs.hidden_states[layer][0, -1, :]
                hidden_states.append(h)
        
        return torch.stack(hidden_states)
    
    def train_probe(self, texts: List[str], labels: List[int], 
                    layer: int) -> Tuple[LogisticRegression, float]:
        """
        Train linear probe for concept classification.
        
        Args:
            texts: Training texts
            labels: Binary labels (0/1)
            layer: Layer to probe
        
        Returns:
            Trained probe and accuracy
        """
        # Extract hidden states
        hidden_states = self.extract_hidden_states(texts, layer)
        X = hidden_states.numpy()
        y = np.array(labels)
        
        # Train probe
        probe = LogisticRegression(max_iter=1000, C=1.0)
        probe.fit(X, y)
        
        # Evaluate
        accuracy = probe.score(X, y)
        
        return probe, accuracy
    
    def analyze_trait(self, trait: str, n_samples: int = 100):
        """
        Analyze decodability of personality trait across layers.
        
        Args:
            trait: Big Five trait name
            n_samples: Number of samples per level
        """
        # Generate prompts
        high_prompts = [BigFiveDimensions.get_prompt(trait, 'high')] * n_samples
        low_prompts = [BigFiveDimensions.get_prompt(trait, 'low')] * n_samples
        
        texts = high_prompts + low_prompts
        labels = [1] * n_samples + [0] * n_samples
        
        # Train probes at each layer
        self.accuracies[trait] = {}
        self.probes[trait] = {}
        
        for layer in range(self.n_layers):
            probe, acc = self.train_probe(texts, labels, layer)
            self.probes[trait][layer] = probe
            self.accuracies[trait][layer] = acc
    
    def get_peak_layer(self, trait: str) -> int:
        """Get layer with highest decoding accuracy."""
        accuracies = self.accuracies[trait]
        return max(accuracies, key=accuracies.get)


class ConceptNeuronIdentifier:
    """Identify concept-selective neurons using statistical analysis."""
    
    def __init__(self, model: nn.Module):
        self.model = model
    
    def collect_activations(self, texts: List[str], 
                           label: int) -> Dict[int, List[torch.Tensor]]:
        """
        Collect neuron activations for labeled texts.
        
        Args:
            texts: Input texts
            label: Label (0 or 1)
        
        Returns:
            Dictionary mapping layer -> list of activations
        """
        activations = defaultdict(list)
        
        self.model.eval()
        with torch.no_grad():
            for text in texts:
                inputs = self.model.tokenizer(text, return_tensors='pt')
                outputs = self.model(**inputs, output_hidden_states=True)
                
                for layer_idx, hidden in enumerate(outputs.hidden_states):
                    # Mean over sequence
                    layer_activations = hidden[0].mean(dim=0)
                    activations[layer_idx].append(layer_activations)
        
        return dict(activations)
    
    def compute_selectivity(self, pos_activations: Dict[int, torch.Tensor],
                           neg_activations: Dict[int, torch.Tensor],
                           threshold: float = 0.5) -> List[Dict]:
        """
        Compute neuron selectivity using Cohen's d effect size.
        
        Args:
            pos_activations: Activations for positive class
            neg_activations: Activations for negative class
            threshold: Effect size threshold
        
        Returns:
            List of selective neuron dictionaries
        """
        selective_neurons = []
        
        for layer in pos_activations.keys():
            pos = torch.stack(pos_activations[layer])
            neg = torch.stack(neg_activations[layer])
            
            # Compute statistics
            pos_mean = pos.mean(dim=0)
            neg_mean = neg.mean(dim=0)
            pos_std = pos.std(dim=0)
            neg_std = neg.std(dim=0)
            
            # Cohen's d
            pooled_std = torch.sqrt((pos_std**2 + neg_std**2) / 2)
            cohens_d = (pos_mean - neg_mean) / (pooled_std + 1e-8)
            
            # Select neurons with large effect size
            for neuron_idx in range(len(cohens_d)):
                if abs(cohens_d[neuron_idx]) > threshold:
                    selective_neurons.append({
                        'layer': layer,
                        'neuron': neuron_idx,
                        'effect_size': cohens_d[neuron_idx].item(),
                        'direction': 'positive' if cohens_d[neuron_idx] > 0 else 'negative'
                    })
        
        return selective_neurons


class NeuronIntervener:
    """Intervene on concept neurons to control generation."""
    
    def __init__(self, model: nn.Module, concept_neurons: Dict[str, List[Dict]]):
        """
        Initialize intervener.
        
        Args:
            model: LLM model
            concept_neurons: Dictionary mapping trait -> list of neuron specs
        """
        self.model = model
        self.concept_neurons = concept_neurons
        self.hooks = []
    
    def _make_hook(self, neuron_idx: int, direction: str, 
                   strength: float):
        """Create hook function for neuron intervention."""
        def hook_fn(module, input, output):
            modified = output.clone()
            if direction == 'enhance':
                modified[:, :, neuron_idx] += strength * torch.abs(modified[:, :, neuron_idx])
            else:  # suppress
                modified[:, :, neuron_idx] *= (1 - strength)
            return modified
        return hook_fn
    
    def intervene(self, text: str, trait: str, direction: str = 'enhance',
                  strength: float = 0.5) -> str:
        """
        Generate text with concept neuron intervention.
        
        Args:
            text: Input prompt
            trait: Target Big Five trait
            direction: 'enhance' or 'suppress'
            strength: Intervention strength (0-1)
        
        Returns:
            Generated text
        """
        # Register hooks
        hooks = []
        neurons = self.concept_neurons.get(trait, [])
        
        for neuron_spec in neurons[:20]:  # Limit to top 20
            layer_idx = neuron_spec['layer']
            neuron_idx = neuron_spec['neuron']
            
            # Register hook on layer
            layer = self.model.model.layers[layer_idx]
            hook = layer.register_forward_hook(
                self._make_hook(neuron_idx, direction, strength)
            )
            hooks.append(hook)
        
        # Generate
        try:
            inputs = self.model.tokenizer(text, return_tensors='pt')
            outputs = self.model.generate(**inputs, max_length=100)
            result = self.model.tokenizer.decode(outputs[0])
        finally:
            # Remove hooks
            for hook in hooks:
                hook.remove()
        
        return result


def demonstrate_concept_analysis():
    """Demonstrate concept neuron analysis pipeline."""
    print("=" * 60)
    print("Psychological Concept Neurons Analysis")
    print("=" * 60)
    
    print("\n1. Big Five Personality Framework")
    print("-" * 40)
    for trait in BigFiveDimensions.DIMENSIONS.keys():
        high = BigFiveDimensions.DIMENSIONS[trait]['high'][:3]
        low = BigFiveDimensions.DIMENSIONS[trait]['low'][:3]
        print(f"{trait.capitalize()}:")
        print(f"  High: {', '.join(high)}")
        print(f"  Low:  {', '.join(low)}")
    
    print("\n2. Example Prompts")
    print("-" * 40)
    for trait in ['openness', 'extraversion']:
        high_prompt = BigFiveDimensions.get_prompt(trait, 'high')
        low_prompt = BigFiveDimensions.get_prompt(trait, 'low')
        print(f"\n{trait.capitalize()} - High:")
        print(f"  {high_prompt}")
        print(f"{trait.capitalize()} - Low:")
        print(f"  {low_prompt}")
    
    print("\n" + "=" * 60)
    print("Analysis Pipeline:")
    print("  1. Extract hidden states at each layer")
    print("  2. Train linear probes for trait classification")
    print("  3. Identify selective neurons using Cohen's d")
    print("  4. Intervene to enhance/suppress traits")
    print("  5. Evaluate representation vs behavior control")
    print("=" * 60)


if __name__ == '__main__':
    demonstrate_concept_analysis()
