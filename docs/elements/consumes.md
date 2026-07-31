---
search:
  boost: 5.0
---

# Slot: consumes 


_Holds between a process and an entity that is taken in and depleted by the process; for example a metabolite consumed in a biochemical reaction._



<div data-search-exclude markdown="1">



URI: [namo:consumes](https://w3id.org/monarch-initiative/namo/consumes)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_participant](has_participant.md)
            * [has_input](has_input.md)
                * **consumes**








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



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:consumes |
| native | namo:consumes |
| narrow | RO:0004009 |




## LinkML Source

<details>
```yaml
name: consumes
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between a process and an entity that is taken in and depleted by
  the process; for example a metabolite consumed in a biochemical reaction.
from_schema: https://w3id.org/monarch-initiative/namo
narrow_mappings:
- RO:0004009
rank: 1000
is_a: has input
domain: named thing
inherited: true
range: named thing
multivalued: true

```
</details></div>