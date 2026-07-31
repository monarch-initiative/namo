---
search:
  boost: 5.0
---

# Slot: chemically_similar_to 


_holds between one small molecule entity and another that it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity._



<div data-search-exclude markdown="1">



URI: [namo:chemically_similar_to](https://w3id.org/monarch-initiative/namo/chemically_similar_to)
Alias: chemically_similar_to


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [similar_to](similar_to.md)
            * **chemically_similar_to**








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
| self | namo:chemically_similar_to |
| native | namo:chemically_similar_to |
| narrow | CHEBI:has_parent_hydride, CHEBI:has_functional_parent, CHEBI:is_conjugate_acid_of, CHEBI:is_conjugate_base_of, CHEBI:is_enantiomer_of, CHEBI:is_tautomer_of, NCIT:has_salt_form |




## LinkML Source

<details>
```yaml
name: chemically similar to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between one small molecule entity and another that it approximates
  for purposes of scientific study, in virtue of its exhibiting similar features of
  the studied entity.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
narrow_mappings:
- CHEBI:has_parent_hydride
- CHEBI:has_functional_parent
- CHEBI:is_conjugate_acid_of
- CHEBI:is_conjugate_base_of
- CHEBI:is_enantiomer_of
- CHEBI:is_tautomer_of
- NCIT:has_salt_form
rank: 1000
is_a: similar to
domain: named thing
inherited: true
alias: chemically_similar_to
symmetric: true
range: named thing
multivalued: true

```
</details></div>