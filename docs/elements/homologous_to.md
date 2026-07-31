---
search:
  boost: 5.0
---

# Slot: homologous_to 


_holds between two biological entities that have common evolutionary origin_



<div data-search-exclude markdown="1">



URI: [namo:homologous_to](https://w3id.org/monarch-initiative/namo/homologous_to)
Alias: homologous_to


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [similar_to](similar_to.md)
            * **homologous_to**
                * [paralogous_to](paralogous_to.md)
                * [orthologous_to](orthologous_to.md)
                * [xenologous_to](xenologous_to.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NamedThing](NamedThing.md) |
| Domain | [NamedThing](NamedThing.md) |

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



## Aliases


* in homology relationship with


## Comments

* typically used to describe homology relationships between genes or gene products



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
| self | namo:homologous_to |
| native | namo:homologous_to |
| exact | RO:HOM0000001, SIO:010302 |
| narrow | UBERON_CORE:sexually_homologous_to |




## LinkML Source

<details>
```yaml
name: homologous to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two biological entities that have common evolutionary origin
comments:
- typically used to describe homology relationships between genes or gene products
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- in homology relationship with
exact_mappings:
- RO:HOM0000001
- SIO:010302
narrow_mappings:
- UBERON_CORE:sexually_homologous_to
rank: 1000
is_a: similar to
domain: named thing
inherited: true
alias: homologous_to
symmetric: true
range: named thing
multivalued: true

```
</details></div>