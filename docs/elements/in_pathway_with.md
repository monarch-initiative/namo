---
search:
  boost: 5.0
---

# Slot: in_pathway_with 


_holds between two genes or gene products that are part of in the same biological pathway_



<div data-search-exclude markdown="1">



URI: [namo:in_pathway_with](https://w3id.org/monarch-initiative/namo/in_pathway_with)
Alias: in_pathway_with


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [coexists_with](coexists_with.md)
            * **in_pathway_with**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeneOrGeneProduct](GeneOrGeneProduct.md) |
| Domain | [GeneOrGeneProduct](GeneOrGeneProduct.md) |

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
| self | namo:in_pathway_with |
| native | namo:in_pathway_with |
| related | SIO:010532 |




## LinkML Source

<details>
```yaml
name: in pathway with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two genes or gene products that are part of in the same
  biological pathway
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
related_mappings:
- SIO:010532
rank: 1000
is_a: coexists with
domain: gene or gene product
inherited: true
alias: in_pathway_with
symmetric: true
range: gene or gene product
multivalued: true

```
</details></div>