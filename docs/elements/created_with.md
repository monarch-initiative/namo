---
search:
  boost: 5.0
---

# Slot: created_with 


_An identifier (typically a URL or CURIE) of the software tool, service, or pipeline used to create the dataset._



<div data-search-exclude markdown="1">



URI: [namo:created_with](https://w3id.org/monarch-initiative/namo/created_with)
Alias: created_with


## Inheritance

* [node_property](node_property.md)
    * **created_with**








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
| self | namo:created_with |
| native | namo:created_with |
| exact | pav:createdWith |




## LinkML Source

<details>
```yaml
name: created with
description: An identifier (typically a URL or CURIE) of the software tool, service,
  or pipeline used to create the dataset.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- pav:createdWith
rank: 1000
is_a: node property
domain: dataset
alias: created_with
range: string

```
</details></div>