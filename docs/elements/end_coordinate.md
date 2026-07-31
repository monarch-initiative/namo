---
search:
  boost: 5.0
---

# Slot: end_coordinate 


_The position at which the subject genomic entity ends on the chromosome or other entity to which it is located on._



<div data-search-exclude markdown="1">



URI: [namo:end_coordinate](https://w3id.org/monarch-initiative/namo/end_coordinate)
Alias: end_coordinate


## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * [base_coordinate](base_coordinate.md)
            * **end_coordinate**








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


* end




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:end_coordinate |
| native | namo:end_coordinate |
| exact | gff3:end |
| close | faldo:end |




## LinkML Source

<details>
```yaml
name: end coordinate
description: The position at which the subject genomic entity ends on the chromosome
  or other entity to which it is located on.
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- end
exact_mappings:
- gff3:end
close_mappings:
- faldo:end
rank: 1000
is_a: base coordinate
domain: genomic sequence localization
alias: end_coordinate
range: integer

```
</details></div>