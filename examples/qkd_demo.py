"""Real Quantum Key Distribution Demo."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from quantum_nexus.quantum_key_distribution import QuantumKeyDistribution
import numpy as np


def demo_bb84():
    """Demonstrate BB84 protocol."""
    print("=== BB84 Quantum Key Distribution ===\n")
    
    qkd = QuantumKeyDistribution()
    
    # Generate key
    result = qkd.bb84_protocol(n_qubits=256)
    
    print(f"Qubits transmitted: 256")
    print(f"Sifted key length: {result['key_length']} bits")
    print(f"Quantum bit error rate: {result['error_rate']:.4f}")
    print(f"Eavesdropping detected: {result['eavesdropping_detected']}")
    print(f"\nSecure key generated!")
    print(f"Key length: {result['key_length']} bits")


if __name__ == "__main__":
    demo_bb84()
