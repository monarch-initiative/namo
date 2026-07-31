---
search:
  boost: 5.0
---

# Slot: extraction_confidence_score 


_A quantitative confidence value that represents the probability of obtaining a result at least as extreme as that actually obtained, assuming that the actual value was the result of chance alone._



<div data-search-exclude markdown="1">



URI: [namo:extraction_confidence_score](https://w3id.org/monarch-initiative/namo/extraction_confidence_score)
Alias: extraction_confidence_score


## Inheritance

* [association_slot](association_slot.md)
    * **extraction_confidence_score**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TextMiningStudyResult](TextMiningStudyResult.md) | A study result that represents information extracted from text using natural ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain | [Association](Association.md) |
| Domain Of | [TextMiningStudyResult](TextMiningStudyResult.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 0.6188385904738642 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:extraction_confidence_score |
| native | namo:extraction_confidence_score |




## LinkML Source

<details>
```yaml
name: extraction confidence score
description: A quantitative confidence value that represents the probability of obtaining
  a result at least as extreme as that actually obtained, assuming that the actual
  value was the result of chance alone.
examples:
- value: '0.6188385904738642'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: extraction_confidence_score
domain_of:
- text mining study result
range: float

```
</details></div>