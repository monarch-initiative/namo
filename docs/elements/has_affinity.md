---
search:
  boost: 5.0
---

# Slot: has_affinity 


_Set of measurements documenting the strength of chemical entity to gene or gene product interactions._



<div data-search-exclude markdown="1">



URI: [namo:has_affinity](https://w3id.org/monarch-initiative/namo/has_affinity)
Alias: has_affinity


## Inheritance

* [association_slot](association_slot.md)
    * **has_affinity**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | describes an interaction between a chemical entity and a gene or gene product |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AffinityMeasurement](AffinityMeasurement.md) |
| Domain | [Association](Association.md) |
| Domain Of | [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_affinity |
| native | namo:has_affinity |




## LinkML Source

<details>
```yaml
name: has affinity
description: Set of measurements documenting the strength of chemical entity to gene
  or gene product interactions.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: has_affinity
domain_of:
- chemical gene interaction association
range: affinity measurement
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>