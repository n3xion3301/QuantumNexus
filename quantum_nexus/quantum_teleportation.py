"""Quantum Teleportation - Transfer quantum states via classical channels."""

import numpy as np
from typing import Tuple, List


class QuantumTeleportation:
    """Implement quantum teleportation protocol."""

    def __init__(self):
        """Initialize teleportation system."""
        self.teleportation_log = []

    def create_bell_pair(self) -> Tuple[np.ndarray, np.ndarray]:
        """Create entangled Bell pair for teleportation."""
        sqrt2 = np.sqrt(2)
        # |Φ+⟩ = (|00⟩ + |11⟩)/√2
        bell_state = np.array([1, 0, 0, 1], dtype=complex) / sqrt2
        return bell_state, bell_state

    def encode_state(self, state: np.ndarray) -> np.ndarray:
        """Encode quantum state for teleportation."""
        return state.copy()

    def bell_measurement(self, qubit1: np.ndarray, qubit2: np.ndarray) -> Tuple[int, int]:
        """Perform Bell measurement on two qubits.
        
        Returns:
            Tuple of (bit1, bit2) - classical bits from measurement
        """
        # Simulate measurement outcomes
        prob1 = np.abs(qubit1[0])**2
        prob2 = np.abs(qubit2[0])**2
        
        bit1 = 1 if np.random.random() < prob1 else 0
        bit2 = 1 if np.random.random() < prob2 else 0
        
        return bit1, bit2

    def apply_correction(self, state: np.ndarray, bit1: int, bit2: int) -> np.ndarray:
        """Apply correction gates based on measurement results.
        
        Args:
            state: Quantum state at receiver
            bit1: First classical bit
            bit2: Second classical bit
            
        Returns:
            Corrected state (should match original)
        """
        corrected = state.copy()
        
        # Apply Pauli corrections based on bits
        if bit1 == 1:
            # Apply Pauli Z
            pauli_z = np.array([[1, 0], [0, -1]], dtype=complex)
            corrected = pauli_z @ corrected
        
        if bit2 == 1:
            # Apply Pauli X
            pauli_x = np.array([[0, 1], [1, 0]], dtype=complex)
            corrected = pauli_x @ corrected
        
        return corrected

    def teleport(self, state: np.ndarray) -> Tuple[np.ndarray, Tuple[int, int]]:
        """Complete quantum teleportation protocol.
        
        Args:
            state: Quantum state to teleport
            
        Returns:
            Tuple of (teleported_state, classical_bits)
        """
        # Step 1: Create Bell pair
        bell_pair, _ = self.create_bell_pair()
        
        # Step 2: Bell measurement (sender)
        bit1, bit2 = self.bell_measurement(state, bell_pair)
        
        # Step 3: Send classical bits (simulated)
        classical_bits = (bit1, bit2)
        
        # Step 4: Apply correction (receiver)
        teleported_state = self.apply_correction(state, bit1, bit2)
        
        # Log teleportation
        self.teleportation_log.append({
            "original": state,
            "classical_bits": classical_bits,
            "teleported": teleported_state,
            "fidelity": self.calculate_fidelity(state, teleported_state)
        })
        
        return teleported_state, classical_bits

    def calculate_fidelity(self, state1: np.ndarray, state2: np.ndarray) -> float:
        """Calculate fidelity between original and teleported state."""
        overlap = np.abs(np.conj(state1) @ state2) ** 2
        return float(overlap)

    def teleport_multiple(self, states: List[np.ndarray]) -> List[Tuple[np.ndarray, Tuple[int, int]]]:
        """Teleport multiple quantum states."""
        results = []
        for state in states:
            teleported, bits = self.teleport(state)
            results.append((teleported, bits))
        return results

    def get_average_fidelity(self) -> float:
        """Get average fidelity of all teleportations."""
        if not self.teleportation_log:
            return 0.0
        fidelities = [log["fidelity"] for log in self.teleportation_log]
        return np.mean(fidelities)

    def __repr__(self) -> str:
        return f"QuantumTeleportation(teleportations={len(self.teleportation_log)})"
