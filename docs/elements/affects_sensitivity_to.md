---
search:
  boost: 5.0
---

# Slot: affects_sensitivity_to 


_holds between two chemical entities or genes or gene products where the action of one affects the susceptibility/sensitivity of a biological entity or system to the other._



<div data-search-exclude markdown="1">



URI: [namo:affects_sensitivity_to](https://w3id.org/monarch-initiative/namo/affects_sensitivity_to)
Alias: affects_sensitivity_to


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **affects_sensitivity_to**
            * [increases_sensitivity_to](increases_sensitivity_to.md)
            * [decreases_sensitivity_to](decreases_sensitivity_to.md)








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




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:affects_sensitivity_to |
| native | namo:affects_sensitivity_to |
| exact | CTD:affects_response_to |




## LinkML Source

<details>
```yaml
name: affects sensitivity to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two chemical entities or genes or gene products where the
  action of one affects the susceptibility/sensitivity of a biological entity or system
  to the other.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- CTD:affects_response_to
rank: 1000
is_a: related to at instance level
domain: chemical entity or gene or gene product
inherited: true
alias: affects_sensitivity_to
range: chemical entity or gene or gene product
multivalued: true

```
</details></div>