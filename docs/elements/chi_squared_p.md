---
search:
  boost: 5.0
---

# Slot: chi_squared_p 


_The chi-square p-value tells you the probability that the observed differences (or associations) in your data occurred by random chance, assuming the null hypothesis is true._



<div data-search-exclude markdown="1">



URI: [namo:chi_squared_p](https://w3id.org/monarch-initiative/namo/chi_squared_p)
Alias: chi_squared_p


## Inheritance

* [association_slot](association_slot.md)
    * **chi_squared_p**






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
| 2.7967079822744063e-07 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:chi_squared_p |
| native | namo:chi_squared_p |




## LinkML Source

<details>
```yaml
name: chi squared p
description: The chi-square p-value tells you the probability that the observed differences
  (or associations) in your data occurred by random chance, assuming the null hypothesis
  is true.
examples:
- value: '2.7967079822744063e-07'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: chi_squared_p
domain_of:
- icees study result
range: float

```
</details></div>