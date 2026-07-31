---
search:
  boost: 5.0
---

# Slot: has_gene_product 


_holds between a gene and a transcribed and/or translated product generated from it_



<div data-search-exclude markdown="1">



URI: [namo:has_gene_product](https://w3id.org/monarch-initiative/namo/has_gene_product)
Alias: has_gene_product


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_gene_product**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeneProductMixin](GeneProductMixin.md) |
| Domain | [Gene](Gene.md) |

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
| Inverse | [gene_product_of](gene_product_of.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_gene_product |
| native | namo:has_gene_product |
| exact | RO:0002205, WIKIDATA_PROPERTY:P688, NCIT:gene_encodes_gene_product |
| narrow | NCIT:R178 |
| close | PR:has_gene_template |




## LinkML Source

<details>
```yaml
name: has gene product
description: holds between a gene and a transcribed and/or translated product generated
  from it
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002205
- WIKIDATA_PROPERTY:P688
- NCIT:gene_encodes_gene_product
close_mappings:
- PR:has_gene_template
narrow_mappings:
- NCIT:R178
rank: 1000
is_a: related to at instance level
domain: gene
inherited: true
alias: has_gene_product
inverse: gene product of
range: gene product mixin
multivalued: true

```
</details></div>