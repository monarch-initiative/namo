---
search:
  boost: 5.0
---

# Slot: source_logo 


_A URL referencing an image that serves as the visual logo of a data source._



<div data-search-exclude markdown="1">



URI: [schema:logo](http://schema.org/logo)
Alias: source_logo


## Inheritance

* [node_property](node_property.md)
    * **source_logo**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DatasetSummary](DatasetSummary.md) | an item that holds summary level information about a dataset |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [DatasetSummary](DatasetSummary.md) |
| Domain Of | [DatasetSummary](DatasetSummary.md) |
| Slot URI | [schema:logo](http://schema.org/logo) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:logo |
| native | namo:source_logo |




## LinkML Source

<details>
```yaml
name: source logo
description: A URL referencing an image that serves as the visual logo of a data source.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: dataset summary
slot_uri: schema:logo
alias: source_logo
domain_of:
- dataset summary
range: string

```
</details></div>