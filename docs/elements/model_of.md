---
search:
  boost: 5.0
---

# Slot: model_of 


_holds between a thing and some other thing it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity._



<div data-search-exclude markdown="1">



URI: [namo:model_of](https://w3id.org/monarch-initiative/namo/model_of)
Alias: model_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **model_of**








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
| self | namo:model_of |
| native | namo:model_of |
| exact | RO:0003301 |
| narrow | FOODON:00001301 |




## LinkML Source

<details>
```yaml
name: model of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a thing and some other thing it approximates for purposes
  of scientific study, in virtue of its exhibiting similar features of the studied
  entity.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0003301
narrow_mappings:
- FOODON:00001301
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: model_of
range: named thing
multivalued: true

```
</details></div>