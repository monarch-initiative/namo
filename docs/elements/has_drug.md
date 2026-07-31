---
search:
  boost: 5.0
---

# Slot: has_drug 


_connects an entity to one or more drugs_



<div data-search-exclude markdown="1">



URI: [namo:has_drug](https://w3id.org/monarch-initiative/namo/has_drug)
Alias: has_drug


## Inheritance

* [node_property](node_property.md)
    * **has_drug**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Treatment](Treatment.md) | A treatment is targeted at a disease or phenotype and may involve multiple dr... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Drug](Drug.md) |
| Domain | [NamedThing](NamedThing.md) |
| Domain Of | [Treatment](Treatment.md) |

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
| self | namo:has_drug |
| native | namo:has_drug |




## LinkML Source

<details>
```yaml
name: has drug
description: connects an entity to one or more drugs
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: named thing
alias: has_drug
domain_of:
- treatment
range: drug
multivalued: true

```
</details></div>