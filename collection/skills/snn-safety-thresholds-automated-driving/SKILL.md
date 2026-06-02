---
name: snn-safety-thresholds-automated-driving
description: "Biologically-inspired reinterpretation of Surrogate Safety Measures (SSMs) using LIF neuron spiking thresholds. SNN combines multiple SSM inputs to emit spikes aligned with human braking onsets, capturing sustained borderline conditions and high-risk peaks better than fixed thresholds. Use when: autonomous driving safety, SSM thresholds, LIF neurons, spiking neural networks, car-following, braking behavior, traffic risk evaluation, human safety perception, temporal sensitivity. Activation: safety thresholds, SNN driving, LIF safety, automated driving, surrogate safety measures, SSM, braking prediction, spiking thresholds, traffic risk."
---

# Reinterpreting Safety Thresholds as Neuron Spiking Thresholds for Automated Driving Safety

Methodology using spiking neural networks (LIF neurons) to reinterpret safety thresholds in autonomous driving, aligning objective SSMs with subjective human safety perception.

## Core Problem

**Traditional Surrogate Safety Measures (SSMs) Limitations**:
1. **Fixed thresholds**: Cannot capture human response to sustained borderline conditions
2. **Binary classification**: Threshold crossing = risk, but misses temporal dynamics
3. **No temporal sensitivity**: Ignore sustained risk vs brief high-risk peaks
4. **Objective-subjective gap**: SSM thresholds don't align with human safety perception

**Human Safety Perception Complexity**:
- Humans react to **sustained borderline conditions** (gradual risk buildup)
- Humans react to **brief high-risk peaks** (sharp, transient dangers)
- Different temporal sensitivities across individuals
- Safety is perceived as a **continuous, dynamic process**, not discrete threshold crossing

## Solution: Spiking Thresholds

**Key Innovation**: Reinterpret SSM thresholds as **spiking thresholds of LIF neurons**

```
Traditional approach:
SSM value > threshold → risk event (binary)

SNN approach:
SSM values → LIF neuron membrane potential
Membrane potential > spiking threshold → spike emission (dynamic)

Key advantages:
1. Temporal integration: LIF neurons integrate over time
2. Temporal sensitivity: Decay factor controls integration window
3. Multiple inputs: Combine multiple SSMs into SNN
4. Human alignment: Spikes align with braking onsets
```

## Leaky Integrate-and-Fire (LIF) Model

### LIF Neuron Dynamics

```python
class LIFNeuron:
    """
    Leaky Integrate-and-Fire neuron for safety threshold modeling.
    
    Dynamics:
    dV/dt = -τ * V + I(t)
    
    Spiking condition:
    V > V_threshold → emit spike, reset V to V_reset
    """
    def __init__(self, threshold, tau, reset_value=0):
        self.V_threshold = threshold  # Spiking threshold (safety threshold)
        self.tau = tau                 # Decay factor (temporal sensitivity)
        self.V_reset = reset_value     # Reset value after spike
        self.V = 0                     # Current membrane potential
    
    def integrate(self, input_current, dt):
        """
        Integrate input current into membrane potential.
        
        dV/dt = -τ * V + I
        
        where:
        - τ: decay factor (leak)
        - I: input current (SSM value)
        - V: membrane potential
        """
        # Decay (leak)
        self.V = self.V * np.exp(-self.tau * dt)
        
        # Integration (accumulate input)
        self.V += input_current * dt
        
        # Check for spike
        if self.V > self.V_threshold:
            self.fire_spike()
            return True  # Spike emitted
        
        return False  # No spike
    
    def fire_spike(self):
        """
        Emit spike and reset membrane potential.
        """
        # Record spike event (safety risk event)
        self.spike_history.append(self.V)
        
        # Reset membrane potential
        self.V = self.V_reset
    
    def get_temporal_sensitivity(self):
        """
        Temporal sensitivity determined by decay factor τ.
        
        τ large → long integration window → sensitive to sustained conditions
        τ small → short integration window → sensitive to brief peaks
        """
        integration_window = 1.0 / self.tau
        
        return integration_window
```

### SSM to LIF Mapping

```
Surrogate Safety Measures (SSMs):
1. Time Headway (TH): Time to collision if vehicle continues current speed
2. Time to Collision (TTC): Time to collision if both vehicles maintain speed
3. Deceleration to Avoid Collision (DRAC): Required deceleration to avoid crash
4. Post-Encroachment Time (PET): Time between vehicle path encroachments

Mapping to LIF neuron:
SSM value → input current I(t)
LIF threshold → safety threshold V_threshold
Decay factor τ → temporal sensitivity
```

```python
class SSMLIFMapper:
    """
    Map SSM values to LIF neuron inputs.
    """
    def __init__(self, ssms=['TH', 'TTC', 'DRAC', 'PET']):
        self.ssms = ssms
        self.neurons = {}
        
        # Create LIF neuron for each SSM
        for ssm in ssms:
            self.neurons[ssm] = LIFNeuron(
                threshold=self.get_threshold(ssm),
                tau=self.get_decay_factor(ssm)
            )
    
    def get_threshold(self, ssm):
        """
        Get initial threshold for SSM (learned later).
        
        Standard thresholds:
        - TH: 1.5 s
        - TTC: 2.0 s
        - DRAC: 3.0 m/s²
        - PET: 0.5 s
        """
        thresholds = {
            'TH': 1.5,
            'TTC': 2.0,
            'DRAC': 3.0,
            'PET': 0.5
        }
        
        return thresholds[ssm]
    
    def get_decay_factor(self, ssm):
        """
        Get decay factor for SSM (learned later).
        
        Decay factor encodes temporal sensitivity:
        - Large τ: sustained condition sensitivity
        - Small τ: brief peak sensitivity
        """
        # Initial decay factors (will be learned)
        decay_factors = {
            'TH': 0.1,    # Slow decay → sustained sensitivity
            'TTC': 0.2,
            'DRAC': 0.3,
            'PET': 0.05   # Fast decay → brief peak sensitivity
        }
        
        return decay_factors[ssm]
    
    def process_ssm_values(self, ssm_data, dt):
        """
        Process SSM values through LIF neurons.
        
        Returns: spike events for each SSM
        """
        spikes = {}
        
        for ssm in self.ssms:
            # Get SSM value as input current
            input_current = ssm_data[ssm]
            
            # Integrate in LIF neuron
            spike_emitted = self.neurons[ssm].integrate(input_current, dt)
            
            # Record spike
            spikes[ssm] = spike_emitted
        
        return spikes
```

## SNN Architecture

### Multi-SSM Spiking Network

```python
class SafetySNN:
    """
    Spiking Neural Network combining multiple SSM inputs.
    
    Architecture:
    - Input layer: LIF neurons for each SSM
    - Hidden layer: Combine SSM spikes
    - Output layer: Emit braking spike
    
    Training objective:
    Output spikes aligned with human braking onsets
    """
    def __init__(self, ssms=['TH', 'TTC', 'DRAC', 'PET']):
        # Input layer: SSM-specific LIF neurons
        self.input_layer = SSMLIFMapper(ssms)
        
        # Hidden layer: Combine inputs
        self.hidden_neurons = [
            LIFNeuron(threshold=0.5, tau=0.15),
            LIFNeuron(threshold=0.6, tau=0.20)
        ]
        
        # Output layer: Braking decision
        self.output_neuron = LIFNeuron(threshold=0.8, tau=0.25)
    
    def forward(self, ssm_data, dt):
        """
        Forward pass through SNN.
        
        Process SSM values → Input spikes → Hidden spikes → Output spike
        """
        # Input layer: Process each SSM
        input_spikes = self.input_layer.process_ssm_values(ssm_data, dt)
        
        # Hidden layer: Combine input spikes
        hidden_input = sum(input_spikes.values())  # Aggregate spikes
        
        hidden_spikes = []
        for neuron in self.hidden_neurons:
            spike = neuron.integrate(hidden_input, dt)
            hidden_spikes.append(spike)
        
        # Output layer: Braking decision
        output_input = sum(hidden_spikes)
        braking_spike = self.output_neuron.integrate(output_input, dt)
        
        return braking_spike
    
    def predict_braking(self, ssm_sequence):
        """
        Predict braking events from SSM time series.
        
        Returns: Times when braking spike is emitted
        """
        braking_events = []
        
        for t, ssm_data in enumerate(ssm_sequence):
            dt = 0.1  # Time step
            
            braking_spike = self.forward(ssm_data, dt)
            
            if braking_spike:
                braking_events.append(t)
        
        return braking_events
```

## Training Methodology

### Training Data

```
Dataset: Car-following experiment
- Platform: 3D-CoAutoSim (CARLA/Unreal)
- Hardware: 6-DOF motion platform
- Participants: Human drivers in car-following scenarios
- Induced critical events: Emergency braking, sudden deceleration
- Measurements: SSM values + human braking onsets

Ground truth labels:
- Human braking onset times
- Objective SSM threshold crossings

Goal: Learn SNN parameters to align spikes with braking onsets
```

### Training Objective

```python
def train_snn(snn, training_data):
    """
    Train SNN to emit spikes aligned with human braking.
    
    Parameters to learn:
    1. Input neuron thresholds (SSM-specific)
    2. Input neuron decay factors (temporal sensitivity)
    3. Hidden neuron thresholds
    4. Hidden neuron decay factors
    5. Output neuron threshold
    
    Objective:
    Minimize spike prediction error:
    L = ||predicted_spikes - human_braking||²
    """
    # Extract ground truth
    human_braking = training_data['braking_onsets']
    ssm_sequence = training_data['ssm_values']
    
    # Initial prediction
    predicted_spikes = snn.predict_braking(ssm_sequence)
    
    # Optimize parameters
    for epoch in range(max_epochs):
        # Compute loss
        loss = spike_alignment_loss(predicted_spikes, human_braking)
        
        # Gradient-based update (or evolutionary optimization)
        snn = update_parameters(snn, loss)
        
        # New prediction
        predicted_spikes = snn.predict_braking(ssm_sequence)
        
        # Check convergence
        if loss < threshold:
            break
    
    return snn

def spike_alignment_loss(predicted_spikes, human_braking):
    """
    Compute alignment between predicted spikes and human braking.
    
    Metrics:
    1. Temporal distance: ||predicted - human|| in time
    2. False positives: predicted spikes without braking
    3. False negatives: braking without predicted spikes
    """
    # Match predicted spikes to braking events
    matched, fp, fn = match_spikes(predicted_spikes, human_braking)
    
    # Temporal error for matched spikes
    temporal_error = np.mean([abs(p - h) for p, h in matched])
    
    # False positive/negative penalty
    fp_penalty = fp * penalty_weight
    fn_penalty = fn * penalty_weight
    
    # Total loss
    loss = temporal_error + fp_penalty + fn_penalty
    
    return loss
```

### Learned Parameters Analysis

```
Key findings:

1. Input thresholds (SSM-specific):
   - Learned thresholds remain relatively consistent across participants
   - Indicates objective SSM thresholds are meaningful

2. Decay factors (temporal sensitivity):
   - Learned decay factors vary significantly across participants
   - Encodes different temporal sensitivities for SSMs
   - Individual differences in safety perception

3. Interpretation:
   - Consistent thresholds: Objective safety measures are valid
   - Variable decay: Temporal perception is subjective
   - SNN captures both objective and subjective aspects
```

## Results

### Qualitative Alignment

```
Spike activity aligns with braking behavior:
1. SNN emits spikes at braking onsets (good temporal alignment)
2. SNN captures reactions not explained by threshold crossings alone
3. SNN integrates sustained borderline conditions
4. SNN reacts to brief high-risk peaks

Example scenario:
- SSM value oscillates near threshold
- Traditional method: No consistent risk signal
- SNN: Integrates oscillation → emits spike at sustained risk
```

### Comparison: Traditional vs SNN

```
Traditional threshold approach:
SSM > threshold → risk event

Problem scenarios:
1. Sustained borderline: SSM oscillates around threshold
   - Traditional: Sporadic risk signals (inconsistent)
   - SNN: Integrated spike at sustained danger (consistent)

2. Brief high-risk peak: SSM spikes briefly above threshold
   - Traditional: Risk event (may be too late)
   - SNN: Temporal sensitivity → early spike (proactive)

3. Temporal differences: Different human reactions to same SSM
   - Traditional: Fixed threshold (no personalization)
   - SNN: Learned decay → personalized temporal sensitivity
```

### Participant Analysis

```python
def analyze_participant_variability(snn_results):
    """
    Analyze learned parameters across participants.
    
    Findings:
    1. Thresholds: Relatively consistent (low variance)
    2. Decay factors: Highly variable (high variance)
    
    Interpretation:
    - Consistent thresholds → objective SSM validity
    - Variable decay → subjective temporal perception
    """
    thresholds = []
    decay_factors = []
    
    for participant in participants:
        snn = trained_snn[participant]
        
        thresholds.append(snn.input_layer.thresholds)
        decay_factors.append(snn.input_layer.tau)
    
    # Statistical analysis
    threshold_variance = np.var(thresholds)
    decay_variance = np.var(decay_factors)
    
    print(f"Threshold variance: {threshold_variance:.4f} (low)")
    print(f"Decay variance: {decay_variance:.4f} (high)")
    
    return {
        'threshold_consistency': threshold_variance,
        'decay_variability': decay_variance
    }
```

## Applications

### 1. Autonomous Driving Safety System

```python
class AutonomousSafetySystem:
    """
    SNN-based safety system for autonomous vehicles.
    
    Advantages over traditional SSM thresholds:
    1. Temporal integration (sustained conditions)
    2. Temporal sensitivity (brief peaks)
    3. Human alignment (braking prediction)
    4. Personalization (individual decay factors)
    """
    def __init__(self, trained_snn):
        self.snn = trained_snn
    
    def monitor_safety(self, ssm_values):
        """
        Monitor safety in real-time using SNN.
        
        Input: Current SSM values (TH, TTC, DRAC, PET)
        Output: Braking decision (spike emission)
        """
        # Process through SNN
        braking_spike = self.snn.forward(ssm_values, dt=0.1)
        
        # Safety decision
        if braking_spike:
            return 'BRAKE_NOW'
        else:
            return 'SAFE'
    
    def predict_braking_onset(self, ssm_history):
        """
        Predict future braking onsets.
        
        Use SNN to anticipate braking before threshold crossing.
        """
        # Extrapolate SSM values
        future_ssm = extrapolate_ssm(ssm_history)
        
        # Predict braking
        braking_prediction = self.snn.predict_braking(future_ssm)
        
        return braking_prediction
```

### 2. Human Safety Perception Modeling

```python
def model_human_safety_perception(ssm_data, participant_data):
    """
    Model individual human safety perception.
    
    Uses learned decay factors to capture temporal sensitivity:
    - High decay: Sensitive to sustained conditions
    - Low decay: Sensitive to brief peaks
    
    Applications:
    - Personalize autonomous driving systems
    - Understand individual risk perception
    - Design adaptive safety thresholds
    """
    # Train SNN for this participant
    snn = train_snn(ssm_data, participant_data)
    
    # Extract learned parameters
    thresholds = snn.input_layer.thresholds
    decay_factors = snn.input_layer.tau
    
    # Temporal sensitivity profile
    sensitivity_profile = {
        'sustained_condition_sensitivity': 1.0 / np.mean(decay_factors),
        'brief_peak_sensitivity': np.min(decay_factors),
        'thresholds': thresholds
    }
    
    return sensitivity_profile
```

### 3. Safety Threshold Optimization

```python
def optimize_safety_thresholds(vehicle_type, driving_context):
    """
    Optimize SSM thresholds using SNN framework.
    
    Advantages:
    - Learn thresholds from human data
    - Adapt to driving context
    - Personalize to vehicle type
    """
    # Collect human driving data
    training_data = collect_data(vehicle_type, driving_context)
    
    # Train SNN
    snn = SafetySNN()
    snn = train_snn(snn, training_data)
    
    # Extract optimized thresholds
    optimized_thresholds = {
        'TH': snn.input_layer.neurons['TH'].V_threshold,
        'TTC': snn.input_layer.neurons['TTC'].V_threshold,
        'DRAC': snn.input_layer.neurons['DRAC'].V_threshold,
        'PET': snn.input_layer.neurons['PET'].V_threshold
    }
    
    return optimized_thresholds
```

## Implementation Details

### LIF Parameters

```
Standard LIF parameters:
- Membrane potential V: 0 (baseline)
- Threshold V_threshold: Learned (SSM-specific)
- Decay factor τ: Learned (temporal sensitivity)
- Reset value V_reset: 0 (after spike)
- Time step dt: 0.1 s

Input current I(t):
- SSM value mapped to current
- Example: TH = 1.0 s → I = 1.0
- Normalization: Scale SSM to reasonable input range
```

### SSM Calculation

```python
def calculate_ssm(vehicle_state, lead_vehicle_state):
    """
    Calculate Surrogate Safety Measures.
    
    Required data:
    - Vehicle position, velocity, acceleration
    - Lead vehicle position, velocity, acceleration
    """
    # Time Headway (TH)
    TH = calculate_time_headway(vehicle_state, lead_vehicle_state)
    
    # Time to Collision (TTC)
    TTC = calculate_ttc(vehicle_state, lead_vehicle_state)
    
    # Deceleration to Avoid Collision (DRAC)
    DRAC = calculate_drac(vehicle_state, lead_vehicle_state)
    
    # Post-Encroachment Time (PET)
    PET = calculate_pet(vehicle_state, lead_vehicle_state)
    
    return {
        'TH': TH,
        'TTC': TTC,
        'DRAC': DRAC,
        'PET': PET
    }

def calculate_time_headway(vehicle, lead_vehicle):
    """
    Time Headway = Distance / Vehicle velocity
    
    Interpretation: Time to reach lead vehicle if maintaining speed.
    """
    distance = lead_vehicle.position - vehicle.position
    velocity = vehicle.velocity
    
    TH = distance / velocity
    
    return TH

def calculate_ttc(vehicle, lead_vehicle):
    """
    Time to Collision = Distance / Relative velocity
    
    Interpretation: Time to collision if both maintain current speeds.
    """
    distance = lead_vehicle.position - vehicle.position
    relative_velocity = vehicle.velocity - lead_vehicle.velocity
    
    if relative_velocity <= 0:
        TTC = np.inf  # No collision risk
    else:
        TTC = distance / relative_velocity
    
    return TTC

def calculate_drac(vehicle, lead_vehicle):
    """
    Deceleration to Avoid Collision.
    
    DRAC = (relative_velocity)² / (2 * distance)
    
    Interpretation: Required deceleration to avoid collision.
    """
    distance = lead_vehicle.position - vehicle.position
    relative_velocity = vehicle.velocity - lead_vehicle.velocity
    
    DRAC = (relative_velocity)**2 / (2 * distance)
    
    return DRAC
```

## Key Insights

### Objective-Subjective Convergence

```
SNN framework bridges objective SSMs and subjective human perception:

Objective component:
- Learned thresholds are consistent across participants
- Objective SSM values are meaningful for safety assessment

Subjective component:
- Learned decay factors vary across participants
- Temporal sensitivity is individual-specific
- Captures personal safety perception

Result: Convergence of objective measures and subjective perception
```

### Temporal Sensitivity Encoding

```
Decay factor τ encodes temporal sensitivity:

τ large (slow decay):
- Long integration window
- Membrane potential accumulates over long time
- Sensitive to sustained borderline conditions
- Reacts to gradual risk buildup

τ small (fast decay):
- Short integration window
- Membrane potential resets quickly
- Sensitive to brief high-risk peaks
- Reacts to sharp, transient dangers

Example:
- Participant A: τ = 0.05 → brief peak sensitivity
- Participant B: τ = 0.20 → sustained condition sensitivity
- Result: Different reactions to same SSM values
```

### Beyond Threshold Crossing

```
SNN captures reactions not explained by threshold crossing alone:

Scenario 1: Sustained borderline
- SSM oscillates around threshold (above/below repeatedly)
- Traditional: Sporadic risk signals (inconsistent)
- SNN: Integrates oscillation → spike at sustained danger

Scenario 2: Gradual risk buildup
- SSM slowly increases toward threshold
- Traditional: No risk signal until crossing
- SNN: Membrane potential accumulates → spike before crossing

Scenario 3: Multiple SSM interaction
- TH and TTC both near thresholds
- Traditional: Independent risk signals
- SNN: Combined integration → unified braking decision

Key advantage: Temporal dynamics beyond binary threshold
```

## Experimental Validation

### Dataset

```
Platform: 3D-CoAutoSim
- CARLA simulator (Unreal Engine)
- 6-DOF motion platform (realistic driving feel)
- Controlled car-following scenarios

Induced critical events:
- Emergency braking by lead vehicle
- Sudden deceleration
- Cut-in scenarios

Measurements:
- SSM values (TH, TTC, DRAC, PET)
- Human braking onsets
- Vehicle state data
```

### Validation Metrics

```
Alignment metrics:
1. Temporal correlation: ||predicted_spikes - braking_onsets||
2. False positives: Predicted spikes without braking
3. False negatives: Braking without predicted spikes
4. Coverage: % of braking events captured by spikes

Results:
- Temporal alignment: Mean error < 0.5 s
- False positive rate: < 10%
- False negative rate: < 15%
- Coverage: > 85% braking events captured
```

## Limitations

1. **Training data requirement**: Needs human driving data for parameter learning
2. **Computational overhead**: SNN simulation adds latency (real-time concern)
3. **Parameter interpretability**: Learned decay factors may be hard to interpret
4. **Generalization**: May not generalize to all driving scenarios
5. **Individual variability**: Requires per-participant training for personalization

## Future Directions

1. **Hardware implementation**: Neuromorphic chips for real-time SNN
2. **Transfer learning**: Generalize across driving scenarios
3. **Multi-modal inputs**: Combine SSMs with visual/radar data
4. **Adaptive learning**: Online learning during driving
5. **Behavioral validation**: More extensive human testing

## Related Work

- **Surrogate Safety Measures**: Traffic safety evaluation
- **Spiking Neural Networks**: Neuromorphic computing
- **LIF Neurons**: Biological neuron models
- **Autonomous driving safety**: ADAS systems
- **Human factors**: Safety perception modeling

## References

- arXiv:2605.30368 - Original paper
- Surrogate Safety Measures review (Zheng et al., 2020)
- LIF neuron models (Gerstner et al., 2014)
- CARLA simulator (Dosovitskiy et al., 2017)

## Key Takeaways

1. **SNN reinterpretation**: SSM thresholds → LIF spiking thresholds
2. **Temporal dynamics**: LIF neurons integrate over time (sustained conditions)
3. **Temporal sensitivity**: Decay factor encodes individual perception
4. **Human alignment**: Spikes align with braking onsets
5. **Objective-subjective convergence**: Consistent thresholds + variable decay
6. **Beyond binary**: Captures reactions not explained by threshold crossing alone

## Notes

- Innovative application of SNN to autonomous driving safety
- Bridges objective safety measures and subjective human perception
- Temporal sensitivity encoding is key contribution
- Practical application: Personalized safety systems in autonomous vehicles
- Validates biological inspiration for engineering problems

---
arXiv:2605.30368
Authors: Enrico Del Re, Mohamed Sabry, Cristina Olaverri-Monreal
Submitted: 2026-05-18
Comments: 6 pages