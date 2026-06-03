# LLM Prompt Templates for Quantum Device Information Extraction

## Template 1: Full Device Extraction

```
You are a quantum device researcher. Extract ALL device parameters from the
following text. The text describes a quantum cascade laser or similar photonic device.

Output ONLY valid JSON with this schema:
{
  "device_type": "string",
  "structure": {
    "active_region": {"material": "string", "type": "string"},
    "layers": [
      {"material": "string", "thickness_nm": "number|null", "role": "string"}
    ],
    "total_periods": "number|null"
  },
  "materials": [
    {"compound": "string", "composition": "string", "doping_cm3": "string|null"}
  ],
  "performance": {
    "emission_wavelength_um": "number|null",
    "operating_temperature_k": "number|null",
    "peak_power_mw": "number|null"
  }
}

Text: {PAPER_TEXT}
```

## Template 2: Material-Specific Extraction

```
Extract only material composition information from this text.
Focus on: alloy ratios, doping concentrations, growth methods, substrate material.

Output as JSON:
{"materials": [...], "growth_method": "string", "substrate": "string"}

Text: {PAPER_TEXT}
```

## Template 3: Performance Parameter Extraction

```
Extract all performance metrics from this text.
Include: wavelength, power, efficiency, temperature range, threshold current.

Output as JSON:
{"metrics": [{"name": "string", "value": "number", "unit": "string", "condition": "string|null"}]}

Text: {PAPER_TEXT}
```

## Cross-Validation Template

```
Compare these two extractions of the same paper section.
Identify conflicts and suggest the most likely correct value:

Extraction 1: {EXTRACTION_1}
Extraction 2: {EXTRACTION_2}

Output: {"conflicts": [...], "resolved": {...}}
```
