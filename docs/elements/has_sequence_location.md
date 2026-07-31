---
search:
  boost: 5.0
---

# Slot: has_sequence_location 


_holds between two nucleic acid entities when the subject can be localized in sequence coordinates on the object. For example, between an exon and a chromosome/contig._



<div data-search-exclude markdown="1">



URI: [namo:has_sequence_location](https://w3id.org/monarch-initiative/namo/has_sequence_location)
Alias: has_sequence_location


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_sequence_location**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NucleicAcidEntity](NucleicAcidEntity.md) |
| Domain | [NucleicAcidEntity](NucleicAcidEntity.md) |

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
| self | namo:has_sequence_location |
| native | namo:has_sequence_location |
| exact | faldo:location |




## LinkML Source

<details>
```yaml
name: has sequence location
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two nucleic acid entities when the subject can be localized
  in sequence coordinates on the object. For example, between an exon and a chromosome/contig.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- faldo:location
rank: 1000
is_a: related to at instance level
domain: nucleic acid entity
inherited: true
alias: has_sequence_location
range: nucleic acid entity
multivalued: true

```
</details></div>