---
search:
  boost: 5.0
---

# Slot: dataset_count 


_The total number of instances in a dataset/cohort._



<div data-search-exclude markdown="1">



URI: [namo:dataset_count](https://w3id.org/monarch-initiative/namo/dataset_count)
Alias: dataset_count


## Inheritance

* [association_slot](association_slot.md)
    * **dataset_count**
        * [total_sample_size](total_sample_size.md)








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
| 100000 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:dataset_count |
| native | namo:dataset_count |




## LinkML Source

<details>
```yaml
name: dataset count
description: The total number of instances in a dataset/cohort.
examples:
- value: '100000'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: dataset_count
range: integer

```
</details></div>