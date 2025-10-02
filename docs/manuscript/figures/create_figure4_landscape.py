#!/usr/bin/env python3
"""
Create Figure 4: Comparative Landscape of NAM Databases and NAMO Integration
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.lines as mlines
import numpy as np

# Set up the figure with two subplots
fig = plt.figure(figsize=(14, 8))

# Panel A: Fragmented landscape
ax1 = plt.subplot(1, 2, 1)
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
ax1.set_title('A. Current State: Fragmented Databases', fontsize=12, fontweight='bold')

# Database colors
db_colors = {
    'organoiddb': '#8DD3C7',
    'mpsdb': '#FFFFB3',
    'cellpass': '#BEBADA',
    'comptox': '#FB8072',
    'namo': '#2E86AB'
}

# Panel A: Draw isolated databases
databases_a = [
    ('OrganoidDB', (2.5, 7.5), db_colors['organoiddb'], '16,218 organoids\nTranscriptomics'),
    ('MPS-DB', (7.5, 7.5), db_colors['mpsdb'], '32 MPS models\nPharmacokinetics'),
    ('Cell Model\nPassports', (2.5, 2.5), db_colors['cellpass'], '2,000 cancer models\nGenomics'),
    ('CompTox', (7.5, 2.5), db_colors['comptox'], '900,000 chemicals\nToxicity')
]

for name, pos, color, description in databases_a:
    # Draw database box
    rect = FancyBboxPatch((pos[0]-1.5, pos[1]-1), 3, 2,
                          boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor='black',
                          linewidth=2, alpha=0.8)
    ax1.add_patch(rect)
    ax1.text(pos[0], pos[1]+0.3, name, ha='center', va='center',
            fontsize=10, fontweight='bold')
    ax1.text(pos[0], pos[1]-0.3, description, ha='center', va='center',
            fontsize=8, style='italic')

# Add "no connection" symbols (X marks)
no_connect_positions = [(5, 7.5), (5, 2.5), (2.5, 5), (7.5, 5)]
for pos in no_connect_positions:
    ax1.plot([pos[0]-0.3, pos[0]+0.3], [pos[1]-0.3, pos[1]+0.3],
            'r-', linewidth=3, alpha=0.5)
    ax1.plot([pos[0]-0.3, pos[0]+0.3], [pos[1]+0.3, pos[1]-0.3],
            'r-', linewidth=3, alpha=0.5)

# Add problems text
problems = ['• Incompatible schemas', '• No cross-references', '• Limited interoperability',
            '• Siloed communities']
for i, problem in enumerate(problems):
    ax1.text(5, 0.5 - i*0.3, problem, ha='center', va='center',
            fontsize=8, color='red')

# Panel B: NAMO Integration
ax2 = plt.subplot(1, 2, 2)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_title('B. With NAMO: Semantic Integration', fontsize=12, fontweight='bold')

# Central NAMO hub
namo_center = (5, 5)
namo_circle = Circle(namo_center, 1.2, facecolor=db_colors['namo'],
                     edgecolor='black', linewidth=3, zorder=10)
ax2.add_patch(namo_circle)
ax2.text(namo_center[0], namo_center[1]+0.2, 'NAMO',
        ha='center', va='center', fontsize=12,
        fontweight='bold', color='white')
ax2.text(namo_center[0], namo_center[1]-0.3, 'Semantic\nBridge',
        ha='center', va='center', fontsize=8, color='white')

# Panel B: Connected databases
databases_b = [
    ('OrganoidDB', (2.5, 7.5), db_colors['organoiddb']),
    ('MPS-DB', (7.5, 7.5), db_colors['mpsdb']),
    ('Cell Model\nPassports', (2.5, 2.5), db_colors['cellpass']),
    ('CompTox', (7.5, 2.5), db_colors['comptox'])
]

for name, pos, color in databases_b:
    # Draw database box
    rect = FancyBboxPatch((pos[0]-1.2, pos[1]-0.8), 2.4, 1.6,
                          boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor='black',
                          linewidth=2, alpha=0.8)
    ax2.add_patch(rect)
    ax2.text(pos[0], pos[1], name, ha='center', va='center',
            fontsize=9, fontweight='bold')

    # Draw bidirectional arrows to NAMO
    arrow1 = FancyArrowPatch(pos, namo_center,
                            connectionstyle="arc3,rad=.2",
                            arrowstyle='<->', mutation_scale=15,
                            linewidth=2, color='green', alpha=0.6)
    ax2.add_patch(arrow1)

# Add integration benefits
benefits = [
    (5, 8.5, 'Cross-platform\nqueries'),
    (8.5, 6, 'Unified\nvalidation'),
    (5, 1.5, 'Regulatory\nalignment'),
    (1.5, 6, 'Semantic\ninteroperability')
]

for x, y, benefit in benefits:
    ax2.text(x, y, benefit, ha='center', va='center',
            fontsize=8, color='green',
            bbox=dict(boxstyle="round,pad=0.2",
                     facecolor='#E6FFE6',
                     edgecolor='green', linewidth=1))

# Add data flow indicators
flow_angles = [45, 135, 225, 315]
for angle in flow_angles:
    rad = np.radians(angle)
    x_start = namo_center[0] + 0.8 * np.cos(rad)
    y_start = namo_center[1] + 0.8 * np.sin(rad)
    x_end = namo_center[0] + 1.5 * np.cos(rad)
    y_end = namo_center[1] + 1.5 * np.sin(rad)

    ax2.plot([x_start, x_end], [y_start, y_end], 'g--',
            linewidth=1, alpha=0.5)

# Overall title
fig.suptitle('Figure 4: Comparative Landscape of NAM Databases',
            fontsize=14, fontweight='bold', y=0.98)

# Save figure
plt.tight_layout()
plt.savefig('figure4_database_landscape.pdf', dpi=300, bbox_inches='tight')
plt.savefig('figure4_database_landscape.png', dpi=300, bbox_inches='tight')
# plt.show()  # Commented out for non-interactive execution

print("Figure 4 created successfully!")