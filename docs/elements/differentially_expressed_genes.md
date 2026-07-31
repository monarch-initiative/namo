---
search:
  boost: 5.0
---

# Slot: differentially_expressed_genes 


_List of genes that are differentially expressed in the model system._



<div data-search-exclude markdown="1">



URI: [namo:differentially_expressed_genes](https://w3id.org/monarch-initiative/namo/differentially_expressed_genes)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MolecularSimilarity](MolecularSimilarity.md) | Detailed assessment of molecular-level concordance between model and biologic... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeneExpressionResult](GeneExpressionResult.md) |
| Domain Of | [MolecularSimilarity](MolecularSimilarity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
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
| self | namo:differentially_expressed_genes |
| native | namo:differentially_expressed_genes |




## LinkML Source

<details>
```yaml
name: differentially_expressed_genes
description: List of genes that are differentially expressed in the model system.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: MolecularSimilarity
domain_of:
- MolecularSimilarity
range: GeneExpressionResult
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>