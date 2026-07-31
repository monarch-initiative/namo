---
search:
  boost: 5.0
---

# Slot: genetic_neighborhood_of 


_holds between two genes located nearby one another on a chromosome._



<div data-search-exclude markdown="1">



URI: [namo:genetic_neighborhood_of](https://w3id.org/monarch-initiative/namo/genetic_neighborhood_of)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [interacts_with](interacts_with.md)
            * [genetically_interacts_with](genetically_interacts_with.md)
                * **genetic_neighborhood_of**








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
| self | namo:genetic_neighborhood_of |
| native | namo:genetic_neighborhood_of |




## LinkML Source

<details>
```yaml
name: genetic_neighborhood_of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two genes located nearby one another on a chromosome.
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