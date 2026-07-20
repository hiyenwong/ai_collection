---
name: hardware-faithful-plc-verification
description: "Hardware-faithful formal verification for IEC 61131-3 PLC programs on resource-constrained microcontrollers. Closes the deployment gap between abstract verification models and real MCU hardware by using declarative HAL descriptors (word width, ADC/PWM resolution, I/O binding) and sound lowering that constrains inputs to hardware-realizable ranges. Use when: (1) verifying PLC programs for embedded MCUs, (2) formal verification of industrial control systems, (3) eliminating false alarms in bounded-width arithmetic verification, (4) hardware-aware model checking for automation systems, (5) ESBMC-based PLC verification."
metadata:
  arxiv_id: "2607.08550"
  published: "2026-07-09"
  authors: "Pierre Dantas, Lucas Cordeiro, Waldir Junior"
  tags: [formal-verification, PLC, IEC-61131-3, ESBMC, embedded-systems, model-checking, hardware-abstraction]
---

# Hardware-Faithful PLC Verification

## Problem: The Deployment Gap

Formal verifiers for IEC 61131-3 PLC programs (e.g., ESBMC-PLC) prove safety over an abstract scan-cycle model with idealized unbounded integers. Real PLCs run on resource-constrained MCUs with:
- **Finite word widths** (16-bit words, 8-bit AVR Arduinos)
- **Finite-resolution ADC** (sensors produce bounded, discrete values)
- **Fixed I/O bindings** (specific pins mapped to specific signals)

**Consequence**: Naive width-aware verification produces **44% false alarms** (54/123 programs) because it explores sensor values no ADC can produce. Unbounded input models fabricate alarms that no real environment can trigger.

## Core Methodology: HAL + Sound Lowering

### 1. Hardware Abstraction Layer (HAL) Descriptor

Declarative specification of target hardware:
```yaml
# HAL descriptor structure
word_width: 16           # MCU native word size
adc_resolution: 10       # bits (0-1023 range)
pwm_resolution: 8        # bits (0-255 range)
io_bindings:             # pin-to-signal mapping
  - pin: "A0"
    signal: "temperature_sensor"
    range: [0, 1023]
```

### 2. Sound Lowering

The verification pipeline applies two transformations:

**Arithmetic at target width**: All arithmetic operations are interpreted at the MCU's native word width (not infinite precision). Overflow behavior matches hardware semantics.

**Hardware-realizable input constraints**: Sensor inputs are constrained to values the actual ADC can produce. A 10-bit ADC produces integers in [0, 1023] — not arbitrary integers.

### 3. Verification Result

On a 123-program corpus:
- **Before HAL**: 54 false alarms, 0 genuine defects found
- **After HAL**: 0 false alarms, genuine width-dependent defects detected with realizable witnesses

## Application Pattern

1. **Identify target hardware**: MCU architecture, word width, ADC/PWM specs
2. **Create HAL descriptor**: Document width, resolution, I/O bindings
3. **Apply sound lowering**: Constrain verification inputs to hardware-realizable ranges
4. **Run verification**: Check safety properties with hardware-faithful semantics
5. **Analyze results**: Distinguish genuine defects from hardware-Impossible scenarios

## Key Insight

The deployment gap lies where computation meets the physical process — a bounded sensor reading scaled by finite-width arithmetic into an actuation command. An overflow can silently suppress a safety action (e.g., high-level alarm). Verification must model this boundary faithfully.

## Activation Keywords

- hardware-faithful verification
- PLC formal verification
- IEC 61131-3 verification
- ESBMC
- embedded model checking
- deployment gap
- HAL descriptor
- Arduino PLC
- false alarm elimination
- bounded arithmetic verification
