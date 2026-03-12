"""Quantum Key Distribution - Secure communication using quantum mechanics."""

import numpy as np
from typing import List, Tuple, Dict


class QuantumKeyDistribution:
    """Implement BB84 quantum key distribution protocol."""

    def __init__(self):
        """Initialize QKD system."""
        self.key_log = []
        self.eavesdropping_detected = False

    def generate_random_bits(self, n: int) -> List[int]:
        """Generate random bits."""
        return [np.random.randint(0, 2) for _ in range(n)]

    def generate_random_bases(self, n: int) -> List[str]:
        """Generate random measurement bases (rectilinear or diagonal)."""
        return [np.random.choice(['rectilinear', 'diagonal']) for _ in range(n)]

    def encode_qubit(self, bit: int, basis: str) -> np.ndarray:
        """Encode classical bit into quantum state.
        
        Args:
            bit: Classical bit (0 or 1)
            basis: Measurement basis ('rectilinear' or 'diagonal')
            
        Returns:
            Quantum state
        """
        if basis == 'rectilinear':
            # |0⟩ or |1⟩
            if bit == 0:
                return np.array([1, 0], dtype=complex)
            else:
                return np.array([0, 1], dtype=complex)
        else:  # diagonal
            # |+⟩ or |-⟩
            sqrt2 = np.sqrt(2)
            if bit == 0:
                return np.array([1, 1], dtype=complex) / sqrt2
            else:
                return np.array([1, -1], dtype=complex) / sqrt2

    def measure_qubit(self, state: np.ndarray, basis: str) -> int:
        """Measure quantum state in given basis.
        
        Args:
            state: Quantum state
            basis: Measurement basis
            
        Returns:
            Measurement result (0 or 1)
        """
        if basis == 'rectilinear':
            prob_0 = np.abs(state[0])**2
        else:  # diagonal
            sqrt2 = np.sqrt(2)
            plus_state = np.array([1, 1], dtype=complex) / sqrt2
            prob_0 = np.abs(np.conj(plus_state) @ state)**2
        
        return 0 if np.random.random() < prob_0 else 1

    def bb84_protocol(self, n_qubits: int = 100) -> Dict:
        """Execute BB84 quantum key distribution protocol.
        
        Args:
            n_qubits: Number of qubits to transmit
            
        Returns:
            Dictionary with protocol results
        """
        # Alice's random bits and bases
        alice_bits = self.generate_random_bits(n_qubits)
        alice_bases = self.generate_random_bases(n_qubits)
        
        # Bob's random bases
        bob_bases = self.generate_random_bases(n_qubits)
        
        # Bob's measurement results
        bob_bits = []
        for i in range(n_qubits):
            qubit = self.encode_qubit(alice_bits[i], alice_bases[i])
            measured_bit = self.measure_qubit(qubit, bob_bases[i])
            bob_bits.append(measured_bit)
        
        # Sift keys (keep only where bases match)
        sifted_key = []
        matching_indices = []
        for i in range(n_qubits):
            if alice_bases[i] == bob_bases[i]:
                sifted_key.append(alice_bits[i])
                matching_indices.append(i)
        
        # Check for eavesdropping
        error_rate = self._calculate_error_rate(alice_bits, bob_bits, matching_indices)
        eavesdropping_detected = error_rate > 0.11  # Threshold for BB84
        
        result = {
            "alice_bits": alice_bits,
            "alice_bases": alice_bases,
            "bob_bases": bob_bases,
            "bob_bits": bob_bits,
            "sifted_key": sifted_key,
            "key_length": len(sifted_key),
            "error_rate": error_rate,
            "eavesdropping_detected": eavesdropping_detected
        }
        
        self.key_log.append(result)
        self.eavesdropping_detected = eavesdropping_detected
        
        return result

    def _calculate_error_rate(self, alice_bits: List[int], bob_bits: List[int], 
                             indices: List[int]) -> float:
        """Calculate quantum bit error rate."""
        if not indices:
            return 0.0
        
        errors = sum(1 for i in indices if alice_bits[i] != bob_bits[i])
        return errors / len(indices)

    def get_secure_key(self) -> List[int]:
        """Get the final secure key from last protocol execution."""
        if self.key_log:
            return self.key_log[-1]["sifted_key"]
        return []

    def __repr__(self) -> str:
        return f"QuantumKeyDistribution(keys_generated={len(self.key_log)})"
