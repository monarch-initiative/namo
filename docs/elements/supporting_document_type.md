---
search:
  boost: 5.0
---

# Slot: supporting_document_type 


_The document type (e.g., Journal Article, Case Study, Preprint) for the supporting document used in a Text Mining Result._



<div data-search-exclude markdown="1">



URI: [namo:supporting_document_type](https://w3id.org/monarch-initiative/namo/supporting_document_type)
Alias: supporting_document_type


## Inheritance

* [association_slot](association_slot.md)
    * **supporting_document_type**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TextMiningStudyResult](TextMiningStudyResult.md) | A study result that represents information extracted from text using natural ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Association](Association.md) |
| Domain Of | [TextMiningStudyResult](TextMiningStudyResult.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Journal Article |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:supporting_document_type |
| native | namo:supporting_document_type |




## LinkML Source

<details>
```yaml
name: supporting document type
description: The document type (e.g., Journal Article, Case Study, Preprint) for the
  supporting document used in a Text Mining Result.
examples:
- value: Journal Article
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: supporting_document_type
domain_of:
- text mining study result
range: string

```
</details></div>