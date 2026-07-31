---
search:
  boost: 5.0
---

# Slot: version 


_A label identifying a particular release or edition of a dataset or resource, typically following a versioning scheme such as a semantic version string or a release date._



<div data-search-exclude markdown="1">



URI: [namo:version](https://w3id.org/monarch-initiative/namo/version)

## Inheritance

* [node_property](node_property.md)
    * **version**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Dataset](Dataset.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:version |
| native | namo:version |
| broad | pav:version, owl:versionInfo |




## LinkML Source

<details>
```yaml
name: version
description: A label identifying a particular release or edition of a dataset or resource,
  typically following a versioning scheme such as a semantic version string or a release
  date.
from_schema: https://w3id.org/monarch-initiative/namo
broad_mappings:
- pav:version
- owl:versionInfo
rank: 1000
is_a: node property
domain: dataset
range: string

```
</details></div>