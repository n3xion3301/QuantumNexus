"""Entanglement demonstrations."""

import sys
sys.path.insert(0, '..')

from quantum_nexus.entanglement import Entanglement
import numpy as np


def demo_bell_states():
    """Demonstrate Bell states."""
    print("=== Bell States ===")
    ent = Entanglement()
    
    bell_types = ["00", "01", "10", "11"]
    for bell_type in bell_types:
        state = ent.create_bell_pair(bell_type)
        entropy = ent.measure_entanglement_entropy(state)
        print(f"Bell state |{bell_type}⟩: entropy = {entropy:.3f}")
        print(f"  State: {state}")


def demo_ghz_state():
    """Demonstrate GHZ state."""
    print("\n=== GHZ State ===")
    ent = Entanglement()
    
    for n in [2, 3, 4]:
        state = ent.create_ghz_state(n)
        entropy = ent.measure_entanglement_entropy(state)
        print(f"{n}-qubit GHZ state: entropy = {entropy:.3f}")


def demo_w_state():
    """Demonstrate W state."""
    print("\n=== W State ===")
    ent = Entanglement()
    
    for n in [2, 3, 4]:
        state = ent.create_w_state(n)
        entropy = ent.measure_entanglement_entropy(state)
        print(f"{n}-qubit W state: entropy = {entropy:.3f}")


def demo_bell_inequality():
    """Demonstrate Bell inequality."""
    print("\n=== Bell Inequality ===")
    ent = Entanglement()
    
    # Simulate measurements
    measurements = [(1, 1), (1, -1), (-1, 1), (-1, -1)] * 25
    chsh = ent.check_bell_inequality(measurements)
    print(f"CHSH parameter: {chsh:.3f}")
    print(f"Classical limit: 2.0")
    print(f"Quantum limit: 2√2 ≈ 2.828")
    print(f"Violation: {chsh > 2}")


if __name__ == "__main__":
    demo_bell_states()
    demo_ghz_state()
    demo_w_state()
    demo_bell_inequality()
