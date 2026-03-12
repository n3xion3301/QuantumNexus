"""Superposition - Quantum superposition states and operations."""

import numpy as np
from typing import List, Tuple


class Superposition:
    """Handle quantum superposition states."""

    def __init__(self):
        """Initialize superposition handler."""
        self.states = []

    def create_equal_superposition(self, n_qubits: int) -> np.ndarray:
        """Create equal superposition of all basis states."""
        dim = 2 ** n_qubits
        state = np.ones(dim, dtype=complex) / np.sqrt(dim)
        return state

    def create_weighted_superposition(self, amplitudes: List[complex]) -> np.ndarray:
        """Create superposition with custom amplitudes."""
        state = np.array(amplitudes, dtype=complex)
        norm = np.linalg.norm(state)
        if norm == 0:
            raise ValueError("Cannot normalize zero vector")
        return state / norm

    def measure_superposition(self, state: np.ndarray) -> Tuple[int, float]:
        """Measure superposition and collapse to basis state."""
        probabilities = np.abs(state) ** 2
        measured_index = np.random.choice(len(state), p=probabilities)
        probability = probabilities[measured_index]
        return measured_index, probability

    def get_probabilities(self, state: np.ndarray) -> np.ndarray:
        """Get measurement probabilities for all basis states."""
        return np.abs(state) ** 2

    def superposition_statistics(self, state: np.ndarray, n_measurements: int = 1000) -> dict:
        """Simulate multiple measurements and get statistics."""
        results = [self.measure_superposition(state)[0] for _ in range(n_measurements)]
        unique, counts = np.unique(results, return_counts=True)
        
        return {
            "measured_states": unique.tolist(),
            "counts": counts.tolist(),
            "frequencies": (counts / n_measurements).tolist(),
            "theoretical_probabilities": self.get_probabilities(state).tolist()
        }

    def __repr__(self) -> str:
        return f"Superposition(states={len(self.states)})"
