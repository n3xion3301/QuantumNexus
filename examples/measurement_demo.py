"""Measurement demonstrations."""

import sys
sys.path.insert(0, '..')

from quantum_nexus.measurement import Measurement
from quantum_nexus.quantum_gates import QuantumGates
import numpy as np


def demo_computational_basis():
    """Demonstrate computational basis measurement."""
    print("=== Computational Basis Measurement ===")
    meas = Measurement()
    gates = QuantumGates()
    
    # Create superposition
    state = np.array([1, 1], dtype=complex) / np.sqrt(2)
    print(f"Superposition state: {state}")
    
    print("\nMeasurement results (10 trials):")
    for _ in range(10):
        result, prob = meas.measure_computational_basis(state)
        print(f"  Measured {result} with probability {prob:.3f}")


def demo_observable_measurement():
    """Demonstrate observable measurement."""
    print("\n=== Observable Measurement ===")
    meas = Measurement()
    
    state = np.array([1, 1], dtype=complex) / np.sqrt(2)
    
    pauli_x_exp = meas.measure_pauli_x(state)
    pauli_z_exp = meas.measure_pauli_z(state)
    
    print(f"⟨X⟩ = {pauli_x_exp:.3f}")
    print(f"⟨Z⟩ = {pauli_z_exp:.3f}")


def demo_repeated_measurements():
    """Demonstrate repeated measurements."""
    print("\n=== Repeated Measurements ===")
    meas = Measurement()
    
    state = np.array([1, 1], dtype=complex) / np.sqrt(2)
    stats = meas.repeated_measurements(state, n_measurements=1000)
    
    print(f"Measured states: {stats['measured_states']}")
    print(f"Frequencies: {[f'{f:.3f}' for f in stats['frequencies']]}")


if __name__ == "__main__":
    demo_computational_basis()
    demo_observable_measurement()
    demo_repeated_measurements()
