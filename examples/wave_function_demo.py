"""Real Wave Function Demonstrations."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from quantum_nexus.wave_function import WaveFunction
import numpy as np


def demo_gaussian_packet():
    """Demonstrate Gaussian wave packet."""
    print("=== Gaussian Wave Packet ===")
    wf = WaveFunction()
    
    # Create Gaussian packet
    x = np.linspace(-5, 5, 100)
    sigma = 1.0
    k0 = 2.0
    psi = np.exp(-(x**2)/(2*sigma**2)) * np.exp(1j*k0*x)
    psi = psi / np.linalg.norm(psi)
    
    # Calculate expectation values
    exp_x = np.sum(np.abs(psi)**2 * x)
    exp_p = k0
    
    print(f"⟨x⟩ = {exp_x:.3f}")
    print(f"⟨p⟩ = {exp_p:.3f}")
    print(f"Packet width: {sigma:.3f}")


def demo_particle_in_box():
    """Demonstrate particle in a box."""
    print("\n=== Particle in a Box ===")
    wf = WaveFunction()
    
    # Ground state (n=1)
    n = 1
    L = 1.0
    x = np.linspace(0, L, 100)
    psi = np.sqrt(2/L) * np.sin(n * np.pi * x / L)
    
    # Energy
    energy = (n**2 * np.pi**2) / (2 * L**2)
    
    print(f"Ground state (n={n})")
    print(f"Energy: {energy:.4f}")
    print(f"Normalization: {np.sum(np.abs(psi)**2):.4f}")


def demo_harmonic_oscillator():
    """Demonstrate quantum harmonic oscillator."""
    print("\n=== Quantum Harmonic Oscillator ===")
    wf = WaveFunction()
    
    # Ground state
    x = np.linspace(-5, 5, 100)
    omega = 1.0
    psi = (np.pi**(-0.25)) * np.exp(-x**2/2)
    
    # Energy
    energy = 0.5 * omega
    
    print(f"Ground state energy: {energy:.4f}")
    print(f"Normalization: {np.sum(np.abs(psi)**2):.4f}")
    print(f"Peak amplitude: {np.max(np.abs(psi)):.4f}")


if __name__ == "__main__":
    demo_gaussian_packet()
    demo_particle_in_box()
    demo_harmonic_oscillator()
