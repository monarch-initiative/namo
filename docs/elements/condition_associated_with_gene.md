---
search:
  boost: 5.0
---

# Slot: condition_associated_with_gene 


_holds between a gene and a disease or phenotypic feature that may be influenced, contribute to, or be correlated with the gene or its alleles/products_



<div data-search-exclude markdown="1">



URI: [namo:condition_associated_with_gene](https://w3id.org/monarch-initiative/namo/condition_associated_with_gene)
Alias: condition_associated_with_gene


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * [genetically_associated_with](genetically_associated_with.md)
                * **condition_associated_with_gene**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Gene](Gene.md) |
| Domain | [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |


<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Inverse | [gene_associated_with_condition](gene_associated_with_condition.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)



## Aliases


* disease associated with gene




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:condition_associated_with_gene |
| native | namo:condition_associated_with_gene |
| narrow | RO:0004000, NCIT:R176 |




## LinkML Source

<details>
```yaml
name: condition associated with gene
description: holds between a gene and a disease or phenotypic feature that may be
  influenced, contribute to, or be correlated with the gene or its alleles/products
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- disease associated with gene
narrow_mappings:
- RO:0004000
- NCIT:R176
rank: 1000
is_a: genetically associated with
domain: disease or phenotypic feature
inherited: true
alias: condition_associated_with_gene
inverse: gene associated with condition
range: gene
multivalued: true

```
</details></div>