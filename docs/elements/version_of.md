---
search:
  boost: 5.0
---

# Slot: version_of 


_Links a dataset version to the dataset summary of which it is a version, edition, or adaptation._



<div data-search-exclude markdown="1">



URI: [namo:version_of](https://w3id.org/monarch-initiative/namo/version_of)
Alias: version_of


## Inheritance

* [node_property](node_property.md)
    * **version_of**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DatasetSummary](DatasetSummary.md) |
| Domain | [DatasetVersion](DatasetVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:version_of |
| native | namo:version_of |
| exact | dct:isVersionOf |




## LinkML Source

<details>
```yaml
name: version of
description: Links a dataset version to the dataset summary of which it is a version,
  edition, or adaptation.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- dct:isVersionOf
rank: 1000
is_a: node property
domain: dataset version
alias: version_of
range: dataset summary

```
</details></div>