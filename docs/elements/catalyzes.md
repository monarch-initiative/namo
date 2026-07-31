---
search:
  boost: 5.0
---

# Slot: catalyzes 


_Holds between a macromolecular machine (typically an enzyme or ribozyme) and a biochemical reaction or process whose rate it accelerates, without itself being consumed, by lowering the activation energy._



<div data-search-exclude markdown="1">



URI: [namo:catalyzes](https://w3id.org/monarch-initiative/namo/catalyzes)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [participates_in](participates_in.md)
            * **catalyzes**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) |
| Domain | [Occurrent](Occurrent.md) |

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
| self | namo:catalyzes |
| native | namo:catalyzes |
| exact | RO:0002327 |




## LinkML Source

<details>
```yaml
name: catalyzes
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between a macromolecular machine (typically an enzyme or ribozyme)
  and a biochemical reaction or process whose rate it accelerates, without itself
  being consumed, by lowering the activation energy.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002327
rank: 1000
is_a: participates in
domain: occurrent
inherited: true
range: biological process or activity
multivalued: true

```
</details></div>