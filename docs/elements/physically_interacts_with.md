---
search:
  boost: 5.0
---

# Slot: physically_interacts_with 


_holds between two entities that make physical contact as part of some interaction. does not imply a causal relationship._



<div data-search-exclude markdown="1">



URI: [namo:physically_interacts_with](https://w3id.org/monarch-initiative/namo/physically_interacts_with)
Alias: physically_interacts_with


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [interacts_with](interacts_with.md)
            * **physically_interacts_with** [ [interacts_with](interacts_with.md)]
                * [directly_physically_interacts_with](directly_physically_interacts_with.md)
                * [indirectly_physically_interacts_with](indirectly_physically_interacts_with.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NamedThing](NamedThing.md) |
| Domain | [NamedThing](NamedThing.md) |

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
| self | namo:physically_interacts_with |
| native | namo:physically_interacts_with |
| narrow | DRUGBANK:drug-interaction, FMA:adheres_to, NCIT:A7, PR:non-covalently_bound_to |
| broad | WIKIDATA_PROPERTY:P129 |




## LinkML Source

<details>
```yaml
name: physically interacts with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two entities that make physical contact as part of some
  interaction. does not imply a causal relationship.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
narrow_mappings:
- DRUGBANK:drug-interaction
- FMA:adheres_to
- NCIT:A7
- PR:non-covalently_bound_to
broad_mappings:
- WIKIDATA_PROPERTY:P129
rank: 1000
is_a: interacts with
mixins:
- interacts with
domain: named thing
inherited: true
alias: physically_interacts_with
symmetric: true
range: named thing
multivalued: true

```
</details></div>