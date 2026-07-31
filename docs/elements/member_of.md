---
search:
  boost: 5.0
---

# Slot: member_of 


_Defines a mereological relation between a item and a collection._



<div data-search-exclude markdown="1">



URI: [namo:member_of](https://w3id.org/monarch-initiative/namo/member_of)
Alias: member_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * **member_of**








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
| Inverse | [has_member](has_member.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:member_of |
| native | namo:member_of |
| exact | RO:0002350 |
| close | skos:member |




## LinkML Source

<details>
```yaml
name: member of
description: Defines a mereological relation between a item and a collection.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002350
close_mappings:
- skos:member
rank: 1000
is_a: related to at concept level
domain: named thing
inherited: true
alias: member_of
inverse: has member
range: named thing
multivalued: true

```
</details></div>