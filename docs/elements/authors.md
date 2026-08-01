---
search:
  boost: 5.0
---

# Slot: authors 


_Authors of the publication_



<div data-search-exclude markdown="1">



URI: [namo:authors](https://w3id.org/monarch-initiative/namo/authors)
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
| Multivalued | Yes |
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
| self | namo:authors |
| native | namo:authors |




## LinkML Source

<details>
```yaml
name: authors
description: Authors of the publication
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: Reference
domain_of:
- Reference
range: string
multivalued: true

```
</details></div>