---
search:
  boost: 5.0
---

# Slot: actively_involves 

<div data-search-exclude markdown="1">



URI: [namo:actively_involves](https://w3id.org/monarch-initiative/namo/actively_involves)
Alias: actively_involves


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_participant](has_participant.md)
            * **actively_involves**
                * [can_be_carried_out_by](can_be_carried_out_by.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NamedThing](NamedThing.md) |
| Domain | [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) |

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
| Inverse | [actively_involved_in](actively_involved_in.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:actively_involves |
| native | namo:actively_involves |




## LinkML Source

<details>
```yaml
name: actively involves
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: has participant
domain: biological process or activity
inherited: true
alias: actively_involves
inverse: actively involved in
range: named thing
multivalued: true

```
</details></div>