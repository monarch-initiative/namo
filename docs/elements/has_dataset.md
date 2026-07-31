---
search:
  boost: 5.0
---

# Slot: has_dataset 


_Links a dataset version to the underlying dataset that it is a version of._



<div data-search-exclude markdown="1">



URI: [namo:has_dataset](https://w3id.org/monarch-initiative/namo/has_dataset)
Alias: has_dataset


## Inheritance

* [node_property](node_property.md)
    * **has_dataset**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DatasetVersion](DatasetVersion.md) | an item that holds version level information about a dataset |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Dataset](Dataset.md) |
| Domain | [DatasetVersion](DatasetVersion.md) |
| Domain Of | [DatasetVersion](DatasetVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_dataset |
| native | namo:has_dataset |
| broad | dct:source |




## LinkML Source

<details>
```yaml
name: has dataset
description: Links a dataset version to the underlying dataset that it is a version
  of.
from_schema: https://w3id.org/monarch-initiative/namo
broad_mappings:
- dct:source
rank: 1000
is_a: node property
domain: dataset version
alias: has_dataset
domain_of:
- dataset version
range: dataset

```
</details></div>