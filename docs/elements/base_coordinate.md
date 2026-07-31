---
search:
  boost: 5.0
---

# Slot: base_coordinate 


_A position in the base coordinate system.  Base coordinates start at position 1 instead of position 0._



<div data-search-exclude markdown="1">



URI: [namo:base_coordinate](https://w3id.org/monarch-initiative/namo/base_coordinate)
Alias: base_coordinate


## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * **base_coordinate**
            * [start_coordinate](start_coordinate.md)
            * [end_coordinate](end_coordinate.md)








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


* one-based
* fully-closed




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:base_coordinate |
| native | namo:base_coordinate |




## LinkML Source

<details>
```yaml
name: base coordinate
description: A position in the base coordinate system.  Base coordinates start at
  position 1 instead of position 0.
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- one-based
- fully-closed
rank: 1000
is_a: sequence localization attribute
domain: genomic sequence localization
alias: base_coordinate
range: integer

```
</details></div>