---
search:
  boost: 5.0
---

# Slot: qualified_predicate 


_Predicate to be used in an association when subject and object qualifiers are present and the full reading of the statement requires a qualification to the predicate in use in order to refine or increase the specificity of the full statement reading.  Has a value from the Biolink 'related_to' hierarchy, for example, biolink:related_to, biolink:causes, biolink:treats This qualifier holds a relationship to be used instead of that expressed by the primary predicate, in a ‘full statement’ reading of the association, where qualifier-based semantics are included. This is necessary only in cases where the primary predicate does not work in a full statement reading._



<div data-search-exclude markdown="1">



URI: [namo:qualified_predicate](https://w3id.org/monarch-initiative/namo/qualified_predicate)
Alias: qualified_predicate


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **qualified_predicate**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | parent class for different kinds of gene-gene or gene product to gene product... |  no  |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | An association between a chemical entity and a biological process, where the ... |  no  |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | describes an interaction between a chemical entity and a gene or gene product |  no  |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | Describes the relationship between an enzyme (usually a macromolecular comple... |  no  |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | Describes a regulatory relationship between two genes or gene products |  yes  |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | Describes an effect that a chemical has on a biological entity (e |  yes  |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | Describes a relationship in which a chemical entity affects the sensitivity o... |  yes  |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | Describes an effect that a gene or gene product has on a chemical entity (e |  yes  |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | Qualifiers for entity to disease or phenotype associations |  no  |
| [EntityToFeatureOrVariantQualifiersMixin](EntityToFeatureOrVariantQualifiersMixin.md) | Qualifiers for entity to variant associations |  no  |
| [EntityToFeatureOrGeneQualifiersMixin](EntityToFeatureOrGeneQualifiersMixin.md) | Qualifiers for entity to gene associations |  no  |
| [FeatureOrDiseaseQualifiersToEntityMixin](FeatureOrDiseaseQualifiersToEntityMixin.md) | Qualifiers for disease or phenotype to entity associations |  no  |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | An association between a gene or gene product and a disease, where variation ... |  no  |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | An association between a gene and a disease where variation in the gene has b... |  no  |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | An association between a gene (or gene product) and a disease for which the g... |  no  |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | A homology association between two genes |  no  |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | Indicates that two genes are co-expressed, generally under the same condition... |  no  |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | An interaction between two genes or two gene products |  no  |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | An interaction at the molecular level between two physical entities |  no  |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  no  |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  no  |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  no  |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |  no  |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | A mixin applied to any association whose object (target node) is a phenotypic... |  no  |
| [PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md) | A mixin applied to any association whose subject (source node) is a phenotypi... |  no  |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | Association between two concept nodes of phenotypic character, qualified by t... |  no  |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | mixin class for any association whose object (target node) is a disease |  no  |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | Any association between one genotype and a phenotypic feature, where having t... |  no  |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | Any association between an environment and a phenotypic feature, where being ... |  no  |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | An association between a disease and a phenotypic feature in which the phenot... |  no  |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | An association between two diseases |  no  |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | An association between a case (e |  no  |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | An association between an mixture behavior and a behavioral feature manifeste... |  no  |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | An association between a gene or gene product and a phenotypic feature, where... |  no  |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | An association between a gene (or gene product) and a disease in which the ge... |  no  |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | An association between a phenotypic feature (sign or symptom) and a disease, ... |  no  |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | An association between a sequence variant and a phenotypic feature, in which ... |  no  |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | An association between a sequence variant and a disease, in which the allele ... |  no  |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | An association between a genotype and a disease, in which the genotype (typic... |  no  |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | An association in which a gene (e |  no  |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | An association in which a sequence variant serves as a model of a disease, re... |  no  |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | An association in which a genotype serves as a model of a disease, recapitula... |  no  |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | An association in which a cell line - typically derived from an organismal en... |  no  |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | An association in which an organismal entity (e |  no  |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | A gene-to-disease association that is asserted on the grounds that the gene h... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain | [Association](Association.md) |
| Domain Of | [PredicateMapping](PredicateMapping.md), [GeneToGeneAssociation](GeneToGeneAssociation.md), [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md), [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md), [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md), [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md), [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md), [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md), [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md), [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md), [EntityToFeatureOrVariantQualifiersMixin](EntityToFeatureOrVariantQualifiersMixin.md), [EntityToFeatureOrGeneQualifiersMixin](EntityToFeatureOrGeneQualifiersMixin.md), [FeatureOrDiseaseQualifiersToEntityMixin](FeatureOrDiseaseQualifiersToEntityMixin.md), [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md), [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md), [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| biolink:causes |

## Notes

* to express the statement that “Chemical X causes increased expression of Gene Y”, the core triple is read using the fields subject:ChemX, predicate:affects, object:GeneY . . . and the full statement is read using the fields subject:ChemX, qualified_predicate:causes, object:GeneY, object_aspect: expression, object_direction:increased. The predicate ‘affects’ is needed for the core triple reading, but does not make sense in the full statement reading  (because “Chemical X affects increased expression of Gene Y'' is not what we mean to say here: it causes increased expression of Gene Y)



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:qualified_predicate |
| native | namo:qualified_predicate |




## LinkML Source

<details>
```yaml
name: qualified predicate
description: Predicate to be used in an association when subject and object qualifiers
  are present and the full reading of the statement requires a qualification to the
  predicate in use in order to refine or increase the specificity of the full statement
  reading.  Has a value from the Biolink 'related_to' hierarchy, for example, biolink:related_to,
  biolink:causes, biolink:treats This qualifier holds a relationship to be used instead
  of that expressed by the primary predicate, in a ‘full statement’ reading of the
  association, where qualifier-based semantics are included. This is necessary only
  in cases where the primary predicate does not work in a full statement reading.
notes:
- 'to express the statement that “Chemical X causes increased expression of Gene Y”,
  the core triple is read using the fields subject:ChemX, predicate:affects, object:GeneY
  . . . and the full statement is read using the fields subject:ChemX, qualified_predicate:causes,
  object:GeneY, object_aspect: expression, object_direction:increased. The predicate
  ‘affects’ is needed for the core triple reading, but does not make sense in the
  full statement reading  (because “Chemical X affects increased expression of Gene
  Y'''' is not what we mean to say here: it causes increased expression of Gene Y)'
examples:
- value: biolink:causes
  description: used with `affects` predicate to express causal statements
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: qualifier
domain: association
alias: qualified_predicate
domain_of:
- predicate mapping
- gene to gene association
- chemical entity to biological process association
- chemical gene interaction association
- macromolecular machine has substrate association
- gene regulates gene association
- chemical affects biological entity association
- chemical gene sensitivity association
- gene affects chemical association
- entity to feature or disease qualifiers mixin
- entity to feature or variant qualifiers mixin
- entity to feature or gene qualifiers mixin
- feature or disease qualifiers to entity mixin
- gene to disease association
- causal gene to disease association
- correlated gene to disease association
range: uriorcurie

```
</details></div>