---
search:
  boost: 5.0
---

# Slot: has_member 


_Defines a mereological relation between a collection and an item._



<div data-search-exclude markdown="1">



URI: [namo:has_member](https://w3id.org/monarch-initiative/namo/has_member)
Alias: has_member


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * **has_member**








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








## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_member |
| native | namo:has_member |
| exact | RO:0002351, skos:member |




## LinkML Source

<details>
```yaml
name: has member
description: Defines a mereological relation between a collection and an item.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002351
- skos:member
rank: 1000
is_a: related to at concept level
domain: named thing
inherited: true
alias: has_member
range: named thing
multivalued: true

```
</details></div>