"""Qiskit Aer Quantum Simulator Integration."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
    from qiskit_aer import AerSimulator
    import numpy as np
    
    print("=" * 60)
    print("QISKIT AER QUANTUM SIMULATOR")
    print("=" * 60)
    
    # Create a simple Bell state circuit
    qr = QuantumRegister(2, 'q')
    cr = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qr, cr)
    
    # Create Bell pair
    circuit.h(qr[0])
    circuit.cx(qr[0], qr[1])
    circuit.measure(qr, cr)
    
    print("\n✓ Bell State Circuit created")
    print(circuit)
    
    # Simulate
    simulator = AerSimulator()
    job = simulator.run(circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    
    print("\n✓ Simulation Results:")
    print(f"  Counts: {counts}")
    print(f"  Fidelity: {max(counts.values())/1000:.4f}")
    
except ImportError:
    print("❌ Qiskit Aer not installed")
    print("Run: pip install qiskit-aer")
