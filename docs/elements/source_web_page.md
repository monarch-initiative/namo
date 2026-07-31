---
search:
  boost: 5.0
---

# Slot: source_web_page 


_A URL of a web page that documents or serves as the landing page for a data source._



<div data-search-exclude markdown="1">



URI: [namo:source_web_page](https://w3id.org/monarch-initiative/namo/source_web_page)
Alias: source_web_page


## Inheritance

* [node_property](node_property.md)
    * **source_web_page**






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

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:source_web_page |
| native | namo:source_web_page |
| broad | dct:source |




## LinkML Source

<details>
```yaml
name: source web page
description: A URL of a web page that documents or serves as the landing page for
  a data source.
from_schema: https://w3id.org/monarch-initiative/namo
broad_mappings:
- dct:source
rank: 1000
is_a: node property
domain: dataset summary
alias: source_web_page
domain_of:
- dataset summary
range: string

```
</details></div>