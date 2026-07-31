---
search:
  boost: 5.0
---

# Slot: latitude 


_latitude_



<div data-search-exclude markdown="1">



URI: [namo:latitude](https://w3id.org/monarch-initiative/namo/latitude)

## Inheritance

* [node_property](node_property.md)
    * **latitude**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeographicLocation](GeographicLocation.md) | a location that can be described in lat/long coordinates |  no  |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | a location that can be described in lat/long coordinates, for a particular ti... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain | [NamedThing](NamedThing.md) |
| Domain Of | [GeographicLocation](GeographicLocation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:latitude |
| native | namo:latitude |
| exact | wgs:lat |




## LinkML Source

<details>
```yaml
name: latitude
description: latitude
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- wgs:lat
rank: 1000
is_a: node property
domain: named thing
domain_of:
- geographic location
range: float

```
</details></div>