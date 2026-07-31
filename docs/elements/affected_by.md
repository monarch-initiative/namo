---
search:
  boost: 5.0
---

# Slot: affected_by 


_describes an entity of which the state or quality is affected by another existing entity._



<div data-search-exclude markdown="1">



URI: [namo:affected_by](https://w3id.org/monarch-initiative/namo/affected_by)
Alias: affected_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **affected_by**
            * [regulated_by](regulated_by.md)
            * [disrupted_by](disrupted_by.md)
            * [condition_ameliorated_by](condition_ameliorated_by.md)
            * [condition_exacerbated_by](condition_exacerbated_by.md)
            * [adverse_event_of](adverse_event_of.md)
            * [is_side_effect_of](is_side_effect_of.md)








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
| Inverse | [affects](affects.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:affected_by |
| native | namo:affected_by |




## LinkML Source

<details>
```yaml
name: affected by
description: describes an entity of which the state or quality is affected by another
  existing entity.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: affected_by
inverse: affects
range: named thing
multivalued: true

```
</details></div>