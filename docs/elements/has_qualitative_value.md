---
search:
  boost: 5.0
---

# Slot: has_qualitative_value 


_connects an attribute to a value_



<div data-search-exclude markdown="1">



URI: [namo:has_qualitative_value](https://w3id.org/monarch-initiative/namo/has_qualitative_value)
Alias: has_qualitative_value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Attribute](Attribute.md) | A property or characteristic of an entity |  no  |
| [ChemicalRole](ChemicalRole.md) | A role played by the molecular entity or part thereof within a chemical conte... |  no  |
| [BiologicalSex](BiologicalSex.md) | An organismal quality inhering in a bearer by virtue of the bearer's ability ... |  no  |
| [PhenotypicSex](PhenotypicSex.md) | An attribute corresponding to the phenotypic sex of the individual, based upo... |  no  |
| [GenotypicSex](GenotypicSex.md) | An attribute corresponding to the genotypic sex of the individual, based upon... |  no  |
| [SeverityValue](SeverityValue.md) | describes the severity of a phenotypic feature or disease |  no  |
| [OrganismAttribute](OrganismAttribute.md) | describes a characteristic of an organismal entity |  no  |
| [PhenotypicQuality](PhenotypicQuality.md) | A characteristic of a phenotype (e |  no  |
| [Zygosity](Zygosity.md) | An allelic state describing the degree of similarity between features at a si... |  no  |
| [ClinicalAttribute](ClinicalAttribute.md) | Attributes relating to a clinical manifestation |  no  |
| [ClinicalMeasurement](ClinicalMeasurement.md) | A clinical measurement is a special kind of attribute which results from a la... |  no  |
| [ClinicalModifier](ClinicalModifier.md) | Used to characterize and specify the phenotypic abnormalities defined in the ... |  no  |
| [ClinicalCourse](ClinicalCourse.md) | The course a disease typically takes from its onset, progression in time, and... |  no  |
| [Onset](Onset.md) | The age group in which (disease) symptom manifestations appear |  no  |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | Attributes relating to a socioeconomic manifestation |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NamedThing](NamedThing.md) |
| Domain | [Attribute](Attribute.md) |
| Domain Of | [Attribute](Attribute.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |






## In Subsets


* [Samples](Samples.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_qualitative_value |
| native | namo:has_qualitative_value |




## LinkML Source

<details>
```yaml
name: has qualitative value
description: connects an attribute to a value
in_subset:
- samples
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
domain: attribute
alias: has_qualitative_value
domain_of:
- attribute
range: named thing
multivalued: false

```
</details></div>