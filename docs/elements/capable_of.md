---
search:
  boost: 5.0
---

# Slot: capable_of 


_holds between a physical entity and process or function, where the continuant alone has the ability to carry out the process or function._



<div data-search-exclude markdown="1">



URI: [namo:capable_of](https://w3id.org/monarch-initiative/namo/capable_of)
Alias: capable_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [participates_in](participates_in.md)
            * [actively_involved_in](actively_involved_in.md)
                * **capable_of**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Occurrent](Occurrent.md) |
| Domain | [NamedThing](NamedThing.md) |

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
| self | namo:capable_of |
| native | namo:capable_of |
| exact | RO:0002215 |
| narrow | NCIT:R52, RO:0002500 |




## LinkML Source

<details>
```yaml
name: capable of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a physical entity and process or function, where the continuant
  alone has the ability to carry out the process or function.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002215
narrow_mappings:
- NCIT:R52
- RO:0002500
rank: 1000
is_a: actively involved in
domain: named thing
inherited: true
alias: capable_of
range: occurrent
multivalued: true

```
</details></div>