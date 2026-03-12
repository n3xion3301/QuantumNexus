"""Quantum Key Distribution demonstrations."""

import sys
sys.path.insert(0, '..')

from quantum_nexus.quantum_key_distribution import QuantumKeyDistribution


def demo_bb84():
    """Demonstrate BB84 quantum key distribution."""
    print("=== BB84 Quantum Key Distribution ===")
    qkd = QuantumKeyDistribution()
    
    # Run BB84 protocol
    result = qkd.bb84_protocol(n_qubits=100)
    
    print(f"Qubits transmitted: 100")
    print(f"Sifted key length: {result['key_length']}")
    print(f"Quantum bit error rate: {result['error_rate']:.3f}")
    print(f"Eavesdropping detected: {result['eavesdropping_detected']}")
    print(f"Secure key: {result['sifted_key'][:20]}...")


def demo_secure_communication():
    """Demonstrate secure communication."""
    print("\n=== Secure Communication ===")
    qkd = QuantumKeyDistribution()
    
    # Generate secure key
    result = qkd.bb84_protocol(n_qubits=256)
    secure_key = qkd.get_secure_key()
    
    print(f"Secure key length: {len(secure_key)} bits")
    print(f"Key can be used for encryption")
    print(f"Security guaranteed by quantum mechanics")


if __name__ == "__main__":
    demo_bb84()
    demo_secure_communication()
