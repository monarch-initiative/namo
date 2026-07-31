---
search:
  boost: 5.0
---

# Slot: gene_product_of 


_definition x has gene product of y if and only if y is a gene (SO:0000704) that participates in some gene expression process (GO:0010467) where the output of thatf process is either y or something that is ribosomally translated from x_



<div data-search-exclude markdown="1">



URI: [namo:gene_product_of](https://w3id.org/monarch-initiative/namo/gene_product_of)
Alias: gene_product_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **gene_product_of**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Gene](Gene.md) |
| Domain | [GeneProductMixin](GeneProductMixin.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |








## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:gene_product_of |
| native | namo:gene_product_of |
| exact | RO:0002204 |




## LinkML Source

<details>
```yaml
name: gene product of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: definition x has gene product of y if and only if y is a gene (SO:0000704)
  that participates in some gene expression process (GO:0010467) where the output
  of thatf process is either y or something that is ribosomally translated from x
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002204
rank: 1000
is_a: related to at instance level
domain: gene product mixin
inherited: true
alias: gene_product_of
range: gene
multivalued: true

```
</details></div>