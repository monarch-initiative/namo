---
search:
  boost: 5.0
---

# Slot: molecular_descriptors 


_Types of molecular descriptors used (topological, electronic, etc.)_



<div data-search-exclude markdown="1">



URI: [namo:molecular_descriptors](https://w3id.org/monarch-initiative/namo/molecular_descriptors)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QSARModel](QSARModel.md) | Quantitative Structure-Activity Relationship models that predict chemical/bio... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [QSARModel](QSARModel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [QSARModel](QSARModel.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:molecular_descriptors |
| native | namo:molecular_descriptors |




## LinkML Source

<details>
```yaml
name: molecular_descriptors
description: Types of molecular descriptors used (topological, electronic, etc.)
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: QSARModel
domain_of:
- QSARModel
range: string
multivalued: true

```
</details></div>