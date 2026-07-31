---
search:
  boost: 5.0
---

# Slot: similar_to 


_holds between an entity and some other entity with similar features._



<div data-search-exclude markdown="1">



URI: [namo:similar_to](https://w3id.org/monarch-initiative/namo/similar_to)
Alias: similar_to


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **similar_to**
            * [homologous_to](homologous_to.md)
            * [chemically_similar_to](chemically_similar_to.md)








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
| self | namo:similar_to |
| native | namo:similar_to |
| exact | RO:HOM0000000, SO:similar_to |




## LinkML Source

<details>
```yaml
name: similar to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between an entity and some other entity with similar features.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:HOM0000000
- SO:similar_to
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: similar_to
symmetric: true
range: named thing
multivalued: true

```
</details></div>