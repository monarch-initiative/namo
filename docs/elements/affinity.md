---
search:
  boost: 5.0
---

# Slot: affinity 


_The numerical value describing the strength of an affinity between two entities.  For instance, if a chemical inhibits a protein with a pIC50 of 8.6, the affinity is 8.6. Used in conjunction with the affinity parameter slot._



<div data-search-exclude markdown="1">



URI: [namo:affinity](https://w3id.org/monarch-initiative/namo/affinity)

## Inheritance

* [node_property](node_property.md)
    * **affinity**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AffinityMeasurement](AffinityMeasurement.md) | The type of measurement describing the strength of an affinity between two en... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain | [NamedThing](NamedThing.md) |
| Domain Of | [AffinityMeasurement](AffinityMeasurement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:affinity |
| native | namo:affinity |




## LinkML Source

<details>
```yaml
name: affinity
description: The numerical value describing the strength of an affinity between two
  entities.  For instance, if a chemical inhibits a protein with a pIC50 of 8.6, the
  affinity is 8.6. Used in conjunction with the affinity parameter slot.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: named thing
domain_of:
- affinity measurement
range: float

```
</details></div>