---
search:
  boost: 5.0
---

# Slot: specialization_qualifier 


_A qualifier that composes with a core subject/object concept to define a more specific version of the subject concept, specifically using an ontology term that is not a subclass or descendant of the core concept and in the vast majority of cases, is of a different ontological namespace than the category or namespace of the subject identifier._



<div data-search-exclude markdown="1">


* __NOTE__: this is an abstract slot and should not be populated directly


URI: [namo:specialization_qualifier](https://w3id.org/monarch-initiative/namo/specialization_qualifier)
Alias: specialization_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **specialization_qualifier**
            * [subject_specialization_qualifier](subject_specialization_qualifier.md)
            * [object_specialization_qualifier](object_specialization_qualifier.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Association](Association.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| CHEBI:5118 |
| GO:0005634 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:specialization_qualifier |
| native | namo:specialization_qualifier |




## LinkML Source

<details>
```yaml
name: specialization qualifier
description: A qualifier that composes with a core subject/object concept to define
  a more specific version of the subject concept, specifically using an ontology term
  that is not a subclass or descendant of the core concept and in the vast majority
  of cases, is of a different ontological namespace than the category or namespace
  of the subject identifier.
examples:
- value: CHEBI:5118
  description: fluoxetine. In a MAXO annotation this would be a specialization in
    treatment of a disease. For example, fluoxetine would be a specialization of the
    MAXO term 'serotonin-norepinephrine reuptake inhibitor agent therapy' as a treatment
    for the HP term 'Fatigable muscle weakness' in the context of the MONDO term 'congenital
    myasthenic syndrome '4A.'
- value: GO:0005634
  description: nucleus. In an expression annotation this would be a specialization
    in location of an anatomical entity. For example, "expression in the nucleus of
    hepatic cells" would be a specialization of "expression in hepatic cells"
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: qualifier
abstract: true
domain: association
alias: specialization_qualifier
range: string

```
</details></div>