---
search:
  boost: 5.0
---

# Slot: has_attribute_type 


_connects an attribute to a class that describes it_



<div data-search-exclude markdown="1">



URI: [namo:has_attribute_type](https://w3id.org/monarch-initiative/namo/has_attribute_type)
Alias: has_attribute_type

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
| [ClinicalMeasurement](ClinicalMeasurement.md) | A clinical measurement is a special kind of attribute which results from a la... |  yes  |
| [ClinicalModifier](ClinicalModifier.md) | Used to characterize and specify the phenotypic abnormalities defined in the ... |  no  |
| [ClinicalCourse](ClinicalCourse.md) | The course a disease typically takes from its onset, progression in time, and... |  no  |
| [Onset](Onset.md) | The age group in which (disease) symptom manifestations appear |  no  |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | Attributes relating to a socioeconomic manifestation |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OntologyClass](OntologyClass.md) |
| Domain | [Attribute](Attribute.md) |
| Domain Of | [Attribute](Attribute.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |






## In Subsets


* [Samples](Samples.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_attribute_type |
| native | namo:has_attribute_type |
| narrow | LOINC:has_modality_type, LOINC:has_view_type |




## LinkML Source

<details>
```yaml
name: has attribute type
description: connects an attribute to a class that describes it
in_subset:
- samples
from_schema: https://w3id.org/monarch-initiative/namo
narrow_mappings:
- LOINC:has_modality_type
- LOINC:has_view_type
rank: 1000
domain: attribute
alias: has_attribute_type
domain_of:
- attribute
range: ontology class
required: true
multivalued: false

```
</details></div>