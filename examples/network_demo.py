"""Real Quantum Network Demo."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from quantum_nexus.network_quantum_computing import QuantumNetwork
import numpy as np


def demo_quantum_network():
    """Demonstrate quantum network."""
    print("=== Quantum Network ===\n")

    # Create network
    network = QuantumNetwork(n_nodes=5)

    print(f"Network created with {len(network.nodes)} nodes")
    print(f"Network: {network}")

    # Entangle nodes
    print("\nEntangling nodes...")
    network.entangle_nodes(0, 1)
    network.entangle_nodes(1, 2)
    network.entangle_nodes(2, 3)
    network.entangle_nodes(3, 4)

    print(f"✓ Nodes entangled successfully")
    print(f"Network info: {network.get_network_info()}")


if __name__ == "__main__":
    demo_quantum_network()
