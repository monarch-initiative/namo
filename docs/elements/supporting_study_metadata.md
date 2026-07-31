---
search:
  boost: 5.0
---

# Slot: supporting_study_metadata 


_Information about a study used to generate information used as evidence to support the knowledge expressed in an Association. In practice, data creators should use one of the more specific subtypes of this property._



<div data-search-exclude markdown="1">


* __NOTE__: this is an abstract slot and should not be populated directly


URI: [namo:supporting_study_metadata](https://w3id.org/monarch-initiative/namo/supporting_study_metadata)
Alias: supporting_study_metadata


## Inheritance

* [association_slot](association_slot.md)
    * **supporting_study_metadata**
        * [supporting_study_method_types](supporting_study_method_types.md)
        * [supporting_study_method_description](supporting_study_method_description.md)
        * [supporting_study_size](supporting_study_size.md)
        * [supporting_study_cohort](supporting_study_cohort.md)
        * [supporting_study_date_range](supporting_study_date_range.md)
        * [supporting_study_context](supporting_study_context.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Association](Association.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |








## Comments

* This is an abstract slot that groups a set of concrete slots used to directly attach to an association information about a study that produced evidence used to generate the knowledge expressed in the edge.
* Note that these concrete 'supporting study metadata' slots are used only when a more normalized model that leverages the 'supporting studdies' slot and 'Study' class to link to and describe the Study itself are not possible or preferred, such that this study metadata must be captured directly on the edge.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:supporting_study_metadata |
| native | namo:supporting_study_metadata |




## LinkML Source

<details>
```yaml
name: supporting study metadata
description: Information about a study used to generate information used as evidence
  to support the knowledge expressed in an Association. In practice, data creators
  should use one of the more specific subtypes of this property.
comments:
- This is an abstract slot that groups a set of concrete slots used to directly attach
  to an association information about a study that produced evidence used to generate
  the knowledge expressed in the edge.
- Note that these concrete 'supporting study metadata' slots are used only when a
  more normalized model that leverages the 'supporting studdies' slot and 'Study'
  class to link to and describe the Study itself are not possible or preferred, such
  that this study metadata must be captured directly on the edge.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
abstract: true
domain: association
alias: supporting_study_metadata
range: string

```
</details></div>