# Implementation: Adaptive Spiking Neurons (ASN)

## Base ASN Neuron

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class AdaptiveSpikingNeuron(nn.Module):
    """
    Adaptive Spiking Neuron (ASN) with trainable membrane dynamics
    and adaptive firing threshold.
    """
    
    def __init__(self, hidden_dim=64, tau_init=0.5, threshold_init=1.0,
                 adaptive_threshold=True, learn_leak=True):
        """
        Args:
            hidden_dim: Dimensionality of the membrane state
            tau_init: Initial leak/decay rate (learned if learn_leak=True)
            threshold_init: Initial firing threshold
            adaptive_threshold: Whether threshold adapts based on history
            learn_leak: Whether membrane decay rate is trainable
        """
        super().__init__()
        self.hidden_dim = hidden_dim
        self.adaptive_threshold = adaptive_threshold
        
        # Trainable membrane dynamics parameters
        if learn_leak:
            # Learnable decay rate (constrained to [0, 1] via sigmoid)
            self.logit_tau = nn.Parameter(torch.randn(hidden_dim) * 0.1)
        else:
            self.register_buffer('logit_tau', torch.log(torch.tensor(tau_init / (1 - tau_init))))
            
        # Membrane potential update MLP
        self.membrane_mlp = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim * 2),  # [u_prev, x]
            nn.ReLU(),
            nn.Linear(hidden_dim * 2, hidden_dim)
        )
        
        # Adaptive firing threshold
        if adaptive_threshold:
            self.threshold_base = nn.Parameter(torch.tensor(threshold_init))
            self.threshold_adapt = nn.Linear(hidden_dim, 1)  # Adapt based on spike history
        else:
            self.register_buffer('threshold_base', torch.tensor(threshold_init))
            self.threshold_adapt = None
            
        # State
        self.register_buffer('u', torch.zeros(hidden_dim))  # Membrane potential
        self.register_buffer('spike_history', torch.zeros(hidden_dim))  # For threshold adaptation
        
    @property
    def tau(self):
        """Get current decay rate (sigmoid-constrained)."""
        return torch.sigmoid(self.logit_tau)
    
    @property
    def threshold(self):
        """Get current adaptive threshold."""
        if self.adaptive_threshold and self.threshold_adapt is not None:
            adapt_term = self.threshold_adapt(self.spike_history).squeeze(-1)
            return self.threshold_base + adapt_term
        return self.threshold_base
    
    def reset(self, batch_size=None):
        """Reset neuron state."""
        shape = (batch_size, self.hidden_dim) if batch_size else (self.hidden_dim,)
        self.u = torch.zeros(shape, device=self.u.device)
        self.spike_history = torch.zeros(shape, device=self.spike_history.device)
        
    def forward(self, x):
        """
        Single step of ASN dynamics.
        
        Args:
            x: Input tensor [..., hidden_dim]
        Returns:
            spikes: Binary spike tensor [..., hidden_dim]
        """
        # Compute decay rate
        tau = self.tau
        
        # Trainable membrane potential update
        # f_θ(u(t-1), x(t)) — learned dynamics
        mem_input = torch.cat([self.u, x], dim=-1)
        u_update = self.membrane_mlp(mem_input)
        
        # Leaky integration with learned decay
        self.u = tau * self.u + (1 - tau) * u_update
        
        # Adaptive firing
        spikes = (self.u >= self.threshold.unsqueeze(-1)).float()
        
        # Update spike history for threshold adaptation
        self.spike_history = 0.9 * self.spike_history + 0.1 * spikes
        
        # Soft reset (partial) — trainable
        self.u = self.u * (1 - 0.8 * spikes)
        
        return spikes


class ASNCell(nn.Module):
    """ASN wrapped as a recurrent cell for sequential processing."""
    
    def __init__(self, input_dim, hidden_dim, **kwargs):
        super().__init__()
        self.input_proj = nn.Linear(input_dim, hidden_dim)
        self.neuron = AdaptiveSpikingNeuron(hidden_dim, **kwargs)
        self.hidden_dim = hidden_dim
        
    def forward(self, x, reset=False):
        if reset:
            self.neuron.reset()
        x_proj = self.input_proj(x)
        return self.neuron(x_proj)
```

## NASN — Normalized Adaptive Spiking Neuron

```python
class NormalizedAdaptiveSpikingNeuron(AdaptiveSpikingNeuron):
    """
    NASN: ASN with normalization for stable training.
    Adds layer normalization to membrane potential before
    threshold comparison and update.
    """
    
    def __init__(self, hidden_dim=64, norm_type='layer', **kwargs):
        """
        Args:
            hidden_dim: Dimensionality
            norm_type: 'layer' or 'batch' normalization
            **kwargs: Passed to AdaptiveSpikingNeuron
        """
        super().__init__(hidden_dim, **kwargs)
        
        if norm_type == 'layer':
            self.norm = nn.LayerNorm(hidden_dim)
        elif norm_type == 'batch':
            self.norm = nn.BatchNorm1d(hidden_dim)
        else:
            raise ValueError(f"Unknown norm_type: {norm_type}")
            
    def forward(self, x):
        """Forward pass with normalization."""
        tau = self.tau
        
        # Trainable membrane potential update
        mem_input = torch.cat([self.u, x], dim=-1)
        u_update = self.membrane_mlp(mem_input)
        
        # Normalize membrane potential before integration
        u_normed = self.norm(self.u)
        
        # Leaky integration
        self.u = tau * u_normed + (1 - tau) * u_update
        
        # Normalize before threshold comparison
        u_for_threshold = self.norm(self.u)
        spikes = (u_for_threshold >= self.threshold.unsqueeze(-1)).float()
        
        # Update spike history
        self.spike_history = 0.9 * self.spike_history + 0.1 * spikes
        
        # Soft reset
        self.u = self.u * (1 - 0.8 * spikes)
        
        return spikes
```

## Integer Training + Spike Inference Pipeline

```python
class IntegerTrainingSNN(nn.Module):
    """
    SNN using integer training with spike inference.
    During training: integer-valued representations for efficiency.
    During inference: standard spike-based representation.
    """
    
    def __init__(self, n_layers=4, input_dim=64, hidden_dim=128, 
                 output_dim=10, neuron_type='asn', 
                 training_mode='integer', **neuron_kwargs):
        """
        Args:
            training_mode: 'integer' or 'spike'
        """
        super().__init__()
        self.training_mode = training_mode
        self.n_layers = n_layers
        self.quantize_bits = 8  # 8-bit integer quantization
        
        # Build layers
        self.layers = nn.ModuleList()
        
        for i in range(n_layers):
            in_dim = input_dim if i == 0 else hidden_dim
            out_dim = output_dim if i == n_layers - 1 else hidden_dim
            
            in_proj = nn.Linear(in_dim, hidden_dim)
            
            if neuron_type == 'asn':
                neuron = AdaptiveSpikingNeuron(hidden_dim, **neuron_kwargs)
            elif neuron_type == 'nasn':
                neuron = NormalizedAdaptiveSpikingNeuron(hidden_dim, **neuron_kwargs)
            else:
                raise ValueError(f"Unknown neuron_type: {neuron_type}")
                
            out_proj = nn.Linear(hidden_dim, out_dim) if i == n_layers - 1 else None
            
            self.layers.append(nn.ModuleDict({
                'in_proj': in_proj,
                'neuron': neuron,
                'out_proj': out_proj
            }))
            
        # Output pooling
        self.output_pool = 'sum'  # Sum spikes over time
            
    def _quantize(self, x):
        """Quantize to integer representation."""
        scale = 2 ** (self.quantize_bits - 1)
        x_int = torch.round(x * scale).clamp(-scale, scale - 1)
        return x_int / scale  # Dequantize for gradient flow
    
    def _spikify(self, x):
        """Convert continuous values to binary spikes."""
        return (x > 0).float()
    
    def forward(self, input_sequence, time_steps=None):
        """
        Forward pass through the SNN.
        
        Args:
            input_sequence: [..., time_steps, input_dim]
            time_steps: Number of time steps (optional)
        """
        if time_steps is None:
            time_steps = input_sequence.size(-2)
            
        # Reset all neurons
        for layer in self.layers:
            layer['neuron'].reset()
            
        # Collect output spikes
        all_outputs = []
        
        for t in range(time_steps):
            # Get input at time t
            if input_sequence.dim() == 3:
                x = input_sequence[:, t, :]  # [batch, input_dim]
            else:
                x = input_sequence[t]  # [input_dim]
                
            # Forward through layers
            for i, layer in enumerate(self.layers):
                # Project input
                x = layer['in_proj'](x)
                
                # Apply neuron dynamics
                spikes = layer['neuron'](x)
                
                # Apply training mode conversion
                if self.training:
                    if self.training_mode == 'integer':
                        # Integer quantization during training
                        x = self._quantize(spikes)
                    else:
                        # Direct spike representation
                        x = spikes
                else:
                    # Inference: always use spikes
                    x = self._spikify(spikes)
                    
                # Output projection for last layer
                if layer['out_proj'] is not None:
                    x = layer['out_proj'](x)
                    
            all_outputs.append(x)
            
        # Pool outputs over time
        outputs = torch.stack(all_outputs, dim=0)
        
        if self.output_pool == 'sum':
            return outputs.sum(dim=0)  # [batch, output_dim]
        elif self.output_pool == 'mean':
            return outputs.mean(dim=0)
        elif self.output_pool == 'max':
            return outputs.max(dim=0)[0]
        elif self.output_pool == 'last':
            return outputs[-1]
        else:
            return outputs


class HybridTrainingPipeline:
    """
    Manages the integer training → spike inference pipeline.
    """
    
    def __init__(self, model, lr=1e-3, quantize_bits=8):
        self.model = model
        self.lr = lr
        self.quantize_bits = quantize_bits
        
    def train_integer(self, dataloader, n_epochs=50):
        """Train with integer quantization."""
        self.model.training_mode = 'integer'
        optimizer = torch.optim.Adam(self.model.parameters(), lr=self.lr)
        criterion = nn.CrossEntropyLoss()
        
        for epoch in range(n_epochs):
            self.model.train()
            total_loss = 0
            correct = 0
            total = 0
            
            for batch_x, batch_y in dataloader:
                optimizer.zero_grad()
                
                logits = self.model(batch_x)
                loss = criterion(logits, batch_y)
                
                loss.backward()
                optimizer.step()
                
                total_loss += loss.item()
                correct += (logits.argmax(-1) == batch_y).sum().item()
                total += batch_y.size(0)
                
            acc = correct / total
            avg_loss = total_loss / len(dataloader)
            print(f"Epoch {epoch}: loss={avg_loss:.4f}, acc={acc:.4f}")
            
        return self.model
    
    def evaluate_spike(self, dataloader):
        """Evaluate with spike inference."""
        self.model.eval()
        self.model.training_mode = 'spike'
        
        correct = 0
        total = 0
        
        with torch.no_grad():
            for batch_x, batch_y in dataloader:
                logits = self.model(batch_x)
                correct += (logits.argmax(-1) == batch_y).sum().item()
                total += batch_y.size(0)
                
        return correct / total
    
    def full_pipeline(self, train_loader, val_loader, n_epochs=50):
        """Run complete integer train → spike eval pipeline."""
        print("=== Phase 1: Integer Training ===")
        self.train_integer(train_loader, n_epochs)
        
        print("\n=== Phase 2: Spike Inference Evaluation ===")
        spike_acc = self.evaluate_spike(val_loader)
        print(f"Spike inference accuracy: {spike_acc:.4f}")
        
        return spike_acc
```

## Multi-Modal Integration

```python
class VisionASNSNN(nn.Module):
    """ASN-based SNN for vision tasks."""
    
    def __init__(self, img_channels=3, img_size=32, hidden_dim=128, 
                 n_classes=10, n_layers=4, **neuron_kwargs):
        super().__init__()
        
        # Image → spike encoding (convolutional)
        self.conv_encoder = nn.Sequential(
            nn.Conv2d(img_channels, 64, 3, padding=1),
            nn.BatchNorm2d(64),
            nn.Conv2d(64, hidden_dim, 3, padding=1),
            nn.Flatten()
        )
        
        self.fc_input = nn.Linear(hidden_dim * img_size * img_size // 4, hidden_dim)
        
        # ASN layers
        self.asn_layers = nn.ModuleList([
            AdaptiveSpikingNeuron(hidden_dim, **neuron_kwargs)
            for _ in range(n_layers)
        ])
        
        self.readout = nn.Linear(hidden_dim, n_classes)
        self.hidden_dim = hidden_dim
        
    def encode_image(self, x):
        """Convert image to spike train."""
        # Conv encoding → spike rate coding
        features = self.conv_encoder(x)
        return self.fc_input(features)
    
    def forward(self, images, time_steps=20):
        batch_size = images.size(0)
        
        # Reset neurons
        for asn in self.asn_layers:
            asn.reset(batch_size)
            
        # Encode input
        encoded = self.encode_image(images)
        
        # Process through time
        spike_counts = torch.zeros(batch_size, self.hidden_dim, device=images.device)
        
        for t in range(time_steps):
            x = encoded
            for asn in self.asn_layers:
                spikes = asn(x)
                x = spikes
                
            spike_counts += x
            
        return self.readout(spike_counts / time_steps)


class LanguageASNSNN(nn.Module):
    """ASN-based SNN for language/sequence tasks."""
    
    def __init__(self, vocab_size=10000, embed_dim=64, hidden_dim=128,
                 n_classes=2, n_layers=3, **neuron_kwargs):
        super().__init__()
        
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        
        # ASN recurrent layers
        self.asn_layers = nn.ModuleList([
            ASNCell(embed_dim if i == 0 else hidden_dim, hidden_dim, **neuron_kwargs)
            for i in range(n_layers)
        ])
        
        self.readout = nn.Linear(hidden_dim, n_classes)
        
    def forward(self, token_ids, time_steps=None):
        """
        Args:
            token_ids: [batch, seq_len]
        """
        batch_size, seq_len = token_ids.shape
        
        if time_steps is None:
            time_steps = seq_len
            
        # Reset neurons
        for asn in self.asn_layers:
            asn.neuron.reset(batch_size)
            
        # Embed tokens
        embeddings = self.embedding(token_ids)  # [batch, seq_len, embed_dim]
        
        # Process sequence through ASN layers
        final_spikes = None
        spike_accum = torch.zeros(batch_size, 128, device=token_ids.device)  # hidden_dim
        
        for t in range(time_steps):
            x = embeddings[:, t, :]  # [batch, embed_dim]
            
            for asn in self.asn_layers:
                x = asn(x)
                spike_accum += x
                
            final_spikes = x
            
        # Readout from accumulated spikes
        return self.readout(spike_accum / time_steps)
```

## Training Utilities

```python
def create_vision_model(img_size=32, n_classes=10, neuron_type='asn', **kwargs):
    """Create ASN-based vision model."""
    if neuron_type == 'asn':
        return VisionASNSNN(img_size=img_size, n_classes=n_classes, **kwargs)
    elif neuron_type == 'nasn':
        # Use normalized variant
        model = VisionASNSNN(img_size=img_size, n_classes=n_classes, **kwargs)
        # Replace neurons with NASN
        for i, asn in enumerate(model.asn_layers):
            model.asn_layers[i] = NormalizedAdaptiveSpikingNeuron(
                asn.hidden_dim, norm_type='layer', **kwargs
            )
        return model
        

def create_language_model(vocab_size=10000, n_classes=2, neuron_type='asn', **kwargs):
    """Create ASN-based language model."""
    if neuron_type == 'asn':
        return LanguageASNSNN(vocab_size=vocab_size, n_classes=n_classes, **kwargs)
    elif neuron_type == 'nasn':
        model = LanguageASNSNN(vocab_size=vocab_size, n_classes=n_classes, **kwargs)
        for i, asn in enumerate(model.asn_layers):
            model.asn_layers[i].neuron = NormalizedAdaptiveSpikingNeuron(
                asn.neuron.hidden_dim, norm_type='layer', **kwargs
            )
        return model


def train_model(model, dataloader, n_epochs=50, lr=1e-3, device='cuda'):
    """Standard training loop for ASN models."""
    model = model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, n_epochs)
    criterion = nn.CrossEntropyLoss()
    
    best_acc = 0
    
    for epoch in range(n_epochs):
        model.train()
        total_loss = 0
        correct = 0
        total = 0
        
        for batch_x, batch_y in dataloader:
            batch_x, batch_y = batch_x.to(device), batch_y.to(device)
            
            optimizer.zero_grad()
            logits = model(batch_x)
            loss = criterion(logits, batch_y)
            
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
            
            total_loss += loss.item()
            correct += (logits.argmax(-1) == batch_y).sum().item()
            total += batch_y.size(0)
            
        scheduler.step()
        
        acc = correct / total
        avg_loss = total_loss / len(dataloader)
        
        if acc > best_acc:
            best_acc = acc
            
        if epoch % 5 == 0:
            print(f"Epoch {epoch}: loss={avg_loss:.4f}, acc={acc:.4f}, best={best_acc:.4f}")
            
    return model, best_acc
```
