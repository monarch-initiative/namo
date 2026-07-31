---
search:
  boost: 5.0
---

# Slot: distribution_download_url 


_A URL from which a specific distribution (serialization or format) of a dataset may be directly downloaded; corresponds to dcat:downloadURL specialised for the dataset distribution domain._



<div data-search-exclude markdown="1">



URI: [namo:distribution_download_url](https://w3id.org/monarch-initiative/namo/distribution_download_url)
Alias: distribution_download_url


## Inheritance

* [node_property](node_property.md)
    * **distribution_download_url**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DatasetDistribution](DatasetDistribution.md) | an item that holds distribution level information about a dataset |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [DatasetDistribution](DatasetDistribution.md) |
| Domain Of | [DatasetDistribution](DatasetDistribution.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:distribution_download_url |
| native | namo:distribution_download_url |
| exact | dcat:downloadURL |




## LinkML Source

<details>
```yaml
name: distribution download url
description: A URL from which a specific distribution (serialization or format) of
  a dataset may be directly downloaded; corresponds to dcat:downloadURL specialised
  for the dataset distribution domain.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- dcat:downloadURL
rank: 1000
is_a: node property
domain: dataset distribution
alias: distribution_download_url
domain_of:
- dataset distribution
range: string

```
</details></div>