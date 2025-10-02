#!/usr/bin/env python3
"""
Create Figure 3: Ontology Integration Network
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
import numpy as np

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(12, 10))
ax.set_xlim(-7, 7)
ax.set_ylim(-6, 6)
ax.axis('off')

# Color scheme for ontologies by domain
colors = {
    'namo': '#2E86AB',
    'anatomy': '#4A90E2',
    'cell': '#7FBA00',
    'chemical': '#F25022',
    'species': '#FFB900',
    'experimental': '#737373',
    'evidence': '#5C2D91'
}

# Central NAMO node
namo_radius = 1.5
namo_circle = Circle((0, 0), namo_radius, facecolor=colors['namo'],
                     edgecolor='black', linewidth=3, zorder=10)
ax.add_patch(namo_circle)
ax.text(0, 0.3, 'NAMO', ha='center', va='center',
        fontsize=16, fontweight='bold', color='white')
ax.text(0, -0.3, 'New Approach\nMethodology\nOntology', ha='center', va='center',
        fontsize=8, color='white')

# Define positions for external ontologies (hexagonal layout)
angles = np.linspace(0, 2*np.pi, 7)[:-1]
radius = 4.5
ontology_data = [
    ('UBERON', 'Anatomy\n13,000+ terms', colors['anatomy'], 'UBERON:0002107\n(liver)'),
    ('Cell\nOntology', 'Cell Types\n2,400+ terms', colors['cell'], 'CL:0000182\n(hepatocyte)'),
    ('ChEBI', 'Chemicals\n140,000+ terms', colors['chemical'], 'CHEBI:46195\n(acetaminophen)'),
    ('NCBITaxon', 'Species\nTaxonomy', colors['species'], 'NCBITaxon:9606\n(Homo sapiens)'),
    ('OBI', 'Experimental\nDesign', colors['experimental'], 'OBI:0002119\n(cell viability)'),
    ('ECO', 'Evidence\nTypes', colors['evidence'], 'ECO:0000353\n(computational)')
]

# Draw ontology nodes and connections
for i, (angle, (name, description, color, example)) in enumerate(zip(angles, ontology_data)):
    # Calculate position
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)

    # Draw connection line
    ax.plot([0, x], [0, y], 'k-', linewidth=2, alpha=0.2, zorder=1)

    # Draw bidirectional arrow
    arrow_start_x = namo_radius * 0.8 * np.cos(angle)
    arrow_start_y = namo_radius * 0.8 * np.sin(angle)
    arrow_end_x = (radius - 1) * np.cos(angle)
    arrow_end_y = (radius - 1) * np.sin(angle)

    arrow = FancyArrowPatch((arrow_start_x, arrow_start_y),
                           (arrow_end_x * 0.8, arrow_end_y * 0.8),
                           connectionstyle="arc3,rad=0", arrowstyle='<->',
                           mutation_scale=20, linewidth=2,
                           color='black', alpha=0.6, zorder=2)
    ax.add_patch(arrow)

    # Draw ontology circle
    node_size = 0.8 if 'Taxon' in name or 'ECO' in name else 1.0
    onto_circle = Circle((x, y), node_size, facecolor=color,
                         edgecolor='black', linewidth=2,
                         alpha=0.9, zorder=5)
    ax.add_patch(onto_circle)

    # Add ontology name and description
    ax.text(x, y + 0.2, name, ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')
    ax.text(x, y - 0.25, description, ha='center', va='center',
            fontsize=7, color='white')

    # Add example term box
    example_angle = angle + np.pi/12
    example_x = (radius + 1.5) * np.cos(example_angle)
    example_y = (radius + 1.5) * np.sin(example_angle)

    # Create example box
    bbox = dict(boxstyle="round,pad=0.2", facecolor='white',
                edgecolor=color, linewidth=1.5, alpha=0.95)
    ax.text(example_x, example_y, example,
            ha='center', va='center', fontsize=7,
            style='italic', bbox=bbox)

    # Draw dotted line to example
    ax.plot([x, example_x], [y, example_y], '--',
            color=color, linewidth=1, alpha=0.5)

# Add semantic relationships annotations
relationships = [
    (2.5, 2.5, 'organ_modeled'),
    (-2.5, 2.5, 'cell_types'),
    (-3, 0, 'chemicals_tested'),
    (3, 0, 'species'),
    (2.5, -2.5, 'assay_type'),
    (-2.5, -2.5, 'evidence')
]

for x, y, rel in relationships:
    ax.text(x, y, rel, ha='center', va='center',
            fontsize=8, style='italic', color='#666666',
            bbox=dict(boxstyle="round,pad=0.2", facecolor='#F0F0F0',
                     edgecolor='none', alpha=0.7))

# Add title
ax.text(0, 5.5, 'Figure 3: NAMO Ontology Integration Network',
        ha='center', va='center', fontsize=14, fontweight='bold')

# Add legend/key
legend_text = ('Semantic Integration Features:\n'
               '• Bidirectional term mapping\n'
               '• Hierarchical inheritance\n'
               '• Cross-ontology reasoning\n'
               '• Validation constraints')
ax.text(-6.5, -5, legend_text, ha='left', va='bottom',
        fontsize=8, bbox=dict(boxstyle="round,pad=0.4",
                             facecolor='#F8F8F8',
                             edgecolor='gray'))

# Save figure
plt.tight_layout()
plt.savefig('figure3_ontology_network.pdf', dpi=300, bbox_inches='tight')
plt.savefig('figure3_ontology_network.png', dpi=300, bbox_inches='tight')
# plt.show()  # Commented out for non-interactive execution

print("Figure 3 created successfully!")