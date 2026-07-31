---
search:
  boost: 5.0
---

# Slot: conserved_genes 


_List of genes with conserved expression patterns between model and target._



<div data-search-exclude markdown="1">



URI: [namo:conserved_genes](https://w3id.org/monarch-initiative/namo/conserved_genes)
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
| self | namo:conserved_genes |
| native | namo:conserved_genes |




## LinkML Source

<details>
```yaml
name: conserved_genes
description: List of genes with conserved expression patterns between model and target.
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