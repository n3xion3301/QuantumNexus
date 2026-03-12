"""Network Quantum Computing - Distributed quantum computation."""

import numpy as np
from typing import List, Dict, Tuple


class QuantumNode:
    """Represents a quantum computing node in the network."""

    def __init__(self, node_id: int, n_qubits: int = 2):
        """Initialize quantum node.
        
        Args:
            node_id: Unique node identifier
            n_qubits: Number of qubits on this node
        """
        self.node_id = node_id
        self.n_qubits = n_qubits
        self.state = np.zeros(2**n_qubits, dtype=complex)
        self.state[0] = 1.0  # Initialize to |0...0⟩
        self.operations_log = []

    def apply_gate(self, gate: np.ndarray) -> None:
        """Apply quantum gate to local state."""
        self.state = gate @ self.state
        self.operations_log.append({"type": "gate", "gate": gate})

    def measure(self) -> int:
        """Measure local qubits."""
        probabilities = np.abs(self.state)**2
        result = np.random.choice(len(self.state), p=probabilities)
        self.operations_log.append({"type": "measurement", "result": result})
        return result

    def get_state(self) -> np.ndarray:
        """Get current quantum state."""
        return self.state.copy()

    def __repr__(self) -> str:
        return f"QuantumNode(id={self.node_id}, qubits={self.n_qubits})"


class QuantumNetwork:
    """Quantum computing network with multiple nodes."""

    def __init__(self, n_nodes: int, qubits_per_node: int = 2):
        """Initialize quantum network.
        
        Args:
            n_nodes: Number of nodes in network
            qubits_per_node: Qubits per node
        """
        self.nodes = [QuantumNode(i, qubits_per_node) for i in range(n_nodes)]
        self.entanglement_map = {}
        self.communication_log = []

    def entangle_nodes(self, node1_id: int, node2_id: int) -> None:
        """Create entanglement between two nodes."""
        self.entanglement_map[(node1_id, node2_id)] = True
        self.communication_log.append({
            "type": "entanglement",
            "nodes": (node1_id, node2_id)
        })

    def send_classical_bit(self, from_node: int, to_node: int, bit: int) -> None:
        """Send classical bit between nodes."""
        self.communication_log.append({
            "type": "classical_communication",
            "from": from_node,
            "to": to_node,
            "bit": bit
        })

    def distributed_computation(self, computation_type: str) -> Dict:
        """Execute distributed quantum computation.
        
        Args:
            computation_type: Type of computation
            
        Returns:
            Computation results
        """
        results = {}
        
        if computation_type == "parallel_measurement":
            results["measurements"] = [node.measure() for node in self.nodes]
        
        elif computation_type == "distributed_search":
            # Simplified distributed Grover search
            for node in self.nodes:
                hadamard = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
                node.apply_gate(hadamard)
            results["states"] = [node.get_state() for node in self.nodes]
        
        return results

    def get_network_state(self) -> List[np.ndarray]:
        """Get states from all nodes."""
        return [node.get_state() for node in self.nodes]

    def get_communication_overhead(self) -> Dict:
        """Calculate communication overhead."""
        classical_bits = sum(1 for log in self.communication_log 
                           if log["type"] == "classical_communication")
        entanglements = sum(1 for log in self.communication_log 
                          if log["type"] == "entanglement")
        
        return {
            "classical_bits_sent": classical_bits,
            "entanglements_created": entanglements,
            "total_communications": len(self.communication_log)
        }

    def __repr__(self) -> str:
        return f"QuantumNetwork(nodes={len(self.nodes)})"
