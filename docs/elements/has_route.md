---
search:
  boost: 5.0
---

# Slot: has_route 


_the process that results in the stressor coming into direct contact with the receptor_



<div data-search-exclude markdown="1">



URI: [namo:has_route](https://w3id.org/monarch-initiative/namo/has_route)
Alias: has_route


## Inheritance

* [node_property](node_property.md)
    * **has_route**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [ExposureEvent](ExposureEvent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_route |
| native | namo:has_route |
| exact | ExO:0000055 |
| narrow | LOINC:has_pharmaceutical_route, SNOMED:has_dose_form_intended_site, SNOMED:has_route_of_administration |




## LinkML Source

<details>
```yaml
name: has route
description: the process that results in the stressor coming into direct contact with
  the receptor
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- ExO:0000055
narrow_mappings:
- LOINC:has_pharmaceutical_route
- SNOMED:has_dose_form_intended_site
- SNOMED:has_route_of_administration
rank: 1000
is_a: node property
domain: exposure event
alias: has_route
range: string

```
</details></div>