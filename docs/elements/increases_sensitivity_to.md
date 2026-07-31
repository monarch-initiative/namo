---
search:
  boost: 5.0
---

# Slot: increases_sensitivity_to 


_holds between two chemical entities or genes or gene products where the action or effect of one increases the susceptibility/sensitivity of a biological entity or system to the other_



<div data-search-exclude markdown="1">



URI: [namo:increases_sensitivity_to](https://w3id.org/monarch-initiative/namo/increases_sensitivity_to)
Alias: increases_sensitivity_to


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects_sensitivity_to](affects_sensitivity_to.md)
            * **increases_sensitivity_to**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) |
| Domain | [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |








## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |
| opposite_of | decreases sensitivity to |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:increases_sensitivity_to |
| native | namo:increases_sensitivity_to |
| exact | CTD:increases_response_to |




## LinkML Source

<details>
```yaml
name: increases sensitivity to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  opposite_of:
    tag: opposite_of
    value: decreases sensitivity to
description: holds between two chemical entities or genes or gene products where the
  action or effect of one increases the susceptibility/sensitivity of a biological
  entity or system to the other
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- CTD:increases_response_to
rank: 1000
is_a: affects sensitivity to
domain: chemical entity or gene or gene product
inherited: true
alias: increases_sensitivity_to
range: chemical entity or gene or gene product
multivalued: true

```
</details></div>