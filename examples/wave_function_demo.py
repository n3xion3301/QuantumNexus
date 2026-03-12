"""Wave function demonstrations."""

import sys
sys.path.insert(0, '..')

from quantum_nexus.wave_function import WaveFunction
import numpy as np


def demo_gaussian_packet():
    """Demonstrate Gaussian wave packet."""
    print("=== Gaussian Wave Packet ===")
    wf = WaveFunction()
    
    psi = wf.gaussian_wavepacket(x0=0, sigma=1, k0=2)
    x_exp = wf.expectation_position(psi)
    p_exp = wf.expectation_momentum(psi)
    
    print(f"⟨x⟩ = {x_exp:.3f}")
    print(f"⟨p⟩ = {p_exp:.3f}")
    
    delta_x, delta_p, product = wf.uncertainty_principle(psi)
    print(f"Δx = {delta_x:.3f}")
    print(f"Δp = {delta_p:.3f}")
    print(f"Δx·Δp = {product:.3f} (minimum: ℏ/2 ≈ 0.5)")


def demo_particle_in_box():
    """Demonstrate particle in a box."""
    print("\n=== Particle in a Box ===")
    wf = WaveFunction()
    
    for n in [1, 2, 3]:
        psi = wf.particle_in_box(n=n, box_width=1)
        x_exp = wf.expectation_position(psi)
        print(f"State n={n}: ⟨x⟩ = {x_exp:.3f}")


def demo_harmonic_oscillator():
    """Demonstrate harmonic oscillator."""
    print("\n=== Harmonic Oscillator ===")
    wf = WaveFunction()
    
    for n in [0, 1, 2]:
        psi = wf.harmonic_oscillator(n=n, omega=1)
        x_exp = wf.expectation_position(psi)
        print(f"State n={n}: ⟨x⟩ = {x_exp:.3f}")


if __name__ == "__main__":
    demo_gaussian_packet()
    demo_particle_in_box()
    demo_harmonic_oscillator()
