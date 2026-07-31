---
search:
  boost: 5.0
---

# Slot: composed_primarily_of 


_x composed_primarily_of_y if:more than half of the mass of x is made from parts of y._



<div data-search-exclude markdown="1">



URI: [namo:composed_primarily_of](https://w3id.org/monarch-initiative/namo/composed_primarily_of)
Alias: composed_primarily_of


## Inheritance

* [related_to](related_to.md)
    * **composed_primarily_of**








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
| self | namo:composed_primarily_of |
| native | namo:composed_primarily_of |
| exact | RO:0002473 |




## LinkML Source

<details>
```yaml
name: composed primarily of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: x composed_primarily_of_y if:more than half of the mass of x is made
  from parts of y.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002473
rank: 1000
is_a: related to
domain: named thing
inherited: true
alias: composed_primarily_of
range: named thing
multivalued: true

```
</details></div>