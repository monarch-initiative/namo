---
search:
  boost: 5.0
---

# Slot: population_context_qualifier 


_a biological population (general, study, cohort, etc.) with a specific set of characteristics to constrain an association._



<div data-search-exclude markdown="1">



URI: [namo:population_context_qualifier](https://w3id.org/monarch-initiative/namo/population_context_qualifier)
Alias: population_context_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **population_context_qualifier**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | An association in which the subject entity is linked to the likelihood of the... |  no  |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | An association between an exposure event and an outcome |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) |
| Domain | [Association](Association.md) |
| Domain Of | [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md), [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:population_context_qualifier |
| native | namo:population_context_qualifier |




## LinkML Source

<details>
```yaml
name: population context qualifier
description: a biological population (general, study, cohort, etc.) with a specific
  set of characteristics to constrain an association.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: qualifier
domain: association
alias: population_context_qualifier
domain_of:
- named thing associated with likelihood of named thing association
- exposure event to outcome association
range: population of individual organisms

```
</details></div>