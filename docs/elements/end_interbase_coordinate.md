---
search:
  boost: 5.0
---

# Slot: end_interbase_coordinate 


_The position at which the subject nucleic acid entity ends on the chromosome or other entity to which it is located on._



<div data-search-exclude markdown="1">



URI: [namo:end_interbase_coordinate](https://w3id.org/monarch-initiative/namo/end_interbase_coordinate)
Alias: end_interbase_coordinate


## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * [interbase_coordinate](interbase_coordinate.md)
            * **end_interbase_coordinate**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | A relationship between a sequence feature and a nucleic acid entity it is loc... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain | [GenomicSequenceLocalization](GenomicSequenceLocalization.md) |
| Domain Of | [GenomicSequenceLocalization](GenomicSequenceLocalization.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| opposite_of | start interbase coordinate |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:end_interbase_coordinate |
| native | namo:end_interbase_coordinate |
| close | faldo:end |




## LinkML Source

<details>
```yaml
name: end interbase coordinate
annotations:
  opposite_of:
    tag: opposite_of
    value: start interbase coordinate
description: The position at which the subject nucleic acid entity ends on the chromosome
  or other entity to which it is located on.
from_schema: https://w3id.org/monarch-initiative/namo
close_mappings:
- faldo:end
rank: 1000
is_a: interbase coordinate
domain: genomic sequence localization
alias: end_interbase_coordinate
domain_of:
- genomic sequence localization
range: integer

```
</details></div>