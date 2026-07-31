---
search:
  boost: 5.0
---

# Slot: chi_squared_statistic 


_The chi-squared statistic measures how much observed data deviate from expected values under the null hypothesis._



<div data-search-exclude markdown="1">



URI: [namo:chi_squared_statistic](https://w3id.org/monarch-initiative/namo/chi_squared_statistic)
Alias: chi_squared_statistic


## Inheritance

* [association_slot](association_slot.md)
    * **chi_squared_statistic**






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
| 26.38523077566414 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:chi_squared_statistic |
| native | namo:chi_squared_statistic |
| exact | STATO:0000030 |




## LinkML Source

<details>
```yaml
name: chi squared statistic
description: The chi-squared statistic measures how much observed data deviate from
  expected values under the null hypothesis.
examples:
- value: '26.38523077566414'
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- STATO:0000030
rank: 1000
is_a: association slot
domain: association
alias: chi_squared_statistic
domain_of:
- icees study result
range: float

```
</details></div>