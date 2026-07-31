---
search:
  boost: 5.0
---

# Slot: fisher_exact_p 


_The Fisher exact p-value tells you the probability of observing a table as extreme as (or more extreme than) your actual data, assuming that the null hypothesis of independence is true. It's most commonly used for 2×2 contingency tables, especially when sample sizes are small or expected counts are low._



<div data-search-exclude markdown="1">



URI: [namo:fisher_exact_p](https://w3id.org/monarch-initiative/namo/fisher_exact_p)
Alias: fisher_exact_p


## Inheritance

* [association_slot](association_slot.md)
    * **fisher_exact_p**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IceesStudyResult](IceesStudyResult.md) | A study result that represents a result, from a supporting Study, which is sp... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain | [Association](Association.md) |
| Domain Of | [IceesStudyResult](IceesStudyResult.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 2.8581244515361156e-06 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:fisher_exact_p |
| native | namo:fisher_exact_p |




## LinkML Source

<details>
```yaml
name: fisher exact p
description: The Fisher exact p-value tells you the probability of observing a table
  as extreme as (or more extreme than) your actual data, assuming that the null hypothesis
  of independence is true. It's most commonly used for 2×2 contingency tables, especially
  when sample sizes are small or expected counts are low.
examples:
- value: '2.8581244515361156e-06'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: fisher_exact_p
domain_of:
- icees study result
range: float

```
</details></div>