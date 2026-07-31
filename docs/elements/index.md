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

Name: namo



## Classes

| Class | Description |
| --- | --- |
| [Annotation](Annotation.md) | Biolink Model root class for entity annotations |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QuantityValue](QuantityValue.md) | A value of an attribute that is quantitative and measurable, expressed as a c... |
| [BehavioralOutcome](BehavioralOutcome.md) | An outcome resulting from an exposure event which is the manifestation of hum... |
| [CaseToEntityAssociationMixin](CaseToEntityAssociationMixin.md) | An abstract association for use where the case is the subject |
| [CellLineToEntityAssociationMixin](CellLineToEntityAssociationMixin.md) | An relationship between a cell line and another entity |
| [CellRatio](CellRatio.md) | Ratio specification for different cell types in co-culture systems |
| [CellTypeProportion](CellTypeProportion.md) | Quantitative comparison of cell type proportions between systems |
| [ChannelDimensions](ChannelDimensions.md) | Dimensions of a microfluidic channel according to ISO 10991:2023 definitions ... |
| [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) | A union of chemical entities and children, and gene or gene product |
| [ChemicalEntityOrProteinOrPolypeptide](ChemicalEntityOrProteinOrPolypeptide.md) | A union of chemical entities and children, and protein and polypeptide |
| [ChemicalEntityToEntityAssociationMixin](ChemicalEntityToEntityAssociationMixin.md) | An interaction between a chemical entity and another entity |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md) | An interaction between a chemical entity and another entity |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DrugToEntityAssociationMixin](DrugToEntityAssociationMixin.md) | An interaction between a drug and another entity |
| [ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md) | A mixin for entities that represent chemical substances, pharmacological agen... |
| [ConcordanceResult](ConcordanceResult.md) |  |
| [CrossValidation](CrossValidation.md) | Cross-validation strategy and results for ML models |
| [DiseaseOrPhenotypicFeatureOutcome](DiseaseOrPhenotypicFeatureOutcome.md) | Physiological outcomes resulting from an exposure event which is the manifest... |
| [DiseaseOrPhenotypicFeatureToEntityAssociationMixin](DiseaseOrPhenotypicFeatureToEntityAssociationMixin.md) |  |
| [DiseaseToEntityAssociationMixin](DiseaseToEntityAssociationMixin.md) | A mixin applied to any association whose subject (source node) is a disease |
| [DoseResponseSimilarity](DoseResponseSimilarity.md) | Comparison of dose-response relationships between model and biological system... |
| [DrugProperties](DrugProperties.md) | Physicochemical and pharmacological properties of a drug in PBPK models |
| [Edge](Edge.md) | A generic edge in a KGX-formatted knowledge graph, representing a directed re... |
| [EnrichmentStatistics](EnrichmentStatistics.md) | Statistical measures for pathway enrichment analysis |
| [Entity](Entity.md) | Root Biolink Model class for all things and informational relationships, real... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Association](Association.md) | A typed association between two entities, supported by evidence |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | An abstract parent class for associations between two anatomical entities, su... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | A relationship between two anatomical entities where the relationship is mere... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | A relationship between two anatomical entities where the relationship is mere... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | A relationship between two anatomical entities where the relationship is onto... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | An association between an mixture behavior and a behavioral feature manifeste... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | An association between a biological process or activity and an anatomical ent... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | Classification relationship between biological processes or activities (e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | Relationship between a biological processor activity (e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | An association between a Case (patient) and a Disease |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CaseToGeneAssociation](CaseToGeneAssociation.md) | Association between a Case and a Gene (e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | An association between a case (e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CaseToVariantAssociation](CaseToVariantAssociation.md) | Association between a Case and a Genetic Variant |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | An association between a gene and a disease where variation in the gene has b... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | An relationship between a cell line and a disease or a phenotype, where the c... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | An association in which a cell line - typically derived from an organismal en... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | Describes an effect that a chemical has on a biological entity (e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | A regulatory relationship between two genes |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | An association between a chemical entity and a biological process, where the ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | A relationship between two chemical entities |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | A causal relationship between two chemical entities, where the subject repres... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | An association between a biochemical reaction and a participating molecular e... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | A specialization of reaction-to-participant association in which the particip... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | An interaction between a chemical entity and a phenotype or disease, where th... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | An interaction between a chemical entity and a biological process or pathway |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | describes an interaction between a chemical entity and a gene or gene product |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | Describes a relationship in which a chemical entity affects the sensitivity o... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContributorAssociation](ContributorAssociation.md) | Any association between an entity (such as a publication) and various agents ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | An association between a gene (or gene product) and a disease for which the g... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | A statistical association between a disease and a chemical entity where the c... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | An association between either a disease or a phenotypic feature and its mode ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | An association between either a disease or a phenotypic feature and an anatom... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | An association between two diseases |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | An association between an exposure event and a disease |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | An association between a disease and a phenotypic feature in which the phenot... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DrugToGeneAssociation](DrugToGeneAssociation.md) | An interaction between a drug and a gene or gene product |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | An association between any entity and a disease, capturing clinical context s... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | An association between any entity and a phenotypic feature, capturing clinica... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | An association between an exposure event and an outcome |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | Any association between an environment and a phenotypic feature, where being ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FunctionalAssociation](FunctionalAssociation.md) | An association between a macromolecular machine mixin (gene, gene product or ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToGoTermAssociation](GeneToGoTermAssociation.md) | A functional association between a gene (or gene product or macromolecular co... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | A functional association between a macromolecular machine (gene, gene product... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | A functional association between a macromolecular machine (gene, gene product... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | A functional association between a macromolecular machine (gene, gene product... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | Describes an effect that a gene or gene product has on a chemical entity (e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | Relationship between a gene family and a contained gene or gene product or ge... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | An association between a gene or gene product or gene family and an anatomica... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | Relationship between a gene or gene product or gene family to a specified bio... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | Describes a regulatory relationship between two genes or gene products |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | An association between a gene or gene product and a disease, where variation ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | An association between a gene (or gene product) and a disease in which the ge... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | An association in which a gene (e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | A gene-to-disease association that is asserted on the grounds that the gene h... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | An association between a gene and a gene expression site, possibly qualified ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToGeneAssociation](GeneToGeneAssociation.md) | parent class for different kinds of gene-gene or gene product to gene product... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | Indicates that two genes are co-expressed, generally under the same condition... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | A homology association between two genes |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | An interaction between two genes or two gene products |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | An interaction at the molecular level between two physical entities |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | Set membership of a gene in a family of genes related by common evolutionary ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToPathwayAssociation](GeneToPathwayAssociation.md) | An interaction between a gene or gene product and a biological process or pat... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | An association between a gene or gene product and a phenotypic feature, where... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | An association between a genotype and a disease, in which the genotype (typic... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | An association in which a genotype serves as a model of a disease, recapitula... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | Any association between a genotype and a gene |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | Any association between one genotype and a genotypic entity that is a sub-com... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | Any association between one genotype and a phenotypic feature, where having t... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | Any association between a genotype and a sequence variant |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | association between a named thing and a information content entity where the ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | Describes the relationship between an enzyme (usually a macromolecular comple... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | An association between a material sample and the material entity from which i... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | An association between a material sample and a disease or phenotype |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | Added in response to capturing relationship between microbiome activities as ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | Added in response to capturing relationship between microbiome activities as ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | Association that holds the relationship between a reaction and the pathway it... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | An association in which the subject entity is linked to the likelihood of the... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | An abstract association between an organism taxon and an environmental contex... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | A relationship between two organism taxon nodes |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | An interaction relationship between two taxa |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | A child-parent relationship between two taxa |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | An association between two individual organisms (e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | An association in which an organismal entity (e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | An association between a phenotypic feature (sign or symptom) and a disease, ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | Association between two concept nodes of phenotypic character, qualified by t... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | An association between a two populations |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | Describes a regulatory relationship between two genes or gene products |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SequenceAssociation](SequenceAssociation.md) | An association between a sequence feature and a nucleic acid entity it is loc... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenomicSequenceLocalization](GenomicSequenceLocalization.md) | A relationship between a sequence feature and a nucleic acid entity it is loc... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SequenceFeatureRelationship](SequenceFeatureRelationship.md) | For example, a particular exon is part of a particular transcript or gene |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | A transcript is formed from multiple exons |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | A gene is transcribed and potentially translated to a gene product |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | A gene is a collection of transcripts |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | An association between a sequence variant and a treatment or health intervent... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | An association between two organism taxa, capturing ecological or evolutionar... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | An association between a sequence variant and a disease, in which the allele ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | An association in which a sequence variant serves as a model of a disease, re... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VariantToGeneAssociation](VariantToGeneAssociation.md) | An association between a variant and a gene, where the variant has a genetic ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | An association between a variant and expression of a gene (i |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | An association between a sequence variant and a phenotypic feature, in which ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VariantToPopulationAssociation](VariantToPopulationAssociation.md) | An association between a variant and a population, where the variant has part... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NamedThing](NamedThing.md) | a databased entity or concept/class |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Activity](Activity.md) | An activity is something that occurs over a period of time and acts upon or w... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Study](Study.md) | a detailed investigation and/or analysis |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalTrial](ClinicalTrial.md) | A clinical trial is a research study that prospectively assigns human partici... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NAMStudy](NAMStudy.md) | A study is a structured investigation or analysis, often involving the collec... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AdministrativeEntity](AdministrativeEntity.md) | An entity that is the byproduct of an administrative process |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Agent](Agent.md) | person, group, organization or project that provides a piece of information (... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AffinityMeasurement](AffinityMeasurement.md) | The type of measurement describing the strength of an affinity between two en... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Attribute](Attribute.md) | A property or characteristic of an entity |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalSex](BiologicalSex.md) | An organismal quality inhering in a bearer by virtue of the bearer's ability ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenotypicSex](GenotypicSex.md) | An attribute corresponding to the genotypic sex of the individual, based upon... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhenotypicSex](PhenotypicSex.md) | An attribute corresponding to the phenotypic sex of the individual, based upo... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalRole](ChemicalRole.md) | A role played by the molecular entity or part thereof within a chemical conte... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalAttribute](ClinicalAttribute.md) | Attributes relating to a clinical manifestation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalCourse](ClinicalCourse.md) | The course a disease typically takes from its onset, progression in time, and... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Onset](Onset.md) | The age group in which (disease) symptom manifestations appear |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalMeasurement](ClinicalMeasurement.md) | A clinical measurement is a special kind of attribute which results from a la... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalModifier](ClinicalModifier.md) | Used to characterize and specify the phenotypic abnormalities defined in the ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismAttribute](OrganismAttribute.md) | describes a characteristic of an organismal entity |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhenotypicQuality](PhenotypicQuality.md) | A characteristic of a phenotype (e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SeverityValue](SeverityValue.md) | describes the severity of a phenotypic feature or disease |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SocioeconomicAttribute](SocioeconomicAttribute.md) | Attributes relating to a socioeconomic manifestation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Zygosity](Zygosity.md) | An allelic state describing the degree of similarity between features at a si... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalEntity](BiologicalEntity.md) | A heterogeneous substance that contains genomic material or is the product of... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | Either an individual molecular activity, or a collection of causally connecte... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalProcess](BiologicalProcess.md) | One or more causally connected executions of molecular functions |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Behavior](Behavior.md) | The internally coordinated responses (actions or inactions) of organisms (ind... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PathologicalProcess](PathologicalProcess.md) | A biologic function or a process having an abnormal or deleterious effect at ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Pathway](Pathway.md) | A hierarchical ordering of connected molecular reactions (steps) that represe... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhysiologicalProcess](PhysiologicalProcess.md) | A biological or chemical function within a living organism |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MolecularActivity](MolecularActivity.md) | An execution of a molecular function carried out by a gene product or macromo... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CodingSequence](CodingSequence.md) | A contiguous sequence which begins with, and includes, a start codon and ends... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | A disease or an individual phenotypic feature, grouped as a single class to a... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Disease](Disease.md) | A disease is a disposition to undergo pathological processes that exists in a... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhenotypicFeature](PhenotypicFeature.md) | A combination of entity and quality that makes up a phenotyping statement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BehavioralFeature](BehavioralFeature.md) | A phenotypic feature which is behavioral in nature |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalFinding](ClinicalFinding.md) | this category is currently considered broad enough to tag clinical lab measur... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Exon](Exon.md) | A region of the transcript sequence within a gene which is not removed from t... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Gene](Gene.md) | A region (or regions) that includes all of the sequence elements necessary to... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneFamily](GeneFamily.md) | any grouping of multiple genes or gene products related by common descent |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneticInheritance](GeneticInheritance.md) | The pattern or 'mode' in which a particular genetic trait or disorder is pass... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Genome](Genome.md) | A genome is the sum of genetic material within a cell or virion |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Genotype](Genotype.md) | An information content entity that describes a genome by specifying the total... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Haplotype](Haplotype.md) | A set of zero or more Alleles on a single instance of a Sequence[VMC] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MacromolecularComplex](MacromolecularComplex.md) | A stable assembly of two or more macromolecules, i |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md) | A linear nucleotide sequence pattern that is widespread and has, or is conjec... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NucleosomeModification](NucleosomeModification.md) | A chemical modification of a histone protein within a nucleosome octomer or a... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismalEntity](OrganismalEntity.md) | A named entity that is either a part of an organism, a whole organism, popula... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AnatomicalEntity](AnatomicalEntity.md) | A part of a cellular organism at or above the granularity of a protein comple... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Cell](Cell.md) | The basic structural and functional unit of all organisms |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellularComponent](CellularComponent.md) | A location in or around a cell |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GrossAnatomicalStructure](GrossAnatomicalStructure.md) | An anatomical structure that has more than one cell as a part |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | An anatomical structure with the potential of have an abnormal or deleterious... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Bacterium](Bacterium.md) | A member of a group of unicellular microorganisms lacking a nuclear membrane,... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellLine](CellLine.md) | A cultured cell population that is genetically stable and homogeneous, sharin... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellularOrganism](CellularOrganism.md) | An organism that contains one or more cells belonging to the cellular lineage... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fungus](Fungus.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Invertebrate](Invertebrate.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Mammal](Mammal.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Human](Human.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Plant](Plant.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Vertebrate](Vertebrate.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IndividualOrganism](IndividualOrganism.md) | An instance of an organism |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Case](Case.md) | An individual (human) organism that has a patient role in some clinical conte... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LifeStage](LifeStage.md) | A stage of development or growth of an organism, including post-natal adult s... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | A collection of individuals from the same taxonomic class distinguished by on... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StudyPopulation](StudyPopulation.md) | A group of people banded together or treated as a group as participants in a ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Cohort](Cohort.md) | A group of people banded together or treated as a group who share common char... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virus](Virus.md) | A virus is a microorganism that replicates itself as a microRNA and infects t... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Polypeptide](Polypeptide.md) | A polypeptide is a molecular entity characterized by availability in protein ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Protein](Protein.md) | A gene product that is composed of a chain of amino acid sequences and is pro... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProteinIsoform](ProteinIsoform.md) | Represents a protein that is a specific isoform of the canonical or reference... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PosttranslationalModification](PosttranslationalModification.md) | A chemical modification of a polypeptide or protein that occurs after transla... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProteinDomain](ProteinDomain.md) | A conserved part of protein sequence and (tertiary) structure that can evolve... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProteinFamily](ProteinFamily.md) | A set of proteins coding for diverse functions which, by virtue of their high... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ReagentTargetedGene](ReagentTargetedGene.md) | A gene altered in its expression level in the context of some experiment as a... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RegulatoryRegion](RegulatoryRegion.md) | A region (or regions) of the genome that contains known or putative regulator... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AccessibleDnaRegion](AccessibleDnaRegion.md) | A region (or regions) of a chromatinized genome that has been measured to be ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) | A region (or regions) of the genome that contains a region of DNA known or pr... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SequenceVariant](SequenceVariant.md) | A sequence_variant is a non exact copy of a sequence_feature or genome exhibi... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Snv](Snv.md) | SNVs are single nucleotide positions in genomic DNA at which different sequen... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Transcript](Transcript.md) | An RNA synthesized on a DNA or RNA template by an RNA polymerase |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RNAProduct](RNAProduct.md) | High molecular weight, linear polymers, composed of nucleotides containing ri... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NoncodingRNAProduct](NoncodingRNAProduct.md) | An RNA transcript that does not encode for a protein rather the RNA molecule ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MicroRNA](MicroRNA.md) | A small (~22 nucleotide) RNA molecule that is the endogenous transcript of a ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SiRNA](SiRNA.md) | A small RNA molecule that is the product of a longer exogenous or endogenous ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RNAProductIsoform](RNAProductIsoform.md) | Represents a protein that is a specific isoform of the canonical or reference... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalSystem](BiologicalSystem.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellTypeCoverage](CellTypeCoverage.md) | Assessment of cell type representation and cellular diversity between systems |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalEntity](ChemicalEntity.md) | A chemical entity is a physical entity that pertains to chemistry or biochemi... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalMixture](ChemicalMixture.md) | A chemical mixture is a chemical entity composed of two or more molecular ent... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ComplexMolecularMixture](ComplexMolecularMixture.md) | A complex molecular mixture is a chemical mixture composed of two or more mol... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Food](Food.md) | A substance of plant, animal, or artificial origin consumed by a living organ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MolecularMixture](MolecularMixture.md) | A molecular mixture is a chemical mixture composed of two or more molecular e... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Drug](Drug.md) | A substance intended for use in the diagnosis, cure, mitigation, treatment, o... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProcessedMaterial](ProcessedMaterial.md) | A chemical entity (often a mixture) processed for consumption for nutritional... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | Any unwanted chemical in food |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FoodAdditive](FoodAdditive.md) | Any substance which is added to food to preserve or enhance its flavour and/o... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MolecularEntity](MolecularEntity.md) | A molecular entity is a chemical entity composed of individual or covalently ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NucleicAcidEntity](NucleicAcidEntity.md) | A nucleic acid entity is a molecular entity characterized by availability in ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SmallMolecule](SmallMolecule.md) | A small molecule entity is a molecular entity characterized by availability i... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalEntity](ClinicalEntity.md) | Any entity or process that exists in the clinical domain and outside the biol... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalIntervention](ClinicalIntervention.md) | A medical procedure, treatment, or action taken by healthcare professionals t... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Hospitalization](Hospitalization.md) | The admission and care of a patient in a hospital for observation, diagnosis,... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Device](Device.md) | A thing made or adapted for a particular purpose, especially a piece of mecha... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiagnosticAid](DiagnosticAid.md) | A device or substance used to help diagnose disease or injury |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Event](Event.md) | Something that happens at a given place and time |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EvidenceType](EvidenceType.md) | Class of evidence that supports an association |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExposureEvent](ExposureEvent.md) | A (possibly time bounded) incidence of a feature of the environment of an org... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BehavioralExposure](BehavioralExposure.md) | A behavioral exposure is a factor relating to behavior impacting an individua... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BioticExposure](BioticExposure.md) | An external biotic exposure is an intake of (sometimes pathological) biologic... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalExposure](ChemicalExposure.md) | A chemical exposure is an intake of a particular chemical entity |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DrugExposure](DrugExposure.md) | A drug exposure is an intake of a particular drug |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | drug to gene interaction exposure is a drug exposure is where the interaction... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ComplexChemicalExposure](ComplexChemicalExposure.md) | A complex chemical exposure is an intake of a chemical mixture, other than a ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | A disease or phenotypic feature state, when viewed as an exposure, represente... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EnvironmentalExposure](EnvironmentalExposure.md) | A environmental exposure is a factor relating to abiotic processes in the env... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeographicExposure](GeographicExposure.md) | A geographic exposure is a factor relating to geographic proximity to some im... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenomicBackgroundExposure](GenomicBackgroundExposure.md) | A genomic background exposure is where an individual's specific genomic backg... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) | An abnormal anatomical structure, when viewed as an exposure, represented as ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PathologicalProcessExposure](PathologicalProcessExposure.md) | A pathological process, when viewed as an exposure, representing a preconditi... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SocioeconomicExposure](SocioeconomicExposure.md) | A socioeconomic exposure is a factor relating to social and financial status ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Treatment](Treatment.md) | A treatment is targeted at a disease or phenotype and may involve multiple dr... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FunctionalAssay](FunctionalAssay.md) | A functional assay used to assess biological capabilities |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FunctionalParity](FunctionalParity.md) | Evaluation of functional capabilities and physiological responses between sys... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneExpressionResult](GeneExpressionResult.md) | A differential-expression measurement for a single gene in a model system |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InformationContentEntity](InformationContentEntity.md) | a piece of information that typically describes some topic of discourse or is... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CommonDataElement](CommonDataElement.md) | A Common Data Element (CDE) is a standardized, precisely defined question, pa... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ConfidenceLevel](ConfidenceLevel.md) | Level of confidence in a statement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Dataset](Dataset.md) | an item that refers to a collection of data from a data source |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NAMDataset](NAMDataset.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DatasetDistribution](DatasetDistribution.md) | an item that holds distribution level information about a dataset |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DatasetSummary](DatasetSummary.md) | an item that holds summary level information about a dataset |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DatasetVersion](DatasetVersion.md) | an item that holds version level information about a dataset |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Evidence](Evidence.md) | Dereferences detailed evidence that supports an association |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Publication](Publication.md) | Any ‘published’ piece of information |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Article](Article.md) | a piece of writing on a particular topic presented as a stand-alone section o... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[JournalArticle](JournalArticle.md) | an article, typically presenting results of research, that is published in an... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Book](Book.md) | This class may rarely be instantiated except if use cases of a given knowledg... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BookChapter](BookChapter.md) | A section of a book that forms a discrete unit of a larger published work and... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DrugLabel](DrugLabel.md) | a document accompanying a drug or its container that provides written, printe... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Patent](Patent.md) | a legal document granted by a patent issuing authority which confers upon the... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PreprintPublication](PreprintPublication.md) | a document reresenting an early version of an author's original scholarly wor... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Serial](Serial.md) | This class may rarely be instantiated except if use cases of a given knowledg... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[WebPage](WebPage.md) | a document that is published according to World Wide Web standards, which may... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RetrievalSource](RetrievalSource.md) | Provides information about how a particular InformationResource served as a s... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StudyVariable](StudyVariable.md) | a variable that is used as a measure in the investigation of a study |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MechanicalStimulation](MechanicalStimulation.md) | Specification of mechanical forces applied to the model system |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MicrofluidicDesign](MicrofluidicDesign.md) | Detailed specification of a microfluidic device design including its architec... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ModelSystem](ModelSystem.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AnimalModel](AnimalModel.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NAMModel](NAMModel.md) | A New Approach Methodology (NAM) model, which is a type of model system that ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellularSystem](CellularSystem.md) | Cell-based model systems that use living cells to model biological processes |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CoCulture](CoCulture.md) | Co-culture systems combining multiple cell types to mimic microenvironments a... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ThreeDCellCulture](ThreeDCellCulture.md) | Three-dimensional cell culture systems including spheroids and organoids |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Organoid](Organoid.md) | A 3D cell culture system that self-organizes to recapitulate key structural a... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TwoDCellCulture](TwoDCellCulture.md) | Conventional monolayer cell cultures grown on flat surfaces |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellLineModel](CellLineModel.md) | A model system based on immortalized cell lines that can be maintained in cul... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InSilicoModel](InSilicoModel.md) | Computational models that simulate biological processes without physical biol... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DigitalTwin](DigitalTwin.md) | Computational replicas of biological systems for real-time prediction and per... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MetabolicModel](MetabolicModel.md) | A model that simulates the metabolic processes of an organism or system |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MLModel](MLModel.md) | Machine Learning and AI-based models for prediction, mechanism inference, and... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PBPKModel](PBPKModel.md) | Physiologically Based Pharmacokinetic models that simulate drug absorption, d... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QSARModel](QSARModel.md) | Quantitative Structure-Activity Relationship models that predict chemical/bio... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MicrophysiologicalSystem](MicrophysiologicalSystem.md) | Organ-/tissue-on-chip systems that integrate microfluidics, biomaterials, and... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganOnChip](OrganOnChip.md) | A model system that simulates the physiological functions of an organ using a... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TissueOnChip](TissueOnChip.md) | Tissue-level microphysiological systems that model specific tissue functions ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MolecularSimilarity](MolecularSimilarity.md) | Detailed assessment of molecular-level concordance between model and biologic... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismTaxon](OrganismTaxon.md) | A classification of a set of organisms |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PathwayActivityResult](PathwayActivityResult.md) | An activity and enrichment measurement for a single biological pathway |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PathwayConcordance](PathwayConcordance.md) | Assessment of biological pathway conservation and activity between model and ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PBPKCompartment](PBPKCompartment.md) | A physiological compartment in a PBPK model |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Phenomenon](Phenomenon.md) | a fact or situation that is observed to exist or happen, especially one whose... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhenotypeOverlap](PhenotypeOverlap.md) | Comparison of phenotypic manifestations between model and biological systems |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhysicalEntity](PhysicalEntity.md) | An entity that has material reality (a |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MaterialSample](MaterialSample.md) | A sample is a limited quantity of something (e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PlanetaryEntity](PlanetaryEntity.md) | Any entity or process that exists at the level of the whole planet |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EnvironmentalFeature](EnvironmentalFeature.md) | A system or entity in the natural environment that has the disposition to env... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EnvironmentalProcess](EnvironmentalProcess.md) | A process that occurs within or involves the components of an environmental s... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeographicLocation](GeographicLocation.md) | a location that can be described in lat/long coordinates |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeographicLocationAtTime](GeographicLocationAtTime.md) | a location that can be described in lat/long coordinates, for a particular ti... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Procedure](Procedure.md) | A series of actions conducted in a certain order or manner |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Reproducibility](Reproducibility.md) | Assessment of experimental reproducibility and consistency of the model syste... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StudyResult](StudyResult.md) | A collection of data items from a study that are about a particular study sub... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChiSquaredAnalysisResult](ChiSquaredAnalysisResult.md) | A result of a chi squared analysis |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ConceptCountAnalysisResult](ConceptCountAnalysisResult.md) | A result of a concept count analysis |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IceesStudyResult](IceesStudyResult.md) | A study result that represents a result, from a supporting Study, which is sp... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LogOddsAnalysisResult](LogOddsAnalysisResult.md) | A result of a log odds ratio analysis |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ObservedExpectedFrequencyAnalysisResult](ObservedExpectedFrequencyAnalysisResult.md) | A result of a observed expected frequency analysis |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RelativeFrequencyAnalysisResult](RelativeFrequencyAnalysisResult.md) | A result of a relative frequency analysis |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TextMiningStudyResult](TextMiningStudyResult.md) | A study result that represents information extracted from text using natural ... |
| [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md) |  |
| [EntityToExposureEventAssociationMixin](EntityToExposureEventAssociationMixin.md) | An association between some entity and an exposure event |
| [EntityToOutcomeAssociationMixin](EntityToOutcomeAssociationMixin.md) | An association between some entity and an outcome |
| [EpidemiologicalOutcome](EpidemiologicalOutcome.md) | An epidemiological outcome, such as societal disease burden, resulting from a... |
| [EpigenomicEntity](EpigenomicEntity.md) | A mixin for entities that represent epigenomic modifications or features asso... |
| [FrequencyQualifierMixin](FrequencyQualifierMixin.md) | Qualifier for frequency type associations |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | Qualifiers for entity to disease or phenotype associations |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | mixin class for any association whose object (target node) is a disease |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | A mixin applied to any association whose object (target node) is a phenotypic... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityToFeatureOrGeneQualifiersMixin](EntityToFeatureOrGeneQualifiersMixin.md) | Qualifiers for entity to gene associations |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityToFeatureOrVariantQualifiersMixin](EntityToFeatureOrVariantQualifiersMixin.md) | Qualifiers for entity to variant associations |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FeatureOrDiseaseQualifiersToEntityMixin](FeatureOrDiseaseQualifiersToEntityMixin.md) | Qualifiers for disease or phenotype to entity associations |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md) | A mixin applied to any association whose subject (source node) is a phenotypi... |
| [GeneExpressionMixin](GeneExpressionMixin.md) | Observed gene expression intensity, context (site, stage) and associated phen... |
| [GeneGroupingMixin](GeneGroupingMixin.md) | any grouping of multiple genes or gene products |
| [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md) |  |
| [GenomicEntity](GenomicEntity.md) | A generically dependent continuant that carries biological sequence that is p... |
| [GenotypeToEntityAssociationMixin](GenotypeToEntityAssociationMixin.md) |  |
| [HospitalizationOutcome](HospitalizationOutcome.md) | An outcome resulting from an exposure event which is the increased manifestat... |
| [KnowledgeGraph](KnowledgeGraph.md) | A knowledge graph is a structured representation of knowledge in the form of ... |
| [KnowledgeGraph](KnowledgeGraph.md) | A container representing a knowledge graph serialized in KGX (Knowledge Graph... |
| [MacromolecularMachineMixin](MacromolecularMachineMixin.md) | A union of gene locus, gene product, and macromolecular complex |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneOrGeneProduct](GeneOrGeneProduct.md) | A union of gene loci or gene products |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneProductMixin](GeneProductMixin.md) | The functional molecular product of a single gene locus |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneProductIsoformMixin](GeneProductIsoformMixin.md) | This is an abstract class that can be mixed in with different kinds of gene p... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneOrGeneProductOrGeneFamily](GeneOrGeneProductOrGeneFamily.md) | A union of gene family or gene loci or gene products, useful to define the as... |
| [MacromolecularMachineToEntityAssociationMixin](MacromolecularMachineToEntityAssociationMixin.md) | an association which has a macromolecular machine mixin as a subject |
| [MappingCollection](MappingCollection.md) | An abstract container class that holds a set of predicate mappings |
| [MaterialSampleToEntityAssociationMixin](MaterialSampleToEntityAssociationMixin.md) | An association between a material sample and something |
| [ModelToDiseaseAssociationMixin](ModelToDiseaseAssociationMixin.md) | This mixin is used for any association class for which the subject (source no... |
| [ModelPerformance](ModelPerformance.md) | Statistical performance metrics for computational models |
| [ModelsRelationship](ModelsRelationship.md) |  |
| [MortalityOutcome](MortalityOutcome.md) | An outcome of death from resulting from an exposure event |
| [Node](Node.md) | A generic node in a KGX-formatted knowledge graph, representing a single enti... |
| [OntologyClass](OntologyClass.md) | a concept or class in an ontology, vocabulary or thesaurus |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RelationshipType](RelationshipType.md) | An OWL property used as an edge label |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TaxonomicRank](TaxonomicRank.md) | A descriptor for the rank within a taxonomic classification |
| [OrganismTaxonToEntityAssociation](OrganismTaxonToEntityAssociation.md) | An association between an organism taxon and another entity |
| [Outcome](Outcome.md) | An entity that has the role of being the consequence of an exposure event |
| [PathologicalAnatomicalOutcome](PathologicalAnatomicalOutcome.md) | An outcome resulting from an exposure event which is the manifestation of an ... |
| [PathologicalEntityMixin](PathologicalEntityMixin.md) | A pathological (abnormal) structure or process |
| [PathologicalProcessOutcome](PathologicalProcessOutcome.md) | An outcome resulting from an exposure event which is the manifestation of a p... |
| [PhysicalEssenceOrOccurrent](PhysicalEssenceOrOccurrent.md) | Either a physical or processual entity |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Occurrent](Occurrent.md) | A processual entity |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ActivityAndBehavior](ActivityAndBehavior.md) | Activity or behavior of any independent integral living, organization or mech... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhysicalEssence](PhysicalEssence.md) | Semantic mixin concept |
| [PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |
| [QualityControlMetric](QualityControlMetric.md) | A quality control measure and its associated value |
| [Reference](Reference.md) | A literature reference with identifier and title for citing published work |
| [RelationshipQuantifier](RelationshipQuantifier.md) | A mixin for quantifying aspects of the strength, frequency, or specificity of... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FrequencyQuantifier](FrequencyQuantifier.md) | A relationship quantifier that expresses how often a relationship holds, usin... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SensitivityQuantifier](SensitivityQuantifier.md) | A relationship quantifier that measures the sensitivity of a relationship, su... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SpecificityQuantifier](SpecificityQuantifier.md) | A relationship quantifier that measures the specificity of a relationship, su... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PathognomonicityQuantifier](PathognomonicityQuantifier.md) | A relationship quantifier between a variant or symptom and a disease, which i... |
| [SocioeconomicOutcome](SocioeconomicOutcome.md) | An general social or economic outcome, such as healthcare costs, utilization,... |
| [StatisticalSignificance](StatisticalSignificance.md) | Statistical measures of significance for molecular comparisons |
| [StructuredConcordanceResult](StructuredConcordanceResult.md) | Detailed structured assessment of concordance between model and biological sy... |
| [SubjectOfInvestigation](SubjectOfInvestigation.md) | An entity that has the role of being studied in an investigation, study, or e... |
| [ThingWithTaxon](ThingWithTaxon.md) | A mixin that can be used on any entity that can be taxonomically classified |
| [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md) |  |



## Slots

| Slot | Description |
| --- | --- |
| [accuracy](accuracy.md) | Overall accuracy of the model (0 |
| [active_in](active_in.md) | Holds between a gene or gene product and a cellular component in which it car... |
| [active_pathways](active_pathways.md) | List of biological pathways that are active in both systems |
| [actively_involved_in](actively_involved_in.md) | holds between a continuant and a process or function, where the continuant ac... |
| [actively_involves](actively_involves.md) |  |
| [activity_endpoint](activity_endpoint.md) | Biological activity or property being predicted |
| [activity_score](activity_score.md) | Quantitative measure of pathway activity |
| [acts_upstream_of](acts_upstream_of.md) | Holds between a gene or gene product and a biological process such that the m... |
| [acts_upstream_of_negative_effect](acts_upstream_of_negative_effect.md) | Holds between a gene or gene product and a biological process where the molec... |
| [acts_upstream_of_or_within](acts_upstream_of_or_within.md) | Holds between a gene or gene product and a biological process when the gene p... |
| [acts_upstream_of_or_within_negative_effect](acts_upstream_of_or_within_negative_effect.md) | Holds between a gene or gene product and a biological process when the gene p... |
| [acts_upstream_of_or_within_positive_effect](acts_upstream_of_or_within_positive_effect.md) | Holds between a gene or gene product and a biological process when the gene p... |
| [acts_upstream_of_positive_effect](acts_upstream_of_positive_effect.md) | Holds between a gene or gene product and a biological process where the molec... |
| [address](address.md) | the particulars of the place where someone or an organization is situated |
| [adjusted_p_value](adjusted_p_value.md) | The adjusted p-value is the probability of obtaining test results at least as... |
| [adjusted_p_value](adjusted_p_value.md) | Multiple testing corrected p-value |
| [adverse_event_of](adverse_event_of.md) |  |
| [affected_by](affected_by.md) | describes an entity of which the state or quality is affected by another exis... |
| [affects](affects.md) | Describes an entity that has an effect on the state or quality of another exi... |
| [affects_likelihood_of](affects_likelihood_of.md) | Holds between two entities where the presence or application of one alters th... |
| [affects_sensitivity_to](affects_sensitivity_to.md) | holds between two chemical entities or genes or gene products where the actio... |
| [affiliation](affiliation.md) | a professional relationship between one provider (often a person) within anot... |
| [affinity](affinity.md) | The numerical value describing the strength of an affinity between two entiti... |
| [affinity_parameter](affinity_parameter.md) | The type of parameter describing the strength of an affinity between two enti... |
| [age_value](age_value.md) | Chronological age of the animal at the time of study, as a numeric value with... |
| [agent_type](agent_type.md) | Describes the high-level category of agent who originally generated a stateme... |
| [aggregate_statistic](aggregate_statistic.md) | An abstract grouping for summary numerical measures (e |
| [aggregator_knowledge_source](aggregator_knowledge_source.md) | An intermediate aggregator resource from which knowledge expressed in an Asso... |
| [allelic_requirement](allelic_requirement.md) | The allele configuration of a particular gene or variant required for the exp... |
| [ameliorates_condition](ameliorates_condition.md) | Holds between an entity and an existing medical condition (disease or phenoty... |
| [amount_or_activity_decreased_by](amount_or_activity_decreased_by.md) |  |
| [amount_or_activity_increased_by](amount_or_activity_increased_by.md) |  |
| [anatomical_context_qualifier](anatomical_context_qualifier.md) | A statement qualifier representing an anatomical location where an relationsh... |
| [anatomical_structure_modeled](anatomical_structure_modeled.md) | The anatomical structure being modeled — a tissue, organ, or other multicellu... |
| [animal_model_available_from](animal_model_available_from.md) | A resource (such as a model organism database) from which an animal model rep... |
| [applied_to_treat](applied_to_treat.md) | Holds between an  substance, procedure, or activity and a medical condition, ... |
| [architecture_type](architecture_type.md) | The overall architecture type of the microfluidic device |
| [aspect_qualifier](aspect_qualifier.md) | Composes with the core concept to describe new concepts of a different ontolo... |
| [assay_result](assay_result.md) | Quantitative result of the assay |
| [assay_type](assay_type.md) | Type of functional assay (e |
| [associated_environmental_context](associated_environmental_context.md) | An attribute that can be applied to an association where the association hold... |
| [associated_with](associated_with.md) | Expresses a relationship between two named things where the relationship is t... |
| [associated_with_decreased_likelihood_of](associated_with_decreased_likelihood_of.md) | Expresses a relationship between two named things where the relationship is t... |
| [associated_with_increased_likelihood_of](associated_with_increased_likelihood_of.md) | Expresses a relationship between two named things where the relationship is t... |
| [associated_with_likelihood_of](associated_with_likelihood_of.md) | A a relationship that holds between two concepts represented by variables for... |
| [associated_with_resistance_to](associated_with_resistance_to.md) | A relation that holds between a named thing and a chemical that specifies tha... |
| [associated_with_response_to](associated_with_response_to.md) | A statistical association used to indicate that the object of a statement usi... |
| [associated_with_sensitivity_to](associated_with_sensitivity_to.md) | A relation that holds between a named thing and a chemical that specifies tha... |
| [association_slot](association_slot.md) | any slot that relates an association to another entity |
| [auc](auc.md) | Area under the ROC curve |
| [authentication_method](authentication_method.md) | Method used for cell line authentication (e |
| [author](author.md) | an instance of one (co-)creator primarily responsible for a written work |
| [authors](authors.md) | connects an publication to the list of authors who contributed to the publica... |
| [available_from](available_from.md) | The regulatory or commercial availability channel through which a drug or che... |
| [barrier_functions](barrier_functions.md) | Tissue barrier functions modeled (epithelial, endothelial, etc |
| [base_coordinate](base_coordinate.md) | A position in the base coordinate system |
| [batch_to_batch_variation](batch_to_batch_variation.md) | Measure of variation between different experimental batches |
| [beneficial_in_models_for](beneficial_in_models_for.md) | Holds between an  substance, procedure, or activity and a medical condition, ... |
| [binds](binds.md) | A causal mechanism mediated by the direct contact between effector and target... |
| [biological_role_mixin](biological_role_mixin.md) | A role played by the chemical entity or part thereof within a biological cont... |
| [biological_context](biological_context.md) | tissue/region (anatomy), cell types, sex/age equivalents, mechanics (e |
| [biological_organization_level](biological_organization_level.md) | The level of biological organization represented by the model |
| [biological_proportion](biological_proportion.md) | Proportion of this cell type in the biological system |
| [biological_specific_phenotypes](biological_specific_phenotypes.md) | List of phenotypes present only in the biological system |
| [biological_system_modeled](biological_system_modeled.md) |  |
| [biomarker_for](biomarker_for.md) | holds between a measurable chemical entity and a disease or phenotypic featur... |
| [blood_flow](blood_flow.md) | Blood flow to the compartment (L/h) |
| [bonferonni_adjusted_p_value](bonferonni_adjusted_p_value.md) | The Bonferroni correction is an adjustment made to P values when several depe... |
| [broad_match](broad_match.md) | a list of terms from different schemas or terminology systems that have a bro... |
| [broad_matches](broad_matches.md) | A list of terms from different schemas or terminology systems that have a bro... |
| [broad_synonym](broad_synonym.md) | An alternate label for an entity whose meaning is broader (more general) than... |
| [can_be_carried_out_by](can_be_carried_out_by.md) |  |
| [capable_of](capable_of.md) | holds between a physical entity and process or function, where the continuant... |
| [catalyst_qualifier](catalyst_qualifier.md) | a qualifier that connects an association between two causally connected entit... |
| [catalyzes](catalyzes.md) | Holds between a macromolecular machine (typically an enzyme or ribozyme) and ... |
| [category](category.md) | Name of the high level ontology class in which this entity is categorized |
| [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | A statement qualifier representing a type of molecular control mechanism thro... |
| [caused_by](caused_by.md) | holds between two entities where the occurrence, existence, or activity of on... |
| [causes](causes.md) | holds between two entities where the occurrence, existence, or activity of on... |
| [cell_ratios](cell_ratios.md) | Ratios of different cell types in the co-culture |
| [cell_source](cell_source.md) | Source of cells (e |
| [cell_type](cell_type.md) | The cell type for which the ratio is specified |
| [cell_type_coverage](cell_type_coverage.md) |  |
| [cell_type_proportions](cell_type_proportions.md) | Quantitative comparison of cell type proportions |
| [cell_types](cell_types.md) | Cell types present in the cellular system |
| [channel_configuration](channel_configuration.md) | Configuration of channels (e |
| [channel_dimensions](channel_dimensions.md) | Dimensions of the channels in the device |
| [channel_name](channel_name.md) | Name or identifier of the channel (e |
| [chapter](chapter.md) | chapter of a book |
| [chembl_assay_description](chembl_assay_description.md) | Text describing the assay associated with a chemical entity |
| [chembl_availability_type](chembl_availability_type.md) | Text indicating the availability type of the chemical entity |
| [chembl_binding_site_comment](chembl_binding_site_comment.md) | Text describing the binding site for a chemical entity |
| [chembl_binding_site_name](chembl_binding_site_name.md) | Text indicating the name of the binding site for a chemical entity |
| [chembl_black_box_warning](chembl_black_box_warning.md) | Text describing black box warnings for use of chemicals as therapeutics |
| [chembl_chirality](chembl_chirality.md) | Tern indicating the chirality of the chemical entity |
| [chembl_confidence_score](chembl_confidence_score.md) | A score defined by ChEMBL that represents the confidence level of a particula... |
| [chembl_drug_warning](chembl_drug_warning.md) | Text describing warnings for use of chemicals as therapeutics |
| [chembl_mechanism_of_action_comment](chembl_mechanism_of_action_comment.md) | Additional comments regarding the mechanism of action |
| [chembl_mechanism_of_action_description](chembl_mechanism_of_action_description.md) | Text describing the mechanism of action for a chemical entity |
| [chembl_mutation](chembl_mutation.md) | Text describing mutations associated with a chemical entity |
| [chembl_mutation_accession](chembl_mutation_accession.md) | Accession identifier for a mutation associated with a chemical entity |
| [chembl_natural_product](chembl_natural_product.md) | Flag indicating if a chemical entity is a natural product |
| [chembl_prodrug](chembl_prodrug.md) | Flag indicating if a drug is a prodrug that is active only after being metabo... |
| [chembl_selectivity_comment](chembl_selectivity_comment.md) | Additional comments regarding the selectivity of the drug |
| [chemical_entity_or_drug_or_treatment](chemical_entity_or_drug_or_treatment.md) | A union of chemical entities and children, and drug or treatment |
| [chemical_role_mixin](chemical_role_mixin.md) | A role played by the chemical entity or part thereof within a chemical contex... |
| [chemically_similar_to](chemically_similar_to.md) | holds between one small molecule entity and another that it approximates for ... |
| [chi_squared_dof](chi_squared_dof.md) | Degrees of freedom (dof) in a chi-squared test referring to the number of val... |
| [chi_squared_p](chi_squared_p.md) | The chi-square p-value tells you the probability that the observed difference... |
| [chi_squared_statistic](chi_squared_statistic.md) | The chi-squared statistic measures how much observed data deviate from expect... |
| [clearance](clearance.md) | Total body clearance (L/h) |
| [clinical_approval_status](clinical_approval_status.md) | The clinical approval status of a chemical entity for treating a specific dis... |
| [clinical_modifier_qualifier](clinical_modifier_qualifier.md) | the method or process of administering a pharmaceutical compound to achieve a... |
| [clinical_trial_age_range](clinical_trial_age_range.md) | The age range of a clinical trial as determined by clinicaltrials |
| [clinical_trial_age_stage](clinical_trial_age_stage.md) | The age stage of a clinical trial as determined by clinicaltrials |
| [clinical_trial_brief_title](clinical_trial_brief_title.md) | The brief title of a clinical trial as determined by clinicaltrials |
| [clinical_trial_conditions](clinical_trial_conditions.md) | connects a clinical trial to one or more conditions being studied in the tria... |
| [clinical_trial_enrollment](clinical_trial_enrollment.md) | The enrollment number of a clinical trial as determined by clinicaltrials |
| [clinical_trial_enrollment_type](clinical_trial_enrollment_type.md) | The enrollment type of a clinical trial as determined by clinicaltrials |
| [clinical_trial_intervention_boxed_warning](clinical_trial_intervention_boxed_warning.md) | A boolean flag indicating whether a clinical trial intervention has a boxed w... |
| [clinical_trial_intervention_model](clinical_trial_intervention_model.md) | The intervention model of a clinical trial as determined by clinicaltrials |
| [clinical_trial_interventions](clinical_trial_interventions.md) | connects a clinical trial to one or more interventions being tested in the tr... |
| [clinical_trial_overall_status](clinical_trial_overall_status.md) | The overall status of a clinical trial as determined by clinicaltrials |
| [clinical_trial_phase](clinical_trial_phase.md) | The phase that a clinical trials study represents |
| [clinical_trial_primary_purpose](clinical_trial_primary_purpose.md) | The primary purpose of a clinical trial as determined by clinicaltrials |
| [clinical_trial_start_date](clinical_trial_start_date.md) | The start date of a clinical trial as determined by clinicaltrials |
| [clinical_trial_tested_intervention](clinical_trial_tested_intervention.md) | Records whether the clinical trials are testing the intervention |
| [clinical_trial_time_perspective](clinical_trial_time_perspective.md) | The time perspective of a clinical trial as determined by clinicaltrials |
| [close_match](close_match.md) | a list of terms from different schemas or terminology systems that have a sem... |
| [coculture_configuration](coculture_configuration.md) | Configuration of co-culture (direct contact, transwell, conditioned media) |
| [coefficient_of_variation](coefficient_of_variation.md) | Coefficient of variation across experimental replicates |
| [coexists_with](coexists_with.md) | holds between two entities that are co-located in the same aggregate object, ... |
| [coexpressed_with](coexpressed_with.md) | holds between any two genes or gene products, in which both are generally exp... |
| [colocalizes_with](colocalizes_with.md) | holds between two entities that are observed to be located in the same place |
| [compartment_type](compartment_type.md) | Type of physiological compartment |
| [compartments](compartments.md) | Physiological compartments included in the model |
| [completed_by](completed_by.md) |  |
| [complexity_level](complexity_level.md) | Level of biological complexity represented (subcellular, cellular, tissue, or... |
| [composed_primarily_of](composed_primarily_of.md) | x composed_primarily_of_y if:more than half of the mass of x is made from par... |
| [compound_tested](compound_tested.md) | Name of compound used in dose-response testing |
| [computational_method](computational_method.md) | Primary computational method or algorithm used |
| [concept_count_object](concept_count_object.md) | The number of instances in a dataset/cohort whose records contain the concept... |
| [concept_count_subject](concept_count_subject.md) | The number of instances in a dataset/cohort whose records contain the concept... |
| [concept_pair_count](concept_pair_count.md) | The number of instances in a dataset/cohort whose records contain both the su... |
| [concordance](concordance.md) | Metrics used to assess the concordance between the model system and the biolo... |
| [condition_ameliorated_by](condition_ameliorated_by.md) |  |
| [condition_associated_with_gene](condition_associated_with_gene.md) | holds between a gene and a disease or phenotypic feature that may be influenc... |
| [condition_exacerbated_by](condition_exacerbated_by.md) |  |
| [condition_predisposed_by](condition_predisposed_by.md) |  |
| [condition_promoted_by](condition_promoted_by.md) |  |
| [confidence_interval_lower](confidence_interval_lower.md) | Lower bound of confidence interval |
| [confidence_interval_upper](confidence_interval_upper.md) | Upper bound of confidence interval |
| [confluence_level](confluence_level.md) | Typical confluence level maintained (0 |
| [conserved_functions](conserved_functions.md) | List of biological functions conserved between model and biological system |
| [conserved_genes](conserved_genes.md) | List of genes with conserved expression patterns between model and target |
| [consumed_by](consumed_by.md) |  |
| [consumes](consumes.md) | Holds between a process and an entity that is taken in and depleted by the pr... |
| [contains_process](contains_process.md) |  |
| [context_qualifier](context_qualifier.md) | Restricts the setting/context/location where the core concept (or qualified c... |
| [context_of_use](context_of_use.md) | What decision will this inform? Care? Policy? Drug approval? |
| [contraindicated_in](contraindicated_in.md) | Holds between a substance, procedure, or activity and a medical condition or ... |
| [contributes_to](contributes_to.md) | holds between two entities where the occurrence, existence, or activity of on... |
| [contribution_from](contribution_from.md) |  |
| [contributor](contributor.md) | Links an information content entity (such as a dataset, publication, or softw... |
| [correlated_with](correlated_with.md) | A relationship that holds between two concepts represented by variables for w... |
| [correlation_coefficient](correlation_coefficient.md) | Pearson correlation coefficient for expression profiles |
| [coverage_percentage](coverage_percentage.md) | Percentage of target cell types represented in the model system |
| [created_with](created_with.md) | An identifier (typically a URL or CURIE) of the software tool, service, or pi... |
| [creation_date](creation_date.md) | date on which an entity was created |
| [cross_validation](cross_validation.md) | Cross-validation strategy and results |
| [culture_conditions](culture_conditions.md) | Standard culture conditions and media used |
| [culture_system](culture_system.md) | Culture system used (e |
| [cv_method](cv_method.md) | Type of cross-validation used |
| [cv_score](cv_score.md) | Average cross-validation score |
| [cv_std](cv_std.md) | Standard deviation of cross-validation scores |
| [cyclic_stretch_percent](cyclic_stretch_percent.md) | Percentage of cyclic stretch applied (if applicable) |
| [data_source](data_source.md) | Source of molecular data (e |
| [dataset_count](dataset_count.md) | The total number of instances in a dataset/cohort |
| [dataset_download_url](dataset_download_url.md) | A URL from which the dataset itself may be directly downloaded specialised fo... |
| [decreased_amount_in](decreased_amount_in.md) |  |
| [decreased_likelihood_associated_with](decreased_likelihood_associated_with.md) |  |
| [decreases_amount_or_activity_of](decreases_amount_or_activity_of.md) | A grouping mixin to help with searching for all the predicates that decrease ... |
| [decreases_sensitivity_to](decreases_sensitivity_to.md) | holds between two chemical entities or genes or gene products where the actio... |
| [deprecated](deprecated.md) | A boolean flag indicating that an entity is no longer considered current or v... |
| [derivative_qualifier](derivative_qualifier.md) | A qualifier that composes with a core subject/object  concept to describe som... |
| [derives_from](derives_from.md) | holds between two distinct material entities, the new entity and the old enti... |
| [derives_into](derives_into.md) | holds between two distinct material entities, the old entity and the new enti... |
| [description](description.md) | a human-readable description of an entity |
| [develops_from](develops_from.md) | Holds between two entities where the first develops, by one or more developme... |
| [develops_into](develops_into.md) |  |
| [dgidb_evidence_score](dgidb_evidence_score.md) | A score defined by DGIdb that is used to report the amount of evidence suppor... |
| [dgidb_interaction_score](dgidb_interaction_score.md) | A score defined by DGIdb that is used to rank interaction record results in D... |
| [dgidb_relative_drug_specificity_score](dgidb_relative_drug_specificity_score.md) | A score defined by DGIdb that quantifies the gene-interaction specificity of ... |
| [dgidb_relative_gene_specificity_score](dgidb_relative_gene_specificity_score.md) | A score defined by DGIdb that quantifies the drug-interaction specificity of ... |
| [diagnoses](diagnoses.md) | a relationship that identifies the nature of (an illness or other problem) by... |
| [differentially_expressed_genes](differentially_expressed_genes.md) | List of genes that are differentially expressed in the model system |
| [differentiation_method](differentiation_method.md) | Method used to differentiate cells into organoid (e |
| [direction_qualifier](direction_qualifier.md) | Composes with the core concept (+ aspect if provided) to describe a change in... |
| [directly_physically_interacts_with](directly_physically_interacts_with.md) | A causal mechanism mediated by a direct contact between the effector and targ... |
| [disease_context_qualifier](disease_context_qualifier.md) | A context qualifier representing a disease or condition in which a relationsh... |
| [disease_has_basis_in](disease_has_basis_in.md) | A relation that holds between a disease and an entity where the state of the ... |
| [disease_has_location](disease_has_location.md) | A relationship between a disease and an anatomical entity where the disease h... |
| [diseases_confidence_score](diseases_confidence_score.md) | A score defined by Jensen Lab Diseases that reports confidence level in an as... |
| [disrupted_by](disrupted_by.md) | describes a relationship where the structure, function, or occurrence of one ... |
| [disrupts](disrupts.md) | describes a relationship where one entity degrades or interferes with the str... |
| [distribution_download_url](distribution_download_url.md) | A URL from which a specific distribution (serialization or format) of a datas... |
| [divergent_pathways](divergent_pathways.md) | List of pathways that show different activity patterns |
| [dose_response_similarity](dose_response_similarity.md) | Comparison of dose-response relationships for therapeutic compounds |
| [download_url](download_url.md) | A URL from which the information content entity may be directly downloaded in... |
| [drug_regulatory_status_world_wide](drug_regulatory_status_world_wide.md) | An agglomeration of drug regulatory status worldwide |
| [drug_properties](drug_properties.md) | Physicochemical and pharmacological properties modeled |
| [drug_rep_hub_disease_area](drug_rep_hub_disease_area.md) | A term used by Drug Repurposing Hub to describe the disease area associated w... |
| [druggable_gene_category](druggable_gene_category.md) | Classification of druggable genes based on knowledge about drug or small mole... |
| [duration_minutes](duration_minutes.md) | Duration of mechanical stimulation in minutes |
| [ec50_ratio](ec50_ratio.md) | Ratio of EC50 values between model and biological system |
| [edges](edges.md) | A list of associations between two entities |
| [editor](editor.md) | editor of a compiled work such as a book or a periodical (newspaper or an aca... |
| [elevate_to_prediction](elevate_to_prediction.md) | A boolean flag indicating whether a clinical trial finding should be elevated... |
| [elimination_pathways](elimination_pathways.md) | Drug elimination and metabolism pathways included |
| [enabled_by](enabled_by.md) | holds between a process and a physical entity, where the physical entity exec... |
| [enables](enables.md) | holds between a physical entity and a process, where the physical entity exec... |
| [end_coordinate](end_coordinate.md) | The position at which the subject genomic entity ends on the chromosome or ot... |
| [end_interbase_coordinate](end_interbase_coordinate.md) | The position at which the subject nucleic acid entity ends on the chromosome ... |
| [endpoints](endpoints.md) | phenotypes, function (TEER/leak, beating rate), and multi-omics |
| [enrichment_score](enrichment_score.md) | Statistical enrichment score for the pathway |
| [enrichment_statistics](enrichment_statistics.md) | Statistical measures of pathway enrichment |
| [environment](environment.md) | The environmental conditions under which the animal model is maintained |
| [equivalent_identifiers](equivalent_identifiers.md) | A set of identifiers that are considered equivalent to the primary identifier... |
| [evidence_count](evidence_count.md) | The number of evidence instances that are connected to an association |
| [exacerbates_condition](exacerbates_condition.md) | Holds between a substance, procedure, or activity and an existing medical con... |
| [exact_match](exact_match.md) | holds between two entities that have strictly equivalent meanings, with a hig... |
| [exact_matches](exact_matches.md) | A list of terms from different schemas or terminology systems that have an id... |
| [exact_synonym](exact_synonym.md) | An alternate label for an entity that denotes exactly the same meaning as the... |
| [expected_count](expected_count.md) | The expected (calculated) number of instances in a dataset/cohort whose recor... |
| [exposure_additional_condition](exposure_additional_condition.md) | Additional conditions impacting an exposure event |
| [exposure_duration](exposure_duration.md) | Duration of an exposure event |
| [exposure_end_age](exposure_end_age.md) | Ending stage of an exposure event |
| [exposure_magnitude](exposure_magnitude.md) | Magnitude of an exposure event, e |
| [exposure_route](exposure_route.md) | Route of exposure |
| [exposure_start_age](exposure_start_age.md) | Starting age of an exposure event |
| [exposure_type](exposure_type.md) | Type of exposure |
| [exposure_vehicle](exposure_vehicle.md) | Type of an exposure event |
| [expressed_in](expressed_in.md) | holds between a gene or gene product and an anatomical entity in which it is ... |
| [expresses](expresses.md) | holds between an anatomical entity and gene or gene product that is expressed... |
| [expression_site](expression_site.md) | location in which gene or protein expression takes place |
| [extraction_confidence_score](extraction_confidence_score.md) | A quantitative confidence value that represents the probability of obtaining ... |
| [FDA_adverse_event_level](FDA_adverse_event_level.md) | The level or severity grade of an adverse event as classified by FDA adverse-... |
| [FDA_regulatory_approvals](FDA_regulatory_approvals.md) | Numbers that identify specific drug applications |
| [feature_types](feature_types.md) | Types of features used (molecular, phenotypic, imaging, etc |
| [fisher_exact_odds_ratio](fisher_exact_odds_ratio.md) | The Fisher Exact Test is used to determine whether there is a non-random asso... |
| [fisher_exact_p](fisher_exact_p.md) | The Fisher exact p-value tells you the probability of observing a table as ex... |
| [flow_control_method](flow_control_method.md) | Methods used to control fluid flow in the device |
| [fold_change](fold_change.md) | Fold change in expression compared to control or reference |
| [food_component_of](food_component_of.md) | holds between a one or more chemical entities present in food, irrespective o... |
| [form_or_variant_qualifier](form_or_variant_qualifier.md) | A qualifier that composes with a core subject/object concept to define a spec... |
| [format](format.md) | The file format, physical medium, or representational form of the information... |
| [frequency_qualifier](frequency_qualifier.md) | a qualifier used in a phenotypic association to state how frequent the phenot... |
| [frequency_hz](frequency_hz.md) | Frequency of mechanical stimulation in Hertz |
| [full_name](full_name.md) | a long-form human readable name for a thing |
| [functional_assays](functional_assays.md) | List of functional assays used to assess parity |
| [functional_parity](functional_parity.md) |  |
| [functional_similarity_score](functional_similarity_score.md) | Quantitative score (0 |
| [gene](gene.md) | The gene this measurement is about |
| [gene_associated_with_condition](gene_associated_with_condition.md) | holds between a gene and a disease or phenotypic feature that the gene or its... |
| [gene_product_of](gene_product_of.md) | definition x has gene product of y if and only if y is a gene (SO:0000704) th... |
| [gene2phenotype_confidence_category](gene2phenotype_confidence_category.md) | A term used by EBI Gene2Phenotype to describe the confidence that the associa... |
| [gene_fusion_with](gene_fusion_with.md) | holds between two independent genes that have fused through translocation, in... |
| [genes_in_dataset](genes_in_dataset.md) | Number of genes from dataset found in pathway |
| [genes_in_pathway](genes_in_pathway.md) | Number of genes in the pathway |
| [genetic_association](genetic_association.md) |  |
| [genetic_neighborhood_of](genetic_neighborhood_of.md) | holds between two genes located nearby one another on a chromosome |
| [genetically_associated_with](genetically_associated_with.md) | A statistical association, observed in genetic studies, between a genetic ent... |
| [genetically_interacts_with](genetically_interacts_with.md) | holds between two genes whose phenotypic effects are dependent on each other ... |
| [genome_build](genome_build.md) | The version of the genome on which a feature is located |
| [has_active_component](has_active_component.md) |  |
| [has_active_ingredient](has_active_ingredient.md) | holds between a drug and a molecular entity in which the latter is a part of ... |
| [has_adverse_event](has_adverse_event.md) | An untoward medical occurrence in a patient or clinical investigation subject... |
| [has_affinity](has_affinity.md) | Set of measurements documenting the strength of chemical entity to gene or ge... |
| [has_attribute](has_attribute.md) | connects any entity to an attribute |
| [has_attribute_type](has_attribute_type.md) | connects an attribute to a class that describes it |
| [has_author](has_author.md) |  |
| [has_binary_relation](has_binary_relation.md) | Qualifies a value context with a mathematical binary relation |
| [has_biological_sequence](has_biological_sequence.md) | connects a genomic feature to its sequence |
| [has_biological_sex](has_biological_sex.md) | The biological sex of the entity regarding a case description from a phenopac... |
| [has_biomarker](has_biomarker.md) | holds between a disease or phenotypic feature and a measurable chemical entit... |
| [has_catalyst](has_catalyst.md) |  |
| [has_chemical_formula](has_chemical_formula.md) | description of chemical compound based on element symbols |
| [has_chemical_role](has_chemical_role.md) | A role is particular behaviour which a chemical entity may exhibit |
| [has_completed](has_completed.md) | holds between an entity and a process that the entity is capable of and has c... |
| [has_confidence_level](has_confidence_level.md) | connects an association to a qualitative term denoting the level of confidenc... |
| [has_confidence_score](has_confidence_score.md) | connects an association to a quantitative (numeric) value that can be interpr... |
| [has_constituent](has_constituent.md) | one or more molecular entities within a chemical mixture |
| [has_contraindication](has_contraindication.md) |  |
| [has_contributor](has_contributor.md) |  |
| [has_count](has_count.md) | number of things with a particular property |
| [has_dataset](has_dataset.md) | Links a dataset version to the underlying dataset that it is a version of |
| [has_decreased_amount](has_decreased_amount.md) | Holds between an entity and a component that is present at lower amount than ... |
| [has_device](has_device.md) | connects an entity to one or more (medical) devices |
| [has_distribution](has_distribution.md) | Links a dataset version to one of its dataset distributions (a specific repre... |
| [has_drug](has_drug.md) | connects an entity to one or more drugs |
| [has_editor](has_editor.md) |  |
| [has_evidence](has_evidence.md) | Connects an association to detailed information providing supporting evidence |
| [has_evidence_of_type](has_evidence_of_type.md) | Connects an association to an evidence type ontology term |
| [has_excipient](has_excipient.md) | holds between a drug and a molecular entities in which the latter is a part o... |
| [has_food_component](has_food_component.md) | holds between food and one or more chemical entities composing it, irrespecti... |
| [has_frameshift_variant](has_frameshift_variant.md) |  |
| [has_gene](has_gene.md) | connects an entity associated with one or more genes |
| [has_gene_or_gene_product](has_gene_or_gene_product.md) | connects an entity with one or more gene or gene products |
| [has_gene_product](has_gene_product.md) | holds between a gene and a transcribed and/or translated product generated fr... |
| [has_increased_amount](has_increased_amount.md) | Holds between an entity and a component that is present at higher amount than... |
| [has_input](has_input.md) | holds between a process and a continuant, where the continuant is an input in... |
| [has_manifestation](has_manifestation.md) |  |
| [has_member](has_member.md) | Defines a mereological relation between a collection and an item |
| [has_metabolite](has_metabolite.md) | holds between two molecular entities in which the second one is derived from ... |
| [has_missense_variant](has_missense_variant.md) |  |
| [has_mode_of_inheritance](has_mode_of_inheritance.md) | Relates a disease or phenotypic feature to its observed genetic segregation a... |
| [has_molecular_consequence](has_molecular_consequence.md) | connects a sequence variant to a class describing the molecular consequence |
| [has_nearby_variant](has_nearby_variant.md) |  |
| [has_negative_upstream_actor](has_negative_upstream_actor.md) |  |
| [has_negative_upstream_or_within_actor](has_negative_upstream_or_within_actor.md) |  |
| [has_non_coding_variant](has_non_coding_variant.md) |  |
| [has_nonsense_variant](has_nonsense_variant.md) |  |
| [has_not_completed](has_not_completed.md) | holds between an entity and a process that the entity is capable of, but has ... |
| [has_numeric_value](has_numeric_value.md) | connects a quantity value to a number |
| [has_nutrient](has_nutrient.md) | one or more nutrients which are growth factors for a living organism |
| [has_output](has_output.md) | holds between a process and a continuant, where the continuant is an output o... |
| [has_part](has_part.md) | holds between wholes and their parts (material entities or processes) |
| [has_participant](has_participant.md) | holds between a process and a continuant, where the continuant is somehow inv... |
| [has_percentage](has_percentage.md) | equivalent to has quotient multiplied by 100 |
| [has_phenotype](has_phenotype.md) | holds between a biological entity and a phenotype, where a phenotype is const... |
| [has_plasma_membrane_part](has_plasma_membrane_part.md) | Holds between a cell c and a protein complex or protein p if and only if that... |
| [has_positive_upstream_actor](has_positive_upstream_actor.md) |  |
| [has_positive_upstream_or_within_actor](has_positive_upstream_or_within_actor.md) |  |
| [has_preventative_intervention](has_preventative_intervention.md) |  |
| [has_procedure](has_procedure.md) | connects an entity to one or more (medical) procedures |
| [has_provider](has_provider.md) |  |
| [has_publisher](has_publisher.md) |  |
| [has_qualitative_value](has_qualitative_value.md) | connects an attribute to a value |
| [has_quantitative_value](has_quantitative_value.md) | connects an attribute to a value |
| [has_quotient](has_quotient.md) |  |
| [has_receptor](has_receptor.md) | An entity that interacts with an exposure stimulus during an exposure event |
| [has_route](has_route.md) | the process that results in the stressor coming into direct contact with the ... |
| [has_sequence_location](has_sequence_location.md) | holds between two nucleic acid entities when the subject can be localized in ... |
| [has_sequence_variant](has_sequence_variant.md) |  |
| [has_side_effect](has_side_effect.md) | An unintended, but predictable, secondary effect shown to be correlated with ... |
| [has_splice_site_variant](has_splice_site_variant.md) |  |
| [has_stressor](has_stressor.md) | An agent, stimulus, activity, or event that causes stress or tension on an or... |
| [has_study_results](has_study_results.md) | Connects an study to instances of its study result |
| [has_substrate](has_substrate.md) | Holds between a biochemical reaction or catalytic process and a chemical enti... |
| [has_supporting_studies](has_supporting_studies.md) | Studies that produced information used as evidence to generate the knowledge ... |
| [has_synonymous_variant](has_synonymous_variant.md) |  |
| [has_target](has_target.md) |  |
| [has_taxonomic_rank](has_taxonomic_rank.md) | The taxonomic rank (e |
| [has_topic](has_topic.md) | Connects a node to a vocabulary term or ontology class that describes some as... |
| [has_total](has_total.md) | total number of things in a particular reference set |
| [has_unit](has_unit.md) | connects a quantity value to a unit |
| [has_upstream_actor](has_upstream_actor.md) |  |
| [has_upstream_or_within_actor](has_upstream_or_within_actor.md) |  |
| [has_variant_part](has_variant_part.md) | holds between a nucleic acid entity and a nucleic acid entity that is a sub-c... |
| [has_zygosity](has_zygosity.md) | The zygosity characterising a genotype or nucleic acid entity at a particular... |
| [height](height.md) | Height of the channel in micrometers |
| [hgvs_nomenclature](hgvs_nomenclature.md) | HGVS syntax refers to the specific rules and conventions used by the Human Va... |
| [highest_FDA_approval_status](highest_FDA_approval_status.md) | Should be the highest level of FDA approval this chemical entity or device ha... |
| [homologous_to](homologous_to.md) | holds between two biological entities that have common evolutionary origin |
| [id](id.md) | A unique identifier for an entity |
| [impaired_functions](impaired_functions.md) | List of functions that are impaired or absent in the model system |
| [in_cell_population_with](in_cell_population_with.md) | holds between two genes or gene products that are expressed in the same cell ... |
| [in_clinical_trials_for](in_clinical_trials_for.md) | Holds between an intervention and a medical condition, and reports that a cli... |
| [in_complex_with](in_complex_with.md) | holds between two genes or gene products that are part of (or code for produc... |
| [in_linkage_disequilibrium_with](in_linkage_disequilibrium_with.md) | holds between two sequence variants, the presence of which are correlated in ... |
| [in_pathway_with](in_pathway_with.md) | holds between two genes or gene products that are part of in the same biologi... |
| [in_preclinical_trials_for](in_preclinical_trials_for.md) | Holds between an  substance, procedure, or activity and a medical condition, ... |
| [in_taxon](in_taxon.md) | connects an entity to its taxonomic classification |
| [in_taxon_label](in_taxon_label.md) | The human readable scientific name for the taxon of the entity |
| [increased_amount_of](increased_amount_of.md) |  |
| [increased_likelihood_associated_with](increased_likelihood_associated_with.md) |  |
| [increases_amount_or_activity_of](increases_amount_or_activity_of.md) | A grouping mixin to help with searching for all the predicates that increase ... |
| [increases_sensitivity_to](increases_sensitivity_to.md) | holds between two chemical entities or genes or gene products where the actio... |
| [indirectly_physically_interacts_with](indirectly_physically_interacts_with.md) | Holds between two entities that physically interact by way of one or more int... |
| [information_content](information_content.md) | Information content (IC) value for a term, primarily from Automats |
| [ingest_date](ingest_date.md) | The date on which a dataset version was ingested into the local knowledge gra... |
| [inheritance](inheritance.md) | Connects genetic inheritance to a disease or phenotypic feature, as a node pr... |
| [intact_confidence_value](intact_confidence_value.md) | A score defined by MI / IntAct that represents the degree of confidence in th... |
| [inter_laboratory_consistency](inter_laboratory_consistency.md) | Measure of consistency across different laboratories |
| [interacting_molecules_category](interacting_molecules_category.md) |  |
| [interaction_mechanisms](interaction_mechanisms.md) | Mechanisms of cell-cell interaction (paracrine, direct contact, mechanical) |
| [interacts_with](interacts_with.md) | holds between any two entities that directly or indirectly interact with each... |
| [interbase_coordinate](interbase_coordinate.md) | A position in interbase coordinates |
| [interface_type](interface_type.md) | Type of interface(s) present in the device |
| [iri](iri.md) | An IRI for an entity |
| [is_active_ingredient_of](is_active_ingredient_of.md) | holds between a molecular entity and a drug, in which the former is a part of... |
| [is_chemical_role_of](is_chemical_role_of.md) | Holds between a chemical role and a chemical entity that exhibits that role |
| [is_diagnosed_by](is_diagnosed_by.md) |  |
| [is_excipient_of](is_excipient_of.md) | holds between a molecular entity and a drug in which the former is a part of ... |
| [is_frameshift_variant_of](is_frameshift_variant_of.md) | holds between a sequence variant and a gene, such the sequence variant causes... |
| [is_input_of](is_input_of.md) |  |
| [is_metabolite](is_metabolite.md) | indicates whether a molecular entity is a metabolite |
| [is_metabolite_of](is_metabolite_of.md) | holds between two molecular entities in which the first one is derived from t... |
| [is_missense_variant_of](is_missense_variant_of.md) | holds between a gene  and a sequence variant, such the sequence variant resul... |
| [is_molecular_consequence_of](is_molecular_consequence_of.md) |  |
| [is_nearby_variant_of](is_nearby_variant_of.md) | holds between a sequence variant and a gene sequence that the variant is geno... |
| [is_non_coding_variant_of](is_non_coding_variant_of.md) | holds between a sequence variant and a gene, where the variant does not affec... |
| [is_nonsense_variant_of](is_nonsense_variant_of.md) | holds between a sequence variant and a gene, such the sequence variant result... |
| [is_output_of](is_output_of.md) |  |
| [is_sequence_variant_of](is_sequence_variant_of.md) | holds between a sequence variant and a nucleic acid entity |
| [is_side_effect_of](is_side_effect_of.md) |  |
| [is_splice_site_variant_of](is_splice_site_variant_of.md) | holds between a sequence variant and a gene, such the sequence variant is in ... |
| [is_substrate_of](is_substrate_of.md) |  |
| [is_supplement](is_supplement.md) | A boolean or categorical flag indicating that a chemical mixture is marketed,... |
| [is_synonymous_variant_of](is_synonymous_variant_of.md) | holds between a sequence variant and a gene, such the sequence variant is in ... |
| [is_toxic](is_toxic.md) | A boolean flag indicating whether a chemical entity is toxic under ordinary c... |
| [is_computed](is_computed.md) | Indicates whether the model is computed or derived from experimental data |
| [iso_abbreviation](iso_abbreviation.md) | Standard abbreviation for periodicals in the International Organization for S... |
| [issue](issue.md) | issue of a newspaper, a scientific journal or magazine for reference purpose |
| [journal](journal.md) | Journal or publication venue |
| [keywords](keywords.md) | keywords tagging a publication |
| [knowledge_level](knowledge_level.md) | Describes the level of knowledge expressed in a statement, based on the reaso... |
| [knowledge_source](knowledge_source.md) | An Information Resource from which the knowledge expressed in an Association ... |
| [lacks_part](lacks_part.md) | Holds between an entity and a component that is absent from it relative to a ... |
| [latitude](latitude.md) | latitude |
| [length](length.md) | Length of the channel in millimeters |
| [license](license.md) | A legal instrument under which the information content entity is made availab... |
| [life_stage](life_stage.md) | The developmental or life-cycle stage of the animal used in the model system ... |
| [likelihood_affected_by](likelihood_affected_by.md) |  |
| [likelihood_associated_with](likelihood_associated_with.md) |  |
| [ln_ratio](ln_ratio.md) | the natural log of the ratio of co-occurrence to expected |
| [ln_ratio_confidence_interval](ln_ratio_confidence_interval.md) | The 99% confidence interval for the ln_ratio calculation (i |
| [located_in](located_in.md) | holds between a material entity and a material entity or site within which it... |
| [location_of](location_of.md) | holds between material entity or site and a material entity that is located w... |
| [location_of_disease](location_of_disease.md) |  |
| [log_odds_ratio](log_odds_ratio.md) | The natural logarithm of the odds ratio (OR), or the ratio of the odds of an ... |
| [log_odds_ratio_95_ci](log_odds_ratio_95_ci.md) | The ninety-five percent confidence range in which the true log odds ratio for... |
| [logical_interpretation](logical_interpretation.md) |  |
| [logp](logp.md) | Lipophilicity (log P) |
| [longitude](longitude.md) | longitude |
| [manifestation_of](manifestation_of.md) | that part of a phenomenon which is directly observable or visibly expressed, ... |
| [mapped_predicate](mapped_predicate.md) | The predicate that is being replaced by the fully qualified representation of... |
| [material](material.md) | Materials used to construct the device |
| [matrix_composition](matrix_composition.md) | Composition of extracellular matrix or scaffold material |
| [max_research_phase](max_research_phase.md) | The maximum research phase reached for a specific chemical-disease pair, indi... |
| [max_tolerated_dose](max_tolerated_dose.md) | The highest dose of a drug or treatment that does not cause unacceptable side... |
| [max_response_ratio](max_response_ratio.md) | Ratio of maximum responses between systems |
| [mechanical_forces](mechanical_forces.md) | Mechanical forces applied to the model system |
| [mechanism_of_action](mechanism_of_action.md) | a boolean flag to indicate if the edge is part of a path or subgraph of a kno... |
| [member_of](member_of.md) | Defines a mereological relation between a item and a collection |
| [membrane_pore_size](membrane_pore_size.md) | Pore size of the membrane in micrometers |
| [membrane_thickness](membrane_thickness.md) | Thickness of the membrane in micrometers |
| [membrane_type](membrane_type.md) | Type of membrane used in the device if applicable |
| [mentioned_by](mentioned_by.md) | refers to is a relation between one named thing and the information content e... |
| [mentions](mentions.md) | refers to is a relation between one information content entity and the named ... |
| [mesh_terms](mesh_terms.md) | mesh terms tagging a publication |
| [methodology](methodology.md) | Description of experimental methods used for molecular comparison |
| [metric_name](metric_name.md) | Name of the quality control metric |
| [metric_value](metric_value.md) | Value of the quality control metric |
| [microfluidic_design](microfluidic_design.md) | Detailed design specifications of the microfluidic device |
| [missing_from](missing_from.md) |  |
| [missing_cell_types](missing_cell_types.md) | List of cell types present in biological system but missing in model |
| [ml_algorithm](ml_algorithm.md) | Type of machine learning algorithm used |
| [mode_of_inheritance_of](mode_of_inheritance_of.md) |  |
| [model_of](model_of.md) | holds between a thing and some other thing it approximates for purposes of sc... |
| [model_interpretability](model_interpretability.md) | Level of model interpretability (black box, interpretable, explainable) |
| [model_performance](model_performance.md) | Statistical performance metrics of the model |
| [model_proportion](model_proportion.md) | Proportion of this cell type in the model system |
| [model_specific_phenotypes](model_specific_phenotypes.md) | List of phenotypes present only in the model system |
| [model_systems](model_systems.md) |  |
| [models](models.md) |  |
| [models_demonstrating_benefits_for](models_demonstrating_benefits_for.md) |  |
| [molecular_descriptors](molecular_descriptors.md) | Types of molecular descriptors used (topological, electronic, etc |
| [molecular_similarity](molecular_similarity.md) |  |
| [molecular_weight](molecular_weight.md) | Molecular weight (g/mol) |
| [n_folds](n_folds.md) | Number of folds in cross-validation |
| [name](name.md) | A human-readable name for an attribute or entity |
| [narrow_match](narrow_match.md) | a list of terms from different schemas or terminology systems that have a nar... |
| [narrow_matches](narrow_matches.md) | A list of terms from different schemas or terminology systems that have a nar... |
| [narrow_synonym](narrow_synonym.md) | An alternate label for an entity whose meaning is narrower (more specific) th... |
| [negated](negated.md) | if set to true, then the association is negated i |
| [negatively_correlated_with](negatively_correlated_with.md) | A relationship that holds between two concepts represented by variables for w... |
| [node_property](node_property.md) | A grouping for any property that holds between a node and a value |
| [nodes](nodes.md) | A list of entities that can be a subject or object of an association |
| [not_completed_by](not_completed_by.md) |  |
| [number_of_cases](number_of_cases.md) | The number of cases in a study or clinical trial, primarily used in conversio... |
| [number_of_channels](number_of_channels.md) | Total number of channels in the device |
| [nutrient_of](nutrient_of.md) | holds between a one or more chemical entities present in food, irrespective o... |
| [object](object.md) | connects an association to the object of the association |
| [object_activity_qualifier](object_activity_qualifier.md) |  |
| [object_aspect_qualifier](object_aspect_qualifier.md) | Composes with the core concept to describe new concepts of a different ontolo... |
| [object_category](object_category.md) | Used to hold the biolink class/category of an association |
| [object_category_closure](object_category_closure.md) | Used to hold the object category closure of an association |
| [object_closure](object_closure.md) | Used to hold the object closure of an association |
| [object_context_qualifier](object_context_qualifier.md) | A qualifier describing the context in which the object of an association hold... |
| [object_derivative_qualifier](object_derivative_qualifier.md) | A qualifier that composes with a core subject/object  concept to describe som... |
| [object_direction_qualifier](object_direction_qualifier.md) | Composes with the core concept (+ aspect if provided) to describe a change in... |
| [object_feature_name](object_feature_name.md) | Used to describe a subordinate feature of the associated object for example, ... |
| [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) | A qualifier that composes with a core subject/object concept to define a spec... |
| [object_label_closure](object_label_closure.md) | Used to hold the object label closure of an association |
| [object_location_in_text](object_location_in_text.md) | Character offsets for the text span(s) in the supporting text corresponding t... |
| [object_namespace](object_namespace.md) | Used to hold the object namespace of an association |
| [object_part_qualifier](object_part_qualifier.md) | defines a specific part/component of the core concept (used in cases there th... |
| [object_process_qualifier](object_process_qualifier.md) |  |
| [object_specialization_qualifier](object_specialization_qualifier.md) | A qualifier that composes with a core subject/object concept to define a more... |
| [occurs_in](occurs_in.md) | holds between a process and a material entity or site within which the proces... |
| [occurs_in_disease](occurs_in_disease.md) |  |
| [occurs_together_in_literature_with](occurs_together_in_literature_with.md) | holds between two entities where their co-occurrence is correlated by counts ... |
| [onset_qualifier](onset_qualifier.md) | a qualifier used in a phenotypic association to state when the phenotype appe... |
| [opposite_of](opposite_of.md) | x is the opposite of y if there exists some distance metric M, and there exis... |
| [organ_modeled](organ_modeled.md) | The organ or tissue being modeled |
| [original_object](original_object.md) | used to hold the original object of a relation (or predicate) that an externa... |
| [original_predicate](original_predicate.md) | used to hold the original relation/predicate that an external knowledge sourc... |
| [original_subject](original_subject.md) | used to hold the original subject of a relation (or predicate) that an extern... |
| [orthologous_to](orthologous_to.md) | a homology relationship between entities (typically genes) that diverged afte... |
| [overlaps](overlaps.md) | holds between entities that overlap in their extents (materials or processes) |
| [p_value](p_value.md) | A quantitative confidence value that represents the probability of obtaining ... |
| [p_value](p_value.md) | Statistical p-value for differential expression |
| [pages](pages.md) | page number of source referenced for statement or publication |
| [paralogous_to](paralogous_to.md) | a homology relationship that holds between entities (typically genes) that di... |
| [part_of](part_of.md) | holds between parts and wholes (material entities or processes) |
| [part_qualifier](part_qualifier.md) | defines a specific part/component of the core concept (used in cases there th... |
| [participates_in](participates_in.md) | holds between a continuant and a process, where the continuant is somehow inv... |
| [partition_coefficient](partition_coefficient.md) | Tissue-to-plasma partition coefficient |
| [pass_fail_status](pass_fail_status.md) | Whether this metric passes quality control criteria |
| [passage_protocol](passage_protocol.md) | Standard passaging protocol and frequency |
| [passage_range](passage_range.md) | Recommended passage number range for experimental use |
| [pathway](pathway.md) | The pathway this measurement is about |
| [pathway_analysis_method](pathway_analysis_method.md) | Method used for pathway analysis (e |
| [pathway_concordance](pathway_concordance.md) |  |
| [pathway_overlap_score](pathway_overlap_score.md) | Quantitative score (0 |
| [perfusion_system](perfusion_system.md) | Description of perfusion and flow systems |
| [personalization_parameters](personalization_parameters.md) | Parameters used for personalization (genetic, phenotypic, etc |
| [perturbations](perturbations.md) | exposure/dose/time; diet/drugs/toxicants |
| [pharmacologically_interacts_with](pharmacologically_interacts_with.md) | holds between two pharmacologically active chemicals (typically drugs), where... |
| [phase](phase.md) | The phase for a coding sequence entity |
| [phenotype_of](phenotype_of.md) |  |
| [phenotype_ontology](phenotype_ontology.md) | Ontology used for phenotype classification (e |
| [phenotype_overlap](phenotype_overlap.md) |  |
| [phenotype_similarity_score](phenotype_similarity_score.md) | Quantitative score (0 |
| [phenotypic_state](phenotypic_state.md) | in experiments (e |
| [physically_interacts_with](physically_interacts_with.md) | holds between two entities that make physical contact as part of some interac... |
| [pka](pka.md) | Acid dissociation constant |
| [plan_comparators](plan_comparators.md) | human data, gold-standard assays, or high-quality animal references |
| [plasma_membrane_part_of](plasma_membrane_part_of.md) |  |
| [population_context_qualifier](population_context_qualifier.md) | a biological population (general, study, cohort, etc |
| [positively_correlated_with](positively_correlated_with.md) | A relationship that holds between two concepts represented by variables for w... |
| [preceded_by](preceded_by.md) | holds between two processes, where the other is completed before the one begi... |
| [precedes](precedes.md) | holds between two processes, where one completes before the other begins |
| [predicate](predicate.md) | Has a value from the Biolink 'related_to' hierarchy |
| [predicate_mappings](predicate_mappings.md) | A collection of relationships that are not used in biolink, but have biolink ... |
| [prediction_scope](prediction_scope.md) | Scope and limitations of model predictions |
| [predisposes_to_condition](predisposes_to_condition.md) | Holds between two entities where the presence or application of one increases... |
| [pressure_pascal](pressure_pascal.md) | Pressure applied in Pascals |
| [preventative_for_condition](preventative_for_condition.md) | Holds between a substance, procedure, or activity and a medical condition (di... |
| [primarily_composed_of](primarily_composed_of.md) |  |
| [primary_knowledge_source](primary_knowledge_source.md) | The most upstream source of the knowledge expressed in an Association that an... |
| [process_qualifier](process_qualifier.md) | Restricts the biological process within which the core concept (or qualified ... |
| [produced_by](produced_by.md) |  |
| [produces](produces.md) | holds between a material entity and a product that is generated through the i... |
| [promotes_condition](promotes_condition.md) | Holds between a substance, procedure, or activity and a medical condition (di... |
| [proportion_ratio](proportion_ratio.md) | Ratio of model to biological proportions |
| [protein_binding](protein_binding.md) | Fraction bound to plasma proteins (0 |
| [provided_by](provided_by.md) | The value in this node property represents the knowledge provider that create... |
| [provider](provider.md) | person, group, organization or project that provides a piece of information |
| [publication_type](publication_type.md) | Ontology term for publication type may be drawn from Dublin Core types (https... |
| [publications](publications.md) | One or more publications that report the statement expressed in an Associatio... |
| [published_in](published_in.md) | CURIE identifier of a broader publication context within which the publicatio... |
| [publisher](publisher.md) | organization or person responsible for publishing books, periodicals, podcast... |
| [q_value](q_value.md) | False discovery rate corrected p-value |
| [qualified_predicate](qualified_predicate.md) | Predicate to be used in an association when subject and object qualifiers are... |
| [qualifier](qualifier.md) | grouping slot for all qualifiers on an edge |
| [qualifiers](qualifiers.md) | connects an association to qualifiers that modify or qualify the meaning of t... |
| [quality_control_metrics](quality_control_metrics.md) | List of quality control measures and their values |
| [quantifier_qualifier](quantifier_qualifier.md) | A measurable quantity for the object of the association |
| [r_squared](r_squared.md) | R-squared value for regression models |
| [ratio](ratio.md) | Proportion or ratio of this cell type (0 |
| [ratio_type](ratio_type.md) | Type of ratio specification (percentage, absolute, fold) |
| [reaction_balanced](reaction_balanced.md) | Indicates whether a chemical reaction is stoichiometrically balanced, i |
| [reaction_direction](reaction_direction.md) | the direction of a reaction as constrained by the direction enum (ie: left_to... |
| [reaction_side](reaction_side.md) | the side of a reaction being modeled (ie: left or right) |
| [real_time_data_sources](real_time_data_sources.md) | Sources of real-time data for model updating |
| [reference_value](reference_value.md) | Reference or control value for comparison |
| [references](references.md) | Literature references that describe, validate, or support this model |
| [regulated_by](regulated_by.md) |  |
| [regulates](regulates.md) | A more specific form of affects, that implies the effect results from a biolo... |
| [related_condition](related_condition.md) | Links a genotype or genetic variant to a condition (disease or phenotypic fea... |
| [related_synonym](related_synonym.md) | An alternate label that is related to the primary label but is neither exactl... |
| [related_to](related_to.md) | A relationship that is asserted between two named things |
| [related_to_at_concept_level](related_to_at_concept_level.md) | Represents a relationship held between terminology components that describe t... |
| [related_to_at_instance_level](related_to_at_instance_level.md) | Represents a relationship held between two instances of a data classes |
| [relation](relation.md) |  |
| [relative_frequency_object](relative_frequency_object.md) | The frequency at which subject and object concepts co-occur in records within... |
| [relative_frequency_object_confidence_interval](relative_frequency_object_confidence_interval.md) | The 99% confidence interval for the relative_frequency_object calculation (i |
| [relative_frequency_subject](relative_frequency_subject.md) | The frequency at which subject and object concepts co-occur in records within... |
| [relative_frequency_subject_confidence_interval](relative_frequency_subject_confidence_interval.md) | The 99% confidence interval for the relative_frequency_subject calculation (i |
| [replicate_count](replicate_count.md) | Number of experimental replicates used in assessment |
| [represented_cell_types](represented_cell_types.md) | List of cell types present in both model and biological system |
| [reproducibility](reproducibility.md) |  |
| [reproducibility_score](reproducibility_score.md) | Quantitative score (0 |
| [resistance_associated_with](resistance_associated_with.md) |  |
| [resource_id](resource_id.md) | The CURIE for an Information Resource that served as a source of knowledge ex... |
| [resource_role](resource_role.md) | The role played by the InformationResource in serving as a source for an Edge |
| [response_associated_with](response_associated_with.md) |  |
| [response_context_qualifier](response_context_qualifier.md) | a biological response (general, study, cohort, etc |
| [response_target_context_qualifier](response_target_context_qualifier.md) | a biological response target (a patient, a cohort, a model system, a cell lin... |
| [retrieval_source_ids](retrieval_source_ids.md) | A list of retrieval sources that served as a source of knowledge expressed in... |
| [retrieved_on](retrieved_on.md) | The date on which a dataset was retrieved or harvested from its original sour... |
| [rights](rights.md) | A statement describing rights held in or over the information content entity,... |
| [rmse](rmse.md) | Root mean square error |
| [routes_of_delivery](routes_of_delivery.md) | the method or process of administering a pharmaceutical compound to achieve a... |
| [same_as](same_as.md) | holds between two entities that are considered equivalent to each other |
| [semmed_agreement_count](semmed_agreement_count.md) | The number of times this concept has been asserted in the SemMedDB literature... |
| [sensitivity](sensitivity.md) | Sensitivity/recall of the model (0 |
| [sensitivity_affected_by](sensitivity_affected_by.md) |  |
| [sensitivity_associated_with](sensitivity_associated_with.md) |  |
| [sensitivity_decreased_by](sensitivity_decreased_by.md) |  |
| [sensitivity_increased_by](sensitivity_increased_by.md) |  |
| [sensor_integration](sensor_integration.md) | Sensors integrated for real-time monitoring |
| [sensors_integrated](sensors_integrated.md) | Sensors integrated into the device for monitoring |
| [sequence_localization_attribute](sequence_localization_attribute.md) | An attribute that can be applied to a genome sequence localization edge |
| [sequence_location_of](sequence_location_of.md) |  |
| [sequence_variant_qualifier](sequence_variant_qualifier.md) | a qualifier used in an association with the variant |
| [severity_qualifier](severity_qualifier.md) | a qualifier used in a phenotypic association to state how severe the phenotyp... |
| [sex_qualifier](sex_qualifier.md) | a qualifier used in a phenotypic association to state whether the association... |
| [shared_phenotypes](shared_phenotypes.md) | List of phenotypes present in both model and biological system |
| [shear_stress](shear_stress.md) | Shear stress applied in dyn/cm² |
| [signor_confidence_score](signor_confidence_score.md) | A score defined by SIGNOR Lab Diseases that reports confidence level in a cur... |
| [similar_to](similar_to.md) | holds between an entity and some other entity with similar features |
| [similarity_score](similarity_score.md) | Quantitative similarity score (0 |
| [single_cell_method](single_cell_method.md) | Method used for single-cell analysis (e |
| [size_range](size_range.md) | Typical size range of 3D structures |
| [software_platform](software_platform.md) | Software platform or programming language used |
| [source_logo](source_logo.md) | A URL referencing an image that serves as the visual logo of a data source |
| [source_record_urls](source_record_urls.md) | A URL linking to a specific web page or document provided by the source, that... |
| [source_web_page](source_web_page.md) | A URL of a web page that documents or serves as the landing page for a data s... |
| [sources](sources.md) | A set of RetrievalSources, which traces where the statement expressed in an A... |
| [spatial_context](spatial_context.md) | Description of spatial organization and context captured by the model |
| [special_features](special_features.md) | Additional special features of the device (e |
| [specialization_qualifier](specialization_qualifier.md) | A qualifier that composes with a core subject/object concept to define a more... |
| [species](species.md) | The species of the animal used in the model system |
| [species_context_qualifier](species_context_qualifier.md) | A statement qualifier representing a taxonomic category of species in which a... |
| [species_modeled](species_modeled.md) | Species for which the model is designed |
| [specificity](specificity.md) | Specificity of the model (0 |
| [stage_qualifier](stage_qualifier.md) | stage during which gene or protein expression of takes place |
| [start_coordinate](start_coordinate.md) | The position at which the subject genomic entity starts on the chromosome or ... |
| [start_interbase_coordinate](start_interbase_coordinate.md) | The position at which the subject nucleic acid entity starts on the chromosom... |
| [statement_qualifier](statement_qualifier.md) | A property that qualifies the entirety of the statement made in an associatio... |
| [statistical_significance](statistical_significance.md) | Statistical measures of significance for the molecular similarity |
| [statistical_test](statistical_test.md) | Name of statistical test used |
| [stimulation_type](stimulation_type.md) | Type of mechanical stimulation applied |
| [stoichiometry](stoichiometry.md) | the relationship between the relative quantities of substances taking part in... |
| [strain](strain.md) | The specific strain of the animal used in the model system, as a strain-rank ... |
| [strand](strand.md) | The strand on which a feature is located |
| [structured_concordance](structured_concordance.md) | Detailed structured assessment of concordance between the model system and th... |
| [studied_to_treat](studied_to_treat.md) | Holds between an  substance, procedure, or activity and a medical condition, ... |
| [studies](studies.md) |  |
| [subclass_of](subclass_of.md) | holds between two classes where the domain class is a specialization of the r... |
| [subject](subject.md) | connects an association to the subject of the association |
| [subject_activity_qualifier](subject_activity_qualifier.md) |  |
| [subject_aspect_qualifier](subject_aspect_qualifier.md) | Composes with the core concept to describe new concepts of a different ontolo... |
| [subject_category](subject_category.md) | Used to hold the biolink class/category of an association |
| [subject_category_closure](subject_category_closure.md) | Used to hold the subject category closure of an association |
| [subject_closure](subject_closure.md) | Used to hold the subject closure of an association |
| [subject_context_qualifier](subject_context_qualifier.md) | A qualifier describing the context in which the subject of an association hol... |
| [subject_derivative_qualifier](subject_derivative_qualifier.md) | A qualifier that composes with a core subject/object  concept to describe som... |
| [subject_direction_qualifier](subject_direction_qualifier.md) | Composes with the core concept (+ aspect if provided) to describe a change in... |
| [subject_feature_name](subject_feature_name.md) | Used to describe a subordinate feature of the associated subject for example,... |
| [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | A qualifier that composes with a core subject/object concept to define a spec... |
| [subject_label_closure](subject_label_closure.md) | Used to hold the subject label closure of an association |
| [subject_location_in_text](subject_location_in_text.md) | Character offsets for the text span(s) in the supporting text corresponding t... |
| [subject_namespace](subject_namespace.md) | Used to hold the subject namespace of an association |
| [subject_of_treatment_application_or_study_for_treatment_by](subject_of_treatment_application_or_study_for_treatment_by.md) |  |
| [subject_part_qualifier](subject_part_qualifier.md) | defines a specific part/component of the core concept (used in cases there th... |
| [subject_process_qualifier](subject_process_qualifier.md) |  |
| [subject_specialization_qualifier](subject_specialization_qualifier.md) | A qualifier that composes with a core subject/object concept to define a more... |
| [subsets](subsets.md) | The set of ontology subsets a term belongs to (e |
| [substrate_type](substrate_type.md) | Type of culture substrate (e |
| [summary](summary.md) | executive  summary of a publication |
| [superclass_of](superclass_of.md) | holds between two classes where the domain class is a super class of the rang... |
| [support_graphs](support_graphs.md) | A list of knowledge graphs that support the existence of this association |
| [supporting_data_set](supporting_data_set.md) | A set of data used as evidence to generate the knowledge expressed in an Asso... |
| [supporting_data_source](supporting_data_source.md) | An Information Resource from which data was retrieved and subsequently used a... |
| [supporting_document_type](supporting_document_type.md) | The document type (e |
| [supporting_document_year](supporting_document_year.md) | The document year (typically the publication year) for the supporting documen... |
| [supporting_documents](supporting_documents.md) | One or more referenceable documents that report the statement expressed in an... |
| [supporting_study_cohort](supporting_study_cohort.md) | A description of a study population/cohort that was interrogated to provide e... |
| [supporting_study_context](supporting_study_context.md) | A term or terms describing the experimental setting/context in which evidence... |
| [supporting_study_date_range](supporting_study_date_range.md) | The date range over which data was collected in a study that provided evidenc... |
| [supporting_study_metadata](supporting_study_metadata.md) | Information about a study used to generate information used as evidence to su... |
| [supporting_study_method_description](supporting_study_method_description.md) | A uri or curie pointing to information about the methodology used to generate... |
| [supporting_study_method_types](supporting_study_method_types.md) | Type(s) of methods that were applied in a study used to generate the informat... |
| [supporting_study_size](supporting_study_size.md) | The sample size used in a study that provided evidence for the association (e |
| [supporting_text](supporting_text.md) | The segment of text from a document that supports the mined assertion |
| [supporting_text_section_type](supporting_text_section_type.md) | The section of the supporting text of a Text Mining Result within the support... |
| [surface_treatment](surface_treatment.md) | Surface treatments or coatings applied to the device |
| [symbol](symbol.md) | Symbol for a particular thing |
| [synonym](synonym.md) | Alternate human-readable names for a thing |
| [systematic_synonym](systematic_synonym.md) | more commonly used for gene symbols in yeast |
| [target_for](target_for.md) | A gene is a target of a disease when its products are druggable and when a dr... |
| [taxon](taxon.md) | A property that indicates the taxonomic classification of an entity |
| [taxon_of](taxon_of.md) |  |
| [temporal_context_qualifier](temporal_context_qualifier.md) | a constraint of time placed upon the truth value of an association |
| [temporal_interval_qualifier](temporal_interval_qualifier.md) | a constraint of a time interval placed upon the truth value of an association |
| [temporally_related_to](temporally_related_to.md) | holds between two entities with a temporal relationship |
| [tested_by_clinical_trials_of](tested_by_clinical_trials_of.md) |  |
| [tested_by_preclinical_trials_of](tested_by_preclinical_trials_of.md) |  |
| [three_d_architecture](three_d_architecture.md) | Type of 3D architecture (spheroid, organoid, scaffold-based, etc |
| [threshold](threshold.md) | Acceptable threshold for this metric |
| [timepoint](timepoint.md) | a point in time |
| [tissue_architecture](tissue_architecture.md) | Description of tissue-level architecture and organization |
| [title](title.md) | Title of the referenced publication or dataset |
| [total_sample_size](total_sample_size.md) | The total number of patients or participants within a sample population |
| [trade_name](trade_name.md) | A proprietary brand or trade name under which a chemical entity (typically a ... |
| [training_data_size](training_data_size.md) | Size of training dataset |
| [training_dataset_size](training_dataset_size.md) | Number of compounds in training dataset |
| [transcribed_from](transcribed_from.md) | x is transcribed from y if and only if x is synthesized from template y |
| [transcribed_to](transcribed_to.md) | inverse of transcribed from |
| [translates_to](translates_to.md) | x (amino acid chain/polypeptide) is the ribosomal translation of y (transcrip... |
| [translation_of](translation_of.md) | inverse of translates to |
| [treated_by](treated_by.md) |  |
| [treated_in_studies_by](treated_in_studies_by.md) |  |
| [treatment_applications_from](treatment_applications_from.md) |  |
| [treats](treats.md) | Holds between an intervention (substance, procedure, or activity) and a medic... |
| [treats_or_applied_or_studied_to_treat](treats_or_applied_or_studied_to_treat.md) | Holds between an substance, procedure, or activity and a medical condition (d... |
| [twin_scope](twin_scope.md) | Scope of digital twin (organ, patient, population) |
| [type](type.md) | An rdf:type property asserting that an entity is an instance of a particular ... |
| [units](units.md) | Units of measurement for the assay result |
| [update_date](update_date.md) | date on which an entity was updated |
| [update_frequency](update_frequency.md) | Frequency of model updates based on new data |
| [upstream_resource_ids](upstream_resource_ids.md) | An upstream InformationResource from which the resource being described direc... |
| [url](url.md) | This slot holds a string representation of a URL for an external resource abo... |
| [validation_datasets](validation_datasets.md) | Datasets used for model training and validation |
| [variant_part_of](variant_part_of.md) |  |
| [version](version.md) | A label identifying a particular release or edition of a dataset or resource,... |
| [version_of](version_of.md) | Links a dataset version to the dataset summary of which it is a version, edit... |
| [volume](volume.md) | volume of a book or music release in a collection/series or a published colle... |
| [was_tested_for_effect_of](was_tested_for_effect_of.md) |  |
| [was_tested_for_effect_on](was_tested_for_effect_on.md) | Reports that the subject was interrogated in an experiment to determine how i... |
| [width](width.md) | Width of the channel in micrometers |
| [xenologous_to](xenologous_to.md) | a homology relationship characterized by an interspecies (horizontal) transfe... |
| [xref](xref.md) | A database cross reference or alternative identifier for a NamedThing or edge... |
| [year](year.md) | Publication year |
| [z_score](z_score.md) | A measure of the divergence of an individual experimental result from the mos... |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AffinityParameterEnum](AffinityParameterEnum.md) | The types of parameters that can be used to describe the affinity between two... |
| [AgentTypeEnum](AgentTypeEnum.md) | An enumeration of agent types responsible for generating a statement of knowl... |
| [AnatomicalStructureEnum](AnatomicalStructureEnum.md) |  |
| [ApprovalStatusEnum](ApprovalStatusEnum.md) | An enumeration of regulatory and development milestones for a drug or therape... |
| [BinaryRelationEnum](BinaryRelationEnum.md) | Mathematical binary relation qualifiers of a value in its context |
| [BiologicalOrganizationLevelEnum](BiologicalOrganizationLevelEnum.md) |  |
| [CaseOrControlEnum](CaseOrControlEnum.md) |  |
| [CausalMechanismQualifierEnum](CausalMechanismQualifierEnum.md) | An enumeration used as a qualifier to specify the causal or pharmacologic mec... |
| [CellTypeEnum](CellTypeEnum.md) |  |
| [ChannelConfigurationEnum](ChannelConfigurationEnum.md) | Channel configurations for microfluidic devices aligned with ISO 22916:2022 i... |
| [ChemicalEntityDerivativeEnum](ChemicalEntityDerivativeEnum.md) | An enumeration of relationships by which one chemical entity is derived from ... |
| [ChemicalOrGeneOrGeneProductFormOrVariantEnum](ChemicalOrGeneOrGeneProductFormOrVariantEnum.md) | An enumeration used as a qualifier to indicate a specific form or variant of ... |
| [ClinicalApprovalStatusEnum](ClinicalApprovalStatusEnum.md) | An enumeration describing whether a chemical or therapy is approved for use i... |
| [ClinicalTrialAgeStageEnum](ClinicalTrialAgeStageEnum.md) | Enumeration of age stages or populations commonly used in clinical trials to ... |
| [ClinicalTrialStatusEnum](ClinicalTrialStatusEnum.md) | Enumeration of clinical trial statuses indicating the recruitment state, avai... |
| [CocultureConfigurationEnum](CocultureConfigurationEnum.md) |  |
| [ComplexityLevelEnum](ComplexityLevelEnum.md) |  |
| [CrossValidationMethodEnum](CrossValidationMethodEnum.md) |  |
| [DeviceMaterialEnum](DeviceMaterialEnum.md) |  |
| [DigitalTwinScopeEnum](DigitalTwinScopeEnum.md) |  |
| [DirectionQualifierEnum](DirectionQualifierEnum.md) | An enumeration of values that qualify a change or effect by its direction, i |
| [DrugAvailabilityEnum](DrugAvailabilityEnum.md) | An enumeration describing how a drug or chemical entity may be obtained, dist... |
| [DrugDeliveryEnum](DrugDeliveryEnum.md) | An enumeration of routes by which a drug is administered or delivered to a pa... |
| [DruggableGeneCategoryEnum](DruggableGeneCategoryEnum.md) | An enumeration of druggability categories for gene targets as defined by the ... |
| [FDAIDAAdverseEventEnum](FDAIDAAdverseEventEnum.md) | please consult with the FDA guidelines as proposed in this document: https://... |
| [FeatureTypeEnum](FeatureTypeEnum.md) |  |
| [FlowControlMethodEnum](FlowControlMethodEnum.md) | Flow control methods for microfluidic devices as defined in ISO 10991:2023 |
| [GeneOrGeneProductOrChemicalEntityAspectEnum](GeneOrGeneProductOrChemicalEntityAspectEnum.md) | An enumeration used as a qualifier to indicate the specific aspect of a gene,... |
| [GeneOrGeneProductOrChemicalPartQualifierEnum](GeneOrGeneProductOrChemicalPartQualifierEnum.md) | An enumeration used as a qualifier to indicate a particular structural or fun... |
| [GeneToDiseasePredicateEnum](GeneToDiseasePredicateEnum.md) | Enumeration of predicates permissible for use in gene to disease associations |
| [GeneToPhenotypicFeaturePredicateEnum](GeneToPhenotypicFeaturePredicateEnum.md) | Enumeration of predicates permissible for use in gene to phenotypic feature a... |
| [IntegratedSensorEnum](IntegratedSensorEnum.md) |  |
| [InterfaceTypeEnum](InterfaceTypeEnum.md) |  |
| [InterpretabilityLevelEnum](InterpretabilityLevelEnum.md) |  |
| [InvestigativeProtocolEnum](InvestigativeProtocolEnum.md) |  |
| [KnowledgeLevelEnum](KnowledgeLevelEnum.md) | An enumeration characterizing the type of knowledge expressed in a statement ... |
| [LifeStageEnum](LifeStageEnum.md) |  |
| [LogicalInterpretationEnum](LogicalInterpretationEnum.md) | An enumeration of logical interpretations that can be applied to a triple to ... |
| [MechanicalStimulationTypeEnum](MechanicalStimulationTypeEnum.md) |  |
| [MembraneTypeEnum](MembraneTypeEnum.md) |  |
| [MicrofluidicArchitectureEnum](MicrofluidicArchitectureEnum.md) | Architecture types for microfluidic devices as defined in ISO 10991:2023 |
| [MLAlgorithmEnum](MLAlgorithmEnum.md) |  |
| [OrganEnum](OrganEnum.md) |  |
| [PBPKCompartmentEnum](PBPKCompartmentEnum.md) |  |
| [PhaseEnum](PhaseEnum.md) | phase |
| [PhenotypeEnum](PhenotypeEnum.md) |  |
| [PredictionOutcomeEnum](PredictionOutcomeEnum.md) |  |
| [PresenceEnum](PresenceEnum.md) |  |
| [RatioTypeEnum](RatioTypeEnum.md) |  |
| [ReactionDirectionEnum](ReactionDirectionEnum.md) | An enumeration of possible directions for a biochemical reaction, indicating ... |
| [ReactionSideEnum](ReactionSideEnum.md) | An enumeration indicating on which side of a biochemical reaction a participa... |
| [RelativeTimeEnum](RelativeTimeEnum.md) |  |
| [ResearchPhaseEnum](ResearchPhaseEnum.md) | An enumeration of research phases describing the stage of investigation for a... |
| [ResourceRoleEnum](ResourceRoleEnum.md) | The role played by the information reource in serving as a source for an edge... |
| [ResponseEnum](ResponseEnum.md) | A response to a treatment or intervention |
| [ResponseTargetEnum](ResponseTargetEnum.md) | The target of a treatment or intervention |
| [SampleProcessingEnum](SampleProcessingEnum.md) |  |
| [SequenceEnum](SequenceEnum.md) | type of sequence |
| [SpeciesEnum](SpeciesEnum.md) |  |
| [StrandEnum](StrandEnum.md) | strand |
| [StudyDesignEnum](StudyDesignEnum.md) |  |
| [SurfaceCoatingEnum](SurfaceCoatingEnum.md) |  |
| [ThreeDArchitectureEnum](ThreeDArchitectureEnum.md) |  |


## Types

| Type | Description |
| --- | --- |
| [BiologicalSequence](BiologicalSequence.md) | A string of characters representing a biological macromolecule sequence, such... |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [ChemicalFormulaValue](ChemicalFormulaValue.md) | A type of string representing a chemical formula |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [FrequencyValue](FrequencyValue.md) | A quantity expressing the number of occurrences of a repeating event per unit... |
| [Integer](Integer.md) | An integer |
| [IriType](IriType.md) | An IRI |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [LabelType](LabelType.md) | A type of string that provides a human-readable name for an entity |
| [NarrativeText](NarrativeText.md) | A type of string that provides a human-readable description of something |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [PercentageFrequencyValue](PercentageFrequencyValue.md) | A frequency value expressed as a percentage (UO:0000187), i |
| [Quotient](Quotient.md) | A dimensionless value obtained by dividing one quantity by another of the sam... |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [SymbolType](SymbolType.md) | A type of string that is typically short, used as a human-readable label or s... |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [TimeType](TimeType.md) | A value representing a point in time, serialised as a lexical representation ... |
| [Unit](Unit.md) | A standard of measurement in which the magnitude of a physical quantity is ex... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [ModelOrganismDatabase](ModelOrganismDatabase.md) | Subset that is relevant for a typical Model Organism Database (MOD) |
| [Samples](Samples.md) | Sample/biosample datamodel |
| [Testing](Testing.md) | TBD |
| [TranslatorMinimal](TranslatorMinimal.md) | Minimum subset of translator work |
