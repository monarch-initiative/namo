---
search:
  boost: 5.0
---

# Slot: data_source 


_Source of molecular data (e.g., RNA-seq, proteomics, metabolomics)._



<div data-search-exclude markdown="1">



URI: [namo:data_source](https://w3id.org/monarch-initiative/namo/data_source)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MolecularSimilarity](MolecularSimilarity.md) | Detailed assessment of molecular-level concordance between model and biologic... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MolecularSimilarity](MolecularSimilarity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MolecularSimilarity](MolecularSimilarity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:data_source |
| native | namo:data_source |




## LinkML Source

<details>
```yaml
name: data_source
description: Source of molecular data (e.g., RNA-seq, proteomics, metabolomics).
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: MolecularSimilarity
domain_of:
- MolecularSimilarity
range: string

```
</details></div>