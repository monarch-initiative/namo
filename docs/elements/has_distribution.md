---
search:
  boost: 5.0
---

# Slot: has_distribution 


_Links a dataset version to one of its dataset distributions (a specific representation or serialization of the dataset)._



<div data-search-exclude markdown="1">



URI: [dct:distribution](http://purl.org/dc/terms/distribution)
Alias: has_distribution


## Inheritance

* [node_property](node_property.md)
    * **has_distribution**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DatasetVersion](DatasetVersion.md) | an item that holds version level information about a dataset |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DatasetDistribution](DatasetDistribution.md) |
| Domain | [DatasetVersion](DatasetVersion.md) |
| Domain Of | [DatasetVersion](DatasetVersion.md) |
| Slot URI | [dct:distribution](http://purl.org/dc/terms/distribution) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:distribution |
| native | namo:has_distribution |




## LinkML Source

<details>
```yaml
name: has distribution
description: Links a dataset version to one of its dataset distributions (a specific
  representation or serialization of the dataset).
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: dataset version
slot_uri: dct:distribution
alias: has_distribution
domain_of:
- dataset version
range: dataset distribution

```
</details></div>