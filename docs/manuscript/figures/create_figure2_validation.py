#!/usr/bin/env python3
"""
Create Figure 2: NAMO Validation and Concordance Framework
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Wedge
import numpy as np

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(12, 10))
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.axis('off')

# Color scheme for each validation dimension
colors = {
    'center': '#2E86AB',
    'molecular': '#F18F01',
    'pathway': '#C73E1D',
    'phenotype': '#A23B72',
    'functional': '#54577C',
    'statistical': '#3F7D20'
}

# Draw central hub
center_circle = Circle((0, 0), 1.5, facecolor=colors['center'],
                       edgecolor='black', linewidth=2, zorder=10)
ax.add_patch(center_circle)
ax.text(0, 0, 'Structured\nConcordance\nResult',
        ha='center', va='center', fontsize=12,
        fontweight='bold', color='white')

# Define positions for satellite components (pentagon layout)
angles = np.linspace(np.pi/2, -3*np.pi/2 + 2*np.pi, 6)[:-1]
radius = 3.5
component_positions = [(radius * np.cos(a), radius * np.sin(a)) for a in angles]
component_names = [
    'Molecular\nSimilarity',
    'Pathway\nConcordance',
    'Phenotype\nOverlap',
    'Functional\nParity',
    'Statistical\nMeasures'
]
component_colors = [
    colors['molecular'],
    colors['pathway'],
    colors['phenotype'],
    colors['functional'],
    colors['statistical']
]

# Component details
component_details = [
    ['• Gene expression\n  correlation', '• Protein abundance', '• Metabolite profiles'],
    ['• Activation scores', '• Directional\n  consistency', '• Pathway coverage'],
    ['• Disease\n  manifestations', '• Severity metrics', '• Penetrance'],
    ['• TEER values', '• Contractility', '• Barrier function'],
    ['• P-values', '• Confidence\n  intervals', '• Effect sizes']
]

# Draw components and connections
for i, (pos, name, color, details) in enumerate(zip(component_positions,
                                                     component_names,
                                                     component_colors,
                                                     component_details)):
    # Draw connection line first (so it's behind the circles)
    ax.plot([0, pos[0]], [0, pos[1]], 'k-', linewidth=2, alpha=0.3, zorder=1)

    # Draw arrow
    arrow_start_x = 1.2 * np.cos(angles[i])
    arrow_start_y = 1.2 * np.sin(angles[i])
    arrow_end_x = (radius - 1.2) * np.cos(angles[i])
    arrow_end_y = (radius - 1.2) * np.sin(angles[i])

    ax.annotate('', xy=(pos[0] - arrow_end_x/2, pos[1] - arrow_end_y/2),
                xytext=(arrow_start_x, arrow_start_y),
                arrowprops=dict(arrowstyle='<->', color='black', lw=2))

    # Draw component circle
    component_circle = Circle(pos, 1, facecolor=color,
                             edgecolor='black', linewidth=2,
                             alpha=0.8, zorder=5)
    ax.add_patch(component_circle)

    # Add component name
    ax.text(pos[0], pos[1] + 0.3, name,
            ha='center', va='center', fontsize=10,
            fontweight='bold', color='white')

    # Add details in a box below the component
    detail_box_y = pos[1] - 1.8
    detail_text = '\n'.join(details)

    # Create detail box
    bbox = dict(boxstyle="round,pad=0.3", facecolor='white',
                edgecolor=color, linewidth=1.5, alpha=0.9)
    ax.text(pos[0], detail_box_y, detail_text,
            ha='center', va='center', fontsize=8,
            bbox=bbox)

# Add annotation explaining bidirectional flow
ax.text(0, -5.5, 'Bidirectional data flow enables iterative refinement and validation',
        ha='center', va='center', fontsize=10, style='italic')

# Add title
ax.text(0, 5.5, 'Figure 2: Multi-dimensional Validation Framework',
        ha='center', va='center', fontsize=14, fontweight='bold')

# Add methodological metadata note
method_box = dict(boxstyle="round,pad=0.5", facecolor='#F0F0F0',
                  edgecolor='gray', linewidth=1, alpha=0.8)
ax.text(-5, 5, 'Each dimension includes:\n• Quantitative metrics\n• Method specifications\n• Reference datasets',
        ha='left', va='top', fontsize=8, bbox=method_box)

# Save figure
plt.tight_layout()
plt.savefig('figure2_validation_framework.pdf', dpi=300, bbox_inches='tight')
plt.savefig('figure2_validation_framework.png', dpi=300, bbox_inches='tight')
# plt.show()  # Commented out for non-interactive execution

print("Figure 2 created successfully!")