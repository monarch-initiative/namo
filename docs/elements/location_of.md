---
search:
  boost: 5.0
---

# Slot: location_of 


_holds between material entity or site and a material entity that is located within it (but not considered a part of it)_



<div data-search-exclude markdown="1">



URI: [namo:location_of](https://w3id.org/monarch-initiative/namo/location_of)
Alias: location_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **location_of**
            * [expresses](expresses.md)








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
| Inverse | [located_in](located_in.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)



## Aliases


* site of




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:location_of |
| native | namo:location_of |
| exact | RO:0001015, SEMMEDDB:LOCATION_OF, WIKIDATA_PROPERTY:P276, FMA:location_of |
| narrow | SNOMED:inherent_location_of, NCIT:Anatomic_Structure_Has_Location_Role |




## LinkML Source

<details>
```yaml
name: location of
description: holds between material entity or site and a material entity that is located
  within it (but not considered a part of it)
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- site of
exact_mappings:
- RO:0001015
- SEMMEDDB:LOCATION_OF
- WIKIDATA_PROPERTY:P276
- FMA:location_of
narrow_mappings:
- SNOMED:inherent_location_of
- NCIT:Anatomic_Structure_Has_Location_Role
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: location_of
inverse: located in
range: named thing
multivalued: true

```
</details></div>