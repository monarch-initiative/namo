---
search:
  boost: 5.0
---

# Slot: aspect_qualifier 


_Composes with the core concept to describe new concepts of a different ontological type. e.g. a process in which the core concept participates, a function/activity/role held by the core concept, or a characteristic/quality that inheres in the core concept.  The purpose of the aspect slot is to indicate what aspect is being affected in an 'affects' association._



<div data-search-exclude markdown="1">


* __NOTE__: this is an abstract slot and should not be populated directly


URI: [namo:aspect_qualifier](https://w3id.org/monarch-initiative/namo/aspect_qualifier)
Alias: aspect_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **aspect_qualifier**
            * [subject_aspect_qualifier](subject_aspect_qualifier.md)
            * [object_aspect_qualifier](object_aspect_qualifier.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeneOrGeneProductOrChemicalEntityAspectEnum](GeneOrGeneProductOrChemicalEntityAspectEnum.md) |
| Domain | [Association](Association.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |






## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)





## Examples

| Value |
| --- |
| stability |
| abundance |
| expression |
| exposure |

## Notes

* for good examples of aspects in the gene-> chemical space, please see the GeneOrGeneProductOrChemicalEntityAspectEnum (below) which lists many aspects that can be used to qualify the gene making the full subject a different ontological type. the qualifier ‘expression’ combines with a core concept of ‘Gene X’ to express the composed concept ‘expression of Gene X’ (Gene → Biological Process) the qualifier ‘exposure’ combines with a core concept of ‘Chemical X’ to express the composed concept ‘exposure to Chemical X’ (Chemical → Exposure Process) the qualifier ‘activity’ combines with a core concept of ‘PPARG’ to express the concept ‘activity of PPARG’ (Gene → function/activity) the qualifier ‘emergency Department Visit’ combines with a core concept of ‘Disease X’ to express the concept ‘Emergency Department visits for Disease X’ (Disease → Clinical Event) the qualifier ‘infection’ combines with a core concept of ‘Giardia’ to express the concept ‘Infection with Giardia’ (Taxon → Biological / Pathological Process) the qualifier ‘severity’ combines with a core concept of ‘DILI’ to express the concept ‘the severity level of DILI’ (Disease → (intrinsic) Characteristic/Quality) the qualifier ‘abundance’ combines with a core concept of ‘BRCA2’ to express the concept ‘abundance of BRCA2’ (Gene → (extrinsic) characteristic/quality)



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:aspect_qualifier |
| native | namo:aspect_qualifier |




## LinkML Source

<details>
```yaml
name: aspect qualifier
description: Composes with the core concept to describe new concepts of a different
  ontological type. e.g. a process in which the core concept participates, a function/activity/role
  held by the core concept, or a characteristic/quality that inheres in the core concept.  The
  purpose of the aspect slot is to indicate what aspect is being affected in an 'affects'
  association.
notes:
- for good examples of aspects in the gene-> chemical space, please see the GeneOrGeneProductOrChemicalEntityAspectEnum
  (below) which lists many aspects that can be used to qualify the gene making the
  full subject a different ontological type. the qualifier ‘expression’ combines with
  a core concept of ‘Gene X’ to express the composed concept ‘expression of Gene X’
  (Gene → Biological Process) the qualifier ‘exposure’ combines with a core concept
  of ‘Chemical X’ to express the composed concept ‘exposure to Chemical X’ (Chemical
  → Exposure Process) the qualifier ‘activity’ combines with a core concept of ‘PPARG’
  to express the concept ‘activity of PPARG’ (Gene → function/activity) the qualifier
  ‘emergency Department Visit’ combines with a core concept of ‘Disease X’ to express
  the concept ‘Emergency Department visits for Disease X’ (Disease → Clinical Event)
  the qualifier ‘infection’ combines with a core concept of ‘Giardia’ to express the
  concept ‘Infection with Giardia’ (Taxon → Biological / Pathological Process) the
  qualifier ‘severity’ combines with a core concept of ‘DILI’ to express the concept
  ‘the severity level of DILI’ (Disease → (intrinsic) Characteristic/Quality) the
  qualifier ‘abundance’ combines with a core concept of ‘BRCA2’ to express the concept
  ‘abundance of BRCA2’ (Gene → (extrinsic) characteristic/quality)
examples:
- value: stability
- value: abundance
- value: expression
- value: exposure
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: qualifier
abstract: true
domain: association
alias: aspect_qualifier
range: GeneOrGeneProductOrChemicalEntityAspectEnum

```
</details></div>