"""Quantum Algorithms - Common quantum algorithms."""

import numpy as np


class QuantumAlgorithms:
    """Implement common quantum algorithms."""

    @staticmethod
    def grover_search(marked_state: int, n_qubits: int) -> np.ndarray:
        """Grover's search algorithm."""
        dim = 2 ** n_qubits
        state = np.ones(dim, dtype=complex) / np.sqrt(dim)
        iterations = int(np.pi / 4 * np.sqrt(dim))
        
        for _ in range(iterations):
            oracle = np.eye(dim, dtype=complex)
            oracle[marked_state, marked_state] = -1
            state = oracle @ state
            
            diffusion = 2 * np.outer(np.ones(dim), np.ones(dim)) / dim - np.eye(dim)
            state = diffusion @ state
        
        return state

    @staticmethod
    def quantum_fourier_transform(state: np.ndarray) -> np.ndarray:
        """Quantum Fourier Transform."""
        n = len(state)
        qft_matrix = np.zeros((n, n), dtype=complex)
        for j in range(n):
            for k in range(n):
                qft_matrix[j, k] = np.exp(2j * np.pi * j * k / n) / np.sqrt(n)
        return qft_matrix @ state

    def __repr__(self) -> str:
        return "QuantumAlgorithms()"
