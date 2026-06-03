"""
Fluxonium Qubit Measurement Analysis Tools

Python tools for analyzing measurement-induced state transitions
in fluxonium qubit systems.
"""

import numpy as np
from typing import Dict, Tuple


class FluxoniumAnalyzer:
    """
    Analyzer for fluxonium qubit measurement-induced transitions.
    """

    def __init__(
        self,
        omega_01: float,  # Ground to first excited transition (Hz)
        omega_12: float,  # First to second excited transition (Hz)
        omega_r: float,  # Readout resonator frequency (Hz)
        g: float,  # Qubit-resonator coupling (Hz)
        flux: float = 0.0,  # External flux (in units of Φ₀)
    ):
        """
        Initialize fluxonium analyzer with system parameters.

        Args:
            omega_01: Qubit transition frequency
            omega_12: Second transition frequency
            omega_r: Readout resonator frequency
            g: Coupling strength
            flux: External flux parameter
        """
        self.omega_01 = omega_01
        self.omega_12 = omega_12
        self.omega_r = omega_r
        self.g = g
        self.flux = flux

    def calculate_anharmonicity(self) -> float:
        """
        Calculate qubit anharmonicity.

        Returns:
            Anharmonicity α = ω₁₂ - ω₀₁
        """
        return self.omega_12 - self.omega_01

    def check_multiphoton_resonance(
        self, drive_frequency: float, max_photons: int = 5
    ) -> Dict[int, float]:
        """
        Check for multi-photon resonance conditions.

        Args:
            drive_frequency: Measurement drive frequency
            max_photons: Maximum number of photons to check

        Returns:
            Dictionary of photon number -> detuning
        """
        resonances = {}

        # Check transitions from ground state
        for n in range(2, max_photons + 1):
            detuning_01 = n * drive_frequency - self.omega_01
            detuning_12 = n * drive_frequency - self.omega_12

            resonances[f"{n}-photon (0→1)"] = detuning_01
            resonances[f"{n}-photon (1→2)"] = detuning_12

        # Check 2-photon transition between excited states
        two_photon_02 = 2 * drive_frequency - (self.omega_01 + self.omega_12)
        resonances["2-photon (0→2)"] = two_photon_02

        return resonances

    def estimate_transition_rate(
        self,
        photon_number: int,
        drive_power: float,  # In units of g
        detuning: float,
    ) -> float:
        """
        Estimate measurement-induced transition rate.

        Args:
            photon_number: Number of photons in process
            drive_power: Drive amplitude (Ω/g)
            detuning: Detuning from resonance

        Returns:
            Estimated transition rate (Γ)
        """
        # Multi-photon coupling scales as Ω^n / Δ^(n-1)
        effective_coupling = drive_power**photon_number / (
            abs(detuning) ** (photon_number - 1)
        )

        # Rate ~ effective_coupling^2
        rate = effective_coupling**2

        return rate

    def estimate_purcell_rate(self) -> float:
        """
        Estimate Purcell decay rate through resonator.

        Returns:
            Purcell decay rate
        """
        detuning = abs(self.omega_r - self.omega_01)
        purcell_rate = self.g**2 / detuning

        return purcell_rate

    def estimate_readout_fidelity(
        self, measurement_rate: float, transition_rate: float, integration_time: float
    ) -> Tuple[float, Dict]:
        """
        Estimate single-shot readout fidelity.

        Args:
            measurement_rate: Measurement-induced dephasing rate
            transition_rate: Measurement-induced transition rate
            integration_time: Measurement duration

        Returns:
            Tuple of (fidelity, details dict)
        """
        # Probability of remaining in initial state
        P_remain = np.exp(-transition_rate * integration_time)

        # Signal-to-noise ratio
        SNR = measurement_rate * integration_time

        # Assignment fidelity from SNR
        assignment_fidelity = (1 + np.exp(-SNR)) / 2

        # Total fidelity
        total_fidelity = assignment_fidelity * P_remain

        details = {
            "P_remain": P_remain,
            "SNR": SNR,
            "assignment_fidelity": assignment_fidelity,
            "measurement_rate": measurement_rate,
            "transition_rate": transition_rate,
        }

        return total_fidelity, details

    def find_safe_operating_region(
        self,
        flux_range: Tuple[float, float] = (-0.5, 0.5),
        flux_steps: int = 100,
        drive_frequency: float = None,
    ) -> Dict:
        """
        Find flux regions with minimal multi-photon resonances.

        Args:
            flux_range: Range of flux to search
            flux_steps: Number of flux points
            drive_frequency: Drive frequency (defaults to resonator frequency)

        Returns:
            Dictionary with safe regions and recommended flux
        """
        if drive_frequency is None:
            drive_frequency = self.omega_r

        flux_values = np.linspace(flux_range[0], flux_range[1], flux_steps)

        # Calculate resonance strength at each flux point
        # (Simplified - would need actual fluxonium spectrum)
        safe_regions = []

        for flux in flux_values:
            # Check resonances
            resonances = self.check_multiphoton_resonance(drive_frequency)

            # Find minimum resonance strength
            min_detuning = min(abs(d) for d in resonances.values())

            if min_detuning > self.g:  # More than one coupling strength detuned
                safe_regions.append(flux)

        if safe_regions:
            recommended_flux = safe_regions[len(safe_regions) // 2]
        else:
            recommended_flux = 0.0

        return {
            "safe_regions": safe_regions,
            "recommended_flux": recommended_flux,
            "total_safe_fraction": len(safe_regions) / flux_steps,
        }


def analyze_fluxonium_system(
    omega_01: float,
    omega_12: float,
    omega_r: float,
    g: float,
    drive_frequency: float = None,
    drive_power: float = 0.1,
    integration_time: float = 1e-6,
) -> Dict:
    """
    Complete analysis of a fluxonium qubit system for readout.

    Args:
        omega_01: Qubit frequency (Hz)
        omega_12: Second transition frequency (Hz)
        omega_r: Resonator frequency (Hz)
        g: Coupling strength (Hz)
        drive_frequency: Drive frequency (defaults to omega_r)
        drive_power: Drive power (Ω/g)
        integration_time: Measurement time (s)

    Returns:
        Complete analysis dictionary
    """
    if drive_frequency is None:
        drive_frequency = omega_r

    analyzer = FluxoniumAnalyzer(omega_01, omega_12, omega_r, g)

    # Check resonances
    resonances = analyzer.check_multiphoton_resonance(drive_frequency)

    # Estimate rates
    purcell_rate = analyzer.estimate_purcell_rate()

    # Find dominant transition mechanism
    dominant_resonance = min(resonances.items(), key=lambda x: abs(x[1]))

    # Estimate measurement rate (dispersive approximation)
    measurement_rate = drive_power**2 * g**2 / abs(omega_r - omega_01)

    # Estimate transition rate from dominant resonance
    photon_number = int(dominant_resonance[0].split("-")[0])
    transition_rate = analyzer.estimate_transition_rate(
        photon_number, drive_power, dominant_resonance[1]
    )

    # Estimate fidelity
    fidelity, fidelity_details = analyzer.estimate_readout_fidelity(
        measurement_rate, transition_rate, integration_time
    )

    return {
        "anharmonicity": analyzer.calculate_anharmonicity(),
        "resonances": resonances,
        "dominant_resonance": dominant_resonance,
        "purcell_rate": purcell_rate,
        "measurement_rate": measurement_rate,
        "transition_rate": transition_rate,
        "fidelity": fidelity,
        "fidelity_details": fidelity_details,
        "recommendations": {
            "safe_flux": 0.0,  # Would calculate properly with fluxonium spectrum
            "max_drive_power": 0.05,  # Estimate based on avoiding transitions
            "integration_time": integration_time,
        },
    }


# Example usage
if __name__ == "__main__":
    # Example parameters (typical fluxonium)
    omega_01 = 500e6  # 500 MHz
    omega_12 = 1.5e9  # 1.5 GHz
    omega_r = 6e9  # 6 GHz
    g = 50e6  # 50 MHz coupling

    analysis = analyze_fluxonium_system(
        omega_01, omega_12, omega_r, g, drive_power=0.1, integration_time=1e-6
    )

    print("Fluxonium Qubit Analysis Results:")
    print(f"  Anharmonicity: {analysis['anharmonicity'] / 1e6:.2f} MHz")
    print(f"  Dominant resonance: {analysis['dominant_resonance']}")
    print(f"  Measurement rate: {analysis['measurement_rate'] / 1e6:.2f} MHz")
    print(f"  Transition rate: {analysis['transition_rate'] / 1e6:.2f} MHz")
    print(f"  Estimated fidelity: {analysis['fidelity'] * 100:.2f}%")
