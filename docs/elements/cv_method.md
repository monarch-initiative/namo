---
search:
  boost: 5.0
---

# Slot: cv_method 


_Type of cross-validation used_



<div data-search-exclude markdown="1">



URI: [namo:cv_method](https://w3id.org/monarch-initiative/namo/cv_method)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CrossValidation](CrossValidation.md) | Cross-validation strategy and results for ML models |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CrossValidationMethodEnum](CrossValidationMethodEnum.md) |
| Domain Of | [CrossValidation](CrossValidation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CrossValidation](CrossValidation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:cv_method |
| native | namo:cv_method |




## LinkML Source

<details>
```yaml
name: cv_method
description: Type of cross-validation used
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: CrossValidation
domain_of:
- CrossValidation
range: CrossValidationMethodEnum

```
</details></div>