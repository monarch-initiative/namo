---
search:
  boost: 5.0
---

# Slot: preceded_by 


_holds between two processes, where the other is completed before the one begins_



<div data-search-exclude markdown="1">



URI: [namo:preceded_by](https://w3id.org/monarch-initiative/namo/preceded_by)
Alias: preceded_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [temporally_related_to](temporally_related_to.md)
            * **preceded_by**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Occurrent](Occurrent.md) |
| Domain | [Occurrent](Occurrent.md) |

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
| Inverse | [precedes](precedes.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:preceded_by |
| native | namo:preceded_by |
| exact | BFO:0000062 |
| narrow | FMA:transforms_from, RO:0002087, RO:0002285 |
| broad | GENEPIO:0001739 |




## LinkML Source

<details>
```yaml
name: preceded by
description: holds between two processes, where the other is completed before the
  one begins
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- BFO:0000062
narrow_mappings:
- FMA:transforms_from
- RO:0002087
- RO:0002285
broad_mappings:
- GENEPIO:0001739
rank: 1000
is_a: temporally related to
domain: occurrent
inherited: true
alias: preceded_by
inverse: precedes
range: occurrent
multivalued: true

```
</details></div>