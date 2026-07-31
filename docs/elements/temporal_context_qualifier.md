---
search:
  boost: 5.0
---

# Slot: temporal_context_qualifier 


_a constraint of time placed upon the truth value of an association. for time intervales, use temporal interval qualifier._



<div data-search-exclude markdown="1">



URI: [namo:temporal_context_qualifier](https://w3id.org/monarch-initiative/namo/temporal_context_qualifier)
Alias: temporal_context_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **temporal_context_qualifier**
            * [temporal_interval_qualifier](temporal_interval_qualifier.md)






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | An association between an exposure event and an outcome |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TimeType](TimeType.md) |
| Domain | [Association](Association.md) |
| Domain Of | [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:temporal_context_qualifier |
| native | namo:temporal_context_qualifier |




## LinkML Source

<details>
```yaml
name: temporal context qualifier
description: a constraint of time placed upon the truth value of an association. for
  time intervales, use temporal interval qualifier.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: qualifier
domain: association
alias: temporal_context_qualifier
domain_of:
- exposure event to outcome association
range: time type

```
</details></div>