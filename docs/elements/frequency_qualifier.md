---
search:
  boost: 5.0
---

# Slot: frequency_qualifier 


_a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_



<div data-search-exclude markdown="1">



URI: [namo:frequency_qualifier](https://w3id.org/monarch-initiative/namo/frequency_qualifier)
Alias: frequency_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **frequency_qualifier**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FrequencyQualifierMixin](FrequencyQualifierMixin.md) | Qualifier for frequency type associations |  no  |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  no  |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  no  |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  no  |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | Qualifiers for entity to disease or phenotype associations |  no  |
| [EntityToFeatureOrVariantQualifiersMixin](EntityToFeatureOrVariantQualifiersMixin.md) | Qualifiers for entity to variant associations |  no  |
| [EntityToFeatureOrGeneQualifiersMixin](EntityToFeatureOrGeneQualifiersMixin.md) | Qualifiers for entity to gene associations |  no  |
| [FeatureOrDiseaseQualifiersToEntityMixin](FeatureOrDiseaseQualifiersToEntityMixin.md) | Qualifiers for disease or phenotype to entity associations |  no  |
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
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | An association between a gene (or gene product) and a disease for which the g... |  no  |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | An association between a gene (or gene product) and a disease in which the ge... |  no  |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | An association between a phenotypic feature (sign or symptom) and a disease, ... |  no  |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | An association between a variant and a population, where the variant has part... |  no  |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | An association between a sequence variant and a phenotypic feature, in which ... |  no  |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | An association between a sequence variant and a disease, in which the allele ... |  no  |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | An association between a genotype and a disease, in which the genotype (typic... |  no  |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | An association in which a gene (e |  no  |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | An association in which a sequence variant serves as a model of a disease, re... |  no  |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | An association in which a genotype serves as a model of a disease, recapitula... |  no  |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | An association in which a cell line - typically derived from an organismal en... |  no  |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | An association in which an organismal entity (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FrequencyValue](FrequencyValue.md) |
| Domain | [Association](Association.md) |
| Domain Of | [FrequencyQualifierMixin](FrequencyQualifierMixin.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |






## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:frequency_qualifier |
| native | namo:frequency_qualifier |




## LinkML Source

<details>
```yaml
name: frequency qualifier
description: a qualifier used in a phenotypic association to state how frequent the
  phenotype is observed in the subject
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: qualifier
domain: association
alias: frequency_qualifier
domain_of:
- frequency qualifier mixin
range: frequency value

```
</details></div>