---
search:
  boost: 5.0
---

# Slot: feature_types 


_Types of features used (molecular, phenotypic, imaging, etc.)_



<div data-search-exclude markdown="1">



URI: [namo:feature_types](https://w3id.org/monarch-initiative/namo/feature_types)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MLModel](MLModel.md) | Machine Learning and AI-based models for prediction, mechanism inference, and... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FeatureTypeEnum](FeatureTypeEnum.md) |
| Domain Of | [MLModel](MLModel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MLModel](MLModel.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:feature_types |
| native | namo:feature_types |




## LinkML Source

<details>
```yaml
name: feature_types
description: Types of features used (molecular, phenotypic, imaging, etc.)
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: MLModel
domain_of:
- MLModel
range: FeatureTypeEnum
multivalued: true

```
</details></div>