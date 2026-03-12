"""Superposition demonstrations."""

import sys
sys.path.insert(0, '..')

from quantum_nexus.superposition import Superposition
import numpy as np


def demo_equal_superposition():
    """Demonstrate equal superposition."""
    print("=== Equal Superposition ===")
    sup = Superposition()
    
    # Create 2-qubit equal superposition
    state = sup.create_equal_superposition(2)
    print(f"2-qubit superposition: {state}")
    print(f"Probabilities: {sup.get_probabilities(state)}")
    
    # Measure multiple times
    print("\nMeasurement results (10 trials):")
    for _ in range(10):
        result, prob = sup.measure_superposition(state)
        print(f"  Measured state {result} with probability {prob:.3f}")


def demo_weighted_superposition():
    """Demonstrate weighted superposition."""
    print("\n=== Weighted Superposition ===")
    sup = Superposition()
    
    # Create weighted superposition
    amplitudes = [1, 0, 1, 0]  # |0⟩ + |2⟩
    state = sup.create_weighted_superposition(amplitudes)
    print(f"Weighted superposition: {state}")
    print(f"Probabilities: {sup.get_probabilities(state)}")


def demo_statistics():
    """Demonstrate measurement statistics."""
    print("\n=== Measurement Statistics ===")
    sup = Superposition()
    
    state = sup.create_equal_superposition(2)
    stats = sup.superposition_statistics(state, n_measurements=1000)
    
    print(f"Measured states: {stats['measured_states']}")
    print(f"Counts: {stats['counts']}")
    print(f"Frequencies: {[f'{f:.3f}' for f in stats['frequencies']]}")
    print(f"Theoretical: {[f'{p:.3f}' for p in stats['theoretical_probabilities']]}")


if __name__ == "__main__":
    demo_equal_superposition()
    demo_weighted_superposition()
    demo_statistics()
