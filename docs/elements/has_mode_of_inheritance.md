---
search:
  boost: 5.0
---

# Slot: has_mode_of_inheritance 


_Relates a disease or phenotypic feature to its observed genetic segregation and assumed associated underlying DNA manifestation (i.e. autosomal, sex or mitochondrial chromosome)._



<div data-search-exclude markdown="1">



URI: [namo:has_mode_of_inheritance](https://w3id.org/monarch-initiative/namo/has_mode_of_inheritance)
Alias: has_mode_of_inheritance


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_manifestation](has_manifestation.md)
            * **has_mode_of_inheritance**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeneticInheritance](GeneticInheritance.md) |
| Domain | [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |








## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_mode_of_inheritance |
| native | namo:has_mode_of_inheritance |




## LinkML Source

<details>
```yaml
name: has mode of inheritance
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Relates a disease or phenotypic feature to its observed genetic segregation
  and assumed associated underlying DNA manifestation (i.e. autosomal, sex or mitochondrial
  chromosome).
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: has manifestation
domain: disease or phenotypic feature
inherited: true
alias: has_mode_of_inheritance
range: genetic inheritance
multivalued: true

```
</details></div>