"""Quantum Network demonstrations."""

import sys
sys.path.insert(0, '..')

from quantum_nexus.network_quantum_computing import QuantumNetwork


def demo_quantum_network():
    """Demonstrate quantum network."""
    print("=== Quantum Network ===")
    network = QuantumNetwork(n_nodes=4, qubits_per_node=2)
    
    print(f"Network created with {len(network.nodes)} nodes")
    
    # Entangle nodes
    network.entangle_nodes(0, 1)
    network.entangle_nodes(1, 2)
    network.entangle_nodes(2, 3)
    
    # Send classical bits
    network.send_classical_bit(0, 1, 1)
    network.send_classical_bit(1, 2, 0)
    
    # Get communication overhead
    overhead = network.get_communication_overhead()
    print(f"Classical bits sent: {overhead['classical_bits_sent']}")
    print(f"Entanglements created: {overhead['entanglements_created']}")


def demo_distributed_computation():
    """Demonstrate distributed computation."""
    print("\n=== Distributed Computation ===")
    network = QuantumNetwork(n_nodes=3, qubits_per_node=2)
    
    # Perform distributed search
    results = network.distributed_computation("distributed_search")
    print(f"Distributed search completed")
    print(f"States from {len(results['states'])} nodes")


if __name__ == "__main__":
    demo_quantum_network()
    demo_distributed_computation()
