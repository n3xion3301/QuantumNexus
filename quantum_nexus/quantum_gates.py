"""Quantum Gates - Quantum logic gates and circuits."""

import numpy as np
from typing import List


class QuantumGates:
    """Quantum logic gates and operations."""

    @staticmethod
    def pauli_x() -> np.ndarray:
        """Pauli X gate (NOT gate)."""
        return np.array([[0, 1], [1, 0]], dtype=complex)

    @staticmethod
    def pauli_y() -> np.ndarray:
        """Pauli Y gate."""
        return np.array([[0, -1j], [1j, 0]], dtype=complex)

    @staticmethod
    def pauli_z() -> np.ndarray:
        """Pauli Z gate."""
        return np.array([[1, 0], [0, -1]], dtype=complex)

    @staticmethod
    def hadamard() -> np.ndarray:
        """Hadamard gate."""
        return np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)

    @staticmethod
    def phase_gate(theta: float) -> np.ndarray:
        """Phase gate with angle theta."""
        return np.array([[1, 0], [0, np.exp(1j * theta)]], dtype=complex)

    @staticmethod
    def cnot_gate() -> np.ndarray:
        """CNOT gate for 2 qubits."""
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ], dtype=complex)

    @staticmethod
    def apply_gate(state: np.ndarray, gate: np.ndarray) -> np.ndarray:
        """Apply quantum gate to state."""
        return gate @ state

    @staticmethod
    def apply_sequence(state: np.ndarray, gates: List[np.ndarray]) -> np.ndarray:
        """Apply sequence of gates."""
        result = state.copy()
        for gate in gates:
            result = gate @ result
        return result

    def __repr__(self) -> str:
        return "QuantumGates()"
