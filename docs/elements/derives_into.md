---
search:
  boost: 5.0
---

# Slot: derives_into 


_holds between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity_



<div data-search-exclude markdown="1">



URI: [namo:derives_into](https://w3id.org/monarch-initiative/namo/derives_into)
Alias: derives_into


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **derives_into**
            * [has_metabolite](has_metabolite.md)








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
| Inverse | [derives_from](derives_from.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)



## Aliases


* is normal cell origin of disease
* may be normal cell origin of disease




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:derives_into |
| native | namo:derives_into |
| exact | RO:0001001, SEMMEDDB:CONVERTS_TO, FMA:derives |




## LinkML Source

<details>
```yaml
name: derives into
description: holds between two distinct material entities, the old entity and the
  new entity, in which the new entity begins to exist when the old entity ceases to
  exist, and the new entity inherits the significant portion of the matter of the
  old entity
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- is normal cell origin of disease
- may be normal cell origin of disease
exact_mappings:
- RO:0001001
- SEMMEDDB:CONVERTS_TO
- FMA:derives
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: derives_into
inverse: derives from
range: named thing
multivalued: true

```
</details></div>