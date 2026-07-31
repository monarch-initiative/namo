---
search:
  boost: 5.0
---

# Slot: subject_location_in_text 


_Character offsets for the text span(s) in the supporting text corresponding to the subject concept of the extracted assertion._



<div data-search-exclude markdown="1">



URI: [namo:subject_location_in_text](https://w3id.org/monarch-initiative/namo/subject_location_in_text)
Alias: subject_location_in_text


## Inheritance

* [association_slot](association_slot.md)
    * **subject_location_in_text**






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
| Multivalued | Yes |









## Examples

| Value |
| --- |
| 33 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:subject_location_in_text |
| native | namo:subject_location_in_text |




## LinkML Source

<details>
```yaml
name: subject location in text
description: Character offsets for the text span(s) in the supporting text corresponding
  to the subject concept of the extracted assertion.
examples:
- value: '33'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: subject_location_in_text
domain_of:
- text mining study result
range: integer
multivalued: true

```
</details></div>