# Figure Requirements for NAMO Manuscript

## Figure 1: NAMO Hierarchical Schema Architecture
**Type:** Hierarchical tree diagram / dendrogram
**Purpose:** Show the class hierarchy of NAMO

**Key Elements:**
- Root: ModelSystem (abstract class)
- Level 1 branches:
  - AnimalModel
  - NAMModel
- Level 2 (under NAMModel):
  - CellularSystem
  - MicrophysiologicalSystem
  - InSilicoModel
- Level 3 (examples):
  - Under CellularSystem: TwoDCellCulture, ThreeDCellCulture, Organoid, CoCulture, CellLineModel
  - Under MicrophysiologicalSystem: OrganOnChip, TissueOnChip
  - Under InSilicoModel: QSARModel, PBPKModel, MLModel, DigitalTwin, MetabolicModel

**Design suggestions:**
- Use different colors for each major branch
- Show abstract classes in italics or dashed borders
- Include small icons for each model type if possible
- Could be created with GraphViz, D3.js, or draw.io

## Figure 2: NAMO Validation and Concordance Framework
**Type:** Conceptual diagram with interconnected components
**Purpose:** Illustrate the multi-dimensional validation approach

**Key Elements:**
Central hub: "StructuredConcordanceResult"
Five connected components:
1. Molecular Similarity
   - Gene expression correlation
   - Protein concordance
   - Metabolite profiles
2. Pathway Concordance
   - Activation scores
   - Directional consistency
   - Pathway coverage
3. Phenotype Overlap
   - Disease manifestations
   - Severity scores
   - Penetrance metrics
4. Functional Parity
   - TEER measurements
   - Contractility
   - Barrier function
5. Statistical Measures
   - P-values
   - Confidence intervals
   - Effect sizes

**Design suggestions:**
- Radial/spider diagram with central hub
- Use consistent color coding
- Show bidirectional arrows indicating data flow
- Include example metrics in smaller text

## Figure 3: Ontology Integration Network
**Type:** Network diagram
**Purpose:** Show how NAMO integrates with external ontologies

**Key Elements:**
- Central node: NAMO (larger, distinctive)
- Connected nodes (6 ontologies):
  - UBERON (13,000+ anatomy terms)
  - Cell Ontology (2,400+ cell types)
  - ChEBI (140,000+ chemicals)
  - NCBITaxon (species)
  - OBI (experimental design)
  - ECO (evidence types)

**Example mappings to show:**
- UBERON → "liver" (UBERON:0002107)
- CL → "hepatocyte" (CL:0000182)
- ChEBI → "acetaminophen" (CHEBI:46195)
- NCBITaxon → "Homo sapiens" (NCBITaxon:9606)

**Design suggestions:**
- Use force-directed layout or circular arrangement
- Size nodes by number of terms
- Color code by domain (anatomy=blue, cells=green, chemicals=orange, etc.)
- Show selected example terms with dotted lines

## Figure 4: Comparative Landscape of NAM Databases
**Type:** Before/After comparison diagram
**Purpose:** Illustrate fragmentation problem and NAMO solution

**Panel A - Current State (Fragmented):**
- Four isolated boxes representing databases:
  - OrganoidDB (icon: organoid, label: "Transcriptomics")
  - MPS-DB (icon: chip, label: "Pharmacokinetics")
  - Cell Model Passports (icon: cells, label: "Cancer models")
  - CompTox (icon: molecule, label: "Chemical-centric")
- Show no connections between them
- Use different colors/styles to emphasize incompatibility

**Panel B - With NAMO Integration:**
- Same four databases but now connected through central NAMO layer
- NAMO shown as semantic bridge/hub
- Bidirectional arrows showing data flow
- Add benefits labels:
  - "Cross-platform queries"
  - "Unified validation"
  - "Regulatory alignment"
  - "Semantic interoperability"

**Design suggestions:**
- Side-by-side panels for clear comparison
- Use consistent iconography
- Highlight transformation with arrows or animation (if digital)
- Consider using Sankey diagram style for data flow

## Additional Optional Figures

### Figure 5: Example NAM Implementation (Optional)
**Type:** Multi-panel figure showing specific example
**Purpose:** Concrete illustration of NAMO in practice

Could show:
- Panel A: Hepatic organoid photo/microscopy
- Panel B: YAML representation snippet
- Panel C: Validation data visualization (correlation plots, bar charts)
- Panel D: Ontology annotations mapped

### Figure 6: NAMO Development Timeline (Optional for supplement)
**Type:** Timeline/Gantt chart
**Purpose:** Show development process

Elements:
- Requirements gathering phase
- Community engagement workshops
- Schema development iterations
- Validation and testing
- Public release

## Technical Notes for Figure Creation

**Tools that could be used:**
- **For diagrams:** draw.io, Lucidchart, OmniGraffle, Adobe Illustrator
- **For network graphs:** Cytoscape, Gephi, D3.js, NetworkX + matplotlib
- **For hierarchical trees:** GraphViz, D3.js hierarchy layouts
- **For professional publication:** Adobe Illustrator or Inkscape for final polish

**Style guidelines:**
- Use consistent color palette throughout
- Ensure accessibility (colorblind-friendly palettes)
- Vector format (SVG/PDF) for publication quality
- 300 DPI minimum for raster elements
- Follow journal guidelines for figure dimensions
- Sans-serif fonts (Arial, Helvetica) for clarity

**Color scheme suggestion:**
- Primary: Blue (#2E86AB)
- Secondary: Green (#A23B72)
- Accent: Orange (#F18F01)
- Neutral: Grays
- Error/Important: Red (#C73E1D)