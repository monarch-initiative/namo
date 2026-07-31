---
search:
  boost: 5.0
---

# Slot: enables 


_holds between a physical entity and a process, where the physical entity executes the process_



<div data-search-exclude markdown="1">



URI: [namo:enables](https://w3id.org/monarch-initiative/namo/enables)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [participates_in](participates_in.md)
            * **enables**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) |
| Domain | [PhysicalEntity](PhysicalEntity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |








## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






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
| self | namo:enables |
| native | namo:enables |
| exact | RO:0002327 |




## LinkML Source

<details>
```yaml
name: enables
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a physical entity and a process, where the physical entity
  executes the process
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002327
rank: 1000
is_a: participates in
domain: physical entity
inherited: true
range: biological process or activity
multivalued: true

```
</details></div>