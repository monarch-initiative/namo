---
search:
  boost: 5.0
---

# Slot: has_numeric_value 


_connects a quantity value to a number_



<div data-search-exclude markdown="1">



URI: [namo:has_numeric_value](https://w3id.org/monarch-initiative/namo/has_numeric_value)
Alias: has_numeric_value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantityValue](QuantityValue.md) | A value of an attribute that is quantitative and measurable, expressed as a c... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
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
| self | namo:has_numeric_value |
| native | namo:has_numeric_value |
| exact | qud:quantityValue |




## LinkML Source

<details>
```yaml
name: has numeric value
description: connects a quantity value to a number
in_subset:
- samples
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- qud:quantityValue
rank: 1000
domain: quantity value
alias: has_numeric_value
domain_of:
- quantity value
range: double
multivalued: false

```
</details></div>