---
search:
  boost: 5.0
---

# Slot: actively_involved_in 


_holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes_



<div data-search-exclude markdown="1">



URI: [namo:actively_involved_in](https://w3id.org/monarch-initiative/namo/actively_involved_in)
Alias: actively_involved_in


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [participates_in](participates_in.md)
            * **actively_involved_in**
                * [capable_of](capable_of.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) |
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



## Aliases


* involved in




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
| self | namo:actively_involved_in |
| native | namo:actively_involved_in |
| exact | RO:0002331 |
| narrow | NBO-PROPERTY:by_means, orphanet:317348, orphanet:317349, orphanet:327767, RO:0002503 |




## LinkML Source

<details>
```yaml
name: actively involved in
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a continuant and a process or function, where the continuant
  actively contributes to part or all of the process or function it realizes
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- involved in
exact_mappings:
- RO:0002331
narrow_mappings:
- NBO-PROPERTY:by_means
- orphanet:317348
- orphanet:317349
- orphanet:327767
- RO:0002503
rank: 1000
is_a: participates in
domain: named thing
inherited: true
alias: actively_involved_in
range: biological process or activity
multivalued: true

```
</details></div>