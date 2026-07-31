---
search:
  boost: 5.0
---

# Slot: concept_pair_count 


_The number of instances in a dataset/cohort whose records contain both the subject and object concept of an association._



<div data-search-exclude markdown="1">



URI: [namo:concept_pair_count](https://w3id.org/monarch-initiative/namo/concept_pair_count)
Alias: concept_pair_count


## Inheritance

* [association_slot](association_slot.md)
    * **concept_pair_count**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain | [Association](Association.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 1731 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:concept_pair_count |
| native | namo:concept_pair_count |




## LinkML Source

<details>
```yaml
name: concept pair count
description: The number of instances in a dataset/cohort whose records contain both
  the subject and object concept of an association.
examples:
- value: '1731'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: concept_pair_count
range: integer

```
</details></div>