---
search:
  boost: 5.0
---

# Slot: mentioned_by 


_refers to is a relation between one named thing and the information content entity that it makes reference to._



<div data-search-exclude markdown="1">



URI: [namo:mentioned_by](https://w3id.org/monarch-initiative/namo/mentioned_by)
Alias: mentioned_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **mentioned_by**








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
| Inverse | [mentions](mentions.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:mentioned_by |
| native | namo:mentioned_by |




## LinkML Source

<details>
```yaml
name: mentioned by
description: refers to is a relation between one named thing and the information content
  entity that it makes reference to.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: mentioned_by
inverse: mentions
range: named thing
multivalued: true

```
</details></div>