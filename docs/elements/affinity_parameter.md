---
search:
  boost: 5.0
---

# Slot: affinity_parameter 


_The type of parameter describing the strength of an affinity between two entities.  For instance, if a chemical inhibits a protein with a pIC50 of 8.6, the 'affinity parameter' is pIC50. Used in conjunction with the 'affinity' slot, within an 'affinity measurement'._



<div data-search-exclude markdown="1">



URI: [namo:affinity_parameter](https://w3id.org/monarch-initiative/namo/affinity_parameter)
Alias: affinity_parameter


## Inheritance

* [node_property](node_property.md)
    * **affinity_parameter**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AffinityMeasurement](AffinityMeasurement.md) | The type of measurement describing the strength of an affinity between two en... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AffinityParameterEnum](AffinityParameterEnum.md) |
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
| self | namo:affinity_parameter |
| native | namo:affinity_parameter |




## LinkML Source

<details>
```yaml
name: affinity parameter
description: The type of parameter describing the strength of an affinity between
  two entities.  For instance, if a chemical inhibits a protein with a pIC50 of 8.6,
  the 'affinity parameter' is pIC50. Used in conjunction with the 'affinity' slot,
  within an 'affinity measurement'.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: named thing
alias: affinity_parameter
domain_of:
- affinity measurement
range: AffinityParameterEnum

```
</details></div>