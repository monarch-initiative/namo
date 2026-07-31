---
search:
  boost: 5.0
---

# Slot: has_gene 


_connects an entity associated with one or more genes_



<div data-search-exclude markdown="1">



URI: [namo:has_gene](https://w3id.org/monarch-initiative/namo/has_gene)
Alias: has_gene


## Inheritance

* [node_property](node_property.md)
    * [has_gene_or_gene_product](has_gene_or_gene_product.md)
        * **has_gene**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SequenceVariant](SequenceVariant.md) | A sequence_variant is a non exact copy of a sequence_feature or genome exhibi... |  yes  |
| [Snv](Snv.md) | SNVs are single nucleotide positions in genomic DNA at which different sequen... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Gene](Gene.md) |
| Domain | [NamedThing](NamedThing.md) |
| Domain Of | [SequenceVariant](SequenceVariant.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_gene |
| native | namo:has_gene |




## LinkML Source

<details>
```yaml
name: has gene
description: connects an entity associated with one or more genes
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: has gene or gene product
domain: named thing
alias: has_gene
domain_of:
- sequence variant
range: gene
multivalued: true

```
</details></div>