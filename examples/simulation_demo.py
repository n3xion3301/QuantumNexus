"""Quantum simulation demonstrations."""

import sys
sys.path.insert(0, '..')

from quantum_nexus.quantum_simulation import QuantumSimulation
import numpy as np


def demo_time_evolution():
    """Demonstrate time evolution."""
    print("=== Time Evolution ===")
    
    # Simple 2-qubit Hamiltonian
    H = np.array([
        [1, 0.5, 0, 0],
        [0.5, -1, 0, 0],
        [0, 0, 0.5, 0.2],
        [0, 0, 0.2, -0.5]
    ], dtype=complex)
    
    sim = QuantumSimulation(H)
    
    # Initial state |00⟩
    initial_state = np.array([1, 0, 0, 0], dtype=complex)
    
    print("Time evolution:")
    for t in [0, 0.5, 1.0, 1.5, 2.0]:
        evolved = sim.time_evolution(initial_state, t)
        prob_00 = np.abs(evolved[0])**2
        print(f"  t={t}: P(|00⟩) = {prob_00:.3f}")


def demo_ground_state():
    """Demonstrate ground state calculation."""
    print("\n=== Ground State ===")
    
    # Pauli Z Hamiltonian
    H = np.array([[1, 0], [0, -1]], dtype=complex)
    
    sim = QuantumSimulation(H)
    energy, state = sim.ground_state()
    
    print(f"Ground state energy: {energy:.3f}")
    print(f"Ground state: {state}")


if __name__ == "__main__":
    demo_time_evolution()
    demo_ground_state()
