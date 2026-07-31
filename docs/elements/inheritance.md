---
search:
  boost: 5.0
---

# Slot: inheritance 


_Connects genetic inheritance to a disease or phenotypic feature, as a node property._



<div data-search-exclude markdown="1">



URI: [namo:inheritance](https://w3id.org/monarch-initiative/namo/inheritance)

## Inheritance

* [node_property](node_property.md)
    * **inheritance**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | A disease or an individual phenotypic feature, grouped as a single class to a... |  no  |
| [Disease](Disease.md) | A disease is a disposition to undergo pathological processes that exists in a... |  no  |
| [PhenotypicFeature](PhenotypicFeature.md) | A combination of entity and quality that makes up a phenotyping statement |  no  |
| [BehavioralFeature](BehavioralFeature.md) | A phenotypic feature which is behavioral in nature |  no  |
| [ClinicalFinding](ClinicalFinding.md) | this category is currently considered broad enough to tag clinical lab measur... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeneticInheritance](GeneticInheritance.md) |
| Domain | [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) |
| Domain Of | [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:inheritance |
| native | namo:inheritance |
| exact | OMIM:has_inheritance_type |




## LinkML Source

<details>
```yaml
name: inheritance
description: Connects genetic inheritance to a disease or phenotypic feature, as a
  node property.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- OMIM:has_inheritance_type
rank: 1000
is_a: node property
domain: disease or phenotypic feature
domain_of:
- disease or phenotypic feature
range: genetic inheritance

```
</details></div>