---
search:
  boost: 5.0
---

# Slot: log_odds_ratio_95_ci 


_The ninety-five percent confidence range in which the true log odds ratio for the sample population falls. To calculate the 95% confidence interval (CI) for a log odds ratio (a pair of numbers), you need the standard error (SE) of the log odds ratio.  This interval helps you understand the precision of your estimate and whether the association is statistically significant._



<div data-search-exclude markdown="1">



URI: [namo:log_odds_ratio_95_ci](https://w3id.org/monarch-initiative/namo/log_odds_ratio_95_ci)
Alias: log_odds_ratio_95_ci


## Inheritance

* [association_slot](association_slot.md)
    * **log_odds_ratio_95_ci**






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
| Multivalued | Yes |









## Examples

| Value |
| --- |
| [0.6996904681742875, 1.6429124024089072] |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:log_odds_ratio_95_ci |
| native | namo:log_odds_ratio_95_ci |




## LinkML Source

<details>
```yaml
name: log odds ratio 95 ci
description: The ninety-five percent confidence range in which the true log odds ratio
  for the sample population falls. To calculate the 95% confidence interval (CI) for
  a log odds ratio (a pair of numbers), you need the standard error (SE) of the log
  odds ratio.  This interval helps you understand the precision of your estimate and
  whether the association is statistically significant.
examples:
- value: '[0.6996904681742875, 1.6429124024089072]'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: log_odds_ratio_95_ci
domain_of:
- icees study result
range: float
multivalued: true

```
</details></div>