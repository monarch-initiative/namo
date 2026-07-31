---
search:
  boost: 5.0
---

# Slot: derives_from 


_holds between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity_



<div data-search-exclude markdown="1">



URI: [namo:derives_from](https://w3id.org/monarch-initiative/namo/derives_from)
Alias: derives_from


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **derives_from**
            * [is_metabolite_of](is_metabolite_of.md)








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








## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)
* [Samples](Samples.md)






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
| self | namo:derives_from |
| native | namo:derives_from |
| exact | RO:0001000, FMA:derives_from, DOID-PROPERTY:derives_from |
| narrow | CHEBI:has_functional_parent, SNOMED:has_specimen_source_topography |




## LinkML Source

<details>
```yaml
name: derives from
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two distinct material entities, the new entity and the
  old entity, in which the new entity begins to exist when the old entity ceases to
  exist, and the new entity inherits the significant portion of the matter of the
  old entity
in_subset:
- translator_minimal
- samples
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0001000
- FMA:derives_from
- DOID-PROPERTY:derives_from
narrow_mappings:
- CHEBI:has_functional_parent
- SNOMED:has_specimen_source_topography
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: derives_from
range: named thing
multivalued: true

```
</details></div>