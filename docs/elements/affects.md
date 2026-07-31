---
search:
  boost: 5.0
---

# Slot: affects 


_Describes an entity that has an effect on the state or quality of another existing entity._



<div data-search-exclude markdown="1">



URI: [namo:affects](https://w3id.org/monarch-initiative/namo/affects)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **affects**
            * [regulates](regulates.md) [ [interacts_with](interacts_with.md)]
            * [disrupts](disrupts.md)
            * [ameliorates_condition](ameliorates_condition.md) [ [treats](treats.md)]
            * [exacerbates_condition](exacerbates_condition.md) [ [promotes_condition](promotes_condition.md)]
            * [has_adverse_event](has_adverse_event.md)
            * [has_side_effect](has_side_effect.md)








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




## Notes

* Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects likelihood of' and 'prevents' where the effect concerns whether or when something may or may not come into existence.



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
| self | namo:affects |
| native | namo:affects |
| exact | SEMMEDDB:AFFECTS, DGIdb:affects |
| narrow | CTD:prediction_hypothesis, GOREL:0001006, CTD:inferred, UPHENO:0000001, RO:0002263, RO:0002264, NCIT:R158, NCIT:R160, NCIT:R30, NCIT:R150, NCIT:R72, NCIT:R146, NCIT:R124, NCIT:R173, NCIT:R100, NCIT:R102, NCIT:R101, NCIT:R113, NCIT:R23, NCIT:R25, NCIT:gene_mapped_to_disease, NCIT:R133, RO:0002343, RO:0002355, RO:0002591, RO:0002592, RO:0012003, SNOMED:has_pathological_process, UBERGRAPH:is_increase_of, UBERGRAPH:is_decrease_of |
| related | DRUGBANK:pathway |




## LinkML Source

<details>
```yaml
name: affects
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Describes an entity that has an effect on the state or quality of another
  existing entity.
notes:
- Use of the 'affects' predicate implies that the affected entity already exists,
  unlike predicates such as 'affects likelihood of' and 'prevents' where the effect
  concerns whether or when something may or may not come into existence.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- SEMMEDDB:AFFECTS
- DGIdb:affects
related_mappings:
- DRUGBANK:pathway
narrow_mappings:
- CTD:prediction_hypothesis
- GOREL:0001006
- CTD:inferred
- UPHENO:0000001
- RO:0002263
- RO:0002264
- NCIT:R158
- NCIT:R160
- NCIT:R30
- NCIT:R150
- NCIT:R72
- NCIT:R146
- NCIT:R124
- NCIT:R173
- NCIT:R100
- NCIT:R102
- NCIT:R101
- NCIT:R113
- NCIT:R23
- NCIT:R25
- NCIT:gene_mapped_to_disease
- NCIT:R133
- RO:0002343
- RO:0002355
- RO:0002591
- RO:0002592
- RO:0012003
- SNOMED:has_pathological_process
- UBERGRAPH:is_increase_of
- UBERGRAPH:is_decrease_of
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
range: named thing
multivalued: true

```
</details></div>