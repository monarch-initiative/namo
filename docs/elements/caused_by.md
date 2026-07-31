---
search:
  boost: 5.0
---

# Slot: caused_by 


_holds between two entities where the occurrence, existence, or activity of one is caused by the occurrence or generation of the other_



<div data-search-exclude markdown="1">



URI: [namo:caused_by](https://w3id.org/monarch-initiative/namo/caused_by)
Alias: caused_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [contribution_from](contribution_from.md)
            * **caused_by**








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
| Inverse | [causes](causes.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)



## Aliases


* disease caused by disruption of
* disease has basis in dysfunction of
* realized in response to
* realized in response to stimulus




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:caused_by |
| native | namo:caused_by |
| exact | WIKIDATA_PROPERTY:P828 |
| narrow | RO:0001022, RO:0002608, RO:0004019, RO:0004020, RO:0004028, RO:0009501 |




## LinkML Source

<details>
```yaml
name: caused by
description: holds between two entities where the occurrence, existence, or activity
  of one is caused by the occurrence or generation of the other
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- disease caused by disruption of
- disease has basis in dysfunction of
- realized in response to
- realized in response to stimulus
exact_mappings:
- WIKIDATA_PROPERTY:P828
narrow_mappings:
- RO:0001022
- RO:0002608
- RO:0004019
- RO:0004020
- RO:0004028
- RO:0009501
rank: 1000
is_a: contribution from
domain: named thing
inherited: true
alias: caused_by
inverse: causes
range: named thing
multivalued: true

```
</details></div>