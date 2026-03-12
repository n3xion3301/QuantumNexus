"""Quantum Teleportation demonstrations."""

import sys
sys.path.insert(0, '..')

from quantum_nexus.quantum_teleportation import QuantumTeleportation
import numpy as np


def demo_basic_teleportation():
    """Demonstrate basic quantum teleportation."""
    print("=== Quantum Teleportation ===")
    teleport = QuantumTeleportation()
    
    # Create state to teleport
    state = np.array([1, 1], dtype=complex) / np.sqrt(2)
    print(f"Original state: {state}")
    
    # Teleport
    teleported, bits = teleport.teleport(state)
    print(f"Teleported state: {teleported}")
    print(f"Classical bits sent: {bits}")
    
    # Calculate fidelity
    fidelity = teleport.calculate_fidelity(state, teleported)
    print(f"Fidelity: {fidelity:.3f}")


def demo_multiple_teleportations():
    """Demonstrate multiple teleportations."""
    print("\n=== Multiple Teleportations ===")
    teleport = QuantumTeleportation()
    
    # Create multiple states
    states = [
        np.array([1, 0], dtype=complex),
        np.array([0, 1], dtype=complex),
        np.array([1, 1], dtype=complex) / np.sqrt(2)
    ]
    
    results = teleport.teleport_multiple(states)
    
    print(f"Teleported {len(results)} states")
    print(f"Average fidelity: {teleport.get_average_fidelity():.3f}")


if __name__ == "__main__":
    demo_basic_teleportation()
    demo_multiple_teleportations()
