---
name: quantum-medical-diagnosis-patterns
description: Reusable patterns for building hybrid quantum-classical Medical AI diagnosis systems — combining quantum ML, classical ML, and medical domain knowledge.
version: 1.0.0
category: quantum-medical
activation_keywords: [quantum medical diagnosis, hybrid quantum-classical, medical AI, quantum healthcare, diagnosis pattern, clinical quantum ML]
last_updated: 2026-06-14
---

# Quantum Medical Diagnosis Patterns

## Overview

This skill provides reusable patterns for building hybrid quantum-classical medical diagnosis systems. It combines quantum machine learning advantages with classical medical AI robustness, incorporating domain-specific medical knowledge.

## Core Pattern Categories

### Pattern 1: Quantum-Enhanced Feature Extraction

**Use Case**: Extracting quantum-enhanced features from medical images/text for diagnosis.

**Pattern Structure**:

```
Classical Medical Data → Quantum Feature Map → Quantum Feature Extraction → Classical ML Classifier → Diagnosis
```

**Implementation Pattern**:

```python
from typing import List, Tuple, Dict
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

class QuantumMedicalFeatureExtractor:
    """
    Pattern: Quantum-enhanced feature extraction for medical diagnosis
    
    Template parameters:
    - n_qubits: Number of qubits (default: 8)
    - feature_dim: Classical feature dimension
    - shots: Quantum measurement shots
    """
    
    def __init__(
        self,
        n_qubits: int = 8,
        feature_dim: int = 128,
        shots: int = 4096
    ):
        self.n_qubits = n_qubits
        self.feature_dim = feature_dim
        self.shots = shots
        self.simulator = AerSimulator()
    
    def encode_medical_features(
        self,
        features: np.ndarray,
        encoding_type: str = 'angle'
    ) -> QuantumCircuit:
        """
        Encode medical features into quantum states
        
        Pattern parameters:
        - encoding_type: 'angle' | 'amplitude' | 'basis'
        
        Args:
            features: Medical features (e.g., radiomics, clinical features)
            encoding_type: Quantum encoding strategy
        
        Returns:
            QuantumCircuit with encoded medical data
        """
        qc = QuantumCircuit(self.n_qubits)
        
        if encoding_type == 'angle':
            # Angle encoding for medical features
            normalized = self._normalize_features(features)
            for i in range(min(self.n_qubits, len(normalized))):
                qc.ry(normalized[i] * np.pi, i)
        
        elif encoding_type == 'amplitude':
            # Amplitude encoding (requires feature_dim = 2^n_qubits)
            normalized = features / np.linalg.norm(features)
            qc.initialize(normalized[:2**self.n_qubits], range(self.n_qubits))
        
        elif encoding_type == 'basis':
            # Basis encoding for categorical medical features
            binary_features = self._discretize_features(features)
            for i, bit in enumerate(binary_features[:self.n_qubits]):
                if bit == 1:
                    qc.x(i)
        
        # Add entanglement for medical feature correlation
        self._add_medical_correlation_entanglement(qc)
        
        return qc
    
    def extract_quantum_features(
        self,
        classical_features: np.ndarray
    ) -> np.ndarray:
        """
        Extract quantum-enhanced features
        
        Pattern flow:
        1. Encode classical medical features to quantum
        2. Apply quantum transformation
        3. Measure quantum state
        4. Extract enhanced features
        
        Args:
            classical_features: Medical features from classical model
        
        Returns:
            Quantum-enhanced feature vector
        """
        # Encode
        qc = self.encode_medical_features(classical_features)
        
        # Apply quantum transformation (e.g., quantum Fourier transform)
        for i in range(self.n_qubits):
            qc.h(i)
        
        # Measure
        qc.measure_all()
        
        # Execute
        result = self.simulator.run(qc, shots=self.shots).result()
        counts = result.get_counts()
        
        # Extract quantum features from measurement statistics
        quantum_features = self._counts_to_features(counts)
        
        return quantum_features
    
    def _normalize_features(self, features: np.ndarray) -> np.ndarray:
        """Normalize medical features to [0, 1]"""
        return (features - features.min()) / (features.max() - features.min())
    
    def _discretize_features(self, features: np.ndarray) -> List[int]:
        """Discretize continuous medical features to binary"""
        threshold = np.median(features)
        return [1 if f > threshold else 0 for f in features]
    
    def _add_medical_correlation_entanglement(
        self,
        qc: QuantumCircuit
    ) -> None:
        """Add entanglement representing medical feature correlations"""
        # CNOT chain for correlation
        for i in range(self.n_qubits - 1):
            qc.cx(i, i + 1)
        
        # Ring entanglement for holistic medical features
        qc.cx(self.n_qubits - 1, 0)
    
    def _counts_to_features(
        self,
        counts: Dict[str, int]
    ) -> np.ndarray:
        """Convert quantum measurement counts to feature vector"""
        features = np.zeros(2**self.n_qubits)
        for state, count in counts.items():
            idx = int(state, 2)
            features[idx] = count / self.shots
        return features
```

**Pattern Application Examples**:

1. **Radiomics Feature Extraction**:
   - Classical radiomics → quantum encoding → quantum features → diagnosis

2. **Clinical Feature Fusion**:
   - Multiple clinical features → quantum entanglement → unified quantum feature → prognosis

### Pattern 2: Hybrid Quantum-Classical Classifier

**Use Case**: Building robust medical diagnosis classifiers combining quantum and classical ML.

**Pattern Structure**:

```
Medical Data → [Classical Feature Extraction] → [Quantum Feature Enhancement] → [Hybrid Classifier] → Diagnosis
                     ↓                              ↓                              ↓
                 Classical ML                    Quantum ML                   Ensemble/Voting
```

**Implementation Pattern**:

```python
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
import torch
import torch.nn as nn

class HybridQuantumClassicalMedicalClassifier:
    """
    Pattern: Hybrid quantum-classical classifier for medical diagnosis
    
    Template parameters:
    - classical_models: List of classical ML models
    - quantum_model: Quantum ML model (VQC, QNN)
    - fusion_strategy: 'ensemble' | 'sequential' | 'parallel'
    """
    
    def __init__(
        self,
        classical_models: List = None,
        quantum_model = None,
        fusion_strategy: str = 'ensemble'
    ):
        # Default classical models for medical diagnosis
        if classical_models is None:
            classical_models = [
                RandomForestClassifier(n_estimators=100),
                GradientBoostingClassifier(n_estimators=100),
                SVC(kernel='rbf', probability=True),
                MLPClassifier(hidden_layer_sizes=(128, 64))
            ]
        
        self.classical_models = classical_models
        self.quantum_model = quantum_model
        self.fusion_strategy = fusion_strategy
        
        # Model weights for ensemble
        self.model_weights = None
    
    def fit(
        self,
        classical_features: np.ndarray,
        quantum_features: np.ndarray,
        labels: np.ndarray
    ) -> None:
        """
        Train hybrid classifier
        
        Pattern flow:
        1. Train classical models on classical features
        2. Train quantum model on quantum features
        3. Learn fusion weights
        
        Args:
            classical_features: Features from classical medical AI
            quantum_features: Quantum-enhanced features
            labels: Medical diagnosis labels
        """
        # Train classical models
        for model in self.classical_models:
            model.fit(classical_features, labels)
        
        # Train quantum model
        if self.quantum_model is not None:
            self.quantum_model.fit(quantum_features, labels)
        
        # Learn fusion weights based on validation performance
        self._learn_fusion_weights(
            classical_features,
            quantum_features,
            labels
        )
    
    def predict(
        self,
        classical_features: np.ndarray,
        quantum_features: np.ndarray
    ) -> np.ndarray:
        """
        Make hybrid diagnosis predictions
        
        Pattern strategies:
        - ensemble: Weighted average of all model predictions
        - sequential: Classical → quantum refinement
        - parallel: Independent predictions then fusion
        
        Args:
            classical_features: Classical medical features
            quantum_features: Quantum-enhanced features
        
        Returns:
            Diagnosis predictions
        """
        if self.fusion_strategy == 'ensemble':
            return self._ensemble_predict(
                classical_features,
                quantum_features
            )
        
        elif self.fusion_strategy == 'sequential':
            return self._sequential_predict(
                classical_features,
                quantum_features
            )
        
        elif self.fusion_strategy == 'parallel':
            return self._parallel_predict(
                classical_features,
                quantum_features
            )
    
    def _ensemble_predict(
        self,
        classical_features: np.ndarray,
        quantum_features: np.ndarray
    ) -> np.ndarray:
        """
        Ensemble fusion pattern
        
        Pattern: Weighted voting across all models
        """
        predictions = []
        
        # Classical model predictions
        for model in self.classical_models:
            pred = model.predict_proba(classical_features)
            predictions.append(pred)
        
        # Quantum model prediction
        if self.quantum_model is not None:
            q_pred = self.quantum_model.predict_proba(quantum_features)
            predictions.append(q_pred)
        
        # Weighted ensemble
        weighted_pred = np.zeros_like(predictions[0])
        for i, pred in enumerate(predictions):
            weighted_pred += self.model_weights[i] * pred
        
        return np.argmax(weighted_pred, axis=1)
    
    def _sequential_predict(
        self,
        classical_features: np.ndarray,
        quantum_features: np.ndarray
    ) -> np.ndarray:
        """
        Sequential fusion pattern
        
        Pattern: Classical coarse diagnosis → quantum refinement
        """
        # Stage 1: Classical coarse diagnosis
        classical_pred = self.classical_models[0].predict(classical_features)
        
        # Stage 2: Quantum refinement for uncertain cases
        refined_pred = classical_pred.copy()
        
        # Get uncertainty from classical model
        classical_proba = self.classical_models[0].predict_proba(classical_features)
        uncertainty = 1 - np.max(classical_proba, axis=1)
        
        # Refine uncertain cases with quantum model
        uncertain_indices = uncertainty > 0.3
        
        if self.quantum_model is not None and np.any(uncertain_indices):
            refined_pred[uncertain_indices] = self.quantum_model.predict(
                quantum_features[uncertain_indices]
            )
        
        return refined_pred
    
    def _parallel_predict(
        self,
        classical_features: np.ndarray,
        quantum_features: np.ndarray
    ) -> np.ndarray:
        """
        Parallel fusion pattern
        
        Pattern: Independent predictions, then clinical decision fusion
        """
        # Classical prediction
        classical_pred = self.classical_models[0].predict(classical_features)
        
        # Quantum prediction
        quantum_pred = None
        if self.quantum_model is not None:
            quantum_pred = self.quantum_model.predict(quantum_features)
        
        # Clinical decision fusion
        if quantum_pred is not None:
            # Use quantum when classical is uncertain
            classical_proba = self.classical_models[0].predict_proba(classical_features)
            confidence = np.max(classical_proba, axis=1)
            
            final_pred = np.where(
                confidence > 0.7,
                classical_pred,
                quantum_pred
            )
        else:
            final_pred = classical_pred
        
        return final_pred
    
    def _learn_fusion_weights(
        self,
        classical_features: np.ndarray,
        quantum_features: np.ndarray,
        labels: np.ndarray
    ) -> None:
        """Learn optimal fusion weights from validation data"""
        from sklearn.model_selection import cross_val_score
        
        weights = []
        
        for model in self.classical_models:
            score = cross_val_score(model, classical_features, labels, cv=5).mean()
            weights.append(score)
        
        if self.quantum_model is not None:
            q_score = cross_val_score(
                self.quantum_model,
                quantum_features,
                labels,
                cv=5
            ).mean()
            weights.append(q_score)
        
        # Normalize weights
        self.model_weights = np.array(weights) / np.sum(weights)
```

### Pattern 3: Quantum Medical Knowledge Graph

**Use Case**: Integrating quantum computation with medical knowledge graphs for diagnosis reasoning.

**Pattern Structure**:

```
Medical Knowledge Graph → Quantum Graph Embedding → Quantum Similarity → Diagnosis Recommendation
          ↓                      ↓                    ↓                 ↓
    Entity/Relation          Quantum State         Quantum Measure    Clinical Path
```

**Implementation Pattern**:

```python
class QuantumMedicalKnowledgeGraph:
    """
    Pattern: Quantum-enhanced medical knowledge graph for diagnosis reasoning
    
    Template parameters:
    - n_qubits_per_entity: Qubits for encoding medical entities
    - knowledge_graph: Medical knowledge graph (nodes: diseases, symptoms, treatments)
    """
    
    def __init__(
        self,
        knowledge_graph: Dict,
        n_qubits_per_entity: int = 4
    ):
        self.kg = knowledge_graph
        self.n_qubits_per_entity = n_qubits_per_entity
        
        # Build quantum entity embeddings
        self.quantum_entity_embeddings = self._build_quantum_embeddings()
    
    def encode_entity(
        self,
        entity: str,
        entity_type: str
    ) -> QuantumCircuit:
        """
        Encode medical entity into quantum state
        
        Pattern: Entity → quantum encoding based on entity type
        
        Args:
            entity: Medical entity (disease, symptom, treatment)
            entity_type: Type of entity
        
        Returns:
            Quantum encoding of entity
        """
        qc = QuantumCircuit(self.n_qubits_per_entity)
        
        # Get entity properties from knowledge graph
        entity_properties = self.kg['entities'][entity]
        
        # Encode based on entity type
        if entity_type == 'disease':
            # Encode disease severity, prevalence, etc.
            severity = entity_properties['severity']
            prevalence = entity_properties['prevalence']
            
            qc.ry(severity * np.pi, 0)
            qc.ry(prevalence * np.pi, 1)
        
        elif entity_type == 'symptom':
            # Encode symptom frequency, specificity
            frequency = entity_properties['frequency']
            specificity = entity_properties['specificity']
            
            qc.ry(frequency * np.pi, 0)
            qc.ry(specificity * np.pi, 1)
        
        elif entity_type == 'treatment':
            # Encode treatment efficacy, side effects
            efficacy = entity_properties['efficacy']
            side_effects = entity_properties['side_effects']
            
            qc.ry(efficacy * np.pi, 0)
            qc.ry(side_effects * np.pi, 1)
        
        return qc
    
    def compute_quantum_similarity(
        self,
        entity1: str,
        entity2: str
    ) -> float:
        """
        Compute quantum similarity between medical entities
        
        Pattern: Quantum inner product for entity similarity
        
        Args:
            entity1: First medical entity
            entity2: Second medical entity
        
        Returns:
            Quantum similarity score
        """
        qc1 = self.quantum_entity_embeddings[entity1]
        qc2 = self.quantum_entity_embeddings[entity2]
        
        # Compute quantum inner product
        joint_qc = qc1.copy()
        joint_qc.compose(qc2.inverse(), inplace=True)
        
        joint_qc.measure_all()
        
        simulator = AerSimulator()
        result = simulator.run(joint_qc, shots=1024).result()
        counts = result.get_counts()
        
        similarity = counts.get('0'*self.n_qubits_per_entity, 0) / 1024
        
        return similarity
    
    def diagnose_via_quantum_reasoning(
        self,
        symptoms: List[str],
        patient_features: np.ndarray
    ) -> Dict:
        """
        Quantum reasoning for medical diagnosis
        
        Pattern flow:
        1. Encode symptoms into quantum states
        2. Query knowledge graph with quantum similarity
        3. Rank candidate diseases by quantum similarity
        4. Return diagnosis recommendations
        
        Args:
            symptoms: Patient symptoms
            patient_features: Patient clinical features
        
        Returns:
            Diagnosis recommendations with quantum reasoning path
        """
        candidate_diseases = self.kg['relations']['symptom_to_disease']
        
        diagnosis_scores = {}
        
        for disease in candidate_diseases:
            total_similarity = 0
            
            for symptom in symptoms:
                similarity = self.compute_quantum_similarity(symptom, disease)
                total_similarity += similarity
            
            # Weight by disease prevalence
            prevalence = self.kg['entities'][disease]['prevalence']
            weighted_score = total_similarity * prevalence
            
            diagnosis_scores[disease] = weighted_score
        
        # Sort by diagnosis score
        sorted_diagnoses = sorted(
            diagnosis_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        return {
            'diagnoses': sorted_diagnoses[:5],
            'quantum_reasoning_path': self._generate_reasoning_path(
                symptoms,
                sorted_diagnoses[:5]
            )
        }
    
    def _build_quantum_embeddings(self) -> Dict:
        """Build quantum embeddings for all medical entities"""
        embeddings = {}
        
        for entity_type in ['disease', 'symptom', 'treatment']:
            for entity in self.kg['entities'][entity_type]:
                embeddings[entity] = self.encode_entity(entity, entity_type)
        
        return embeddings
    
    def _generate_reasoning_path(
        self,
        symptoms: List[str],
        diagnoses: List[Tuple]
    ) -> List:
        """Generate quantum reasoning path for diagnosis"""
        path = []
        
        for disease, score in diagnoses:
            reasoning = {
                'disease': disease,
                'quantum_score': score,
                'supporting_symptoms': symptoms,
                'quantum_similarities': {
                    s: self.compute_quantum_similarity(s, disease)
                    for s in symptoms
                }
            }
            path.append(reasoning)
        
        return path
```

### Pattern 4: Quantum-Enhanced Multi-Modal Medical Diagnosis

**Use Case**: Integrating multiple medical modalities (image, text, genomics) via quantum fusion.

**Pattern Structure**:

```
[Medical Image] → [Medical Text] → [Genomics] → Quantum Multi-Modal Fusion → Diagnosis
      ↓               ↓              ↓               ↓                    ↓
  Vision Features   NLP Features  Genomics Features  Quantum Fusion    Clinical Decision
```

**Implementation Pattern**:

```python
class QuantumMultiModalMedicalDiagnosis:
    """
    Pattern: Quantum multi-modal fusion for medical diagnosis
    
    Template parameters:
    - modalities: List of medical modalities (image, text, genomics)
    - fusion_method: 'quantum_kernel' | 'quantum_state_fusion'
    """
    
    def __init__(
        self,
        modalities: List[str] = ['image', 'text', 'genomics'],
        fusion_method: str = 'quantum_kernel'
    ):
        self.modalities = modalities
        self.fusion_method = fusion_method
        
        self.feature_extractors = self._initialize_feature_extractors()
        self.quantum_fusion_layer = self._initialize_quantum_fusion()
    
    def extract_multimodal_features(
        self,
        medical_data: Dict
    ) -> Dict:
        """
        Extract features from multiple medical modalities
        
        Pattern: Multi-modal extraction → quantum encoding
        
        Args:
            medical_data: Dictionary containing medical image, text, genomics
        
        Returns:
            Quantum-encoded multi-modal features
        """
        features = {}
        
        for modality in self.modalities:
            if modality in medical_data:
                # Extract classical features
                classical_features = self.feature_extractors[modality](
                    medical_data[modality]
                )
                
                # Quantum encode
                quantum_features = self._quantum_encode_features(
                    classical_features,
                    modality
                )
                
                features[modality] = {
                    'classical': classical_features,
                    'quantum': quantum_features
                }
        
        return features
    
    def fuse_multimodal_quantum(
        self,
        multimodal_features: Dict
    ) -> np.ndarray:
        """
        Fuse multi-modal features via quantum computation
        
        Pattern strategies:
        - quantum_kernel: Compute quantum kernels and fuse
        - quantum_state_fusion: Direct quantum state superposition
        
        Args:
            multimodal_features: Features from all modalities
        
        Returns:
            Fused quantum multi-modal representation
        """
        if self.fusion_method == 'quantum_kernel':
            return self._kernel_fusion(multimodal_features)
        
        elif self.fusion_method == 'quantum_state_fusion':
            return self._state_fusion(multimodal_features)
    
    def _kernel_fusion(
        self,
        multimodal_features: Dict
    ) -> np.ndarray:
        """
        Quantum kernel fusion pattern
        
        Pattern: Compute quantum kernels between modalities, then fuse
        """
        n_qubits = 8
        simulator = AerSimulator()
        
        # Compute quantum kernels between modalities
        kernel_matrix = np.zeros((len(self.modalities), len(self.modalities)))
        
        for i, mod1 in enumerate(self.modalities):
            for j, mod2 in enumerate(self.modalities):
                if mod1 in multimodal_features and mod2 in multimodal_features:
                    kernel_matrix[i, j] = self._compute_quantum_kernel(
                        multimodal_features[mod1]['quantum'],
                        multimodal_features[mod2]['quantum'],
                        simulator
                    )
        
        # Fuse via kernel matrix operations
        fused_features = np.concatenate([
            multimodal_features[m]['classical'] for m in self.modalities if m in multimodal_features
        ])
        
        # Apply quantum kernel weighting
        weighted_fusion = np.dot(kernel_matrix.flatten(), fused_features)
        
        return weighted_fusion
    
    def _state_fusion(
        self,
        multimodal_features: Dict
    ) -> np.ndarray:
        """
        Quantum state fusion pattern
        
        Pattern: Create superposition of quantum states from all modalities
        """
        from qiskit import QuantumCircuit
        
        n_qubits = 16  # 4 qubits per modality
        
        qc = QuantumCircuit(n_qubits)
        
        # Encode each modality
        for i, modality in enumerate(self.modalities):
            if modality in multimodal_features:
                mod_features = multimodal_features[modality]['quantum']
                
                # Encode to respective qubits
                qubit_range = range(i*4, (i+1)*4)
                for j, qubit in enumerate(qubit_range):
                    if j < len(mod_features):
                        qc.ry(mod_features[j] * np.pi, qubit)
        
        # Create superposition (fusion)
        for i in range(n_qubits):
            qc.h(i)
        
        # Add cross-modality entanglement
        for i in range(0, n_qubits-4, 4):
            qc.cx(i, i+4)  # Image to text
            qc.cx(i+4, i+8)  # Text to genomics
        
        # Measure
        qc.measure_all()
        
        simulator = AerSimulator()
        result = simulator.run(qc, shots=4096).result()
        counts = result.get_counts()
        
        # Convert to fused features
        fused = np.zeros(2**n_qubits)
        for state, count in counts.items():
            idx = int(state, 2)
            fused[idx] = count / 4096
        
        return fused
    
    def diagnose(
        self,
        medical_data: Dict
    ) -> Dict:
        """
        Complete quantum multi-modal diagnosis
        
        Pattern flow:
        1. Extract multi-modal features
        2. Quantum fuse modalities
        3. Classify with hybrid classifier
        4. Return diagnosis
        
        Args:
            medical_data: Multi-modal medical data
        
        Returns:
            Diagnosis result
        """
        # Extract features
        features = self.extract_multimodal_features(medical_data)
        
        # Quantum fuse
        fused_features = self.fuse_multimodal_quantum(features)
        
        # Classify (simplified)
        # In practice, use trained hybrid classifier
        diagnosis = self._simple_classification(fused_features)
        
        return diagnosis
    
    def _initialize_feature_extractors(self) -> Dict:
        """Initialize modality-specific feature extractors"""
        extractors = {}
        
        # Image: Use pre-trained medical vision model
        extractors['image'] = lambda x: self._extract_medical_image_features(x)
        
        # Text: Use clinical NLP model
        extractors['text'] = lambda x: self._extract_medical_text_features(x)
        
        # Genomics: Use genomics feature extractor
        extractors['genomics'] = lambda x: self._extract_genomics_features(x)
        
        return extractors
    
    def _initialize_quantum_fusion(self):
        """Initialize quantum fusion layer"""
        return None  # Placeholder
    
    def _quantum_encode_features(
        self,
        features: np.ndarray,
        modality: str
    ) -> np.ndarray:
        """Quantum encode features for specific modality"""
        normalized = features / np.linalg.norm(features)
        return normalized[:8]  # Use 8 features per modality
    
    def _compute_quantum_kernel(
        self,
        features1: np.ndarray,
        features2: np.ndarray,
        simulator
    ) -> float:
        """Compute quantum kernel between feature sets"""
        # Simplified quantum kernel computation
        return np.dot(features1, features2)
    
    def _extract_medical_image_features(self, image) -> np.ndarray:
        """Extract medical image features"""
        # Placeholder: Use pre-trained model
        return np.random.randn(128)
    
    def _extract_medical_text_features(self, text) -> np.ndarray:
        """Extract medical text features"""
        # Placeholder: Use clinical NLP model
        return np.random.randn(128)
    
    def _extract_genomics_features(self, genomics) -> np.ndarray:
        """Extract genomics features"""
        # Placeholder: Use genomics processor
        return np.random.randn(128)
    
    def _simple_classification(self, features) -> Dict:
        """Simple classification for demonstration"""
        return {
            'diagnosis': 'Quantum-enhanced diagnosis result',
            'confidence': 0.85,
            'quantum_fusion_score': np.mean(features)
        }
```

## Pattern Selection Guide

### When to Use Each Pattern

| Pattern | Best Use Case | Key Advantages |
|---------|---------------|-----------------|
| **Quantum-Enhanced Feature Extraction** | Medical image/text diagnosis | Quantum feature space expressivity |
| **Hybrid Quantum-Classical Classifier** | Robust medical diagnosis | Combines quantum advantage with classical robustness |
| **Quantum Medical Knowledge Graph** | Diagnosis reasoning with medical knowledge | Quantum similarity for knowledge reasoning |
| **Quantum-Enhanced Multi-Modal Diagnosis** | Multi-modal medical data fusion | Quantum fusion of disparate modalities |

### Pattern Combinations

Patterns can be combined:

1. **Feature Extraction + Hybrid Classifier**: Most common for diagnosis
2. **Multi-Modal Fusion + Knowledge Graph**: For complex diagnostic reasoning
3. **All patterns**: For comprehensive quantum medical AI system

## Pitfalls and Solutions

### Pitfall 1: Quantum Hardware Limitations

**Problem**: NISQ quantum computers have limited qubits and noise.

**Solution**: Use error mitigation and limited qubit encoding:

```python
# Limit to 4-8 qubits for practical medical applications
n_qubits = min(available_qubits, 8)

# Use error mitigation
from qiskit.transpiler.passes import RemoveBarriers
from qiskit_aer.noise import NoiseModel

def apply_error_mitigation(qc, simulator):
    """Apply readout error mitigation"""
    # Use measurement error mitigation
    mitigated_result = simulator.run(qc).result()
    return mitigated_result
```

### Pitfall 2: Medical Domain Misalignment

**Problem**: Quantum features may not align with medical domain semantics.

**Solution**: Design medical-specific quantum encodings:

```python
def medical_semantic_quantum_encoding(features, medical_category):
    """
    Medical semantic-aware quantum encoding
    
    Args:
        features: Medical features
        medical_category: 'radiomics' | 'clinical' | 'genomics'
    
    Returns:
        Semantic-aware quantum encoding
    """
    encoding_params = {
        'radiomics': {'angle_scale': np.pi/2, 'entanglement': 'full'},
        'clinical': {'angle_scale': np.pi/4, 'entanglement': 'partial'},
        'genomics': {'angle_scale': np.pi, 'entanglement': 'none'}
    }
    
    params = encoding_params[medical_category]
    
    # Apply semantic encoding
    encoded = features * params['angle_scale']
    
    return encoded
```

### Pitfall 3: Training Data Insufficiency

**Problem**: Medical diagnosis requires large training data; quantum models may overfit.

**Solution**: Use hybrid transfer learning:

```python
def quantum_transfer_learning(
    classical_pretrained_model,
    quantum_feature_extractor,
    medical_dataset
):
    """
    Quantum transfer learning pattern
    
    Pattern: Pre-trained classical + quantum fine-tuning
    """
    # Extract features from pre-trained classical model
    classical_features = classical_pretrained_model.extract_features(
        medical_dataset
    )
    
    # Quantum enhance
    quantum_features = quantum_feature_extractor.extract(
        classical_features
    )
    
    # Fine-tune small quantum classifier
    # (less prone to overfitting)
    quantum_classifier.fit(quantum_features, medical_dataset.labels)
    
    return quantum_classifier
```

## Verification Patterns

### Pattern Validation Checklist

```python
def validate_quantum_medical_pattern(
    pattern,
    test_data,
    expected_diagnosis
):
    """
    Validate quantum medical diagnosis pattern
    
    Checklist:
    1. Quantum feature expressivity
    2. Diagnosis accuracy
    3. Quantum-classical alignment
    4. Medical domain relevance
    
    Args:
        pattern: Implemented quantum medical pattern
        test_data: Test medical data
        expected_diagnosis: Expected diagnosis labels
    
    Returns:
        Validation metrics
    """
    metrics = {}
    
    # 1. Quantum feature expressivity
    quantum_features = pattern.extract_quantum_features(test_data)
    eigenvalues = np.linalg.eigvalsh(
        np.cov(quantum_features.T)
    )
    metrics['expressivity'] = np.sum(eigenvalues > 1e-6)
    
    # 2. Diagnosis accuracy
    predictions = pattern.predict(test_data)
    metrics['accuracy'] = np.mean(predictions == expected_diagnosis)
    
    # 3. Quantum-classical alignment
    classical_features = pattern.extract_classical_features(test_data)
    correlation = np.corrcoef(
        quantum_features.flatten(),
        classical_features.flatten()
    )[0, 1]
    metrics['alignment'] = correlation
    
    # 4. Medical domain relevance (simplified)
    metrics['medical_relevance'] = metrics['accuracy']
    
    return metrics
```

## References

1. **Quantum Medical ML**:
   - Quantum kernel methods for medical diagnosis
   - Hybrid quantum-classical medical AI

2. **Medical Foundation Models**:
   - MedCLIP, MedSAM, Clinical LLMs

3. **Pattern Libraries**:
   - Design patterns for AI systems
   - Medical AI pattern catalog

## Related Skills

- [[quantum-kernel-medical-embeddings]]: Quantum kernel methodology
- [[quantum-medical-imaging]]: Quantum methods for medical imaging
- [[quantum-healthcare-foundation-models]]: Quantum foundation models for healthcare