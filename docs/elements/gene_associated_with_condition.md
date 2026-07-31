---
search:
  boost: 5.0
---

# Slot: gene_associated_with_condition 


_holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with_



<div data-search-exclude markdown="1">



URI: [namo:gene_associated_with_condition](https://w3id.org/monarch-initiative/namo/gene_associated_with_condition)
Alias: gene_associated_with_condition


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * [genetically_associated_with](genetically_associated_with.md)
                * **gene_associated_with_condition**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) |
| Domain | [Gene](Gene.md) |

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
| self | namo:gene_associated_with_condition |
| native | namo:gene_associated_with_condition |
| narrow | NCIT:R38, NCIT:R175, NCIT:R48 |
| broad | GENO:0000840, GENO:0000841 |




## LinkML Source

<details>
```yaml
name: gene associated with condition
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a gene and a disease or phenotypic feature that the gene
  or its alleles/products may influence, contribute to, or correlate with
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
narrow_mappings:
- NCIT:R38
- NCIT:R175
- NCIT:R48
broad_mappings:
- GENO:0000840
- GENO:0000841
rank: 1000
is_a: genetically associated with
domain: gene
inherited: true
alias: gene_associated_with_condition
range: disease or phenotypic feature
multivalued: true

```
</details></div>