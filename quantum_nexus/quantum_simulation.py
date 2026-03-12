"""Quantum Simulation - Simulate quantum systems."""

import numpy as np
from typing import Tuple


class QuantumSimulation:
    """Simulate quantum systems and dynamics."""

    def __init__(self, hamiltonian: np.ndarray):
        """Initialize quantum simulation."""
        self.hamiltonian = hamiltonian
        self.dim = hamiltonian.shape[0]

    def time_evolution(self, initial_state: np.ndarray, time: float) -> np.ndarray:
        """Evolve state under Hamiltonian."""
        eigenvalues, eigenvectors = np.linalg.eigh(self.hamiltonian)
        evolution_op = eigenvectors @ np.diag(np.exp(-1j * eigenvalues * time)) @ np.conj(eigenvectors.T)
        return evolution_op @ initial_state

    def ground_state(self) -> Tuple[float, np.ndarray]:
        """Get ground state energy and state."""
        eigenvalues, eigenvectors = np.linalg.eigh(self.hamiltonian)
        return eigenvalues[0], eigenvectors[:, 0]

    def expectation_value(self, state: np.ndarray, observable: np.ndarray) -> float:
        """Calculate expectation value of observable."""
        return np.real(np.conj(state) @ observable @ state)

    def __repr__(self) -> str:
        return f"QuantumSimulation(dim={self.dim})"
