"""Real Quantum Simulation Demo."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from quantum_nexus.quantum_simulation import QuantumSimulation
import numpy as np


def demo_time_evolution():
    """Demonstrate time evolution."""
    print("=== Quantum Time Evolution ===\n")

    # Hamiltonian
    H = np.array([[1, 0.5], [0.5, -1]], dtype=complex)
    
    # Create simulation with hamiltonian
    sim = QuantumSimulation(hamiltonian=H)

    # Initial state
    psi0 = np.array([1, 0], dtype=complex)

    print(f"Initial state: {psi0}")
    print(f"Hamiltonian eigenvalues: {np.linalg.eigvalsh(H)}")

    # Evolve
    times = np.linspace(0, 2*np.pi, 10)
    energies = []

    for t in times:
        eigenvalues, eigenvectors = np.linalg.eigh(H)
        U = eigenvectors @ np.diag(np.exp(-1j * eigenvalues * t)) @ np.conj(eigenvectors.T)
        psi_t = U @ psi0
        energy = np.real(np.conj(psi_t) @ H @ psi_t)
        energies.append(energy)

    print(f"\nTime Evolution Results:")
    print(f"  Energy range: [{min(energies):.4f}, {max(energies):.4f}]")
    print(f"  Oscillation detected: {max(energies) - min(energies) > 0.01}")


if __name__ == "__main__":
    demo_time_evolution()
