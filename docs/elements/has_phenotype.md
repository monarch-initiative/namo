---
search:
  boost: 5.0
---

# Slot: has_phenotype 


_holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). In SNOMEDCT, disorders with keyword 'characterized by' should translate into this predicate._



<div data-search-exclude markdown="1">



URI: [namo:has_phenotype](https://w3id.org/monarch-initiative/namo/has_phenotype)
Alias: has_phenotype


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_phenotype**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhenotypicFeature](PhenotypicFeature.md) |
| Domain | [BiologicalEntity](BiologicalEntity.md) |

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



## Aliases


* disease presents symptom


## Notes

* check the range



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
| self | namo:has_phenotype |
| native | namo:has_phenotype |
| exact | RO:0002200 |
| narrow | NCIT:R89, DOID-PROPERTY:has_symptom, RO:0004022, RO:0004029 |
| broad | NCIT:R115, NCIT:R108 |




## LinkML Source

<details>
```yaml
name: has phenotype
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a biological entity and a phenotype, where a phenotype
  is construed broadly as any kind of quality of an organism part, a collection of
  these qualities, or a change in quality or qualities (e.g. abnormally increased
  temperature). In SNOMEDCT, disorders with keyword 'characterized by' should translate
  into this predicate.
notes:
- check the range
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- disease presents symptom
exact_mappings:
- RO:0002200
narrow_mappings:
- NCIT:R89
- DOID-PROPERTY:has_symptom
- RO:0004022
- RO:0004029
broad_mappings:
- NCIT:R115
- NCIT:R108
rank: 1000
is_a: related to at instance level
domain: biological entity
inherited: true
alias: has_phenotype
range: phenotypic feature
multivalued: true

```
</details></div>