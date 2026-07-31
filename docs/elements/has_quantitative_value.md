---
search:
  boost: 5.0
---

# Slot: has_quantitative_value 


_connects an attribute to a value_



<div data-search-exclude markdown="1">



URI: [namo:has_quantitative_value](https://w3id.org/monarch-initiative/namo/has_quantitative_value)
Alias: has_quantitative_value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Attribute](Attribute.md) | A property or characteristic of an entity |  no  |
| [ChemicalExposure](ChemicalExposure.md) | A chemical exposure is an intake of a particular chemical entity |  no  |
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
| [DrugExposure](DrugExposure.md) | A drug exposure is an intake of a particular drug |  no  |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | drug to gene interaction exposure is a drug exposure is where the interaction... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [QuantityValue](QuantityValue.md) |
| Domain | [Attribute](Attribute.md) |
| Domain Of | [Attribute](Attribute.md), [ChemicalExposure](ChemicalExposure.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |






## In Subsets


* [Samples](Samples.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_quantitative_value |
| native | namo:has_quantitative_value |
| exact | qud:quantityValue |
| narrow | SNOMED:has_concentration_strength_numerator_value, SNOMED:has_presentation_strength_denominator_value, SNOMED:has_presentation_strength_numerator_value |




## LinkML Source

<details>
```yaml
name: has quantitative value
description: connects an attribute to a value
in_subset:
- samples
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- qud:quantityValue
narrow_mappings:
- SNOMED:has_concentration_strength_numerator_value
- SNOMED:has_presentation_strength_denominator_value
- SNOMED:has_presentation_strength_numerator_value
rank: 1000
domain: attribute
alias: has_quantitative_value
domain_of:
- attribute
- chemical exposure
range: quantity value
multivalued: true

```
</details></div>