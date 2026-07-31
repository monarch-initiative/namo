---
search:
  boost: 5.0
---

# Slot: start_coordinate 


_The position at which the subject genomic entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 1)._



<div data-search-exclude markdown="1">



URI: [namo:start_coordinate](https://w3id.org/monarch-initiative/namo/start_coordinate)
Alias: start_coordinate


## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * [base_coordinate](base_coordinate.md)
            * **start_coordinate**








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


* start




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:start_coordinate |
| native | namo:start_coordinate |
| exact | gff3:start |
| close | faldo:begin |




## LinkML Source

<details>
```yaml
name: start coordinate
description: 'The position at which the subject genomic entity starts on the chromosome
  or other entity to which it is located on. (ie: the start of the sequence being
  referenced is 1).'
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- start
exact_mappings:
- gff3:start
close_mappings:
- faldo:begin
rank: 1000
is_a: base coordinate
domain: genomic sequence localization
alias: start_coordinate
range: integer

```
</details></div>