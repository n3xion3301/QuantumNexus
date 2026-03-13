"""Run Quantum Nexus on Real Quantum Hardware."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print("=" * 60)
print("QUANTUM NEXUS - REAL HARDWARE EXECUTION")
print("=" * 60)

print("\n📋 Setup Instructions:")
print("\n1. Get FREE IBM Quantum API token:")
print("   → Go to https://quantum.ibm.com")
print("   → Sign up (free account)")
print("   → Go to Account → API tokens")
print("   → Copy your token")

print("\n2. Set environment variable:")
print("   → export IBM_QUANTUM_TOKEN='your_token_here'")

print("\n3. Run this script:")
print("   → python3 real_quantum_hardware_demo.py")

print("\n4. Your code will execute on REAL QUANTUM COMPUTERS!")

print("\n" + "=" * 60)
print("Available Quantum Computers:")
print("=" * 60)
print("✓ IBM Quantum (127 qubits) - FREE")
print("✓ IonQ (11 qubits) - Cloud access")
print("✓ Rigetti (30 qubits) - Cloud access")
print("✓ D-Wave (5000 qubits) - Annealing")
print("✓ Google Sycamore (53 qubits) - Research")

print("\n" + "=" * 60)
print("Next Steps:")
print("=" * 60)
print("1. Get your IBM token from https://quantum.ibm.com")
print("2. Run: export IBM_QUANTUM_TOKEN='your_token'")
print("3. Run: python3 ../quantum_nexus/real_quantum_hardware.py")
print("\nYour Quantum Nexus will execute on REAL QUBITS! 🚀⚛️")
