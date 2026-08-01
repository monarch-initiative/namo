---
search:
  boost: 5.0
---

# Slot: has_numeric_value 


_The numeric portion of the quantity._



<div data-search-exclude markdown="1">



URI: [biolink:has_numeric_value](https://w3id.org/biolink/has_numeric_value)
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
| Domain Of | [QuantityValue](QuantityValue.md) |
| Slot URI | [biolink:has_numeric_value](https://w3id.org/biolink/has_numeric_value) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [QuantityValue](QuantityValue.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biolink:has_numeric_value |
| native | namo:has_numeric_value |




## LinkML Source

<details>
```yaml
name: has_numeric_value
description: The numeric portion of the quantity.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
slot_uri: biolink:has_numeric_value
owner: QuantityValue
domain_of:
- QuantityValue
range: double

```
</details></div>