---
search:
  boost: 5.0
---

# Slot: develops_from 


_Holds between two entities where the first develops, by one or more developmental processes, from the second; for example a cell type developing from a precursor cell type or a tissue developing from an embryonic primordium. Corresponds to RO:0002202._



<div data-search-exclude markdown="1">



URI: [namo:develops_from](https://w3id.org/monarch-initiative/namo/develops_from)
Alias: develops_from


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **develops_from**








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
| self | namo:develops_from |
| native | namo:develops_from |
| exact | BTO:develops_from, DDANAT:develops_from, FMA:develops_from, RO:0002202 |
| narrow | RO:0002207, RO:0002225, RO:0002226 |
| close | RO:0002203, FMA:develops_into |




## LinkML Source

<details>
```yaml
name: develops from
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between two entities where the first develops, by one or more developmental
  processes, from the second; for example a cell type developing from a precursor
  cell type or a tissue developing from an embryonic primordium. Corresponds to RO:0002202.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- BTO:develops_from
- DDANAT:develops_from
- FMA:develops_from
- RO:0002202
close_mappings:
- RO:0002203
- FMA:develops_into
narrow_mappings:
- RO:0002207
- RO:0002225
- RO:0002226
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: develops_from
range: named thing
multivalued: true

```
</details></div>