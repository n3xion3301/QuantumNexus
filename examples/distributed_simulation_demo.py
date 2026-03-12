"""Distributed Quantum Simulation demonstrations."""

import sys
sys.path.insert(0, '..')

from quantum_nexus.distributed_quantum_simulation import DistributedQuantumSimulation
import numpy as np


def demo_distributed_evolution():
    """Demonstrate distributed quantum evolution."""
    print("=== Distributed Quantum Evolution ===")
    
    # Create Hamiltonians for each node
    hamiltonians = [
        np.array([[1, 0], [0, -1]], dtype=complex),
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex)
    ]
    
    sim = DistributedQuantumSimulation(n_nodes=3, hamiltonian_parts=hamiltonians)
    
    # Evolve system
    time_steps = [0, 0.5, 1.0, 1.5, 2.0]
    results = sim.distributed_evolution(time_steps)
    
    print(f"Simulated {len(time_steps)} time steps")
    print(f"Nodes synchronized at each step")
    
    # Get efficiency
    efficiency = sim.get_simulation_efficiency()
    print(f"Operations per node: {efficiency['operations_per_node']:.1f}")


if __name__ == "__main__":
    demo_distributed_evolution()
