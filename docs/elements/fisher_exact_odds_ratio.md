---
search:
  boost: 5.0
---

# Slot: fisher_exact_odds_ratio 


_The Fisher Exact Test is used to determine whether there is a non-random association between two categorical variables in a 2×2 contingency table, especially when sample sizes are small. The odds ratio (OR) quantifies the strength of that association._

_   OR = 1 implies No association_

_   OR > 1 implies Positive association (Group A more likely to have Outcome 1)_

_   OR < 1 implies Negative association (Group A less likely to have Outcome 1)_



<div data-search-exclude markdown="1">



URI: [namo:fisher_exact_odds_ratio](https://w3id.org/monarch-initiative/namo/fisher_exact_odds_ratio)
Alias: fisher_exact_odds_ratio


## Inheritance

* [association_slot](association_slot.md)
    * **fisher_exact_odds_ratio**






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
| 3.226188583240579 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:fisher_exact_odds_ratio |
| native | namo:fisher_exact_odds_ratio |




## LinkML Source

<details>
```yaml
name: fisher exact odds ratio
description: "The Fisher Exact Test is used to determine whether there is a non-random\
  \ association between two categorical variables in a 2×2 contingency table, especially\
  \ when sample sizes are small. The odds ratio (OR) quantifies the strength of that\
  \ association.\n   OR = 1 implies No association\n   OR > 1 implies Positive association\
  \ (Group A more likely to have Outcome 1)\n   OR < 1 implies Negative association\
  \ (Group A less likely to have Outcome 1)"
examples:
- value: '3.226188583240579'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: fisher_exact_odds_ratio
domain_of:
- icees study result
range: float

```
</details></div>