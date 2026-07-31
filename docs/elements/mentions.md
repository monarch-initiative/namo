---
search:
  boost: 5.0
---

# Slot: mentions 


_refers to is a relation between one information content entity and the named thing that it makes reference to._



<div data-search-exclude markdown="1">



URI: [namo:mentions](https://w3id.org/monarch-initiative/namo/mentions)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **mentions**








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












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:mentions |
| native | namo:mentions |
| exact | IAO:0000142 |
| narrow | SIO:000628 |




## LinkML Source

<details>
```yaml
name: mentions
description: refers to is a relation between one information content entity and the
  named thing that it makes reference to.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- IAO:0000142
narrow_mappings:
- SIO:000628
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
range: named thing
multivalued: true

```
</details></div>