---
search:
  boost: 5.0
---

# Slot: has_unit 


_connects a quantity value to a unit_



<div data-search-exclude markdown="1">



URI: [namo:has_unit](https://w3id.org/monarch-initiative/namo/has_unit)
Alias: has_unit

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantityValue](QuantityValue.md) | A value of an attribute that is quantitative and measurable, expressed as a c... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Unit](Unit.md) |
| Domain | [QuantityValue](QuantityValue.md) |
| Domain Of | [QuantityValue](QuantityValue.md) |

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
| self | namo:has_unit |
| native | namo:has_unit |
| exact | qud:unit, IAO:0000039 |
| narrow | SNOMED:has_concentration_strength_denominator_unit, SNOMED:has_concentration_strength_numerator_unit, SNOMED:has_presentation_strength_denominator_unit, SNOMED:has_presentation_strength_numerator_unit, SNOMED:has_unit_of_presentation |
| close | EFO:0001697, UO-PROPERTY:is_unit_of |




## LinkML Source

<details>
```yaml
name: has unit
description: connects a quantity value to a unit
in_subset:
- samples
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- qud:unit
- IAO:0000039
close_mappings:
- EFO:0001697
- UO-PROPERTY:is_unit_of
narrow_mappings:
- SNOMED:has_concentration_strength_denominator_unit
- SNOMED:has_concentration_strength_numerator_unit
- SNOMED:has_presentation_strength_denominator_unit
- SNOMED:has_presentation_strength_numerator_unit
- SNOMED:has_unit_of_presentation
rank: 1000
domain: quantity value
alias: has_unit
domain_of:
- quantity value
range: unit
multivalued: false

```
</details></div>