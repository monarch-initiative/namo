---
search:
  boost: 5.0
---

# Slot: diagnoses 


_a relationship that identifies the nature of (an illness or other problem) by examination of the symptoms._



<div data-search-exclude markdown="1">



URI: [namo:diagnoses](https://w3id.org/monarch-initiative/namo/diagnoses)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **diagnoses**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) |
| Domain | [DiagnosticAid](DiagnosticAid.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |












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
| self | namo:diagnoses |
| native | namo:diagnoses |
| exact | DrugCentral:5271, SEMMEDDB:DIAGNOSES |
| close | NCIT:C15220, SIO:001331 |




## LinkML Source

<details>
```yaml
name: diagnoses
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: a relationship that identifies the nature of (an illness or other problem)
  by examination of the symptoms.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- DrugCentral:5271
- SEMMEDDB:DIAGNOSES
close_mappings:
- NCIT:C15220
- SIO:001331
rank: 1000
is_a: related to at instance level
domain: diagnostic aid
inherited: true
range: disease or phenotypic feature
multivalued: true

```
</details></div>