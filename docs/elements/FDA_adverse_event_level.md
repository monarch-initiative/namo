---
search:
  boost: 5.0
---

# Slot: FDA_adverse_event_level 


_The level or severity grade of an adverse event as classified by FDA adverse-event terminology, drawn from FDAIDAAdverseEventEnum; used on adverse-event associations._



<div data-search-exclude markdown="1">



URI: [namo:FDA_adverse_event_level](https://w3id.org/monarch-initiative/namo/FDA_adverse_event_level)
Alias: FDA_adverse_event_level


## Inheritance

* [association_slot](association_slot.md)
    * **FDA_adverse_event_level**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FDAIDAAdverseEventEnum](FDAIDAAdverseEventEnum.md) |
| Domain | [Association](Association.md) |
| Domain Of | [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:FDA_adverse_event_level |
| native | namo:FDA_adverse_event_level |




## LinkML Source

<details>
```yaml
name: FDA adverse event level
description: The level or severity grade of an adverse event as classified by FDA
  adverse-event terminology, drawn from FDAIDAAdverseEventEnum; used on adverse-event
  associations.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: FDA_adverse_event_level
domain_of:
- chemical or drug or treatment adverse event association
range: FDAIDAAdverseEventEnum

```
</details></div>