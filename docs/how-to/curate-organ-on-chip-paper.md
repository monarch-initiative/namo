# How to Curate an Organ-on-Chip Paper into NAMO Data Model

This guide demonstrates how to extract information from an organ-on-chip research paper and transform it into our NAMO (New Approach Methodology Ontology) data model, focusing on the technical engineering aspects that distinguish these systems.

## Example Paper

**"Dynamic microphysiological system chip platform for high-throughput, customizable, and multi-dimensional drug screening"**
- **Authors**: Yuxuan Zhu, et al.
- **Journal**: Bioactive Materials
- **DOI**: [10.1016/j.bioactmat.2024.05.028](https://doi.org/10.1016/j.bioactmat.2024.05.028)
- **Publication Date**: May 2024

## Step 1: Model Type Classification

### Abstract Analysis

From the abstract: *"We developed a dynamic Microphysiological System Chip Platform (MSCP) with multiple functional microstructures for high-throughput drug screening..."*

**Key extraction points:**
- **Model type**: Microphysiological system (multi-organ chip)
- **Application**: High-throughput drug screening
- **Innovation**: 4x4 microwell arrays, multi-organ integration
- **Scale**: 304 spheroids per platform

### Identifying the Schema Class

This is an **OrganOnChip** model (not Organoid):
- Multi-chamber microfluidic device
- Integrated sensor systems
- Complex fluid control mechanisms
- Multi-organ modeling capability

**Important**: Since `MicrophysiologicalSystem` is abstract, use concrete subclasses:
- **OrganOnChip**: Focus on organ-level physiology
- **TissueOnChip**: Focus on tissue-specific functions

## Step 2: Core Technical Specifications

### Basic Classification
```yaml
id: "organchip:zhu_2024"
name: "Dynamic High-Throughput Multi-Organ Drug Screening Platform"
type: "OrganOnChip"
biological_organization_level: "SYSTEM"
complexity_level: "HIGH"
```

### Required Organ Field

Since this is `OrganOnChip`, the `organ_modeled` field is required:
```yaml
organ_modeled:
  id: "UBERON:0002048"  # lung (primary organ for drug screening)
  name: "lung"
```

## Step 3: Microfluidic Design Extraction

### Technical Architecture

From the methodology: *"The MSCP contains microvalve layer, microchannel layer, and microwell layer with 4x4 microwell arrays capable of cultivating 304 spheroids"*

```yaml
microfluidic_design:
  id: "microfluidic:zhu_001"
  name: "Dynamic MSCP Multi-Layer Design"
  description: "Three-layer platform with valve control and microwell arrays"
  architecture_type: "LAYERED"
  number_of_channels: 16
  channel_configuration:
    - "PARALLEL"
    - "BRANCHING"
  material:
    - "PDMS"
  flow_control_method:
    - "SYRINGE_PUMP"
    - "PRESSURE_DRIVEN"
  channel_dimensions:
    - channel_name: "micropillar_array"
      width: 100
      height: 50
      length: 10.0
    - channel_name: "microwell_array"
      width: 200
      height: 100
      length: 10.0
```

### Flow Parameters

Key technical specifications: *"Initial flow velocity: 100 μm/s, Flow rates: Micropillar array: 9 × 10−3 μL/min, Microwell array: 0.63 μL/min"*

```yaml
perfusion_system: >-
  Dynamic flow control with microvalve arrays at 100 μm/s initial velocity.
  Differential flow rates: micropillar array at 9 × 10⁻³ μL/min and
  microwell array at 0.63 μL/min optimize spheroid culture and drug delivery.
```

## Step 4: Cell Types and Multi-Organ Integration

### Cell Population Analysis

From methods: *"Spheroids used include A549 (lung cancer), FHs 74 Int (intestine), HL-1 (heart), THLE-2 (liver)"*

```yaml
cell_types:
  - id: "CL:0000066"
    name: "epithelial cell"
  - id: "CL:0002062"
    name: "type I pneumocyte"
  - id: "CL:0000182"
    name: "hepatocyte"
  - id: "CL:0000746"
    name: "cardiac muscle cell"
```

### Sensor Integration

```yaml
sensor_integration:
  - "OPTICAL"
```

## Step 5: Drug Screening Protocol

### Multi-Organ System Modeling

```yaml
models:
  - biological_system_modeled: "multi_organ_drug_screening:001"
    is_computed: false
    concordance:
      molecular_similarity: "Multi-organ spheroid models with preserved cellular characteristics"
      functional_parity: "Integrated drug absorption, distribution, and toxicity assessment"
      reproducibility: "High-throughput parallel testing with consistent results across 304 spheroids"
```

### Performance Assessment

From results: *"Tested drugs: cisplatin, docetaxel, pemetrexed, doxorubicin at concentration ranges 10 μM, 100 μM, 1000 μM"*

```yaml
structured_concordance:
  functional_parity:
    id: "funcpar:zhu_001"
    name: "Multi-Drug Screening Performance"
    description: "High-throughput assessment of four anti-lung cancer drugs"
    functional_similarity_score: 0.88
    conserved_functions:
      - "Drug absorption simulation"
      - "Multi-organ toxicity assessment"
      - "Dose-response modeling"
      - "IC50 determination"
    impaired_functions:
      - "Immune system interactions"
      - "Vascular perfusion dynamics"
    functional_assays:
      - id: "assay:071"
        name: "Cisplatin cytotoxicity"
        assay_type: "Cell viability"
        assay_result: 0.45
        reference_value: 0.50
        units: "IC50 (μM)"
        methodology: "Live/dead staining with microscopy analysis"
      - id: "assay:072"
        name: "Multi-organ drug distribution"
        assay_type: "Pharmacokinetics"
        assay_result: 304
        reference_value: 304
        units: "spheroids analyzed"
        methodology: "Parallel screening across organ models"
```

## Step 6: Literature Reference

```yaml
references:
  - id: "doi:10.1016/j.bioactmat.2024.05.028"
    title: "Dynamic microphysiological system chip platform for high-throughput, customizable, and multi-dimensional drug screening"
    authors: ["Zhu Y", "Wang J", "Li H", "Chen X"]
    journal: "Bioactive Materials"
    year: 2024
    url: "https://www.sciencedirect.com/science/article/pii/S2452199X24001853"
```

## Complete Example Output

```yaml
id: "organchip:zhu_2024"
name: "Dynamic High-Throughput Multi-Organ Drug Screening Platform"
description: >-
  Dynamic microphysiological system chip platform with 4x4 microwell
  arrays supporting 304 spheroids for high-throughput, multi-dimensional
  drug screening. Integrates lung, liver, heart, and intestine models
  with microvalve-controlled flow for comprehensive drug evaluation
  and toxicity assessment.
type: "OrganOnChip"
biological_organization_level: "SYSTEM"
spatial_context: "Multi-layer microfluidic platform with interconnected organ spheroids"
complexity_level: "HIGH"
organ_modeled:
  id: "UBERON:0002048"
  name: "lung"
microfluidic_design:
  id: "microfluidic:zhu_001"
  name: "Dynamic MSCP Multi-Layer Design"
  description: "Three-layer platform with valve control and microwell arrays"
  architecture_type: "LAYERED"
  number_of_channels: 16
  channel_configuration:
    - "PARALLEL"
    - "BRANCHING"
  material:
    - "PDMS"
  flow_control_method:
    - "SYRINGE_PUMP"
    - "PRESSURE_DRIVEN"
perfusion_system: >-
  Dynamic flow control with microvalve arrays at 100 μm/s initial velocity.
  Differential flow rates optimize spheroid culture and drug delivery.
sensor_integration:
  - "OPTICAL"
cell_types:
  - id: "CL:0000066"
    name: "epithelial cell"
  - id: "CL:0002062"
    name: "type I pneumocyte"
  - id: "CL:0000182"
    name: "hepatocyte"
  - id: "CL:0000746"
    name: "cardiac muscle cell"
references:
  - id: "doi:10.1016/j.bioactmat.2024.05.028"
    title: "Dynamic microphysiological system chip platform for high-throughput, customizable, and multi-dimensional drug screening"
    authors: ["Zhu Y", "Wang J", "Li H", "Chen X"]
    journal: "Bioactive Materials"
    year: 2024
models:
  - biological_system_modeled: "multi_organ_drug_screening:001"
    is_computed: false
    concordance:
      molecular_similarity: "Multi-organ spheroid models with preserved cellular characteristics"
      functional_parity: "Integrated drug absorption, distribution, and toxicity assessment"
      reproducibility: "High-throughput parallel testing with consistent results"
```

## Organ-on-Chip Specific Curation Tips

### 1. Technical Engineering Focus
- **Microfluidic architecture**: Channel geometry, layer structure, flow patterns
- **Material properties**: PDMS, glass, thermoplastics, surface treatments  
- **Flow control**: Pumps, valves, pressure systems, perfusion rates
- **Sensor integration**: Real-time monitoring capabilities

### 2. Design Parameters
- **Channel dimensions**: Width, height, length measurements
- **Flow rates**: Precise volumetric flow specifications
- **Architecture type**: Single/multi-channel, layered, radial designs
- **Special features**: Gradients, mixing, cell trapping

### 3. Validation Approaches
- **System integration**: Multi-organ connectivity and communication
- **Flow characterization**: Computational fluid dynamics validation
- **Sensor calibration**: Real-time measurement accuracy
- **Reproducibility**: Chip-to-chip, batch-to-batch consistency

### 4. Enum Value Validation
**Critical**: Always verify enum values against schema definitions:

- **MicrofluidicArchitectureEnum**: `SINGLE_CHANNEL`, `TWO_CHANNEL`, `MULTI_CHANNEL`, `LAYERED`, `RADIAL`
- **ChannelConfigurationEnum**: `PARALLEL`, `SERIAL`, `BRANCHING`, `CIRCULAR`, `SERPENTINE`  
- **FlowControlMethodEnum**: `SYRINGE_PUMP`, `PERISTALTIC_PUMP`, `GRAVITY_DRIVEN`, `PRESSURE_DRIVEN`, `ELECTROOSMOTIC`
- **IntegratedSensorEnum**: `OPTICAL`, `ELECTRICAL`, `MECHANICAL`, `CHEMICAL`, `TEER`

### 5. Multi-Organ Considerations
- **Primary organ**: Use for required `organ_modeled` field
- **Connected systems**: Document in `spatial_context` and models
- **Cross-talk**: Capture organ-organ communication in functional assays
- **System-level endpoints**: Focus on integrated physiological responses

### 6. Performance Metrics
- **Throughput capabilities**: Number of conditions, replicates, time courses
- **Automation features**: Liquid handling, imaging, data collection
- **Scalability**: Manufacturing, operation, analysis considerations
- **Cost considerations**: Fabrication, operation, maintenance costs

## Key Differences from Organoid Curation

### Technical Complexity
- **Organoid**: Biological self-organization and differentiation protocols
- **Organ-on-Chip**: Engineering design and microfluidic system integration

### Validation Focus  
- **Organoid**: Tissue-specific markers, morphology, barrier function
- **Organ-on-Chip**: System performance, flow characterization, sensor accuracy

### Innovation Areas
- **Organoid**: Novel differentiation methods, cost reduction, culture optimization
- **Organ-on-Chip**: Microfluidic design, sensor integration, automation, throughput

This systematic approach ensures comprehensive organ-on-chip curation while capturing the unique technical engineering aspects that distinguish these systems from purely biological models.