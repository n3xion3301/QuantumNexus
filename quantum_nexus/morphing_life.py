"""Morphing Life - Dynamic quantum state transformations."""

import numpy as np
from typing import List, Callable, Dict


class MorphingLife:
    """Dynamic quantum state transformations and adaptive quantum systems."""

    def __init__(self, initial_state: np.ndarray):
        """Initialize morphing life system.
        
        Args:
            initial_state: Initial quantum state
        """
        self.state = initial_state
        self.history = [initial_state.copy()]
        self.transformation_count = 0

    def apply_evolution(self, hamiltonian: np.ndarray, time: float) -> np.ndarray:
        """Apply quantum evolution under Hamiltonian.
        
        Args:
            hamiltonian: Hamiltonian matrix
            time: Evolution time
            
        Returns:
            Evolved quantum state
        """
        eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
        evolution_op = eigenvectors @ np.diag(np.exp(-1j * eigenvalues * time)) @ np.conj(eigenvectors.T)
        self.state = evolution_op @ self.state
        self.history.append(self.state.copy())
        return self.state

    def morph_to_state(self, target_state: np.ndarray, steps: int = 10) -> List[np.ndarray]:
        """Gradually morph current state to target state.
        
        Args:
            target_state: Target quantum state
            steps: Number of morphing steps
            
        Returns:
            List of intermediate states
        """
        morphing_path = []
        for i in range(steps + 1):
            alpha = i / steps
            intermediate = (1 - alpha) * self.state + alpha * target_state
            intermediate = intermediate / np.linalg.norm(intermediate)
            morphing_path.append(intermediate)
        
        self.state = morphing_path[-1]
        self.history.extend(morphing_path)
        self.transformation_count += 1
        return morphing_path

    def adaptive_transformation(self, feedback: float, learning_rate: float = 0.1) -> np.ndarray:
        """Apply adaptive transformation based on feedback.
        
        Args:
            feedback: Feedback signal for adaptation
            learning_rate: Learning rate for adaptation
            
        Returns:
            Transformed state
        """
        phase_shift = learning_rate * feedback
        transformation = np.diag(np.exp(1j * phase_shift * np.arange(len(self.state))))
        self.state = transformation @ self.state
        self.history.append(self.state.copy())
        self.transformation_count += 1
        return self.state

    def oscillate(self, frequency: float, duration: float, steps: int = 100) -> List[np.ndarray]:
        """Create oscillating quantum state.
        
        Args:
            frequency: Oscillation frequency
            duration: Total duration
            steps: Number of time steps
            
        Returns:
            List of oscillating states
        """
        oscillation_path = []
        times = np.linspace(0, duration, steps)
        
        for t in times:
            phase = 2 * np.pi * frequency * t
            oscillating_state = self.state * np.exp(1j * phase)
            oscillation_path.append(oscillating_state)
        
        self.history.extend(oscillation_path)
        return oscillation_path

    def get_state_purity(self) -> float:
        """Calculate purity of current state.
        
        Returns:
            Purity value (1 = pure state, <1 = mixed state)
        """
        density_matrix = np.outer(self.state, np.conj(self.state))
        purity = np.real(np.trace(density_matrix @ density_matrix))
        return float(purity)

    def reset_to_initial(self) -> np.ndarray:
        """Reset to initial state."""
        self.state = self.history[0].copy()
        return self.state

    def get_history(self) -> List[np.ndarray]:
        """Get transformation history."""
        return self.history

    def __repr__(self) -> str:
        return f"MorphingLife(transformations={self.transformation_count}, purity={self.get_state_purity():.3f})"
