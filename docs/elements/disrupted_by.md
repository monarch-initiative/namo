---
search:
  boost: 5.0
---

# Slot: disrupted_by 


_describes a relationship where the structure, function, or occurrence of one entity is degraded or interfered with by another._



<div data-search-exclude markdown="1">



URI: [namo:disrupted_by](https://w3id.org/monarch-initiative/namo/disrupted_by)
Alias: disrupted_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affected_by](affected_by.md)
            * **disrupted_by**








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
| Inverse | [disrupts](disrupts.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:disrupted_by |
| native | namo:disrupted_by |




## LinkML Source

<details>
```yaml
name: disrupted by
description: describes a relationship where the structure, function, or occurrence
  of one entity is degraded or interfered with by another.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: affected by
domain: named thing
inherited: true
alias: disrupted_by
inverse: disrupts
range: named thing
multivalued: true

```
</details></div>