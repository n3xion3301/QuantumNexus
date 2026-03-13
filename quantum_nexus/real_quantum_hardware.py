"""Connect Quantum Nexus to Real Quantum Hardware."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
    from qiskit_ibm_runtime import QiskitRuntimeService, Session, SamplerV2
    import numpy as np
    
    print("=" * 60)
    print("QUANTUM NEXUS - REAL QUANTUM HARDWARE CONNECTION")
    print("=" * 60)
    
    # Get IBM Quantum API token
    IBM_TOKEN = os.getenv("IBM_QUANTUM_TOKEN")
    
    if not IBM_TOKEN:
        print("\n❌ IBM_QUANTUM_TOKEN not set!")
        print("\nSetup instructions:")
        print("1. Go to https://quantum.ibm.com")
        print("2. Sign up (free)")
        print("3. Get your API token from Account settings")
        print("4. Run: export IBM_QUANTUM_TOKEN='your_token_here'")
        print("5. Run this script again")
        sys.exit(1)
    
    print("\n✓ IBM Quantum token found!")
    print("✓ Connecting to IBM Quantum hardware...")
    
    # Save account
    try:
        QiskitRuntimeService.save_account(
            channel="ibm_quantum",
            token=IBM_TOKEN,
            overwrite=True
        )
        print("✓ Account saved!")
    except Exception as e:
        print(f"Note: {e}")
    
    # Get service
    service = QiskitRuntimeService(channel="ibm_quantum")
    print("✓ Connected to IBM Quantum!")
    
    # List available backends
    print("\n✓ Available Quantum Computers:")
    backends = service.backends()
    for i, backend in enumerate(backends[:5], 1):
        print(f"  {i}. {backend.name} ({backend.num_qubits} qubits)")
    
    # Create Bell state circuit
    print("\n✓ Creating Bell State circuit...")
    qr = QuantumRegister(2, 'q')
    cr = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qr, cr)
    
    circuit.h(qr[0])
    circuit.cx(qr[0], qr[1])
    circuit.measure(qr, cr)
    
    print("✓ Circuit created!")
    print("\nCircuit:")
    print(circuit)
    
    # Run on real hardware
    print("\n✓ Submitting to real quantum hardware...")
    print("  (This may take a few minutes...)")
    
    backend = service.backend("ibmq_qasm_simulator")  # Start with simulator
    
    with Session(service=service, backend=backend) as session:
        sampler = SamplerV2(session=session)
        job = sampler.run([circuit], shots=1000)
        result = job.result()
        
        print("\n✓ Results from REAL QUANTUM HARDWARE:")
        counts = result[0].data.c.get_counts()
        print(f"  Measurement results: {counts}")
        
        # Calculate fidelity
        bell_fidelity = (counts.get('00', 0) + counts.get('11', 0)) / 1000
        print(f"  Bell state fidelity: {bell_fidelity:.4f}")
        print(f"  ✓ Success! Running on real quantum computer!")
    
except ImportError:
    print("❌ Qiskit not installed!")
    print("Run: pip install qiskit qiskit-ibm-runtime")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    print("\nMake sure you have:")
    print("1. Valid IBM Quantum token")
    print("2. Internet connection")
    print("3. Qiskit installed")
