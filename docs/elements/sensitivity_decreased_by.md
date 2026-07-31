---
search:
  boost: 5.0
---

# Slot: sensitivity_decreased_by 

<div data-search-exclude markdown="1">



URI: [namo:sensitivity_decreased_by](https://w3id.org/monarch-initiative/namo/sensitivity_decreased_by)
Alias: sensitivity_decreased_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [sensitivity_affected_by](sensitivity_affected_by.md)
            * **sensitivity_decreased_by**








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


<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Inverse | [decreases_sensitivity_to](decreases_sensitivity_to.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:sensitivity_decreased_by |
| native | namo:sensitivity_decreased_by |




## LinkML Source

<details>
```yaml
name: sensitivity decreased by
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: sensitivity affected by
domain: chemical entity or gene or gene product
inherited: true
alias: sensitivity_decreased_by
inverse: decreases sensitivity to
range: chemical entity or gene or gene product
multivalued: true

```
</details></div>