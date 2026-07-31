---
search:
  boost: 5.0
---

# Slot: object 


_connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._



<div data-search-exclude markdown="1">



URI: [rdf:object](http://www.w3.org/1999/02/22-rdf-syntax-ns#object)

## Inheritance

* [association_slot](association_slot.md)
    * **object**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Association](Association.md) | A typed association between two entities, supported by evidence |  no  |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | parent class for different kinds of gene-gene or gene product to gene product... |  yes  |
| [CellLineToEntityAssociationMixin](CellLineToEntityAssociationMixin.md) | An relationship between a cell line and another entity |  no  |
| [ChemicalEntityToEntityAssociationMixin](ChemicalEntityToEntityAssociationMixin.md) | An interaction between a chemical entity and another entity |  no  |
| [DrugToEntityAssociationMixin](DrugToEntityAssociationMixin.md) | An interaction between a drug and another entity |  no  |
| [ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md) | An interaction between a chemical entity and another entity |  no  |
| [CaseToEntityAssociationMixin](CaseToEntityAssociationMixin.md) | An abstract association for use where the case is the subject |  no  |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | A relationship between two chemical entities |  yes  |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | An association in which the subject entity is linked to the likelihood of the... |  no  |
| [MaterialSampleToEntityAssociationMixin](MaterialSampleToEntityAssociationMixin.md) | An association between a material sample and something |  no  |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | An association between a material sample and the material entity from which i... |  yes  |
| [DiseaseToEntityAssociationMixin](DiseaseToEntityAssociationMixin.md) | A mixin applied to any association whose subject (source node) is a disease |  no  |
| [EntityToExposureEventAssociationMixin](EntityToExposureEventAssociationMixin.md) | An association between some entity and an exposure event |  yes  |
| [EntityToOutcomeAssociationMixin](EntityToOutcomeAssociationMixin.md) | An association between some entity and an outcome |  yes  |
| [FrequencyQualifierMixin](FrequencyQualifierMixin.md) | Qualifier for frequency type associations |  no  |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | A mixin applied to any association whose object (target node) is a phenotypic... |  yes  |
| [DiseaseOrPhenotypicFeatureToEntityAssociationMixin](DiseaseOrPhenotypicFeatureToEntityAssociationMixin.md) |  |  no  |
| [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md) |  |  yes  |
| [GenotypeToEntityAssociationMixin](GenotypeToEntityAssociationMixin.md) |  |  no  |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | An association between a Case (patient) and a Disease |  yes  |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | Association between a Case and a Genetic Variant |  yes  |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | Association between a Case and a Gene (e |  yes  |
| [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md) |  |  no  |
| [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md) |  |  no  |
| [ModelToDiseaseAssociationMixin](ModelToDiseaseAssociationMixin.md) | This mixin is used for any association class for which the subject (source no... |  no  |
| [MacromolecularMachineToEntityAssociationMixin](MacromolecularMachineToEntityAssociationMixin.md) | an association which has a macromolecular machine mixin as a subject |  no  |
| [OrganismTaxonToEntityAssociation](OrganismTaxonToEntityAssociation.md) | An association between an organism taxon and another entity |  no  |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | A statistical association between a disease and a chemical entity where the c... |  yes  |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) |  |  yes  |
| [ContributorAssociation](ContributorAssociation.md) | Any association between an entity (such as a publication) and various agents ... |  yes  |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | Any association between one genotype and a genotypic entity that is a sub-com... |  yes  |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | Any association between a genotype and a gene |  yes  |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | Any association between a genotype and a sequence variant |  yes  |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | A homology association between two genes |  yes  |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | Set membership of a gene in a family of genes related by common evolutionary ... |  yes  |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | Relationship between a gene family and a contained gene or gene product or ge... |  yes  |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | Relationship between a gene or gene product or gene family to a specified bio... |  yes  |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | Relationship between a biological processor activity (e |  yes  |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | Classification relationship between biological processes or activities (e |  yes  |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | Indicates that two genes are co-expressed, generally under the same condition... |  no  |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | An interaction between two genes or two gene products |  no  |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | An interaction at the molecular level between two physical entities |  yes  |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | An relationship between a cell line and a disease or a phenotype, where the c... |  no  |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | An association between a biochemical reaction and a participating molecular e... |  no  |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | A specialization of reaction-to-participant association in which the particip... |  yes  |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | A causal relationship between two chemical entities, where the subject repres... |  yes  |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | An interaction between a chemical entity and a phenotype or disease, where th... |  yes  |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  no  |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  no  |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  no  |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | An interaction between a gene or gene product and a biological process or pat... |  yes  |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | Association that holds the relationship between a reaction and the pathway it... |  yes  |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | An interaction between a chemical entity and a biological process or pathway |  yes  |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | An association between a chemical entity and a biological process, where the ... |  yes  |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | describes an interaction between a chemical entity and a gene or gene product |  yes  |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | Describes the relationship between an enzyme (usually a macromolecular comple... |  yes  |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | Describes a regulatory relationship between two genes or gene products |  yes  |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | Describes a regulatory relationship between two genes or gene products |  yes  |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | Describes an effect that a chemical has on a biological entity (e |  yes  |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |  no  |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | Describes a relationship in which a chemical entity affects the sensitivity o... |  yes  |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | Describes an effect that a gene or gene product has on a chemical entity (e |  yes  |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | An interaction between a drug and a gene or gene product |  yes  |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | An association between a material sample and a disease or phenotype |  no  |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | An association between an exposure event and a disease |  no  |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | An association between an exposure event and an outcome |  no  |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | Qualifiers for entity to disease or phenotype associations |  no  |
| [EntityToFeatureOrVariantQualifiersMixin](EntityToFeatureOrVariantQualifiersMixin.md) | Qualifiers for entity to variant associations |  no  |
| [EntityToFeatureOrGeneQualifiersMixin](EntityToFeatureOrGeneQualifiersMixin.md) | Qualifiers for entity to gene associations |  no  |
| [FeatureOrDiseaseQualifiersToEntityMixin](FeatureOrDiseaseQualifiersToEntityMixin.md) | Qualifiers for disease or phenotype to entity associations |  no  |
| [PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md) | A mixin applied to any association whose subject (source node) is a phenotypi... |  no  |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | Association between two concept nodes of phenotypic character, qualified by t... |  no  |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | association between a named thing and a information content entity where the ... |  yes  |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | mixin class for any association whose object (target node) is a disease |  yes  |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | An association between either a disease or a phenotypic feature and an anatom... |  yes  |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | An association between either a disease or a phenotypic feature and its mode ... |  yes  |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | Any association between one genotype and a phenotypic feature, where having t... |  no  |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | Any association between an environment and a phenotypic feature, where being ... |  no  |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | An association between a disease and a phenotypic feature in which the phenot... |  yes  |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | An association between two diseases |  yes  |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | An association between a case (e |  no  |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | An association between an mixture behavior and a behavioral feature manifeste... |  yes  |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | An association between a gene or gene product and a phenotypic feature, where... |  yes  |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | An association between a gene or gene product and a disease, where variation ... |  yes  |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | An association between a gene and a disease where variation in the gene has b... |  yes  |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | An association between a gene (or gene product) and a disease for which the g... |  yes  |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | An association between a gene (or gene product) and a disease in which the ge... |  no  |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | An association between a phenotypic feature (sign or symptom) and a disease, ... |  no  |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | An association between a variant and a gene, where the variant has a genetic ... |  yes  |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | An association between a variant and expression of a gene (i |  no  |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | An association between a variant and a population, where the variant has part... |  yes  |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | An association between a two populations |  yes  |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | An association between a sequence variant and a phenotypic feature, in which ... |  no  |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | An association between a sequence variant and a disease, in which the allele ... |  yes  |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | An association between a genotype and a disease, in which the genotype (typic... |  yes  |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | An association in which a gene (e |  no  |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | An association in which a sequence variant serves as a model of a disease, re... |  no  |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | An association in which a genotype serves as a model of a disease, recapitula... |  no  |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | An association in which a cell line - typically derived from an organismal en... |  no  |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | An association in which an organismal entity (e |  no  |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | An association between two individual organisms (e |  yes  |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | An association between two organism taxa, capturing ecological or evolutionar... |  yes  |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | A gene-to-disease association that is asserted on the grounds that the gene h... |  yes  |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | An association between a gene and a gene expression site, possibly qualified ... |  yes  |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | An association between a sequence variant and a treatment or health intervent... |  yes  |
| [FunctionalAssociation](FunctionalAssociation.md) | An association between a macromolecular machine mixin (gene, gene product or ... |  yes  |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | A functional association between a macromolecular machine (gene, gene product... |  yes  |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | A functional association between a macromolecular machine (gene, gene product... |  yes  |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | A functional association between a macromolecular machine (gene, gene product... |  yes  |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | Added in response to capturing relationship between microbiome activities as ... |  yes  |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | Added in response to capturing relationship between microbiome activities as ... |  yes  |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | A functional association between a gene (or gene product or macromolecular co... |  yes  |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | An association between any entity and a disease, capturing clinical context s... |  no  |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | An association between any entity and a phenotypic feature, capturing clinica... |  no  |
| [SequenceAssociation](SequenceAssociation.md) | An association between a sequence feature and a nucleic acid entity it is loc... |  no  |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | A relationship between a sequence feature and a nucleic acid entity it is loc... |  yes  |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | For example, a particular exon is part of a particular transcript or gene |  yes  |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | A gene is a collection of transcripts |  yes  |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | A gene is transcribed and potentially translated to a gene product |  yes  |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | A transcript is formed from multiple exons |  yes  |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | A regulatory relationship between two genes |  yes  |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | An abstract parent class for associations between two anatomical entities, su... |  yes  |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | A relationship between two anatomical entities where the relationship is mere... |  yes  |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | A relationship between two anatomical entities where the relationship is mere... |  yes  |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | A relationship between two anatomical entities where the relationship is onto... |  yes  |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | An association between a gene or gene product or gene family and an anatomica... |  yes  |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | An association between a biological process or activity and an anatomical ent... |  yes  |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | A relationship between two organism taxon nodes |  yes  |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | A child-parent relationship between two taxa |  yes  |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | An interaction relationship between two taxa |  yes  |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | An abstract association between an organism taxon and an environmental contex... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NamedThing](NamedThing.md) |
| Domain | [Association](Association.md) |
| Domain Of | [Association](Association.md), [GeneToGeneAssociation](GeneToGeneAssociation.md), [CellLineToEntityAssociationMixin](CellLineToEntityAssociationMixin.md), [ChemicalEntityToEntityAssociationMixin](ChemicalEntityToEntityAssociationMixin.md), [DrugToEntityAssociationMixin](DrugToEntityAssociationMixin.md), [ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md), [CaseToEntityAssociationMixin](CaseToEntityAssociationMixin.md), [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md), [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md), [MaterialSampleToEntityAssociationMixin](MaterialSampleToEntityAssociationMixin.md), [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md), [DiseaseToEntityAssociationMixin](DiseaseToEntityAssociationMixin.md), [EntityToExposureEventAssociationMixin](EntityToExposureEventAssociationMixin.md), [EntityToOutcomeAssociationMixin](EntityToOutcomeAssociationMixin.md), [FrequencyQualifierMixin](FrequencyQualifierMixin.md), [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md), [DiseaseOrPhenotypicFeatureToEntityAssociationMixin](DiseaseOrPhenotypicFeatureToEntityAssociationMixin.md), [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md), [GenotypeToEntityAssociationMixin](GenotypeToEntityAssociationMixin.md), [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md), [CaseToVariantAssociation](CaseToVariantAssociation.md), [CaseToGeneAssociation](CaseToGeneAssociation.md), [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md), [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md), [ModelToDiseaseAssociationMixin](ModelToDiseaseAssociationMixin.md), [MacromolecularMachineToEntityAssociationMixin](MacromolecularMachineToEntityAssociationMixin.md), [OrganismTaxonToEntityAssociation](OrganismTaxonToEntityAssociation.md) |
| Slot URI | [rdf:object](http://www.w3.org/1999/02/22-rdf-syntax-ns#object) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdf:object |
| native | namo:object |
| exact | owl:annotatedTarget, OBAN:association_has_object |




## LinkML Source

<details>
```yaml
name: object
local_names:
  ga4gh:
    local_name_source: ga4gh
    local_name_value: descriptor
  neo4j:
    local_name_source: neo4j
    local_name_value: node with incoming relationship
description: connects an association to the object of the association. For example,
  in a gene-to-phenotype association, the gene is subject and phenotype is object.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- owl:annotatedTarget
- OBAN:association_has_object
rank: 1000
is_a: association slot
domain: association
slot_uri: rdf:object
domain_of:
- association
- gene to gene association
- cell line to entity association mixin
- chemical entity to entity association mixin
- drug to entity association mixin
- chemical to entity association mixin
- case to entity association mixin
- chemical entity to chemical entity association
- named thing associated with likelihood of named thing association
- material sample to entity association mixin
- material sample derivation association
- disease to entity association mixin
- entity to exposure event association mixin
- entity to outcome association mixin
- frequency qualifier mixin
- entity to phenotypic feature association mixin
- disease or phenotypic feature to entity association mixin
- entity to disease or phenotypic feature association mixin
- genotype to entity association mixin
- case to disease association
- case to variant association
- case to gene association
- gene to entity association mixin
- variant to entity association mixin
- model to disease association mixin
- macromolecular machine to entity association mixin
- organism taxon to entity association
range: named thing
required: true

```
</details></div>