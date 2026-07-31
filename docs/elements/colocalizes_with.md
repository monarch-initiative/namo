---
search:
  boost: 5.0
---

# Slot: colocalizes_with 


_holds between two entities that are observed to be located in the same place._



<div data-search-exclude markdown="1">



URI: [namo:colocalizes_with](https://w3id.org/monarch-initiative/namo/colocalizes_with)
Alias: colocalizes_with


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [coexists_with](coexists_with.md)
            * **colocalizes_with**








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
| self | namo:colocalizes_with |
| native | namo:colocalizes_with |
| exact | RO:0002325 |




## LinkML Source

<details>
```yaml
name: colocalizes with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two entities that are observed to be located in the same
  place.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002325
rank: 1000
is_a: coexists with
domain: named thing
inherited: true
alias: colocalizes_with
symmetric: true
range: named thing
multivalued: true

```
</details></div>