---
search:
  boost: 5.0
---

# Slot: gene_fusion_with 


_holds between two independent genes that have fused through translocation, interstitial deletion, or chromosomal inversion to form a new, hybrid gene. Fusion genes are often implicated in various neoplasms and cancers._



<div data-search-exclude markdown="1">



URI: [namo:gene_fusion_with](https://w3id.org/monarch-initiative/namo/gene_fusion_with)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [interacts_with](interacts_with.md)
            * [genetically_interacts_with](genetically_interacts_with.md)
                * **gene_fusion_with**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Gene](Gene.md) |
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
| Symmetric | Yes |

</details>







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
| self | namo:gene_fusion_with |
| native | namo:gene_fusion_with |




## LinkML Source

<details>
```yaml
name: gene_fusion_with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two independent genes that have fused through translocation,
  interstitial deletion, or chromosomal inversion to form a new, hybrid gene. Fusion
  genes are often implicated in various neoplasms and cancers.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: genetically interacts with
domain: gene
inherited: true
symmetric: true
range: gene
multivalued: true

```
</details></div>