---
search:
  boost: 5.0
---

# Slot: gene_symbol 


_Standard gene symbol (e.g., HGNC symbol for human genes)._



<div data-search-exclude markdown="1">



URI: [namo:gene_symbol](https://w3id.org/monarch-initiative/namo/gene_symbol)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Gene](Gene.md) | A gene entity with identifiers and expression information |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Gene](Gene.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Gene](Gene.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:gene_symbol |
| native | namo:gene_symbol |




## LinkML Source

<details>
```yaml
name: gene_symbol
description: Standard gene symbol (e.g., HGNC symbol for human genes).
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: Gene
domain_of:
- Gene
range: string

```
</details></div>