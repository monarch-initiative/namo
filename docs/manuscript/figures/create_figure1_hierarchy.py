#!/usr/bin/env python3
"""
Create Figure 1: NAMO Hierarchical Schema Architecture
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Color scheme
colors = {
    'abstract': '#E8E8E8',
    'animal': '#FFE5CC',
    'cellular': '#E6F3FF',
    'mps': '#FFE6F0',
    'insilico': '#F0FFE6',
    'concrete': '#FFFFFF'
}

# Define positions
positions = {
    'ModelSystem': (7, 9),
    'AnimalModel': (3, 7),
    'NAMModel': (11, 7),
    'CellularSystem': (5, 5),
    'MicrophysiologicalSystem': (9, 5),
    'InSilicoModel': (13, 5),
    # Cellular subtypes
    'TwoDCellCulture': (2, 3),
    'ThreeDCellCulture': (4, 3),
    'Organoid': (4, 1.5),
    'CoCulture': (6, 3),
    'CellLineModel': (8, 3),
    # MPS subtypes
    'OrganOnChip': (8.5, 3),
    'TissueOnChip': (10.5, 3),
    # In Silico subtypes
    'QSARModel': (11, 3),
    'PBPKModel': (12, 3),
    'MLModel': (13, 3),
    'DigitalTwin': (12, 1.5),
    'MetabolicModel': (14, 1.5),
}

# Box properties
def create_box(ax, pos, text, color, is_abstract=False):
    """Create a box for a class"""
    width = 1.8
    height = 0.6

    if is_abstract:
        # Italic font and dashed border for abstract classes
        box = FancyBboxPatch(
            (pos[0] - width/2, pos[1] - height/2),
            width, height,
            boxstyle="round,pad=0.1",
            facecolor=color,
            edgecolor='#666666',
            linestyle='--',
            linewidth=2
        )
        font_style = 'italic'
    else:
        box = FancyBboxPatch(
            (pos[0] - width/2, pos[1] - height/2),
            width, height,
            boxstyle="round,pad=0.1",
            facecolor=color,
            edgecolor='#333333',
            linewidth=2
        )
        font_style = 'normal'

    ax.add_patch(box)
    ax.text(pos[0], pos[1], text, ha='center', va='center',
            fontsize=10, fontweight='bold' if not is_abstract else 'normal',
            fontstyle=font_style)
    return box

# Draw connections
def draw_connection(ax, start_pos, end_pos, style='solid'):
    """Draw connection between boxes"""
    arrow = ConnectionPatch(
        start_pos, end_pos, "data", "data",
        arrowstyle="->", shrinkA=30, shrinkB=30,
        mutation_scale=20, fc="black", linestyle=style,
        linewidth=1.5
    )
    ax.add_artist(arrow)

# Create boxes
create_box(ax, positions['ModelSystem'], 'ModelSystem', colors['abstract'], True)
create_box(ax, positions['AnimalModel'], 'AnimalModel', colors['animal'])
create_box(ax, positions['NAMModel'], 'NAMModel', colors['abstract'], True)

# NAM subtypes
create_box(ax, positions['CellularSystem'], 'CellularSystem', colors['cellular'], True)
create_box(ax, positions['MicrophysiologicalSystem'], 'Microphysiological\nSystem', colors['mps'], True)
create_box(ax, positions['InSilicoModel'], 'InSilicoModel', colors['insilico'], True)

# Cellular subtypes
create_box(ax, positions['TwoDCellCulture'], '2D Cell\nCulture', colors['cellular'])
create_box(ax, positions['ThreeDCellCulture'], '3D Cell\nCulture', colors['cellular'], True)
create_box(ax, positions['Organoid'], 'Organoid', colors['cellular'])
create_box(ax, positions['CoCulture'], 'Co-Culture', colors['cellular'])
create_box(ax, positions['CellLineModel'], 'Cell Line\nModel', colors['cellular'])

# MPS subtypes
create_box(ax, positions['OrganOnChip'], 'Organ-\non-Chip', colors['mps'])
create_box(ax, positions['TissueOnChip'], 'Tissue-\non-Chip', colors['mps'])

# In Silico subtypes
create_box(ax, positions['QSARModel'], 'QSAR\nModel', colors['insilico'])
create_box(ax, positions['PBPKModel'], 'PBPK\nModel', colors['insilico'])
create_box(ax, positions['MLModel'], 'ML\nModel', colors['insilico'])
create_box(ax, positions['DigitalTwin'], 'Digital\nTwin', colors['insilico'])
create_box(ax, positions['MetabolicModel'], 'Metabolic\nModel', colors['insilico'])

# Draw connections
# From ModelSystem
draw_connection(ax, positions['ModelSystem'], positions['AnimalModel'])
draw_connection(ax, positions['ModelSystem'], positions['NAMModel'])

# From NAMModel
draw_connection(ax, positions['NAMModel'], positions['CellularSystem'])
draw_connection(ax, positions['NAMModel'], positions['MicrophysiologicalSystem'])
draw_connection(ax, positions['NAMModel'], positions['InSilicoModel'])

# From CellularSystem
draw_connection(ax, positions['CellularSystem'], positions['TwoDCellCulture'])
draw_connection(ax, positions['CellularSystem'], positions['ThreeDCellCulture'])
draw_connection(ax, positions['CellularSystem'], positions['CoCulture'])
draw_connection(ax, positions['CellularSystem'], positions['CellLineModel'])

# From ThreeDCellCulture to Organoid
draw_connection(ax, positions['ThreeDCellCulture'], positions['Organoid'])

# From MicrophysiologicalSystem
draw_connection(ax, positions['MicrophysiologicalSystem'], positions['OrganOnChip'])
draw_connection(ax, positions['MicrophysiologicalSystem'], positions['TissueOnChip'])

# From InSilicoModel
draw_connection(ax, positions['InSilicoModel'], positions['QSARModel'])
draw_connection(ax, positions['InSilicoModel'], positions['PBPKModel'])
draw_connection(ax, positions['InSilicoModel'], positions['MLModel'])
draw_connection(ax, positions['InSilicoModel'], positions['DigitalTwin'])
draw_connection(ax, positions['InSilicoModel'], positions['MetabolicModel'])

# Add legend
legend_elements = [
    mpatches.Patch(facecolor=colors['abstract'], edgecolor='#666666',
                   linestyle='--', label='Abstract Class'),
    mpatches.Patch(facecolor=colors['animal'], edgecolor='#333333',
                   label='Animal Model'),
    mpatches.Patch(facecolor=colors['cellular'], edgecolor='#333333',
                   label='Cellular System'),
    mpatches.Patch(facecolor=colors['mps'], edgecolor='#333333',
                   label='Microphysiological System'),
    mpatches.Patch(facecolor=colors['insilico'], edgecolor='#333333',
                   label='In Silico Model')
]
ax.legend(handles=legend_elements, loc='lower center', ncol=5,
          bbox_to_anchor=(0.5, -0.05), frameon=False)

# Add title
plt.title('Figure 1: NAMO Hierarchical Schema Architecture',
          fontsize=14, fontweight='bold', pad=20)

# Save figure
plt.tight_layout()
plt.savefig('figure1_namo_hierarchy.pdf', dpi=300, bbox_inches='tight')
plt.savefig('figure1_namo_hierarchy.png', dpi=300, bbox_inches='tight')
# plt.show()  # Commented out for non-interactive execution

print("Figure 1 created successfully!")