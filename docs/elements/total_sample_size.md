---
search:
  boost: 5.0
---

# Slot: total_sample_size 


_The total number of patients or participants within a sample population._



<div data-search-exclude markdown="1">



URI: [namo:total_sample_size](https://w3id.org/monarch-initiative/namo/total_sample_size)
Alias: total_sample_size


## Inheritance

* [association_slot](association_slot.md)
    * [dataset_count](dataset_count.md)
        * **total_sample_size**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IceesStudyResult](IceesStudyResult.md) | A study result that represents a result, from a supporting Study, which is sp... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain | [Association](Association.md) |
| Domain Of | [IceesStudyResult](IceesStudyResult.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:total_sample_size |
| native | namo:total_sample_size |




## LinkML Source

<details>
```yaml
name: total sample size
description: The total number of patients or participants within a sample population.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: dataset count
domain: association
alias: total_sample_size
domain_of:
- icees study result
range: integer

```
</details></div>