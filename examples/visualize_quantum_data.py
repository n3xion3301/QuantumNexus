"""Visualize quantum simulation data."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import json
from datetime import datetime

print("="*60)
print("QUANTUM NEXUS - DATA VISUALIZATION")
print("="*60)

# Generate visualization data
viz_data = {
    "timestamp": datetime.now().isoformat(),
    "visualizations": {
        "quantum_walk_path": {
            "type": "line_plot",
            "title": "Quantum Random Walk",
            "x_label": "Step",
            "y_label": "Position",
            "data": [0, -1, 0, 1, 0, 1, 0, 1, 0, -1, 0]
        },
        "phase_estimation_convergence": {
            "type": "scatter_plot",
            "title": "Phase Estimation Convergence",
            "x_label": "Iteration",
            "y_label": "Phase Error",
            "data": [0.5, 0.3, 0.15, 0.08, 0.01]
        },
        "vqe_energy_landscape": {
            "type": "heatmap",
            "title": "VQE Energy Landscape",
            "x_label": "Parameter θ",
            "y_label": "Energy",
            "min_energy": -1.5,
            "max_energy": 1.5
        },
        "qaoa_optimization": {
            "type": "contour_plot",
            "title": "QAOA Cost Function",
            "x_label": "γ (gamma)",
            "y_label": "β (beta)",
            "optimal_point": (2.4435, 2.7925)
        },
        "quantum_ml_accuracy": {
            "type": "bar_chart",
            "title": "Quantum ML Classifier Accuracy",
            "categories": ["Training", "Validation", "Test"],
            "values": [0.6667, 0.6667, 0.6667]
        },
        "system_dynamics": {
            "type": "line_plot",
            "title": "Quantum System Dynamics",
            "x_label": "Time",
            "y_label": "Energy",
            "data": [1.0] * 20
        },
        "error_mitigation_comparison": {
            "type": "bar_chart",
            "title": "Error Mitigation Results",
            "categories": ["1%", "5%", "10%", "20%"],
            "noisy": [0.4706, 0.4430, 0.4343, 0.4133],
            "mitigated": [0.4803, 0.4922, 0.5429, 0.6888]
        }
    }
}

# Save visualization data
with open('quantum_visualization_data.json', 'w') as f:
    json.dump(viz_data, f, indent=2)

print("\n✓ Visualization data generated!")
print("\nVisualization Types:")
for name, viz in viz_data["visualizations"].items():
    print(f"  • {viz['title']} ({viz['type']})")

print("\n✓ Data saved to quantum_visualization_data.json")
