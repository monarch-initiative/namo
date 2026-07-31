---
search:
  boost: 5.0
---

# Slot: dataset_download_url 


_A URL from which the dataset itself may be directly downloaded specialised for the dataset domain._



<div data-search-exclude markdown="1">



URI: [dcat:downloadURL](http://www.w3.org/ns/dcat#downloadURL)
Alias: dataset_download_url


## Inheritance

* [node_property](node_property.md)
    * **dataset_download_url**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Dataset](Dataset.md) |
| Slot URI | [dcat:downloadURL](http://www.w3.org/ns/dcat#downloadURL) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:downloadURL |
| native | namo:dataset_download_url |




## LinkML Source

<details>
```yaml
name: dataset download url
description: A URL from which the dataset itself may be directly downloaded specialised
  for the dataset domain.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: dataset
slot_uri: dcat:downloadURL
alias: dataset_download_url
range: string

```
</details></div>