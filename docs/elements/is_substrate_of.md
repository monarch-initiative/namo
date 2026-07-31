---
search:
  boost: 5.0
---

# Slot: is_substrate_of 

<div data-search-exclude markdown="1">



URI: [namo:is_substrate_of](https://w3id.org/monarch-initiative/namo/is_substrate_of)
Alias: is_substrate_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [participates_in](participates_in.md)
            * **is_substrate_of**








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
| Inverse | [has_substrate](has_substrate.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:is_substrate_of |
| native | namo:is_substrate_of |




## LinkML Source

<details>
```yaml
name: is substrate of
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: participates in
domain: chemical entity or gene or gene product
inherited: true
alias: is_substrate_of
inverse: has substrate
range: chemical entity or gene or gene product
multivalued: true

```
</details></div>