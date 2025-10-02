# namo 

NAMO (New Approach Methodology Ontology) is a comprehensive schema for representing diverse 
in vitro and in silico model systems used as alternatives to traditional animal testing. 
It supports organoids, organ-on-chip systems, 3D cell cultures, computational models, and 
other New Approach Methodologies (NAMs) used in toxicology, drug discovery, and biomedical research.

## Schema Organization

The schema follows a hierarchical structure that mirrors how NAM research is organized and conducted:

The top-level entity is a [Dataset](Dataset.md), which serves as a container for related research
activities. A dataset might represent all NAM models from a specific laboratory, regulatory study, 
or collaborative research program.

Each dataset contains one or more [Studies](Study.md), which are focused investigations using
specific NAM approaches. For example, a study might investigate "Hepatotoxicity screening using
liver organoids" or "Multi-organ drug ADMET assessment using microphysiological systems."

Within each study, you'll find:

### Model Systems
The core of NAMO is the representation of different [NAM model types](NAMModel.md):

- **[Organoids](Organoid.md)**: Self-organizing 3D tissue models derived from stem cells that 
  recapitulate organ-specific architecture and function. Examples include brain organoids for 
  neurotoxicity testing, intestinal organoids for drug absorption studies, and liver organoids 
  for metabolism research.

- **[Organ-on-Chip Systems](OrganOnChip.md)**: Microfluidic devices that simulate organ-level 
  physiology with precise control over cellular microenvironment. These include lung-on-chip 
  for inhalation toxicology, heart-on-chip for cardiotoxicity assessment, and multi-organ 
  chips for systemic drug effects.

- **[Tissue-on-Chip Systems](TissueOnChip.md)**: Microfluidic models focused on specific tissue
  functions such as blood-brain barrier chips, skin models for dermatological testing, and 
  kidney proximal tubule chips for nephrotoxicity screening.

- **[3D Cell Cultures](ThreeDCellCulture.md)**: Three-dimensional cell culture systems including
  spheroids, scaffold-based cultures, and bioengineered tissues that provide more physiologically
  relevant environments than traditional 2D cultures.

- **[2D Cell Cultures](TwoDCellCulture.md)**: Monolayer cell culture systems with specialized
  configurations, substrates, and culture conditions optimized for specific applications.

- **[Co-Culture Systems](CoCulture.md)**: Multi-cell-type culture systems that model cellular
  interactions, tissue interfaces, and organ-level communication pathways.

### Computational Models
NAMO supports various in silico approaches:

- **[Machine Learning Models](MLModel.md)**: AI/ML systems for toxicity prediction, including
  deep learning models for chemical structure-activity relationships, neural networks for 
  dose-response modeling, and ensemble methods for multi-endpoint prediction.

- **[QSAR Models](QSARModel.md)**: Quantitative Structure-Activity Relationship models that
  predict biological activity from molecular structure, including traditional statistical
  approaches and modern machine learning implementations.

- **[PBPK Models](PBPKModel.md)**: Physiologically-based pharmacokinetic models that simulate
  drug absorption, distribution, metabolism, and excretion using mathematical representations
  of biological processes.

- **[Digital Twins](DigitalTwin.md)**: Integrated computational models that combine multiple
  data sources and modeling approaches to create personalized, real-time simulations of 
  biological systems.

- **[Metabolic Models](MetabolicModel.md)**: Systems biology models of cellular metabolism,
  including flux balance analysis, kinetic modeling, and constraint-based approaches for
  understanding metabolic perturbations.

### Technical Specifications

#### Microfluidic Design
For chip-based systems, detailed [microfluidic design](MicrofluidicDesign.md) specifications 
capture device architecture, including channel configurations, flow control methods, sensor
integration, and material properties essential for reproducibility and standardization.

#### Validation and Concordance
NAMO emphasizes validation through [structured concordance analysis](StructuredConcordanceResult.md):

- **[Molecular Similarity](MolecularSimilarity.md)**: Gene expression profiles, protein markers,
  and metabolomic signatures compared to reference biological systems
- **[Functional Parity](FunctionalParity.md)**: Physiological responses, barrier functions,
  and cellular behaviors that match in vivo counterparts
- **[Reproducibility](Reproducibility.md)**: Inter-laboratory consistency, batch-to-batch 
  variation, and quality control metrics

#### Performance Metrics
Quantitative assessment through standardized [functional assays](FunctionalAssay.md) that
measure model performance, sensitivity, specificity, and predictive accuracy against known
outcomes and regulatory endpoints.

## Use Cases

NAMO supports diverse applications across multiple domains:

### Regulatory Toxicology
- **Chemical Safety Assessment**: Systematic evaluation of chemical toxicity using integrated
  NAM approaches, supporting regulatory submissions to EPA, FDA, and ECHA
- **Cosmetics Testing**: Non-animal approaches for skin sensitization, eye irritation, and
  systemic toxicity assessment as required by regulations worldwide
- **Pesticide Evaluation**: Environmental and human health risk assessment using NAMs for 
  neurotoxicity, endocrine disruption, and developmental toxicity endpoints

### Pharmaceutical Development
- **Drug Discovery**: Early-stage compound screening using organ-specific models to identify
  promising candidates and eliminate toxic compounds
- **ADMET Profiling**: Absorption, Distribution, Metabolism, Excretion, and Toxicity assessment
  using integrated organ-on-chip platforms and computational models
- **Precision Medicine**: Patient-derived organoids and digital twins for personalized drug
  selection and dosing strategies

### Academic Research
- **Disease Modeling**: Patient-specific organoids for studying rare diseases, cancer biology,
  and genetic disorders in controlled laboratory environments
- **Mechanistic Studies**: Investigation of toxicity pathways, cellular responses, and 
  molecular mechanisms using well-characterized NAM systems
- **Method Development**: Innovation in NAM technologies, validation approaches, and 
  standardization protocols

## Key Features

- **Multi-Modal Integration**: Support for combining multiple NAM approaches in integrated
  testing strategies (ITS) and adverse outcome pathways (AOPs)
- **Standardization Focus**: Emphasis on reproducibility, quality control, and inter-laboratory
  harmonization essential for regulatory acceptance
- **Literature Integration**: Comprehensive [reference](Reference.md) system linking models
  to peer-reviewed publications, regulatory guidance, and validation studies
- **Ontology Alignment**: Integration with established ontologies including UBERON (anatomy),
  CL (cell types), CHEBI (chemicals), and OBI (biomedical investigations)

For detailed curation guidelines, see:
- [How to Curate Organoid Papers](https://monarch-initiative.github.io/namo/how-to/curate-organoid-paper/)
- [How to Curate Organ-on-Chip Papers](https://monarch-initiative.github.io/namo/how-to/curate-organ-on-chip-paper/)

## Community and Standards

NAMO is developed in collaboration with the NAM research community, regulatory agencies, and 
standards organizations including OECD, ICCVAM, and ESTIV. It supports the 3Rs principles 
(Replacement, Reduction, Refinement) and contributes to the transition toward animal-free 
testing methodologies in safety assessment and biomedical research.


URI: https://w3id.org/monarch-initiative/namo