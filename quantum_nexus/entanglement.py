"""Entanglement - Quantum entanglement and correlations."""

import numpy as np
from typing import Tuple, List


class Entanglement:
    """Handle quantum entanglement operations."""

    def __init__(self):
        """Initialize entanglement handler."""
        self.entangled_pairs = []

    def create_bell_pair(self, bell_type: str = "00") -> np.ndarray:
        """Create Bell entangled pair."""
        sqrt2 = np.sqrt(2)
        bell_states = {
            "00": np.array([1, 0, 0, 1], dtype=complex) / sqrt2,
            "01": np.array([0, 1, 1, 0], dtype=complex) / sqrt2,
            "10": np.array([1, 0, 0, -1], dtype=complex) / sqrt2,
            "11": np.array([0, 1, -1, 0], dtype=complex) / sqrt2,
        }
        return bell_states.get(bell_type, bell_states["00"])

    def create_ghz_state(self, n_qubits: int = 3) -> np.ndarray:
        """Create GHZ state."""
        dim = 2 ** n_qubits
        state = np.zeros(dim, dtype=complex)
        state[0] = 1.0 / np.sqrt(2)
        state[-1] = 1.0 / np.sqrt(2)
        return state

    def create_w_state(self, n_qubits: int = 3) -> np.ndarray:
        """Create W state."""
        dim = 2 ** n_qubits
        state = np.zeros(dim, dtype=complex)
        for i in range(n_qubits):
            index = 2 ** i
            state[index] = 1.0
        return state / np.sqrt(n_qubits)

    def measure_entanglement_entropy(self, state: np.ndarray) -> float:
        """Calculate entanglement entropy."""
        probabilities = np.abs(state) ** 2
        nonzero_probs = probabilities[probabilities > 1e-10]
        entropy = -np.sum(nonzero_probs * np.log2(nonzero_probs))
        return float(entropy)

    def check_bell_inequality(self, measurements: List[Tuple[int, int]]) -> float:
        """Check CHSH Bell inequality violation."""
        if not measurements:
            return 0.0
        correlations = [m[0] * m[1] for m in measurements]
        chsh = 2 * np.sqrt(2) * np.mean(correlations)
        return float(chsh)

    def __repr__(self) -> str:
        return f"Entanglement(pairs={len(self.entangled_pairs)})"
