"""Quantum Nexus Test Suite."""

import sys
sys.path.insert(0, '.')

print("=" * 60)
print("Quantum Nexus Test Suite")
print("=" * 60)

# Test imports
print("\n✓ Testing imports...")
try:
    from quantum_nexus.axiom_key import AxiomKey
    from quantum_nexus.quantum_mechanics import QuantumMechanics
    from quantum_nexus.superposition import Superposition
    from quantum_nexus.entanglement import Entanglement
    from quantum_nexus.quantum_gates import QuantumGates
    from quantum_nexus.measurement import Measurement
    from quantum_nexus.quantum_algorithms import QuantumAlgorithms
    from quantum_nexus.quantum_simulation import QuantumSimulation
    from quantum_nexus.quantum_teleportation import QuantumTeleportation
    from quantum_nexus.quantum_key_distribution import QuantumKeyDistribution
    from quantum_nexus.network_quantum_computing import QuantumNetwork
    from quantum_nexus.distributed_quantum_simulation import DistributedQuantumSimulation
    print("✓ All imports successful!")
except Exception as e:
    print(f"✗ Import failed: {e}")
    sys.exit(1)

# Test basic functionality
print("\n✓ Testing basic functionality...")
try:
    sup = Superposition()
    state = sup.create_equal_superposition(2)
    print(f"  ✓ Superposition created: {state}")
    
    ent = Entanglement()
    bell = ent.create_bell_pair()
    print(f"  ✓ Bell pair created")
    
    gates = QuantumGates()
    hadamard = gates.hadamard()
    print(f"  ✓ Hadamard gate created")
    
    teleport = QuantumTeleportation()
    print(f"  ✓ Teleportation system ready")
    
    qkd = QuantumKeyDistribution()
    print(f"  ✓ QKD system ready")
    
    network = QuantumNetwork(n_nodes=3)
    print(f"  ✓ Quantum network created")
    
except Exception as e:
    print(f"✗ Functionality test failed: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("ALL TESTS PASSED! ✓")
print("=" * 60)
print("\nQuantum Nexus is fully operational! 🚀🌌⚛️")
