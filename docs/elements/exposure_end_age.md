---
search:
  boost: 5.0
---

# Slot: exposure_end_age 


_Ending stage of an exposure event._



<div data-search-exclude markdown="1">



URI: [namo:exposure_end_age](https://w3id.org/monarch-initiative/namo/exposure_end_age)
Alias: exposure_end_age


## Inheritance

* [node_property](node_property.md)
    * **exposure_end_age**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExposureEvent](ExposureEvent.md) | A (possibly time bounded) incidence of a feature of the environment of an org... |  no  |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | A genomic background exposure is where an individual's specific genomic backg... |  no  |
| [PathologicalProcessExposure](PathologicalProcessExposure.md) | A pathological process, when viewed as an exposure, representing a preconditi... |  no  |
| [PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) | An abnormal anatomical structure, when viewed as an exposure, represented as ... |  no  |
| [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | A disease or phenotypic feature state, when viewed as an exposure, represente... |  no  |
| [ChemicalExposure](ChemicalExposure.md) | A chemical exposure is an intake of a particular chemical entity |  no  |
| [ComplexChemicalExposure](ComplexChemicalExposure.md) | A complex chemical exposure is an intake of a chemical mixture, other than a ... |  no  |
| [DrugExposure](DrugExposure.md) | A drug exposure is an intake of a particular drug |  no  |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | drug to gene interaction exposure is a drug exposure is where the interaction... |  no  |
| [Treatment](Treatment.md) | A treatment is targeted at a disease or phenotype and may involve multiple dr... |  no  |
| [BioticExposure](BioticExposure.md) | An external biotic exposure is an intake of (sometimes pathological) biologic... |  no  |
| [GeographicExposure](GeographicExposure.md) | A geographic exposure is a factor relating to geographic proximity to some im... |  no  |
| [EnvironmentalExposure](EnvironmentalExposure.md) | A environmental exposure is a factor relating to abiotic processes in the env... |  no  |
| [BehavioralExposure](BehavioralExposure.md) | A behavioral exposure is a factor relating to behavior impacting an individua... |  no  |
| [SocioeconomicExposure](SocioeconomicExposure.md) | A socioeconomic exposure is a factor relating to social and financial status ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain | [ExposureEvent](ExposureEvent.md) |
| Domain Of | [ExposureEvent](ExposureEvent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:exposure_end_age |
| native | namo:exposure_end_age |




## LinkML Source

<details>
```yaml
name: exposure end age
description: Ending stage of an exposure event.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: exposure event
alias: exposure_end_age
domain_of:
- exposure event
range: integer

```
</details></div>