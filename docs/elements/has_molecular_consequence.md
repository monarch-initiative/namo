---
search:
  boost: 5.0
---

# Slot: has_molecular_consequence 


_connects a sequence variant to a class describing the molecular consequence. E.g.  SO:0001583_



<div data-search-exclude markdown="1">



URI: [namo:has_molecular_consequence](https://w3id.org/monarch-initiative/namo/has_molecular_consequence)
Alias: has_molecular_consequence


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_molecular_consequence**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OntologyClass](OntologyClass.md) |
| Domain | [NamedThing](NamedThing.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |









## Aliases


* allele has activity




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
| self | namo:has_molecular_consequence |
| native | namo:has_molecular_consequence |
| narrow | NCIT:allele_has_activity |




## LinkML Source

<details>
```yaml
name: has molecular consequence
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: connects a sequence variant to a class describing the molecular consequence.
  E.g.  SO:0001583
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- allele has activity
narrow_mappings:
- NCIT:allele_has_activity
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: has_molecular_consequence
range: ontology class
multivalued: true

```
</details></div>