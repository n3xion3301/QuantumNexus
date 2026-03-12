"""Quantum gates demonstrations."""

import sys
sys.path.insert(0, '..')

from quantum_nexus.quantum_gates import QuantumGates
import numpy as np


def demo_pauli_gates():
    """Demonstrate Pauli gates."""
    print("=== Pauli Gates ===")
    gates = QuantumGates()
    
    # Initial state |0⟩
    state = np.array([1, 0], dtype=complex)
    print(f"Initial state |0⟩: {state}")
    
    # Apply Pauli X
    x_state = gates.apply_gate(state, gates.pauli_x())
    print(f"After Pauli X: {x_state}")
    
    # Apply Pauli Z
    z_state = gates.apply_gate(state, gates.pauli_z())
    print(f"After Pauli Z: {z_state}")


def demo_hadamard():
    """Demonstrate Hadamard gate."""
    print("\n=== Hadamard Gate ===")
    gates = QuantumGates()
    
    state = np.array([1, 0], dtype=complex)
    h_state = gates.apply_gate(state, gates.hadamard())
    print(f"|0⟩ after Hadamard: {h_state}")
    print(f"This is |+⟩ = (|0⟩ + |1⟩)/√2")


def demo_gate_sequence():
    """Demonstrate gate sequences."""
    print("\n=== Gate Sequences ===")
    gates = QuantumGates()
    
    state = np.array([1, 0], dtype=complex)
    sequence = [gates.hadamard(), gates.pauli_z(), gates.hadamard()]
    final_state = gates.apply_sequence(state, sequence)
    print(f"Initial: {state}")
    print(f"After H-Z-H: {final_state}")


def demo_cnot():
    """Demonstrate CNOT gate."""
    print("\n=== CNOT Gate ===")
    gates = QuantumGates()
    
    # Initial state |00⟩
    state = np.array([1, 0, 0, 0], dtype=complex)
    cnot = gates.cnot_gate()
    result = gates.apply_gate(state, cnot)
    print(f"|00⟩ after CNOT: {result}")


if __name__ == "__main__":
    demo_pauli_gates()
    demo_hadamard()
    demo_gate_sequence()
    demo_cnot()
