---
search:
  boost: 5.0
---

# Slot: has_device 


_connects an entity to one or more (medical) devices_



<div data-search-exclude markdown="1">



URI: [namo:has_device](https://w3id.org/monarch-initiative/namo/has_device)
Alias: has_device


## Inheritance

* [node_property](node_property.md)
    * **has_device**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Treatment](Treatment.md) | A treatment is targeted at a disease or phenotype and may involve multiple dr... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Device](Device.md) |
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
| self | namo:has_device |
| native | namo:has_device |




## LinkML Source

<details>
```yaml
name: has device
description: connects an entity to one or more (medical) devices
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: named thing
alias: has_device
domain_of:
- treatment
range: device
multivalued: true

```
</details></div>