---
search:
  boost: 5.0
---

# Slot: allelic_requirement 


_The allele configuration of a particular gene or variant required for the expression of a disease or phenotype in a specific patient or instance._



<div data-search-exclude markdown="1">



URI: [namo:allelic_requirement](https://w3id.org/monarch-initiative/namo/allelic_requirement)
Alias: allelic_requirement


## Inheritance

* [association_slot](association_slot.md)
    * **allelic_requirement**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | An association between a gene or gene product and a phenotypic feature, where... |  no  |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | An association between a gene or gene product and a disease, where variation ... |  no  |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | An association between a gene and a disease where variation in the gene has b... |  no  |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | An association between a gene (or gene product) and a disease for which the g... |  no  |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | An association between a gene (or gene product) and a disease in which the ge... |  no  |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | An association in which a gene (e |  no  |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | A gene-to-disease association that is asserted on the grounds that the gene h... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Association](Association.md) |
| Domain Of | [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md), [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md), [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md), [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^HP:\d{7}$` |










## Comments

* This edge property may be used by associations between Genes or SequenceVariants and DiseaseOrPhenotypicFeatures to provide the inheritance pattern and genetic context of the relationship. Terms from the HP mode of inheritance sub-ontology (HP:0000005) should be used in the value of this slot. This slot differs from the predicate "has_mode_of_inheritance", in that the predicate is used to link a disease or phenotype with its general inheritance pattern (how it is typically transmitted from one generation to the next, regardless of the specific genetic variant that is present in an individual or instance).



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:allelic_requirement |
| native | namo:allelic_requirement |




## LinkML Source

<details>
```yaml
name: allelic requirement
description: The allele configuration of a particular gene or variant required for
  the expression of a disease or phenotype in a specific patient or instance.
comments:
- This edge property may be used by associations between Genes or SequenceVariants
  and DiseaseOrPhenotypicFeatures to provide the inheritance pattern and genetic context
  of the relationship. Terms from the HP mode of inheritance sub-ontology (HP:0000005)
  should be used in the value of this slot. This slot differs from the predicate "has_mode_of_inheritance",
  in that the predicate is used to link a disease or phenotype with its general inheritance
  pattern (how it is typically transmitted from one generation to the next, regardless
  of the specific genetic variant that is present in an individual or instance).
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: allelic_requirement
domain_of:
- gene to phenotypic feature association
- gene to disease association
- causal gene to disease association
- correlated gene to disease association
range: string
pattern: ^HP:\d{7}$

```
</details></div>