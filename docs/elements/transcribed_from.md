---
search:
  boost: 5.0
---

# Slot: transcribed_from 


_x is transcribed from y if and only if x is synthesized from template y_



<div data-search-exclude markdown="1">



URI: [namo:transcribed_from](https://w3id.org/monarch-initiative/namo/transcribed_from)
Alias: transcribed_from


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **transcribed_from**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Gene](Gene.md) |
| Domain | [Transcript](Transcript.md) |

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
| self | namo:transcribed_from |
| native | namo:transcribed_from |
| exact | RO:0002510, SIO:010081 |




## LinkML Source

<details>
```yaml
name: transcribed from
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: x is transcribed from y if and only if x is synthesized from template
  y
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002510
- SIO:010081
rank: 1000
is_a: related to at instance level
domain: transcript
inherited: true
alias: transcribed_from
range: gene
multivalued: true

```
</details></div>