---
search:
  boost: 5.0
---

# Slot: interbase_coordinate 


_A position in interbase coordinates. Interbase coordinates start at position 0 instead of position 1. This is applied to a sequence localization edge._



<div data-search-exclude markdown="1">



URI: [namo:interbase_coordinate](https://w3id.org/monarch-initiative/namo/interbase_coordinate)
Alias: interbase_coordinate


## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * **interbase_coordinate**
            * [start_interbase_coordinate](start_interbase_coordinate.md)
            * [end_interbase_coordinate](end_interbase_coordinate.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain | [GenomicSequenceLocalization](GenomicSequenceLocalization.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* zero-based
* half-open
* space-based




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:interbase_coordinate |
| native | namo:interbase_coordinate |




## LinkML Source

<details>
```yaml
name: interbase coordinate
description: A position in interbase coordinates. Interbase coordinates start at position
  0 instead of position 1. This is applied to a sequence localization edge.
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- zero-based
- half-open
- space-based
rank: 1000
is_a: sequence localization attribute
domain: genomic sequence localization
alias: interbase_coordinate
range: integer

```
</details></div>