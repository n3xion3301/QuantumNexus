"""Real Quantum Algorithms Demo."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from quantum_nexus.quantum_algorithms import QuantumAlgorithms
import numpy as np


def demo_grover():
    """Demonstrate Grover's algorithm."""
    print("=== Grover's Search Algorithm ===\n")
    
    algo = QuantumAlgorithms()
    
    # Search for marked state
    marked = 5
    n_qubits = 3
    
    print(f"Searching for marked state: {marked}")
    print(f"Database size: {2**n_qubits}")
    
    result_state = algo.grover_search(marked, n_qubits)
    probabilities = np.abs(result_state) ** 2
    
    print(f"\nSearch Results:")
    print(f"  Probability of marked state: {probabilities[marked]:.4f}")
    print(f"  Success rate: {probabilities[marked]*100:.1f}%")


def demo_qft():
    """Demonstrate Quantum Fourier Transform."""
    print("\n=== Quantum Fourier Transform ===\n")
    
    algo = QuantumAlgorithms()
    
    # Create state
    state = np.array([1, 0, 0, 0], dtype=complex)
    
    print(f"Input state: {state}")
    
    qft_state = algo.quantum_fourier_transform(state)
    
    print(f"QFT output: {qft_state}")
    print(f"Output probabilities: {np.abs(qft_state)**2}")


if __name__ == "__main__":
    demo_grover()
    demo_qft()
