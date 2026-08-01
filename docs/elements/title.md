---
search:
  boost: 5.0
---

# Slot: title 


_Title of the referenced publication or dataset_



<div data-search-exclude markdown="1">



URI: [namo:title](https://w3id.org/monarch-initiative/namo/title)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Reference](Reference.md) | A literature reference with identifier and title for citing published work |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Reference](Reference.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Reference](Reference.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:title |
| native | namo:title |




## LinkML Source

<details>
```yaml
name: title
description: Title of the referenced publication or dataset
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: Reference
domain_of:
- Reference
range: string
required: true

```
</details></div>