---
search:
  boost: 5.0
---

# Slot: number_of_cases 


_The number of cases in a study or clinical trial, primarily used in conversion of drug approval data._



<div data-search-exclude markdown="1">



URI: [namo:number_of_cases](https://w3id.org/monarch-initiative/namo/number_of_cases)
Alias: number_of_cases


## Inheritance

* [node_property](node_property.md)
    * [aggregate_statistic](aggregate_statistic.md)
        * [has_count](has_count.md)
            * **number_of_cases**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | An association between any entity and a disease, capturing clinical context s... |  no  |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | An association between any entity and a phenotypic feature, capturing clinica... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain | [NamedThing](NamedThing.md) |
| Domain Of | [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md), [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:number_of_cases |
| native | namo:number_of_cases |




## LinkML Source

<details>
```yaml
name: number of cases
description: The number of cases in a study or clinical trial, primarily used in conversion
  of drug approval data.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: has count
domain: named thing
alias: number_of_cases
domain_of:
- entity to disease association
- entity to phenotypic feature association
range: integer

```
</details></div>