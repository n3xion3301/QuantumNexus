"""Wave Functions - Quantum wave function operations."""

import numpy as np
from typing import Tuple


class WaveFunction:
    """Handle quantum wave functions."""

    def __init__(self, position_range: Tuple[float, float] = (-10, 10), n_points: int = 1000):
        """Initialize wave function handler."""
        self.x = np.linspace(position_range[0], position_range[1], n_points)
        self.dx = self.x[1] - self.x[0]
        self.psi = None

    def gaussian_wavepacket(self, x0: float = 0, sigma: float = 1, k0: float = 0) -> np.ndarray:
        """Create Gaussian wave packet."""
        psi = np.exp(-(self.x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k0 * self.x)
        norm = np.sqrt(np.sum(np.abs(psi)**2) * self.dx)
        self.psi = psi / norm
        return self.psi

    def particle_in_box(self, n: int = 1, box_width: float = 1) -> np.ndarray:
        """Create particle in a box eigenstate."""
        x_shifted = self.x - self.x[0]
        x_shifted = x_shifted * box_width / x_shifted[-1]
        psi = np.sqrt(2 / box_width) * np.sin(n * np.pi * x_shifted / box_width)
        self.psi = psi
        return self.psi

    def harmonic_oscillator(self, n: int = 0, omega: float = 1) -> np.ndarray:
        """Create harmonic oscillator eigenstate."""
        from scipy.special import hermite, factorial
        H_n = hermite(n)
        gaussian = np.exp(-omega * self.x**2 / 2)
        psi = (omega / np.pi)**(1/4) * H_n(np.sqrt(omega) * self.x) * gaussian
        psi = psi / np.sqrt(2**n * factorial(n))
        norm = np.sqrt(np.sum(np.abs(psi)**2) * self.dx)
        self.psi = psi / norm
        return self.psi

    def probability_density(self, psi: np.ndarray = None) -> np.ndarray:
        """Calculate probability density."""
        if psi is None:
            psi = self.psi
        return np.abs(psi)**2

    def expectation_position(self, psi: np.ndarray = None) -> float:
        """Calculate <x>."""
        if psi is None:
            psi = self.psi
        return np.real(np.sum(np.conj(psi) * self.x * psi) * self.dx)

    def expectation_momentum(self, psi: np.ndarray = None) -> float:
        """Calculate <p>."""
        if psi is None:
            psi = self.psi
        dpsi_dx = np.gradient(psi, self.dx)
        return np.real(np.sum(np.conj(psi) * (-1j) * dpsi_dx) * self.dx)

    def __repr__(self) -> str:
        return f"WaveFunction(points={len(self.x)})"
