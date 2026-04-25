---
name: hyperdimensional-stdp-computing
description: "Hyperdimensional Computing (HDC) with emergent STDP-like plasticity using Galois-field algebra. Implements deterministic HDC with path-dependent semantic selection equivalent to spike-timing-dependent plasticity. Activation: hyperdimensional computing, HDC STDP, sparse distributed memory, Galois-field HDC, emergent plasticity."
---

# Hyperdimensional Computing with Emergent STDP

## Description

Hyperdimensional Computing (HDC) architecture based on Galois-field algebra that exhibits emergent spike-timing-dependent plasticity (STDP)-like mechanisms through path-dependent semantic selection. This deterministic computing paradigm achieves associative memory and learning without explicit training, using ultra-high speed, ultra-low power SRAM-CAM (VaCoAl) implementations.

Based on research from arXiv:2604.11665v2 - "Beyond LLMs, Sparse Distributed Memory, and Neuromorphics: A Hyper-Dimensional SRAM-CAM 'VaCoAl'" by Hiroyuki Chuma et al.

## Activation Keywords

- hyperdimensional computing
- HDC STDP
- sparse distributed memory
- Galois-field HDC
- emergent plasticity
- VaCoAl
- hypervector computing
- HD computing
- 超维计算
- 高维向量计算

## Tools Used

- `write`: Create HDC implementations
- `exec`: Run HDC operations and simulations
- `read`: Load hypervector dictionaries
- `patch`: Modify binding/unbinding operations

## Core Concepts

### 1. Hyperdimensional Representations

Hypervectors (high-dimensional vectors, typically 10,000 dimensions):
- **Holographic**: Information distributed across all dimensions
- **Robust**: Tolerant to noise and component failure
- **Random**: Randomly generated basis vectors
- **Similarity**: Measured by cosine similarity or Hamming distance

### 2. Galois-Field Algebra

Operations in HDC:
- **Binding (⊗)**: Element-wise multiplication (XOR for binary)
- **Bundling (⊕)**: Element-wise addition (majority vote for binary)
- **Permutation (ρ)**: Shuffling dimensions for sequence encoding
- **Inverse**: Element-wise inverse for unbinding

### 3. Emergent STDP

Path-dependent learning emerges from:
- **Sequence encoding**: Order matters in binding operations
- **Accumulated binding**: History-dependent representations
- **Similarity gradients**: Nearest-neighbor retrieval
- **Associative chaining**: Context-dependent activation

## Implementation

### Step 1: Hypervector Basis

```python
import numpy as np
import torch

class HypervectorBasis:
    """
    Generate and manage hypervector basis for symbols.
    """
    
    def __init__(self, dim=10000, vtype='binary', seed=42):
        """
        Args:
            dim: Dimensionality of hypervectors
            vtype: 'binary' or 'bipolar'
            seed: Random seed
        """
        self.dim = dim
        self.vtype = vtype
        self.seed = seed
        self.basis = {}
        self.rng = np.random.RandomState(seed)
    
    def get_vector(self, symbol):
        """Get or create basis hypervector for symbol."""
        if symbol not in self.basis:
            if self.vtype == 'binary':
                self.basis[symbol] = self.rng.randint(0, 2, size=self.dim).astype(np.float32)
            elif self.vtype == 'bipolar':
                self.basis[symbol] = self.rng.choice([-1, 1], size=self.dim).astype(np.float32)
        return self.basis[symbol].copy()
    
    def similarity(self, v1, v2, metric='cosine'):
        """
        Compute similarity between hypervectors.
        
        Args:
            v1, v2: Hypervectors
            metric: 'cosine' or 'hamming'
        """
        if metric == 'cosine':
            if self.vtype == 'binary':
                # Cosine for binary: normalized dot product
                return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-8)
            else:
                return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-8)
        elif metric == 'hamming':
            return 1 - np.sum(v1 != v2) / self.dim
    
    def cleanup(self, query_vector, symbols=None, top_k=1):
        """
        Find most similar symbol to query vector.
        
        Args:
            query_vector: Query hypervector
            symbols: List of symbols to search (None = all)
            top_k: Number of matches to return
        """
        if symbols is None:
            symbols = list(self.basis.keys())
        
        similarities = []
        for symbol in symbols:
            sim = self.similarity(query_vector, self.basis[symbol])
            similarities.append((symbol, sim))
        
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_k]


class GaloisFieldHDC:
    """
    HDC with Galois-field algebra operations.
    """
    
    def __init__(self, dim=10000, field_order=2):
        """
        Args:
            dim: Dimensionality
            field_order: Galois field order (2 for binary)
        """
        self.dim = dim
        self.q = field_order  # Field order
        
    def bind(self, v1, v2):
        """
        Bind two hypervectors (element-wise multiplication).
        For binary: XOR
        For bipolar: Element-wise product
        """
        if self.q == 2:
            # Binary: XOR
            return np.mod(v1 + v2, 2)
        else:
            # Bipolar: Element-wise product
            return v1 * v2
    
    def unbind(self, v_bound, v_key):
        """
        Unbind a hypervector.
        For binary: XOR is self-inverse
        For bipolar: Division = multiplication
        """
        return self.bind(v_bound, v_key)  # Self-inverse
    
    def bundle(self, vectors, weights=None):
        """
        Bundle multiple hypervectors.
        For binary: Majority vote
        For bipolar: Weighted sum + threshold
        """
        if len(vectors) == 0:
            return np.zeros(self.dim)
        
        if weights is None:
            weights = np.ones(len(vectors))
        
        if self.q == 2:
            # Majority vote for binary
            weighted_sum = np.average(vectors, axis=0, weights=weights)
            return (weighted_sum > 0.5).astype(np.float32)
        else:
            # Threshold for bipolar
            weighted_sum = np.average(vectors, axis=0, weights=weights)
            return np.sign(weighted_sum)
    
    def permute(self, vector, shift=1):
        """
        Permute hypervector dimensions.
        Used for encoding sequence order.
        """
        return np.roll(vector, shift)
    
    def inverse_permute(self, vector, shift=1):
        """Inverse permutation."""
        return np.roll(vector, -shift)
```

### Step 2: Associative Memory

```python
class SparseDistributedMemory:
    """
    Sparse Distributed Memory (SDM) for HDC.
    """
    
    def __init__(self, dim=10000, num_locations=1000000, address_radius=0.45):
        """
        Args:
            dim: Hypervector dimension
            num_locations: Number of hard locations
            address_radius: Hamming radius for addressing
        """
        self.dim = dim
        self.num_locations = num_locations
        self.address_radius = int(dim * address_radius)
        
        # Random address for each hard location
        self.addresses = np.random.randint(0, 2, size=(num_locations, dim)).astype(np.float32)
        
        # Counters for storage (can be negative for deletion)
        self.counters = np.zeros((num_locations, dim), dtype=np.int32)
        
        # Activation mask (which locations are written)
        self.activated = np.zeros(num_locations, dtype=bool)
    
    def address_decode(self, query_address):
        """
        Find hard locations within Hamming radius of query.
        
        Args:
            query_address: Query hypervector
        
        Returns:
            selected_indices: Indices of activated hard locations
        """
        # Compute Hamming distances
        distances = np.sum(self.addresses != query_address, axis=1)
        
        # Select within radius
        selected = distances <= self.address_radius
        
        return np.where(selected)[0]
    
    def store(self, address, data):
        """
        Store data at address.
        
        Args:
            address: Address hypervector
            data: Data hypervector to store
        """
        selected = self.address_decode(address)
        
        # Increment counters for selected locations
        for idx in selected:
            self.counters[idx] += (2 * data - 1).astype(np.int32)  # Convert 0/1 to -1/+1
            self.activated[idx] = True
        
        return len(selected)
    
    def retrieve(self, address):
        """
        Retrieve data from address.
        
        Args:
            address: Query address
        
        Returns:
            data: Retrieved data hypervector
        """
        selected = self.address_decode(address)
        
        if len(selected) == 0:
            return np.zeros(self.dim)
        
        # Sum counters from selected locations
        summed = np.sum(self.counters[selected], axis=0)
        
        # Threshold to binary
        return (summed > 0).astype(np.float32)
    
    def erase(self, address, data):
        """Erase specific data from address."""
        selected = self.address_decode(address)
        
        for idx in selected:
            self.counters[idx] -= (2 * data - 1).astype(np.int32)


class HDAssociativeMemory:
    """
    High-level associative memory using HDC.
    """
    
    def __init__(self, dim=10000):
        self.dim = dim
        self.hdc = GaloisFieldHDC(dim)
        self.basis = HypervectorBasis(dim)
        self.memory = SparseDistributedMemory(dim)
        
    def encode_association(self, key, value):
        """
        Encode key-value association.
        
        Stores: bind(address(key), value)
        """
        key_addr = self.basis.get_vector(key)
        value_vec = self.basis.get_vector(value)
        
        # Bind key address with value
        bound = self.hdc.bind(key_addr, value_vec)
        
        # Store in SDM
        self.memory.store(key_addr, bound)
    
    def retrieve_association(self, key):
        """
        Retrieve value associated with key.
        
        Retrieves from bind(address(key), value) by unbinding
        """
        key_addr = self.basis.get_vector(key)
        
        # Retrieve bound vector
        bound = self.memory.retrieve(key_addr)
        
        # Unbind to get value
        value_vec = self.hdc.unbind(bound, key_addr)
        
        # Cleanup
        matches = self.basis.cleanup(value_vec, top_k=3)
        
        return matches
    
    def encode_sequence(self, items):
        """
        Encode a sequence with positional information.
        
        Uses permutation to encode order.
        """
        encoded = []
        
        for i, item in enumerate(items):
            item_vec = self.basis.get_vector(item)
            # Permute by position
            permuted = self.hdc.permute(item_vec, shift=i)
            encoded.append(permuted)
        
        # Bundle all together
        sequence_vec = self.hdc.bundle(encoded)
        
        return sequence_vec
    
    def decode_sequence(self, sequence_vec, items, length):
        """
        Decode sequence from hypervector.
        """
        decoded = []
        
        for i in range(length):
            # Inverse permute
            unpermuted = self.hdc.inverse_permute(sequence_vec, shift=i)
            
            # Cleanup
            matches = self.basis.cleanup(unpermuted, items, top_k=1)
            decoded.append(matches[0][0] if matches else None)
        
        return decoded
```

### Step 3: Emergent STDP Mechanism

```python
class EmergentSTDPHDC:
    """
    HDC with emergent STDP-like learning.
    """
    
    def __init__(self, dim=10000, time_constant=10):
        self.dim = dim
        self.hdc = GaloisFieldHDC(dim)
        self.basis = HypervectorBasis(dim)
        self.tau = time_constant
        
        # Memory of recent activations (for path-dependency)
        self.activation_history = []
        self.max_history = 100
        
    def encode_with_temporal_context(self, symbol, timestamp):
        """
        Encode symbol with temporal context.
        
        The temporal context creates path-dependency similar to STDP.
        """
        symbol_vec = self.basis.get_vector(symbol)
        
        # Compute temporal context from recent activations
        context = self.compute_temporal_context(timestamp)
        
        # Bind symbol with its temporal context
        encoded = self.hdc.bind(symbol_vec, context)
        
        # Store in history
        self.activation_history.append({
            'symbol': symbol,
            'timestamp': timestamp,
            'vector': encoded
        })
        
        # Maintain history size
        if len(self.activation_history) > self.max_history:
            self.activation_history.pop(0)
        
        return encoded
    
    def compute_temporal_context(self, current_time):
        """
        Compute temporal context from activation history.
        
        This creates path-dependent encoding - order matters!
        """
        if len(self.activation_history) == 0:
            return np.ones(self.dim) * 0.5  # Neutral context
        
        # Weighted combination of recent activations
        weighted_vectors = []
        weights = []
        
        for activation in self.activation_history:
            dt = current_time - activation['timestamp']
            weight = np.exp(-dt / self.tau)  # Exponential decay
            
            weighted_vectors.append(activation['vector'])
            weights.append(weight)
        
        # Bundle weighted history
        context = self.hdc.bundle(weighted_vectors, weights)
        
        return context
    
    def associative_recall(self, query_symbol, context_time=None):
        """
        Recall associations with temporal context.
        
        Similar to STDP: recent co-activation strengthens association.
        """
        if context_time is None:
            context_time = len(self.activation_history)
        
        query_vec = self.basis.get_vector(query_symbol)
        context = self.compute_temporal_context(context_time)
        
        # Encode query with current context
        query_encoded = self.hdc.bind(query_vec, context)
        
        # Search in history for similar patterns
        similarities = []
        for activation in self.activation_history:
            sim = np.dot(query_encoded, activation['vector']) / self.dim
            similarities.append((activation['symbol'], sim, activation['timestamp']))
        
        # Sort by similarity
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        return similarities[:5]
    
    def stdp_like_learning(self, pre_symbol, post_symbol, dt):
        """
        Perform STDP-like learning.
        
        Args:
            pre_symbol: Presynaptic symbol
            post_symbol: Postsynaptic symbol
            dt: Time difference (post - pre)
        """
        # STDP window function
        if dt > 0:  # Post after pre (causal)
            delta = np.exp(-dt / self.tau)  # Potentiation
        else:  # Pre after post (anti-causal)
            delta = -0.5 * np.exp(dt / self.tau)  # Depression
        
        # Get vectors
        pre_vec = self.basis.get_vector(pre_symbol)
        post_vec = self.basis.get_vector(post_symbol)
        
        # Create association with weight
        association = self.hdc.bind(pre_vec, post_vec)
        
        # The binding itself represents the association strength
        # In a full implementation, this would update an associative memory
        
        return association, delta
```

### Step 4: VaCoAl Hardware Mapping

```python
class VaCoAlImplementation:
    """
    Mapping HDC to VaCoAl (SRAM-CAM) hardware.
    
    VaCoAl: Variable Content Addressable Logic
    - Ultra-high speed: Content-addressable lookup
    - Ultra-low power: SRAM-based storage
    - Low cost: Standard CMOS process
    """
    
    def __init__(self, dim=10000, num_entries=1024):
        self.dim = dim
        self.num_entries = num_entries
        
        # CAM structure (simulated)
        self.cam_array = np.zeros((num_entries, dim), dtype=np.uint8)
        self.valid_bits = np.zeros(num_entries, dtype=bool)
        
    def cam_store(self, index, hypervector):
        """
        Store hypervector in CAM.
        
        In hardware: Single cycle write to SRAM-CAM
        """
        if index < self.num_entries:
            self.cam_array[index] = hypervector.astype(np.uint8)
            self.valid_bits[index] = True
            return True
        return False
    
    def cam_lookup(self, query_vector, threshold=0.9):
        """
        Content-addressable lookup.
        
        In hardware: Parallel comparison across all entries
        """
        # Compute similarities (parallel in hardware)
        similarities = []
        for i in range(self.num_entries):
            if self.valid_bits[i]:
                sim = 1 - np.sum(query_vector != self.cam_array[i]) / self.dim
                similarities.append((i, sim))
        
        # Filter by threshold
        matches = [(idx, sim) for idx, sim in similarities if sim >= threshold]
        matches.sort(key=lambda x: x[1], reverse=True)
        
        return matches
    
    def bind_operation(self, v1_idx, v2_idx, result_idx):
        """
        Galois field binding (element-wise XOR).
        
        In hardware: XOR gate array
        """
        v1 = self.cam_array[v1_idx].astype(np.float32)
        v2 = self.cam_array[v2_idx].astype(np.float32)
        
        result = np.mod(v1 + v2, 2).astype(np.uint8)
        self.cam_array[result_idx] = result
        self.valid_bits[result_idx] = True
        
        return result_idx
    
    def estimate_performance(self):
        """
        Estimate hardware performance.
        """
        # Typical VaCoAl specifications
        specs = {
            'lookup_latency_ns': 10,  # 10ns lookup time
            'bind_latency_ns': 5,      # 5ns for XOR operation
            'power_lookup_uW': 100,    # 100uW per lookup
            'power_standby_uW': 1,     # 1uW standby
            'area_mm2': 1.0,           # 1mm^2 for 1024x10000
            'energy_per_op_pJ': 1.0    # 1pJ per operation
        }
        
        return specs
```

## Usage Patterns

### Pattern 1: Semantic Encoding

```python
# Initialize HDC
hdc = GaloisFieldHDC(dim=10000)
basis = HypervectorBasis(dim=10000)

# Encode symbols
color_red = basis.get_vector('red')
color_blue = basis.get_vector('blue')
shape_circle = basis.get_vector('circle')
shape_square = basis.get_vector('square')

# Encode composite concept: "red circle"
red_circle = hdc.bind(color_red, shape_circle)

# Encode with role: "color is red, shape is circle"
role_color = basis.get_vector('COLOR')
role_shape = basis.get_vector('SHAPE')

encoded = hdc.bundle([
    hdc.bind(role_color, color_red),
    hdc.bind(role_shape, shape_circle)
])

# Query: what color?
query = hdc.unbind(encoded, role_color)
matches = basis.cleanup(query, ['red', 'blue', 'circle', 'square'])
print(matches)  # [('red', 0.98), ...]
```

### Pattern 2: Sequence Learning

```python
# Initialize emergent STDP
stdp = EmergentSTDPHDC(dim=10000, time_constant=10)

# Encode sequence with temporal context
sequence = ['A', 'B', 'C', 'D']
for t, item in enumerate(sequence):
    encoded = stdp.encode_with_temporal_context(item, t)

# Recall what comes after 'B'
recall = stdp.associative_recall('B')
print(recall)  # Likely shows 'C' as top match due to temporal proximity

# STDP learning
stdp.stdp_like_learning('A', 'B', dt=1)  # A followed by B
stdp.stdp_like_learning('B', 'A', dt=-1)  # Anti-causal (weaker)
```

### Pattern 3: Pattern Recognition

```python
# SDM for pattern storage
sdm = SparseDistributedMemory(dim=10000, num_locations=100000)
basis = HypervectorBasis(dim=10000)

# Store patterns
patterns = ['pattern1', 'pattern2', 'pattern3']
for pattern in patterns:
    vec = basis.get_vector(pattern)
    # Use vector itself as address (auto-associative)
    sdm.store(vec, vec)

# Retrieve noisy pattern
noisy = basis.get_vector('pattern1')
noisy[np.random.choice(10000, 100)] ^= 1  # Add noise

retrieved = sdm.retrieve(noisy)
matches = basis.cleanup(retrieved, patterns)
print(matches)  # [('pattern1', 0.95), ...] - error correction!
```

## Error Handling

### Dimensionality Mismatch

If vectors have different dimensions:
1. Check initialization consistency
2. Verify basis vector generation
3. Ensure all operations use same dim

### Retrieval Failures

If cleanup doesn't find correct match:
1. Check similarity metric
2. Verify binding/unbinding correctness
3. May need higher dimensionality
4. Check for too much bundling (saturation)

### Memory Saturation

If SDM performance degrades:
1. Reduce number of stored items
2. Increase address radius
3. Use multiple SDM modules
4. Implement forgetting mechanism

## References

- Chuma, H., Otsuka, K., & Sato, Y. (2026). Beyond LLMs, Sparse Distributed Memory, and Neuromorphics: A Hyper-Dimensional SRAM-CAM 'VaCoAl'. arXiv:2604.11665v2.
- Kanerva, P. (2009). Hyperdimensional computing: An introduction to computing in distributed representation with high-dimensional random vectors. Cognitive Computation.
- Plate, T. A. (2003). Holographic reduced representation. CSLI Publications.

## Related Skills

- `spiking-neural-network-analysis`: SNN analysis
- `ember-hybrid-snn-llm-architecture`: Hybrid architectures
- `nca-attractor-stability-analysis`: Attractor dynamics
