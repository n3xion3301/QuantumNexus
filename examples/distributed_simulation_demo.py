"""Real Distributed Quantum Simulation Demo."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from quantum_nexus.distributed_quantum_simulation import DistributedQuantumSimulation
import numpy as np


def demo_distributed_simulation():
    """Demonstrate distributed quantum simulation."""
    print("=== Distributed Quantum Simulation ===\n")
    
    # Create distributed system
    sim = DistributedQuantumSimulation(n_nodes=4)
    
    print(f"Distributed system created with {sim.n_nodes} nodes")
    print(f"System: {sim}")
    
    # Run simulation
    print("\nRunning distributed simulation...")
    result = sim.run_distributed_simulation()
    
    print(f"Simulation complete!")
    print(f"Result: {result}")


if __name__ == "__main__":
    demo_distributed_simulation()
