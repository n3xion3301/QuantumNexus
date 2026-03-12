"""Measurement - Quantum measurement and collapse."""

import numpy as np
from typing import List, Tuple, Dict


class Measurement:
    """Handle quantum measurement operations."""

    def __init__(self):
        """Initialize measurement handler."""
        self.measurement_history = []

    def measure_computational_basis(self, state: np.ndarray) -> Tuple[int, float]:
        """Measure in computational basis."""
        probabilities = np.abs(state) ** 2
        measured_state = np.random.choice(len(state), p=probabilities)
        probability = probabilities[measured_state]
        self.measurement_history.append({
            "basis": "computational",
            "result": measured_state,
            "probability": probability
        })
        return measured_state, probability

    def measure_observable(self, state: np.ndarray, observable: np.ndarray) -> float:
        """Measure expectation value of observable."""
        expectation = np.real(np.conj(state) @ observable @ state)
        return float(expectation)

    def measure_pauli_x(self, state: np.ndarray) -> float:
        """Measure expectation value of Pauli X."""
        pauli_x = np.array([[0, 1], [1, 0]], dtype=complex)
        return self.measure_observable(state, pauli_x)

    def measure_pauli_z(self, state: np.ndarray) -> float:
        """Measure expectation value of Pauli Z."""
        pauli_z = np.array([[1, 0], [0, -1]], dtype=complex)
        return self.measure_observable(state, pauli_z)

    def repeated_measurements(self, state: np.ndarray, n_measurements: int = 100) -> Dict:
        """Perform repeated measurements."""
        results = []
        for _ in range(n_measurements):
            result, _ = self.measure_computational_basis(state)
            results.append(result)
        unique, counts = np.unique(results, return_counts=True)
        return {
            "measured_states": unique.tolist(),
            "counts": counts.tolist(),
            "frequencies": (counts / n_measurements).tolist(),
        }

    def __repr__(self) -> str:
        return f"Measurement(history={len(self.measurement_history)})"
