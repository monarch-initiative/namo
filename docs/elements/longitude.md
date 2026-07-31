---
search:
  boost: 5.0
---

# Slot: longitude 


_longitude_



<div data-search-exclude markdown="1">



URI: [namo:longitude](https://w3id.org/monarch-initiative/namo/longitude)

## Inheritance

* [node_property](node_property.md)
    * **longitude**






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
| self | namo:longitude |
| native | namo:longitude |
| exact | wgs:long |




## LinkML Source

<details>
```yaml
name: longitude
description: longitude
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- wgs:long
rank: 1000
is_a: node property
domain: named thing
domain_of:
- geographic location
range: float

```
</details></div>