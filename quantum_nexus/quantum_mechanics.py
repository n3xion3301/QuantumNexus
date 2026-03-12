"""Quantum Mechanics - Core quantum operations and simulations."""

import numpy as np
from typing import Tuple, List
from scipy import linalg


class QuantumMechanics:
    """Core quantum mechanics operations and simulations."""

    def __init__(self, dimension: int = 2):
        """Initialize quantum mechanics system.
        
        Args:
            dimension: Hilbert space dimension (default: 2 for qubit)
        """
        self.dimension = dimension
        self.pauli_x = np.array([[0, 1], [1, 0]], dtype=complex)
        self.pauli_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
        self.pauli_z = np.array([[1, 0], [0, -1]], dtype=complex)
        self.identity = np.eye(dimension, dtype=complex)

    def create_superposition(self, amplitudes: List[complex]) -> np.ndarray:
        """Create a quantum superposition state.
        
        Args:
            amplitudes: Complex amplitudes for each basis state
            
        Returns:
            Normalized quantum state vector
        """
        state = np.array(amplitudes, dtype=complex)
        norm = np.linalg.norm(state)
        if norm == 0:
            raise ValueError("Cannot normalize zero vector")
        return state / norm

    def measure_probability(self, state: np.ndarray, basis_index: int) -> float:
        """Calculate measurement probability for a basis state.
        
        Args:
            state: Quantum state vector
            basis_index: Index of the basis state
            
        Returns:
            Probability of measuring that basis state
        """
        if basis_index >= len(state):
            raise IndexError("Basis index out of range")
        return abs(state[basis_index]) ** 2

    def apply_gate(self, state: np.ndarray, gate: np.ndarray) -> np.ndarray:
        """Apply a quantum gate to a state.
        
        Args:
            state: Quantum state vector
            gate: Unitary gate matrix
            
        Returns:
            Transformed quantum state
        """
        return gate @ state

    def hadamard_gate(self) -> np.ndarray:
        """Create Hadamard gate for superposition."""
        return np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)

    def phase_gate(self, theta: float) -> np.ndarray:
        """Create phase gate with angle theta."""
        return np.array([[1, 0], [0, np.exp(1j * theta)]], dtype=complex)

    def expectation_value(self, state: np.ndarray, observable: np.ndarray) -> float:
        """Calculate expectation value of an observable.
        
        Args:
            state: Quantum state vector
            observable: Observable operator matrix
            
        Returns:
            Expectation value <ψ|O|ψ>
        """
        return np.real(np.conj(state) @ observable @ state)

    def fidelity(self, state1: np.ndarray, state2: np.ndarray) -> float:
        """Calculate fidelity between two quantum states.
        
        Args:
            state1: First quantum state
            state2: Second quantum state
            
        Returns:
            Fidelity value between 0 and 1
        """
        overlap = abs(np.conj(state1) @ state2) ** 2
        return overlap

    def __repr__(self) -> str:
        return f"QuantumMechanics(dimension={self.dimension})"
