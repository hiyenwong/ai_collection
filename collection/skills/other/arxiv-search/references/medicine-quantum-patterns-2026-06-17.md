# Medicine+Quantum Patterns — 2026-06-17 Session

## Pattern 1: PINN Replaces Monte Carlo for Scintillation Cascade (2606.16309)

**Signal**: "physics-informed neural network" + "medical imaging" + "quant-ph" cross-list
- Scintillators (radiation→light conversion) modeled by non-differentiable Monte Carlo cascades
- PINN surrogate enables end-to-end differentiable optimization of nanophotonic geometry
- **Reusable skill pattern**: When a physics process is simulated by Monte Carlo and blocks gradient-based ML, replace with physics-informed neural surrogate → enables inverse design
- **Cross-domain bridge**: quant-ph (nanophotonics/quantum optics) + medical imaging (X-ray scintillators)

## Pattern 2: Passive Picotesla Magnetic Environment (2606.16722)

**Signal**: "quantum sensing" + "biomagnetism" + "physics.med-ph"
- Passive shielding + magnetic equilibration achieves <100 pT without active compensation
- Robotic field mapping resolves ultra-low residual patterns
- OPMs (optically pumped magnetometers) operate at design noise during motion without feedback
- Applications: MCG (adult+fetal), MEG (standing), ultra-low field MRI with polarized noble gases
- **Reusable skill pattern**: Passive magnetic environments eliminate active-compensation noise in quantum sensing; robotic mapping + equilibration is the key operational sequence
