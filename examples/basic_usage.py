"""Basic usage examples for Quantum Nexus."""

import sys
sys.path.insert(0, '..')

from quantum_nexus import AxiomKey, QuantumMechanics, DoppelgangerEntrapment, MorphingLife
import numpy as np


def example_axiom_key():
    """Example: Using Axiom Key."""
    print("=== Axiom Key Example ===")
    axiom = AxiomKey()
    
    print(f"\nFundamental Axioms:")
    for axiom_name in axiom.list_axioms():
        print(f"  - {axiom_name}: {axiom.get_axiom(axiom_name)}")
    
    frequency = 1e15
    energy = axiom.calculate_energy_frequency(frequency)
    print(f"\nEnergy at {frequency:.2e} Hz: {energy:.3e} Joules")
    
    momentum = 1e-24
    wavelength = axiom.calculate_wavelength(momentum)
    print(f"de Broglie wavelength at momentum {momentum:.2e}: {wavelength:.3e} m")


def example_quantum_mechanics():
    """Example: Quantum Mechanics operations."""
    print("\n=== Quantum Mechanics Example ===")
    qm = QuantumMechanics(dimension=2)
    
    state = qm.create_superposition([1, 1])
    print(f"\nSuperposition state: {state}")
    
    prob_0 = qm.measure_probability(state, 0)
    prob_1 = qm.measure_probability(state, 1)
    print(f"Probability of |0⟩: {prob_0:.3f}")
    print(f"Probability of |1⟩: {prob_1:.3f}")
    
    hadamard = qm.hadamard_gate()
    new_state = qm.apply_gate(state, hadamard)
    print(f"\nState after Hadamard: {new_state}")


def example_doppelganger_entrapment():
    """Example: Quantum Entanglement."""
    print("\n=== Doppelganger Entrapment Example ===")
    entangle = DoppelgangerEntrapment()
    
    bell_state = entangle.create_bell_state("00")
    print(f"\nBell state |Φ+⟩: {bell_state}")
    
    entanglement = entangle.measure_entanglement(bell_state)
    print(f"Entanglement measure: {entanglement:.3f}")
    
    ghz_state = entangle.create_ghz_state(3)
    print(f"\nGHZ state (3 qubits): {ghz_state}")


def example_morphing_life():
    """Example: Morphing Life transformations."""
    print("\n=== Morphing Life Example ===")
    
    initial_state = np.array([1, 0], dtype=complex)
    morph = MorphingLife(initial_state)
    
    print(f"Initial state: {initial_state}")
    print(f"Initial purity: {morph.get_state_purity():.3f}")
    
    target_state = np.array([1, 1], dtype=complex) / np.sqrt(2)
    morphing_path = morph.morph_to_state(target_state, steps=5)
    
    print(f"\nMorphed to target state: {morph.state}")
    print(f"Final purity: {morph.get_state_purity():.3f}")
    print(f"Transformation count: {morph.transformation_count}")


if __name__ == "__main__":
    example_axiom_key()
    example_quantum_mechanics()
    example_doppelganger_entrapment()
    example_morphing_life()
    print("\n=== All examples completed ===")
