---
search:
  boost: 5.0
---

# Slot: contributes_to 


_holds between two entities where the occurrence, existence, or activity of one contributes to the occurrence or generation of the other_



<div data-search-exclude markdown="1">



URI: [namo:contributes_to](https://w3id.org/monarch-initiative/namo/contributes_to)
Alias: contributes_to


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **contributes_to**
            * [causes](causes.md)








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
| self | namo:contributes_to |
| native | namo:contributes_to |
| exact | RO:0002326 |
| narrow | CTD:marker_mechanism, MONDO:predisposes_towards, RO:0002255, RO:0003304 |
| close | IDO:0000664 |




## LinkML Source

<details>
```yaml
name: contributes to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two entities where the occurrence, existence, or activity
  of one contributes to the occurrence or generation of the other
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002326
close_mappings:
- IDO:0000664
narrow_mappings:
- CTD:marker_mechanism
- MONDO:predisposes_towards
- RO:0002255
- RO:0003304
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: contributes_to
range: named thing
multivalued: true

```
</details></div>