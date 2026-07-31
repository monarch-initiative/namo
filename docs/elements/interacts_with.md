---
search:
  boost: 5.0
---

# Slot: interacts_with 


_holds between any two entities that directly or indirectly interact with each other_



<div data-search-exclude markdown="1">



URI: [namo:interacts_with](https://w3id.org/monarch-initiative/namo/interacts_with)
Alias: interacts_with


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **interacts_with**
            * [physically_interacts_with](physically_interacts_with.md) [ [interacts_with](interacts_with.md)]
            * [genetically_interacts_with](genetically_interacts_with.md)
            * [pharmacologically_interacts_with](pharmacologically_interacts_with.md)







## Mixin Usage

| mixed into | description | range | domain |
| --- | --- | --- | --- |
| [physically_interacts_with](physically_interacts_with.md) | holds between two entities that make physical contact as part of some interac... | None |  |
| [regulates](regulates.md) | A more specific form of affects, that implies the effect results from a biolo... | physical essence or occurrent |  |



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
| Mixin | Yes |


<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Symmetric | Yes |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)




## Notes

* Please use a more specific child predicate of interacts with, either physically interacts with or genetically interacts with or pharmacologically interacts with.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:interacts_with |
| native | namo:interacts_with |
| exact | SEMMEDDB:INTERACTS_WITH |




## LinkML Source

<details>
```yaml
name: interacts with
description: holds between any two entities that directly or indirectly interact with
  each other
notes:
- Please use a more specific child predicate of interacts with, either physically
  interacts with or genetically interacts with or pharmacologically interacts with.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- SEMMEDDB:INTERACTS_WITH
rank: 1000
is_a: related to at instance level
mixin: true
domain: named thing
inherited: true
alias: interacts_with
symmetric: true
range: named thing
multivalued: true

```
</details></div>