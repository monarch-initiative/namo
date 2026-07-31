---
search:
  boost: 5.0
---

# Slot: equivalent_identifiers 


_A set of identifiers that are considered equivalent to the primary identifier of the entity. This attribute is used to represent a collection of identifiers that are considered equivalent to the primary identifier of an entity. These equivalent identifiers may come from different databases, ontologies, or naming conventions, but they all refer to the same underlying concept or entity. This attribute is particularly useful in data integration and interoperability scenarios, where it is important to recognize and link different representations of the same entity across various sources._



<div data-search-exclude markdown="1">



URI: [namo:equivalent_identifiers](https://w3id.org/monarch-initiative/namo/equivalent_identifiers)
Alias: equivalent_identifiers

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NamedThing](NamedThing.md) | a databased entity or concept/class |  no  |
| [NAMDataset](NAMDataset.md) |  |  no  |
| [NAMStudy](NAMStudy.md) | A study is a structured investigation or analysis, often involving the collec... |  no  |
| [ModelSystem](ModelSystem.md) |  |  no  |
| [AnimalModel](AnimalModel.md) |  |  no  |
| [NAMModel](NAMModel.md) | A New Approach Methodology (NAM) model, which is a type of model system that ... |  no  |
| [CellularSystem](CellularSystem.md) | Cell-based model systems that use living cells to model biological processes |  no  |
| [TwoDCellCulture](TwoDCellCulture.md) | Conventional monolayer cell cultures grown on flat surfaces |  no  |
| [ThreeDCellCulture](ThreeDCellCulture.md) | Three-dimensional cell culture systems including spheroids and organoids |  no  |
| [CoCulture](CoCulture.md) | Co-culture systems combining multiple cell types to mimic microenvironments a... |  no  |
| [Organoid](Organoid.md) | A 3D cell culture system that self-organizes to recapitulate key structural a... |  no  |
| [CellLineModel](CellLineModel.md) | A model system based on immortalized cell lines that can be maintained in cul... |  no  |
| [MicrophysiologicalSystem](MicrophysiologicalSystem.md) | Organ-/tissue-on-chip systems that integrate microfluidics, biomaterials, and... |  no  |
| [OrganOnChip](OrganOnChip.md) | A model system that simulates the physiological functions of an organ using a... |  no  |
| [TissueOnChip](TissueOnChip.md) | Tissue-level microphysiological systems that model specific tissue functions ... |  no  |
| [InSilicoModel](InSilicoModel.md) | Computational models that simulate biological processes without physical biol... |  no  |
| [QSARModel](QSARModel.md) | Quantitative Structure-Activity Relationship models that predict chemical/bio... |  no  |
| [PBPKModel](PBPKModel.md) | Physiologically Based Pharmacokinetic models that simulate drug absorption, d... |  no  |
| [DigitalTwin](DigitalTwin.md) | Computational replicas of biological systems for real-time prediction and per... |  no  |
| [MLModel](MLModel.md) | Machine Learning and AI-based models for prediction, mechanism inference, and... |  no  |
| [MetabolicModel](MetabolicModel.md) | A model that simulates the metabolic processes of an organism or system |  no  |
| [PBPKCompartment](PBPKCompartment.md) | A physiological compartment in a PBPK model |  no  |
| [MicrofluidicDesign](MicrofluidicDesign.md) | Detailed specification of a microfluidic device design including its architec... |  no  |
| [MechanicalStimulation](MechanicalStimulation.md) | Specification of mechanical forces applied to the model system |  no  |
| [BiologicalSystem](BiologicalSystem.md) |  |  no  |
| [MolecularSimilarity](MolecularSimilarity.md) | Detailed assessment of molecular-level concordance between model and biologic... |  no  |
| [PathwayConcordance](PathwayConcordance.md) | Assessment of biological pathway conservation and activity between model and ... |  no  |
| [PhenotypeOverlap](PhenotypeOverlap.md) | Comparison of phenotypic manifestations between model and biological systems |  no  |
| [CellTypeCoverage](CellTypeCoverage.md) | Assessment of cell type representation and cellular diversity between systems |  no  |
| [FunctionalParity](FunctionalParity.md) | Evaluation of functional capabilities and physiological responses between sys... |  no  |
| [Reproducibility](Reproducibility.md) | Assessment of experimental reproducibility and consistency of the model syste... |  no  |
| [GeneExpressionResult](GeneExpressionResult.md) | A differential-expression measurement for a single gene in a model system |  no  |
| [PathwayActivityResult](PathwayActivityResult.md) | An activity and enrichment measurement for a single biological pathway |  no  |
| [FunctionalAssay](FunctionalAssay.md) | A functional assay used to assess biological capabilities |  no  |
| [Attribute](Attribute.md) | A property or characteristic of an entity |  no  |
| [ChemicalRole](ChemicalRole.md) | A role played by the molecular entity or part thereof within a chemical conte... |  no  |
| [BiologicalSex](BiologicalSex.md) | An organismal quality inhering in a bearer by virtue of the bearer's ability ... |  no  |
| [PhenotypicSex](PhenotypicSex.md) | An attribute corresponding to the phenotypic sex of the individual, based upo... |  no  |
| [GenotypicSex](GenotypicSex.md) | An attribute corresponding to the genotypic sex of the individual, based upon... |  no  |
| [SeverityValue](SeverityValue.md) | describes the severity of a phenotypic feature or disease |  no  |
| [OrganismTaxon](OrganismTaxon.md) | A classification of a set of organisms |  no  |
| [Event](Event.md) | Something that happens at a given place and time |  no  |
| [AdministrativeEntity](AdministrativeEntity.md) | An entity that is the byproduct of an administrative process |  no  |
| [StudyResult](StudyResult.md) | A collection of data items from a study that are about a particular study sub... |  no  |
| [ConceptCountAnalysisResult](ConceptCountAnalysisResult.md) | A result of a concept count analysis |  no  |
| [ObservedExpectedFrequencyAnalysisResult](ObservedExpectedFrequencyAnalysisResult.md) | A result of a observed expected frequency analysis |  no  |
| [RelativeFrequencyAnalysisResult](RelativeFrequencyAnalysisResult.md) | A result of a relative frequency analysis |  no  |
| [ChiSquaredAnalysisResult](ChiSquaredAnalysisResult.md) | A result of a chi squared analysis |  no  |
| [LogOddsAnalysisResult](LogOddsAnalysisResult.md) | A result of a log odds ratio analysis |  no  |
| [TextMiningStudyResult](TextMiningStudyResult.md) | A study result that represents information extracted from text using natural ... |  no  |
| [IceesStudyResult](IceesStudyResult.md) | A study result that represents a result, from a supporting Study, which is sp... |  no  |
| [Study](Study.md) | a detailed investigation and/or analysis |  no  |
| [StudyVariable](StudyVariable.md) | a variable that is used as a measure in the investigation of a study |  no  |
| [CommonDataElement](CommonDataElement.md) | A Common Data Element (CDE) is a standardized, precisely defined question, pa... |  no  |
| [Agent](Agent.md) | person, group, organization or project that provides a piece of information (... |  no  |
| [InformationContentEntity](InformationContentEntity.md) | a piece of information that typically describes some topic of discourse or is... |  no  |
| [Dataset](Dataset.md) | an item that refers to a collection of data from a data source |  no  |
| [DatasetDistribution](DatasetDistribution.md) | an item that holds distribution level information about a dataset |  no  |
| [DatasetVersion](DatasetVersion.md) | an item that holds version level information about a dataset |  no  |
| [DatasetSummary](DatasetSummary.md) | an item that holds summary level information about a dataset |  no  |
| [ConfidenceLevel](ConfidenceLevel.md) | Level of confidence in a statement |  no  |
| [EvidenceType](EvidenceType.md) | Class of evidence that supports an association |  no  |
| [Evidence](Evidence.md) | Dereferences detailed evidence that supports an association |  no  |
| [Publication](Publication.md) | Any ‘published’ piece of information |  no  |
| [Book](Book.md) | This class may rarely be instantiated except if use cases of a given knowledg... |  no  |
| [BookChapter](BookChapter.md) | A section of a book that forms a discrete unit of a larger published work and... |  no  |
| [Serial](Serial.md) | This class may rarely be instantiated except if use cases of a given knowledg... |  no  |
| [Article](Article.md) | a piece of writing on a particular topic presented as a stand-alone section o... |  no  |
| [JournalArticle](JournalArticle.md) | an article, typically presenting results of research, that is published in an... |  no  |
| [Patent](Patent.md) | a legal document granted by a patent issuing authority which confers upon the... |  no  |
| [WebPage](WebPage.md) | a document that is published according to World Wide Web standards, which may... |  no  |
| [PreprintPublication](PreprintPublication.md) | a document reresenting an early version of an author's original scholarly wor... |  no  |
| [DrugLabel](DrugLabel.md) | a document accompanying a drug or its container that provides written, printe... |  no  |
| [RetrievalSource](RetrievalSource.md) | Provides information about how a particular InformationResource served as a s... |  no  |
| [PhysicalEntity](PhysicalEntity.md) | An entity that has material reality (a |  no  |
| [Activity](Activity.md) | An activity is something that occurs over a period of time and acts upon or w... |  no  |
| [Procedure](Procedure.md) | A series of actions conducted in a certain order or manner |  no  |
| [Phenomenon](Phenomenon.md) | a fact or situation that is observed to exist or happen, especially one whose... |  no  |
| [Device](Device.md) | A thing made or adapted for a particular purpose, especially a piece of mecha... |  no  |
| [DiagnosticAid](DiagnosticAid.md) | A device or substance used to help diagnose disease or injury |  no  |
| [StudyPopulation](StudyPopulation.md) | A group of people banded together or treated as a group as participants in a ... |  no  |
| [MaterialSample](MaterialSample.md) | A sample is a limited quantity of something (e |  no  |
| [PlanetaryEntity](PlanetaryEntity.md) | Any entity or process that exists at the level of the whole planet |  no  |
| [EnvironmentalProcess](EnvironmentalProcess.md) | A process that occurs within or involves the components of an environmental s... |  no  |
| [EnvironmentalFeature](EnvironmentalFeature.md) | A system or entity in the natural environment that has the disposition to env... |  no  |
| [GeographicLocation](GeographicLocation.md) | a location that can be described in lat/long coordinates |  no  |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | a location that can be described in lat/long coordinates, for a particular ti... |  no  |
| [BiologicalEntity](BiologicalEntity.md) | A heterogeneous substance that contains genomic material or is the product of... |  no  |
| [MolecularEntity](MolecularEntity.md) | A molecular entity is a chemical entity composed of individual or covalently ... |  no  |
| [ChemicalEntity](ChemicalEntity.md) | A chemical entity is a physical entity that pertains to chemistry or biochemi... |  no  |
| [AffinityMeasurement](AffinityMeasurement.md) | The type of measurement describing the strength of an affinity between two en... |  no  |
| [SmallMolecule](SmallMolecule.md) | A small molecule entity is a molecular entity characterized by availability i... |  no  |
| [ChemicalMixture](ChemicalMixture.md) | A chemical mixture is a chemical entity composed of two or more molecular ent... |  no  |
| [NucleicAcidEntity](NucleicAcidEntity.md) | A nucleic acid entity is a molecular entity characterized by availability in ... |  no  |
| [RegulatoryRegion](RegulatoryRegion.md) | A region (or regions) of the genome that contains known or putative regulator... |  no  |
| [AccessibleDnaRegion](AccessibleDnaRegion.md) | A region (or regions) of a chromatinized genome that has been measured to be ... |  no  |
| [TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) | A region (or regions) of the genome that contains a region of DNA known or pr... |  no  |
| [MolecularMixture](MolecularMixture.md) | A molecular mixture is a chemical mixture composed of two or more molecular e... |  no  |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | A complex molecular mixture is a chemical mixture composed of two or more mol... |  no  |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | Either an individual molecular activity, or a collection of causally connecte... |  no  |
| [MolecularActivity](MolecularActivity.md) | An execution of a molecular function carried out by a gene product or macromo... |  no  |
| [BiologicalProcess](BiologicalProcess.md) | One or more causally connected executions of molecular functions |  no  |
| [Pathway](Pathway.md) | A hierarchical ordering of connected molecular reactions (steps) that represe... |  no  |
| [PhysiologicalProcess](PhysiologicalProcess.md) | A biological or chemical function within a living organism |  no  |
| [Behavior](Behavior.md) | The internally coordinated responses (actions or inactions) of organisms (ind... |  no  |
| [ProcessedMaterial](ProcessedMaterial.md) | A chemical entity (often a mixture) processed for consumption for nutritional... |  no  |
| [Drug](Drug.md) | A substance intended for use in the diagnosis, cure, mitigation, treatment, o... |  no  |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | Any unwanted chemical in food |  no  |
| [FoodAdditive](FoodAdditive.md) | Any substance which is added to food to preserve or enhance its flavour and/o... |  no  |
| [Food](Food.md) | A substance of plant, animal, or artificial origin consumed by a living organ... |  no  |
| [OrganismAttribute](OrganismAttribute.md) | describes a characteristic of an organismal entity |  no  |
| [PhenotypicQuality](PhenotypicQuality.md) | A characteristic of a phenotype (e |  no  |
| [GeneticInheritance](GeneticInheritance.md) | The pattern or 'mode' in which a particular genetic trait or disorder is pass... |  no  |
| [OrganismalEntity](OrganismalEntity.md) | A named entity that is either a part of an organism, a whole organism, popula... |  no  |
| [Bacterium](Bacterium.md) | A member of a group of unicellular microorganisms lacking a nuclear membrane,... |  no  |
| [Virus](Virus.md) | A virus is a microorganism that replicates itself as a microRNA and infects t... |  no  |
| [CellularOrganism](CellularOrganism.md) | An organism that contains one or more cells belonging to the cellular lineage... |  no  |
| [Mammal](Mammal.md) |  |  no  |
| [Human](Human.md) |  |  no  |
| [Plant](Plant.md) |  |  no  |
| [Invertebrate](Invertebrate.md) |  |  no  |
| [Vertebrate](Vertebrate.md) |  |  no  |
| [Fungus](Fungus.md) |  |  no  |
| [LifeStage](LifeStage.md) | A stage of development or growth of an organism, including post-natal adult s... |  no  |
| [IndividualOrganism](IndividualOrganism.md) | An instance of an organism |  no  |
| [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | A collection of individuals from the same taxonomic class distinguished by on... |  no  |
| [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | A disease or an individual phenotypic feature, grouped as a single class to a... |  no  |
| [Disease](Disease.md) | A disease is a disposition to undergo pathological processes that exists in a... |  no  |
| [PhenotypicFeature](PhenotypicFeature.md) | A combination of entity and quality that makes up a phenotyping statement |  no  |
| [BehavioralFeature](BehavioralFeature.md) | A phenotypic feature which is behavioral in nature |  no  |
| [AnatomicalEntity](AnatomicalEntity.md) | A part of a cellular organism at or above the granularity of a protein comple... |  no  |
| [CellularComponent](CellularComponent.md) | A location in or around a cell |  no  |
| [Cell](Cell.md) | The basic structural and functional unit of all organisms |  no  |
| [CellLine](CellLine.md) | A cultured cell population that is genetically stable and homogeneous, sharin... |  no  |
| [GrossAnatomicalStructure](GrossAnatomicalStructure.md) | An anatomical structure that has more than one cell as a part |  no  |
| [Gene](Gene.md) | A region (or regions) that includes all of the sequence elements necessary to... |  no  |
| [MacromolecularComplex](MacromolecularComplex.md) | A stable assembly of two or more macromolecules, i |  no  |
| [NucleosomeModification](NucleosomeModification.md) | A chemical modification of a histone protein within a nucleosome octomer or a... |  no  |
| [Genome](Genome.md) | A genome is the sum of genetic material within a cell or virion |  no  |
| [Exon](Exon.md) | A region of the transcript sequence within a gene which is not removed from t... |  no  |
| [Transcript](Transcript.md) | An RNA synthesized on a DNA or RNA template by an RNA polymerase |  no  |
| [CodingSequence](CodingSequence.md) | A contiguous sequence which begins with, and includes, a start codon and ends... |  no  |
| [Polypeptide](Polypeptide.md) | A polypeptide is a molecular entity characterized by availability in protein ... |  no  |
| [Protein](Protein.md) | A gene product that is composed of a chain of amino acid sequences and is pro... |  no  |
| [ProteinIsoform](ProteinIsoform.md) | Represents a protein that is a specific isoform of the canonical or reference... |  no  |
| [ProteinDomain](ProteinDomain.md) | A conserved part of protein sequence and (tertiary) structure that can evolve... |  no  |
| [PosttranslationalModification](PosttranslationalModification.md) | A chemical modification of a polypeptide or protein that occurs after transla... |  no  |
| [ProteinFamily](ProteinFamily.md) | A set of proteins coding for diverse functions which, by virtue of their high... |  no  |
| [NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md) | A linear nucleotide sequence pattern that is widespread and has, or is conjec... |  no  |
| [RNAProduct](RNAProduct.md) | High molecular weight, linear polymers, composed of nucleotides containing ri... |  no  |
| [RNAProductIsoform](RNAProductIsoform.md) | Represents a protein that is a specific isoform of the canonical or reference... |  no  |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | An RNA transcript that does not encode for a protein rather the RNA molecule ... |  no  |
| [MicroRNA](MicroRNA.md) | A small (~22 nucleotide) RNA molecule that is the endogenous transcript of a ... |  no  |
| [SiRNA](SiRNA.md) | A small RNA molecule that is the product of a longer exogenous or endogenous ... |  no  |
| [GeneFamily](GeneFamily.md) | any grouping of multiple genes or gene products related by common descent |  no  |
| [Zygosity](Zygosity.md) | An allelic state describing the degree of similarity between features at a si... |  no  |
| [Genotype](Genotype.md) | An information content entity that describes a genome by specifying the total... |  no  |
| [Haplotype](Haplotype.md) | A set of zero or more Alleles on a single instance of a Sequence[VMC] |  no  |
| [SequenceVariant](SequenceVariant.md) | A sequence_variant is a non exact copy of a sequence_feature or genome exhibi... |  no  |
| [Snv](Snv.md) | SNVs are single nucleotide positions in genomic DNA at which different sequen... |  no  |
| [ReagentTargetedGene](ReagentTargetedGene.md) | A gene altered in its expression level in the context of some experiment as a... |  no  |
| [ClinicalAttribute](ClinicalAttribute.md) | Attributes relating to a clinical manifestation |  no  |
| [ClinicalMeasurement](ClinicalMeasurement.md) | A clinical measurement is a special kind of attribute which results from a la... |  no  |
| [ClinicalModifier](ClinicalModifier.md) | Used to characterize and specify the phenotypic abnormalities defined in the ... |  no  |
| [ClinicalCourse](ClinicalCourse.md) | The course a disease typically takes from its onset, progression in time, and... |  no  |
| [Onset](Onset.md) | The age group in which (disease) symptom manifestations appear |  no  |
| [ClinicalEntity](ClinicalEntity.md) | Any entity or process that exists in the clinical domain and outside the biol... |  no  |
| [ClinicalTrial](ClinicalTrial.md) | A clinical trial is a research study that prospectively assigns human partici... |  no  |
| [ClinicalIntervention](ClinicalIntervention.md) | A medical procedure, treatment, or action taken by healthcare professionals t... |  no  |
| [ClinicalFinding](ClinicalFinding.md) | this category is currently considered broad enough to tag clinical lab measur... |  no  |
| [Hospitalization](Hospitalization.md) | The admission and care of a patient in a hospital for observation, diagnosis,... |  no  |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | Attributes relating to a socioeconomic manifestation |  no  |
| [Case](Case.md) | An individual (human) organism that has a patient role in some clinical conte... |  no  |
| [Cohort](Cohort.md) | A group of people banded together or treated as a group who share common char... |  no  |
| [ExposureEvent](ExposureEvent.md) | A (possibly time bounded) incidence of a feature of the environment of an org... |  no  |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | A genomic background exposure is where an individual's specific genomic backg... |  no  |
| [PathologicalProcess](PathologicalProcess.md) | A biologic function or a process having an abnormal or deleterious effect at ... |  no  |
| [PathologicalProcessExposure](PathologicalProcessExposure.md) | A pathological process, when viewed as an exposure, representing a preconditi... |  no  |
| [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | An anatomical structure with the potential of have an abnormal or deleterious... |  no  |
| [PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) | An abnormal anatomical structure, when viewed as an exposure, represented as ... |  no  |
| [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | A disease or phenotypic feature state, when viewed as an exposure, represente... |  no  |
| [ChemicalExposure](ChemicalExposure.md) | A chemical exposure is an intake of a particular chemical entity |  no  |
| [ComplexChemicalExposure](ComplexChemicalExposure.md) | A complex chemical exposure is an intake of a chemical mixture, other than a ... |  no  |
| [DrugExposure](DrugExposure.md) | A drug exposure is an intake of a particular drug |  no  |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | drug to gene interaction exposure is a drug exposure is where the interaction... |  no  |
| [Treatment](Treatment.md) | A treatment is targeted at a disease or phenotype and may involve multiple dr... |  no  |
| [BioticExposure](BioticExposure.md) | An external biotic exposure is an intake of (sometimes pathological) biologic... |  no  |
| [GeographicExposure](GeographicExposure.md) | A geographic exposure is a factor relating to geographic proximity to some im... |  no  |
| [EnvironmentalExposure](EnvironmentalExposure.md) | A environmental exposure is a factor relating to abiotic processes in the env... |  no  |
| [BehavioralExposure](BehavioralExposure.md) | A behavioral exposure is a factor relating to behavior impacting an individua... |  no  |
| [SocioeconomicExposure](SocioeconomicExposure.md) | A socioeconomic exposure is a factor relating to social and financial status ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [NamedThing](NamedThing.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |








## See Also

* [biolink:xref](https://w3id.org/biolink/vocab/xref)
* [biolink:synonyms](https://w3id.org/biolink/vocab/synonyms)



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:equivalent_identifiers |
| native | namo:equivalent_identifiers |




## LinkML Source

<details>
```yaml
name: equivalent identifiers
description: A set of identifiers that are considered equivalent to the primary identifier
  of the entity. This attribute is used to represent a collection of identifiers that
  are considered equivalent to the primary identifier of an entity. These equivalent
  identifiers may come from different databases, ontologies, or naming conventions,
  but they all refer to the same underlying concept or entity. This attribute is particularly
  useful in data integration and interoperability scenarios, where it is important
  to recognize and link different representations of the same entity across various
  sources.
from_schema: https://w3id.org/monarch-initiative/namo
see_also:
- biolink:xref
- biolink:synonyms
rank: 1000
alias: equivalent_identifiers
domain_of:
- named thing
range: uriorcurie
multivalued: true

```
</details></div>