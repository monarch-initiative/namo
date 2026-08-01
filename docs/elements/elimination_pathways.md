---
search:
  boost: 5.0
---

# Slot: elimination_pathways 


_Drug elimination and metabolism pathways included_



<div data-search-exclude markdown="1">



URI: [namo:elimination_pathways](https://w3id.org/monarch-initiative/namo/elimination_pathways)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PBPKModel](PBPKModel.md) | Physiologically Based Pharmacokinetic models that simulate drug  absorption, ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PBPKModel](PBPKModel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PBPKModel](PBPKModel.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:elimination_pathways |
| native | namo:elimination_pathways |




## LinkML Source

<details>
```yaml
name: elimination_pathways
description: Drug elimination and metabolism pathways included
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: PBPKModel
domain_of:
- PBPKModel
range: string
multivalued: true

```
</details></div>