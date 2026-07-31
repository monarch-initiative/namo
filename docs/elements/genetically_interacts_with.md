---
search:
  boost: 5.0
---

# Slot: genetically_interacts_with 


_holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality._



<div data-search-exclude markdown="1">



URI: [namo:genetically_interacts_with](https://w3id.org/monarch-initiative/namo/genetically_interacts_with)
Alias: genetically_interacts_with


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [interacts_with](interacts_with.md)
            * **genetically_interacts_with**
                * [gene_fusion_with](gene_fusion_with.md)
                * [genetic_neighborhood_of](genetic_neighborhood_of.md)








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
| self | namo:genetically_interacts_with |
| native | namo:genetically_interacts_with |
| exact | RO:0002435 |




## LinkML Source

<details>
```yaml
name: genetically interacts with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two genes whose phenotypic effects are dependent on each
  other in some way - such that their combined phenotypic effects are the result of
  some interaction between the activity of their gene products. Examples include epistasis
  and synthetic lethality.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002435
rank: 1000
is_a: interacts with
domain: gene
inherited: true
alias: genetically_interacts_with
symmetric: true
range: gene
multivalued: true

```
</details></div>