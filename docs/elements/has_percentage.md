---
search:
  boost: 5.0
---

# Slot: has_percentage 


_equivalent to has quotient multiplied by 100_



<div data-search-exclude markdown="1">



URI: [namo:has_percentage](https://w3id.org/monarch-initiative/namo/has_percentage)
Alias: has_percentage


## Inheritance

* [node_property](node_property.md)
    * [aggregate_statistic](aggregate_statistic.md)
        * **has_percentage**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FrequencyQuantifier](FrequencyQuantifier.md) | A relationship quantifier that expresses how often a relationship holds, usin... |  no  |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | A mixin applied to any association whose object (target node) is a phenotypic... |  no  |
| [PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md) | A mixin applied to any association whose subject (source node) is a phenotypi... |  no  |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | Association between two concept nodes of phenotypic character, qualified by t... |  no  |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | Any association between one genotype and a phenotypic feature, where having t... |  no  |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | Any association between an environment and a phenotypic feature, where being ... |  no  |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | An association between a disease and a phenotypic feature in which the phenot... |  no  |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | An association between a case (e |  no  |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | An association between an mixture behavior and a behavioral feature manifeste... |  no  |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | An association between a gene or gene product and a phenotypic feature, where... |  no  |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | An association between a phenotypic feature (sign or symptom) and a disease, ... |  no  |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | An association between a variant and a population, where the variant has part... |  no  |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | An association between a sequence variant and a phenotypic feature, in which ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain | [NamedThing](NamedThing.md) |
| Domain Of | [FrequencyQuantifier](FrequencyQuantifier.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_percentage |
| native | namo:has_percentage |




## LinkML Source

<details>
```yaml
name: has percentage
description: equivalent to has quotient multiplied by 100
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: aggregate statistic
domain: named thing
alias: has_percentage
domain_of:
- frequency quantifier
range: double

```
</details></div>