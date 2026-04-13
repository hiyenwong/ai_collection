---
name: auto-configured-networks-forecasting
description: "Auto-configured neural networks for multi-scale multi-output time-series forecasting. Automated framework for co-designing preprocessing, architecture, and hyperparameters to generate Pareto-optimal forecasting models balancing prediction error and model complexity. Use for: industrial time-series forecasting, multi-source signal processing, autoML for forecasting, model architecture search. Activation: auto-configured forecasting, multi-scale time series, multi-output regression, MS-BCNN, Pareto optimization, industrial forecasting."
---

# Auto-Configured Networks for Multi-Scale Multi-Output Time-Series Forecasting

Automated framework for generating deployable Pareto sets of forecasting models that balance prediction error and model complexity for industrial multi-source time-series data.

## Overview

Industrial forecasting involves handling multi-source asynchronous signals with multiple output targets, requiring explicit trade-offs between prediction accuracy and computational complexity. This skill implements an auto-configuration framework that systematically co-designs preprocessing, architecture, and hyperparameters to produce Pareto-optimal forecasting models.

**Key Features:**
- Automated co-design of preprocessing, architecture, and hyperparameters
- Multi-Scale Bi-Branch CNN (MS-BCNN) for capturing local and long-term trends
- Pareto-optimal model generation balancing error vs complexity
- Budget-limited training-based evaluation support

## Architecture: Multi-Scale Bi-Branch CNN (MS-BCNN)

### Design Philosophy

The MS-BCNN architecture addresses the challenge of multi-scale temporal patterns in industrial signals:

```
┌─────────────────────────────────────────────────────────────┐
│              MS-BCNN ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Input: Multi-source asynchronous time-series signals       │
│                    │                                        │
│        ┌───────────┴───────────┐                           │
│        │                       │                           │
│   ┌────▼────┐            ┌────▼────┐                      │
│   │ Short   │            │ Long    │                      │
│   │ Kernel  │            │ Kernel  │                      │
│   │ Branch  │            │ Branch  │                      │
│   │ (Local  │            │ (Trend) │                      │
│   │ Fluct.) │            │         │                      │
│   └────┬────┘            └────┬────┘                      │
│        │                       │                           │
│        └───────────┬───────────┘                           │
│                    │                                        │
│              Fusion Layer                                   │
│                    │                                        │
│         Multi-Output Regression                             │
│                    │                                        │
│              Forecast Outputs                               │
└─────────────────────────────────────────────────────────────┘
```

### Component Details

**Short-Kernel Branch:**
- Captures local fluctuations and short-term dynamics
- Uses small convolutional kernels (e.g., kernel size 3-5)
- High temporal resolution for rapid signal changes

**Long-Kernel Branch:**
- Captures long-term trends and seasonal patterns
- Uses larger convolutional kernels (e.g., kernel size 15-31)
- Aggregates information over extended time windows

**Fusion Layer:**
- Combines representations from both branches
- Learnable weighting for adaptive branch importance
- Enables dynamic balancing of local vs global features

## Auto-Configuration Framework

### Framework Overview

```
┌─────────────────────────────────────────────────────────────┐
│           AUTO-CONFIGURATION PIPELINE                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │ Preprocess  │───→│  Architect  │───→│ Hyperparam  │     │
│  │   Config    │    │   Search    │    │   Optimize  │     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
│         │                  │                  │             │
│         ▼                  ▼                  ▼             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Pareto Front Generation                 │   │
│  │  • Model A: Low Error, High Complexity              │   │
│  │  • Model B: Balanced Error/Complexity               │   │
│  │  • Model C: Higher Error, Low Complexity            │   │
│  └─────────────────────────────────────────────────────┘   │
│                          │                                  │
│                          ▼                                  │
│                 Deployable Model Set                        │
└─────────────────────────────────────────────────────────────┘
```

### Configuration Space

**Preprocessing Configuration:**
- Signal alignment strategies (synchronous/asynchronous)
- Normalization methods (z-score, min-max, robust)
- Windowing parameters (input/output horizons)
- Missing value handling strategies

**Architecture Configuration:**
- Branch configurations (short/long kernel sizes)
- Channel dimensions per branch
- Fusion mechanism type (concatenation, attention, gating)
- Depth of convolutional stacks

**Hyperparameter Configuration:**
- Learning rate schedules
- Batch sizes
- Regularization strengths (dropout, weight decay)
- Early stopping criteria

## Implementation

### Step 1: Data Preprocessing

```python
import numpy as np
from sklearn.preprocessing import StandardScaler, RobustScaler

class MultiSourcePreprocessor:
    """
    Preprocessor for multi-source asynchronous time-series signals.
    """
    def __init__(self, alignment_strategy='interpolate', normalization='robust'):
        self.alignment_strategy = alignment_strategy
        self.normalization = normalization
        self.scalers = {}
    
    def align_signals(self, signals, timestamps, target_timestamps):
        """
        Align asynchronous signals to common timestamps.
        
        Args:
            signals: Dict of {source_name: values_array}
            timestamps: Dict of {source_name: timestamps_array}
            target_timestamps: Common timestamp array
        
        Returns:
            Aligned signals as numpy array [n_samples, n_sources]
        """
        from scipy.interpolate import interp1d
        
        aligned = []
        for source_name in signals.keys():
            f = interp1d(
                timestamps[source_name], 
                signals[source_name],
                kind='linear',
                fill_value='extrapolate'
            )
            aligned.append(f(target_timestamps))
        
        return np.column_stack(aligned)
    
    def fit_transform(self, data):
        """
        Fit scalers and transform data.
        
        Args:
            data: numpy array [n_samples, n_features]
        
        Returns:
            Normalized data
        """
        if self.normalization == 'standard':
            scaler = StandardScaler()
        elif self.normalization == 'robust':
            scaler = RobustScaler()
        else:
            raise ValueError(f"Unknown normalization: {self.normalization}")
        
        return scaler.fit_transform(data)
```

### Step 2: MS-BCNN Model

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class MSBCNN(nn.Module):
    """
    Multi-Scale Bi-Branch Convolutional Neural Network.
    
    Captures both local fluctuations and long-term trends
    through parallel short and long kernel branches.
    """
    def __init__(self, 
                 input_dim,
                 output_dim,
                 short_kernel=3,
                 long_kernel=15,
                 short_channels=64,
                 long_channels=64,
                 fusion_type='attention'):
        super().__init__()
        
        self.input_dim = input_dim
        self.output_dim = output_dim
        
        # Short-kernel branch (local fluctuations)
        self.short_branch = nn.Sequential(
            nn.Conv1d(input_dim, short_channels, short_kernel, padding=short_kernel//2),
            nn.ReLU(),
            nn.Conv1d(short_channels, short_channels, short_kernel, padding=short_kernel//2),
            nn.ReLU()
        )
        
        # Long-kernel branch (long-term trends)
        self.long_branch = nn.Sequential(
            nn.Conv1d(input_dim, long_channels, long_kernel, padding=long_kernel//2),
            nn.ReLU(),
            nn.Conv1d(long_channels, long_channels, long_kernel, padding=long_kernel//2),
            nn.ReLU()
        )
        
        # Fusion mechanism
        total_channels = short_channels + long_channels
        if fusion_type == 'attention':
            self.fusion = nn.Sequential(
                nn.Linear(total_channels, total_channels // 2),
                nn.ReLU(),
                nn.Linear(total_channels // 2, 2),
                nn.Softmax(dim=-1)
            )
        else:
            self.fusion = None
        
        # Output layers
        self.output_layer = nn.Sequential(
            nn.Linear(total_channels, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, output_dim)
        )
    
    def forward(self, x):
        """
        Forward pass.
        
        Args:
            x: Input tensor [batch, seq_len, features]
        
        Returns:
            Output predictions [batch, output_dim]
        """
        # Transpose for Conv1d: [batch, features, seq_len]
        x = x.transpose(1, 2)
        
        # Extract features from both branches
        short_features = self.short_branch(x)  # [batch, short_channels, seq_len]
        long_features = self.long_branch(x)    # [batch, long_channels, seq_len]
        
        # Global average pooling
        short_pooled = short_features.mean(dim=2)  # [batch, short_channels]
        long_pooled = long_features.mean(dim=2)    # [batch, long_channels]
        
        # Concatenate
        combined = torch.cat([short_pooled, long_pooled], dim=1)
        
        # Fusion (if using attention)
        if self.fusion:
            weights = self.fusion(combined)  # [batch, 2]
            short_weight = weights[:, 0:1]
            long_weight = weights[:, 1:2]
            combined = torch.cat([
                short_pooled * short_weight,
                long_pooled * long_weight
            ], dim=1)
        
        # Output prediction
        output = self.output_layer(combined)
        return output
```

### Step 3: Pareto Optimization

```python
from typing import List, Dict, Tuple
import numpy as np

class ParetoOptimizer:
    """
    Generate Pareto-optimal model configurations balancing
    prediction error and model complexity.
    """
    def __init__(self, error_weight=1.0, complexity_weight=1.0):
        self.error_weight = error_weight
        self.complexity_weight = complexity_weight
    
    def compute_complexity(self, model_config: Dict) -> float:
        """
        Estimate model complexity based on configuration.
        
        Args:
            model_config: Dictionary with architecture parameters
        
        Returns:
            Complexity score (FLOPs or parameter count proxy)
        """
        short_channels = model_config.get('short_channels', 64)
        long_channels = model_config.get('long_channels', 64)
        short_kernel = model_config.get('short_kernel', 3)
        long_kernel = model_config.get('long_kernel', 15)
        
        # Proxy for computational complexity
        complexity = (
            short_channels * short_kernel +
            long_channels * long_kernel
        )
        return complexity
    
    def is_pareto_optimal(self, point: Tuple[float, float], 
                          points: List[Tuple[float, float]]) -> bool:
        """
        Check if a point is Pareto optimal.
        
        Args:
            point: (error, complexity) tuple
            points: List of all evaluated points
        
        Returns:
            True if point is on Pareto front
        """
        error, complexity = point
        for other_error, other_complexity in points:
            if other_error <= error and other_complexity <= complexity:
                if other_error < error or other_complexity < complexity:
                    return False
        return True
    
    def select_pareto_set(self, 
                          configs: List[Dict],
                          errors: List[float]) -> List[Dict]:
        """
        Select Pareto-optimal configurations.
        
        Args:
            configs: List of model configurations
            errors: List of validation errors for each config
        
        Returns:
            List of Pareto-optimal configurations
        """
        points = []
        for config, error in zip(configs, errors):
            complexity = self.compute_complexity(config)
            points.append((error, complexity, config))
        
        # Find Pareto front
        pareto_configs = []
        for i, (error, complexity, config) in enumerate(points):
            point = (error, complexity)
            other_points = [(p[0], p[1]) for j, p in enumerate(points) if j != i]
            
            if self.is_pareto_optimal(point, other_points):
                pareto_configs.append(config)
        
        return pareto_configs
```

### Step 4: Complete Training Pipeline

```python
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

class AutoConfigTrainer:
    """
    Complete training pipeline for auto-configured forecasting.
    """
    def __init__(self, config_space, budget_epochs=50):
        self.config_space = config_space
        self.budget_epochs = budget_epochs
    
    def train_model(self, model, train_loader, val_loader, epochs):
        """Train a single model configuration."""
        criterion = nn.MSELoss()
        optimizer = optim.Adam(model.parameters(), lr=1e-3)
        scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=5)
        
        best_val_loss = float('inf')
        
        for epoch in range(epochs):
            # Training
            model.train()
            train_loss = 0
            for batch_x, batch_y in train_loader:
                optimizer.zero_grad()
                outputs = model(batch_x)
                loss = criterion(outputs, batch_y)
                loss.backward()
                optimizer.step()
                train_loss += loss.item()
            
            # Validation
            model.eval()
            val_loss = 0
            with torch.no_grad():
                for batch_x, batch_y in val_loader:
                    outputs = model(batch_x)
                    loss = criterion(outputs, batch_y)
                    val_loss += loss.item()
            
            val_loss = val_loss / len(val_loader)
            scheduler.step(val_loss)
            
            if val_loss < best_val_loss:
                best_val_loss = val_loss
        
        return best_val_loss
    
    def search(self, X_train, y_train, X_val, y_val, n_configs=20):
        """
        Search for Pareto-optimal configurations.
        
        Args:
            X_train, y_train: Training data
            X_val, y_val: Validation data
            n_configs: Number of configurations to evaluate
        
        Returns:
            Pareto-optimal model set
        """
        train_loader = DataLoader(
            TensorDataset(torch.FloatTensor(X_train), torch.FloatTensor(y_train)),
            batch_size=32, shuffle=True
        )
        val_loader = DataLoader(
            TensorDataset(torch.FloatTensor(X_val), torch.FloatTensor(y_val)),
            batch_size=32
        )
        
        configs = []
        errors = []
        
        # Sample configurations
        for i in range(n_configs):
            config = self.sample_config()
            
            # Build and train model
            model = MSBCNN(
                input_dim=X_train.shape[2],
                output_dim=y_train.shape[1],
                **config
            )
            
            val_error = self.train_model(
                model, train_loader, val_loader, 
                epochs=self.budget_epochs
            )
            
            configs.append(config)
            errors.append(val_error)
        
        # Select Pareto-optimal set
        optimizer = ParetoOptimizer()
        pareto_set = optimizer.select_pareto_set(configs, errors)
        
        return pareto_set
    
    def sample_config(self):
        """Sample a random configuration from the search space."""
        return {
            'short_kernel': np.random.choice([3, 5, 7]),
            'long_kernel': np.random.choice([15, 21, 31]),
            'short_channels': np.random.choice([32, 64, 128]),
            'long_channels': np.random.choice([32, 64, 128]),
            'fusion_type': np.random.choice(['concat', 'attention'])
        }
```

## Usage Patterns

### Pattern 1: Industrial Equipment Forecasting

```python
# Load multi-source sensor data
sensor_data = load_equipment_sensors()  # Temperature, pressure, vibration, etc.

# Preprocess
preprocessor = MultiSourcePreprocessor(
    alignment_strategy='interpolate',
    normalization='robust'
)
X_aligned = preprocessor.align_signals(
    sensor_data['values'],
    sensor_data['timestamps'],
    target_timestamps=common_timestamps
)
X_normalized = preprocessor.fit_transform(X_aligned)

# Create sequences for forecasting
X_seq, y_seq = create_sequences(X_normalized, input_len=100, output_len=10)

# Search for Pareto-optimal models
trainer = AutoConfigTrainer(budget_epochs=50)
pareto_models = trainer.search(
    X_seq['train'], y_seq['train'],
    X_seq['val'], y_seq['val'],
    n_configs=30
)

# Deploy selected model
selected_model = pareto_models[1]  # Balanced option
```

### Pattern 2: Energy Demand Prediction

```python
# Multi-output: predict demand for multiple zones
zones = ['zone_a', 'zone_b', 'zone_c']
features = ['temperature', 'humidity', 'hour', 'day_of_week', 'holiday']

# Configure for energy forecasting
config = {
    'short_kernel': 5,    # Capture hourly patterns
    'long_kernel': 24*7,  # Capture weekly patterns
    'short_channels': 128,
    'long_channels': 128,
    'fusion_type': 'attention'
}

model = MSBCNN(
    input_dim=len(features),
    output_dim=len(zones),
    **config
)
```

## Best Practices

### Preprocessing Guidelines

1. **Alignment Strategy:**
   - Use interpolation for regularly sampled but asynchronous signals
   - Use resampling for irregularly sampled data
   - Consider time-lag compensation for causal relationships

2. **Normalization:**
   - Use RobustScaler for data with outliers
   - Use StandardScaler for normally distributed data
   - Fit on training data only, transform all sets

### Architecture Guidelines

1. **Kernel Size Selection:**
   - Short kernel: 3-7 for high-frequency signals
   - Long kernel: 15-31+ for seasonal/trend patterns
   - Ratio of long/short should match dominant frequency ratio

2. **Channel Allocation:**
   - Equal channels for balanced local/global importance
   - Increase channels for complex multi-source data
   - Consider computational constraints

### Training Guidelines

1. **Budget Allocation:**
   - Start with 50 epochs for initial search
   - Increase to 100+ for final selected models
   - Use early stopping with patience=5-10

2. **Validation Strategy:**
   - Use temporal split (not random) for time-series
   - Reserve recent data for testing
   - Consider walk-forward validation

## References

- Zha et al. (2026): "Auto-Configured Networks for Multi-Scale Multi-Output Time-Series Forecasting", arXiv:2604.07610

## Related Skills

- `discounted-mpc-robust-control`: Robust control for uncertain systems
- `system-resilience-design-patterns`: System resilience patterns
- `energy-based-neurocomputation`: Energy-based dynamical models

## Activation Keywords

- auto-configured forecasting
- multi-scale time series
- multi-output regression
- MS-BCNN
- Pareto optimization
- industrial forecasting
- automated model search
- time-series autoML


## Tools Used

- `exec`
- `read`
- `write`


## Instructions for Agents

1. **理解需求**：分析用户请求的具体场景
2. **选择方法**：根据上下文选择合适的技术方案
3. **执行操作**：按照技能描述实施具体步骤
4. **验证结果**：检查结果是否符合预期


## Examples

### Example 1: Basic Usage

**User:** 请帮我应用此技能

**Agent:** 我将按照标准流程执行...

### Example 2: Advanced Usage

**User:** 有更复杂的场景需要处理

**Agent:** 针对复杂场景，我将采用以下策略...
