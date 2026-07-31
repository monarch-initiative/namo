---
search:
  boost: 5.0
---

# Slot: has_procedure 


_connects an entity to one or more (medical) procedures_



<div data-search-exclude markdown="1">



URI: [namo:has_procedure](https://w3id.org/monarch-initiative/namo/has_procedure)
Alias: has_procedure


## Inheritance

* [node_property](node_property.md)
    * **has_procedure**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Treatment](Treatment.md) | A treatment is targeted at a disease or phenotype and may involve multiple dr... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Procedure](Procedure.md) |
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
| self | namo:has_procedure |
| native | namo:has_procedure |




## LinkML Source

<details>
```yaml
name: has procedure
description: connects an entity to one or more (medical) procedures
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: named thing
alias: has_procedure
domain_of:
- treatment
range: procedure
multivalued: true

```
</details></div>