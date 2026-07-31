---
search:
  boost: 5.0
---

# Slot: supporting_text_section_type 


_The section of the supporting text of a Text Mining Result within the supporting document. This is in the form of the name of the document section (e.g., Abstract, Introduction) that contains the supporting text._



<div data-search-exclude markdown="1">



URI: [namo:supporting_text_section_type](https://w3id.org/monarch-initiative/namo/supporting_text_section_type)
Alias: supporting_text_section_type


## Inheritance

* [association_slot](association_slot.md)
    * **supporting_text_section_type**






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
| abstract |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:supporting_text_section_type |
| native | namo:supporting_text_section_type |




## LinkML Source

<details>
```yaml
name: supporting text section type
description: The section of the supporting text of a Text Mining Result within the
  supporting document. This is in the form of the name of the document section (e.g.,
  Abstract, Introduction) that contains the supporting text.
examples:
- value: abstract
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: supporting_text_section_type
domain_of:
- text mining study result
range: string

```
</details></div>