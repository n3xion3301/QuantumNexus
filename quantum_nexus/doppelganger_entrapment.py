"""Doppelganger Entrapment - Quantum entanglement simulations."""

import numpy as np
from typing import Tuple, List


class DoppelgangerEntrapment:
    """Simulate quantum entanglement and dual-state phenomena."""

    def __init__(self):
        """Initialize entanglement system."""
        self.entangled_pairs = []
        self.correlation_strength = 0.0

    def create_bell_state(self, state_type: str = "00") -> np.ndarray:
        """Create Bell entangled states.
        
        Args:
            state_type: Type of Bell state ("00", "01", "10", "11")
            
        Returns:
            Entangled two-qubit state
        """
        sqrt2 = np.sqrt(2)
        
        bell_states = {
            "00": np.array([1, 0, 0, 1], dtype=complex) / sqrt2,  # |Φ+⟩
            "01": np.array([0, 1, 1, 0], dtype=complex) / sqrt2,  # |Ψ+⟩
            "10": np.array([1, 0, 0, -1], dtype=complex) / sqrt2,  # |Φ-⟩
            "11": np.array([0, 1, -1, 0], dtype=complex) / sqrt2,  # |Ψ-⟩
        }
        
        if state_type not in bell_states:
            raise ValueError(f"Unknown Bell state: {state_type}")
        
        return bell_states[state_type]

    def measure_entanglement(self, state: np.ndarray) -> float:
        """Calculate entanglement entropy (concurrence).
        
        Args:
            state: Two-qubit entangled state
            
        Returns:
            Entanglement measure (0 = separable, 1 = maximally entangled)
        """
        probabilities = np.abs(state) ** 2
        entropy = -np.sum(probabilities[probabilities > 0] * np.log2(probabilities[probabilities > 0]))
        return min(entropy, 1.0)

    def correlate_doppelgangers(self, particle1: np.ndarray, particle2: np.ndarray) -> float:
        """Calculate correlation between entangled doppelgangers.
        
        Args:
            particle1: First particle state
            particle2: Second particle state
            
        Returns:
            Correlation coefficient
        """
        correlation = abs(np.conj(particle1) @ particle2)
        return float(correlation)

    def violate_bell_inequality(self, measurements: List[Tuple[int, int]]) -> float:
        """Calculate CHSH parameter for Bell inequality violation.
        
        Args:
            measurements: List of measurement outcome pairs
            
        Returns:
            CHSH parameter (>2 indicates violation)
        """
        if not measurements:
            return 0.0
        
        correlations = [m[0] * m[1] for m in measurements]
        chsh = 2 * np.sqrt(2) * np.mean(correlations)
        return float(chsh)

    def create_ghz_state(self, n_qubits: int = 3) -> np.ndarray:
        """Create GHZ entangled state for n qubits.
        
        Args:
            n_qubits: Number of qubits
            
        Returns:
            GHZ state |000...⟩ + |111...⟩
        """
        dim = 2 ** n_qubits
        state = np.zeros(dim, dtype=complex)
        state[0] = 1.0 / np.sqrt(2)
        state[-1] = 1.0 / np.sqrt(2)
        return state

    def __repr__(self) -> str:
        return f"DoppelgangerEntrapment(pairs={len(self.entangled_pairs)})"
