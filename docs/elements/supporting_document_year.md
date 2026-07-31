---
search:
  boost: 5.0
---

# Slot: supporting_document_year 


_The document year (typically the publication year) for the supporting document used in a Text Mining Result._



<div data-search-exclude markdown="1">



URI: [namo:supporting_document_year](https://w3id.org/monarch-initiative/namo/supporting_document_year)
Alias: supporting_document_year


## Inheritance

* [association_slot](association_slot.md)
    * **supporting_document_year**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TextMiningStudyResult](TextMiningStudyResult.md) | A study result that represents information extracted from text using natural ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain | [Association](Association.md) |
| Domain Of | [TextMiningStudyResult](TextMiningStudyResult.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 2018 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:supporting_document_year |
| native | namo:supporting_document_year |




## LinkML Source

<details>
```yaml
name: supporting document year
description: The document year (typically the publication year) for the supporting
  document used in a Text Mining Result.
examples:
- value: '2018'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: supporting_document_year
domain_of:
- text mining study result
range: integer

```
</details></div>