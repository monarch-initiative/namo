# NAMO: New Approach Methodology Ontology and Schema

## Overview

The **New Approach Methodology Ontology and Schema (NAMO)** is a comprehensive data framework designed to standardize and integrate information about alternative methods to animal testing in biomedical research. Built on [LinkML](https://linkml.io/), NAMO provides a common vocabulary and data structure for describing diverse model systems, from cellular cultures and organ-on-chip devices to computational models and digital twins.

## Why NAMO Matters

### The Challenge

The biomedical research landscape is rapidly evolving with innovative alternatives to traditional animal models:

- **Organ-on-chip** devices that mimic human tissue physiology
- **3D organoids** that recapitulate organ development and disease
- **In silico models** including AI/ML systems and physiologically-based pharmacokinetic (PBPK) models
- **Advanced cellular systems** with complex co-cultures and microenvironments

However, these New Approach Methodologies (NAMs) exist in isolated silos with:
- **Inconsistent terminology** across research groups and disciplines
- **Fragmented data** that cannot be easily compared or integrated
- **Limited discoverability** of relevant models for specific research questions
- **Unclear relationships** between model capabilities and human disease contexts

### The Solution

NAMO addresses these challenges by providing:

1. **Unified Data Model**: A comprehensive schema that captures the essential characteristics of all NAM types under a common framework
2. **Ontology Integration**: Deep integration with established biomedical ontologies (Cell Ontology, UBERON, MONDO) ensuring semantic interoperability
3. **Rich Metadata**: Detailed capture of model specifications, concordance metrics, and validation data
4. **Cross-Platform Compatibility**: Generation of multiple data formats (JSON Schema, OWL, Python models) for diverse technical ecosystems

## Core Applications

### Integrated Database Development

NAMO serves as the foundational schema for building comprehensive databases that:

- **Catalog NAM systems** across research institutions and companies
- **Enable cross-model comparisons** through standardized metadata
- **Support model discovery** via semantic search and filtering
- **Track validation evidence** and concordance with human biology
- **Facilitate regulatory acceptance** through structured documentation

### Research Integration Platforms

Organizations can use NAMO to:

- **Harmonize data** from multiple model types and sources
- **Build knowledge graphs** connecting models to diseases, pathways, and phenotypes  
- **Support AI/ML applications** with structured training data
- **Enable meta-analyses** across different experimental approaches
- **Create recommendation systems** for optimal model selection

### Regulatory Documentation

NAMO supports regulatory science by:

- **Standardizing evidence packages** for model validation
- **Tracking concordance metrics** between models and human biology
- **Documenting use contexts** and limitations transparently
- **Enabling systematic reviews** of model performance across studies

## Key Features

### Hierarchical Model Organization

NAMO organizes model systems into three main categories:

1. **Cellular Systems**: 2D/3D cultures, organoids, co-cultures, and cell line models
2. **Microphysiological Systems**: Organ-on-chip and tissue-on-chip devices
3. **In Silico Models**: QSAR, PBPK, digital twins, and machine learning models

Each category captures domain-specific attributes while sharing common metadata patterns.

### Rich Concordance Assessment

The schema includes sophisticated frameworks for documenting how well models recapitulate human biology:

- **Molecular similarity** with gene expression correlation and pathway conservation
- **Phenotype overlap** using standardized phenotype ontologies
- **Functional parity** through quantitative assay comparisons
- **Cell type coverage** with single-cell resolution
- **Reproducibility metrics** across batches and laboratories

### Ontology-Driven Interoperability

NAMO leverages established biomedical ontologies:

- **Cell Ontology (CL)** for standardized cell type annotations
- **UBERON** for anatomical structure references
- **MONDO** for disease associations
- **Gene Ontology (GO)** for molecular function and pathway annotations

This enables seamless integration with existing biomedical databases and knowledge graphs.

### Flexible Validation Framework

The schema supports diverse types of validation evidence:

- **Literature references** with DOI/PMID tracking
- **Experimental assays** with methodology and performance metrics
- **Omics data integration** including transcriptomics and proteomics
- **Quality control metrics** with pass/fail status tracking
- **Cross-validation results** for computational models

## Technical Implementation

### Multi-Format Generation

From a single LinkML schema definition, NAMO automatically generates:

- **Python dataclasses** and Pydantic models for programmatic access
- **JSON Schema** for web applications and API validation
- **OWL ontology** for semantic web applications
- **GraphQL schemas** for modern API development
- **Documentation** with cross-referenced class and property descriptions

### Extensible Architecture

The schema is designed for evolution:

- **Abstract base classes** enable addition of new model types
- **Flexible slot definitions** accommodate emerging measurement modalities
- **Enum extensibility** supports new controlled vocabularies
- **Mixin patterns** allow cross-cutting concerns like provenance tracking

### Validation and Quality Control

NAMO includes comprehensive validation mechanisms:

- **Schema validation** ensures data integrity and completeness
- **Ontology term validation** verifies proper vocabulary usage
- **Cross-reference checking** maintains referential integrity
- **Example validation** through curated test cases

## Getting Started

### For Database Developers

Use NAMO as your foundational schema for NAM data integration:

```python
from namo.datamodel import Dataset, Organoid, QSARModel

# Create a dataset with multiple model types
dataset = Dataset(
    model_systems=[
        Organoid(
            id="org_001",
            name="Brain Organoid Model",
            organ_modeled={"id": "UBERON:0000955", "name": "brain"}
        ),
        QSARModel(
            id="qsar_001", 
            name="Hepatotoxicity Predictor",
            activity_endpoint="DILI classification"
        )
    ]
)
```

### For Data Integration

Leverage NAMO's ontology mappings for semantic interoperability:

```yaml
model_system:
  id: "organoid:001"
  type: "Organoid"
  cell_types:
    - id: "CL:0000540"  # neuron
      name: "neuron"
    - id: "CL:0000127"  # astrocyte  
      name: "astrocyte"
  models:
    - biological_system_modeled: "alzheimers_disease"
      concordance:
        molecular_similarity: "0.85"
        phenotype_overlap: "High concordance with patient tissue"
```

### For Computational Applications

Build on NAMO's structured data for AI/ML applications:

- **Feature extraction** from standardized model metadata
- **Similarity scoring** using ontology-based distance metrics
- **Recommendation systems** for model selection
- **Knowledge graph embeddings** for novel association discovery

## Community and Standards

NAMO is developed as an open standard with broad community input:

- **Open source** development on GitHub with transparent governance
- **Community-driven** extension through working groups and feedback
- **Standards-compliant** with FAIR data principles and biomedical ontology practices
- **Interoperable** with existing databases like Monarch Initiative and EBI resources

The schema serves as a bridge between the traditional model organism research community and emerging NAM technologies, providing a path for integrated translational research platforms.

## Future Directions

NAMO continues to evolve to meet emerging needs:

- **Expanded model types** including digital twins and multi-organ systems
- **Enhanced concordance metrics** with quantitative benchmarking frameworks
- **Regulatory alignment** with guidelines from FDA, EMA, and OECD
- **AI integration** with structured training data for model recommendation systems
- **Real-time data capture** from connected laboratory instruments and devices

By providing a robust, extensible, and community-driven foundation, NAMO enables the next generation of integrated biomedical research platforms that harness the full potential of alternative methodologies for human health advancement.

## Documentation

- [Complete Schema Documentation](elements/index.md) - Auto-generated documentation for all classes, slots, and enumerations
- [Use Cases and Examples](use-cases.md) - Practical applications and implementation patterns