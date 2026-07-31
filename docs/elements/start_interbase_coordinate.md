---
search:
  boost: 5.0
---

# Slot: start_interbase_coordinate 


_The position at which the subject nucleic acid entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 0)._



<div data-search-exclude markdown="1">



URI: [namo:start_interbase_coordinate](https://w3id.org/monarch-initiative/namo/start_interbase_coordinate)
Alias: start_interbase_coordinate


## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * [interbase_coordinate](interbase_coordinate.md)
            * **start_interbase_coordinate**






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
| opposite_of | end interbase coordinate |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:start_interbase_coordinate |
| native | namo:start_interbase_coordinate |
| close | faldo:begin |




## LinkML Source

<details>
```yaml
name: start interbase coordinate
annotations:
  opposite_of:
    tag: opposite_of
    value: end interbase coordinate
description: 'The position at which the subject nucleic acid entity starts on the
  chromosome or other entity to which it is located on. (ie: the start of the sequence
  being referenced is 0).'
from_schema: https://w3id.org/monarch-initiative/namo
close_mappings:
- faldo:begin
rank: 1000
is_a: interbase coordinate
domain: genomic sequence localization
alias: start_interbase_coordinate
domain_of:
- genomic sequence localization
range: integer

```
</details></div>