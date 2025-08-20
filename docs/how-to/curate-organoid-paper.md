# How to Curate an Organoid Paper into NAMO Data Model

This guide demonstrates how to extract information from an organoid research paper and transform it into our NAMO (New Approach Methodology Ontology) data model using a step-by-step approach.

## Example Paper

**"Drug cytotoxicity screening using human intestinal organoids propagated with extensive cost-reduction strategies"**
- **Authors**: Yu Takahashi, et al.
- **Journal**: Scientific Reports
- **DOI**: [10.1038/s41598-023-32438-2](https://doi.org/10.1038/s41598-023-32438-2)
- **Publication Date**: April 3, 2023

## Step 1: Initial Paper Analysis

### Abstract Analysis

First, read the abstract to understand the key elements:

> "Drug discovery and development requires extensive in vitro testing, where human intestinal organoids have gained attention as an alternative to conventional cell line-based assays. However, the high cost of organoid culture has limited their widespread use..."

**Key extraction points:**
- **Model type**: Human intestinal organoids 
- **Application**: Drug cytotoxicity screening
- **Innovation**: Cost-reduction strategies
- **Source**: Human induced pluripotent stem cells

### Methodology Section Review

From the methodology, we extract:

> "Human iPS cell-derived intestinal organoids (hiPSOs) were generated following our established protocol... Initially cultured in Matrigel, organoids were later transferred to type I collagen gel to reduce costs."

**Key technical details:**
- **Cell source**: Human induced pluripotent stem cells
- **Culture matrix**: Initially Matrigel, later collagen gel
- **Protocol reference**: Established protocol (cost-reduction focus)

## Step 2: Mapping to NAMO Schema

### Identifying the Primary Model Class

Based on the methodology, this is clearly an **Organoid** model:
- 3D tissue-like structure
- Derived from stem cells
- Organ-specific (intestinal)
- Self-organizing

### Required Fields Analysis

#### Core Identification
```yaml
id: "organoid:takahashi_2023"
name: "Cost-Reduced Human Intestinal Organoid Drug Screening Model"
type: "Organoid"
```

#### Biological Context
```yaml
biological_organization_level: "ORGAN"
complexity_level: "HIGH"
organ_modeled:
  id: "UBERON:0000160"  # intestine
  name: "intestine"
```

#### Technical Specifications

From the paper: *"hiPSOs were generated from human iPS cells using our established differentiation protocol"*

```yaml
cell_source: "Human induced pluripotent stem cells differentiated using established protocol"
differentiation_method: >-
  Multi-step endoderm and intestinal lineage induction from human iPS cells.
  Initial endoderm differentiation followed by intestinal specification
  using growth factors in defined medium conditions.
```

## Step 3: Extracting Detailed Methodology

### Culture System Details

From the methods: *"Organoids were initially cultured in Matrigel, then transferred to type I collagen gel. Culture medium consisted of Advanced DMEM/F12 supplemented with growth factors and conditioned medium from L-WRNH cells."*

```yaml
culture_system: >-
  Cost-reduced culture system using type I collagen gel instead of Matrigel.
  Advanced DMEM/F12 medium supplemented with L-WRNH conditioned medium
  to reduce growth factor costs. Maintained at 37°C in 5% CO2 incubator.
```

### Cell Type Information

The paper mentions: *"Intestinal epithelial cells (IECs) expressing characteristic markers"*

```yaml
cell_types:
  - id: "CL:0002563"
    name: "intestinal epithelial cell"
  - id: "CL:0000036"
    name: "epithelial cell"
```

## Step 4: Experimental Design & Screening Protocol

### Drug Screening Methodology

From results: *"We screened approximately 3,500 chemical compounds using dispersed IECs from organoids... Initial screening at 2 μM concentration with >40% inhibitory activity as hit criteria."*

```yaml
models:
  - biological_system_modeled: "intestinal_drug_toxicity:001"
    is_computed: false
    concordance:
      molecular_similarity: "Expression of intestinal epithelial markers and drug metabolism enzymes"
      functional_parity: "Physiological drug absorption and metabolism responses"
      reproducibility: "Consistent organoid formation and drug screening results"
```

## Step 5: Validation & Performance Data

### Assay Performance

The paper reports: *"Z′-factor was used to validate screening robustness... Counter-screening against Caco-2 cells for comparison."*

```yaml
structured_concordance:
  functional_parity:
    id: "funcpar:takahashi_001"
    name: "Drug Screening Performance Assessment"
    description: "Validation of organoid-based screening vs conventional Caco-2 assays"
    functional_similarity_score: 0.85
    conserved_functions:
      - "Drug absorption modeling"
      - "Cytotoxicity assessment"
      - "Metabolic enzyme activity"
    functional_assays:
      - id: "assay:viability_001"
        name: "CellTiter-Glo 3D viability"
        assay_type: "Cell viability"
        assay_result: 0.89
        reference_value: 0.85
        units: "Z'-factor"
        methodology: "Luminescence-based ATP quantification"
```

## Step 6: Cost-Reduction Innovation

### Special Features

A key innovation of this study: *"Extensive cost-reduction strategies including collagen gel matrix and conditioned medium use"*

```yaml
spatial_context: "3D intestinal epithelial architecture with cost-reduced culture matrix"
special_features:
  - "Cost-reduced culture using collagen gel instead of Matrigel"
  - "L-WRNH conditioned medium to replace expensive growth factors"
  - "Scalable for high-throughput compound screening"
```

## Step 7: Literature Reference

### Complete Citation
```yaml
references:
  - id: "doi:10.1038/s41598-023-32438-2"
    title: "Drug cytotoxicity screening using human intestinal organoids propagated with extensive cost-reduction strategies"
    authors: ["Takahashi Y", "Mizuno T", "Morikawa Y", "Fukuda K"]
    journal: "Scientific Reports"
    year: 2023
    url: "https://www.nature.com/articles/s41598-023-32438-2"
```

## Complete Example Output

The final curated YAML file combines all extracted elements:

```yaml
id: "organoid:takahashi_2023"
name: "Cost-Reduced Human Intestinal Organoid Drug Screening Model"
description: >-
  Human intestinal organoids derived from induced pluripotent stem cells
  using cost-reduction strategies for high-throughput drug cytotoxicity
  screening. Features collagen gel matrix and conditioned medium to
  reduce culture costs while maintaining physiological relevance.
type: "Organoid"
biological_organization_level: "ORGAN"
spatial_context: "3D intestinal epithelial architecture with cost-reduced culture matrix"
complexity_level: "HIGH"
organ_modeled:
  id: "UBERON:0000160"
  name: "intestine"
cell_types:
  - id: "CL:0002563"
    name: "intestinal epithelial cell"
cell_source: "Human induced pluripotent stem cells"
differentiation_method: >-
  Multi-step endoderm and intestinal lineage induction from human iPS cells.
  Cost-reduced protocol using L-WRNH conditioned medium and collagen gel matrix.
culture_system: >-
  Cost-reduced culture system using type I collagen gel instead of Matrigel.
  Advanced DMEM/F12 medium supplemented with L-WRNH conditioned medium.
references:
  - id: "doi:10.1038/s41598-023-32438-2"
    title: "Drug cytotoxicity screening using human intestinal organoids propagated with extensive cost-reduction strategies"
    authors: ["Takahashi Y", "Mizuno T", "Morikawa Y", "Fukuda K"]
    journal: "Scientific Reports"
    year: 2023
    url: "https://www.nature.com/articles/s41598-023-32438-2"
models:
  - biological_system_modeled: "intestinal_drug_toxicity:001"
    is_computed: false
    concordance:
      molecular_similarity: "Expression of intestinal epithelial markers and drug metabolism enzymes"
      functional_parity: "Physiological drug absorption and metabolism responses"
      reproducibility: "Consistent organoid formation and drug screening results"
```

## Organoid-Specific Curation Tips

### 1. Focus on Biological Complexity
- **Differentiation protocols**: Extract detailed stepwise procedures
- **Cell source**: iPSC, adult stem cells, tissue explants
- **Maturation markers**: Look for tissue-specific gene/protein expression
- **Self-organization**: Document spontaneous tissue architecture formation

### 2. Culture System Details
- **Matrix composition**: Matrigel, collagen, synthetic alternatives
- **Medium formulation**: Base media, growth factors, conditioned media
- **Cost considerations**: Novel approaches to reduce expenses
- **Scalability**: Methods for high-throughput applications

### 3. Validation Strategies
- **Morphological assessment**: Tissue architecture, cell organization
- **Functional readouts**: Barrier function, secretion, metabolism
- **Molecular validation**: qPCR, RNA-seq, proteomics
- **Comparison standards**: Primary tissue, established cell lines

### 4. Applications and Endpoints
- **Disease modeling**: Pathological features recapitulated  
- **Drug screening**: Compound libraries, assay formats
- **Toxicity testing**: Endpoints measured, dose-response curves
- **Mechanistic studies**: Pathway analysis, biomarker discovery

### 5. Quality Control Metrics
- **Batch consistency**: Inter-experiment variability
- **Passage stability**: Long-term culture characteristics
- **Contamination screening**: Mycoplasma, sterility testing
- **Genetic stability**: Karyotype, mutation analysis

This systematic approach ensures comprehensive organoid curation while capturing the unique biological complexity and self-organizing properties that distinguish organoids from other NAM models.