---
search:
  boost: 5.0
---

# Slot: pharmacologically_interacts_with 


_holds between two pharmacologically active chemicals (typically drugs), where one alters the availability, efficacy, or toxicity of the other in the body when taken simultaneously - typically by altering how the body processes the chemical (pharmacokinetics) or how the chemical acts on the body (pharmacodynamics)._



<div data-search-exclude markdown="1">



URI: [namo:pharmacologically_interacts_with](https://w3id.org/monarch-initiative/namo/pharmacologically_interacts_with)
Alias: pharmacologically_interacts_with


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [interacts_with](interacts_with.md)
            * **pharmacologically_interacts_with**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChemicalEntity](ChemicalEntity.md) |
| Domain | [ChemicalEntity](ChemicalEntity.md) |

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
| Symmetric | Yes |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)



## Aliases


* drug drug interaction




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
| self | namo:pharmacologically_interacts_with |
| native | namo:pharmacologically_interacts_with |




## LinkML Source

<details>
```yaml
name: pharmacologically interacts with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two pharmacologically active chemicals (typically drugs),
  where one alters the availability, efficacy, or toxicity of the other in the body
  when taken simultaneously - typically by altering how the body processes the chemical
  (pharmacokinetics) or how the chemical acts on the body (pharmacodynamics).
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- drug drug interaction
rank: 1000
is_a: interacts with
domain: chemical entity
inherited: true
alias: pharmacologically_interacts_with
symmetric: true
range: chemical entity
multivalued: true

```
</details></div>