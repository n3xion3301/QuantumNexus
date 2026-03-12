"""Quantum algorithms demonstrations."""

import sys
sys.path.insert(0, '..')

from quantum_nexus.quantum_algorithms import QuantumAlgorithms
import numpy as np


def demo_grover():
    """Demonstrate Grover's algorithm."""
    print("=== Grover's Search Algorithm ===")
    algo = QuantumAlgorithms()
    
    marked_state = 5
    n_qubits = 3
    
    result_state = algo.grover_search(marked_state, n_qubits)
    probabilities = np.abs(result_state) ** 2
    
    print(f"Searching for state {marked_state} in {2**n_qubits} states")
    print(f"Probability of marked state: {probabilities[marked_state]:.3f}")
    print(f"Other probabilities: {[f'{p:.3f}' for p in probabilities if p > 0.01]}")


def demo_qft():
    """Demonstrate Quantum Fourier Transform."""
    print("\n=== Quantum Fourier Transform ===")
    algo = QuantumAlgorithms()
    
    # Simple state
    state = np.array([1, 0, 0, 0], dtype=complex)
    qft_state = algo.quantum_fourier_transform(state)
    
    print(f"Input state: {state}")
    print(f"QFT output: {qft_state}")


if __name__ == "__main__":
    demo_grover()
    demo_qft()
