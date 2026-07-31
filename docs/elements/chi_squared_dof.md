---
search:
  boost: 5.0
---

# Slot: chi_squared_dof 


_Degrees of freedom (dof) in a chi-squared test referring to the number of values in the final calculation of a statistic that are free to vary_



<div data-search-exclude markdown="1">



URI: [namo:chi_squared_dof](https://w3id.org/monarch-initiative/namo/chi_squared_dof)
Alias: chi_squared_dof


## Inheritance

* [association_slot](association_slot.md)
    * **chi_squared_dof**






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









## Examples

| Value |
| --- |
| 1 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:chi_squared_dof |
| native | namo:chi_squared_dof |




## LinkML Source

<details>
```yaml
name: chi squared dof
description: Degrees of freedom (dof) in a chi-squared test referring to the number
  of values in the final calculation of a statistic that are free to vary
examples:
- value: '1'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: chi_squared_dof
domain_of:
- icees study result
range: integer

```
</details></div>